# (C) Log — build-your-own-x Wiki

---

## [2026-04-18] setup | Phase 0+1 — Pre-flight + Scaffold (8th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (8th auto-execution — **first outside-taxonomy meta-reference**)
- **Phase 0 pre-flight (API-probe-first per routine v2 rule from v6 retries):**
  - ✅ GitHub API HTTP 200
  - Size: **1,201 KB (~1.2 MB)** — tiny, README is entire content
  - **Stars: 491,391** — highest in corpus (7x notebooklm-py's 11K)
  - **Forks: 46,424** — massive community
  - License: CC0 (public domain)
  - Language: Markdown
  - Default branch: **master** (old-style, predates `main` convention)
  - Pushed: 2026-02-21 (2 months stale, moderate)
  - Fork: false, Archived: false
  - Root contents: just README.md (46.5 KB) + ISSUE_TEMPLATE + .gitattributes + banner PNG
  - **Sibling detection: 7 projects** — all agent-related
  - **Domain classification: OUTSIDE AGENT TAXONOMY** → meta-reference (general programming education aggregator)
  - **Phase 4b routing = meta-reference positioning** (NEW routing mode: outside-scope, not taxonomy extension)

- **Phase 1 scaffold:**
  - Project folder created via `mkdir -p`
  - 8 subfolders created
  - Source acquisition: WebFetch (tiny repo, README-only)

- **WebFetch source acquired:**
  - README.md — Feynman tagline, 28 primary categories + Uncategorized + Distributed Systems mention, format `[**Language**: _Title_](URL)`, CodeCrafters Inc. current maintenance, Daniel Stefanovic origin, CC0 license, PR/issue contribution flow

- **Unique findings:**
  - **491K stars** — iconic repo, top of all 8 corpus items (7 agent wikis combined ≈ 80K stars vs this 1 = 491K)
  - **Single-file architecture** — entire knowledge base = 1 README (unique in corpus)
  - **CodeCrafters paradox** — company sells paid courses + maintains free aggregator = interesting business model
  - **Flat categorization** — 29 categories, no nesting
  - **Feynman framing** — learning philosophy baked into positioning
  - **Contribution-based growth** — 491K stars from community PRs over years
  - **Language diversity explicit** — every entry tagged với language
  - **No AI/agent content** — categories include Neural Network but as "build your own" (understanding fundamentals), not "use AI agent framework"
  - **Meta-pattern for Storm Bear** — this repo IS a curated knowledge aggregator, same meta-pattern as Storm Bear vault itself but at different scale (491K stars vs 1 user)

- **Source strategy (unusual — single README):**
  1. README positioning summary (tagline, philosophy, meta-info)
  2. 29 Categories catalog (the actual catalog content)
  3. Governance + Curation cluster (CodeCrafters/Daniel/CC0/contribution)

- **Meta-reference framing decision:**
  - **NOT proposing Tier 5** — avoids tier inflation and conflation của "catalog of ANY topic" với "agent-as-service" tiers
  - **INSTEAD framing as OUTSIDE SCOPE** — acknowledges this is different axis (general programming vs agent ecosystem)
  - **PRIMARY VALUE** = Phase 4b extracts knowledge organization lessons Storm Bear can apply to vault itself
  - Unique entity page: `(C) Storm Bear Vault — Knowledge Architecture Lessons`

- **Phase 0+1 status:** ✅ COMPLETE
- **Next:** Phase 2 source summaries

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 files from single README)

- **Source #1:** `(C) README positioning summary.md` — Feynman tagline ("What I cannot create, I do not understand"), single-file architecture (46KB README = entire content), 29 categories list, entry format `[**Language**: _Title_](URL)`, language coverage analysis (JS/Python/C/C++/Go/Rust dominant), contribution model via PR, CodeCrafters Inc. maintenance + Daniel Stefanovic origin, CC0 license, signals of quality, risks
- **Source #2:** `(C) 29 Categories catalog summary.md` — all 29 categories organized in 7 clusters (systems/web/AI/creative/tools/automation/blockchain + catchall), size distribution (power law: Database/Programming Language 10+ entries, Memory Allocator 1 entry), language coverage matrix per category, graduation dynamics (Uncategorized → promoted), deprecation patterns, what's NOT covered (mobile/security/DevOps gaps)
- **Source #3:** `(C) Governance + Curation cluster summary.md` — origin + ownership (Daniel → CodeCrafters 2022), CC0 vs MIT license decision rationale, PR flow detailed, implicit quality criteria, curator + community + infrastructure role split, business model (paid courses fund free aggregator), 10-year evolution phases, governance risks
- **Key findings:**
  1. **Single-file architecture works at 491K-star scale** — challenges Storm Bear's multi-file assumption
  2. **Format standardization = value** — consistent entry format across ~500 entries
  3. **Feynman philosophy** = foundational framing ("build to understand")
  4. **CodeCrafters business model** = paid courses fund free aggregator (sustainable)
  5. **CC0 license** = zero friction remix
  6. **Curator voice** = defining asset (Daniel → CodeCrafters preserved)
  7. **Outside Storm Bear agent taxonomy** — general programming education, different axis
- **Phase 2 status:** ✅ COMPLETE

---

## [2026-04-18] entities | Phase 3 — Entity pages (4, 1 novel)

- **Entity #1:** `(C) 29 Categories Taxonomy.md` — flat taxonomy design decisions, 29 categories grouped by 7 clusters, size distribution patterns, graduation/pruning dynamics, language × category matrix, trade-offs vs hierarchical taxonomy, hybrid proposal for Storm Bear
- **Entity #2:** `(C) Feynman Philosophy Applied to Learning.md` — Feynman quote operationalized, passive vs active learning, pedagogical patterns (nano version, progressive elaboration, classic simplification, anti-abstraction), limits (can't build everything, simplified ≠ accurate, time constraint), Feynman vs LLM-era tension + hybrid approach, comparison to sibling wiki learning approaches (7 agent wikis = productivity vs build-your-own-x = understanding)
- **Entity #3:** `(C) Curation Model.md` — 3-role split (curator + community + infrastructure), PR flow detailed, implicit quality criteria, 10-year evolution phases, governance patterns (small team high bar slow pace), pitfalls per role, lessons for Storm Bear scaling
- **Entity #4:** `(C) Storm Bear Vault — Knowledge Architecture Lessons.md` — **NOVEL entity type** (meta-lesson, unique to v8), 7 concrete lessons extracted, dual-mode architecture proposal (deep vault + flat aggregator), vault growth patterns comparison, 7 action items cho vault
- **Format compliance:** 13-section canonical format
- **Novel pattern:** Entity #4 = vault-level meta-lesson (first appearance in 8-wiki corpus). Future wikis with architectural depth can replicate.
- **Phase 3 status:** ✅ COMPLETE

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables, 1 novel framing)

- **Phase 4a:** `03 Published/(C) build-your-own-x - Huong dan cho nguoi moi.md` — bilingual beginner guide (~580 lines, 9 parts). Parts: intro + positioning vs 7 siblings, 29 categories overview, best categories per goal (5 learning paths), Feynman philosophy deep dive, sibling comparison matrix, 3-month roadmap (Git → Database → Programming Language), tips + pitfalls, Storm Bear synergy, next steps. Different angle: not "pick tool to use" but "pick topic to UNDERSTAND."
- **Phase 4b:** `03 Published/(C) Meta-reference — Storm Bear vault architecture lessons.md` — **NOVEL framing** (not taxonomy extension), ~550 lines, 8 parts. Explicit "outside scope" declaration, lessons summary, 7 concrete vault actions (near-term / mid-term / long-term), what build-your-own-x can't teach, new 7th Phase 4b routing mode documented, taxonomy corpus status after v8, cross-vault synthesis reflections.
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** v8 Phase 4b = **7th distinct routing mode**. Prior 6: same-domain N-way (v2/v3/v5), adjacent-domain taxonomy (v4), same-tier 4-way (v5), different-domain taxonomy extension ×2 (v6, v7). v8 adds outside-scope meta-reference.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v8

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v8 build learnings.md`
- **Velocity plateau confirmed 3 consecutive wikis** — ~2h (v6, v7, v8 identical)
- **Key insights:**
  1. Routine handles 7 distinct Phase 4b routing modes
  2. Not every wiki must fit taxonomy (outside-scope legitimate)
  3. Meta-reference framing preserves taxonomy + extracts value
  4. Single-file architecture works at 491K scale (challenges assumptions)
  5. 8-wiki corpus = substantial self-study subject
  6. 26+ action items accumulated → routine v2 urgent
  7. Feynman philosophy ≈ Karpathy LLM Wiki pattern (philosophical alignment)
- **Recommendation strengthened:** **Option B routine v2 upgrade** now equal priority to Option A Storm Bear pilot
- **Phase 5 status:** ✅ COMPLETE

---

## [2026-04-18] vault-sync | Phase 6 — Vault file updates

- Updated project `(C) index.md` — all phases ✅, deliverable tables populated
- Updated project `(C) log.md` — all phase entries appended
- Updated root `CLAUDE.md` — build-your-own-x project entry with "outside scope" framing + 8-wiki milestone
- Updated `GOALS.md` — mark v8 shipped, new 7th routing mode, 26+ action items triggering v2 urgency
- **Phase 6 status:** ✅ COMPLETE

---

## 🎉 v8 ALL PHASES COMPLETE

**8th auto-execution của routine successful.** First outside-scope meta-reference wiki. 7 distinct Phase 4b routing modes now observed. 8-wiki corpus substantial.

**Routine v1 = production-stable across 8 runs** covering 7 distinct routing modes. 26+ action items carryover triggers routine v2 upgrade urgency.
