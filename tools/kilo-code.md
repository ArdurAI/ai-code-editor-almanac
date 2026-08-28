# Kilo Code

| Attribute | Value |
|-----------|-------|
| Tier | B |
| Type | Multi-platform agent |
| License | MIT (open source) |
| Region | Global |
| URL | https://github.com/Kilo-Org/kilocode |

## One-line summary

25K+ GitHub stars; a multi-platform open-source AI coding agent with 500+ model support, Architect/Code/Debug modes, and cross-IDE compatibility — combining the best of Cline and Roo Code.

## Architecture

Kilo Code is an open-source AI coding agent that builds on the Cline/Roo Code lineage while expanding platform support. Key architectural elements:

- **Multi-platform**: VS Code extension with planned support for additional platforms
- **500+ model support**: Broadest model provider support via OpenRouter, direct APIs, and local models
- **Multi-mode system**: Architect, Code, Debug, and custom modes (similar to Roo Code)
- **BYOK**: Full provider flexibility with no subscription
- **MCP integration**: Model Context Protocol support for external tools
- **Enhanced agent loop**: Improved over Cline's with better planning and sub-task delegation
- **Open source**: MIT license — most permissive option in the Cline ecosystem

## Key features

- 500+ model support (broadest in any coding agent)
- Multi-mode: Architect, Code, Debug + custom modes
- VS Code extension (multi-platform planned)
- MIT licensed — most permissive in the ecosystem
- BYOK with extensive provider support
- MCP integration for external tools
- Browser automation (from Cline heritage)
- Checkpoint/rollback system
- Active community development

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not run | Depends on model chosen |
| Latency | Not run | Depends on model provider |
| Token economics | Strong | BYOK; 500+ model options enable cost optimization |
| Scale behavior | Not run | Similar to Cline |
| Ops burden | Low | Extension install; configure API key |
| Developer experience | High | Polished VS Code integration |
| Data sovereignty | Strong | BYOK; local model support |

## Ops reality

**Setup burden:** Low — install from VS Code Marketplace; configure API key.

**Sharp edges:**
- As a newer fork, less battle-tested than Cline
- 500+ models sounds impressive but quality varies dramatically
- Competes directly with Cline and Roo Code — fragmentation risk
- Documentation less comprehensive than Cline's

## Cost model

- **Extension**: Free (MIT open source)
- **API costs**: BYOK — depends on model chosen (500+ options)
- **No subscription**: Pay only for API usage

## When to use / when to avoid

**Use when:**
- You want the broadest model support (500+)
- You need Architect/Code/Debug multi-mode workflow
- You prefer MIT license (most permissive)
- You want a blend of Cline and Roo Code features

**Avoid when:**
- You need the most battle-tested option (use Cline)
- You want the simplest setup (too many model options can be overwhelming)
- Stability is critical (newer project)

## Roster entry

- **Name:** Kilo Code
- **Type:** Multi-platform agent
- **License:** MIT (open source)
- **Region:** Global
- **Tier:** B
- **Notes:** 500+ models; Architect/Code/Debug modes

---

## Deep Analysis

### Daily monitoring update — 2026-08-28

- **Latest release:** `jetbrains/v7.1.0` (2026-08-27): Add the JetBrains Agent Manager beta for creating, opening, organizing, renaming, deleting, and tracking worktree-based tasks and their sessions from the IDE; Show Agent Manager worktree activity, changes, ahead/behind, pull request, failure, and attention badges with clearer row actions, menus, tooltips, and drag-and-drop reordering.
- **Adoption signal:** GitHub stars moved from 26,323 to 27,047 (+724). Track 27,047 as the current monitoring baseline because this crossed the >500 daily-change threshold.
- **Community health:** Open issues moved from 705 to 590 (-115). This is a material backlog reduction; it is a positive triage/maintenance signal, but verify whether it came from closures, migrations, or issue pruning.

### Daily monitoring update — 2026-07-17

- **Latest release:** `v7.4.11` (2026-07-16): Improves project-memory activity in VS Code with a task-header menu, quick actions, and optional verbose detail.

### Daily monitoring update — 2026-07-12

- **Latest release:** `jetbrains/v7.0.4` (2026-07-10): fixes Windows shutdown behavior by stopping orphaned Kilo Core processes when the IDE closes and improving JetBrains CLI shutdown ordering so the process tree is killed before streams close.

### Daily monitoring update — 2026-07-09

- **Latest release:** `v7.4.5` (2026-07-09): release notes list no notable user-facing changes; recorded as a version freshness marker only.

### 1. How Is This Tool Useful?

Kilo Code positions itself as the most flexible open-source AI coding agent, combining the best features of Cline and Roo Code while adding the broadest model support in the ecosystem. The 500+ model integration (via OpenRouter, direct APIs, and local model frameworks) means developers can choose the optimal model for each task — a cheap model for simple edits, a frontier model for complex reasoning, a local model for privacy-sensitive code. This flexibility is unmatched; even Aider, known for model-agnostic design, supports around 50 models.

The multi-mode system (Architect, Code, Debug, custom) provides workflow flexibility similar to Roo Code. Architect mode plans before executing — ideal for complex multi-file changes where understanding the full scope prevents mistakes. Code mode implements directly. Debug mode focuses on diagnosing and fixing issues. Custom modes let teams define specialized workflows. This is more structured than Cline's single-mode approach and helps developers choose the right approach for each task.

The MIT license is notable — it's more permissive than Cline and Roo Code's Apache-2.0. For commercial products that want to embed an AI coding agent, MIT removes attribution requirements and enables easier integration. While this matters more for commercial redistribution than for end-user adoption, it makes Kilo Code the most commercially friendly option in the open-source coding agent space.

### 2. Gotchas of Using This Tool

As a newer fork (created March 2025), Kilo Code is less battle-tested than Cline (July 2024). While it inherits Cline's codebase, the modifications and additions haven't been tested as extensively. Bugs, edge cases, and integration issues are more likely in a newer project. Teams adopting Kilo Code should expect a slightly rougher experience than Cline and should be prepared to contribute bug reports.

The 500+ model claim is technically accurate but practically misleading. Most of the 500+ models are accessed via OpenRouter and are of varying quality — many are small, niche, or experimental models that perform poorly on coding tasks. The practical choice set is similar to other tools: a dozen high-quality frontier and mid-tier models. The headline number is a marketing advantage more than a practical one. Developers should focus on the handful of models that actually perform well on coding tasks.

Fragmentation risk in the Cline ecosystem is real. Cline, Roo Code, and Kilo Code overlap significantly in functionality. Each project divides the community and development resources. If Kilo Code doesn't maintain momentum, it could be abandoned, leaving users to migrate. The MIT license helps (anyone can fork and maintain it), but community fragmentation benefits no one.

### 3. Limitations

- **Newer project**: Less battle-tested than Cline
- **Model quality variance**: 500+ models, but most are not coding-optimized
- **Documentation**: Less comprehensive than Cline's
- **Ecosystem fragmentation**: Competes with Cline and Roo Code
- **VS Code only**: No standalone IDE or JetBrains support (yet)
- **No inline completions**: Task-oriented, not completion-oriented
- **Community size**: Smaller than Cline's community

### 4. How Secure Is This Tool?

- **License**: MIT (fully open source; most permissive)
- **BYOK**: Code goes directly to your chosen provider
- **Local model support**: Ollama and LM Studio integration
- **Telemetry**: Minimal; no code sent to Kilo Code servers
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low — BYOK with local model option
- **Inherits Cline's security model**: Same permission system and safety features

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Kilo Code is a developer tool requiring VS Code, API key configuration, and coding knowledge. The 500+ model options add complexity for newcomers. Non-technical users cannot use it.

### 6. What Does This Tool Solve That Others Don't?

Kilo Code's unique advantages:

- **Broadest model support**: 500+ models via OpenRouter and direct APIs — most options of any agent
- **MIT license**: Most permissive license — best for commercial embedding
- **Multi-mode + multi-platform**: Combines Roo Code's modes with planned broader platform support
- **Cline + Roo Code fusion**: Attempts to merge the best of both forks

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | Cline | Most established; largest community | Single mode; Apache-2.0 |
| 2 | **Kilo Code** | 500+ models; MIT; multi-mode | Newer; less tested |
| 3 | Roo Code | Memory bank; custom modes | Repo archived |
| 4 | Continue | Completions + chat | No agent mode |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Active. [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) has **25,414 stars**, 2,837 forks, 801 open issues. Last pushed: July 2, 2026. Created March 2025 — rapid growth to 25K+ stars in ~15 months.

**Areas for improvement:**
- Battle-testing and stability improvements
- More comprehensive documentation
- Inline completion support
- Platform support beyond VS Code (JetBrains, Neovim)
- Better model recommendation engine (help users choose from 500+)
- Clearer differentiation from Cline and Roo Code
- Enterprise features

### 9. Official Maintainer Contacts

- **GitHub**: [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) — 25K+ stars
- **Discord**: Kilo Code Discord (link in GitHub README)
- **Docs**: Documentation in GitHub repository
- **VS Code Marketplace**: Kilo Code extension

### 10. General Usage Guidance

**Getting started:**
1. Install Kilo Code from VS Code Marketplace
2. Configure your API key (or OpenRouter for maximum model access)
3. Explore modes: Architect (plan first), Code (implement), Debug (fix issues)
4. Start with a well-known model (Claude Sonnet, GPT-4o)
5. Create custom modes for team workflows
6. Use MCP for external tool integration

**Best practices:**
- Don't be overwhelmed by 500+ models — stick to proven options
- Use Architect mode for complex tasks
- Create custom modes for repetitive workflows
- Configure MCP servers for external context
- Contribute bug reports — the project needs community testing
- Compare with Cline to choose the right tool for your needs

**When NOT to use:**
- If you need the most battle-tested option (use Cline)
- If model choice overwhelms you (use Cline with fewer, curated options)
- If you need inline completions
- If stability is critical and you can't afford to deal with a newer project's rough edges

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*

---

*Authored by Team Ardur · CC BY 4.0*
