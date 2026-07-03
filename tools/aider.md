# Aider


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | Terminal pair-programmer |
| License | Apache-2.0 |
| Region | Global |
| URL | https://aider.chat |

## One-line summary

47K+ GitHub stars; the original AI terminal pair-programmer with Git-native diffs, tree-sitter code analysis, and model-agnostic support for 50+ LLMs.

## Architecture

Aider is a terminal-based AI pair-programmer that works directly with your local git repository. Key architectural elements:

- **Git-native workflow**: Every AI change is automatically committed with a descriptive message; full git history preserved
- **Tree-sitter analysis**: Uses tree-sitter for syntactic code understanding (repo map) to provide context without sending entire files
- **Unified diff format**: AI edits expressed as search/replace blocks — more reliable than full-file regeneration
- **Model-agnostic**: Supports 50+ LLM providers (Claude, GPT, Gemini, DeepSeek, local models via Ollama)
- **Repo map**: Automatically builds a structural map of your codebase (functions, classes, dependencies) for context
- **Architect mode**: Uses a strong reasoning model to plan, then a cheaper coding model to execute

## Key features

- Git-native: automatic commits with descriptive messages for every change
- Repo map: structural codebase understanding via tree-sitter
- Unified diff editing: reliable multi-file changes via search/replace blocks
- 50+ LLM provider support (BYOK)
- Architect/Editor mode: use expensive models for planning, cheap models for coding
- Voice support (experimental)
- Browser mode for web interaction
- Linting and testing integration
- Markdown and image support in chat
- Works with any terminal; no IDE required

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Strong | SWE-bench: ~26% (aider-litellm mode); actively improved |
| Latency | Not run | Depends on model provider |
| Token economics | Strong | Architect mode reduces costs; repo map minimizes context |
| Scale behavior | Strong | Repo map handles large codebases efficiently |
| Ops burden | Low | pip install; run in terminal |
| Developer experience | High | Clean TUI; git history as safety net |
| Data sovereignty | Strong | BYOK; local model support |

## Ops reality

**Setup burden:** Low — `pip install aider-chat`; configure API key.

**Sharp edges:**
- Terminal-only — no visual diff preview (relies on git diff after changes)
- Unified diff format can fail on heavily formatted/reindented code
- Repo map building on large codebases can be slow on first run
- Architect mode adds latency (two model calls per task)

## Cost model

- **Software**: Free (Apache-2.0 open source)
- **API costs**: BYOK — depends on model chosen:
  - DeepSeek: ~$0.27/$1.10 per 1M tokens (cheapest quality option)
  - Claude Sonnet: ~$3/$15 per 1M tokens
  - Local models (Ollama): Free
- **Architect mode**: Uses two models — more total tokens but often cheaper (planning with cheap model, coding with mid-tier)

## When to use / when to avoid

**Use when:**
- You prefer terminal-native workflows
- You want git-native AI changes with automatic commits
- You need model flexibility (50+ providers)
- You want open-source with no subscription

**Avoid when:**
- You need inline completions or IDE integration
- You prefer visual diff review
- You need browser automation or MCP extensibility (use Cline)

## Roster entry

- **Name:** Aider
- **Type:** Terminal pair-programmer
- **License:** Apache-2.0
- **Region:** Global
- **Tier:** A
- **Notes:** 47K+ stars; Git-aware diffs; model-agnostic

---

## Deep Analysis

### 1. How Is This Tool Useful?

Aider pioneered the terminal-native AI pair-programming model and remains a top choice for developers who live in the terminal. Its git-native approach is the defining feature: every AI-made change is automatically committed with a descriptive message, creating a clean, reviewable history. If the AI makes a mistake, you simply `git revert`. This makes experimentation safe and reviewable — a significant advantage over tools that make changes without version control integration.

The repo map feature is technically impressive and practically valuable. Using tree-sitter, Aider builds a structural map of your entire codebase (functions, classes, their signatures and relationships) without sending full file contents to the LLM. This provides the AI with architectural awareness while minimizing token consumption. For large codebases where sending all files would exceed context windows or be prohibitively expensive, the repo map is an elegant solution that balances context quality with cost.

The model-agnostic approach with 50+ provider support gives developers maximum flexibility. Aider's model recommendations page is a community resource for understanding which models perform best on coding tasks. The Architect mode (introduced in 2024) is particularly clever: use a strong reasoning model (like Claude Opus or o3) to plan the approach, then a cheaper coding model (like DeepSeek or Sonnet) to implement — reducing costs while maintaining quality.

### 2. Gotchas of Using This Tool

The unified diff format (SEARCH/REPLACE blocks) can fail when code has been reformatted between the AI's analysis and its edit attempt. If your code has inconsistent indentation, tabs vs. spaces conflicts, or auto-formatting (Prettier, Black) that changes the file between Aider's read and write, the diff application can fail. This manifests as "edit failed" errors that frustrate new users. The workaround is to commit or stash changes before asking Aider to edit.

Terminal-only operation means no visual diff preview. You must trust the AI's changes or review them via `git diff` afterward. For developers who prefer to see proposed changes before they're applied (like Cursor's diff view), Aider's commit-first-ask-questions-later approach requires a mindset shift. However, the git history makes this safe — you can always revert.

The repo map for very large codebases (10K+ files) can be slow to build initially and may consume significant tokens. While Aider optimizes by sending only relevant portions, the first interaction with a large codebase can be expensive. Developers should use `/map` commands to understand and control what's included.

### 3. Limitations

- **No inline completions**: Terminal-based; no ghost text or IDE integration
- **No IDE integration**: Cannot be used as a VS Code or JetBrains extension
- **Diff application failures**: Unified diff format can fail on reformatted/inconsistent code
- **No browser automation**: Cannot interact with web applications (unlike Cline)
- **No MCP support**: Less extensible than Cline or Claude Code
- **Context window**: While repo map helps, very large tasks can still exceed limits
- **Single conversation**: No sub-agent or parallel task execution

### 4. How Secure Is This Tool?

- **License**: Apache-2.0 (fully open source; auditable)
- **BYOK**: Code sent directly to your chosen provider; Aider doesn't intermediate
- **Local model support**: Ollama integration for fully offline operation
- **Telemetry**: No telemetry collection; fully local operation
- **Git integration**: All changes version-controlled — auditable and reversible
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low — you control the provider; local models eliminate external exposure
- **No data collection**: Aider doesn't collect or transmit usage data

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Aider requires terminal proficiency, git knowledge, and API key configuration. It's purely a developer tool with no accessible interface for non-technical users. The TUI (text user interface) is clean but requires comfort with command-line workflows.

### 6. What Does This Tool Solve That Others Don't?

Aider's unique advantages:

- **Git-native workflow**: Automatic commits with descriptive messages — no other tool makes version control this seamless
- **Repo map via tree-sitter**: Structural codebase understanding without full-file context — elegant token efficiency
- **Architect/Editor mode**: Cost optimization by separating planning and execution across model tiers
- **50+ model providers**: Most extensive model support of any coding tool
- **Terminal-native**: No IDE, extension, or GUI required — works anywhere with a terminal
- **Transparent benchmarks**: Aider publishes its own SWE-bench results and model performance comparisons

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | **Aider** | Git-native; repo map; 50+ models | Terminal-only; no IDE integration |
| 2 | Claude Code | Best-in-class agentic coding | Claude-only; expensive |
| 3 | OpenCode | TUI; multi-provider | Less mature; fewer features |
| 4 | Codex CLI | ChatGPT integration; Rust | OpenAI-focused |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Very active. [Aider-AI/aider](https://github.com/Aider-AI/aider) has **46,961 stars**, 4,680 forks, 1,699 open issues. Last pushed: May 22, 2026. Created May 2023 — steady, consistent development by primarily one maintainer (Paul Gauthier).

**Areas for improvement:**
- IDE integration (VS Code extension would expand reach significantly)
- Sub-agent support for parallel task execution
- MCP integration for extensibility
- Browser automation for web testing
- Better handling of code formatting conflicts in diffs
- Multi-maintainer team to reduce bus-factor risk

### 9. Official Maintainer Contacts

- **GitHub**: [Aider-AI/aider](https://github.com/Aider-AI/aider)
- **Creator**: Paul Gauthier ([@paul-gauthier](https://github.com/paul-gauthier))
- **Discord**: Aider Discord community (link in GitHub README)
- **Docs**: https://aider.chat/docs/
- **Blog**: https://aider.chat/docs/leaderboards/ (model benchmark leaderboards)

### 10. General Usage Guidance

**Getting started:**
1. Install: `pip install aider-chat`
2. Set API key: `export ANTHROPIC_API_KEY=...` (or OPENAI_API_KEY, etc.)
3. Navigate to your git repo: `cd my-project`
4. Run: `aider` to start interactive mode
5. Describe changes in natural language
6. Review changes: `git diff` or `git log`
7. Use `/help` for commands; `/model` to switch models

**Best practices:**
- Always work in a clean git state before asking Aider to edit
- Use `/add <file>` to explicitly include files in context
- Try Architect mode for complex tasks (`--architect`)
- Use DeepSeek for cost-effective coding; Claude for complex reasoning
- Review commits with `git log --oneline` to see AI's work
- Use `/tokens` to monitor context usage

**When NOT to use:**
- If you need inline completions or IDE integration
- If you need browser automation (use Cline)
- If you want sub-agent parallel execution (use Claude Code)
- If terminal workflows are uncomfortable for your team

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
