"""
ClaudeCodeAdapter — adapter for Claude Code (CLI agent by Anthropic).

Claude Code is a terminal-based CLI agent. It runs as a subprocess and
is driven via stdin/stdout. The adapter spawns the `claude` process,
sends commands via stdin, and parses the output.

Approach:
- Launch: `claude` subprocess in the workspace directory
- Completion: Not applicable (Claude Code is chat/agent only, no inline completion)
- Generation: Send prompt via stdin; capture output via stdout
- Auth: API key (ANTHROPIC_API_KEY) or OAuth

Note: Claude Code may apply edits to files automatically. The adapter
must verify whether the edit was already applied or needs to be applied
manually.
"""

import subprocess
import time
import os
import re
from typing import List, Optional

from base import (
    CodeEditorAdapter,
    CompletionResponse,
    GenerationResponse,
    Edit,
    TestResult,
)


class ClaudeCodeAdapter(CodeEditorAdapter):
    """
    Adapter for Claude Code — terminal CLI agent by Anthropic.
    
    Known issues / sharp edges:
    - Claude Code has no inline completion — only chat/agent mode
    - It may apply edits automatically without explicit confirmation
    - The CLI is interactive; the adapter must handle prompts like "Proceed? [Y/n]"
    - Cost can be high ($2.5B ARR implies significant per-user spend)
    - 1M context window means large files are sent to the API — privacy concern
    """
    
    def __init__(self, config: Optional[dict] = None):
        super().__init__(config)
        self.claude_binary = self.config.get("claude_binary", "claude")
        self.model = self.config.get("model", "claude-sonnet-4")
        self._proc: Optional[subprocess.Popen] = None
    
    def setup(self) -> None:
        """
        Install Claude Code if not present, verify auth, and configure.
        
        Setup steps:
        1. Check if `claude` CLI is available
        2. Verify ANTHROPIC_API_KEY is set
        3. Configure the model (default: claude-sonnet-4)
        """
        start = time.monotonic()
        
        # Step 1: Check CLI availability
        try:
            subprocess.run(
                [self.claude_binary, "--version"],
                capture_output=True,
                check=True,
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError(
                "Claude Code CLI not found. Install with: npm install -g @anthropic/claude-code"
            )
        
        # Step 2: Verify API key
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            self.telemetry.ops_notes.append(
                "ANTHROPIC_API_KEY not set — Claude Code will not authenticate"
            )
        
        self.telemetry.setup_ms = (time.monotonic() - start) * 1000
    
    def open_workspace(self, workspace_path: str) -> None:
        """
        Open the workspace by starting Claude Code in the directory.
        
        Claude Code automatically indexes the workspace when started.
        The adapter waits for the prompt to appear before proceeding.
        """
        start = time.monotonic()
        super().open_workspace(workspace_path)
        
        # Start Claude Code as a subprocess in the workspace directory
        self._proc = subprocess.Popen(
            [self.claude_binary, "--model", self.model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=self.workspace,
        )
        
        # Wait for the initial prompt to appear (e.g., "Claude Code >")
        self._read_until_prompt()
        
        self.telemetry.open_workspace_ms = (time.monotonic() - start) * 1000
    
    def request_completion(
        self, file_path: str, cursor_line: int, cursor_col: int
    ) -> CompletionResponse:
        """
        Claude Code does not support inline completion.
        
        Returns an empty response with a note.
        """
        self.telemetry.ops_notes.append(
            "Claude Code has no inline completion capability — skipping"
        )
        return CompletionResponse(
            text="",
            latency_ms=0.0,
            tokens=0,
            model=self.model,
        )
    
    def request_generation(
        self, prompt: str, context_files: List[str]
    ) -> GenerationResponse:
        """
        Send a prompt to Claude Code and capture the response.
        
        The adapter sends the prompt via stdin, then reads the output
        until the prompt returns. Claude Code may:
        - Return a code block in markdown
        - Apply the edit automatically and return a summary
        - Ask for confirmation ("Proceed? [Y/n]")
        
        The adapter handles auto-confirmation if configured.
        """
        start = time.monotonic()
        
        if not self._proc or self._proc.stdin.closed:
            raise RuntimeError("Claude Code process is not running")
        
        # Build the prompt with context files
        full_prompt = prompt
        if context_files:
            full_prompt += f"\n\nContext files: {', '.join(context_files)}"
        
        # Send the prompt
        self._proc.stdin.write(f"{full_prompt}\n")
        self._proc.stdin.flush()
        
        # Read the response until the prompt returns
        raw_output = self._read_until_prompt()
        
        # Extract code from markdown
        code = self.extract_code_from_markdown(raw_output)
        
        end = time.monotonic()
        latency = (end - start) * 1000
        
        return GenerationResponse(
            code=code,
            raw=raw_output,
            latency_ms=latency,
            end_to_end_ms=latency,
            tokens=0,  # Would be estimated from output length
            model=self.model,
        )
    
    def apply_edit(self, edit: Edit) -> bool:
        """
        Apply the edit to disk.
        
        Claude Code may have already applied the edit automatically. The
        adapter checks the file content first; if it doesn't match, it
        applies the edit manually.
        """
        import os
        
        full_path = os.path.join(self.workspace, edit.file_path) if self.workspace else edit.file_path
        
        try:
            with open(full_path, "r") as f:
                content = f.read()
            
            # Check if Claude already applied the edit
            if edit.new_content in content:
                self.telemetry.ops_notes.append(
                    f"Claude Code already applied edit to {edit.file_path}"
                )
                return self._check_syntax(full_path)
            
            # Apply manually
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
        """
        Send /exit to Claude Code, wait for termination, clean up.
        """
        start = time.monotonic()
        
        if self._proc and not self._proc.stdin.closed:
            try:
                self._proc.stdin.write("/exit\n")
                self._proc.stdin.flush()
                self._proc.wait(timeout=5)
            except (subprocess.TimeoutExpired, BrokenPipeError):
                self._proc.kill()
        
        self.telemetry.teardown_ms = (time.monotonic() - start) * 1000
    
    def _read_until_prompt(self, timeout: float = 60.0) -> str:
        """
        Read stdout from Claude Code until the prompt appears.
        
        Claude Code's prompt looks like:
        "Claude Code > " or "? " (for confirmation questions)
        
        Args:
            timeout: Maximum seconds to wait for the prompt
        
        Returns:
            All output read before the prompt
        """
        if not self._proc:
            return ""
        
        output_lines = []
        start = time.monotonic()
        
        while time.monotonic() - start < timeout:
            line = self._proc.stdout.readline()
            if not line:
                break
            
            output_lines.append(line)
            
            # Detect prompt (customize based on actual Claude Code prompt)
            if line.strip().endswith(">") or line.strip().endswith("?"):
                break
        
        return "".join(output_lines)
