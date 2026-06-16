# Code Editors & IDE Assistants Almanac

A living encyclopedia of AI code editors, IDE assistants, and terminal coding agents. Updated monthly with fresh repo metadata, releases, landscape shifts, and independent benchmark results.

> Vendors publish their own benchmark numbers. Nobody reproduces them independently, and nobody evaluates tools the way a platform engineer has to live with them: ops burden, failure modes, scale curves, and cost. This almanac is the public record of that work.

## How to use this repo

| You want… | Go to |
|-----------|-------|
| The state of the landscape right now | The latest file in `editions/` |
| Everything we know about one tool | `tools/<name>.md` |
| Machine-readable roster + metadata | `data/roster.json` |
| Architecture diagrams | `architecture.md` |
| Benchmark results (rolling) | `benchmarks/` |
| How tools are tested and ranked | `methodology/benchmark-harness.md` |

## The roster

**Tier A** — 17 tools: Cursor, GitHub Copilot, Claude Code, Windsurf, OpenCode, Cline, Aider, Continue, Zed, Trae…

**Tier B** — 12 tools: Supermaven, Cody, Amazon Q Developer, JetBrains Junie, Replit Agent, Kilo Code, Roo Code, Tabby, 通义灵码, 文心快码…

**Tier C** — 34 tools: Bolt.new, Lovable, v0 (Vercel), Appy Pie, Qwen Code CLI, Grok Build, Hermes Agent, OpenClaw, Qodo (CodiumAI), Snyk…

**Total: 63 tools**

## Methodology

Results published here come from a frozen-before-results harness:
- Standard benchmarks for comparability with published claims — every ranking ships a _published vs. reproduced_ table.
- A custom PlatformOps benchmark: testing on infrastructure work — setup, reliability, scale, cost.
- A stress suite: contradiction storms, near-duplicate floods, concurrent writers, kill-the-backing-store chaos, cost-runaway measurement.
- Seven scored dimensions: accuracy, latency, token economics, scale behavior, **ops burden**, developer experience, data sovereignty.

The judge model, prompts (SHA-256-frozen), and control variables were fixed before any tool ran. Raw results JSON is published with every ranking.

## Update cadence

One edition per month under `editions/YYYY-MM.md`: refreshed metadata, notable releases, new entrants triaged in or out, and a diary of what was tested.

## License

Content is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / Code Editors & IDE Assistants Almanac**.
