# Commands ref — codegraph v70 wiki build

## Source probes used at Phase 0

```bash
# Repo metadata
curl -s https://api.github.com/repos/colbymchenry/codegraph | jq .

# Source files
curl -s https://raw.githubusercontent.com/colbymchenry/codegraph/main/README.md
curl -s https://raw.githubusercontent.com/colbymchenry/codegraph/main/CLAUDE.md
curl -s https://raw.githubusercontent.com/colbymchenry/codegraph/main/CHANGELOG.md
curl -s https://raw.githubusercontent.com/colbymchenry/codegraph/main/package.json

# Author profile
curl -s https://api.github.com/users/colbymchenry
```

## Files VERIFIED PRESENT at repo root

- README.md ✅
- CLAUDE.md ✅ (corpus-rare: subject has CLAUDE.md)
- CHANGELOG.md ✅
- LICENSE ✅ (MIT)
- package.json ✅
- tsconfig.json ✅
- vitest.config.ts ✅

## Files NOT FOUND (Phase 0 probe)

- AGENTS.md → not at root (codegraph installer GENERATES AGENTS.md in user's project; corpus-rare observation)
- SKILL.md → not present

## Phase 2 ingestion targets

- README.md (verbatim) — Cluster 1
- CLAUDE.md (verbatim) — Cluster 2 architecture
- CHANGELOG.md (last 10+ versions) — Cluster 3 release history
- package.json — Cluster 3 packaging
- /docs/* — TBD if relevant clusters
- /src/* — TBD architectural references only

## Vault paths for v70

- Project root: `03 Projects/codegraph - Beginner Analysis/`
- Pattern Library entries: `_patterns/03-active-candidates.md` + `_patterns/05-recent-additions.md`
- State chapter: `_state/03c-projects-v61-v69.md` → rename → `_state/03c-projects-v61-v70.md` at Phase 6 + append v70
- Version log: `_goals/02-version-log.md` append v70
- Root state shim: `CLAUDE.md` post-v70 state-block update
- Pattern Library shim: `PATTERN_LIBRARY.md` post-v70 state-block update
