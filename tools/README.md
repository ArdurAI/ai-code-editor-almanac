# Per-Tool Deep-Dive Pages

Each `.md` file in this directory is a deep-dive analysis of one tool on the roster.

## Naming convention

`<tool-name>.md` where `tool-name` is the lowercase, hyphenated version of the tool name (e.g., `cursor.md`, `github-copilot.md`).

## Page structure

Every tool page follows the template:

```markdown
# Tool Name

| Attribute | Value |
|-----------|-------|
| Tier | A / B / C |
| Type | Category |
| License | License |
| Region | Region |
| URL | Homepage |

## One-line summary

## Architecture

## Key features

## Benchmark status

## Ops reality

## Cost model

## When to use / when to avoid
```

## Status

- **Tier A**: 17 pages created (founding edition). Benchmark status is "Not run" pending harness build.
- **Tier B**: Stubs planned for July 2026 edition.
- **Tier C**: Stubs planned for July 2026 edition.

## How to add a new tool page

1. Add the tool to `data/roster.json` with all required fields.
2. Create `tools/<tool-name>.md` from the template above.
3. Link it from the edition in `editions/YYYY-MM.md`.
4. Update the README roster-at-a-glance if the tool is Tier A.
