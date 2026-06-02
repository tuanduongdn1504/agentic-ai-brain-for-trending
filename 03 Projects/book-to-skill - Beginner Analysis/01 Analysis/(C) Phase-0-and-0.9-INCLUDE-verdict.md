# (C) Phase 0 + Phase 0.9 INCLUDE verdict — book-to-skill (v137)

**Subject:** [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill)
**Routine:** v2.6. **Date:** 2026-06-02. **Verdict:** **GOAL-ALIGNED INCLUDE 3/4** ((a) WEAK/geographic + (b) **STRONG** + (c) STRONG + (d) STRONG).

---

## Phase 0 — intake

Operator handed the URL directly with "Build LLM wiki for …". Pre-flight:
1. **Not a duplicate subject** — `virgiliojr94/book-to-skill` has never been a corpus subject, nor a prior citation (unlike v135 open-slide).
2. **Clearly on-corpus + goal-aligned** — it is a Claude Code (+ Amp) **agent skill** whose job is **authoring agent skills from books**. No override needed; this is a normal GOAL-ALIGNED intake.

⚠️ **Data caveat (§37.4):** this sandbox **mocks** `curl`/the GitHub API, so stars / forks / `created_at` are **NOT API-verified**. Metadata is from the GitHub repo page + README + the gh-api mock: ≈**3.5k★** (repo page) / mock `stargazers_count` **3,480** / **436 forks** / **26 watchers** / **1 open issue** / **MIT** / **Python 100%** / created **~2026-05-01** (mock) = ~1 month old. The repo-page "3.5k" and the mock "3,480" agree closely, raising confidence to *stated* — but still **NOT API-verified**. **Velocity (~113★/day if accurate) is NOT used for a Pattern #52 claim** (unverified + <90d pulse window).

## Phase 0.9 — STRICT 4-criterion test

### (a) Cultural-peer / locale — **WEAK / geographic (not load-bearing)**
Author **Virgílio Júnior** (`virgiliojr94`) — **Brazil**, Boa Vista (Roraima); Portuguese-language profile; SRE at Brazilian fintechs (Pagar.me / Stone / MundiPagg); 45 public repos, 147 followers (stated, NOT API-verified). This is **South-American-LOCATED**, not the Asian cultural-peer cluster — so (a) is a **WEAK/geographic** note, *not* a clean PASS (same posture as v131 harness's S-Korea call). Its real significance: it **re-registers the retired Phase-0.9 (a)-8 "South-American-LOCATED" sub-axis at N=2** (v97 distill samuelfaj/Brazil + v137 book-to-skill/Brazil). (a)-8 was registered PROVISIONAL N=1 at v97 and FORCED-RETIRED at v115 (N=1-only, 18 wikis). Per the §28 / §2 re-registration allowance (a genuine 2nd instance, exactly the v135 cited→subject precedent), it returns at **N=2, promotion-eligible at N=3**. This is a **Phase-0.9 (a)-axis ledger** re-registration — it does **NOT** consume the §28 Library-vocab new-standalone cap.

### (b) Goal-relevance — **STRONG** (load-bearing; the call I pressure-tested)
Goal #1 = "Master Claude and autonomous agents for software development."
- **For:** book-to-skill is a **Claude Code / Amp agent skill whose output is another agent skill** — a skill-authoring meta-tool, squarely in the corpus's agentskills.io / skill-creation wheelhouse (sibling to v95 skill-creator, v131 harness). More than that, it **automates the exact step this vault performs by hand**: ingest a source → extract frameworks/mental-models → build a chapter index + glossary + patterns + cheatsheet → load chapters on-demand via a topic index = a mini Karpathy-LLM-wiki built from one book. Directly vault-applicable: Storm Bear reads technical books and could convert them into referenceable Claude skills (a Scrum book; v74 "Build a LLM from Scratch"). LOW, reversible cost-of-trial × DIRECT applicability → STRONG per §10.
- **Against STRONGEST (held honestly):** it is a **knowledge-ingestion / study tool** (knowledge-management domain), not a software-*shipping* tool. It helps you study and reference books while working — adjacent to, but not the center of, "shipping software with agents." This is the **same calibration as v134 obsidian-second-brain** (held at STRONG, not STRONGEST, because PKM/knowledge-domain) and well above v135 open-slide's MODERATE (open-slide is the presentation domain; book-to-skill is core skill-authoring + the vault's own methodology).
- **Verdict: STRONG.** Comfortably GOAL-ALIGNED. STRONG is the honest tier; there was no §35 pressure to inflate (the ceiling is already clear), and no incentive to deflate.

### (c) Skill / engineering exemplar — **STRONG**
A clean, genuinely instructive skill-authoring exemplar (3-file repo: SKILL.md + `scripts/extract.py` + README):
- **Progressive-disclosure output architecture** with explicit token budgets: SKILL.md body <4,000 tokens (front-loaded for compaction) + `chapters/ch*.md` 800–1,200 tokens each (on-demand) + glossary ≤1,500 + patterns ≤2,000 + cheatsheet ≤1,000 + a **topic index** for navigation. "Extract structure, not summaries."
- **Step 2.5 pre-flight cost estimate** — token + USD price (Sonnet/Haiku) + time estimate **before** generation (a Library-vocab #20 Token-Economy-Quantification instance).
- **Step 2.6 RLM-inspired large-book access** — for books >50k tokens, explicitly cites the **Recursive Language Model paradigm** and uses `wc`/`grep`/`sed`/bounded `Read` to slice only relevant chapters instead of loading the whole file ("a 200-page book re-read once per chapter = ~2M input tokens"). This is **the vault's own context-rot discipline**, arrived at independently.
- **Technical-vs-text extraction routing** with fallback chains (Docling for structure-aware technical; pdftotext→PyPDF2→pdfminer for text; ebooklib/python-docx/striprtf/Calibre per format), `--install-missing ask|yes|no` package handling, 3 operating modes (Full / Analyze-only / Generate-from-prior-analysis).
Held at STRONG, not STRONGEST: it's a tight 3-file skill, not a large multi-skill exemplar like v93/v95.

### (d) Corpus connectivity — **STRONG**
- **The corpus's own foundation:** automates the Karpathy-LLM-wiki **construction step** (PRIMARY; see Phase-4b doc) — adjacent to the v118/v134 "generate-the-wiki" corpus-recursive thread.
- **Skill-creation lineage:** v95 skill-creator (general scaffolder) + v131 harness (generates teams + skills) + v137 (generates a skill from a book).
- **Source→knowledge-structure sibling:** v94 Understand-Anything (codebase → knowledge graph) vs v137 (document → knowledge skill).
- **Book-companion thread:** v74 LLMs-from-scratch — book-to-skill could literally convert it.
- **Multi-harness:** Amp (`.agents/skills`, `~/.config/agents/skills`, `~/.config/amp/skills`) + Claude Code (`~/.claude/skills`) = Pattern #84 84c N+1.
- **Token-economy + context-management:** Library-vocab #20 (cost pre-flight) + the vault's surgical-extract discipline (RLM Step 2.6).
Held at STRONG, not STRONGEST: not a distribution-anchor / Karpathy-direct-lineage node like v93/v95.

### Verdict
**GOAL-ALIGNED INCLUDE 3/4** — (a) WEAK/geographic + (b) **STRONG** + (c) STRONG + (d) STRONG. (b) is load-bearing.

## §35 ceiling check (v2.6)
- Entering v137 the ceiling was **CLEAR** (rolling-3 {v134 GA, v135 GA, v136 GA} = 0 OG).
- **v137 = GOAL-ALIGNED → new window {v135 GA, v136 GA, v137 GA} = 0 OG → STAYS CLEAR (§35.3).** Consecutive-GA run v134→v137 = 4.
- **No override** (neither a Phase-0.9 (a)/(b) override nor a ceiling-override). Override-frequency triggers UNCHANGED (lifetime 4: v84+v116+v122+v127; 3-in-30 last tripped at v127).

## Streak (v2.5 §32 forward / v2.6)
Historical **"49+3\*" frozen @v125**. Forward: **`GA:6 · OG:4 [1 ov]` → `GA:7 · OG:4 [1 ov]`** (v137 = 7th GOAL-ALIGNED PASS under v2.5/v2.6). Override subset `[1 ov]` UNCHANGED.

## Calibration note (per the Finding-2 discipline)
- (a) genuinely is **not** a clean PASS — Brazilian/South-American-LOCATED, recorded as WEAK/geographic + an (a)-8 re-registration N=2, **not** laundered into a cultural-peer PASS.
- (b) is held at **STRONG, not STRONGEST** — the knowledge-management/study-domain ceiling, same as v134; clearing §35 did not require inflating it.
- 1 new Library-vocab standalone minted (§28 ≤2, used 1) + the generate-vector relationship recorded as a **candidate, DEFERRED** to audit (no ship-promotion). No top-level pattern, no tier sub-archetype, no state change — the disciplined outcome for a clean GOAL-ALIGNED ship.
