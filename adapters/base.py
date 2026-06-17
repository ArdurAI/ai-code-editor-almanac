"""
CodeEditorAdapter — frozen contract for all code editor benchmarks.

Every adapter in this directory inherits from CodeEditorAdapter and implements
the 7 lifecycle methods. The harness calls these methods identically for every
tool; the adapter is the only thing that changes per editor.

The contract is frozen before any tool runs. If an editor doesn't fit the
contract, we adapt the adapter — not the rules.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import time


@dataclass
class CompletionResponse:
    """Response from an inline completion request."""
    text: str = ""                    # The suggested completion text
    latency_ms: float = 0.0           # Keystroke → first character (ms)
    tokens: int = 0                   # Estimated tokens in the response
    model: str = "unknown"            # Which model produced the completion
    accepted: bool = False            # Whether the user accepted it
    

@dataclass
class GenerationResponse:
    """Response from a chat/agent generation request."""
    code: str = ""                    # The generated code (extracted from raw)
    explanation: str = ""            # The explanation text (if any)
    raw: str = ""                    # Full raw output from the tool
    latency_ms: float = 0.0           # Prompt sent → first token (ms)
    end_to_end_ms: float = 0.0       # Prompt sent → all edits applied (ms)
    tokens: int = 0                   # Estimated tokens in the response
    model: str = "unknown"            # Which model produced the generation
    

@dataclass
class Edit:
    """A single edit operation to apply to a file."""
    file_path: str
    old_content: str = ""            # Content to replace (empty = insert at start)
    new_content: str = ""            # Content to insert
    

@dataclass
class TestResult:
    """Result of running a test suite."""
    passed: bool = False
    stdout: str = ""
    stderr: str = ""
    returncode: int = 1
    duration_ms: float = 0.0
    

@dataclass
class Telemetry:
    """Telemetry collected during a benchmark run."""
    setup_ms: float = 0.0
    open_workspace_ms: float = 0.0
    completions: List[CompletionResponse] = field(default_factory=list)
    generations: List[GenerationResponse] = field(default_factory=list)
    edits_applied: int = 0
    edits_failed: int = 0
    tests_run: int = 0
    tests_passed: int = 0
    teardown_ms: float = 0.0
    peak_memory_mb: float = 0.0
    peak_cpu_percent: float = 0.0
    errors: List[str] = field(default_factory=list)
    ops_notes: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "setup_ms": self.setup_ms,
            "open_workspace_ms": self.open_workspace_ms,
            "completions": [
                {
                    "text": c.text,
                    "latency_ms": c.latency_ms,
                    "tokens": c.tokens,
                    "model": c.model,
                    "accepted": c.accepted,
                }
                for c in self.completions
            ],
            "generations": [
                {
                    "code": g.code,
                    "explanation": g.explanation,
                    "latency_ms": g.latency_ms,
                    "end_to_end_ms": g.end_to_end_ms,
                    "tokens": g.tokens,
                    "model": g.model,
                }
                for g in self.generations
            ],
            "edits_applied": self.edits_applied,
            "edits_failed": self.edits_failed,
            "tests_run": self.tests_run,
            "tests_passed": self.tests_passed,
            "teardown_ms": self.teardown_ms,
            "peak_memory_mb": self.peak_memory_mb,
            "peak_cpu_percent": self.peak_cpu_percent,
            "errors": self.errors,
            "ops_notes": self.ops_notes,
        }


class CodeEditorAdapter(ABC):
    """
    Abstract base class for all code editor adapters.
    
    Every adapter must implement all 7 lifecycle methods. The harness calls
    them in this order:
    
        setup() → open_workspace() → [request_completion | request_generation] →
        apply_edit() → run_tests() → teardown()
    
    The adapter is responsible for:
    - Installing and configuring the editor or extension
    - Opening the workspace and waiting for indexing / LSP readiness
    - Measuring latency around every operation
    - Capturing the generated code and metadata
    - Applying edits to disk and verifying correctness
    - Running tests and returning results
    - Cleaning up and measuring resource usage
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.telemetry = Telemetry()
        self.workspace: Optional[str] = None
    
    # ------------------------------------------------------------------
    # Lifecycle methods (must be implemented by every adapter)
    # ------------------------------------------------------------------
    
    @abstractmethod
    def setup(self) -> None:
        """
        Install, configure, and start the editor or extension.
        
        This is where the adapter installs the tool from the marketplace,
        VSIX, package manager, or binary. It also handles authentication
        (OAuth, API key, SSO) if required.
        
        Must set self.telemetry.setup_ms to the elapsed time.
        """
        pass
    
    @abstractmethod
    def open_workspace(self, workspace_path: str) -> None:
        """
        Open the project/workspace. Index files. Build AST/graph if applicable.
        
        This is the "await_ready" barrier. The adapter must wait until the
        editor has fully indexed the workspace, initialized the language server,
        and built any internal context graph before returning.
        
        Must set self.telemetry.open_workspace_ms to the elapsed time.
        """
        self.workspace = workspace_path
    
    @abstractmethod
    def request_completion(
        self, file_path: str, cursor_line: int, cursor_col: int
    ) -> CompletionResponse:
        """
        Request inline completion at the given cursor position.
        
        The adapter must simulate a keystroke or trigger the completion at the
        exact line/column, then capture the first suggestion and measure the
        latency from trigger to first character displayed.
        
        Args:
            file_path: Path to the file, relative to workspace root
            cursor_line: 0-based line number
            cursor_col: 0-based column number
        
        Returns:
            CompletionResponse with text, latency, tokens, and metadata
        """
        pass
    
    @abstractmethod
    def request_generation(
        self, prompt: str, context_files: List[str]
    ) -> GenerationResponse:
        """
        Send a chat/agent command. Return generated code and metadata.
        
        The adapter sends the prompt to the editor's chat/agent panel (or CLI)
        and waits for the full response. It then extracts the code block from
        the raw output and measures both TTFT and end-to-end latency.
        
        Args:
            prompt: The user prompt (e.g., "Implement this function")
            context_files: List of file paths to include as context
        
        Returns:
            GenerationResponse with code, explanation, latency, and metadata
        """
        pass
    
    @abstractmethod
    def apply_edit(self, edit: Edit) -> bool:
        """
        Apply the suggested edit to the file. Return success/failure.
        
        The adapter writes the edit to disk and optionally verifies syntax
        or compilation. It must not use the editor's built-in apply if that
        would bypass the benchmark's measurement of correctness.
        
        Args:
            edit: Edit object with file_path, old_content, and new_content
        
        Returns:
            True if the edit was applied and verified successfully
        """
        pass
    
    @abstractmethod
    def run_tests(self, test_command: str) -> TestResult:
        """
        Run the test suite and return results.
        
        The adapter executes the test command in the workspace directory and
        captures stdout, stderr, return code, and duration.
        
        Args:
            test_command: Shell command to run (e.g., "pytest", "npm test")
        
        Returns:
            TestResult with pass/fail status and output
        """
        pass
    
    @abstractmethod
    def teardown(self) -> None:
        """
        Clean up, close editor, remove temp files, measure resource usage.
        
        Must set self.telemetry.teardown_ms and capture peak memory/CPU.
        """
        pass
    
    # ------------------------------------------------------------------
    # Utility methods (can be overridden, but default implementations work)
    # ------------------------------------------------------------------
    
    def extract_code_from_markdown(self, raw: str) -> str:
        """
        Extract the first fenced code block from a markdown response.
        
        Most code editors wrap generated code in triple backticks. This
        helper extracts the inner code block. If no block is found, returns
        the raw text as-is.
        """
        import re
        match = re.search(r"```(?:\w+)?\n(.*?)\n```", raw, re.DOTALL)
        if match:
            return match.group(1).strip()
        return raw.strip()
    
    def _check_syntax(self, file_path: str) -> bool:
        """
        Verify that the file at file_path is syntactically valid.
        
        Uses the language-appropriate checker (python -m py_compile,
        node --check, rustc --emit=metadata, etc.) based on file extension.
        """
        import subprocess
        import os
        
        ext = os.path.splitext(file_path)[1]
        
        if ext == ".py":
            result = subprocess.run(
                ["python3", "-m", "py_compile", file_path],
                capture_output=True, text=True
            )
        elif ext in (".js", ".mjs"):
            result = subprocess.run(
                ["node", "--check", file_path],
                capture_output=True, text=True
            )
        elif ext == ".ts":
            result = subprocess.run(
                ["npx", "tsc", "--noEmit", file_path],
                capture_output=True, text=True
            )
        elif ext == ".rs":
            result = subprocess.run(
                ["rustc", "--emit=metadata", file_path],
                capture_output=True, text=True
            )
        elif ext == ".go":
            result = subprocess.run(
                ["go", "build", file_path],
                capture_output=True, text=True
            )
        else:
            # No syntax checker for this language; assume valid
            return True
        
        return result.returncode == 0
