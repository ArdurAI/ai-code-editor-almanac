# Troubleshooting & Debugging

How to understand the code editor almanac codebase, debug issues, and resolve common problems when working with the almanac.

## Table of Contents

1. [Understanding the Codebase](#understanding-the-codebase)
2. [Common Issues](#common-issues)
3. [Debugging the Data Pipeline](#debugging-the-data-pipeline)
4. [Debugging Benchmark Runs](#debugging-benchmark-runs)
5. [FAQ](#faq)
6. [Getting Help](#getting-help)

---

## Understanding the Codebase

### High-level flow

```
Research Agents → Research Output (Markdown) →
  Python Script → roster.json (Structured Data) →
    Manual Review → Edition Markdown →
      Git Commit → GitHub Publication
```

### Key files and their roles

| File | Role | When to read it |
|------|------|-----------------|
| `README.md` | Project overview, quick reference, roster at a glance | First thing you read |
| `INTENT.md` | Philosophy, why we do things this way | When you disagree with a decision or want to understand the mission |
| `IMPLEMENTATION.md` | How things are built, how to add editors, directory conventions | When you want to contribute or add a tool |
| `TESTING.md` | Benchmark methodology, harness details, scoring rubrics | When you want to reproduce or challenge a result |
| `TROUBLESHOOTING.md` | This file | When something is broken |
| `architecture.md` | Stack architecture + test philosophy for code editors | When you want to understand the big picture |
| `editions/YYYY-MM.md` | Monthly snapshot of the code editor landscape | When you want historical data or cost comparisons |
| `data/roster.json` | Machine-readable catalog of 63+ code editors | When you want to query or analyze the data |
| `methodology/benchmark-harness.md` | Harness specification for code editors | When you want to build an adapter or run benchmarks |
| `adapters/` | Code editor adapter implementations | When you want to understand how a specific editor is tested |
| `benchmarks/` | Benchmark results (SWE-bench, Exercism, Terminal-Bench, stress) | When you want to inspect raw results |

### The data model

The almanac is fundamentally a **directed graph** of data:

```
Research findings → Tool metadata → Roster JSON → Edition Markdown → README
                                      ↓
                               Benchmark results → Per-tool pages
```

- **Research findings** are the raw output of the research swarm. They're saved in `research/` (not in the public repo).
- **Tool metadata** is extracted from research and stored in `data/roster.json`.
- **Roster JSON** is the single source of truth. Everything else derives from it.
- **Edition markdown** is human-written based on the roster and research.
- **README** is auto-generated from the roster and the latest edition.

### Understanding `data/roster.json`

This is the most important file in the repo. It is the single source of truth for the code editor catalog.

**Structure**:
```json
{
  "meta": { ... },
  "categories": {
    "code-editors": {
      "name": "Code Editors & IDE Assistants",
      "description": "...",
      "estimated_total": N,
      "tools": [
        { 
          "name": "...", 
          "type": "...", 
          "license": "...", 
          "tier": "A|B|C", 
          "ide_support": ["..."],
          "languages": ["..."],
          "pricing_model": "...",
          "notes": "..." 
        }
      ]
    }
  }
}
```

**How to query it**:
```bash
# Find all Tier A code editors
jq '.categories."code-editors".tools[] | select(.tier == "A") | .name' data/roster.json

# Count tools by tier
jq '.categories."code-editors".tools | group_by(.tier) | map({tier: .[0].tier, count: length})' data/roster.json

# Find all VS Code extensions
jq '.categories."code-editors".tools[] | select(.ide_support | contains(["VS Code"])) | .name' data/roster.json

# Find all open-source tools
jq '.categories."code-editors".tools[] | select(.license | test("MIT|Apache|GPL|BSD"; "i")) | .name' data/roster.json

# Find all Python-supporting editors
jq '.categories."code-editors".tools[] | select(.languages | contains(["Python"])) | {name, tier}' data/roster.json
```

### The edition markdown

Editions are **human-written** summaries, not machine-generated. They are based on the roster but include analysis, interpretation, and narrative that a machine can't produce.

**How editions are structured**:
1. Front matter: date, research method, context (e.g., "Cursor released v0.45 this month")
2. Landscape at a glance: summary table by tier
3. Per-tier sections: findings, roster, analysis, cost comparison
4. Quest diary: what was tested this month (SWE-bench runs, new adapters, stress tests)
5. Cross-category findings: patterns that span the parent almanac's categories

### The benchmark harness (separate repo)

The actual benchmark code lives in a separate repository. The almanac repo contains:
- The methodology specification
- The results (JSON + markdown)
- The adapter interface definitions

The harness repo contains:
- The runner code
- The adapter implementations for each code editor
- The judge model integration
- The telemetry collector (latency, tokens, cost)
- The IDE automation layer (VS Code CLI, JetBrains robot, Playwright for web editors)

**Why separate?** Because the harness is code that runs (and requires IDE installations, API keys, containers), and the almanac is data that is published. They have different lifecycles and different audiences.

## Common Issues

### Issue: `roster.json` is invalid JSON

**Symptoms**:
- `jq` fails to parse it
- GitHub Actions fails on JSON validation
- Python `json.load()` raises `JSONDecodeError`

**Diagnosis**:
```bash
python3 -c "import json; json.load(open('data/roster.json'))"
```

**Resolution**:
1. Find the line with the error: `python3 -m json.tool data/roster.json`
2. Common causes: trailing commas, unescaped quotes in tool names, incorrect nesting of `ide_support` or `languages` arrays
3. Fix the JSON and re-validate
4. Consider using a JSON linter in your editor

### Issue: Edition markdown has broken links

**Symptoms**:
- Links to tools return 404
- Links to benchmarks don't exist yet
- Relative links work locally but break on GitHub
- Links to per-tool pages (`tools/cursor.md`) are dead

**Diagnosis**:
```bash
# Check all links in the repo
find . -name "*.md" -exec grep -oP '\[.*?\]\(.*?\)' {} + | grep -v "http" | grep -v "mailto"
```

**Resolution**:
1. For internal links, use relative paths: `../tools/cursor.md`
2. For external links, verify the URL is correct (editor homepages change)
3. For tools without a per-tool page yet, link to their homepage or GitHub repo
4. Run a link checker as part of CI

### Issue: Tier assignment is wrong

**Symptoms**:
- A tool is Tier A but has no production usage or poor SWE-bench scores
- A tool is Tier C but is widely adopted (e.g., has 50K+ active users)
- A tool's tier changed without explanation in the edition notes

**Diagnosis**:
1. Check the tier assignment rules in `IMPLEMENTATION.md`
2. Verify the tool's adoption (GitHub stars, Discord members, download counts), activity, and community health
3. Check the edition notes for the rationale
4. Check the benchmark results — a tool with poor accuracy may be Tier C even if popular

**Resolution**:
1. File an issue with evidence (GitHub stars, last push, production references, benchmark scores)
2. The tier will be reviewed in the next edition cycle
3. Tiers are not changed mid-edition; they are updated at edition boundaries

### Issue: Benchmark results can't be reproduced

**Symptoms**:
- Running the harness produces different SWE-bench pass rates
- The adapter fails with a different editor version
- The judge model is unavailable or changed
- Inline completion latency differs by 2x

**Diagnosis**:
1. Check the `results.json` metadata for the exact editor version, extension version, IDE version, commit, seed, and hardware
2. Check if the editor version has changed since the published run (editors update frequently)
3. Verify the judge model is accessible and pinned to the exact version
4. Check if the LLM temperature was set to 0 (required for reproducibility)
5. Check network conditions — cloud editors may have variable latency

**Resolution**:
1. Use the exact editor version, extension version, and IDE version from the results metadata
2. If the editor version changed, the results are for a different version — this is expected; rerun and compare
3. If the judge model changed, that's a methodology issue — file an issue
4. Set temperature to 0 for all LLM calls in the adapter
5. Run multiple trials and report confidence intervals

### Issue: Adapter fails on IDE integration

**Symptoms**:
- `setup()` crashes because the IDE is not installed
- `open_workspace()` hangs because the language server never initializes
- `request_completion()` fails because the extension API changed
- `apply_edit()` fails because the editor uses a different file format

**Diagnosis**:
1. Check if the IDE (VS Code, JetBrains, Zed) is installed at the expected path
2. Check if the extension is installed and enabled
3. Check the extension version — APIs change between versions
4. Check the IDE logs for LSP crashes or extension errors
5. Check if the workspace has a valid project structure (e.g., `package.json`, `Cargo.toml`)

**Resolution**:
1. Install the exact IDE version specified in the adapter metadata
2. Install the extension from the exact source (marketplace vs. VSIX vs. bundled)
3. Update the adapter to match the new extension API if needed
4. Start the language server manually if the adapter doesn't auto-start it
5. Use a Docker container with a pinned IDE + extension image for reproducibility

### Issue: Benchmark results inconsistent due to LLM temperature

**Symptoms**:
- Same editor, same SWE-bench task, different pass/fail across runs
- Exercism scores vary by >10% between runs
- Chat responses vary significantly in structure

**Diagnosis**:
1. Check if the adapter sets `temperature=0` for all LLM API calls
2. Check if the editor has its own temperature setting that overrides the adapter
3. Check if the editor uses a non-deterministic sampling method even at temperature 0

**Resolution**:
1. Force `temperature=0` and `seed` in all LLM calls in the adapter
2. If the editor doesn't expose temperature control, note this in the results metadata
3. Run at least 3 trials per task and report the average and confidence interval
4. For non-deterministic editors, report the range (min/max) rather than a single point

### Issue: Tool not found in triage

**Symptoms**:
- A well-known AI editor is not in the roster
- A tool from a specific region (e.g., China, EU) is missing
- A newly launched editor is not in the latest edition

**Diagnosis**:
1. Check if the tool meets triage criteria in `IMPLEMENTATION.md`
2. Check if it was added in a previous edition and later removed (search edition history)
3. Check if it falls outside the search scope (e.g., pure web playground with no IDE integration)

**Resolution**:
1. File an issue with the tool name, URL, and evidence of adoption/activity
2. The tool will be triaged for the next edition
3. If it meets criteria, it will be added

### Issue: Monthly update cron failed

**Symptoms**:
- No new edition was published on the 15th
- The cron job is missing from the scheduler
- The research agent timed out
- The benchmark harness failed mid-run

**Diagnosis**:
```bash
# Check cron status
cron status

# Check the cron job list
# (use the Kimi Work cron interface)
```

**Resolution**:
1. Check if the cron job is still registered
2. Check if the research agent timed out (increase timeout if needed)
3. Check if the benchmark harness failed — review harness logs for adapter crashes
4. Manually trigger the update if the cron missed a cycle
5. Check the workspace path in the cron job configuration

### Issue: GitHub push fails

**Symptoms**:
- `git push` returns 403 or 401
- The remote is not configured
- The branch is behind origin
- Large binary files (screenshots, videos) exceed GitHub's size limit

**Diagnosis**:
```bash
git remote -v
git status
git log --oneline -5
du -sh assets/
```

**Resolution**:
1. Verify the remote URL is correct: `git remote set-url origin https://github.com/ArdurAI/...`
2. Verify GitHub CLI auth: `gh auth status`
3. If behind origin, pull first: `git pull origin main`
4. If there are conflicts, resolve them manually
5. If assets are too large, use Git LFS or compress images

## Debugging the Data Pipeline

### Research output → roster.json

**Problem**: Research agents produce markdown, but the roster JSON is incomplete or wrong.

**Debug steps**:
1. Read the research output files in `research/` (local workspace, not in the repo)
2. Check if the Python extraction script correctly parsed the editor tables
3. Check if tools were dropped during triage (check the triage log)
4. Verify the JSON schema is correct (especially `ide_support` and `languages` arrays)

**Common bugs**:
- Tool names with special characters (e.g., "Qwen Code CLI") break JSON parsing → Escape them properly
- Tools with no `ide_support` get dropped → Default to `["Standalone"]` if unsure
- Tools with no `languages` get empty arrays → Research the primary language support
- Tools with no tier get dropped → Default to Tier C if unsure
- Tools with no notes get empty strings → Add a minimal note

### roster.json → edition markdown

**Problem**: The edition doesn't reflect the roster.

**Debug steps**:
1. Compare the tool counts in the roster vs. the edition
2. Check if the edition was written before the roster was updated
3. Check if tools were manually edited in the edition but not in the roster

**Resolution**:
1. The edition should be derived from the roster, not the other way around
2. If the edition has manual additions, ensure they are also in the roster
3. The edition is a human-readable summary; the roster is the source of truth

### Edition markdown → README

**Problem**: The README roster-at-a-glance doesn't match the latest edition.

**Debug steps**:
1. Check which edition is referenced in the README
2. Check if the README was updated after the edition was published

**Resolution**:
1. The README should always reference the latest edition
2. Update the README when a new edition is published
3. Consider automating README updates from the roster JSON

## Debugging Benchmark Runs

### The adapter fails

**Symptoms**:
- `setup()` crashes (IDE not found, extension fails to install)
- `open_workspace()` throws an exception (language server crashes)
- `request_completion()` returns nothing or garbage (extension not loaded)
- `request_generation()` times out (LLM API rate limit)

**Debug steps**:
1. Run the adapter in isolation (without the harness) using a minimal test script
2. Check the tool's documentation for setup requirements (IDE version, OS, dependencies)
3. Check if environment variables are set (API keys, auth tokens, paths)
4. Check if the editor version matches what the adapter expects
5. Check IDE logs: VS Code (`~/.config/Code/logs/`), JetBrains (`Help → Show Log in Finder`)

**Common fixes**:
- Missing IDE installation → Install the exact version specified
- Missing extension → Install from marketplace or VSIX
- Missing API key → Set the environment variable (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`)
- Wrong editor version → Update the adapter or pin the version in the metadata
- Dependency conflict → Use a virtual environment, container, or separate IDE profile
- Language server crash → Restart the LSP, increase memory, or check for conflicting extensions

### The canary fails

**Symptoms**:
- The no-tool baseline scores above zero on code generation
- The inline completion returns non-empty results without an editor
- The abstention score is not 1.000

**Debug steps**:
1. Check if the benchmark workload has leaked answers (e.g., test files contain solution code)
2. Check if the grading pipeline has a bug (judge model hallucinating a score)
3. Check if the random seed was set
4. Check if a default IDE extension is auto-installed and interfering

**Resolution**:
1. If the workload leaked answers, redesign the test cases (remove solution code from repo)
2. If the grader has a bug, fix the grader and rerun all tests
3. If an extension is auto-installed, disable it in the canary adapter
4. This is a critical failure — the entire batch is invalid

### Results are inconsistent

**Symptoms**:
- Same editor, same test, different results across runs
- Scores vary by more than the confidence interval
- SWE-bench pass rates differ by >5% between runs

**Debug steps**:
1. Check if the editor has non-deterministic behavior (temperature > 0, top-p > 0, async timing)
2. Check if the hardware was different between runs (different machines, different load)
3. Check if the editor version changed between runs (auto-updates)
4. Check if the LLM model version changed (cloud providers silently update models)
5. Check network conditions for cloud-based editors

**Resolution**:
1. Set temperature to 0 and seed to a fixed integer for all LLM calls in the adapter
2. Record hardware specs in the results metadata
3. Pin editor versions and disable auto-updates during testing
4. Record the LLM model version from API responses
5. Run multiple trials and report confidence intervals

## FAQ

### Q: Why is editor X not in the roster?

A: Either it doesn't meet triage criteria (no IDE integration, no real users, no releases in 6+ months), it hasn't been discovered yet, or it was removed for inactivity. File an issue with evidence (homepage URL, GitHub stars, download counts, screenshots) and we'll triage it.

### Q: Why did editor X's score change?

A: Either the editor was updated (new version, new model), the methodology was refined (new SWE-bench split, new judge prompt), or we found a bug in our previous test (adapter fix, temperature correction). All three are valid reasons. Check the edition notes for the rationale. Code editors move fast — scores can shift month to month.

### Q: Can I run the benchmarks myself?

A: Yes. The harness is published separately. Clone it, install the IDE and extension versions specified in the metadata, set your API keys, and run the adapter for the editor you want to test. See `TESTING.md` for reproducibility instructions. Note: Some proprietary editors (Cursor, Copilot) may require subscriptions.

### Q: How do I challenge a ranking?

A: File an issue with specific evidence. Check the raw results JSON (every prompt and response is there), the adapter code (you can see how the editor was driven), and the judge prompts (frozen and hashed). If you find a real problem (e.g., "Adapter X used the wrong API version for Editor Y"), we'll re-run or update the methodology.

### Q: Can I add an editor to the roster?

A: Yes. See `CONTRIBUTING.md` for instructions. The editor must meet triage criteria (real IDE integration, real users, active development) and pass the smoke gate (open file, generate code, verify correctness).

### Q: Why are there separate category almanacs?

A: Each category is deep enough to warrant its own dedicated repo with per-tool pages, category-specific benchmarks, and focused community. The code editor category alone has 63+ tools with complex IDE integrations, language support matrices, and pricing models. The parent almanac is the master catalog.

### Q: How often are benchmarks re-run?

A: Standard: every quarter for each editor. Stress: annually. Integration: quarterly. If an editor releases a major version (e.g., Cursor 0.5x, Copilot major update), we may re-run early. Inline completion latency is measured monthly because it's sensitive to model updates.

### Q: What's the difference between Tier A, B, and C?

A: Tier A = market leader or strongest technical merit on SWE-bench/accuracy. Tier B = solid option, specific use cases (e.g., privacy-first, self-hosted, language-specific). Tier C = niche, early-stage, or has significant limitations. See `IMPLEMENTATION.md` for full rules.

### Q: Can vendors sponsor the almanac?

A: No. The almanac is independently funded. Sponsorship would compromise the core mission. Vendors can improve their scores by actually improving their editors (better SWE-bench scores, lower latency, lower cost).

### Q: Why does my favorite editor score lower than I expected?

A: Possible reasons: (1) The adapter may not use the editor's optimal mode (e.g., we test chat mode, but you use agent mode); (2) The benchmark may test a weakness of that editor (e.g., polyglot support when it's Python-only); (3) The editor may have regressed since you last used it; (4) The score reflects ops burden or cost that you don't personally experience (e.g., enterprise SSO issues). Check the per-dimension breakdown — the editor may be excellent on accuracy but poor on latency or data sovereignty.

### Q: How do you handle editors with different IDE support?

A: We test the primary IDE/platform advertised by the vendor. If an editor supports VS Code and JetBrains, we test both and report the better score, but note the IDE used. If an editor only supports one IDE, that's part of the "Developer Experience" and "Ops Burden" scores — forcing your team to switch IDEs is a real cost.

## Getting Help

### File an issue

GitHub issues are the primary support channel. Use the appropriate template:

- **Tool request**: "Add [Editor Name] to roster"
- **Data correction**: "[Editor Name] metadata is wrong: [what's wrong]"
- **Benchmark challenge**: "Challenge [Editor Name] ranking on [Dimension]: [evidence]"
- **Bug report**: "[Bug description] in [file/process]"
- **Feature request**: "[Feature description] for [use case]"
- **Adapter issue**: "[Editor] adapter fails on [setup/query/teardown]"

### Discussion

GitHub Discussions are for:
- General questions about the almanac
- Sharing experiences with editors on the roster
- Proposing methodology changes (e.g., "Add a new benchmark for mobile development")
- Community announcements (e.g., "I built an adapter for Editor X")

### Email

For private or sensitive inquiries: Use the contact info in the ArdurAI org profile.

## License

Content: CC BY 4.0
