# Oh-My-Pi (omp)

| Attribute | Value |
|-----------|-------|
| Tier | B |
| Type | Terminal agent |
| License | MIT |
| Stars | 9.3K GitHub |
| Region | Global |
| URL | https://github.com/oh-my-pi/omp |

## One-line summary

Terminal AI agent that bundles IDE-grade capabilities — LSP, DAP debuggers, persistent Python/JS kernels, ripgrep, and ast-grep — into a single MIT-licensed terminal process speaking to 40+ LLM providers.

## Architecture

Oh-My-Pi takes a radically different approach from polished commercial competitors: it bundles IDE-grade capabilities into a single terminal process rather than running as a separate IDE or extension. The architecture includes:

- **LSP integration**: Language server protocol support for multiple languages
- **DAP debuggers**: Debug adapter protocol for interactive debugging
- **Persistent kernels**: Python and JavaScript kernels that maintain state across sessions
- **Search tools**: ripgrep and ast-grep for fast code search and structural matching
- **Multi-provider support**: 40+ LLM providers via unified interface

## Key features

- Terminal-native workflow (no IDE required)
- 40+ LLM provider support
- Persistent Python/JS kernels
- LSP and DAP integration
- Structural search via ast-grep
- MIT-licensed open source
- 410 releases as of June 2026 (very active development)

## Benchmark status

| Dimension | Status | Notes |
|-----------|--------|-------|
| Accuracy | Not run | Pending SWE-bench / Exercism |
| Latency | Not run | Terminal-native may have lower overhead than IDE-based tools |
| Token economics | Not run | Model-agnostic; cost depends on provider chosen |
| Scale behavior | Not run | LSP + ast-grep should handle large codebases well |
| Ops burden | Not run | Single binary install; MIT license |
| Developer experience | Not run | Terminal-only may have steeper learning curve |
| Data sovereignty | Not run | BYOK; no vendor lock-in |

## Ops reality

**Sharp edges:**
- Single-maintainer dependency: the project is primarily driven by one maintainer, creating bus-factor risk
- Volatility: 410 releases in a short time suggests rapid iteration but also potential instability
- Terminal-only: developers who prefer visual IDEs may find the workflow unfamiliar

**Setup experience:**
- Single binary install (likely via package manager or GitHub releases)
- MIT-licensed, no auth required for open-source models
- BYOK for commercial providers

## Cost model

- **Open source**: Free (MIT license)
- **API costs**: Varies by provider (40+ LLM providers supported)
- **Self-hosted**: No infrastructure cost beyond the machine

## When to use / when to avoid

**Use when:**
- You want a terminal-native AI agent with IDE-grade capabilities
- You need model-agnostic support (40+ providers)
- You prefer open-source tools with no vendor lock-in
- You value structural search (ast-grep) over simple text search

**Avoid when:**
- You need a visual IDE with inline completions and diff views
- You require enterprise support or SLAs (single-maintainer project)
- You prefer stability over rapid iteration (410 releases may indicate churn)

## Roster entry

- **Name:** Oh-My-Pi
- **Type:** Terminal agent
- **License:** MIT
- **Region:** Global
- **Tier:** B
- **ide_support:** ["Terminal", "CLI"]
- **languages:** ["Python", "JavaScript", "TypeScript", "Rust", "Go", "Java", "C++", "Ruby"]
- **pricing_model:** "Open Source"
- **Notes:** 9.3K stars; 410 releases; LSP + DAP + kernels + ripgrep + ast-grep; 40+ LLM providers

## Discovered

- **Date:** 2026-06-17
- **Source:** Product Hunt + web search
- **Investigation:** Post-June 2026 new entrants sweep
