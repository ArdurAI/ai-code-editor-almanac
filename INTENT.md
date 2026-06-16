# Project Intent & Philosophy

## Why this almanac exists

The AI code editor landscape is exploding. Every week, a new "AI-native IDE" launches, a blog post claims 10x developer productivity, and a vendor announces the next revolution in coding. But **nobody independently verifies these claims**. The benchmarks are self-reported, the comparisons are marketing, and the "best AI editor" lists are affiliate SEO.

This almanac is the **public record of independent verification**. It exists because software engineers and platform teams need a single source of truth that answers:

- Does this editor actually produce correct code, or does it hallucinate APIs?
- What's the real latency of inline completions under typing pressure?
- How does it fail when the codebase is large, unfamiliar, or polyglot?
- What's the total cost of ownership per 1,000 lines of code generated?
- Can I trust the vendor's SWE-bench score when they trained on it?
- How well does it integrate with my existing IDE ecosystem and toolchain?

## Core principles

### 1. Frozen methodology before results

The harness, judge model, prompts, scoring rubric, and benchmark suites are **fixed and published before any editor is tested**. This prevents "cherry-picking" the methodology that favors a particular vendor. If an editor doesn't fit the harness, we adapt the adapter — not the rules.

For code editors, this means:
- The SWE-bench split, Exercism problem set, and Terminal-Bench commands are frozen before testing
- The IDE integration pattern (LSP, extension API, CLI agent) is defined in advance
- The latency measurement points (keystroke-to-completion, command-to-output) are instrumented identically
- The cost model ($/1K lines generated, $/1K suggestions accepted) is computed the same way for every tool

### 2. Ops-first evaluation

Most benchmarks measure SWE-bench pass rates. We measure **what a developer actually lives with**:
- Time from `cursor install` to first working inline completion
- Dependency conflicts when the editor's language server clashes with your existing LSP
- Time to debug when the editor silently generates wrong imports or hallucinated APIs
- Upgrade pain when version N → N+1 breaks your keybindings, settings, or extensions
- Cost predictability when you use the editor 8 hours a day, 5 days a week
- The experience of working in a 100K-line monorepo vs. a greenfield project

### 3. Raw data is always published

Every benchmark run produces a JSON file with every prompt, every generated code snippet, every token count, every latency measurement, and every judge evaluation. These raw files are published alongside the summary. If you disagree with a ranking, you can re-analyze the data yourself — or rerun the exact same adapter on your own machine.

### 4. No tool is above criticism

Every editor on the roster has been through a smoke gate. Every editor has bugs — hallucinated imports, wrong types, broken refactors, silent failures on large files. We document them honestly. A vendor relationship or sponsorship does not influence rankings. The only way an editor improves its score is by actually improving.

### 5. Living document, not a static snapshot

The almanac is updated monthly. Tools enter and exit the roster. Scores change as editors improve or degrade. The "founding edition" is a snapshot; the current edition is the truth. A tool that was Tier A in January may drop to Tier B by June if it stagnates while competitors leap ahead.

## Design philosophy

### The two-bar test

Every tool must clear two bars to justify its existence:
1. **Beat the naive baseline** on accuracy/quality/performance (e.g., vanilla Copilot vs. no AI)
2. **Beat the full-capability baseline** on cost/ops burden/complexity (e.g., Claude Code vs. hiring a junior dev)

If a tool can't do both, it has no reason to exist as a code editor. A tool that is 5% more accurate on SWE-bench but requires 10x the setup, breaks your IDE, and costs $500/month is not worth adopting over a simpler alternative.

### The seven dimensions

We score every code editor on seven dimensions because no single number captures "good AI coding assistance":

| Dimension | Why it matters for code editors |
|-----------|--------------------------------|
| **Accuracy** | Does it produce correct, compilable, test-passing code? Does it understand your existing codebase? |
| **Latency** | Is the inline completion fast enough to feel native? What's the TTFT for chat/agent commands? |
| **Token economics** | What does it cost per 1,000 lines of code generated? Per accepted suggestion? Per SWE-bench task? |
| **Scale behavior** | What happens in a 100K-line monorepo? A 50-file multi-language project? A 10-year legacy codebase? |
| **Ops burden** | How much of your life does it consume to install, configure, upgrade, and debug? |
| **Developer experience** | Is it pleasant or painful to use? Does it respect your workflow, keybindings, and mental model? |
| **Data sovereignty** | Can you run it locally? Does your code leave your machine? Can you audit what the LLM sees? |

### The adapter pattern

Every code editor is tested through a **CodeEditorAdapter** — a frozen interface that the tool must satisfy. The adapter handles setup, workspace ingestion, code generation, and teardown. This means:
- Editors are tested identically across the same codebase snapshots
- The adapter is the only thing that changes per editor (VS Code extension, JetBrains plugin, CLI agent, etc.)
- New editors can be added without changing the harness
- The adapter is published and open for review

Code editor adapters typically implement:
- `setup()` → install the editor/extension, authenticate, configure language server
- `open_workspace()` → load the project, index files, build AST/graph
- `request_completion()` → trigger inline completion at a cursor position, measure latency
- `request_generation()` → send a chat/agent command (e.g., "refactor this function"), measure end-to-end time
- `apply_edit()` → accept or apply the suggested edit, verify correctness
- `teardown()` → clean up, measure resource usage, ensure no code leakage

### The canary

Every benchmark batch starts with a **no-tool baseline** (the "canary") — running the exact same codebase and prompts through the pipeline with no AI assistance. If the benchmark leaked answers anywhere, or if the test harness itself is flawed, the canary would score above zero. The canary must score exactly zero on generation tasks and exactly zero on "helpfulness" — this is a hard invariant. If it doesn't, the entire batch is invalid.

## Who this is for

- **Software engineers** evaluating which AI editor to adopt for daily use
- **Platform engineering teams** choosing a standardized AI coding tool for the organization
- **CTOs/VP Engineering** making build-vs-buy decisions with actual data on accuracy, cost, and security
- **Open-source maintainers** of AI editors who want independent benchmarking of their project
- **Researchers** studying the AI code generation landscape, SWE-bench dynamics, or IDE ergonomics
- **Vendors** who want to improve their editors based on real evidence, not just internal metrics

## What this is NOT

- Not a marketing site for any vendor (Cursor, GitHub, Anthropic, or any other)
- Not a "best of" list based on GitHub stars, funding rounds, or Twitter hype
- Not a tutorial on how to use any editor (no "10 tips for Cursor" content)
- Not a replacement for your own due diligence on your specific codebase
- Not a static document that never changes — the landscape moves too fast for that

## The "Quest"

The "Developer's Quest for the Best AI Editor" is the ongoing effort to test, measure, and rank every tool on the roster. It's not a one-time effort. It's a continuous process of:
1. **Discovery** — finding new editors via research, community, Hacker News, Product Hunt, and submissions
2. **Triage** — deciding if an editor is serious enough to enter the roster (not a toy, not a wrapper, not dead)
3. **Smoke gate** — running every editor through an identical 3-turn scenario: open file, generate/edit code, verify correctness
4. **Benchmark** — running standard suites (SWE-bench, Exercism, Terminal-Bench) + custom + stress tests
5. **Publication** — publishing raw data + summary + per-tool deep-dives
6. **Iteration** — re-testing as editors update, as methodology improves, as new benchmarks emerge

## How to challenge a result

If you believe a ranking or score is wrong:
1. Check the **raw results JSON** — the data is public, every prompt and every response is there
2. Check the **adapter implementation** — the adapter code is public, you can see exactly how the editor was driven
3. Check the **judge prompts** — the prompts are frozen and public, with SHA-256 hashes
4. File an issue with a specific claim and evidence (e.g., "Adapter X used the wrong API version for Tool Y")
5. We'll re-run the test or update the methodology if warranted

## Governance

- **ArdurAI** maintains the almanac and runs the Quest
- **Methodology changes** require a public RFC and at least one edition cycle of notice (e.g., changing the SWE-bench split)
- **Tool additions/removals** are decided by the triage criteria (stars, last push, community activity, seriousness)
- **Benchmark results** are machine-generated; summaries are human-reviewed for fairness
- **Conflicts of interest** are disclosed (e.g., ArdurAI contributes to some tools on the roster); mitigation is identical harness for all

## License

Content: CC BY 4.0  
Harness code: MIT  
Raw data: CC BY 4.0
