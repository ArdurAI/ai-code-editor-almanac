# SWE-bench Baseline

SWE-bench baseline for the Code Editors & IDE Assistants Almanac.

## Split

We use a **held-out split** of 50 tasks not present in the training data of major LLMs. The split is verified via n-gram analysis against publicly available training corpora.

**Task distribution:**
- Bug fixes: 20 tasks
- Feature additions: 15 tasks
- Refactoring: 15 tasks

## Task IDs

The held-out task IDs are stored in `methodology/benchmark-harness.md` (SHA-256 frozen). They are not published here to prevent contamination.

## Baseline results

| Editor | Pass@1 | Pass@k | Avg Tokens/Task | Date | Notes |
|--------|--------|--------|-----------------|------|-------|
| — | — | — | — | — | Baseline not yet run. Adapters are skeletons; harness runner is separate. |

## Published vs. reproduced

Every standard benchmark ranking ships a comparison table:

| Editor | Published Claim | Our Result | Delta | Verdict |
|--------|----------------|------------|-------|---------|
| Cursor | — | — | — | — |
| Claude Code | SWE-bench 82% | — | — | — |
| OpenHands | — | — | — | — |

## How to run

The SWE-bench harness is in a separate repo (benchmark harness). This directory only holds the results.

```bash
# From the benchmark harness repo:
python harness.py --suite swe-bench --adapter cursor --split held-out-50
python harness.py --suite swe-bench --adapter copilot --split held-out-50
python harness.py --suite swe-bench --adapter claude-code --split held-out-50
```

Results are copied here as `<editor>-swe-bench-<date>.json`.

## Archive policy

Old results are never deleted. They are the audit trail. Each result is tagged with:
- Editor version
- Model version
- Harness commit SHA
- Hardware spec
- Random seed
