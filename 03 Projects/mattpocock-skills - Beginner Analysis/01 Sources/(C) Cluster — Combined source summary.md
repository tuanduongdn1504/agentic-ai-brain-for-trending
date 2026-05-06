# Cluster — Combined source summary

> **Scope:** README + CLAUDE.md + CONTEXT.md + .claude-plugin/plugin.json + 3 SKILL.md probes (grill-with-docs / tdd / diagnose) + 1 productivity SKILL (caveman)
> **Compression rationale:** Compressed-scope per v56 lesson (avoid agent-thrash for high-primitive-count repos); single combined cluster summary covers user-facing + contributor-facing + technical/distribution

## 1. Repo positioning verbatim

- Tagline: "Skills for Real Engineers. Straight from my .claude directory."
- README opener: "My agent skills that I use every day to do real engineering - not vibe coding."
- Anti-pattern positioning: "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."
- Design philosophy: "These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience."

## 2. Author + commercial brand

- **Matt Pocock** (Oxfordshire, UK) — TypeScript educator
- Commercial brand: **Total TypeScript** ("comprehensive, production-grade TypeScript course")
- Ex-Vercel + ex-Stately
- 13.9K Twitter followers (@mattpocockuk)
- Newsletter pitched in README: "join ~60,000 other devs on my newsletter" → `aihero.dev/s/skills-newsletter` (commercial-funnel surface)
- Other notable repos: ts-reset (8.5K stars), sandcastle (3.7K stars — "Orchestrate sandboxed coding agents in TypeScript"), dictionary-of-ai-coding (1.1K stars)

## 3. Repo metrics (probe 2026-05-06)

| Metric | Value |
|---|---|
| Stars | 62,000 |
| Forks | 5,300 |
| Watchers | 478 |
| Open issues | 16 |
| Commits | 66 |
| Primary language | Shell (100%) — markdown skill files + shell installer; no TS source |
| License | MIT |

**Velocity observation:** 62K stars / 66 commits ≈ 939 stars per commit. Extreme-density commit-to-star ratio. Time-axis unknown at probe (Pattern #52 OBSERVATIONAL flag).

## 4. Top-level file structure

- `README.md` — primary user-facing doc
- `LICENSE` — MIT 2026 Matt Pocock
- `CLAUDE.md` — bucket-folder organization rules (concise; ~10 lines actual content)
- `CONTEXT.md` — domain-glossary (issue tracker / issue / triage role definitions)
- `scripts/` — shell installer logic
- `skills/` — main skill directory (6 sub-buckets)
- `.claude-plugin/plugin.json` — plugin manifest declaring 13 skills
- `.out-of-scope/` — explicitly-excluded items
- `docs/adr/` — architecture decision records

## 5. Skills directory structure (per CLAUDE.md verbatim)

Skills organized into 6 bucket folders under `skills/`:

| Bucket | Visibility | Purpose |
|---|---|---|
| `engineering/` | Public (README + plugin.json required) | Daily code work |
| `productivity/` | Public (README + plugin.json required) | Daily non-code workflow tools |
| `misc/` | Public (README + plugin.json required) | Kept around, rarely used |
| `personal/` | Hidden (must NOT appear in README/plugin.json) | Tied to author's own setup |
| `in-progress/` | Hidden | Drafts not ready to ship |
| `deprecated/` | Hidden | No longer used |

**Governance discipline:** Each bucket has its own README listing every skill in the bucket. Each skill name in top-level README must link to its `SKILL.md`.

## 6. Active skills list (13 declared in plugin.json)

### Engineering (10)

- `diagnose` — 6-phase debugging loop
- `grill-with-docs` — Grilling session + CONTEXT.md + ADR maintenance
- `triage` — State-machine issue triage
- `improve-codebase-architecture` — Deep-modules audit informed by CONTEXT.md + ADRs
- `setup-matt-pocock-skills` — Interactive per-repo config (issue tracker + triage labels + doc layout)
- `tdd` — Red-green-refactor with vertical-slice tracer-bullet emphasis
- `to-issues` — Break plan/spec/PRD into independently-grabbable GitHub issues
- `to-prd` — Synthesize current conversation into PRD as GitHub issue
- `zoom-out` — Force agent to give higher-level/system-context perspective
- `prototype` — Throwaway prototype (terminal app for state/logic; UI variations for design)

### Productivity (3)

- `caveman` — Ultra-compressed communication mode (~75% token reduction)
- `grill-me` — Relentless interview about plan/design (non-code variant of grill-with-docs)
- `write-a-skill` — Create new skills with structure + progressive disclosure

### Misc (4 — README references; plugin.json count differs)

- `git-guardrails-claude-code` — Claude Code hooks blocking dangerous git commands
- `migrate-to-shoehorn` — Migrate `as` type assertions to @total-typescript/shoehorn (TS-specific; commercial brand integration)
- `scaffold-exercises` — Exercise directory scaffolding (course-creator-tool)
- `setup-pre-commit` — Husky + lint-staged + Prettier + types + tests setup

## 7. Methodology citations in README (verbatim)

5 explicit named-source citations:

1. **David Thomas & Andrew Hunt — The Pragmatic Programmer**
   - Cited 2× in README (problem-#1 + problem-#3)
   - Quotes: "No-one knows exactly what they want" / "Always take small, deliberate steps. The rate of feedback is your speed limit."

2. **Eric Evans — Domain-Driven-Design**
   - Cited in problem-#2 (verbosity)
   - Quote: "With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model."

3. **Kent Beck — Extreme Programming Explained**
   - Cited in problem-#4 (ball of mud)
   - Quote: "Invest in the design of the system every day."

4. **John Ousterhout — A Philosophy Of Software Design**
   - Cited in problem-#4 (ball of mud)
   - Quote: "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."

5. **Anti-pattern foils** (3 prior corpus subjects cited as anti-pattern):
   - **GSD** (corpus v5 + v54)
   - **BMAD** (corpus v11)
   - **Spec-Kit** (corpus v17)
   - Verbatim: "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."

## 8. Distribution surfaces

| Surface | Mechanism |
|---|---|
| GitHub source-of-truth | `mattpocock/skills` repo |
| npm installer | `npx skills@latest add mattpocock/skills` |
| Newsletter funnel | aihero.dev/s/skills-newsletter (~60K subscribers; commercial-funnel) |
| Twitter | @mattpocockuk (13.9K followers) |
| Total TypeScript course | Adjacent commercial offering (paid; 4-figure-USD per-seat typical) |
| Sandcastle (sister repo) | "Orchestrate sandboxed coding agents in TypeScript" (3.7K stars) |

5+ distribution surfaces; commercial-educator multi-channel pattern.

## 9. Plugin.json specifics

- Plugin name: `mattpocock-skills`
- Skills array declares 13 skills (10 engineering + 3 productivity)
- Misc skills NOT in plugin.json (per CLAUDE.md governance: only engineering/productivity required to register; misc may differ — needs verification)
- Plugin manifest is structurally similar to agent-skills-of-vercel v51 plugin manifest pattern

## 10. CONTEXT.md domain-glossary content

Defines 3 core terms:

- **Issue tracker** — platform hosting work units (GitHub Issues / Linear / markdown convention)
- **Issue** — "A single tracked unit of work inside an Issue tracker — a bug, task, PRD, or slice produced by `to-issues`."
- **Triage role** — state-machine labels mapping to actual tracker labels via `docs/agents/triage-labels.md`

Resolved naming conflicts documented:
- "Backlog" no longer = hosting tool (now = Issue tracker)
- "Backlog backend" / "backlog manager" consolidated into "Issue tracker"

**Structural significance:** CONTEXT.md is itself a deliverable + input + skill-required-input — `grill-with-docs` updates CONTEXT.md inline; `tdd` reads CONTEXT.md domain glossary; `improve-codebase-architecture` consults CONTEXT.md + `docs/adr/` decisions.

## 11. Skill-internal patterns (from 4 SKILL.md probes)

### grill-with-docs
- Structured one-question-at-a-time interrogation
- Code-first validation (cross-references stated behavior against actual implementation)
- Lazy documentation (CONTEXT.md only when term resolves; ADRs only when 3 conditions hold: hard-to-reverse + surprising-without-rationale + genuinely-trade-off-driven)
- Multi-context support (CONTEXT-MAP.md for multi-bounded-context systems)

### tdd
- Anti-pattern: horizontal slicing (write-all-tests-then-write-all-code) → produces "crap tests"
- Correct: vertical-slice tracer-bullet (one test → one impl → repeat)
- 4-phase workflow: Planning → Tracer Bullet → Incremental Loop → Refactor
- Cites Kent Beck implicitly + Pragmatic Programmer (small steps)
- References sister sub-docs: `tests.md` / `mocking.md` / `deep-modules.md` / `interface-design.md` / `refactoring.md`

### diagnose
- 6-phase methodology: Build feedback loop → Reproduce → Hypothesize → Instrument → Fix+Regression → Cleanup+Post-Mortem
- "Build a feedback loop. Everything else is mechanical." — explicit core principle
- Targeted-logging discipline (`[DEBUG-a4f2]` prefix tagging for cleanup)
- 3-5 ranked hypotheses with falsifiable predictions before testing

### caveman
- Triggers: "caveman mode" / "talk like caveman" / "use caveman" / "less tokens" / "be brief" / `/caveman`
- Drops: articles + filler + pleasantries + hedging
- Pattern: `[thing] [action] [reason]. [next step].`
- Exception: temporary exit for security/destructive/multi-step-clarity-risk
- Persistence: active until "stop caveman" / "normal mode"

## 12. Cross-corpus pattern observations

- **3rd skills-collection at T1**: awesome-claude-skills v50 (aggregator-curated 100s of community skills) + agent-skills-of-vercel v51 (plugin-manifest aggregation of 24 vendor skills) + mattpocock/skills v57 (opinionated-curated-by-author 13+ skills)
- **Curation-mechanism sub-variant axis emerging**: aggregator-curated (v50) / plugin-manifest-aggregation (v51) / opinionated-curated-by-author (v57)
- **Multi-citation README**: corpus-first multi-frontend in-corpus reference (BMAD v11 + GSD v5/v54 + spec-kit v17)
- **5 methodology book citations**: Pragmatic + DDD + XP + Philosophy of Software Design + (negative) GSD/BMAD/Spec-Kit; structurally distinct from individual-name lineage (Karpathy/Lam/Cherny)
- **Anti-vibe positioning**: most-explicit anti-vibe stance in corpus to date — "real engineering, not vibe coding"
- **Domain-glossary as shared primitive**: CONTEXT.md domain-language doc structurally akin to AGENTS.md / vault CLAUDE.md trend
- **CLI installer + interactive setup**: `/setup-matt-pocock-skills` is sister-pattern to gh-aw v48 / aidevops v47 setup-skill primitives

## 13. Notable absences

- No mention of Karpathy / John Lam / Boris Cherny / Anthropic-team methodology figures (pure book-citation lineage)
- No mention of OpenClaw / Hermes / MCP cross-wiki standards
- No mention of AGENTS.md root-doc convention (uses CLAUDE.md instead)
- No i18n / translations (EN-only)
- No AGENTS.md (uses CLAUDE.md as governance root)
- No academic / research-paper citations (book + corpus-internal-anti-pattern only)

## 14. Supply-chain awareness

- `npx skills@latest add` installer pattern is NOT untrusted-code-ingestion at MCP-server level (Pattern #66 sub-category)
- Each skill is markdown-only (no executable code per skill); installer is shell-based with explicit prompts
- Low supply-chain risk surface; comparable to awesome-claude-skills v50 / agent-skills-of-vercel v51 markdown-only pattern

## 15. Key claim density

- Most-cited single argument: "communication gap" / "misalignment" between dev and agent → grilling-session fix (5+ paragraphs in README + 2 dedicated skills + 1 sister skill)
- Anti-pattern positioning extremely explicit (paragraph 3 of README; 3 corpus subjects named)
- Newsletter funnel CTA appears 1× early in README (~60K subscribers signal)
- Decades-of-engineering-experience claim implicit but consistent throughout
