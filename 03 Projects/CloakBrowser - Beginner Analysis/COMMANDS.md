# Commands ref — CloakBrowser v69 wiki build

## Source probes used at Phase 0

```bash
# Repo metadata
curl -s https://api.github.com/repos/CloakHQ/CloakBrowser | jq .

# README raw
curl -s https://raw.githubusercontent.com/CloakHQ/CloakBrowser/main/README.md

# License files
curl -s https://raw.githubusercontent.com/CloakHQ/CloakBrowser/main/LICENSE
curl -s https://raw.githubusercontent.com/CloakHQ/CloakBrowser/main/BINARY-LICENSE.md

# CHANGELOG
curl -s https://raw.githubusercontent.com/CloakHQ/CloakBrowser/main/CHANGELOG.md

# pyproject.toml
curl -s https://raw.githubusercontent.com/CloakHQ/CloakBrowser/main/pyproject.toml

# Org repos list
curl -s https://api.github.com/orgs/CloakHQ/repos | jq -r '.[] | "\(.name) \(.stargazers_count) \(.license.spdx_id // "—")"'
```

## Files NOT FOUND in repo (Phase 0 probe)

- AGENTS.md → 404
- CLAUDE.md → 404
- SKILL.md → 404 (no Anthropic skills protocol presence)

## Phase 2 ingestion targets

- README.md (verbatim) — Cluster 1
- BINARY-LICENSE.md + LICENSE (verbatim) — Cluster 1 license-axis
- CHANGELOG.md (verbatim, last 5-7 versions) — Cluster 2
- examples/ directory listing — Cluster 3
- pyproject.toml + package.json (JS SDK) — Cluster 3

## Vault paths for v69

- Project root: `03 Projects/CloakBrowser - Beginner Analysis/`
- Pattern Library entries: `_patterns/03-active-candidates.md` + `_patterns/05-recent-additions.md`
- State chapter: `_state/03c-projects-v61-v68.md` → rename → `_state/03c-projects-v61-v69.md` at Phase 6 + append v69
- Version log: `_goals/02-version-log.md` append v69
- Root state shim: `CLAUDE.md` post-v69 state-block update
- Pattern Library shim: `PATTERN_LIBRARY.md` post-v69 state-block update
