# OpenCode


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | Terminal TUI |
| License | MIT |
| Region | Global |
| URL | https://github.com/sst/opencode |

## One-line summary

184.9K+ GitHub stars; a terminal-based AI coding agent with TUI, 75+ LLM provider support, and Go-based architecture — one of the fastest-growing developer tools of 2025–2026.

## Architecture

OpenCode is a terminal-native AI coding agent with a TUI (text user interface). Key architectural elements:

- **Go-native**: Built in Go for fast startup, low memory, and cross-platform compilation
- **TUI interface**: Rich terminal UI with file browser, chat panel, and diff viewer
- **75+ LLM providers**: Broad model support via direct APIs, OpenRouter, and local model frameworks
- **Agent loop**: Plans, executes file changes, runs commands, and iterates
- **LSP integration**: Language Server Protocol for code understanding
- **Session management**: Persistent sessions with history
- **File-aware**: Understands project structure and file relationships
- **MCP support**: Extensible via Model Context Protocol

## Key features

- 184.9K+ GitHub stars — one of the most starred developer tools ever
- 75+ LLM provider support (BYOK)
- Rich TUI with file browser, chat, and diff viewer
- Go-native (fast, low resource usage, cross-platform)
- LSP integration for code intelligence
- Session management with history
- MCP support for external tools
- Multi-platform (macOS, Linux, Windows)
- MIT licensed — fully open source
- Git-aware workflow

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not publicly available | Depends on model chosen |
| Latency | High | Go-native; fast startup and response |
| Token economics | Strong | BYOK; no markup |
| Scale behavior | Not run | LSP handles large codebases |
| Ops burden | Low | Single binary; minimal config |
| Developer experience | High | Polished TUI |
| Data sovereignty | Strong | BYOK; local model support |

## Ops reality

**Setup burden:** Low — download binary or `npm install -g opencode`; configure API key.

**Sharp edges:**
- TUI may feel limited compared to full IDE experiences
- As a very new project (April 2025), rapid changes can introduce instability
- 4,658 open issues suggest growing pains with rapid adoption
- Documentation may lag behind features

## Cost model

- **Software**: Free (MIT open source)
- **API costs**: BYOK — depends on model chosen
- **No subscription**: Pay only for API usage

## When to use / when to avoid

**Use when:**
- You prefer terminal-native workflows with a polished TUI
- You want maximum model flexibility (75+ providers)
- You value Go-native performance
- You want the hottest new tool with massive community

**Avoid when:**
- You need IDE integration (use Cursor or Cline)
- You want stability over rapid innovation
- You prefer visual interfaces over TUI

## Roster entry

- **Name:** OpenCode
- **Type:** Terminal TUI
- **License:** MIT
- **Region:** Global
- **Tier:** A
- **Notes:** 184.9K+ stars; 75+ LLM providers; Go-based

---

## Deep Analysis

### Daily monitoring update — 2026-07-12

- **Adoption signal:** GitHub stars moved from 184,364 to 184,883 (+519). Star references in this file now use the new 184,883 baseline.

### Daily monitoring update — 2026-07-10

- **Latest release:** `v1.17.18` (2026-07-09): fixes crashes and bad pricing data when GitHub Copilot returns models with a zero billing batch size, and adds a model-specific system prompt for Meta Muse Spark.

### Daily monitoring update — 2026-07-09

- **Latest release:** `v1.17.17` (2026-07-09): improves Meta reasoning-variant/provider handling, fixes desktop model-selector text clipping, adds a dismissible tabs intro and refreshed help entry point, aligns sub-agent task rows with v2 sessions, restyles the revert dock, and adds a v2 free-model selector.
- **Adoption signal:** GitHub stars moved from 182,320 to 184,123 (+1,803). Star references in this file now use the new 184,123 baseline.
- **Community health:** Open issues decreased from 5,295 to 4,652 (-643). This is a strong backlog-burn/triage signal, though closure quality should still be checked.

### 1. How Is This Tool Useful?

OpenCode's explosive growth (184.9K+ GitHub stars in just over a year) makes it one of the most adopted AI coding tools of 2025–2026. The appeal is clear: a polished terminal UI (TUI) that provides a rich interactive experience without leaving the terminal. Unlike bare CLI tools (Claude Code, Aider) that use simple text interfaces, OpenCode's TUI includes a file browser, chat panel, diff viewer, and session manager — giving terminal lovers a near-IDE experience without leaving their preferred environment.

The Go-native architecture provides tangible benefits: instant startup, minimal memory usage, and single-binary distribution. Compared to Node.js-based CLI tools (Claude Code, Gemini CLI) that require npm and have slower startup, OpenCode's Go binary launches instantly and uses far less RAM. For developers who live in the terminal and value speed, this matters. The cross-platform compilation means the same binary works on macOS, Linux, and Windows without dependencies.

The 75+ LLM provider support gives developers maximum flexibility. Unlike Claude Code (Claude-only) or Codex CLI (OpenAI-only), OpenCode lets you switch between any provider — Claude for complex reasoning, GPT-4o for speed, Gemini for cost, local models for privacy. This model-agnostic approach, combined with the polished TUI, makes OpenCode the most flexible terminal-based AI coding agent.

### 2. Gotchas of Using This Tool

The project's explosive growth brings growing pains. With 4,658 open issues, OpenCode is clearly experiencing the challenges of rapid adoption — bug reports pile up faster than they can be addressed, documentation lags behind features, and breaking changes occur frequently. Developers adopting OpenCode should be prepared for a fast-moving project where today's workflow may change tomorrow. Pinning to specific versions and monitoring changelogs is essential.

The TUI, while polished, has inherent limitations compared to full IDE experiences. There's no inline completion (ghost text), no visual code navigation (go-to-definition in a sidebar), and no rich diff viewing with syntax highlighting at the level of VS Code. Developers who split their time between terminal and IDE may find the TUI insufficient for complex tasks that benefit from visual aids.

As a very new project (created April 2025), OpenCode's long-term sustainability is unproven. While 184K+ stars is impressive, open-source projects can lose momentum. The project is maintained by SST (a well-known web development framework team), which provides some confidence, but the AI tooling space is extremely competitive. Developers should have a migration plan in case the project loses momentum.

### 3. Limitations

- **TUI limitations**: No inline completions, limited visual navigation
- **Rapid changes**: Breaking changes frequent; stability not guaranteed
- **Issue backlog**: 4,658 open issues indicate growing pains
- **Documentation**: May lag behind rapid feature development
- **No IDE integration**: Terminal-only; no VS Code or JetBrains extension
- **Agent maturity**: Newer agent loop; less proven than Claude Code or Aider
- **Community resources**: Fewer tutorials and guides than established tools

### 4. How Secure Is This Tool?

- **License**: MIT (fully open source; auditable)
- **BYOK**: Code goes directly to your chosen provider
- **Local model support**: Ollama and other local frameworks
- **Telemetry**: Minimal; configurable
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low — BYOK with local model option
- **Single binary**: Go binary reduces dependency attack surface
- **SST backing**: Maintained by established open-source organization

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

OpenCode is a terminal-based developer tool. The TUI requires terminal familiarity, and the 75+ provider configuration requires API key management. Non-technical users cannot use it.

### 6. What Does This Tool Solve That Others Don't?

OpenCode's unique advantages:

- **Polished TUI for terminal coding**: Richest terminal interface among AI coding agents
- **Go-native performance**: Fastest startup and lowest resource usage
- **75+ model providers**: Most model options for a TUI-based tool
- **LSP integration**: Code intelligence within the terminal
- **184.9K+ star community**: Massive community and rapid innovation

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | Claude Code | Best agentic coding | Claude-only; expensive |
| 2 | **OpenCode** | TUI; Go-fast; 75+ models; huge community | Rapid changes; growing pains |
| 3 | Aider | Git-native; repo map; stable | Terminal-only; simpler UI |
| 4 | Codex CLI | ChatGPT-included; sandboxed | OpenAI-only |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Extremely active. [sst/opencode](https://github.com/sst/opencode) has **184,883 stars**, 22,447 forks, 4,658 open issues. Last pushed: July 12, 2026. Created April 2025 — the fastest-growing AI coding tool by GitHub stars.

**Areas for improvement:**
- Issue triage and resolution (4,658 open issues)
- Documentation to match feature velocity
- Stability and versioning strategy
- Inline completion support
- IDE integration (VS Code extension)
- Better onboarding for new users
- Clearer differentiation from Claude Code and Aider

### 9. Official Maintainer Contacts

- **GitHub**: [sst/opencode](https://github.com/sst/opencode) — 184K+ stars
- **Organization**: SST (https://sst.dev)
- **Discord**: SST/OpenCode Discord (link in GitHub README)
- **Docs**: Documentation in GitHub repository
- **Twitter/X**: [@sst_dev](https://twitter.com/sst_dev) (SST)

### 10. General Usage Guidance

**Getting started:**
1. Install: `npm install -g opencode` (or download binary from GitHub)
2. Configure API key (Anthropic, OpenAI, OpenRouter, etc.)
3. Navigate to project: `cd my-project`
4. Run: `opencode` to launch TUI
5. Use the file browser to select context files
6. Describe tasks in the chat panel
7. Review diffs in the diff viewer

**Best practices:**
- Pin to specific versions for stability
- Monitor changelogs for breaking changes
- Use @mentions to scope context precisely
- Experiment with different models for different task types
- Use LSP integration for code navigation
- Contribute bug reports — the project needs community help
- Keep a migration plan given the project's youth

**When NOT to use:**
- If you need IDE integration (use Cursor or Cline)
- If stability is critical (use Claude Code or Aider)
- If you need inline completions
- If TUI interfaces are uncomfortable for you

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
