# andrej-karpathy-skills — Beginner Analysis

> **Subject:** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) — *"A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls."*
> **Wiki version:** v63
> **Build date:** 2026-05-09
> **Routine:** `llm-wiki-routine-v2.1` (Storm Bear vault)

---

## Phase 0 — Probe summary

### 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Augmentation — single-skill behavioral-guidelines artifact** (NOT curated collection like mattpocock-skills v57; NOT methodology workflow harness like cc-sdd v61; closer to *behavioral-guideline document distributed as Claude Code skill + Cursor rule*) |
| **Archetype** | Solo individual (forrestchang / @jiayuan_jy on X; ALSO founder of [Multica](https://github.com/multica-ai/multica) coding-agents-with-reusable-skills platform) |
| **Scale tier** | **EXTREME-VIRAL** — 121,227 stars / 12,246 forks / 639 watchers / 28 commits / created 2026-01-27 (~102 days at v63 ship 2026-05-09) = **~1,186 stars/day average** = ~3× mattpocock-skills v57 EXTREME-VIRAL velocity (~370 stars/day at observation) |
| **Primary lang** | Markdown only (no code; CLAUDE.md + SKILL.md + EXAMPLES.md + README.md + README.zh.md + CURSOR.md + 2 JSON manifests) |
| **Packaging tool** | 3-way: (1) Claude Code plugin marketplace `/plugin marketplace add forrestchang/andrej-karpathy-skills` + `/plugin install andrej-karpathy-skills@karpathy-skills`; (2) per-project `curl -o CLAUDE.md https://raw.githubusercontent.com/.../CLAUDE.md`; (3) Cursor `.cursor/rules/karpathy-guidelines.mdc` with `alwaysApply: true` |
| **Origin story** | Solo-engineer derivative-distillation of public-figure observations (Karpathy X tweet → 4-principle distillation → 3-platform packaging) |
| **Methodology** | NONE explicit (no spec/plan/task scaffold; no SDD); 4 behavioral principles instead — Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution |
| **Governance file count** | ~9 (README + README.zh + CLAUDE + CURSOR + EXAMPLES + LICENSE-implicit-MIT + plugin.json + marketplace.json + SKILL.md) |
| **Agent/skill count** | **1 skill** (`karpathy-guidelines` only — single-skill plugin, NOT a collection) |
| **i18n coverage** | **EN + ZH bilingual** (README.md + README.zh.md) |
| **Intellectual influence cited** | **YES — explicit Andrej Karpathy X tweet citation** with URL (https://x.com/karpathy/status/2015883857489522876); Karpathy is the **most-corpus-cited individual in Storm Bear vault** (LLM Wiki pattern foundation; autoresearch v8) |
| **Agent platforms supported** | **2** (Claude Code primary + Cursor secondary via `.cursor/rules/`) — corpus-rare cross-platform behavioral artifact |

### Tier placement decision

**T1 Augmentation — single-skill behavioral-guidelines-as-skill sub-archetype.**

Justified by:
- Subject IS a Claude Code skill plus Cursor rule (operates inside host platform; not standalone)
- Function = behavioral-modification overlay on host LLM (anti-overengineering / anti-assumption-silently)
- Granularity = **finer than all prior T1 collections in corpus**: mattpocock-skills v57 (19 skills) > awesome-claude-skills v50 / agent-skills-of-vercel v51 (multi-skill) > **andrej-karpathy-skills v63 (1 skill)** = corpus-finest T1 granularity

**Sub-archetype proposed:** *behavioral-guideline-document-distributed-as-skill* — distinct from curated-collection (mattpocock) and from methodology-harness (cc-sdd / spec-kit).

### Phase 4b PRIMARY routing mode

**🎯 PRIMARY: Pattern #52 EXTREME-VIRAL-VELOCITY OBSERVATIONAL FLAG strengthening N=2 + un-stale-flag candidate at v66 audit**

Pattern #52 was registered N=1 at v50 with mattpocock-skills as trigger; preserved stale-flag at v60 audit Item 12 with re-evaluation at v66 ~6mo age.

**Velocity comparison (corpus EXTREME-VIRAL observations to date):**

| Subject | Stars at observation | Days | Stars/day | Status at v63 |
|---|---|---|---|---|
| mattpocock-skills v57 | ~12K (initial flag) → ~37K at v63 (~93 days) | ~32 → ~93 | ~370 | Pattern #52 N=1 OBSERVATIONAL FLAG |
| **andrej-karpathy-skills v63** | **121,227** | **102** | **~1,186** | **Pattern #52 N=2 strengthening candidate** |
| AutoGPT v59 reference | 184,043 | corpus-historical multi-year | not-EARLY-BURST | Different timeframe |

**Verdict:** Pattern #52 strengthens N=2 with **3× early-burst velocity vs mattpocock baseline**. Open question: does sustained velocity hold past 6mo? mattpocock at ~93 days = barely past 90-day threshold; karpathy-skills at ~102 days = also early-window. Both subjects need 6mo+ check for sustained-vs-burst-only resolution.

**Recommended v66 audit decision:** Promote Pattern #52 from OBSERVATIONAL FLAG to **EXTREME-VIRAL-VELOCITY confirmed** if both N=2 subjects show sustained >100 stars/day at 6mo age. If burst-only-then-decay, keep as OBSERVATIONAL FLAG with sub-variant *early-burst-vs-sustained* split.

### Secondary routing modes

- **Pattern #19 archetype 2 individual-influence-node — Karpathy-derivative-distillation NEW sub-archetype N=1** (distinct from mattpocock author-original v57; this is *derivative-distillation-of-third-party-public-observations* — solo author packages another individual's public reasoning into installable artifact)
- **Pattern #18 Multi-Platform via Format Translation — Claude Code + Cursor cross-platform NEW sub-axis at single-skill scale** (cc-sdd v61 = multi-platform at framework scale; karpathy-skills = multi-platform at single-skill scale; smaller scope but corpus-rare Cursor-secondary observation)
- **Pattern #57 Recursive Corpus Reference 57c-positive-corpus-citation strengthening** — explicit Karpathy citation matches corpus-foundation lineage (LLM Wiki pattern → Storm Bear vault); recursive corpus-cited-individual inheritance
- **Pattern #51 Vibe-Coding Spectrum NEW NEUTRAL-with-anti-overengineering pole observation** — distinct from anti-vibe-discipline (cc-sdd v61); anti-overengineering is narrower critique (overcomplication / speculative features) vs anti-vibe (entire vibe-coding workflow). Spectrum reformulation evidence at v63 (per v60 deferral to v66).
- **Pattern #59 Claude Code Plugin Marketplace Native at solo-individual scale viral** — was OMC v27 + claude-hud v35 solo + codex-plugin-cc v62 corporate (3 prior); andrej-karpathy-skills = 4th. Solo-individual + EXTREME-VIRAL combination corpus-first within Pattern #59.

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check:**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **FAIL** | forrestchang = solo-engineer + Multica founder; not solo-Asian-diaspora-coach archetype, not Scrum-coach archetype. Solo-individual but not archetype-peer dispositive |
| (b) Operational tool for vault | **PASS** (strong) | Directly installable: `/plugin install andrej-karpathy-skills@karpathy-skills` from Claude Code; behavioral guidelines apply to ALL future vault-coding sessions; very low setup cost (~2 min) |
| (c) Methodology-influence-node | **PASS** (strong) | 4 principles = explicit methodology layer (anti-assumption / simplicity-first / surgical-edits / goal-driven); behavioral overlay distinct from any other methodology in corpus |
| (d) In-corpus reference | **PASS-STRONGEST in corpus** | **Andrej Karpathy = most-corpus-cited individual in Storm Bear vault**: LLM Wiki pattern (Karpathy) is the FOUNDATION of vault per CLAUDE.md "Who I Am & My Purpose" section; autoresearch v8 = 1st explicit Karpathy corpus-citation. Karpathy-derivative-distillation = direct corpus-foundation inheritance. |

**Decision: 3-of-4 PASS** ((b)+(c)+(d) clean; (a) fails) → **INCLUDE Storm Bear meta-entity** as 4th entity slot.

**Streak counter:** Storm Bear meta-entity 3-consecutive post-v60-RESTART → v63 advances to **4** (v60 PASS + v61 PASS + v62 PASS + v63 PASS).

**8-instance Phase 0.9 post-amendment window:** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / v63 PASS = **7 PASS / 1 SKIP = 87.5% INCLUDE rate** validates STRICT amendment regularly satisfiable.

---

## Pattern Library implications (preview — Phase 5 will register)

**Direct strengthenings (within already-CONFIRMED or -CANDIDATE patterns):**

1. **Pattern #52 EXTREME-VIRAL-VELOCITY OBSERVATIONAL FLAG N=2 strengthening** — mattpocock v57 + karpathy-skills v63; 3× velocity multiplier on early-burst observation; un-stale-flag candidate at v66 audit if sustained-velocity criterion satisfied
2. **Pattern #19 archetype 2 individual-influence-node — derivative-distillation-of-public-observations NEW sub-archetype N=1 stale-flagged** (distinct from author-original mattpocock + author-original Karpathy himself; this is solo-engineer-distills-public-figure-observations)
3. **Pattern #18 Layer 2 cross-platform-single-skill NEW sub-axis N=1** — Claude Code + Cursor 2-platform at single-skill scale (smaller-scope sister to cc-sdd v61 framework-scale install-time-translator)
4. **Pattern #57 Recursive Corpus Reference 57c — corpus-foundation-individual inheritance** — Karpathy citation in v63 wiki-subject inherits from autoresearch v8 + LLM Wiki pattern foundation; recursive-citation-back-to-corpus-origin
5. **Pattern #59 Claude Code Plugin Marketplace at solo-individual-EXTREME-VIRAL scale** — was solo-individual at low-medium scale (OMC v27 + claude-hud v35); now 1st EXTREME-VIRAL solo-individual marketplace-published plugin

**Counter-evidence / spectrum observations:**

6. **Pattern #51 Vibe-Coding Spectrum NEW pole observation** — anti-overengineering (narrower critique: overcomplication + speculative features) DISTINCT from anti-vibe-discipline (broader workflow critique: cc-sdd v61). Spectrum reformulation evidence supporting v66 deferred deliberation.

**Cross-wiki standards check:**

- **OpenClaw / Hermes runtime:** N/A (Markdown-only behavioral artifact; no runtime)
- **MCP:** NOT mentioned
- **AGENTS.md:** NOT shipped
- **anthropics/skills protocol:** YES — uses SKILL.md frontmatter (`name` / `description` / `license` fields); 1-skill exemplar of Pattern #18 Layer 2
- **CLAUDE.md primitive:** YES — root CLAUDE.md ships as installable behavioral document (corpus-pattern-conformant)

---

## Sources ingested (Phase 2 will write cluster summaries)

1. README.md — 4-principle framework + install (3-way) + Karpathy citation + tradeoff note
2. CLAUDE.md (root, 65 lines) — installable behavioral document
3. SKILL.md (skills/karpathy-guidelines/, 67 lines) — Claude Code skill format with frontmatter
4. EXAMPLES.md (522 lines) — code-driven illustration of all 4 principles with ❌/✅ before-after
5. CURSOR.md — Cursor IDE integration setup
6. .claude-plugin/marketplace.json + plugin.json — Claude Code plugin marketplace metadata
7. .cursor/rules/karpathy-guidelines.mdc — Cursor rule with `alwaysApply: true`
8. Andrej Karpathy X tweet (cited; not directly fetched — citation is sufficient)

---

## Cross-wiki siblings (mandatory cross-references)

**Pattern #52 EXTREME-VIRAL-VELOCITY peer (N=1 baseline):**
- [mattpocock-skills v57](../mattpocock-skills%20-%20Beginner%20Analysis/) — Pattern #52 OBSERVATIONAL FLAG N=1 trigger; ~370 stars/day at observation

**T1 Augmentation peers (skills/behavioral artifacts):**
- [mattpocock-skills v57](../mattpocock-skills%20-%20Beginner%20Analysis/) — 19-skill curated collection (different granularity)
- [awesome-claude-skills v50](../awesome-claude-skills%20-%20Beginner%20Analysis/) — multi-skill curated collection
- [agent-skills-of-vercel v51](../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — corporate-curated collection

**Karpathy-corpus-foundation lineage:**
- [autoresearch v8](../autoresearch%20-%20Beginner%20Analysis/) — 1st explicit Karpathy corpus citation in vault history; LLM Wiki pattern foundation reference

**Multi-platform at single-skill scale peer:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — Pattern #18 install-time-format-translator at framework scale (8 platforms; 2 stable + 5 beta + 1 experimental)

**Claude Code plugin marketplace solo peers:**
- [oh-my-claudecode v27](../oh-my-claudecode%20-%20Beginner%20Analysis/) — Pattern #59 N=1 OMC solo
- [claude-hud v35](../claude-hud%20-%20Beginner%20Analysis/) — Pattern #59 N=2 solo marketplace-only
- [codex-plugin-cc v62](../codex-plugin-cc%20-%20Beginner%20Analysis/) — Pattern #59 N=3 corporate-OpenAI scale

**Anti-overengineering / anti-vibe-spectrum peers:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — anti-vibe-with-pragmatic-acknowledgment (full workflow critique)
- [free-claude-code v60](../free-claude-code%20-%20Beginner%20Analysis/) — Pattern #51 NEUTRAL pole

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources) | ⏳ in progress (3 cluster summaries) |
| Phase 3 (entities) | pending (4 entity pages) |
| Phase 4a (beginner guide bilingual) | pending |
| Phase 4b (Pattern #52 N=2 strengthening + un-stale-flag candidate) | pending |
| Phase 5 (iteration log + Pattern Library update) | pending |
| Phase 6 (vault sync) | pending |
