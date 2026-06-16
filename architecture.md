# Architecture: Code Editors & IDE Assistants

How the code editors & ide assistants landscape is shaped, and how the Quest tests it.

## The landscape at a glance

| Tool | Tier | License | Focus | Notes |
|------|------|---------|-------|-------|
| Cursor | A | Proprietary | AI-native IDE | VS Code fork; market leader; $20-200/mo |
| GitHub Copilot | A | Proprietary | IDE assistant | Widest adoption; usage-based credits from June 2026 |
| Claude Code | A | Proprietary | CLI agent | ~$2.5B ARR; 1M context; Agent Teams; SWE-bench 82% |
| Windsurf | A | Proprietary | AI-native IDE | Formerly Codeium; acquired by Cognition Dec 2025 |
| OpenCode | A | MIT | Terminal TUI | 150K+ stars; 75+ LLM providers; Go-based |
| Cline | A | Apache-2.0 | VS Code + CLI | 5M+ installs; native subagents; BYOK; browser automation |
| Aider | A | MIT | Terminal pair-programmer | 42K+ stars; Git-aware diffs; model-agnostic |
| Continue | A | Apache-2.0 | IDE extension | 20K+ stars; BYOK; code review; CI-enforceable checks |
| Zed | A | Open source | Rust-native editor | Multi-provider chat; real-time collab; GPU-accelerated |
| Trae | A | Proprietary | AI IDE | ByteDance; free; VS Code fork; 95% WeChat SDK accuracy |
| Tabnine | A | Proprietary | Completion + chat | 1M+ devs; on-prem; zero data retention; SOC 2/GDPR |
| Codex CLI | A | Apache-2.0 | CLI agent | OpenAI; Rust-native; 240+ tok/s; included in ChatGPT |
| Gemini CLI | A | Apache-2.0 | CLI agent | 1M token context; 1,000 req/day free; full open source |
| Kimi CLI | A | Open source | Terminal agent | Moonshot; Agent Swarm up to 300 sub-agents; K2.6 |
| Devin | A | Proprietary | Autonomous SWE | Cognition; full VM; Slack-native; $20/mo entry + ACUs |
| OpenHands | A | MIT | Autonomous agent | 70K+ stars; formerly OpenDevin; Docker sandboxed |
| CodeRabbit | A | Proprietary | AI code review | $550M valuation; 8,000+ customers; line-by-line feedback |

## How the Quest tests a tool

Same harness for all entries; the judge was frozen before any tool ran:

```
Adapter[frozen CategoryAdapter contract]
  ├── setup()    → install, configure
  ├── load()     → ingest workload
  ├── await_ready() → async barrier
  ├── query()    → run test, get response
  └── teardown() → cleanup, measure
       ↓
Telemetry: latency · tokens · $ · ops notes
       ↓
Grading: deterministic + LLM judge (frozen prompts)
       ↓
Raw results JSON (published)
```

The `await_ready()` barrier is where async designs get their cost measured instead of hidden.

## License

Content is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / Code Editors & IDE Assistants Almanac**.
