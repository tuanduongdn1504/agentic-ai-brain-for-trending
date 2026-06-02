# book-to-skill — project context (v137)

**(C) AI-generated project folder.** Subject: [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill). Wiki #137, built 2026-06-02 under LLM Wiki Routine v2.6.

## One-liner
"Turn any technical book or document into a Claude Code skill — ready to study, reference, and use while you work." A multi-harness agent skill (Amp + Claude Code) that converts PDF/EPUB/DOCX/HTML/MD/TXT/RST/AsciiDoc/RTF/MOBI-AZW (via Calibre) into a **progressive-disclosure agent skill**: SKILL.md (frameworks + chapter index) + on-demand `chapters/` + glossary + patterns + cheatsheet, each with explicit token budgets. By **Virgílio Júnior** (`virgiliojr94`, Brazil — Boa Vista, Roraima; SRE at Pagar.me/Stone/MundiPagg). MIT, Python. ≈3.5k★ (NOT API-verified).

## Why it's here (and the honest calibration)
- **(b) is load-bearing and STRONG (not STRONGEST):** it's a Claude Code/Amp **skill-authoring meta-tool** that automates the exact step this vault performs by hand — ingest a source → emit mental-models + chapter index + glossary + cross-refs + on-demand loading (a mini Karpathy-LLM-wiki built from one book). Directly on goal #1 AND directly vault-applicable (Storm Bear reads technical books; this turns them into referenceable Claude skills). Held at STRONG not STRONGEST because it is a **knowledge-ingestion/study tool** (knowledge-management domain), not a software-shipping tool — same calibration as v134 obsidian-second-brain.
- **(a) is WEAK/geographic, not load-bearing:** Brazilian/South-American-LOCATED — **re-registers the retired (a)-8 South-American-LOCATED sub-axis at N=2** (v97 distill + v137; §28-style re-registration on a genuine 2nd instance, like v135's cited→subject). Not the Asian cultural-peer cluster; like v131's WEAK-geographic call. (b) carries the INCLUDE.

## Verdict + Pattern Library impact
- **GOAL-ALIGNED INCLUDE 3/4** — (a) WEAK/geographic + (b) **STRONG** + (c) STRONG + (d) STRONG.
- **PRIMARY:** methodology-embodiment of the Karpathy-LLM-wiki **construction step**, automated as a source→agent-skill generator — a **candidate** relationship to the v118/v134 "generate-the-wiki" vector, with a load-bearing distinction (one-shot source→**skill** artifact vs persistent self-maintaining Obsidian **vault**). **DEFERRED** promote-vs-split to the ~v139–v140 audit (no ship-promotion — mirrors the v134-v135 audit discipline). + **1 NEW Library-vocab standalone FILED** to registry 06 §C: "Source-to-Agent-Skill Knowledge-Base Generator" N=1 CORPUS-FIRST.
- **SECONDARY (instance notes):** Pattern #84 84c multi-harness N+1 (Amp + Claude Code skill dirs, modest) · Library-vocab #20 Token-Economy-Quantification N+1 (Step 2.5 cost pre-flight, token+USD) · context-management corpus-recursive observation (Step 2.6 RLM grep/sed = the vault's own "surgical extracts / never read >1 chapter" discipline, NOT minted) · skill-generating-skill cluster v95/v131/v137 (heterogeneous → observation, NOT minted).
- **NO Pattern Library state change** (46 confirmed / 8 Library-vocab CONFIRMED). NO new top-level pattern. NO new tier sub-archetype. §28 new-standalone count = 1 (≤2). **NOT a Pattern #52 promotion** (velocity ~113★/day strong but <90d pulse AND NOT API-verified). **NOT an agentskills.io 57k `npx skills add` implementer** (installed by copying SKILL.md / curl; Amp `.agents/skills` is a dir convention, not the vercel-labs CLI).

## §35 / streak
- §35 **STAYS CLEAR** — window {v135 GA, v136 GA, v137 GA} = 0 OG. No override. Consecutive-GA run v134→v137 = 4.
- Streak (v2.6 §32): **`GA:6 · OG:4 [1 ov]` → `GA:7 · OG:4 [1 ov]`** ("49+3\*" frozen @v125). v137 = 7th GOAL-ALIGNED PASS.

## Pilot
**Tier-1 PILOTABLE — and the most directly-pilotable, lowest-friction goal-aligned ship in a long run** (addresses the standing "ships goal-aligned subjects, pilots none" critique). Copy SKILL.md + scripts/extract.py into `~/.claude/skills/book-to-skill/`, run `/book-to-skill <a-real-book.pdf>`, inspect the generated skill, delete if unwanted — fully reversible. `install-snapshot` recommended (extract.py optionally pip-installs Docling/PyPDF2/pdfminer/ebooklib/python-docx/striprtf — `--install-missing ask` by default, so it prompts). Concrete vault use: convert a Scrum book or v74 "Build a LLM from Scratch" into a referenceable Claude skill.

## Files
- `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` — the gate.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY + secondaries + honest non-claims.
- `02 Wiki/index.md` — the wiki page.

## Data caveat (§37)
Sandbox mocks the GitHub API → stars/forks/created_at NOT API-verified. Figures (≈3.5k★ / 436 forks / 26 watchers; created ~2026-05-01; MIT; Python) are from the repo page + README + the gh-api mock, flagged `stated, NOT API-verified` (§37.4). Velocity approximate; no Pattern #52 claim.
