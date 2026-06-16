# Contributing to the Code Editor Almanac

How to add code editors, fix data, challenge rankings, and improve the methodology.

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Adding a New Code Editor](#adding-a-new-code-editor)
3. [Fixing Data](#fixing-data)
4. [Challenging a Ranking](#challenging-a-ranking)
5. [Improving the Methodology](#improving-the-methodology)
6. [Code of Conduct](#code-of-conduct)
7. [License](#license)

---

## Ways to Contribute

You can contribute to the code editor almanac in several ways:

| Contribution Type | What you do | Impact |
|-------------------|-------------|--------|
| **Add a code editor** | File an issue with a new AI editor or IDE extension | Expands the roster |
| **Fix data** | Correct incorrect metadata (stars, pricing, language support) | Improves accuracy |
| **Challenge a ranking** | Provide evidence that a score is wrong | Drives quality |
| **Share experience** | Write about using an editor in production on a specific codebase | Adds real-world context |
| **Improve methodology** | Propose a better benchmark or scoring rubric for code editors | Improves fairness |
| **Build an adapter** | Implement the adapter for a new code editor | Enables testing |
| **Review an edition** | Proofread, fact-check, suggest improvements | Improves quality |
| **Spread the word** | Share the almanac with your team or community | Grows the ecosystem |

## Adding a New Code Editor

### Before you submit

Check if the editor meets the triage criteria:

1. **Seriousness**: Is it a real AI code editor with real users, not a toy or demo? Does it generate or edit code?
2. **Activity**: Has it had a push, release, or extension update in the last 6 months?
3. **Documentation**: Does it have a README, docs, or landing page explaining installation and features?
4. **Accessibility**: Is it testable (open source, free tier, evaluation license, or installable extension)?
5. **Scope**: Does it fit the code editor category? Must have IDE integration, CLI agent mode, or standalone editor capability.

### How to submit

**Option 1: GitHub Issue (preferred)**

File an issue with this template:

```markdown
## Tool Request: [Editor Name]

### Category
Code Editors & IDE Assistants

### Tool URL
[GitHub repo or homepage URL]

### Type
[IDE | Extension | CLI Agent | Terminal Agent | Web Agent]

### License
[e.g., MIT, Apache-2.0, Proprietary]

### IDE Support
[e.g., VS Code, JetBrains, Zed, Vim, Standalone]

### Languages Supported
[e.g., Python, JavaScript, Rust]

### Pricing Model
[Free | Freemium | Subscription | Enterprise]

### Description
[What does it do? One paragraph. How does it integrate with the IDE?]

### Why it should be on the roster
[Evidence of adoption, production usage, or technical merit.]

### Evidence
- GitHub stars: [N]
- Last release: [date]
- Extension downloads (if applicable): [N]
- Notable users: [companies, if known]
- Funding: [amount, if known]
- Benchmark scores (if published): [SWE-bench, Exercism, etc.]

### Tier suggestion
[A, B, or C — and why]
```

**Option 2: Pull Request**

If you want to add the editor directly:

1. Fork the repo
2. Edit `data/roster.json` to add the editor to the `code-editors` category
3. Include `ide_support`, `languages`, and `pricing_model` fields
4. Update the relevant edition markdown if the editor is Tier A
5. Update `README.md` if the editor is Tier A
6. Submit a PR with the same template as above

### What happens after submission

1. **Triage**: We check if the editor meets criteria (within 7 days)
2. **Smoke gate**: We run the editor through the 3-turn scenario (open file, generate code, verify correctness) within 14 days
3. **Decision**: Accepted, rejected, or deferred with a note
4. **Publication**: If accepted, it appears in the next edition
5. **Adapter**: If Tier A or B, we schedule an adapter build for benchmarking

## Fixing Data

### If you find incorrect metadata

File an issue with:

```markdown
## Data Correction: [Editor Name]

### Current (incorrect) data
[What does the roster say?]

### Correct data
[What should it say?]

### Evidence
[Link to the source that proves the correct data.]
```

### Common corrections for code editors

| Field | Common errors | How to verify |
|-------|--------------|---------------|
| License | Wrong SPDX identifier | Check the repo's LICENSE file or extension marketplace page |
| Stars | Out of date | Check the GitHub API or GitHub repo page |
| Last push | Wrong date | Check the GitHub repo or extension marketplace "Last updated" |
| Tier | Wrong tier | Check the tier rules in IMPLEMENTATION.md and benchmark scores |
| IDE Support | Missing or wrong IDE | Check the tool's docs or extension marketplace (VS Code Marketplace, JetBrains Marketplace) |
| Languages | Missing primary language | Check the tool's docs or run the smoke gate on that language |
| Pricing Model | Changed since last edition | Check the tool's pricing page or blog announcements |
| Notes | Outdated description | Check the tool's homepage/docs for current features |

### What happens after submission

Data corrections are reviewed and applied in the next edition cycle. We don't edit editions retroactively; we correct the data and note it in the next edition.

## Challenging a Ranking

### If you believe a score is wrong

File an issue with:

```markdown
## Challenge: [Editor Name] on [Dimension]

### Current score
[What does the almanac say?]

### Your evidence
[What data do you have?]

### What you did to verify
[Steps you took to reproduce or verify.]

### Suggested resolution
[What should change? Re-run? Different score? Methodology update?]
```

### What evidence is valid

| Evidence Type | Strength | Example |
|---------------|----------|---------|
| Raw results JSON analysis | Strong | "I re-analyzed the JSON and found the adapter used the wrong API endpoint" |
| Independent reproduction | Strong | "I ran the harness on the same SWE-bench split and got 35% vs. your published 28%" |
| Documentation of a bug | Medium | "The editor has a known bug in v0.42 that affects TypeScript completions, which explains the low latency score" |
| Vendor claim | Weak | "The vendor says they score 50% on SWE-bench" — but we already test vendor claims independently |
| Anecdote | Weak | "It worked great for me" — not reproducible and subject to selection bias |
| Screenshots/recordings | Medium | "Video showing the editor taking 5 seconds for a completion on a 10-line file" |

### What happens after submission

1. **Review**: We review the evidence (within 7 days)
2. **Reproduction**: If the claim is reproducible, we re-run the test
3. **Update**: If the re-run confirms the challenge, we update the score
4. **Publication**: The update appears in the next edition

## Improving the Methodology

### If you want to propose a methodology change

File an issue with:

```markdown
## Methodology Proposal: [Title]

### Current state
[What does the methodology say now?]

### Proposed change
[What should it say?]

### Rationale
[Why is this better? What problem does it solve?]

### Impact
[Which editors/categories would be affected?]

### Backward compatibility
[Can old results be re-scored with the new method?]
```

### Methodology change process

1. **RFC**: The proposal is posted as an RFC for public comment (30 days)
2. **Discussion**: Community feedback is collected
3. **Decision**: ArdurAI makes the final decision based on feedback
4. **Announcement**: If accepted, a public announcement is made with a transition plan
5. **Implementation**: The change is implemented in the next edition cycle
6. **Re-run**: Affected benchmarks are re-run with the new methodology

### What kinds of changes are accepted

| Change Type | Likelihood | Example |
|-------------|------------|---------|
| Bug fix in harness | High | "The adapter incorrectly handles timeout for JetBrains plugins" |
| New benchmark | Medium | "Add a new benchmark for SQL generation" |
| Weight adjustment | Medium | "Increase ops burden weight from 15% to 20% because IDE integration pain is underweighted" |
| New dimension | Low | "Add a 'multi-language support' dimension" |
| Remove dimension | Very low | "Remove latency as a dimension" — latency is critical for code editors |

### What kinds of changes are rejected

- Changes that favor a specific vendor or editor
- Changes that reduce reproducibility (e.g., removing temperature=0 requirement)
- Changes that increase complexity without clear benefit (e.g., adding a 10th dimension with 1% weight)
- Changes that are not backward-compatible without a migration plan

### Code editor-specific methodology improvements

We are particularly interested in proposals for:
- **New language tracks** for Exercism (e.g., adding C++, Ruby, or Swift)
- **New benchmark suites** for specific domains (e.g., data science notebooks, infrastructure-as-code, mobile development)
- **Better IDE integration testing** (e.g., measuring extension marketplace install friction, LSP conflict detection)
- **Cost model refinements** (e.g., accounting for "accepted suggestion rate" vs. "generated suggestion rate")
- **Privacy/compliance testing** (e.g., verifying no code leaves the machine in "local mode")

## Code of Conduct

### Be respectful

This is a collaborative project. Treat others with respect, even when you disagree about which editor is best.

### Be evidence-based

Claims should be backed by evidence. "I think X is better" is not enough. "I measured X and found Y" is. For code editors, "I ran the adapter and got Z" is even better.

### Be constructive

Criticism is welcome if it's constructive. "This editor is terrible" is not helpful. "This editor is terrible because it crashes the language server on files >500 lines, and here's the crash log" is.

### Be patient

The almanac is maintained by a small team. Responses may take time. Repeated pings are not helpful. Remember that testing 60+ editors through 3 benchmark suites takes significant time.

### No spam

Don't submit the same editor multiple times. Don't submit editors that clearly don't meet criteria (e.g., a generic ChatGPT wrapper with no IDE integration). Don't use the almanac for marketing.

## License

By contributing to the almanac, you agree that your contributions are licensed under CC BY 4.0 for content and MIT for code.

## Attribution

Contributors are recognized in the edition notes. If you make a significant contribution (e.g., adding 5+ editors, fixing major data issues, building 3+ adapters, improving methodology), you will be listed as a contributor in the next edition.

## License

Content: CC BY 4.0  
Code: MIT
