"""
CopilotAdapter — adapter for GitHub Copilot (VS Code extension).

GitHub Copilot is a VS Code extension that provides inline completions
and chat. The adapter drives it through the VS Code Extension Host API.

Approach:
- Launch: VS Code CLI with the Copilot extension installed
- Completion: VS Code Extension Host API (commands.executeCommand)
- Generation: Copilot Chat panel via extension API
- Auth: GitHub OAuth (handled by the extension)

Note: The VS Code extension API does not expose completions directly.
The adapter uses the "Trigger Inline Suggestion" command and captures
the ghost text via the editor's text model.
"""

import subprocess
import time
import os
from typing import List, Optional

from base import (
    CodeEditorAdapter,
    CompletionResponse,
    GenerationResponse,
    Edit,
    TestResult,
)


class CopilotAdapter(CodeEditorAdapter):
    """
    Adapter for GitHub Copilot — VS Code extension.
    
    Known issues / sharp edges:
    - Copilot switched to usage-based credits in June 2026 — cost predictability dropped
    - Completions can be slow on first use (cold start / model load)
    - The extension API for chat is not fully public; may require private APIs
    - Auth can drift silently (OAuth token expires)
    """
    
    def __init__(self, config: Optional[dict] = None):
        super().__init__(config)
        self.vscode_cli = self.config.get("vscode_cli", "code")
        self.extension_id = "GitHub.copilot"
        self._proc = None
    
    def setup(self) -> None:
        """
        Install VS Code and the Copilot extension, authenticate.
        
        Setup steps:
        1. Check if VS Code CLI is available
        2. Install the Copilot extension from the marketplace
        3. Verify GitHub authentication (OAuth flow)
        """
        start = time.monotonic()
        
        # Step 1: Check VS Code CLI
        try:
            subprocess.run(
                [self.vscode_cli, "--version"],
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError(
                "VS Code CLI not found. Please install VS Code."
            )
        
        # Step 2: Install Copilot extension
        result = subprocess.run(
            [self.vscode_cli, "--install-extension", self.extension_id],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 and "already installed" not in result.stdout:
            self.telemetry.ops_notes.append(
                f"Copilot extension install warning: {result.stderr}"
            )
        
        # Step 3: Verify auth
        auth_path = os.path.expanduser("~/.config/github-copilot/hosts.json")
        if not os.path.exists(auth_path):
            self.telemetry.ops_notes.append(
                "Copilot auth not found — user may need to log in via VS Code"
            )
        
        self.telemetry.setup_ms = (time.monotonic() - start) * 1000
    
    def open_workspace(self, workspace_path: str) -> None:
        """
        Open the workspace in VS Code and wait for Copilot to initialize.
        
        Steps:
        1. Launch VS Code with the workspace
        2. Wait for Copilot extension to activate
        3. Wait for language server to be ready
        """
        start = time.monotonic()
        super().open_workspace(workspace_path)
        
        self._proc = subprocess.Popen(
            [self.vscode_cli, workspace_path, "--wait"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        
        # Copilot needs a few seconds to activate and authenticate
        time.sleep(3)
        
        self.telemetry.open_workspace_ms = (time.monotonic() - start) * 1000
    
    def request_completion(
        self, file_path: str, cursor_line: int, cursor_col: int
    ) -> CompletionResponse:
        """
        Request inline completion via the VS Code Extension Host API.
        
        The adapter triggers the "editor.action.inlineSuggest.trigger" command
        and captures the ghost text. This requires either:
        - A VS Code extension that exposes an HTTP API for completions
        - A Playwright/Selenium-based UI automation
        - Or using the VS Code CLI with --command
        """
        start = time.monotonic()
        
        # Placeholder: actual implementation would use VS Code extension API
        # or UI automation to capture the ghost text
        # 
        # Option A: Use a custom VS Code extension that exposes an HTTP endpoint
        # Option B: Use Playwright to read the DOM of the VS Code webview
        # Option C: Use the VS Code CLI with --command (limited)
        
        latency = (time.monotonic() - start) * 1000
        
        return CompletionResponse(
            text="",
            latency_ms=latency,
            tokens=0,
            model="copilot",
        )
    
    def request_generation(
        self, prompt: str, context_files: List[str]
    ) -> GenerationResponse:
        """
        Send a chat command via Copilot Chat.
        
        The adapter sends the prompt to the Copilot Chat panel and waits
        for the response. Copilot Chat returns markdown with code blocks.
        """
        start = time.monotonic()
        
        # Placeholder: actual implementation would use the Copilot Chat API
        # or UI automation to send the prompt and read the response
        
        end = time.monotonic()
        latency = (end - start) * 1000
        
        return GenerationResponse(
            code="",
            raw="",
            latency_ms=latency,
            end_to_end_ms=latency,
            tokens=0,
            model="copilot",
        )
    
    def apply_edit(self, edit: Edit) -> bool:
        """Apply the edit to disk and verify syntax."""
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
        """Run tests in the workspace directory."""
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
        """Close VS Code and clean up."""
        start = time.monotonic()
        
        if self._proc:
            self._proc.terminate()
            try:
                self._proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._proc.kill()
        
        self.telemetry.teardown_ms = (time.monotonic() - start) * 1000
