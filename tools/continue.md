# Continue

| Attribute | Value |
|-----------|-------|
| Tier | A |
| Type | IDE extension |
| License | Apache-2.0 |
| Region | Global |
| URL | https://continue.dev |

## One-line summary

35K+ GitHub stars; the leading open-source AI code assistant extension for VS Code and JetBrains with BYOK, codebase chat, inline completions, and configurable code review.

## Architecture

Continue is an open-source extension for VS Code and JetBrains IDEs that provides AI coding assistance. Key architectural elements:

- **Config-driven**: All behavior defined in `config.yaml` — models, providers, slash commands, context providers
- **BYOK**: Supports any LLM provider (OpenAI, Anthropic, Google, local models via Ollama, custom endpoints)
- **Codebase indexing**: Embeds project files for semantic search and retrieval
- **Inline completions**: Ghost-text style completions (configurable model)
- **Chat**: Conversational interface with codebase, file, and documentation context
- **Tab autocomplete**: Configurable autocomplete model (local or cloud)
- **Slash commands**: Custom workflows defined in config (e.g., /review, /test, /explain)
- **Code review**: CI-enforceable code review checks configurable per project

## Key features

- Open-source (Apache-2.0) for VS Code and JetBrains
- BYOK with full provider flexibility
- Inline completions + chat + codebase search in one extension
- Configurable slash commands for custom workflows
- Codebase embedding and semantic retrieval
- Local model support (Ollama, LM Studio)
- MCP support for external tool integration
- Code review automation (CI-enforceable)
- Custom context providers

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not run | Depends on model chosen |
| Latency | Not run | Local models enable sub-100ms completions |
| Token economics | Strong | BYOK with no markup; local models are free |
| Scale behavior | Not run | Codebase indexing handles large projects |
| Ops burden | Low | Extension install; config.yaml setup |
| Developer experience | High | Works in existing IDE |
| Data sovereignty | Strong | BYOK; local model support |

## Ops reality

**Setup burden:** Low — install extension; configure config.yaml with API keys.

**Sharp edges:**
- Configuration is YAML-based — powerful but has a learning curve
- Completion quality depends heavily on model choice
- Codebase indexing can consume resources on large projects
- JetBrains support is less mature than VS Code support
- No built-in agent mode (unlike Cline) — focus is on completion + chat

## Cost model

- **Extension**: Free (Apache-2.0 open source)
- **API costs**: BYOK — depends on model chosen
- **Local models**: Free (Ollama, LM Studio)
- **Continue Hub**: Optional team features (model sharing, config sync) — freemium

## When to use / when to avoid

**Use when:**
- You want open-source AI assistance in VS Code or JetBrains
- You need BYOK with full provider control
- You want inline completions AND chat in one extension
- You need configurable code review workflows

**Avoid when:**
- You need autonomous agent mode (use Cline or Claude Code)
- You want a polished out-of-box experience without configuration
- You need the most advanced completion quality (use Cursor or Copilot)

## Roster entry

- **Name:** Continue
- **Type:** IDE extension
- **License:** Apache-2.0
- **Region:** Global
- **Tier:** A
- **Notes:** 35K+ stars; BYOK; code review; CI-enforceable checks

---

## Deep Analysis

### 1. How Is This Tool Useful?

Continue fills a unique niche: open-source AI coding assistance that works within your existing IDE (VS Code or JetBrains) without requiring a separate editor or subscription. For teams that have standardized on VS Code or IntelliJ and want AI assistance without vendor lock-in, Continue is the most mature option. It provides the full trifecta — inline completions, codebase-aware chat, and configurable workflows — all configurable via a single YAML file.

The config-driven architecture is both powerful and developer-friendly. Every aspect of Continue's behavior — which models to use for chat vs. completions, what context providers to enable, what slash commands to define — is declared in `config.yaml`. This makes Continue highly adaptable: a team can configure `/review` to run a custom code review workflow using their preferred model, `/test` to generate tests with project-specific conventions, and `/explain` to provide architectural overviews. This level of customization is unmatched by subscription tools.

The codebase indexing and semantic search feature gives Continue's chat accurate awareness of project structure. Unlike basic chat that only sees the current file, Continue can search across the entire codebase to answer questions like "where is the authentication middleware?" or "which components use this API?" This makes it valuable for onboarding to new codebases and for understanding large, complex projects.

### 2. Gotchas of Using This Tool

The YAML configuration has a learning curve. While powerful, `config.yaml` requires understanding Continue's configuration schema, provider formats, and context provider APIs. New users often struggle with the initial setup — configuring models, setting up embeddings for codebase indexing, and defining slash commands. The documentation is good but the sheer flexibility can be overwhelming. This contrasts with tools like Copilot or Cursor that work immediately with zero configuration.

Completion quality depends entirely on model choice. Continue doesn't have a proprietary completion engine (unlike Cursor Tab or Copilot). It relies on whatever model you configure for completions — and if you use a general-purpose chat model for completions, the latency and quality will be poor. Getting good completions requires configuring a specialized completion model (like DeepSeek-Coder, StarCoder, or a local model optimized for completion), which adds complexity.

No agent mode is a significant limitation compared to Cline. Continue focuses on completions and chat — it cannot autonomously make multi-file changes, run terminal commands, or execute complex development tasks. If you need agentic capabilities, you'd use Continue alongside Cline or Claude Code, not as a replacement.

### 3. Limitations

- **No agent mode**: Cannot autonomously execute multi-step development tasks
- **Configuration complexity**: YAML config is powerful but has a learning curve
- **Completion quality**: Depends entirely on model choice — no proprietary completion engine
- **JetBrains support**: Less mature than VS Code support
- **Codebase indexing**: Resource-intensive on large projects; embedding generation can be slow
- **No enterprise tier**: No SSO, audit logs, or admin controls (Continue Hub offers some team features)

### 4. How Secure Is This Tool?

- **License**: Apache-2.0 (fully open source; auditable)
- **BYOK**: Code goes directly to your configured provider; Continue doesn't intermediate
- **Local model support**: Ollama/LM Studio for fully local, offline operation
- **Telemetry**: Minimal; anonymous usage data opt-in
- **Config file**: API keys stored locally in config.yaml — ensure proper file permissions
- **Known CVEs**: No major security advisories as of mid-2026
- **Code exfiltration risk**: Low with local models; moderate with cloud providers (you control which)
- **Continue Hub**: Team features may involve data sharing; review privacy policy

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 1/10**

Continue is a developer tool requiring IDE knowledge, API key configuration, and understanding of YAML configuration. Non-technical users cannot use it. The configuration requirement adds a higher barrier than plug-and-play tools like Copilot.

### 6. What Does This Tool Solve That Others Don't?

Continue's unique advantages:

- **Config-driven customization**: YAML configuration enables deep customization of AI behavior — no other tool matches this flexibility
- **VS Code + JetBrains**: One of the few open-source tools supporting both major IDE families
- **Completions + chat + review**: Full-featured combination without requiring multiple tools
- **CI-enforceable code review**: Custom review checks that can run in CI pipelines
- **Local model optimization**: Best-in-class support for local models (Ollama) for fully private AI assistance

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Key Advantage | Key Disadvantage |
|------|------|--------------|-----------------|
| 1 | **Continue** | Open-source; config-driven; multi-IDE | No agent mode; setup complexity |
| 2 | Cline | Open-source agent mode | No completions |
| 3 | GitHub Copilot | Polished; zero config | Proprietary; subscription |
| 4 | Cody | Codebase awareness at scale | Proprietary; Sourcegraph dependency |

### 8. How Can This Tool Be Improved? How Active Is Development?

**Development activity**: Very active. [continuedev/continue](https://github.com/continuedev/continue) has **34,647 stars**, 4,930 forks, 976 open issues. Last pushed: July 1, 2026. Created May 2023.

**Areas for improvement:**
- Agent mode (the biggest gap vs. Cline and Cursor)
- Simplified onboarding (zero-config mode for new users)
- Better JetBrains parity with VS Code features
- Improved completion quality with optimized default models
- Better codebase indexing performance on large projects
- Enterprise features (SSO, audit logs)

### 9. Official Maintainer Contacts

- **GitHub**: [continuedev/continue](https://github.com/continuedev/continue)
- **Company**: Continue Dev, Inc.
- **Discord**: Continue Discord (link in GitHub README)
- **Twitter/X**: [@continuedev](https://twitter.com/continuedev)
- **Docs**: https://docs.continue.dev
- **Email**: team@continue.dev

### 10. General Usage Guidance

**Getting started:**
1. Install Continue extension from VS Code Marketplace or JetBrains plugin repository
2. Open Continue config (gear icon in Continue sidebar)
3. Add your model provider and API key to config.yaml
4. Start chatting in the Continue panel
5. Enable tab autocomplete (configure a completion model)
6. Try slash commands: /explain, /review, /test
7. Index your codebase for semantic search

**Best practices:**
- Use different models for chat vs. completions (chat models are too slow for completions)
- Configure local models (Ollama) for privacy-sensitive code
- Create custom slash commands for team workflows
- Set up codebase indexing for project awareness
- Use the `/docs` context provider to include documentation
- Configure CI code review checks for automated PR review

**When NOT to use:**
- If you need autonomous agent mode (use Cline)
- If you want zero-configuration experience (use Copilot)
- If you need the best completion quality (use Cursor Tab)

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
