# book-to-skill — wiki (v137)

> **(C) AI-generated wiki page.** Subject: [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill). Built 2026-06-02 under LLM Wiki Routine v2.6.
> ⚠️ Metadata caveat (§37): this sandbox mocks the GitHub API, so stars / forks / created_at are **not API-verified** — figures below are from the repo page + README + the gh-api mock, flagged where approximate.

## Identity

| Field | Value |
|---|---|
| Repo | `virgiliojr94/book-to-skill` |
| Tagline | **"Turn any technical book or document into a Claude Code skill — ready to study, reference, and use while you work."** |
| Author | **Virgílio Júnior** (`virgiliojr94`) — **Brazil**, Boa Vista (Roraima); SRE at Pagar.me / Stone / MundiPagg (Portuguese-language profile) |
| Tier | **T1 Assistant Skill** (a Claude Code / Amp skill) — specifically a **skill-authoring meta-skill**; bundled Python extraction script |
| License | MIT |
| Language | Python 100% |
| Stars | ≈ **3.5k** (repo page) / mock 3,480 · 436 forks · 26 watchers · 1 open issue — *stated, NOT API-verified* (§37.4) |
| Created | ~**2026-05-01** (mock) = ~1 month — *NOT API-verified*; ~113★/day **if** accurate, **no #52 claim made** |
| Verdict | **GOAL-ALIGNED INCLUDE 3/4** — (a) WEAK/geographic + (b) **STRONG** + (c) STRONG + (d) STRONG |

## What it is

A **multi-harness agent skill** (Amp + Claude Code) that **converts a document into a structured agent skill** — the inverse of "dump a PDF into context." You run `/book-to-skill <path> [slug]`; it extracts the source and **generates a progressive-disclosure skill** installed at `~/.claude/skills/<slug>/` (or an Amp skill dir):

- **SKILL.md** (<4,000 tokens, front-loaded for compaction) — the author's named frameworks + mental models + chapter index + **topic index**.
- **`chapters/ch*.md`** (800–1,200 tokens each, **loaded on-demand**) — per-chapter core idea, frameworks (exact naming preserved), key concepts, anti-patterns, code/tables (technical books), takeaways, "Connects To".
- **`glossary.md`** (≤1,500) · **`patterns.md`** (≤2,000) · **`cheatsheet.md`** (≤1,000).

**Philosophy: "Extract structure, not summaries."** A skill is a toolkit (named frameworks, actionable principles, techniques, anti-patterns, voice calibration), not a book report. Preserve the author's precision ("The 5 Whys" ≠ "ask why a few times").

**Formats:** PDF, EPUB, DOCX, TXT, Markdown, reStructuredText, AsciiDoc, HTML, RTF, MOBI/AZW/AZW3 (Calibre). **Extraction** (`scripts/extract.py`, Python): technical mode → **Docling** (layout-aware, tables/code preserved, ~1.5s/page); text mode → **pdftotext → PyPDF2 → pdfminer.six**; EPUB → ebooklib/stdlib; DOCX → python-docx/stdlib; RTF → striprtf; with `--install-missing ask|yes|no`.

**Three modes:** Full Conversion (default) · Analyze-only (extraction report, no files) · Generate-from-prior-analysis.

```bash
# install (copy into a skill dir), then:
/book-to-skill /path/to/book.pdf cialdini-influence
```

## The engineering worth studying

- **Step 2.5 — pre-flight cost estimate:** input/output **tokens + USD** (Sonnet/Haiku) + time, shown **before** generation. (Library-vocab #20 Token-Economy-Quantification.)
- **Step 2.6 — RLM large-book access:** explicitly cites the **Recursive Language Model** paradigm; for books >50k tokens it uses `wc`/`grep`/`sed`/bounded `Read` to pull only the relevant chapter instead of loading the whole file ("re-reading a 200-page book once per chapter ≈ 2M input tokens"). *This is the vault's own "surgical extracts / never read >1 chapter" context-rot discipline, arrived at independently.*
- **Progressive disclosure with explicit token budgets** + a topic index for navigation — a clean model of "how to author a skill that produces an on-demand knowledge base."
- **Positioning** (README): *vs RAG* — "RAG works at query time: chunk → embed → similarity-search → inject; book-to-skill operates at compile time, extracting the author's frameworks." *vs NotebookLM* — better for single-book depth than multi-book search. *vs raw PDF injection* — a 400-page book ≈ 200K tokens per conversation; skills load chapters on-demand.

## Why it's in the corpus

- **(a)** WEAK/geographic — Brazilian / South-American-LOCATED; **re-registers the retired (a)-8 sub-axis at N=2** (v97 distill + v137). Not the Asian cultural-peer cluster; **not load-bearing** (like v131's S-Korea call).
- **(b)** **STRONG (load-bearing)** — a Claude Code/Amp **skill-authoring meta-tool** that automates the vault's own source→knowledge-base step; directly on goal #1 and directly vault-applicable. **STRONG not STRONGEST** = knowledge-ingestion/study domain (the v134 obsidian-second-brain calibration), well above v135 open-slide's MODERATE.
- **(c)** STRONG — clean skill-authoring exemplar (cost pre-flight, RLM large-book access, progressive disclosure, extraction routing, 3 modes).
- **(d)** STRONG — automates the Karpathy-LLM-wiki construction step (adjacent to the v118/v134 generate-vector) + skill-creation lineage (v95 skill-creator, v131 harness) + source→knowledge sibling (v94 Understand-Anything) + book-companion (v74) + Pattern #84 multi-harness + Library-vocab #20.

## Pattern Library contribution (Phase 4b)

- **PRIMARY:** methodology-embodiment of the Karpathy-LLM-wiki **construction step**, automated as a source→agent-skill generator — a **candidate** relationship to the v118/v134 "generate-the-wiki" vector, with a load-bearing distinction (one-shot source→**skill** artifact vs persistent self-maintaining **vault**). **Promote-vs-split DEFERRED to the ~v139–v140 audit** (no ship-promotion). + **1 NEW Library-vocab standalone FILED** to registry 06 §C: **"Source-to-Agent-Skill Knowledge-Base Generator"** N=1 CORPUS-FIRST (distinct from v95 skill-creator / v94 Understand-Anything / the 57k chain; promotion-eligible at N=2).
- **SECONDARY (instance notes, not mints):** Phase-0.9 **(a)-8 South-American-LOCATED re-registered N=2** (v97+v137; (a)-axis ledger, not a Library-vocab standalone) · Pattern #84 84c multi-harness N+1 (Amp + Claude Code, modest) · Library-vocab #20 Token-Economy-Quantification N+1 (Step 2.5) · context-management / RLM corpus-recursive (observation, NOT minted) · skill-generating-skill cluster v95/v131/v137 (heterogeneous → observation, NOT minted).
- **State change: NONE** (46 confirmed / 8 Library-vocab CONFIRMED). §28 new-standalone count = 1 (≤2). NO top-level pattern, NO tier sub-archetype. **NOT a Pattern #52 promotion** (velocity unverified + <90d). **NOT an agentskills.io 57k implementer**.

## §35 / streak

- §35 ceiling **STAYS CLEAR** — window {v135 GA, v136 GA, v137 GA} = 0 OG. No override. Consecutive-GA run v134→v137 = 4.
- Streak: **`GA:6 · OG:4 [1 ov]` → `GA:7 · OG:4 [1 ov]`** ("49+3\*" frozen @v125). v137 = 7th GOAL-ALIGNED PASS.

## Pilot note

**Tier-1 PILOTABLE — and the most directly-pilotable, lowest-friction goal-aligned ship in a long stretch** (it answers the standing "ships goal-aligned subjects, pilots none" critique). It is a genuinely useful vault tool: Storm Bear reads technical books and could turn them into referenceable Claude skills.

- **Reversible trial:** copy `SKILL.md` + `scripts/extract.py` into `~/.claude/skills/book-to-skill/`, run `/book-to-skill <a-real-book.pdf>`, inspect the generated skill, delete if unwanted.
- **`install-snapshot` recommended:** `extract.py` optionally pip-installs Docling/PyPDF2/pdfminer/ebooklib/python-docx/striprtf (default `--install-missing ask`, so it prompts — but snapshot first).
- **Concrete first target:** convert a Scrum/coaching book, or v74 "Build a LLM From Scratch", into a Claude skill — then use it while working.
- **Study angle even if you don't keep it:** the Step 2.5 cost pre-flight + Step 2.6 RLM large-book access + the progressive-disclosure/token-budget structure are a clean model to **borrow by hand** into your own skill-authoring and the LLM-wiki routine.
