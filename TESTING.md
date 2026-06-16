# Testing & Benchmarking

How the code editor almanac tests tools, what the harness does, how scoring works, and how to reproduce results.

## Table of Contents

1. [The Three Benchmark Types](#the-three-benchmark-types)
2. [The Seven Dimensions](#the-seven-dimensions)
3. [The Harness Architecture](#the-harness-architecture)
4. [The Canary](#the-canary)
5. [Standard Benchmarks](#standard-benchmarks)
6. [CodeEditor Custom Benchmarks](#codeeditor-custom-benchmarks)
7. [Stress Suite](#stress-suite)
8. [Cross-Category Integration Tests](#cross-category-integration-tests)
9. [Scoring](#scoring)
10. [Reproducibility](#reproducibility)
11. [Failure Mode Taxonomy](#failure-mode-taxonomy)

---

## The Three Benchmark Types

Every code editor is tested across three types of benchmarks:

| Type | Purpose | Frequency |
|------|---------|-----------|
| **Standard benchmarks** | Verify vendor claims with published test suites (SWE-bench, Exercism, Terminal-Bench) | Every benchmark run |
| **CodeEditor custom benchmarks** | Test coding reality: setup, IDE integration, inline completion latency, cost at scale | Every benchmark run |
| **Cross-category integration tests** | Test how editors work with other tools in a full stack (e.g., editor + agent framework + vector DB) | Quarterly |

## The Seven Dimensions

Every code editor is scored 0-100 on each dimension. The final score is a weighted average, but the per-dimension scores are always published.

| Dimension | Weight | What it measures | How it's tested |
|-----------|--------|-----------------|-----------------|
| **Accuracy / Quality** | 25% | Does it produce correct, compilable, test-passing code? Does it understand context? | SWE-bench + Exercism + Terminal-Bench + custom test suites |
| **Latency** | 15% | TTFT for inline completions, chat responses, and agent commands; throughput (completions/sec) | Instrumented measurements; p50, p95, p99 across file sizes |
| **Token Economics** | 15% | Cost per 1,000 lines of code generated, per accepted suggestion, per SWE-bench task | Standardized workloads; $/1K lines, $/1K suggestions, $/task |
| **Scale Behavior** | 15% | What happens in monorepos, multi-file projects, polyglot codebases, legacy code? | Load tests with 10K, 100K, 500K LOC; multi-file navigation |
| **Ops Burden** | 15% | Time to install, configure auth, resolve IDE conflicts, upgrade without breaking workflow | Measured setup time; smoke-gate sweep; dependency matrix |
| **Developer Experience** | 10% | Documentation quality, error messages, UI responsiveness, keybinding respect, community | Structured rubric; community health metrics; UX heuristics |
| **Data Sovereignty** | 5% | Local-mode viability, code privacy, audit trails, compliance (SOC 2, GDPR, HIPAA) | Feature matrix; network traffic analysis; self-hosting path |

### Why these weights?

The weights reflect what a software engineer actually cares about. Accuracy is the most important — an editor that generates wrong code is worse than no editor. But ops burden is nearly as important because an editor that crashes your IDE, conflicts with your LSP, or requires constant re-authentication is not worth the productivity gain.

For code editors specifically, latency is critical because inline completions must feel instantaneous. A 500ms delay breaks flow state. Token economics matter because developers generate thousands of suggestions per day — small per-suggestion cost differences compound into significant monthly bills.

Weights are reviewed annually. Changes require an RFC and a public comment period.

## The Harness Architecture

```
┌─────────────────────────────────────────┐
│  CodeEditorAdapter (frozen contract)    │
│  ├── setup()   → install, configure      │
│  ├── open_workspace() → load project    │
│  ├── request_completion() → inline comp │
│  ├── request_generation() → chat/agent  │
│  ├── apply_edit() → accept & verify     │
│  ├── run_tests() → test suite execution │
│  └── teardown() → cleanup, measure      │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Telemetry Collector                    │
│  ├── latency (p50/p95/p99)            │
│  │   ├── keystroke-to-completion         │
│  │   ├── prompt-to-first-token (TTFT)   │
│  │   └── command-to-output (agent)      │
│  ├── token count & cost                 │
│  ├── memory & CPU usage                 │
│  ├── error rate & failure mode taxonomy │
│  └── ops notes (setup time, deps, bugs) │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Grading Pipeline                         │
│  ├── Deterministic grader (exact match)   │
│  ├── Compiler grader (syntax check)       │
│  ├── Test runner (unit test pass/fail)    │
│  ├── LLM judge (frozen prompts, SHA-256) │
│  ├── Second pass (confidence < 0.7)        │
│  └── Failure mode taxonomy               │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Results Publisher                        │
│  ├── Raw JSON (per prompt, per run)     │
│  ├── Summary tables (per editor)        │
│  ├── Cross-verification analysis          │
│  └── Insight extraction                 │
└─────────────────────────────────────────┘
```

### The `open_workspace()` barrier

This is where IDE integration quality gets measured instead of hidden. Many editors claim "instant context awareness" but actually take 30+ seconds to index a large repo. The `open_workspace()` barrier forces the editor to finish all indexing, LSP initialization, and graph building before the first completion is requested, so the true latency is measured.

### The Telemetry Collector

Every adapter call is instrumented:
- **Latency**: `time.monotonic()` around every call; p50, p95, p99 computed across all runs
  - **Inline completion latency**: Keystroke simulated → first character displayed
  - **Chat TTFT**: Prompt sent → first token received
  - **Agent end-to-end**: Task described → all files edited and tests passing
- **Tokens**: If the editor uses LLM APIs, token counts are captured from API responses or estimated via tokenizer
- **Cost**: Token counts × provider pricing; or measured cloud spend for self-hosted tools; computed as $/1K lines generated
- **Memory**: `psutil` or container metrics for memory usage during the run (editors can be memory-hungry)
- **CPU**: CPU utilization during indexing and generation
- **Errors**: Every exception, timeout, syntax error, or test failure is logged with full traceback
- **Ops notes**: Human observations about setup friction, IDE conflicts, auth flows, documentation quality

## The Canary

The first run of every batch is the **no-tool baseline** (the "canary") — running the exact same codebase and prompts through the pipeline with no AI assistance. If the benchmark leaked answers anywhere, or if the test harness itself generates code without the editor, the canary would score above zero.

**Canary rules**:
- The canary must score exactly **0.000** on all code generation tasks (no code should be produced without the editor)
- The canary must score exactly **0.000** on inline completion (no suggestions should appear)
- The canary must score exactly **1.000** on abstention tasks (it should refuse to generate code when no editor is present)
- If the canary fails, the entire batch is invalid and must be rerun
- The canary run is published alongside the real results
- The canary adapter is a no-op: setup does nothing, open_workspace does nothing, request_completion returns empty, request_generation returns empty, teardown does nothing

## Standard Benchmarks

### Code Editor benchmarks

| Benchmark | What it tests | Scope | Source |
|-----------|--------------|-------|--------|
| **SWE-bench** | Code generation correctness on real GitHub issues (Python repos) | Full repo context, multi-file edits, test validation | [SWE-bench](https://github.com/princeton-nlp/SWE-bench) |
| **Exercism** | Code correctness on curated coding exercises across languages | Single-file, language-specific, test-driven | [Exercism](https://exercism.org) |
| **Terminal-Bench** | Terminal command correctness and file manipulation | CLI tasks, shell scripting, environment setup | [Terminal-Bench](https://github.com/...) |

### SWE-bench specifics

- **Split**: We use a held-out split not present in the training data of major LLMs (verified via n-gram analysis)
- **Tasks**: 50 tasks per run, balanced across bug fixes, feature additions, and refactoring
- **Evaluation**: Generated patch is applied to the repo; tests are run; pass rate is the score
- **Metrics**: Pass@1 (first attempt), Pass@k (k attempts with retry), and average tokens used per task

### Exercism specifics

- **Tracks**: Python, JavaScript, TypeScript, Rust, Go (5 tracks)
- **Problems**: 20 problems per track, selected from the "hard" and "medium" pools
- **Evaluation**: Generated solution is compiled (if applicable) and tests are run; all tests must pass
- **Metrics**: Pass rate, average attempts per problem, average lines of code generated

### Terminal-Bench specifics

- **Commands**: 30 tasks covering file operations, git workflows, environment setup, and debugging
- **Evaluation**: Command is executed in a sandboxed container; output is checked against expected result
- **Metrics**: Success rate, average commands per task, safety violations (destructive commands)

### Published vs. reproduced

Every standard benchmark ranking ships a table:

| Editor | Published Claim | Our Result | Delta | Verdict |
|--------|----------------|------------|-------|---------|
| Editor A | 43% on SWE-bench | 41% on SWE-bench | -2% | ✅ Close |
| Editor B | "fastest completions" | 3rd of 8 on p50 latency | — | ⚠️ Misleading |
| Editor C | No claim | 87% on Exercism Python | N/A | — |

## CodeEditor Custom Benchmarks

### Setup experience

**Measured**:
- Time from "download/install" to first working inline completion
- Number of IDE conflicts when installing alongside other roster tools (e.g., two Copilot-like extensions)
- Time to resolve auth/login (OAuth flows, API key setup, enterprise SSO)
- Number of undocumented steps required (e.g., "you must install Node 18+ but we don't say so")
- Time to find the answer in the docs when stuck

**Scored on**:
- Sub-5 minutes: 90-100
- 5-15 minutes: 70-89
- 15-30 minutes: 50-69
- 30+ minutes or unresolved: 0-49

### Smoke gate

Every code editor must pass an identical 3-turn scenario before entering the roster:

```
Turn 1: Open a source file in a supported workspace (e.g., a Python project with tests)
Turn 2: Request a code generation or edit (inline completion at a function stub, 
        or a chat command to "implement this function")
Turn 3: Verify the generated code is syntactically valid and the project tests still pass
```

**Pass criteria**:
- No crashes, no silent failures, no IDE freezing
- Generated code must be syntactically valid for the target language
- The editor must not break existing code (tests must still pass)
- Results must be deterministic (same prompt → same output structure, though LLM variance is noted)
- The editor must handle the basic case without workarounds (no "you need to manually type the first character")

**What the smoke gate surfaced** (from the code editor almanac, as examples):
- **Hallucinated imports**: Editor generates `from nonexistent import foo` that breaks the project
- **Broken refactors**: "Rename symbol" changes 3 of 5 references, leaving broken code
- **IDE lag**: Inline completion takes 2+ seconds on a 100-line file, breaking typing flow
- **Auth drift**: OAuth token expires after 1 hour and the editor silently stops working
- **Language server conflicts**: Editor's bundled LSP conflicts with user's existing LSP, crashing both
- **Context leakage**: Chat mode includes code from previously opened files without permission

### Stress suite

| Test | What it does | What it reveals |
|------|-------------|---------------|
| **Contradiction storms** | Request contradictory edits in rapid succession ("add X" then "remove X") | How the editor handles conflicting instructions, undo history |
| **Near-duplicate floods** | Open 50 similar files and request completions in each | Deduplication quality, index bloat, memory leaks |
| **Temporal paradoxes** | Edit a file, then ask the editor to explain the old version | Temporal reasoning accuracy, context staleness |
| **Concurrent writers** | Multiple editors/agents editing the same file simultaneously | Race conditions, file locking, merge quality |
| **Kill-the-language-server** | Crash the LSP/indexer mid-completion | Recovery, error handling, graceful degradation |
| **Cost-runaway** | Use the editor at maximum intensity for 1 hour | Cost predictability, billing accuracy, rate limits |
| **Monorepo stress** | Open a 500K-line, 10-language monorepo | Indexing time, memory usage, completion quality degradation |

### Upgrade path

**Tested**:
- Can you upgrade from version N to N+1 without losing settings, keybindings, or extensions?
- Are there breaking changes in the API or configuration format?
- Is there a migration guide for breaking changes?
- Does the editor maintain backward compatibility for workspace formats?

### Debugging experience

**Tested**:
- When the editor fails, can you find out why in <5 minutes?
- Are error messages clear and actionable (e.g., "LSP crashed: restart with `Ctrl+Shift+P` → Restart Language Server")?
- Is there a debug mode, verbose logging, or developer console?
- Are there known issues documented for common failures?
- Can you trace which files the editor used as context for a generation?

## Cross-Category Integration Tests

These tests run quarterly and check how code editors work with other tools in a realistic stack:

| Integration | What it tests | Tools involved |
|-------------|-------------|--------------|
| **Code Editor + Agent Framework** | Can the editor's agent mode call the framework's tools? | Code editor, agent framework (e.g., Claude Code + MCP) |
| **Code Editor + Vector DB** | Can the editor use a vector DB for codebase retrieval? | Code editor, vector database |
| **Code Editor + Security Guardrails** | Do guardrails block insecure code generation without breaking flow? | Code editor, security tool |
| **Code Editor + Observability** | Can the editor integrate with tracing/logs for generated code? | Code editor, observability platform |
| **Protocol compliance (MCP/A2A)** | Does the editor implement MCP servers correctly? | Code editor, protocol test suite |

## Scoring

### Per-dimension scoring

Each dimension is scored 0-100 using a rubric. The rubric is published before any scoring happens.

**Example: Accuracy rubric for code editors**

| Score | Criteria |
|-------|----------|
| 90-100 | ≥40% SWE-bench pass@1; ≥90% Exercism pass rate; no critical failures in stress suite |
| 80-89 | 30-40% SWE-bench; 80-90% Exercism; minor failures in stress suite |
| 70-79 | 20-30% SWE-bench; 70-80% Exercism; some stress suite failures |
| 60-69 | 10-20% SWE-bench; 60-70% Exercism; frequent stress suite failures |
| 50-59 | 5-10% SWE-bench; 50-60% Exercism; significant reliability issues |
| 0-49 | <5% SWE-bench or <50% Exercism; fundamentally unreliable for code generation |

**Example: Latency rubric for code editors**

| Score | Criteria |
|-------|----------|
| 90-100 | p50 inline completion <100ms; p95 <300ms; chat TTFT <1s |
| 80-89 | p50 <200ms; p95 <500ms; chat TTFT <2s |
| 70-79 | p50 <400ms; p95 <1s; chat TTFT <3s |
| 60-69 | p50 <800ms; p95 <2s; chat TTFT <5s |
| 50-59 | p50 <1.5s; p95 <4s; chat TTFT <8s |
| 0-49 | p50 >1.5s or chat TTFT >8s; unusable for real-time coding |

### Composite score

The composite score is a weighted average of the seven dimensions:

```
Composite = (Accuracy × 0.25) + (Latency × 0.15) + (TokenEconomics × 0.15) +
            (ScaleBehavior × 0.15) + (OpsBurden × 0.15) + (DevEx × 0.10) +
            (DataSovereignty × 0.05)
```

The composite is used for ranking, but the per-dimension scores are always published. A tool with a high composite but low latency score is a warning sign — it may be accurate but too slow for daily use.

### Confidence intervals

Every score is reported with a confidence interval computed from the standard error across runs. If the intervals overlap between two editors, the difference is not statistically significant. For LLM-based editors, we run at least 3 trials per benchmark to account for temperature variance.

## Reproducibility

### How to reproduce a benchmark

1. Clone the benchmark harness repo (published separately)
2. Check out the exact commit used for the run (recorded in the results JSON)
3. Install the exact dependencies (lockfile is published)
4. Install the exact editor version and extension version (recorded in metadata)
5. Run the harness with the same adapter and same seed
6. Compare your results to the published results

### What is frozen

| Element | How it's frozen | Where to find it |
|---------|---------------|------------------|
| Judge model | Pinned model name and version | `results.json` metadata |
| Judge prompts | SHA-256 hash | `methodology/benchmark-harness.md` |
| SWE-bench split | Held-out task IDs | `methodology/benchmark-harness.md` |
| Exercism problems | Selected problem slugs | `methodology/benchmark-harness.md` |
| Control variables | Documented values | `results.json` metadata |
| Random seeds | Published integer | `results.json` metadata |
| Adapter code | Published in harness repo | Separate repo |
| Test workloads | Published JSON files | `benchmarks/` directory |
| Editor versions | Pinned version string | `results.json` metadata |

### What is NOT frozen (and why)

| Element | Why it changes | How we handle it |
|---------|---------------|------------------|
| Editor versions | Editors update frequently (weekly for some) | We re-run benchmarks for new versions; old results are archived with version tags |
| LLM model versions | Underlying models change (GPT-4 → GPT-4o) | Model version is recorded; results are model-specific |
| Provider pricing | Cloud pricing changes | Cost is computed at runtime using current pricing; historical results are annotated |
| Hardware | We may upgrade machines | Hardware spec is recorded in `results.json`; results are hardware-specific |
| IDE versions | VS Code, JetBrains update | IDE version is recorded; results are IDE-version-specific |

## Failure Mode Taxonomy

Every failure is classified into a taxonomy. This helps identify patterns across editors and highlight systemic issues in the category.

| Category | Failure Modes |
|----------|--------------|
| **Setup** | `install_failed`, `dependency_conflict`, `config_error`, `missing_env_var`, `docs_incomplete`, `auth_failure`, `ide_version_incompatible` |
| **Generation** | `syntax_error`, `hallucinated_api`, `hallucinated_import`, `wrong_type`, `broken_refactor`, `missing_context`, `off_topic_generation` |
| **Latency** | `completion_timeout`, `chat_timeout`, `agent_timeout`, `indexing_lag`, `lsp_crash`, `ui_freeze` |
| **Quality** | `test_failure`, `regression_introduced`, `partial_edit`, `unwanted_side_effect`, `style_violation` |
| **Scale** | `memory_leak`, `cpu_spike`, `index_bloat`, `slow_monorepo`, `context_window_exceeded`, `file_too_large` |
| **Ops** | `upgrade_breaking`, `undocumented_behavior`, `debug_opacity`, `community_unresponsive`, `rate_limit_hit` |
| **Security** | `code_leakage`, `pii_in_prompt`, `insecure_generation`, `secret_exposure`, `untrusted_dependency` |
| **Integration** | `lsp_conflict`, `extension_conflict`, `mcp_noncompliant`, `protocol_mismatch`, `keybinding_override` |

## License

Content: CC BY 4.0  
Code: MIT
