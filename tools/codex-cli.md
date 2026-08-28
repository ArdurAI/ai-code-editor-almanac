# Codex CLI


[![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | CLI agent |
| License | Apache-2.0 |
| Region | US |
| URL | https://github.com/openai/codex |

## One-line summary

OpenAI's open-source CLI coding agent; 99K+ GitHub stars; Rust-native with sandboxed execution; included in ChatGPT subscriptions; 240+ tok/s streaming.

## Architecture

Codex CLI is OpenAI's terminal-native AI coding agent, written in Rust. Key architectural elements:

- **Rust-native**: Built in Rust for performance and safety; fast startup and low memory footprint
- **Sandboxed execution**: Runs commands in a sandboxed environment for safety
- **Model integration**: Powered by OpenAI models (GPT-4.1, o3, o4-mini); included in ChatGPT subscriptions
- **Agent loop**: Plans, executes code changes, runs tests, and iterates
- **Terminal-native**: No IDE required; works in any terminal
- **Approval system**: Configurable auto-approval for safe operations
- **Multi-platform**: macOS, Linux, Windows

## Key features

- Rust-native performance (fast startup, low resource usage)
- Sandboxed command execution for safety
- Included in ChatGPT Plus/Pro/Team/Enterprise subscriptions
- 240+ tokens/sec streaming output
- Plan and execute modes
- Git-aware workflow
- Multi-file editing with terminal access
- Configurable approval system
- MCP support for external tools

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Strong | SWE-bench: 69.1% (codex-20250617) |
| Latency | High | 240+ tok/s streaming; fast startup |
| Token economics | Strong | Included in ChatGPT subscription |
| Scale behavior | Not run | Sandboxed execution handles complex tasks |
| Ops burden | Low | npm/brew install; ChatGPT auth |
| Developer experience | High | Clean CLI; fast responses |
| Data sovereignty | Partial | OpenAI processes data; enterprise DPA available |

## Ops reality

**Setup burden:** Low — `npm install -g @openai/codex` or `brew install codex`; authenticate with ChatGPT account.

**Sharp edges:**
- OpenAI model lock-in (only works with OpenAI models)
- Sandbox can prevent necessary operations; requires approval tuning
- Agent loop is less mature than Claude Code's
- ChatGPT subscription rate limits apply

## Cost model

| Plan | Price | Codex CLI access |
|------|-------|-----------------|
| ChatGPT Free | $0 | Limited Codex usage |
| ChatGPT Plus | $20/mo | Included with rate limits |
| ChatGPT Pro | $200/mo | Higher rate limits |
| API | Pay-per-token | GPT-4.1: $2/$8 per M tokens; o3: custom |
| Enterprise | Custom | Custom rate limits, DPA |

## When to use / when to avoid

**Use when:**
- You have a ChatGPT subscription and want CLI coding included
- You want a fast, Rust-native CLI agent
- You prefer OpenAI models (GPT, o-series)

**Avoid when:**
- You need multi-model support (Claude, Gemini)
- You want the most capable agentic coding (Claude Code is stronger)
- You require fully open-source models (not just open-source agent)

## Roster entry

- **Name:** Codex CLI
- **Type:** CLI agent
- **License:** Apache-2.0
- **Region:** US
- **Tier:** A
- **Notes:** OpenAI; Rust-native; 240+ tok/s; included in ChatGPT

---

## Deep Analysis

### Daily monitoring update — 2026-08-28

- **Latest release:** `rust-v0.150.1` (2026-08-27): Bug Fixes; Remote compaction now counts retained images toward its token budget by default, trimming older images as needed. (#41003); 41003 Backport retained-image compaction budgeting to 0.150 @rhan-oai.
- **Adoption signal:** GitHub stars moved from 98,990 to 119,255 (+20265). Track 119,255 as the current monitoring baseline because this crossed the >500 daily-change threshold.
- **Community health:** Open issues moved from 9,885 to 14,149 (+4264). This is a material backlog increase; watch maintainer triage capacity, support load, and regression risk.

### Daily monitoring update — 2026-07-17

- **Latest release:** `rust-v0.144.5` (2026-07-16): Hardens dangerous-command detection, including more forced `rm` forms, and returns clearer rejection reasons when commands are denied.
- **Adoption signal:** GitHub stars moved from 97,250 to 98,990 (+1,740). Track 98,990 as the current monitoring baseline because this crossed the >500 daily-change threshold.
- **Community health:** Open issues moved from 9,013 to 9,885 (+872). This is a material backlog increase; watch maintainer triage capacity, support load, and regression risk.

### Daily monitoring update — 2026-07-12

- **Community health:** Open issues increased from 8,764 to 9,013 (+249). This is a material backlog expansion; monitor installer, sandbox, and code-mode regressions plus maintainer triage velocity.

### Daily monitoring update — 2026-07-10

- **Latest release:** `rust-v0.144.1` (2026-07-09): bugfix release for standalone installer robustness when GitHub returns compact/reordered release metadata, macOS package exposure of the code-mode host, and code-mode fallback to the embedded runtime when the companion host binary is unavailable.
- **Community health:** Open issues increased from 8,561 to 8,764 (+203). This is a material backlog expansion; monitor installer/code-mode regressions and maintainer triage velocity.

### Daily monitoring update — 2026-07-09

- **Latest release:** `rust-v0.143.0` (2026-07-08): enables remote plugins by default with richer catalog/npm marketplace metadata, adds macOS/Windows system-proxy routing for auth and Responses API traffic, adds manual daemon pairing, expands Bedrock model support, and improves MCP/session-auth behavior.
- **Adoption signal:** GitHub stars moved from 95,494 to 96,550 (+1,056). Star references in this file now use the new 96,550 baseline.
- **Community health:** Open issues increased from 8,194 to 8,561 (+367). This is a material backlog increase; monitor regression volume and maintainer response time.

### 1. How Is This Tool Useful?

Codex CLI represents OpenAI's entry into the terminal-native agentic coding space, and its inclusion in ChatGPT subscriptions makes it the most accessible CLI agent for the millions of existing ChatGPT subscribers. If you already pay $20/month for ChatGPT Plus, you get a capable CLI coding agent at no additional cost — a compelling value proposition compared to paying per-token API rates for Claude Code or other agents.

The Rust-native implementation gives Codex CLI a performance edge. Fast startup, low memory usage, and 240+ tokens/second streaming make the interaction feel snappy and responsive. For developers who value terminal performance (and who doesn't?), Codex CLI's resource efficiency is notable. The sandboxed execution model provides a safety layer that prevents accidental damage — commands run in an isolated environment that limits file system and network access unless explicitly approved.

For OpenAI ecosystem developers, Codex CLI is the natural choice. It integrates seamlessly with ChatGPT authentication (no separate API key needed for subscribers), supports the latest OpenAI models (GPT-4.1, o3, o4-mini), and benefits from OpenAI's infrastructure reliability. The plan/execute mode separation is well-designed — you can review the plan before execution, adding a layer of human oversight to autonomous operations.

### 2. Gotchas of Using This Tool

OpenAI model lock-in is the primary limitation. Codex CLI only works with OpenAI models — there's no Claude, Gemini, or local model support. For developers who prefer Claude's coding capabilities (which benchmark higher on SWE-bench) or want local model privacy, Codex CLI is not an option. This contrasts sharply with model-agnostic tools like Aider or Cline.

The agent loop is less mature than Claude Code's. While Codex CLI can handle multi-step tasks, its reliability on complex refactors and large-scale changes trails Claude Code's Agent Teams. Users report that Codex CLI sometimes gets stuck in loops, makes redundant changes, or fails to complete complex tasks that Claude Code handles. The gap is closing as OpenAI iterates, but as of mid-2026, Claude Code remains the capability leader.

Sandbox restrictions can be frustrating. The sandboxed execution environment, while safer, sometimes prevents necessary operations — like writing to certain directories, making network requests, or running system commands. Tuning the approval system to balance safety and capability requires trial and error. Some developers disable the sandbox entirely, which defeats its purpose.

### 3. Limitations

- **OpenAI-only**: No multi-model support — a significant limitation vs. Aider/Cline
- **Agent maturity**: Less capable than Claude Code on complex multi-step tasks
- **Sandbox friction**: Safety sandbox can prevent necessary operations
- **Rate limits**: ChatGPT subscription rate limits apply; heavy usage can hit caps
- **Context window**: Limited by OpenAI model context (typically 128K–200K tokens)
- **No IDE integration**: Terminal-only (can run from VS Code terminal but no extension)
- **Relatively new**: Launched April 2025; less battle-tested than Aider (2023)

### 4. How Secure Is This Tool?

- **Sandboxed execution**: Commands run in isolated environment — strong safety default
- **SOC 2 Type II**: Certified (OpenAI)
- **GDPR**: Compliant
- **Data retention**: API data retained for 30 days (Enterprise: zero retention)
- **Approval system**: Configurable auto-approve for file changes and commands
- **Encryption**: TLS in transit, AES-256 at rest
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Moderate — code sent to OpenAI's API for processing
- **Enterprise**: DPA available; custom data processing terms

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Codex CLI is a developer tool requiring terminal knowledge and coding expertise. However, the ChatGPT authentication (no separate API key setup) slightly lowers the barrier for existing ChatGPT users who are developers.

### 6. What Does This Tool Solve That Others Don't?

Codex CLI's unique advantages:

- **Included in ChatGPT**: No additional cost for existing subscribers — most accessible CLI agent
- **Rust-native performance**: Fastest startup and lowest resource usage among CLI agents
- **OpenAI model integration**: Best integration with GPT/o-series models and OpenAI infrastructure
- **Sandboxed execution**: Built-in safety layer not present in Claude Code or Aider
- **240+ tok/s streaming**: Fastest output streaming in the category

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | Claude Code | Best agentic coding; MCP; Agent Teams | Claude-only; expensive |
| 2 | **Codex CLI** | ChatGPT-included; Rust-fast; sandboxed | OpenAI-only; less mature agent |
| 3 | Gemini CLI | Free tier; 1M context | Weaker coding performance |
| 4 | Aider | Git-native; 50+ models | Terminal-only; no agent loop |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Extremely active. [openai/codex](https://github.com/openai/codex) has **98,990 stars**, 14,105 forks, 9,885 open issues. Last pushed: July 17, 2026. Created April 2025 — explosive growth (99K stars in ~14 months).

**Areas for improvement:**
- Multi-model support (Claude, Gemini, local models)
- Stronger agent loop reliability for complex tasks
- Better sandbox tuning options
- IDE integration (VS Code extension)
- More transparent rate limit communication for ChatGPT subscribers
- MCP extensibility (currently limited)
- Better failure recovery for mid-task interruptions

### 9. Official Maintainer Contacts

- **Company**: OpenAI — https://openai.com
- **GitHub**: [openai/codex](https://github.com/openai/codex) — 99K+ stars
- **Twitter/X**: [@OpenAI](https://twitter.com/OpenAI), [@OpenAIDevs](https://twitter.com/OpenAIDevs)
- **Discord**: OpenAI Developer Community
- **Docs**: https://github.com/openai/codex#readme
- **Support**: via OpenAI Help Center (ChatGPT subscribers)

### 10. General Usage Guidance

**Getting started:**
1. Install: `npm install -g @openai/codex` (or `brew install codex`)
2. Authenticate: `codex login` (uses ChatGPT account)
3. Navigate to project: `cd my-project`
4. Run: `codex` to start interactive mode
5. Describe your task in natural language
6. Review proposed changes and approve

**Best practices:**
- Use Plan mode for complex tasks — review before executing
- Configure approval settings for your comfort level
- Work in a git branch for safe rollback
- Monitor ChatGPT rate limit usage
- Use specific, well-scoped task descriptions
- Review all changes with `git diff` before committing

**When NOT to use:**
- If you need Claude or Gemini models (use Claude Code or Gemini CLI)
- If you need the most capable agentic coding (use Claude Code)
- If you need local model support (use Aider or Cline)
- If you don't have a ChatGPT subscription and API costs are a concern

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*

---

*Authored by Team Ardur · CC BY 4.0*
