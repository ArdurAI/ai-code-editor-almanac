"""
CursorAdapter — adapter for Cursor (VS Code fork, AI-native IDE).

Cursor is a VS Code fork with deep AI integration. It runs as a standalone
application with its own binary. The adapter launches Cursor via the CLI
and drives it through the VS Code Extension Host API and internal HTTP
endpoints.

Approach:
- Launch: cursor CLI (macOS: /Applications/Cursor.app/Contents/MacOS/Cursor)
- Completion: Internal HTTP API on port 3000 (or VS Code extension host)
- Generation: Chat panel via internal API or command palette
- Auth: OAuth or API key (stored in ~/.cursor/settings.json)

Note: Cursor does not expose a public API. The adapter uses the same
internal mechanisms that the Cursor extension uses: an HTTP server
running inside the VS Code extension host that accepts completion
and generation requests.
"""

import subprocess
import time
import os
import json
from typing import List, Optional

from base import (
    CodeEditorAdapter,
    CompletionResponse,
    GenerationResponse,
    Edit,
    TestResult,
)


class CursorAdapter(CodeEditorAdapter):
    """
    Adapter for Cursor — AI-native IDE (VS Code fork).
    
    Known issues / sharp edges:
    - Cursor's internal API port can change; the adapter must discover it
    - Heavy users report $40-50/mo on a $20 plan (cost-runaway risk)
    - Indexing can be slow on large monorepos (30+ seconds)
    - Auth token can expire silently after 1 hour
    """
    
    def __init__(self, config: Optional[dict] = None):
        super().__init__(config)
        self.cursor_cli = self.config.get("cursor_cli", "cursor")
        self.api_port = self.config.get("api_port", None)  # Auto-discover if None
        self._proc = None
    
    def setup(self) -> None:
        """
        Install Cursor if not present, authenticate, and verify the CLI.
        
        Setup steps:
        1. Check if cursor CLI is available
        2. If not, download and install (macOS: .dmg, Linux: .AppImage, Windows: .exe)
        3. Authenticate via OAuth or API key
        4. Verify the internal API server is reachable
        """
        start = time.monotonic()
        
        # Step 1: Check CLI availability
        try:
            subprocess.run(
                [self.cursor_cli, "--version"],
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError(
                "Cursor CLI not found. Please install Cursor from https://cursor.com"
            )
        
        # Step 2: Verify auth (check for token in settings)
        settings_path = os.path.expanduser("~/.cursor/settings.json")
        if not os.path.exists(settings_path):
            self.telemetry.ops_notes.append(
                "Cursor settings not found — user may need to log in manually"
            )
        
        # Step 3: Discover internal API port (if not configured)
        if self.api_port is None:
            self.api_port = self._discover_api_port()
        
        self.telemetry.setup_ms = (time.monotonic() - start) * 1000
    
    def open_workspace(self, workspace_path: str) -> None:
        """
        Open the workspace in Cursor and wait for indexing + LSP readiness.
        
        Steps:
        1. Launch Cursor with the workspace path
        2. Wait for language server to initialize
        3. Wait for Cursor's internal indexing to complete
        4. Poll the API server until it responds to /health
        """
        start = time.monotonic()
        super().open_workspace(workspace_path)
        
        # Launch Cursor in the background
        self._proc = subprocess.Popen(
            [self.cursor_cli, workspace_path, "--wait"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        
        # Wait for indexing (poll /health or check process logs)
        # This is a placeholder — the actual implementation would parse
        # Cursor's logs or use the internal API to detect readiness
        time.sleep(5)  # Conservative wait for small workspaces
        
        self.telemetry.open_workspace_ms = (time.monotonic() - start) * 1000
    
    def request_completion(
        self, file_path: str, cursor_line: int, cursor_col: int
    ) -> CompletionResponse:
        """
        Request inline completion via Cursor's internal API.
        
        The adapter sends a POST to the internal HTTP server with the
        file path, line, and column. It measures the time from request
        to response.
        """
        start = time.monotonic()
        
        # Placeholder: actual implementation would POST to Cursor's API
        # response = requests.post(
        #     f"http://localhost:{self.api_port}/complete",
        #     json={"file": file_path, "line": cursor_line, "col": cursor_col},
        # )
        # text = response.json()["completion"]
        
        latency = (time.monotonic() - start) * 1000
        
        return CompletionResponse(
            text="",  # Would be populated from API response
            latency_ms=latency,
            tokens=0,  # Would be estimated from response
            model="cursor",
        )
    
    def request_generation(
        self, prompt: str, context_files: List[str]
    ) -> GenerationResponse:
        """
        Send a chat command via Cursor's internal API.
        
        The adapter sends the prompt to the chat panel and waits for the
        full response. It extracts the code block from the markdown output.
        """
        start = time.monotonic()
        
        # Placeholder: actual implementation would POST to Cursor's API
        # response = requests.post(
        #     f"http://localhost:{self.api_port}/generate",
        #     json={"prompt": prompt, "context": context_files},
        # )
        # raw = response.json()["text"]
        # code = self.extract_code_from_markdown(raw)
        
        end = time.monotonic()
        latency = (end - start) * 1000
        
        return GenerationResponse(
            code="",  # Would be populated from API response
            raw="",  # Would be populated from API response
            latency_ms=latency,
            end_to_end_ms=latency,
            tokens=0,
            model="cursor",
        )
    
    def apply_edit(self, edit: Edit) -> bool:
        """
        Apply the edit to disk and verify syntax.
        """
        import os
        
        full_path = os.path.join(self.workspace, edit.file_path) if self.workspace else edit.file_path
        
        try:
            with open(full_path, "r") as f:
                content = f.read()
            
            new_content = content.replace(edit.old_content, edit.new_content, 1)
            
            with open(full_path, "w") as f:
                f.write(new_content)
            
            return self._check_syntax(full_path)
        except Exception as e:
            self.telemetry.errors.append(f"apply_edit failed: {e}")
            return False
    
    def run_tests(self, test_command: str) -> TestResult:
        """
        Run tests in the workspace directory.
        """
        start = time.monotonic()
        
        result = subprocess.run(
            test_command,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )
        
        duration = (time.monotonic() - start) * 1000
        
        return TestResult(
            passed=result.returncode == 0,
            stdout=result.stdout,
            stderr=result.stderr,
            returncode=result.returncode,
            duration_ms=duration,
        )
    
    def teardown(self) -> None:
        """
        Close Cursor, clean up temp files, and measure resource usage.
        """
        start = time.monotonic()
        
        if self._proc:
            self._proc.terminate()
            try:
                self._proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._proc.kill()
        
        self.telemetry.teardown_ms = (time.monotonic() - start) * 1000
    
    def _discover_api_port(self) -> int:
        """
        Discover the port on which Cursor's internal API server is running.
        
        Cursor opens an HTTP server on a random port. The adapter scans
        open ports or reads Cursor's logs to find the correct one.
        """
        # Placeholder: actual implementation would scan netstat or read logs
        return 3000
