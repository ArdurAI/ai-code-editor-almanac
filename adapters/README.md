# Adapters

This directory contains the `CodeEditorAdapter` implementations for each tool on the roster.

## Files

| File | Tool | Type | Status |
|------|------|------|--------|
| `base.py` | — | Base class + dataclasses | ✅ Implemented |
| `cursor_adapter.py` | Cursor | VS Code fork (standalone) | ✅ Skeleton |
| `copilot_adapter.py` | GitHub Copilot | VS Code extension | ✅ Skeleton |
| `claude_code_adapter.py` | Claude Code | CLI agent | ✅ Skeleton |

## Adapter types

| Editor Type | Adapter Pattern | Examples |
|-------------|-----------------|----------|
| **VS Code Extension** | Launch VS Code, use Extension Host API or CLI | Copilot, Continue, Roo Code |
| **Standalone IDE** | Launch IDE binary, use internal API or LSP | Cursor, Zed, Trae, Windsurf |
| **CLI Agent** | Run as subprocess, drive via stdin/stdout | Claude Code, Aider, Codex CLI, Gemini CLI |
| **Terminal Agent** | Spawn in terminal, send keystrokes | Kimi CLI, OpenCode, Qwen Code CLI |
| **Web-based** | Browser automation (Playwright/Selenium) | v0, Bolt.new, Lovable |

## How to add a new adapter

1. Create `<tool_name>_adapter.py` in this directory
2. Import `CodeEditorAdapter` from `base.py`
3. Implement all 7 lifecycle methods:
   - `setup()` — install, configure, authenticate
   - `open_workspace()` — load project, wait for indexing
   - `request_completion()` — inline completion + latency
   - `request_generation()` — chat/agent command + latency
   - `apply_edit()` — write to disk, verify syntax
   - `run_tests()` — execute test suite
   - `teardown()` — cleanup, measure resources
4. Add the adapter to the table above
5. Document known issues and sharp edges in the docstring

## Rules

- **Pure**: adapters should not modify the editor's behavior, only interface with it
- **Documented**: every step should be explainable in plain English
- **Reproducible**: running twice on the same machine should produce the same setup
- **Isolated**: no cross-adapter dependencies; each editor gets its own venv/container if needed
- **Published**: adapter code is open for review

## Note on completeness

The current adapters are **skeletons** with the full structure and documentation.
The placeholder sections (e.g., HTTP API calls, UI automation) are marked with
`# Placeholder` comments. The actual implementation requires:
- Access to the editor's internal API or UI
- Test workspaces with real code
- The benchmark harness runner (separate repo)

These adapters are ready to be wired into the harness once the infrastructure
is available.
