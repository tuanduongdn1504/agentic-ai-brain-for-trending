# COMMANDS — codymaster Wiki

## Build wiki
- "Chạy routine" → follow `05 Skills/llm-wiki-routine.md` v1
- "Phase 2-6" → proceed phase by phase

## Source acquisition
- WebFetch: `https://raw.githubusercontent.com/tody-agent/codymaster/main/<path>`
- Key files fetched: README.md, README-vi.md, package.json, .claude-plugin/plugin.json
- API listings: skills/ (79 folders), commands/ (11 .md files), docs/ (16 dirs + 4 files)
- Install commands to reference:
  - `claude plugin marketplace add tody-agent/codymaster`
  - `npm install -g codymaster`
  - Cursor: `/add-plugin cody-master`
  - Gemini CLI: `gemini extensions install https://github.com/tody-agent/codymaster`

## Cross-project
- T1 siblings: ECC, Superpowers, gstack, GSD, BMAD (5 peers → 6-way comparison target)
- T1 5-way (v11, pre-codymaster): `../BMAD-METHOD - Beginner Analysis/03 Published/(C) Tier 1 5-way comparison.md`
- Taxonomy v4 (5-tier): `../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`
- BMAD VN comparison point: `../BMAD-METHOD - Beginner Analysis/02 Wiki/(C) VN Localization + Storm Bear Direct Relevance.md`
- Routine: `../../05 Skills/llm-wiki-routine.md`

## Key reality-vs-marketing corrections (Phase 0)

| Claim | README | plugin.json | Actual | Note |
|-------|--------|-------------|--------|------|
| Skill count | "60+ Skills" | "68+ AI agent skills" | **79** (folders in skills/) | Undersells |
| Command count | "20+ Commands" | — | **11** (files in commands/) | Oversells; or CLI `cm` verbs counted separately |
| Version | v6.0.0 (website) | 5.0.0 | 5.1.0 (package) | Rolling channels |
