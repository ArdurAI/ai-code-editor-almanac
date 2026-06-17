# Git Setup & How to Push to GitHub

This repository is intended to be published under the ArdurAI GitHub organization.

## Remote configuration

```bash
# Check current remotes
git remote -v

# If no remote is set, add it (replace with your actual URL)
git remote add origin https://github.com/ArdurAI/ai-code-editor-almanac.git

# Or via SSH
git remote add origin git@github.com:ArdurAI/ai-code-editor-almanac.git
```

## Commit workflow

```bash
# Stage all changes
git add -A

# Commit with a descriptive message
git commit -m "Founding edition: 63 tools, 17 Tier A deep-dives, enriched roster"

# Push to main
git push origin main
```

## Before every commit

- [ ] Run `find . -name '* 2*' -type f` — remove any macOS Finder duplicates
- [ ] Validate `data/roster.json` with `python3 -m json.tool data/roster.json`
- [ ] Check that all `tools/` pages are referenced from the edition or README
- [ ] Ensure empty directories have a `.gitkeep` or README

## Branching

- `main` — the current living edition (always deployable)
- No feature branches for regular monthly updates; use branches for major methodology changes or RFCs

## License

Content: CC BY 4.0  
Code: MIT
