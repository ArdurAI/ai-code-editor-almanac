# Cline


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | VS Code + CLI |
| License | Apache-2.0 |
| Region | Global |
| URL | https://github.com/cline/cline |

## One-line summary

Open-source VS Code extension with 5M+ installs, 64K+ GitHub stars; BYOK autonomous coding agent with native subagents, browser automation, and MCP support.

## Architecture

Cline is a VS Code extension that provides autonomous AI coding capabilities within the editor. Key architectural elements:

- **Agent loop**: Plans → executes → verifies tasks with file system and terminal access
- **BYOK (Bring Your Own Key)**: Supports Anthropic, OpenAI, Google, AWS Bedrock, Azure, OpenRouter, Ollama, LM Studio, and more
- **Subagents**: Native sub-agent spawning for parallel or delegated subtasks
- **Browser automation**: Can control a headless browser for testing, scraping, and web interaction
- **MCP integration**: Full Model Context Protocol support for external tools and data sources
- **Checkpoints**: Automatic workspace snapshots for safe rollback
- **Auto-approval**: Configurable auto-approve settings for file writes, terminal commands, and browser actions

## Key features

- 5M+ VS Code installs — most popular open-source AI coding extension
- BYOK with 20+ provider integrations (no subscription required)
- Native subagent support for complex task decomposition
- Browser automation (headless Chrome control)
- MCP client for extensible tool integration
- Checkpoint/rollback system for safe experimentation
- Plan/Act mode toggle for planning before executing
- Context mentions (@files, @folders, @problems)
- Open-source (Apache-2.0) with active community

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not run | Pending SWE-bench / Exercism |
| Latency | Not run | Depends on model provider chosen |
| Token economics | Strong | BYOK means you pay provider directly — no markup |
| Scale behavior | Not run | Handles large projects with file/folder mentions |
| Ops burden | Low | Extension install; configure API key |
| Developer experience | High | Polished VS Code integration |
| Data sovereignty | Strong | BYOK; can use local models (Ollama/LM Studio) |

## Ops reality

**Setup burden:** Low — install from VS Code Marketplace; configure API key.

**Sharp edges:**
- BYOK means costs scale directly with usage — no subscription cap
- Agent can consume significant tokens on complex tasks
- Auto-approval settings are powerful but risky if too permissive
- Browser automation can trigger security software
- Extension updates occasionally introduce breaking changes

## Cost model

- **Extension**: Free (Apache-2.0 open source)
- **API costs**: BYOK — you pay the model provider directly. Examples:
  - Claude Sonnet: ~$3/$15 per 1M tokens
  - GPT-4o: ~$2.50/$10 per 1M tokens
  - Local models (Ollama): Free
- **No subscription required**: Unlike Cursor/Copilot, no monthly fee beyond API costs

## When to use / when to avoid

**Use when:**
- You want open-source, BYOK AI coding with no subscription
- You need browser automation for web testing
- You want MCP integration and extensibility
- You use VS Code and want Cursor-like features for free

**Avoid when:**
- You want inline completions (Cline is task-oriented, not completion)
- You need enterprise support or SLAs
- Token cost unpredictability is a concern

## Roster entry

- **Name:** Cline
- **Type:** VS Code + CLI
- **License:** Apache-2.0
- **Region:** Global
- **Tier:** A
- **Notes:** 5M+ installs; 64K+ stars; native subagents; BYOK; browser automation

---

## Deep Analysis

### Daily monitoring update — 2026-07-17

- **Latest release:** `cli-v3.0.44` (2026-07-17): Improves max-output-token handling across gateway routing, OpenAI vendor paths, and reasoning providers; fixes UTF-8 BOM parsing for frontmatter and configuration files saved by Windows editors.

### Daily monitoring update — 2026-07-12

- **Latest release:** `v4.0.8` (2026-07-11): expands the GCP Vertex provider with additional models and adds a free-form model entry in the model dropdown for custom Vertex deployments.

### Daily monitoring update — 2026-07-09

- **Latest release:** `cli-v3.0.39` (2026-07-09): adds Cline free models in the ClinePass picker, removes the retired GLM 5.1 model, fixes OpenAI Codex metadata, makes `str_replace` diffs accurate, preserves canonical session history during compaction, and adds daemon/client telemetry identity updates.

### 1. How Is This Tool Useful?

Cline has become the dominant open-source AI coding agent for VS Code, with 5M+ installs and 64K+ GitHub stars. Its primary value is providing Cursor-like agentic coding capabilities without the subscription — you bring your own API key and pay the model provider directly. This makes it the go-to choice for developers who want autonomous AI coding without vendor lock-in or monthly fees. The agent loop is capable: given a task, Cline reads relevant files, makes changes, runs commands, verifies results, and iterates until the task is complete.

The browser automation feature sets Cline apart from most competitors. The agent can control a headless Chrome instance to test web applications, scrape documentation, fill out forms, or interact with web-based tools. This is invaluable for full-stack development where you need to verify that frontend changes work correctly, or for tasks like "test the login flow and fix any issues." Combined with the file system and terminal access, Cline can handle end-to-end development tasks that span code, build, and test.

The BYOK model with 20+ provider integrations means developers have maximum flexibility. You can use Claude for complex reasoning tasks, GPT-4o for speed, local models (Ollama, LM Studio) for privacy-sensitive work, or specialized providers via OpenRouter. The MCP integration extends this further — connecting Cline to databases, issue trackers, documentation systems, and custom internal tools. For teams that want full control over their AI stack, Cline provides the most flexible foundation.

### 2. Gotchas of Using This Tool

BYOK cost unpredictability is the biggest concern. Unlike subscription tools with monthly caps, Cline's costs scale directly with token usage. A complex multi-file task with multiple iterations can consume $5–20+ in API costs. Developers new to agentic coding are often surprised by how quickly costs accumulate. There's no built-in spending cap — you must set limits at the API provider level.

The auto-approval system is a double-edged sword. Enabling auto-approve for file writes and terminal commands makes Cline more autonomous and faster, but it also means the agent can make destructive changes without confirmation. Stories of Cline accidentally deleting files or running harmful commands (e.g., `rm -rf` on wrong directories) circulate in the community. Best practice is to start with manual approval for everything, then selectively auto-approve as you build trust.

Extension updates can introduce breaking changes. Cline's rapid development pace (multiple releases per week) means settings, APIs, and behavior can change between versions. Some users pin to specific versions for stability. The fork ecosystem (Roo Code, Kilo Code) exists partly because of disagreements about Cline's direction.

### 3. Limitations

- **No inline completions**: Cline is task-oriented, not completion-oriented
- **Token costs**: BYOK means no spending cap; complex tasks can be expensive
- **VS Code only**: No standalone IDE or support for JetBrains/Neovim
- **Context window**: Limited by underlying model's context window
- **Agent reliability**: Capable but can make errors on complex tasks; requires human review
- **No enterprise tier**: No SSO, audit logs, or admin controls out of the box
- **Community support only**: No professional support SLA

### 4. How Secure Is This Tool?

- **License**: Apache-2.0 (fully open source; auditable code)
- **BYOK**: Your code goes directly to your chosen model provider — Cline doesn't intermediate
- **Local model support**: Can use Ollama/LM Studio for fully local, offline operation
- **Telemetry**: Minimal; no code sent to Cline's servers
- **Auto-approval risk**: Misconfigured auto-approve can lead to destructive actions
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low — BYOK means you control where data goes; local models eliminate external exposure
- **MCP servers**: Security depends on the MCP servers you connect — audit each one

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Cline is a developer tool requiring VS Code, API key configuration, and coding knowledge. Non-technical users cannot use it. The BYOK requirement (setting up API keys with model providers) adds an additional barrier even for developers compared to subscription-based tools.

### 6. What Does This Tool Solve That Others Don't?

Cline's unique advantages:

- **Open-source agentic coding in VS Code**: The most popular free, open-source AI agent for VS Code
- **Browser automation**: Built-in headless Chrome control for web testing — rare among coding agents
- **Maximum BYOK flexibility**: 20+ providers including local models — no other tool matches this range
- **No subscription**: Pay only for API usage; no monthly fee beyond provider costs
- **Checkpoint/rollback**: Built-in safety net for experimental changes
- **MCP native**: Full MCP support makes it the most extensible open-source agent

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | **Cline** | Open-source; BYOK; browser automation | No completions; VS Code only |
| 2 | Roo Code | Cline fork with enhanced modes | Fork; smaller community |
| 3 | Continue | Open-source; completions + chat | Less capable agent mode |
| 4 | Aider | Git-native terminal tool | Terminal-only; less polished |

Cline is the top-ranked open-source VS Code agent by installs and stars.

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Very active. [cline/cline](https://github.com/cline/cline) has **64,218 stars**, 6,822 forks, 1,191 open issues. Last pushed: July 2, 2026 (daily updates). Created July 2024 — explosive 2-year growth.

**Areas for improvement:**
- Inline completion support (currently task-only)
- Built-in spending caps or budget warnings
- Support for JetBrains and other IDEs
- Enterprise features (SSO, audit logs)
- Better default safety for auto-approval settings
- Improved agent reliability on complex multi-step tasks
- Stability guarantees between releases

### 9. Official Maintainer Contacts

- **GitHub**: [cline/cline](https://github.com/cline/cline) — issues, discussions, PRs
- **Creator**: Cline (https://github.com/cline)
- **Discord**: Cline Discord community (link in GitHub README)
- **Twitter/X**: [@cline](https://twitter.com/cline)
- **Marketplace**: VS Code Marketplace (Cline extension)
- **Docs**: https://docs.cline.bot (community docs)

### 10. General Usage Guidance

**Getting started:**
1. Install Cline from VS Code Marketplace
2. Configure your API key (Anthropic, OpenAI, OpenRouter, etc.)
3. Open Cline panel in VS Code (sidebar icon)
4. Start with simple tasks ("add a comment to this function")
5. Use Plan mode to preview before executing
6. Gradually enable auto-approval for trusted operations

**Best practices:**
- Start with manual approval for all actions
- Use checkpoints before major changes
- Set spending limits at your API provider level
- Use @mentions to scope context precisely
- Enable browser automation only when needed
- Connect MCP servers for external context
- Pin extension version if stability is critical

**When NOT to use:**
- If you need inline completions (use Copilot, Continue, or Cursor)
- If you need enterprise support or SLAs
- If VS Code is not your editor
- If you want a subscription model with spending caps

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*

---

*Authored by Team Ardur · CC BY 4.0*
