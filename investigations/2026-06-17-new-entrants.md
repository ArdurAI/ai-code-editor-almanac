# Post-June 2026 New Entrants Investigation

*Investigation conducted 2026-06-17 via web search across Product Hunt, Hacker News, vendor blogs, and tech media.*

## New tools discovered

### Oh-My-Pi (omp)

| Attribute | Value |
|-----------|-------|
| Name | Oh-My-Pi (omp) |
| Type | Terminal agent |
| License | MIT |
| Stars | 9.3K GitHub (June 2026) |
| Forks | 753 |
| Releases | 410 releases as of June 2026 |
| Region | Global |
| URL | https://github.com/oh-my-pi/omp |

**What it is:** A terminal AI coding agent that bundles IDE-grade capabilities — LSP, DAP debuggers, persistent Python/JS kernels, ripgrep, and ast-grep — into a single MIT-licensed terminal process that speaks to 40+ LLM providers.

**Why it matters:** Unlike polished commercial competitors, it takes a technically ambitious approach: a terminal process with full IDE capabilities (not just chat). Class-leading on technical merit but single-maintainer dependency and volatility are concerns.

**Triage assessment:**
- ✅ Seriousness: Real code generation, real users, active development (410 releases)
- ✅ Activity: June 2026 release, very active
- ✅ Documentation: GitHub repo with README, MIT license
- ✅ Accessibility: Open source, free, MIT-licensed
- ✅ Scope: Terminal AI coding agent — fits the category

**Verdict:** ADD to roster. Suggest Tier B (solid alternative, open-source, model-agnostic, but single-maintainer risk).

### Google AntiGravity CLI

| Attribute | Value |
|-----------|-------|
| Name | Google AntiGravity CLI |
| Type | CLI agent |
| License | Proprietary |
| Region | US |
| URL | — |

**What it is:** Google AntiGravity 2.0 (May 19, 2026) split the platform into four distinct products. The AntiGravity CLI replaces Gemini CLI on June 18, 2026. It is the terminal-first surface of the AntiGravity platform, running the same agent harness as the IDE.

**Relationship to existing roster:** Gemini CLI is already on the roster (Tier A). The AntiGravity CLI is essentially the next generation of the same product, but with significant architectural changes (multi-agent orchestration, 1M token context, built-in browser automation).

**Triage assessment:**
- This is an update/rebrand of an existing tool, not a new entrant
- The Gemini CLI page should be updated to note the AntiGravity CLI transition
- The AntiGravity CLI could be added as a separate entry if it diverges significantly

**Verdict:** UPDATE Gemini CLI page to note AntiGravity CLI transition. Do not add as separate entry unless the products diverge in capability.

### Kiro

| Attribute | Value |
|-----------|-------|
| Name | Kiro |
| Type | AI code editor |
| License | Unknown |
| Region | Unknown |

**What it is:** Agentic development for prototype to production. 5.0 rating, 11 reviews on Product Hunt. Very early stage with limited public information.

**Triage assessment:**
- ⚠️ Seriousness: Too early to tell — 11 reviews, limited public info
- ⚠️ Documentation: Minimal
- ❌ Accessibility: Unknown pricing/license

**Verdict:** WATCH LIST. Revisit in July 2026 edition. Do not add yet.

## Notable updates to existing roster tools

### Claude Code
- **Claude Opus 4.8** released May 28, 2026: 69.2% on SWE-Bench Pro (up from 64.3%)
- **Claude Opus 4.7** (April 2026): 87.6% on SWE-bench Verified — highest accuracy published in the industry
- **Pricing controversy**: Pro subscribers reported weekly caps dropping from 40-50 hours to 6-8 hours after Sonnet 4.6 release, without notice

### Cursor
- **Cursor 3** launched early 2026: vastly upgraded Composer agent, background agents, native MCP support
- **Pricing**: Heavy users report $40-50/mo on a $20 plan

### GitHub Copilot
- **Usage-based credits** moved from June 2026 — broke billing predictability
- **Copilot Workspace**: issue-to-PR workflow, runs CI and iterates until tests pass
- **Rubber Duck feature** (experimental, April 2026): second LLM reviews agent plans mid-execution

### OpenAI Codex
- **Codex 3.0**: launched February 2026, macOS app, "command center for agents"
- **April 2026 update**: background computer use, memory, in-app browser, 90+ new plugins, multiple terminal tabs, GitHub review comments, remote devboxes over SSH
- **Terminal-Bench 2.1**: 83.4% on GPT-5.5 (top score as of May 2026)

### Zed
- **Agent Client Protocol (ACP)** announced January 2026: enables external AI agents to work without being tied to a specific editor
- **Real-time collaboration**: CRDT-based multiplayer editing

## Watch list (revisit in July 2026)

| Tool | Why watching |
|------|-------------|
| Kiro | Too early, 11 reviews, need more data |
| Manus | Autonomous AI agent ($20/mo, 4,000 credits) — may fit agent framework category more than code editor |
| Claude Artifacts | Interactive applications in chat — more of a chat feature than an editor |

## Actions taken

1. ✅ Added **Oh-My-Pi (omp)** to roster as Tier B
2. ✅ Updated **Gemini CLI** page to note AntiGravity CLI transition
3. ✅ Updated **Claude Code** page with latest SWE-bench scores and pricing controversy
4. ✅ Updated **Cursor** page with Cursor 3 features
5. ✅ Updated **Copilot** page with usage-based credits and Rubber Duck feature
6. ✅ Updated **Codex CLI** page with Codex 3.0 and Terminal-Bench 2.1 score
7. ✅ Updated edition with new entrants section

## License

Content is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / Code Editors & IDE Assistants Almanac**.
