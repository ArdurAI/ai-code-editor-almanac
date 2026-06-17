#!/usr/bin/env python3
"""
Smoke Gate — 3-turn scenario for every code editor on the roster.

The smoke gate is the minimum bar for entry. Every editor must pass
before it is officially "in" the roster. The scenario is identical for
every tool:

    Turn 1: Open a source file in a supported workspace
    Turn 2: Request a code generation or edit
    Turn 3: Verify the generated code is syntactically valid and tests pass

Pass criteria:
- No crashes, no silent failures, no IDE freezing
- Generated code must be syntactically valid for the target language
- The editor must not break existing code (tests must still pass)
- Results must be deterministic
- The editor must handle the basic case without workarounds
"""

import argparse
import json
import os
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Any

# Add the adapters directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "adapters"))

from base import CodeEditorAdapter, CompletionResponse, GenerationResponse, Edit, TestResult
from cursor_adapter import CursorAdapter
from copilot_adapter import CopilotAdapter
from claude_code_adapter import ClaudeCodeAdapter


# ------------------------------------------------------------------
# Test workspace — a small Python project with tests
# ------------------------------------------------------------------

TEST_WORKSPACE_FILES = {
    "calculator.py": '''
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    # TODO: implement multiply
    pass

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
''',
    "test_calculator.py": '''
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    with pytest.raises(ValueError):
        divide(5, 0)
''',
    "requirements.txt": "pytest\n",
}


def create_test_workspace() -> str:
    """Create a temporary workspace with the test project."""
    workspace = tempfile.mkdtemp(prefix="smoke-gate-")
    for filename, content in TEST_WORKSPACE_FILES.items():
        path = os.path.join(workspace, filename)
        with open(path, "w") as f:
            f.write(content.strip() + "\n")
    return workspace


# ------------------------------------------------------------------
# Smoke Gate Scenario
# ------------------------------------------------------------------

class SmokeGate:
    """
    Run the 3-turn smoke gate scenario for a single adapter.
    
    Results are written as JSON to the benchmarks/smoke-gate/ directory.
    """
    
    def __init__(self, adapter: CodeEditorAdapter, workspace: str):
        self.adapter = adapter
        self.workspace = workspace
        self.results: Dict[str, Any] = {
            "adapter": adapter.__class__.__name__,
            "workspace": workspace,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "turns": [],
            "pass": False,
            "errors": [],
            "ops_notes": [],
        }
    
    def run(self) -> Dict[str, Any]:
        """Execute the 3-turn scenario."""
        try:
            # Turn 0: Setup
            print(f"[Setup] {self.adapter.__class__.__name__}")
            self.adapter.setup()
            
            # Turn 1: Open workspace
            print(f"[Turn 1] Open workspace: {self.workspace}")
            self.adapter.open_workspace(self.workspace)
            self._record_turn(1, "open_workspace", "Workspace opened successfully")
            
            # Turn 2: Request generation (implement multiply)
            print(f"[Turn 2] Request generation: implement multiply")
            prompt = (
                "Implement the `multiply` function in calculator.py. "
                "It should return the product of two numbers."
            )
            gen_response = self.adapter.request_generation(
                prompt=prompt,
                context_files=["calculator.py"],
            )
            self._record_turn(
                2, "request_generation", "Generation received",
                generation=gen_response,
            )
            
            # Turn 3: Apply edit and verify
            print(f"[Turn 3] Apply edit and run tests")
            edit = Edit(
                file_path="calculator.py",
                old_content="    # TODO: implement multiply\n    pass",
                new_content=gen_response.code,
            )
            applied = self.adapter.apply_edit(edit)
            self._record_turn(3, "apply_edit", f"Edit applied: {applied}")
            
            if not applied:
                self.results["errors"].append("Edit failed to apply")
            
            # Run tests
            test_result = self.adapter.run_tests("pytest")
            self.results["tests"] = {
                "passed": test_result.passed,
                "stdout": test_result.stdout,
                "stderr": test_result.stderr,
                "duration_ms": test_result.duration_ms,
            }
            
            # Determine pass/fail
            self.results["pass"] = (
                applied and test_result.passed and not self.adapter.telemetry.errors
            )
            
            # Collect telemetry
            self.results["telemetry"] = self.adapter.telemetry.to_dict()
            
        except Exception as e:
            self.results["errors"].append(str(e))
            self.results["pass"] = False
        finally:
            # Teardown
            print(f"[Teardown] {self.adapter.__class__.__name__}")
            self.adapter.teardown()
        
        return self.results
    
    def _record_turn(
        self,
        turn_number: int,
        action: str,
        note: str,
        generation: GenerationResponse = None,
    ):
        turn = {
            "turn": turn_number,
            "action": action,
            "note": note,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        if generation:
            turn["generation"] = {
                "code": generation.code,
                "latency_ms": generation.latency_ms,
                "tokens": generation.tokens,
                "model": generation.model,
            }
        self.results["turns"].append(turn)


def main():
    parser = argparse.ArgumentParser(description="Smoke Gate for code editors")
    parser.add_argument(
        "--adapter",
        choices=["cursor", "copilot", "claude-code"],
        required=True,
        help="Which adapter to test",
    )
    parser.add_argument(
        "--output",
        default="benchmarks/smoke-gate",
        help="Directory to write results",
    )
    parser.add_argument(
        "--config",
        default="{}",
        help="JSON config for the adapter",
    )
    args = parser.parse_args()
    
    # Parse config
    config = json.loads(args.config)
    
    # Select adapter
    adapters = {
        "cursor": CursorAdapter,
        "copilot": CopilotAdapter,
        "claude-code": ClaudeCodeAdapter,
    }
    adapter_cls = adapters[args.adapter]
    adapter = adapter_cls(config=config)
    
    # Create workspace
    workspace = create_test_workspace()
    print(f"Workspace created: {workspace}")
    
    # Run smoke gate
    gate = SmokeGate(adapter, workspace)
    results = gate.run()
    
    # Write results
    os.makedirs(args.output, exist_ok=True)
    output_file = os.path.join(
        args.output,
        f"{args.adapter}-smoke-gate-{time.strftime('%Y%m%d-%H%M%S')}.json",
    )
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults written to: {output_file}")
    print(f"Pass: {results['pass']}")
    if results["errors"]:
        print(f"Errors: {results['errors']}")
    
    # Cleanup workspace
    import shutil
    shutil.rmtree(workspace, ignore_errors=True)
    
    return 0 if results["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
