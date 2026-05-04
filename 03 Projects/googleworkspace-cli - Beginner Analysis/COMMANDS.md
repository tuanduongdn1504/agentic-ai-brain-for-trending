# COMMANDS — googleworkspace/cli Wiki

## Build wiki
- "Chạy routine" → follow `05 Skills/llm-wiki-routine.md` v1
- "Phase 2-6" → proceed phase by phase

## Source acquisition
- WebFetch: `https://raw.githubusercontent.com/googleworkspace/cli/main/<path>`
- Key files fetched: README.md, CLAUDE.md (1-liner), AGENTS.md (209 lines), CONTEXT.md (44 lines), skills/ listing (110 folders)
- GitHub repo: github.com/googleworkspace/cli
- Install references:
  - `cargo install --git https://github.com/googleworkspace/cli --locked`
  - `npm install -g @googleworkspace/cli`
  - `brew install googleworkspace-cli`
  - `nix run github:googleworkspace/cli`
  - `gemini extensions install https://github.com/googleworkspace/cli`

## Cross-project
- T4 peer: `../notebooklm-py - Beginner Analysis/02 Wiki/(C) index.md` — v7 T4 N=1 entrant, target for 2-way comparison
- Taxonomy v4 (5-tier): `../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`
- T5 2-way precedent: `../autoresearch - Beginner Analysis/03 Published/(C) T5 2-way comparison + Karpathy meta-reflection.md`
- Routine: `../../05 Skills/llm-wiki-routine.md`

## Key Phase 0 findings — reality checks

| Claim | README | Verified |
|-------|--------|----------|
| 100+ agent skills | ✅ | **110 actual** (44 gws-* + 10 personas + 56 recipes) |
| Services supported | Drive/Gmail/Calendar/Sheets/Docs/Chat/Admin | **11+ (above + Script/Workflow/Events/ModelArmor)** |
| Pre-1.0 | ✅ v0.22.5 | 44 releases, 283 commits |
| Dynamic Discovery | ✅ | Confirmed in AGENTS.md + services.rs registration pattern |

No marketing oversell/undersell gaps caught (unlike codymaster v12). Honest documentation discipline.

## Three agent-facing docs (novel triumvirate)

| File | Audience | Role |
|------|----------|------|
| CLAUDE.md (1 line) | Claude Code contributor | "follow AGENTS.md" pointer |
| AGENTS.md (209 lines) | AI/human contributors | Full contributor guidelines: build/test/changesets/architecture/validation/labels/helpers/env vars |
| CONTEXT.md (44 lines) | AI agents at runtime | "Rules of Engagement": Schema Discovery + Context Window Protection + Dry-Run Safety + Core Syntax |

**First corpus project with distinct CLAUDE.md/AGENTS.md/CONTEXT.md tri-file pattern.** CONTEXT.md is the novel piece — agent-USER rules, not contributor rules.
