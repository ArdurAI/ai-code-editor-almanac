# Smoke Gate Results

The smoke gate is a 3-turn scenario that every editor must pass before entering the roster.

## Scenario

```
Turn 1: Open a source file in a supported workspace (Python project with tests)
Turn 2: Request a code generation or edit ("Implement the multiply function")
Turn 3: Verify the generated code is syntactically valid and the project tests still pass
```

## Pass criteria

- No crashes, no silent failures, no IDE freezing
- Generated code must be syntactically valid for the target language
- The editor must not break existing code (tests must still pass)
- Results must be deterministic
- The editor must handle the basic case without workarounds

## Results

| Adapter | Date | Pass | Notes |
|---------|------|------|-------|
| Cursor | Not yet run | — | Adapter skeleton ready; needs Cursor CLI + auth |
| Copilot | Not yet run | — | Adapter skeleton ready; needs VS Code + Copilot extension + auth |
| Claude Code | Not yet run | — | Adapter skeleton ready; needs `claude` CLI + ANTHROPIC_API_KEY |

## How to run

```bash
# Cursor
python smoke-gate.py --adapter cursor --config '{"cursor_cli": "cursor"}'

# GitHub Copilot
python smoke-gate.py --adapter copilot --config '{"vscode_cli": "code"}'

# Claude Code
python smoke-gate.py --adapter claude-code --config '{"claude_binary": "claude", "model": "claude-sonnet-4"}'
```

Results are written to `benchmarks/smoke-gate/<adapter>-smoke-gate-<timestamp>.json`.

## Failure mode taxonomy

Failures observed during smoke gate are classified by the taxonomy in `TESTING.md`:

- **Setup**: `install_failed`, `dependency_conflict`, `config_error`, `auth_failure`
- **Generation**: `syntax_error`, `hallucinated_api`, `wrong_type`, `missing_context`
- **Latency**: `completion_timeout`, `chat_timeout`, `agent_timeout`, `ui_freeze`
- **Quality**: `test_failure`, `regression_introduced`, `partial_edit`
