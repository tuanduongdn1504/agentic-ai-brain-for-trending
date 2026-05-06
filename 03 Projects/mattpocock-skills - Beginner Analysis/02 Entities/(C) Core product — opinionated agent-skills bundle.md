# Entity 1 — Core product: opinionated agent-skills bundle

## 1. Identity

- **Name:** mattpocock/skills
- **Subtitle:** "Skills For Real Engineers" (verbatim repo title)
- **Tagline:** "Skills for Real Engineers. Straight from my .claude directory."
- **Author:** Matt Pocock — TypeScript educator, founder of Total TypeScript, ex-Vercel + ex-Stately
- **Date probed:** 2026-05-06
- **GitHub URL:** github.com/mattpocock/skills

## 2. Purpose

Opinionated curated collection of 13 active agent skills (10 engineering + 3 productivity) + 4 misc, designed to address what Matt explicitly identifies as 4 common failure modes in AI-assisted development:

1. Misalignment between dev intent and agent output (fix: grilling-session skills `/grill-me` + `/grill-with-docs`)
2. Excessive agent verbosity due to lack of shared domain vocabulary (fix: CONTEXT.md domain-glossary + `/grill-with-docs` integration)
3. Code that doesn't work (fix: TDD red-green-refactor + diagnose 6-phase debugging loop)
4. Architectural ball-of-mud (fix: `/improve-codebase-architecture` + `/zoom-out` + deep-modules philosophy)

## 3. Tier placement

**T1 Assistant** — these skills install into Claude Code / Codex / generic-agents and operate as in-conversation invokable primitives. Not service (T2). Not education-content (T3). Not infrastructure-bridge (T4). Not application (T5).

**Sub-classification:** opinionated-curated-by-author skills-collection at T1. Distinct from:
- v50 awesome-claude-skills — aggregator-curated (community submissions, 100s of skills)
- v51 agent-skills-of-vercel — plugin-manifest-aggregation (24 vendor skills, organized by Vercel)
- v57 mattpocock/skills — opinionated-curated-by-author (13+ skills, single authorial voice + commercial-educator backing)

## 4. Architecture

### Bucket-folder discipline

Per `CLAUDE.md` (verbatim from repo root): 6 bucket folders under `skills/`:

```
skills/
├── engineering/      ← public; README + plugin.json required
├── productivity/     ← public; README + plugin.json required
├── misc/             ← public; README + plugin.json required
├── personal/         ← hidden; must NOT appear in README/plugin.json
├── in-progress/      ← hidden; drafts not ready
└── deprecated/       ← hidden; no longer used
```

**Each public bucket has its own README** listing every skill with one-line description; skill name in top-level README must link to its `SKILL.md`.

### Per-skill structure

Each skill = single `SKILL.md` markdown file (no executable code per skill; markdown-only). Some skills include sister sub-docs (e.g., `tdd/` includes `tests.md` / `mocking.md` / `deep-modules.md` / `interface-design.md` / `refactoring.md`).

### Plugin manifest

`.claude-plugin/plugin.json` declares 13 skills as plugin entries (10 engineering + 3 productivity). Misc skills not formally in plugin.json (per repo CLAUDE.md governance — needs structural verification).

### Per-repo configuration setup

`/setup-matt-pocock-skills` is the entry-point skill for new-repo adoption:
1. Asks which issue tracker (GitHub / Linear / local files)
2. Asks triage label vocabulary
3. Asks where to save generated docs (CONTEXT.md / ADRs / triage-labels mapping)

Generates `docs/agents/triage-labels.md` mapping Triage role → tracker label, plus repo-level CONTEXT.md scaffolding when needed.

## 5. Distribution

| Surface | Mechanism | Audience |
|---|---|---|
| GitHub source-of-truth | mattpocock/skills repo (62K stars) | Direct GitHub users |
| npm installer | `npx skills@latest add mattpocock/skills` | Claude Code / Codex / agent users |
| Newsletter | aihero.dev/s/skills-newsletter (~60K subscribers) | Commercial-funnel + skill-update broadcast |
| Twitter | @mattpocockuk (13.9K followers) | Author-personal-brand surface |
| Total TypeScript course | Adjacent paid commercial offering | TS-educator commercial-brand cross-promotion |
| Sandcastle (sister repo) | "Orchestrate sandboxed coding agents in TypeScript" (3.7K stars) | Adjacent technical product |

5+ distribution surfaces; commercial-educator multi-channel pattern.

## 6. Governance signature

- **Light-Medium per Pattern #12 refined v42 3-factor formulation**:
  - Authority concentration: high (single-author + commercial-brand-backing + 13.9K-Twitter-follower personal authority)
  - Process formality: medium (CLAUDE.md governance rules + plugin manifest discipline + bucket-folder visibility rules; but no contributor RFC process)
  - Documentation depth: medium-high (per-skill SKILL.md + sister sub-docs + CONTEXT.md domain-glossary + docs/adr/ ADRs)
- 16 open issues = low-but-active churn (62K-star repos typically have higher issue volume; suggests author actively closes)
- 66 commits = velocity-burst signature, not slow-build

## 7. Methodology stack

5 explicitly-cited intellectual sources:

1. **Pragmatic Programmer** (Hunt + Thomas) — feedback loops, small deliberate steps, "no one knows exactly what they want"
2. **Domain-Driven Design** (Eric Evans) — ubiquitous language, shared vocabulary
3. **Extreme Programming Explained** (Kent Beck) — invest in design every day
4. **A Philosophy Of Software Design** (Ousterhout) — deep modules, simple interfaces deep implementations
5. **Anti-pattern foils** (negative citations): GSD + BMAD + Spec-Kit (3 prior corpus subjects cited as "approaches that take away your control")

**Pattern #19 archetype 4 strengthening:** named-source lineage via book-citation is structurally distinct from individual-name lineage (Karpathy / Lam / Cherny / Anthropic-team). Five-book curated-citation-set is a corpus-first authorial signature mechanism.

## 8. Pattern Library positioning

- **Pattern #18 horizontal-aggregation N=3 candidate** — 3rd skills-collection at T1 with curation-mechanism sub-variant divergence (aggregator-curated v50 / plugin-manifest v51 / opinionated-curated-by-author v57)
- **Pattern #51 Vibe-Coding Spectrum anti-vibe pole** — most-explicit anti-vibe positioning in corpus to date ("real engineering, not vibe coding")
- **Pattern #57 57c forward-citation-then-wiki STRONGEST evidence** — multi-frontend citation in single README (BMAD + GSD + spec-kit cited as anti-pattern foils — see entity 2)
- **Pattern #19 archetype 4** strengthens via 5-book named-lineage citation set
- **Pattern #29** MIT — standard-OSI; baseline-fits
- **Pattern #2** 5+ distribution surfaces — corpus-typical breadth
- **Pattern #50 Commercial-Funnel Companion Platform 50a Standard sub-variant** — newsletter + Total TypeScript course = adjacent commercial offerings (50a observation strengthening)
- **Pattern #69 Primitive-count taxonomy** — 6 bucket folders + 13 active skills + 4 misc = LARGE tier (not EXTREME 7+)

## 9. Cross-wiki references

- **v50 awesome-claude-skills** — 1st skills-collection at T1; aggregator-curated mechanism distinct
- **v51 agent-skills-of-vercel** — 2nd skills-collection at T1; plugin-manifest-aggregation mechanism distinct
- **v11 BMAD-METHOD** — cited by mattpocock/skills as anti-pattern foil
- **v5 get-shit-done + v54 gsd-2** — cited (as "GSD") by mattpocock/skills as anti-pattern foil
- **v17 spec-kit** — cited by mattpocock/skills as anti-pattern foil
- **v56 n8n** — most-recent prior wiki; v57 extends 20-streak → 21-streak
- **v55 automate-faceless-content** — prior abandoned-author cautionary contrast (v57 inverts: actively-maintained-commercial-educator)

## 10. Strengths (corpus-relative)

1. **Smallest-coherent-set discipline** — 13 active skills vs awesome-claude-skills v50 hundreds; opinionated curation is signal-over-noise
2. **Multi-platform-by-design** — explicit "any model" claim + interactive installer abstracts target agent
3. **Methodology-grounded** — 5 named book citations + corpus-internal anti-pattern foils = strongest documented intellectual lineage in skills-collection sub-class
4. **CONTEXT.md domain-glossary primitive** — explicit shared-language artifact maintained by skill-set itself (`/grill-with-docs` updates inline)
5. **Lazy-ADR discipline** — explicit 3-condition gate (hard-to-reverse + surprising + trade-off-driven) prevents ADR sprawl
6. **MIT license** — minimal commercial-use friction

## 11. Weaknesses / risks (corpus-relative)

1. **Single-author bus-factor** — entirely Matt Pocock authored; no co-maintainer surface
2. **Commercial-educator coupling** — newsletter signup + Total TypeScript course = funnel mechanics (not strictly anti-pattern but axis-of-bias signal)
3. **EN-only** — no i18n
4. **No AGENTS.md** — uses CLAUDE.md as governance-root; misses cross-wiki standard convention
5. **TS-bias** — `migrate-to-shoehorn` skill is TS-specific commercial-brand integration; some skills implicitly assume TS ecosystem familiarity
6. **`/triage` requires interactive setup** — friction for casual single-skill-grab usage

## 12. Storm Bear deployment fit

**Direct deployable in vault workflows:**
- `/grill-me` + `/grill-with-docs` — client-discovery sessions; brain-setup-style routines
- `/tdd` — software-build practice (vault uses TDD-adjacent disciplines via routine v2.1 fact-verification)
- `/triage` — backlog management (vault has v27 HIGH bundle backlog tracking; could deploy)
- `/to-prd` + `/to-issues` — sprint-planning artifact generation
- `/improve-codebase-architecture` — vault-refactor audit pattern (session 67 was structurally this)
- `/zoom-out` — strategic-thinking skill complement to vault routine v2.1
- `/diagnose` — 6-phase methodology directly applicable to wiki-build agent-thrash diagnosis (session 67 v56 n8n 5-failure pattern)
- `/caveman` — token-economy mode for context-budget-pressured vault operations

**Vault-skill-overlap observations:**
- `brain-setup.md` (vault skill) ↔ `/grill-me` (mattpocock/skills) — same pattern, different lineages; 2nd interview-as-skill convergence in corpus
- `llm-wiki-routine-v2.1.md` (vault skill) ↔ `/to-prd` (mattpocock/skills) — both = synthesize-conversation-to-artifact

## 13. Next-step recommendation

Vault should evaluate `/grill-with-docs` for explicit adoption — it's structurally akin to vault `brain-setup.md` interview pattern but with continuous CONTEXT.md maintenance (which vault currently does NOT systematically do). Possible cross-skill-port: vault `brain-setup-v2.md` candidate that extends current 5-round interview with continuous-glossary-maintenance discipline borrowed from `/grill-with-docs`.
