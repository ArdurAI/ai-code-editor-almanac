# Code Editors & IDE Assistants Almanac

A living encyclopedia of AI code editors, IDE assistants, and terminal coding agents. Updated **monthly** with fresh repo metadata, releases, landscape shifts, and independent benchmark results from the *"Platform Engineer's Quest for the Best"* series.

> Vendors publish their own benchmark numbers. Nobody reproduces them independently, and nobody evaluates tools the way a platform engineer has to live with them: ops burden, failure modes, scale curves, and cost. This almanac is the public record of that work.

**30 tools** — **Tier A**: 17 · **Tier B**: 13

## Tool Catalogue

Every tool below has a full deep-dive page in [`tools/`](tools/). Sorted by tier (A → B → C), then alphabetically.

| Tool | Type | License | Stars | Tier | Description | Detail |
|------|------|---------|-------|------|-------------|--------|
| **Aider** | ** Terminal pair-programmer | Apache-2.0 | 47K+ | A | 47K+ GitHub stars; the original AI terminal pair-programmer with Git-native diffs, tree-sitter code analysis, and model-agnostic support for 50+ LLMs. | [`aider.md`](tools/aider.md) |
| **Claude Code** | ** CLI agent | Proprietary | — | A | Anthropic's flagship CLI-based AI coding agent; ~$2.5B ARR; 1M-token context; Agent Teams; SWE-bench 82%; the agentic coding tool of choice for… | [`claude-code.md`](tools/claude-code.md) |
| **Cline** | ** VS Code + CLI | Apache-2.0 | 64K+ | A | Open-source VS Code extension with 5M+ installs, 64K+ GitHub stars; BYOK autonomous coding agent with native subagents, browser automation, and… | [`cline.md`](tools/cline.md) |
| **CodeRabbit** | ** AI code review | Proprietary | — | A | $550M valuation; 8,000+ customers; automated AI code review that provides line-by-line feedback on pull requests with deep context understanding. | [`coderabbit.md`](tools/coderabbit.md) |
| **Codex CLI** | ** CLI agent | Apache-2.0 | 95K+ | A | OpenAI's open-source CLI coding agent; 95K+ GitHub stars; Rust-native with sandboxed execution; included in ChatGPT subscriptions; 240+ tok/s… | [`codex-cli.md`](tools/codex-cli.md) |
| **Continue** | ** IDE extension | Apache-2.0 | 35K+ | A | 35K+ GitHub stars; the leading open-source AI code assistant extension for VS Code and JetBrains with BYOK, codebase chat, inline completions, and… | [`continue.md`](tools/continue.md) |
| **Cursor** | ** AI-native IDE | Proprietary | — | A | VS Code fork by Anysphere; the market-leading AI-native IDE ($20–200/mo) with deep codebase indexing, multi-model chat, Tab completion, and agent… | [`cursor.md`](tools/cursor.md) |
| **Devin** | ** Autonomous SWE | Proprietary | — | A | Cognition's autonomous AI software engineer; operates in a full VM with shell, browser, and editor; Slack-native; $20/mo entry + ACU-based pricing… | [`devin.md`](tools/devin.md) |
| **Gemini CLI** | ** CLI agent | Apache-2.0 | 106K+ | A | 106K+ GitHub stars; Google's open-source CLI agent with 1M-token context, 1,000 requests/day free tier, and full Gemini model integration. | [`gemini-cli.md`](tools/gemini-cli.md) |
| **GitHub Copilot** | ** IDE assistant | Proprietary | — | A | The most widely adopted AI coding assistant; integrated into GitHub's ecosystem with IDE plugins, CLI agent (Copilot CLI), and usage-based credits… | [`github-copilot.md`](tools/github-copilot.md) |
| **Kimi CLI** | ** Terminal agent | Apache-2.0 (open source) | 9.1K+ | A | 9.1K+ GitHub stars; Moonshot AI's open-source CLI agent powered by the K2 model series with Agent Swarm (up to 300 parallel sub-agents) — the… | [`kimi-cli.md`](tools/kimi-cli.md) |
| **OpenCode** | ** Terminal TUI | MIT | 182K+ | A | 182K+ GitHub stars; a terminal-based AI coding agent with TUI, 75+ LLM provider support, and Go-based architecture — one of the fastest-growing… | [`opencode.md`](tools/opencode.md) |
| **OpenHands** | ** Autonomous agent | MIT | 79K+ | A | 79K+ GitHub stars (formerly OpenDevin); the leading open-source autonomous AI software engineering agent with Docker-sandboxed execution,… | [`openhands.md`](tools/openhands.md) |
| **Tabnine** | ** Completion + chat | Proprietary | — | A | 1M+ developers; enterprise-focused AI coding assistant with on-prem deployment, zero data retention, SOC 2/GDPR compliance, and private model… | [`tabnine.md`](tools/tabnine.md) |
| **Trae** | ** AI IDE | Proprietary | — | A | ByteDance's free AI-native IDE (VS Code fork); strong for Chinese language ecosystems with multi-model support (Claude, GPT, DeepSeek) and… | [`trae.md`](tools/trae.md) |
| **Windsurf** | ** AI-native IDE | Proprietary | — | A | Formerly Codeium; an AI-native VS Code fork with Cascade multi-step agentic flows; acquired by Cognition (makers of Devin) in December 2025. | [`windsurf.md`](tools/windsurf.md) |
| **Zed** | ** Rust-native editor | Open source (GPL/AGPL core + proprietary extensions) | 86K+ | A | 86K+ GitHub stars; GPU-accelerated Rust-native code editor with multi-provider AI chat, real-time collaboration, and industry-leading performance. | [`zed.md`](tools/zed.md) |
| **Amazon Q Developer** | ** IDE + CLI | Proprietary | — | B | AWS's AI coding assistant (formerly CodeWhisperer); deeply integrated with AWS services; includes IDE chat, CLI agent, code transformation, and… | [`amazon-q-developer.md`](tools/amazon-q-developer.md) |
| **Cody** | ** Codebase assistant | Proprietary | — | B | Sourcegraph's AI coding assistant; specializes in large-codebase understanding with deep code search, multi-repo context, and enterprise code… | [`cody.md`](tools/cody.md) |
| **JetBrains Junie** | ** IDE agent | Proprietary | — | B | JetBrains' AI coding agent integrated into IntelliJ IDEs; multi-agent support, BYOK, and deep JetBrains platform integration; AI Pro $10/mo or… | [`jetbrains-junie.md`](tools/jetbrains-junie.md) |
| **Kilo Code** | ** Multi-platform agent | MIT (open source) | 25K+ | B | 25K+ GitHub stars; a multi-platform open-source AI coding agent with 500+ model support, Architect/Code/Debug modes, and cross-IDE compatibility —… | [`kilo-code.md`](tools/kilo-code.md) |
| **Oh-My-Pi (omp)** | ** Terminal agent | MIT | 9.3K GitHub | B | Terminal AI agent that bundles IDE-grade capabilities — LSP, DAP debuggers, persistent Python/JS kernels, ripgrep, and ast-grep — into a single… | [`oh-my-pi.md`](tools/oh-my-pi.md) |
| **Replit Agent** | ** Cloud app builder | Proprietary | — | B | Replit's AI agent that builds full-stack applications from natural language prompts, runs them in cloud dev environments, and deploys with one… | [`replit-agent.md`](tools/replit-agent.md) |
| **Roo Code** | ** VS Code extension | Apache-2.0 (open source) | 24K+ | B | 24K+ GitHub stars; a popular Cline fork with enhanced multi-mode agent loop, custom modes, memory bank, and community-driven development — the… | [`roo-code.md`](tools/roo-code.md) |
| **Supermaven** | ** Completion engine | Proprietary | — | B | Acquired by Cursor (Anysphere) in late 2024; known for fast, long-context inline completions with a 1M-token context window and low-latency inference. | [`supermaven.md`](tools/supermaven.md) |
| **Tabby** | ** Self-hosted completion | Apache-2.0 (open source) | 34K+ | B | 34K+ GitHub stars; open-source self-hosted AI code completion server with Kubernetes-ready deployment, server-side code indexing, RAG, and support… | [`tabby.md`](tools/tabby.md) |
| **文心快码 (Baidu Comate)** | ** IDE plugin | Proprietary | — | B | Baidu's AI coding assistant powered by the ERNIE (文心) model series; supports 100+ languages with expertise in Chinese frameworks like 若依 (RuoYi);… | [`文心快码.md`](tools/文心快码.md) |
| **腾讯云AI代码助手 (Tencent Cloud AI Code Assistant)** | ** IDE plugin | Proprietary | — | B | Tencent Cloud's AI coding assistant with a hybrid model approach; reports 50%+ internal usage at Tencent; integrated with Tencent Cloud ecosystem… | [`腾讯云ai代码助手.md`](tools/腾讯云ai代码助手.md) |
| **豆包 MarsCode (Doubao MarsCode)** | ** IDE + cloud IDE | Proprietary | — | B | ByteDance's AI coding assistant and cloud IDE; supports 100+ languages with project-aware completions; integrated into the Doubao (豆包) AI… | [`豆包-marscode.md`](tools/豆包-marscode.md) |
| **通义灵码 (Tongyi Lingma)** | ** IDE plugin | Proprietary | — | B | Alibaba's AI coding assistant powered by the Tongyi (通义) model series; supports 200+ languages with database-aware coding, deep Aliyun… | [`通义灵码.md`](tools/通义灵码.md) |

## Tool Categories

### ** AI IDE (1)
**Trae**

### ** AI code review (1)
**CodeRabbit**

### ** AI-native IDE (2)
**Cursor** · **Windsurf**

### ** Autonomous SWE (1)
**Devin**

### ** Autonomous agent (1)
**OpenHands**

### ** CLI agent (3)
**Claude Code** · **Codex CLI** · **Gemini CLI**

### ** Cloud app builder (1)
**Replit Agent**

### ** Codebase assistant (1)
**Cody**

### ** Completion + chat (1)
**Tabnine**

### ** Completion engine (1)
**Supermaven**

### ** IDE + CLI (1)
**Amazon Q Developer**

### ** IDE + cloud IDE (1)
**豆包 MarsCode (Doubao MarsCode)**

### ** IDE agent (1)
**JetBrains Junie**

### ** IDE assistant (1)
**GitHub Copilot**

### ** IDE extension (1)
**Continue**

### ** IDE plugin (3)
**文心快码 (Baidu Comate)** · **腾讯云AI代码助手 (Tencent Cloud AI Code Assistant)** · **通义灵码 (Tongyi Lingma)**

### ** Multi-platform agent (1)
**Kilo Code**

### ** Rust-native editor (1)
**Zed**

### ** Self-hosted completion (1)
**Tabby**

### ** Terminal TUI (1)
**OpenCode**

### ** Terminal agent (2)
**Kimi CLI** · **Oh-My-Pi (omp)**

### ** Terminal pair-programmer (1)
**Aider**

### ** VS Code + CLI (1)
**Cline**

### ** VS Code extension (1)
**Roo Code**

## Quick Start

```bash
git clone https://github.com/ArdurAI/ai-code-editor-almanac.git
cd ai-code-editor-almanac
```

| You want… | Go to |
|-----------|-------|
| The state of the landscape right now | The latest file in [`editions/`](editions/) |
| Everything we know about one tool | [`tools/<name>.md`](tools/) |
| Machine-readable roster + metadata | [`data/`](data/) |
| Architecture diagrams | [`architecture.md`](architecture.md) |
| Benchmark results (rolling) | [`benchmarks/`](benchmarks/) |
| How tools are tested and ranked | [`methodology/benchmark-harness.md`](methodology/benchmark-harness.md) |
| Project intent & philosophy | [`INTENT.md`](INTENT.md) |
| Implementation guide | [`IMPLEMENTATION.md`](IMPLEMENTATION.md) |
| Testing methodology | [`TESTING.md`](TESTING.md) |
| Troubleshooting | [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) |

## Methodology

Results published here come from a frozen-before-results harness. Full details in [`methodology/benchmark-harness.md`](methodology/benchmark-harness.md):

- Standard benchmarks for comparability with published claims — every ranking ships a *published vs. reproduced* table.
- A custom **PlatformOps** benchmark: testing on infrastructure work — setup, reliability, scale, cost.
- A stress suite: contradiction storms, near-duplicate floods, concurrent writers, kill-the-backing-store chaos, cost-runaway measurement.
- Seven scored dimensions: accuracy, latency, token economics, scale behavior, **ops burden**, developer experience, data sovereignty.

The judge model, prompts (SHA-256-frozen), and control variables were fixed before any tool ran. Raw results JSON is published with every ranking.

## Contributing

We welcome contributions — new tools, data fixes, ranking challenges, and benchmark reproductions. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on how to add a tool, fix data, or challenge a ranking.

## Recent Edition

📖 **[Read the latest edition →](editions/2026-06.md)**

One edition per month under `editions/YYYY-MM.md`: refreshed metadata, notable releases, new entrants triaged in or out, and a diary of what was tested.

---

## License

Content is licensed **CC BY 4.0** — share and adapt with attribution to **ArdurAI**.

---

**Authored by Team Ardur · CC BY 4.0**
