# Implementation Guide

How the code editor almanac is built, how to add a tool, how to update an edition, and how the data pipeline works.

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [The Data Pipeline](#the-data-pipeline)
3. [Adding a New Code Editor](#adding-a-new-code-editor)
4. [Updating an Edition](#updating-an-edition)
5. [The Roster JSON Schema](#the-roster-json-schema)
6. [Directory Conventions](#directory-conventions)
7. [Building the Adapter](#building-the-adapter)
8. [Automation](#automation)

---

## Repository Structure

```
ai-code-editor-almanac/
├── README.md                          # Project overview + roster at a glance
├── INTENT.md                          # Philosophy, design principles, governance
├── IMPLEMENTATION.md                  # This file
├── TESTING.md                         # Benchmark methodology, harness details
├── TROUBLESHOOTING.md                 # Common issues, debugging, FAQ
├── CONTRIBUTING.md                    # How to contribute
├── architecture.md                    # Stack architecture + test philosophy
├── SETUP.md                           # How to push to GitHub
├── .gitignore
│
├── editions/                          # Monthly editions
│   └── 2026-06.md                   # Founding edition
│
├── benchmarks/                        # Benchmark results (rolling)
│   ├── swe-bench/                     # SWE-bench results per editor
│   ├── exercism/                      # Exercism results per editor
│   ├── terminal-bench/                # Terminal-Bench results per editor
│   └── stress/                        # Stress suite results
│
├── methodology/
│   └── benchmark-harness.md         # Detailed harness spec for code editors
│
├── data/
│   └── roster.json                  # Machine-readable catalog (63+ tools)
│
├── tools/                             # Per-tool deep-dive pages
│   ├── cursor.md
│   ├── github-copilot.md
│   ├── claude-code.md
│   └── (populated as deep-dives are written)
│
├── adapters/                          # Code editor adapter implementations
│   ├── base.py                        # CodeEditorAdapter base class
│   ├── cursor_adapter.py
│   ├── copilot_adapter.py
│   ├── claude_code_adapter.py
│   └── (populated as adapters are built)
│
└── assets/                            # Charts, screenshots, latency heatmaps
    ├── smoke-latency-2026-06.png
    ├── landscape-2026-06.png
    └── cost-comparison-2026-06.png
```

## The Data Pipeline

The almanac data flows through four stages:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Discovery      │────▶│  Triage         │────▶│  Research       │────▶│  Publication    │
│  (find editors) │     │  (decide entry) │     │  (deep dive)    │     │  (write edition) │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stage 1: Discovery

Code editors are discovered through:
- **Monthly research swarm**: 8-10 parallel agents search for new AI editors, IDE plugins, and terminal coding agents
- **Community submissions**: Issues, PRs, email, social media, Hacker News "Show HN" posts
- **Vendor announcements**: Major releases (Cursor 0.4x, Copilot X, Claude Code updates)
- **GitHub trending**: New repos with significant star growth in the `ai-code-editor`, `copilot-alternative`, `cline` tags
- **Conference talks**: AI engineering conferences, IDE vendor keynotes, LLM tool demos

### Stage 2: Triage

A code editor enters the roster if it meets ALL of these criteria:
1. **Seriousness**: Not a toy/demo. Must have real code generation capability, real users, or real funding.
2. **Activity**: Last push or release within 6 months. Exceptions for "stable/mature" editors (e.g., VS Code Copilot extension).
3. **Documentation**: Must have a README, docs, or at least a landing page explaining what it does and how to install it.
4. **Accessibility**: Must be accessible to test (open source, free tier, evaluation license, or publicly installable extension).
5. **Scope**: Must fit the code editor category. A general-purpose LLM chatbot doesn't enter unless it has IDE integration.

A code editor is **excluded** if:
- It's a thin wrapper around another editor with no added AI capability
- It has no IDE integration, no CLI agent mode, and no editor extension (pure web playground)
- It has no users, no community, and no evidence of real-world coding use
- It requires an enterprise-only license with no evaluation path

### Stage 3: Research

For each new editor, we collect:
- Name, type (IDE, extension, CLI agent, terminal agent), license, language support, URL, stars
- Last push date, release cadence, changelog quality
- Key features: inline completion, chat, agent mode, multi-file editing, terminal integration
- IDE ecosystem: VS Code, JetBrains, Vim/Neovim, Zed, Emacs, standalone
- Known bugs and sharp edges (from smoke gate): hallucinated imports, broken refactors, lag on large files
- Community health: GitHub issues/PRs, Discord/Slack activity, maintainer responsiveness
- Pricing model: free tier, subscription, per-seat, pay-as-you-go, self-hosted cost

This data is stored in `data/roster.json` and summarized in the edition.

### Stage 4: Publication

The edition is a markdown file that includes:
- Code editor landscape at a glance table
- Per-tier findings and trends (Tier A: market leaders, Tier B: solid alternatives, Tier C: niche/early)
- New tools added and tools removed
- Notable releases and acquisitions (e.g., "Amazon Q Developer now supports X")
- Quest diary (what was tested this month: SWE-bench runs, new adapters, stress tests)
- Cost comparison updates (if pricing changed)

## Adding a New Code Editor

### Step 1: Verify the tool meets triage criteria

Check: seriousness, activity, documentation, accessibility, scope.

For code editors specifically, ask:
- Does it integrate with at least one real IDE or provide a standalone editor?
- Can it generate or edit code, not just chat about code?
- Is there a download, extension marketplace link, or repo to install from?

### Step 2: Add to the roster JSON

Edit `data/roster.json` and add the tool to the `code-editors` category:

```json
{
  "name": "EditorName",
  "type": "IDE|Extension|CLI Agent|Terminal Agent",
  "license": "License",
  "region": "Region",
  "tier": "A|B|C",
  "ide_support": ["VS Code", "JetBrains", "Zed", "Vim", "Standalone"],
  "languages": ["Python", "JavaScript", "TypeScript", "Rust", "Go"],
  "pricing_model": "Free|Freemium|Subscription|Enterprise",
  "notes": "One-line description and key differentiators"
}
```

**Tier assignment rules**:
- **Tier A**: Market leader, widest adoption, or strongest technical merit on SWE-bench/Exercism. Must be actively maintained and have real production usage.
- **Tier B**: Solid option, actively maintained, but not the market leader. Good for specific use cases (e.g., privacy-first, specific language focus, self-hosted).
- **Tier C**: Niche, early-stage, specialized, or has significant limitations. Worth knowing about but not a default choice.

### Step 3: Update the edition

Add the tool to the code editor section in `editions/YYYY-MM.md`. If the tool is Tier A, add it to the roster-at-a-glance table in the README.

### Step 4: Update the category README

If the tool is Tier A, update the tier list in the category README. If there is a parent almanac cross-reference, update `categories/code-editors/README.md` in the parent repo.

### Step 5: Run the smoke gate

Before the tool is officially "in," it must pass the smoke gate (see TESTING.md). The smoke gate for code editors is:

```
Turn 1: Open a source file in a supported IDE/workspace
Turn 2: Request a code generation or edit (inline completion, chat command, or agent task)
Turn 3: Verify the generated code is syntactically valid and semantically reasonable
```

If it fails, document the failure in the edition and assign it to Tier C with a note about the blocker.

### Step 6: Build the adapter (if benchmarking)

If the tool is Tier A or B and will be benchmarked, implement a `CodeEditorAdapter` in `adapters/` (see Building the Adapter below).

## Updating an Edition

### Monthly update checklist

```
□ Check for new code editors (discovery phase: HN, GitHub, Product Hunt, vendor blogs)
□ Triage new editors (add to roster or reject with reason)
□ Update metadata for existing tools (stars, last push, releases, pricing changes)
□ Flag tools for removal (dead/abandoned, no releases in 12+ months, extension delisted)
□ Run smoke gate for new editors
□ Run benchmark updates for re-tested editors (SWE-bench, Exercism, Terminal-Bench)
□ Update cost comparison if pricing models changed
□ Draft the edition markdown
□ Update README roster-at-a-glance
□ Update category READMEs (this repo and parent almanac cross-reference)
□ Commit and push
```

### Edition markdown template

```markdown
# Edition YYYY-MM — [Title]

*Research conducted YYYY-MM-DD. [Context about this month: major releases, new entrants, acquisitions].*

## The code editor landscape at a glance

| Tier | Tool Count | New This Month | Notable Changes |
|------|-----------|----------------|-----------------|
| A    | N         | +X             | [e.g., Cursor released Y] |
| B    | N         | +X             | [e.g., Zed added feature Z] |
| C    | N         | +X             | [e.g., Bolt.new moved from B] |

## Tier A — Market Leaders

[table with accuracy, latency, cost per 1K lines, key findings]

## Tier B — Solid Alternatives

[table with differentiators, best-for notes]

## Tier C — Niche & Early Stage

[table with cautions, watch-list notes]

## Benchmark updates

### SWE-bench
- [Editor]: [score] ([delta from last month])

### Exercism
- [Editor]: [score] ([delta])

### Terminal-Bench
- [Editor]: [score] ([delta])

## Cost comparison

[Updated pricing table if models changed]

## Quest diary — [Month] [Year]

- [what was tested: new adapters, benchmark runs, stress tests]
- [what broke and how it was fixed]

## Coming next month

[what's planned: new tools to triage, adapters to build, methodology updates]

## License
Content is licensed CC BY 4.0.
```

## The Roster JSON Schema

```json
{
  "meta": {
    "name": "Code Editors & IDE Assistants Almanac Roster",
    "version": "YYYY-MM",
    "generated_at": "ISO-8601 timestamp",
    "total_tools": number,
    "categories": number,
    "research_method": "description"
  },
  "categories": {
    "code-editors": {
      "name": "Code Editors & IDE Assistants",
      "description": "AI-powered code editors, IDE extensions, terminal coding agents, and autonomous coding tools",
      "estimated_total": number,
      "tools": [
        {
          "name": "Tool Name",
          "type": "IDE|Extension|CLI Agent|Terminal Agent|Web Agent",
          "license": "License",
          "region": "Region",
          "tier": "A|B|C",
          "ide_support": ["VS Code", "JetBrains", "Zed", "Vim", "Neovim", "Emacs", "Standalone"],
          "languages": ["Python", "JavaScript", "TypeScript", "Rust", "Go", "Java", "C++", "Ruby"],
          "pricing_model": "Free|Freemium|Subscription|Pay-as-you-go|Enterprise|Open Source",
          "notes": "Description"
        }
      ]
    }
  }
}
```

**Field definitions**:
- `name`: The tool's common name. Use the name the tool calls itself (e.g., "Cursor", not "cursor.sh").
- `type`: What kind of tool is it? (IDE = standalone editor; Extension = IDE plugin; CLI Agent = terminal-based; Terminal Agent = interactive shell agent; Web Agent = browser-based)
- `license`: The primary license. Use SPDX identifiers where possible. For proprietary tools, use "Proprietary".
- `region`: Where the tool is primarily developed (US, EU, China, Global, etc.)
- `tier`: A, B, or C (see tier rules above)
- `ide_support`: List of IDE/editor platforms the tool supports. Use standardized names.
- `languages`: List of programming languages with first-class support. Keep to top 5.
- `pricing_model`: How the tool is monetized. "Open Source" for fully free self-hosted tools.
- `notes`: One-line description with key differentiators. Keep under 120 chars.

## Directory Conventions

### `editions/`
- One file per month: `YYYY-MM.md`
- Never delete old editions. The history is part of the record.
- New editions are appended; old editions are never rewritten.
- Include the cost-comparison table in every edition if pricing changed.

### `data/`
- `roster.json` is the single source of truth for the tool catalog.
- It is machine-generated from the research process.
- It should be valid JSON at all times.
- Include `ide_support` and `languages` arrays for every tool.

### `benchmarks/`
- One directory per benchmark suite: `swe-bench/`, `exercism/`, `terminal-bench/`, `stress/`
- One file per benchmark run: `<editor>-<suite>-<date>.md`
- Raw JSON files alongside the markdown: `<editor>-<suite>-<date>.json`
- Raw data is never deleted. It is the audit trail.
- Include the full prompt/response log in the JSON for reproducibility.

### `tools/`
- One file per tool: `<name>.md`
- Contains deep-dive analysis: setup experience, IDE integration quality, benchmark results, bug notes, comparison with peers, cost analysis
- Populated as deep-dives are written (not all tools have a page immediately)
- Tier A tools should have a page by the second edition after entry.

### `adapters/`
- One file per adapter: `<editor_name>_adapter.py`
- Must inherit from `base.CodeEditorAdapter`
- Must be documented with inline comments explaining IDE integration choices
- Must be isolated — no cross-adapter dependencies

### `assets/`
- Images, charts, screenshots, latency heatmaps referenced by editions and benchmarks
- Named descriptively: `smoke-latency-2026-06.png`, `landscape-2026-06.png`, `swe-bench-ranking-2026-06.png`
- Screenshots of IDE integration should include the editor name and version in the filename.

### `methodology/`
- The benchmark harness specification for code editors
- Frozen before any results are generated
- Changes require an RFC and a public announcement
- Must specify the SWE-bench split, Exercism tracks, and Terminal-Bench commands used

## Building the Adapter

When a new code editor is added to the roster and is ready for benchmarking, an adapter must be built. The adapter is the bridge between the editor's API/extension interface and the harness's fixed interface.

### The CodeEditorAdapter contract

```python
class CodeEditorAdapter:
    def setup(self) -> None:
        """Install, configure, and start the editor or extension."""
        pass
    
    def open_workspace(self, workspace_path: str) -> None:
        """Open the project/workspace. Index files. Build AST/graph if applicable."""
        pass
    
    def request_completion(self, file_path: str, cursor_line: int, cursor_col: int) -> CompletionResponse:
        """Request inline completion at the given cursor position. Measure latency."""
        pass
    
    def request_generation(self, prompt: str, context_files: List[str]) -> GenerationResponse:
        """Send a chat/agent command. Return generated code and metadata."""
        pass
    
    def apply_edit(self, edit: Edit) -> bool:
        """Apply the suggested edit to the file. Return success/failure."""
        pass
    
    def run_tests(self, test_command: str) -> TestResult:
        """Run the test suite and return results (pass/fail, output)."""
        pass
    
    def teardown(self) -> None:
        """Clean up, close editor, remove temp files, measure resource usage."""
        pass
```

### Adapter types by editor kind

| Editor Type | Adapter Pattern | Example |
|-------------|-----------------|---------|
| **VS Code Extension** | Launch VS Code headless or UI, use Extension Host API or CLI | Copilot, Cursor, Continue |
| **JetBrains Plugin** | Launch IntelliJ/PyCharm with plugin, use HTTP API or robot framework | Cody, Amazon Q Developer, Junie |
| **Standalone IDE** | Launch the IDE binary, use internal API or LSP | Zed, Trae, Windsurf |
| **CLI Agent** | Run as subprocess, drive via stdin/stdout or CLI flags | Claude Code, Aider, OpenCode |
| **Terminal Agent** | Spawn in terminal emulator, send keystrokes, capture output | Qwen Code CLI, Terminal-Bench drivers |
| **Web-based** | Use browser automation (Playwright/Selenium) to drive the UI | v0, Bolt.new, Lovable |

### Adapter rules

1. The adapter must be **pure** — it should not modify the editor's behavior, only interface with it.
2. The adapter must be **documented** — every step should be explainable in plain English (e.g., "We use the VS Code CLI to open the workspace because the extension API requires a running window").
3. The adapter must be **reproducible** — running it twice on the same machine with the same editor version should produce the same setup.
4. The adapter must be **isolated** — it should not depend on other tools' adapters. Each editor gets its own virtual environment / container if needed.
5. The adapter code is **published** in the benchmark harness repo (separate from the almanac repo).
6. The adapter must handle **language server lifecycle** — starting/stopping LSPs, waiting for indexing, checking readiness.

### Example adapter (pseudocode — VS Code extension)

```python
class VSCodeExtensionAdapter(CodeEditorAdapter):
    def __init__(self, extension_name, config):
        self.extension = extension_name
        self.config = config
        self.vscode_cli = "code"
    
    def setup(self):
        # Install the extension from marketplace or VSIX
        if self.extension == "cursor":
            subprocess.run([self.vscode_cli, "--install-extension", "cursor-extension.vsix"])
        elif self.extension == "copilot":
            subprocess.run([self.vscode_cli, "--install-extension", "GitHub.copilot"])
        # Authenticate if needed
        self._authenticate()
    
    def open_workspace(self, workspace_path):
        self.workspace = workspace_path
        subprocess.run([self.vscode_cli, workspace_path, "--wait"])
        # Wait for language server to be ready
        self._wait_for_lsp_ready()
    
    def request_completion(self, file_path, line, col):
        # Use the extension's internal API or HTTP endpoint
        response = self._post_to_extension_api("/complete", {
            "file": file_path, "line": line, "col": col
        })
        latency = time.monotonic() - start
        return CompletionResponse(text=response["text"], latency=latency)
    
    def request_generation(self, prompt, context_files):
        # Use chat/agent panel API
        response = self._post_to_extension_api("/generate", {
            "prompt": prompt, "context": context_files
        })
        return GenerationResponse(code=response["code"], explanation=response["explanation"])
    
    def apply_edit(self, edit):
        # Write the edit to disk and verify syntax
        with open(edit.file_path, "w") as f:
            f.write(edit.new_content)
        return self._check_syntax(edit.file_path)
    
    def run_tests(self, test_command):
        result = subprocess.run(test_command, shell=True, capture_output=True, text=True)
        return TestResult(passed=(result.returncode == 0), output=result.stdout)
    
    def teardown(self):
        subprocess.run([self.vscode_cli, "--close"])
        # Clean up temp files
```

### Example adapter (pseudocode — CLI agent)

```python
class CLIAgentAdapter(CodeEditorAdapter):
    def __init__(self, tool_name, config):
        self.tool = tool_name
        self.config = config
    
    def setup(self):
        if self.tool == "claude-code":
            self.proc = subprocess.Popen(
                ["claude"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.workspace
            )
        elif self.tool == "aider":
            self.proc = subprocess.Popen(
                ["aider", "--model", self.config.model],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                text=True,
                cwd=self.workspace
            )
    
    def request_generation(self, prompt, context_files):
        # Send the prompt via stdin and capture output
        self.proc.stdin.write(f"/code {prompt}\n")
        self.proc.stdin.flush()
        output = self._read_until_prompt()
        return GenerationResponse(code=self._extract_code(output), raw=output)
    
    def apply_edit(self, edit):
        # Aider/Claude Code may have already applied the edit
        # Verify by checking file content
        return self._verify_file_content(edit.file_path, edit.expected_content)
    
    def teardown(self):
        self.proc.stdin.write("/exit\n")
        self.proc.wait()
```

## Automation

### Monthly update cron

The monthly update is run by a scheduled job:
- **Trigger**: `cron` expression `0 7 15 * *` (monthly, 15th at 7:00 AM)
- **Action**: Runs a research agent to discover new editors, update metadata, and draft the next edition
- **Output**: Commits to the repo with the updated roster and new edition

### GitHub Actions (optional)

For automatic metadata refresh (GitHub stars, last push dates, extension marketplace ratings), a GitHub Actions workflow can be configured:

```yaml
name: Monthly Metadata Refresh
on:
  schedule:
    - cron: '0 7 1 * *'
  workflow_dispatch:
jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Refresh metadata
        run: python scripts/refresh_metadata.py
      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "Monthly metadata refresh: $(date +%Y-%m)" || echo "No changes"
          git push
```

## License

Content: CC BY 4.0  
Code: MIT
