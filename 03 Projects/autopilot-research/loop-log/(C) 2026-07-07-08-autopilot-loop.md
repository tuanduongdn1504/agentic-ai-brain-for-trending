# (C) Autopilot Loop — 2026-07-07-08

> **Trigger:** manual operator session ("build knowledge from this video + double deep dive into the original resource + pilot methods")
> **Topic:** system-thinking-ai-coding (NEW)
> **Started:** 2026-07-07T~07:00+07:00
> **Ended:** 2026-07-07T~08:00+07:00
> **Duration:** ~60m

## Source chain

- Operator-submitted: `t8_M8Ql1Q1I` — **Thầy Hoàng JS (phecode)** / CodeFarm "KỸ NĂNG CODING DUY NHẤT KHÔNG LỖI THỜI - KHÔNG SỢ AI: SYSTEM THINKING (No cut, no edit)" (2026-06-29, 42:31, 2,925 views, 1,920 subs; **FIRST-PARTY VN thesis lecture, no code/repo**; 3rd VN first-party channel after hoidanit + Mì AI).
- Ingest: `yt-dlp` metadata + VN auto-subs (475KB VTT) → `clean.py` dedupe → ~57.4K-char / 1,100-line transcript, **read in full in the main loop** (EN track 429; ffmpeg absent, irrelevant; broken `python3` shim → brew `python3.12`).
- **Original resource (double-dive target):** **Peter Naur, "Programming as Theory Building" (1985)** — attributed at [3:14] via garbled auto-caption ("Peter Law … Programming Story Building").

## What happened

1. Identified the video (WebFetch blocked by JS shell → yt-dlp metadata + captions). Read the full transcript; extracted the thesis, 3 golden questions, 4 practice steps, and the 4 empirical citations.
2. **Double deep-dive, right-sized to a conceptual source** (one essay + 3 citations, not a repo): 2 focused subagents —
   - **Agent A:** primary-source dive on Naur 1985 (essay body via mirrors; Ryle's "theory"; program death/revival; author facts) → produced a fidelity table.
   - **Agent B:** refute-first verification of the 4 empirical claims.
3. **Main-loop ground-checks (2 WebSearches)** on the two highest-risk items → **overturned Agent B's mis-correction** of the Harvard-62M study (see misfires below).
4. Compile: 11 wiki files (NEW topic) + master-index entry + inventory table-row + inventory prose bullet + raw file + this log.
5. Pilot deliverable: `output/(C) 2026-07-07-system-thinking-ai-coding-pilot-methods.md` — 24 methods across A/B/C/D/E + skip-list + critic reframe.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + 1 essay (Naur) + 3 verified citations | 1 (new topic) | 0 topic-level (residuals are watch-list items, not stubs) | 1.0 |

- `gaps_closed_ratio` = **1.0** (cold-start topic fully compiled).
- Stop reason: single-topic manual session complete.

## Verification ledger (Rule 12 — all 4 CONFIRMED)

| Claim | Verdict | Source |
|---|---|---|
| Author = **Peter Naur**, *Programming as Theory Building* (1985); Turing 2005 | CONFIRMED | amturing.acm.org; Wikipedia |
| **Jagged technological frontier** (Harvard/BCG) | CONFIRMED | Dell'Acqua et al., SSRN 4573321 / *Organization Science* 2026 (758 BCG consultants) |
| **Harvard, 62M records**, junior hiring ↓ since 2023 | CONFIRMED | Hosseini Maasoum & Lichtinger, SSRN 5425555 (Aug 2025) |
| **IBM 3×** entry-level hiring 2026 | CONFIRMED | Fortune / Axios / Bloomberg / Tom's Hardware (Feb 2026) |

## Incidents & misfires (prime-directive ledger)

- ⚠️ **Verifier (Agent B) mis-corrected the Harvard-62M claim** — asserted it was a misattribution and the "real" study was Stanford's *Canaries in the Coal Mine* (Brynjolfsson et al.). **OVERRIDDEN by a main-loop WebSearch**: the Harvard 62M study (Hosseini & Lichtinger) is real and exactly matches the speaker; Stanford is a genuine *sibling*, not the cited study. Classic wiki-verify confabulation (substitute-a-known-fact); caught pre-publication. Logged in [[system-thinking-ai-coding/caveats-and-corrections]] + source-provenance. **Lesson: ground-check "misattribution" verdicts, not just the original claim** — verify the correction too (sibling to the discard-as-garble guard).
- **Naur fidelity nuance surfaced (Rule 7):** two of the video's paraphrases are looser than Naur's text ("finished-in-brain-before-code" = PARTIAL; "conductor" metaphor = STRETCH). Recorded, not blended.
- Shell friction (known): vault zsh drops stdout + resets cwd; `python3` shim broken. Worked around per vault memory (brew python3.12, absolute paths, route to files + Read).

## Wiki articles created

- wiki/system-thinking-ai-coding/ — `_index` + 11 articles (overview / what-system-thinking-is / naur-programming-as-theory-building / video-summary / three-golden-questions / four-practice-steps / compiler-vs-llm / code-vs-architecture-and-tech-debt / junior-crisis-and-hiring-2026 / caveats-and-corrections / source-provenance).
- wiki/_master-index.md — NEW topic entry prepended.
- raw/2026-07-07-system-thinking-ai-coding.md — full VN transcript + metadata + chapter map + extracted claims.
- raw/_inventory.md — table row + prose bullet (Status: compiled).
- output/(C) 2026-07-07-system-thinking-ai-coding-pilot-methods.md — 24 methods.

## Suggested next action

Pick from the pilot menu — recommended: **A1 (3-question PR/Definition-of-Ready gate)** + **A2 (design-before-prompt + reverse-review)** on the *running* hireui Candidate-Detail work (both zero-install, both inside the existing BMAD/PR flow), and **D1/D2** (3-questions-as-refinement-ritual + AI-as-patient-teacher junior onboarding) into your next Scrum cycle. Then wrap hireui's first LLM feature in **A3 + A4** so it ships with a human-held theory (anti-dead-program), not just code that runs. Git checkpoint skipped (not committing without your say-so) — files are staged in the working tree for your review.
