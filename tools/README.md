# Per-Tool Deep-Dive Pages

Each `.md` file in this directory is a deep-dive analysis of one tool on the roster, enriched with a standardized 10-section deep analysis.

## Naming convention

`<tool-name>.md` where `tool-name` is the lowercase, hyphenated version of the tool name (e.g., `cursor.md`, `github-copilot.md`).

## Page structure

Every tool page includes the original metadata sections plus a standardized **Deep Analysis** with 10 sections:

1. How Is This Tool Useful?
2. Gotchas of Using This Tool
3. Limitations
4. How Secure Is This Tool?
5. Usefulness to General Public and Non-Technical Users
6. What Does This Tool Solve That Others Don't?
7. How Does This Tool Rank Compared to Others?
8. How Can This Tool Be Improved? How Active Is Development?
9. Official Maintainer Contacts
10. General Usage Guidance

## Tool Roster — Comprehensive Table

| Tool | Type | License | Stars | Tier | Description | File |
|------|------|---------|-------|------|-------------|------|
| Cursor | AI-native IDE | Proprietary | 33K (GH) | A | VS Code fork; market-leading AI IDE with Tab, Composer, Agent mode | [cursor.md](cursor.md) |
| GitHub Copilot | IDE assistant | Proprietary | N/A (proprietary) | A | Widest adoption; multi-model; usage-based credits | [github-copilot.md](github-copilot.md) |
| Claude Code | CLI agent | Proprietary | 135K (GH) | A | Best-in-class agentic coding; SWE-bench 82%; Agent Teams; MCP | [claude-code.md](claude-code.md) |
| Windsurf | AI-native IDE | Proprietary | N/A | A | Formerly Codeium; Cascade flows; acquired by Cognition | [windsurf.md](windsurf.md) |
| Cline | VS Code + CLI | Apache-2.0 | 64K (GH) | A | Open-source VS Code agent; 5M+ installs; BYOK; browser automation | [cline.md](cline.md) |
| Aider | Terminal pair-programmer | Apache-2.0 | 47K (GH) | A | Git-native terminal AI; repo map; 50+ models; Architect mode | [aider.md](aider.md) |
| Continue | IDE extension | Apache-2.0 | 35K (GH) | A | Open-source VS Code + JetBrains; config-driven; BYOK | [continue.md](continue.md) |
| Codex CLI | CLI agent | Apache-2.0 | 95K (GH) | A | OpenAI; Rust-native; sandboxed; included in ChatGPT | [codex-cli.md](codex-cli.md) |
| Gemini CLI | CLI agent | Apache-2.0 | 106K (GH) | A | Google; 1M context; 1,000 req/day free; fully open source | [gemini-cli.md](gemini-cli.md) |
| Devin | Autonomous SWE | Proprietary | N/A | A | Cognition; full VM; Slack-native; ACU pricing | [devin.md](devin.md) |
| OpenHands | Autonomous agent | MIT | 79K (GH) | A | Leading open-source autonomous agent; Docker sandboxed | [openhands.md](openhands.md) |
| Replit Agent | Cloud app builder | Proprietary | N/A | B | Full-stack from prompt; one-click deploy; browser-based | [replit-agent.md](replit-agent.md) |
| Zed | Rust-native editor | GPL/AGPL (core) | 86K (GH) | A | GPU-accelerated; real-time collab; multi-provider AI chat | [zed.md](zed.md) |
| Tabnine | Completion + chat | Proprietary | 11K (legacy GH) | A | Enterprise-focused; on-prem; zero data retention; SOC 2 | [tabnine.md](tabnine.md) |
| CodeRabbit | AI code review | Proprietary | N/A | A | Automated PR review; line-by-line feedback; $550M valuation | [coderabbit.md](coderabbit.md) |
| Tabby | Self-hosted completion | Apache-2.0 | 34K (GH) | B | Open-source self-hosted; Kubernetes; RAG; open models | [tabby.md](tabby.md) |
| Roo Code | VS Code extension | Apache-2.0 | 24K (GH) | B | Cline fork; multi-mode; memory bank; custom modes | [roo-code.md](roo-code.md) |
| Kilo Code | Multi-platform agent | MIT | 25K (GH) | B | 500+ models; Architect/Code/Debug modes; MIT license | [kilo-code.md](kilo-code.md) |
| OpenCode | Terminal TUI | MIT | 182K (GH) | A | Go-native TUI; 75+ providers; one of fastest-growing dev tools | [opencode.md](opencode.md) |
| Supermaven | Completion engine | Proprietary | 1.4K (nvim) | B | Acquired by Cursor; fast long-context completions | [supermaven.md](supermaven.md) |
| Cody | Codebase assistant | Proprietary | 3.8K (snapshot) | B | Sourcegraph; multi-repo context; large codebase expertise | [cody.md](cody.md) |
| Trae | AI IDE | Proprietary | N/A | A | ByteDance; free; VS Code fork; Chinese ecosystem optimization | [trae.md](trae.md) |
| JetBrains Junie | IDE agent | Proprietary | 313 (GH) | B | Native JetBrains integration; multi-agent; BYOK | [jetbrains-junie.md](jetbrains-junie.md) |
| Kimi CLI | Terminal agent | Apache-2.0 | 9.1K (GH) | A | Moonshot; Agent Swarm (300 sub-agents); K2.6 model | [kimi-cli.md](kimi-cli.md) |
| Amazon Q Developer | IDE + CLI | Proprietary | N/A | B | AWS ecosystem; code transformation; security scanning | [amazon-q-developer.md](amazon-q-developer.md) |
| Oh-My-Pi (omp) | Terminal agent | MIT | 9.3K (per file) | B | IDE-grade terminal agent; LSP + DAP + kernels + ast-grep | [oh-my-pi.md](oh-my-pi.md) |
| 豆包 MarsCode | IDE + cloud IDE | Proprietary | N/A | B | ByteDance; 100+ languages; Cloud IDE; Doubao models | [豆包-marscode.md](豆包-marscode.md) |
| 通义灵码 (Tongyi Lingma) | IDE plugin | Proprietary | 21K (Qwen) | B | Alibaba; database-aware; Qwen models; Aliyun integration | [通义灵码.md](通义灵码.md) |
| 文心快码 (Baidu Comate) | IDE plugin | Proprietary | N/A | B | Baidu; ERNIE models; 若依 expert; free | [文心快码.md](文心快码.md) |
| 腾讯云AI代码助手 | IDE plugin | Proprietary | N/A | B | Tencent; WeChat expert; Hunyuan; 50%+ internal usage | [腾讯云ai代码助手.md](腾讯云ai代码助手.md) |

**Star counts** reflect GitHub stars as of July 2, 2026. "N/A" indicates proprietary tools without public GitHub repositories. Star counts for Chinese tools reflect their model repos where applicable (e.g., Qwen for 通义灵码).

## Tier definitions

- **Tier A**: Market-leading tools with significant adoption, proven capabilities, and active development. Recommended for evaluation.
- **Tier B**: Emerging, niche, or specialized tools. Worth evaluating for specific use cases or ecosystems.

## Status

- **30 tool pages** enriched with standardized 10-section deep analysis (July 2026 edition).
- GitHub star counts, issue counts, and activity data verified via GitHub API on July 2, 2026.
- Benchmark scores sourced from official publications (SWE-bench leaderboard, vendor announcements).
- Security and compliance claims sourced from official vendor documentation.
- Chinese tool data sourced from official websites and company announcements; some metrics marked "Not publicly available" where data is not disclosed.

## How to add a new tool page

1. Add the tool to `data/roster.json` with all required fields.
2. Create `tools/<tool-name>.md` from the template above, including all 10 deep analysis sections.
3. Research GitHub stats, benchmarks, security posture, and competitive positioning using real data.
4. Link it from the edition in `editions/YYYY-MM.md`.
5. Update the README roster table above.

---

*Licensed under CC BY 4.0 — ArdurAI / AI Code Editor Almanac*
