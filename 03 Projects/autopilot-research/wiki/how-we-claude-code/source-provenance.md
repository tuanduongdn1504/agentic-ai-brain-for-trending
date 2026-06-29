# Source Provenance & Verification Ledger — how-we-claude-code

> Constitutional rule #4 (never fabricate) honored. The video is a faithful dub of a first-party Anthropic talk, so the *conceptual* content is low-risk; verification focused on **identity, the repo internals, the originals, and the magnitude/version claims** (the confabulation-prone facts).

## What was ingested

- **Video (entry point):** VN dub [ATsbgIRA0Fw](https://www.youtube.com/watch?v=ATsbgIRA0Fw) (BizMate AI). **Path 5 (yt-dlp).** The dub links the English original directly.
- **Original (authoritative):** "How we Claude Code" [IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE) (Anthropic, Arno / Applied AI). **Full English auto-captions pulled** (json3 → parsed in-script; ffmpeg absent), deduped to a ~5,000-word timestamped transcript, **read in full**. Raw: `raw/2026-06-29-how-we-claude-code-anthropic-workshop.md`.
- **Originals (deep-dived directly):** Thariq's blog (claude.com) · `ThariqS/html-effectiveness` + companion site · `anthropics/cwc-workshops/how-we-claude-code/**` (every `phase-3-verify/src/verify/*` file read via `gh api`) · Sutton's *Bitter Lesson* · official Claude Code docs.

## How it was verified

- **Workflow `wf_109aca29-27c`** — 16 agents: **6 deep-dive extractors** (blog · repo internals · Thariq/examples · Bitter Lesson · CC primitives · independent corroboration) + **9 adversarial claim-verifiers** + **1 synthesis**. 717K subagent tokens, 320 tool calls, ~8 min.
- **Plus operator (main-loop) ground-checks:** `gh api` on `cwc-workshops` repo meta + the full recursive `how-we-claude-code/` tree (confirmed every file path independently) + `yt-dlp` metadata on both videos.

### ⚠️ Verifier misfire caught and overridden (Rule 7)

**4 of the 9 adversarial verifiers (c1, c3, c4, c5) misfired**: they interpreted *"verify against the repo"* as *"search the local filesystem"* and grepped `/Users/Cvtot/...` (the operator's machine), found nothing, and returned **false `refuted`/`uncertain`** verdicts on the framework's existence, the Todo-app fact, and the recorder. These were **overridden** because (a) the 6 extract agents fetched the *actual* primary sources (blog via WebFetch, repo files via `gh api`) and confirmed every detail, and (b) the operator independently read the repo tree. **This is logged, not hidden** — it is exactly the "independently check, don't confabulate" discipline. The framework, the Todo app, and `record.ts`/`recorder.ts` **demonstrably exist** in the repo.

## CONFIRMED (verified true)

| Claim | Verdict | Source |
|---|---|---|
| VN video is a dub of "How we Claude Code" (Arno, Anthropic Applied AI), original IlqJqcl8ONE | ✅ CONFIRMED | yt-dlp metadata + VN description links original + transcript |
| Repo `anthropics/cwc-workshops` (1,212★), folder `how-we-claude-code/` with phase-1/2/3 | ✅ CONFIRMED | `gh api` repo tree (operator) + extract agent |
| Phase-3 is a React+Vite **Todo** app (not bill-splitting); bill-splitting is phases 1–2 | ✅ CONFIRMED | `gh api` `src/features/todos/*` + phase-3 README (extract); verifier c3 misfired (local-fs) |
| Verification framework exists & works: `data-verify-*` DOM contract, 4 verifiers, `window.__verify`, 3 surfaces, vitest matrix | ✅ CONFIRMED | every `src/verify/*` file read via `gh api` (extract); verifier c4 "refuted" was a local-fs misfire |
| Recording via `scripts/record.ts` + `harness/recorder.ts` (Playwright → local `recordings/.webm`) | ✅ CONFIRMED | files read via `gh api`; verifier c5 "refuted" was a local-fs misfire |
| Author **Thariq Shihipar**, Claude Code team @ Anthropic; blog at claude.com | ✅ CONFIRMED | blog WebFetch + ChatPRD + GitHub profile + Simon Willison; verifier c1 "uncertain" (searched wrong places, X blocked) |
| `ThariqS/html-effectiveness`: **20 HTML files**, **9 categories**, Apache-2.0, 519★ | ✅ CONFIRMED | `gh api` + companion site WebFetch |
| CC primitives: Auto Mode (shift+Tab), `/fast`, `/effort` (low→max incl. xhigh), `/goal`, AskUserQuestion, Playwright MCP | ✅ CONFIRMED | official docs + transcript |
| *Bitter Lesson* = Richard Sutton, 2019; thesis as stated | ✅ CONFIRMED | Scholar + widely-cited; original essay text not directly fetched (self-signed cert) |
| Opus 4.7 was current at talk date; Opus 4.8 is current now (Fable 5 since 2026-06-09) | ✅ CONFIRMED | platform.claude.com models + operator env |

## CORRECTED / FLAGGED (the guards that mattered)

1. **⚠️ Name:** Arno says "Tariq/Tarik"; canonical spelling is **Thariq Shihipar** (X: @trq212).
2. **⚠️ Phase-3 app:** it is a **Todo app**, not the bill-splitting app — a common misread of the talk.
3. **⚠️ S3:** the repo records **locally** (`recordings/`); the talk mentions S3 only as one optional downstream destination. **No S3 in the repo.**
4. **❌ "Went viral / millions of views":** **UNVERIFIED.** No primary metric supports it; the repos have hundreds of stars. Stated as *reported*, not fact.
5. **⚠️ "5 vs 9 categories":** the blog groups ~5 use-case buckets; the companion site lists **9**. Both verified; different granularity, not a contradiction.
6. **⚠️ Token efficiency:** Arno's "HTML isn't less efficient" is a *long-run-iterations* claim; HTML actually costs **2–4× tokens** per document (Thariq + independent). See [[how-we-claude-code/caveats-and-when-not-to-use-html]].
7. **⚠️ Bitter Lesson analogy:** the *"model extracts requirements better than you"* line is **Arno's analogy, not Sutton's text** — and over-reaches (means vs. ends; no ground truth). Flagged in [[how-we-claude-code/pillar-1-interview-and-bitter-lesson]].
8. **⚠️ Storybook fixtures:** referenced as a pattern, but **not** a first-party-documented Claude Code feature (community).
9. **⚠️ Original video's YouTube description** ("project context files, custom commands, hooks, subagents") **does not match** the talk's actual content — appears to be a generic series blurb; transcript is ground truth.

## Confidence summary

- **Repo internals, framework mechanism, CC primitives, file counts:** HIGH (read directly via `gh api` + docs; operator-confirmed tree).
- **Identity / blog existence:** HIGH (the "uncertain" verdict was a tooling artifact; multiple independent primary sources confirm).
- **Virality / exact token ratios / Bitter-Lesson-textual-fidelity:** flagged as reported/approximate/analogical.

## Cross-links

- [[how-we-claude-code/_index]] · [[how-we-claude-code/overview]] · [[how-we-claude-code/verification-framework-deep-dive]] · [[how-we-claude-code/caveats-and-when-not-to-use-html]]
