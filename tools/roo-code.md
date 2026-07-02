# Roo Code

| Attribute | Value |
|-----------|-------|
| Tier | B |
| Type | VS Code extension |
| License | Apache-2.0 (open source) |
| Region | Global |
| URL | https://github.com/RooCodeInc/Roo-Code |

## One-line summary

24K+ GitHub stars; a popular Cline fork with enhanced multi-mode agent loop, custom modes, memory bank, and community-driven development — the most customizable VS Code AI agent.

## Architecture

Roo Code (formerly "Roo Cline") is a fork of Cline with significant enhancements. Key architectural elements:

- **Multi-mode system**: Architect, Code, Ask, Debug, and custom modes — each with specific behaviors and tool access
- **Custom modes**: User-defined modes with custom instructions, tool permissions, and model preferences
- **Memory bank**: Persistent project context that accumulates across sessions
- **Enhanced agent loop**: Improved planning, execution, and verification compared to Cline
- **BYOK**: Same multi-provider support as Cline (Anthropic, OpenAI, Google, local models)
- **Browser automation**: Retained from Cline; headless Chrome control
- **MCP integration**: Full Model Context Protocol support
- **Boomerang pattern**: Tasks can be thrown out and return with results (sub-task delegation)

## Key features

- Multi-mode agent (Architect, Code, Ask, Debug + custom modes)
- Custom modes with user-defined instructions and permissions
- Memory bank for persistent project context
- Enhanced sub-task delegation (Boomerang pattern)
- BYOK with 20+ providers (same as Cline)
- Browser automation (headless Chrome)
- MCP support for external tools
- Checkpoint/rollback system
- Community-driven with frequent updates
- Open source (Apache-2.0)

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not run | Depends on model chosen |
| Latency | Not run | Depends on model provider |
| Token economics | Strong | BYOK; Architect mode optimizes costs |
| Scale behavior | Not run | Memory bank helps with large projects |
| Ops burden | Low | Extension install; configure API key |
| Developer experience | High | Enhanced UX over Cline |
| Data sovereignty | Strong | BYOK; local model support |

## Ops reality

**Setup burden:** Low — install from VS Code Marketplace; configure API key.

**Sharp edges:**
- As a fork, may diverge from Cline's updates
- More configuration options mean more complexity
- Memory bank requires management to avoid stale context
- Archived main repo as of May 2026 (development may have shifted)

## Cost model

- **Extension**: Free (Apache-2.0 open source)
- **API costs**: BYOK — same as Cline (provider costs)
- **No subscription**: Free extension; pay only for API usage

## When to use / when to avoid

**Use when:**
- You want Cline's features with more customization
- Custom modes and memory bank are valuable
- You prefer community-driven development
- You need enhanced multi-mode workflows

**Avoid when:**
- You want the most mainstream/supported option (use Cline)
- You need stability over features (Cline is more stable)
- You're concerned about fork divergence and maintenance

## Roster entry

- **Name:** Roo Code
- **Type:** VS Code extension
- **License:** Apache-2.0 (open source)
- **Region:** Global
- **Tier:** B
- **Notes:** Cline fork; multi-mode agent loop; community-driven

---

## Deep Analysis

### 1. How Is This Tool Useful?

Roo Code emerged from the Cline community as an enhanced fork that addresses power-user needs. The multi-mode system is the defining feature: rather than a single agent mode, Roo Code offers Architect (plans before executing), Code (direct implementation), Ask (read-only Q&A), Debug (focus on diagnosing issues), and critically, custom modes that users can define. A team could create a "Security Review" mode with specific instructions, a "Documentation" mode that only writes docs, or a "Test Generation" mode that creates comprehensive test suites. This flexibility makes Roo Code more adaptable to team workflows than Cline's single-mode approach.

The memory bank is a significant innovation for long-running projects. While Cline and most agents reset context between sessions, Roo Code's memory bank accumulates project knowledge — architecture decisions, conventions, patterns, and context — across sessions. This means when you start a new session, the agent already "knows" your project structure and conventions without you re-explaining. For complex, ongoing projects, this dramatically reduces the context-setting overhead that plagues session-based agents.

The enhanced Boomerang sub-task delegation pattern allows complex tasks to be broken into smaller sub-tasks, each delegated to a sub-agent, with results "boomeranging" back to the orchestrator. This is more sophisticated than Cline's subagent support and enables handling of genuinely complex, multi-part development tasks. For example, "refactor the authentication system" can be decomposed into: analyze current auth, design new approach, update models, update controllers, update tests, verify — each as a delegated sub-task.

### 2. Gotchas of Using This Tool

The main Roo Code repo (RooCodeInc/Roo-Code) shows as archived on GitHub (archived as of May 2026). This is a significant concern — it suggests the project may have been reorganized, merged back into another project, or development may have stalled. Users should verify the current state of the project before adopting. The fork ecosystem is volatile; projects can be abandoned or merged unpredictably.

As a Cline fork, Roo Code may diverge from Cline's updates. When Cline adds new features or fixes bugs, Roo Code must manually port those changes. This creates a maintenance lag and potential compatibility issues. Conversely, Roo Code's unique features (custom modes, memory bank) may not be available in Cline. Choosing between them requires understanding which features matter most and which project is more actively maintained.

More configuration options mean more complexity. While power users love the customization, less technical developers may find the options overwhelming. The custom mode system, while powerful, requires understanding Roo Code's configuration model to use effectively. Teams adopting Roo Code should document their mode configurations and share them for consistency.

### 3. Limitations

- **Repo archived**: Main repo archived as of May 2026 — verify current status before adoption
- **Fork divergence**: May lag behind Cline updates
- **Complexity**: More options mean steeper learning curve
- **Memory bank management**: Requires periodic cleanup to avoid stale context
- **VS Code only**: No standalone IDE or JetBrains support
- **No inline completions**: Task-oriented, not completion-oriented
- **Community support**: Smaller community than Cline; fewer resources

### 4. How Secure Is This Tool?

- **License**: Apache-2.0 (fully open source; auditable)
- **BYOK**: Code goes directly to your chosen provider
- **Local model support**: Ollama integration for fully local operation
- **Telemetry**: Minimal; no code sent to Roo Code servers
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low — BYOK with local model option
- **Inherits Cline's security model**: Same permission system and safety features

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Roo Code is a developer tool requiring VS Code, API key configuration, and coding knowledge. The additional complexity of custom modes and memory bank makes it even more developer-focused than Cline. Non-technical users cannot use it.

### 6. What Does This Tool Solve That Others Don't?

Roo Code's unique advantages:

- **Custom modes**: User-defined agent modes with specific instructions and permissions — most flexible mode system
- **Memory bank**: Persistent cross-session context — solves the "re-explaining your project" problem
- **Boomerang sub-tasks**: Sophisticated sub-task delegation pattern for complex work
- **Enhanced planning**: Architect mode provides better upfront planning than Cline
- **Community-driven**: More responsive to community feature requests than Cline

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | Cline | Main project; most stable | Less customizable |
| 2 | **Roo Code** | Custom modes; memory bank | Fork; repo archived |
| 3 | Kilo Code | 500+ models; multi-platform | Fork; newer |
| 4 | Continue | Completions + chat | No agent mode |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: The main repo [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) has **24,300 stars**, 3,349 forks, 1,036 open issues. **Last pushed: May 15, 2026**. The repo appears archived — development status uncertain. Verify current state before adoption.

**Areas for improvement:**
- Clarify project status (archived repo is concerning)
- Port latest Cline improvements if development continues
- Better documentation for custom mode creation
- Memory bank management tools (cleanup, export/import)
- IDE support beyond VS Code
- Inline completion support
- Community governance for long-term sustainability

### 9. Official Maintainer Contacts

- **GitHub**: [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) — 24K+ stars (verify status)
- **Discord**: Roo Code Discord community (link in GitHub README)
- **Docs**: Community documentation in GitHub wiki
- **VS Code Marketplace**: Roo Code extension

### 10. General Usage Guidance

**Getting started:**
1. **Verify project status first** — check if the repo is still active
2. Install Roo Code from VS Code Marketplace
3. Configure your API key (same as Cline)
4. Explore built-in modes (Architect, Code, Ask, Debug)
5. Create custom modes for your team workflows
6. Use the memory bank for long-running projects

**Best practices:**
- Start with built-in modes before creating custom ones
- Document custom mode configurations for team consistency
- Periodically clean up the memory bank
- Use Architect mode for complex tasks — review plans before execution
- Configure Boomerang sub-tasks for multi-part work
- Pin extension version if stability is critical
- Have a migration plan in case the project is abandoned

**When NOT to use:**
- If the repo remains archived (project may be abandoned)
- If you need maximum stability (use Cline)
- If you need inline completions
- If VS Code is not your editor

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
