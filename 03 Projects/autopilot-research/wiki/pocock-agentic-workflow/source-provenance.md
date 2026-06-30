# Source provenance — the verified-vs-corrected ledger

## How this topic was built

- **Primary source:** YouTube `nQwJVHCtDDY` (David Ondrej × Matt Pocock), captured via `yt-dlp 2026.06.09` English subtitles → deduped **12,548-word** transcript (`raw/2026-06-30-pocock-agentic-workflow.md`), **read in full** by the main loop. No NotebookLM.
- **Originals deep-dive + adversarial verification:** Workflow **`wf_4562f245-5bc`** — **23 agents** (11 deep-reads → 11 independent adversarial verifiers → 1 synthesis), ~931K subagent tokens, 411 tool calls, ~6 min. Each verifier re-fetched primary sources rather than trusting the deep-read.
- **Operator ground-checks:** direct `gh api` on `mattpocock/sandcastle`, `mattpocock/skills`, `obra/superpowers`, `ghuntley/how-to-ralph-wiggum`; `yt-dlp --dump-json` for the video metadata.
- Honors autopilot-research constitutional rule #4 (never fabricate) and Storm Bear Rule 12 (fail loud).

## The two-video distinction (anti-conflation — load-bearing)

There are **two different Matt Pocock items** circulating in mid-2026; this wiki documents **only the first**:

| | **(A) THIS podcast** | **(B) The workshop** |
|---|---|---|
| Title | "…Agentic Engineering Workflow (just copy him)" | "Workflow for AI Coding" |
| Where | YouTube `nQwJVHCtDDY`, **David Ondrej** channel | **AI Engineer 2026** conference |
| When / length | 2026-06-18 · **1:02:24** | ~April 2026 · **~96 min** |
| Format | conversational interview | structured talk |

**Workshop-only content NOT in this podcast** (and therefore **not** written into this wiki as podcast material): the **Smart Zone / ~100k-token reliable ceiling**, **Frederick Brooks "The Design of Design" / shared design concept**, **tracer bullets**, and the **4-role Planner / Implementation / Reviewer / Merger** parallel architecture. **Sand Castle appears in both** and is verified independently via `gh api`. A web summary conflated (A) and (B); we keep them separate.

## Verifier misfires — overridden (independently check collision/identity claims)

Two agents declared real things false because they couldn't reach the source:

1. **"Sand Castle is fabricated — no evidence."** The two-video agent searched *"Sand Castle"* (with a space) and found only unrelated projects. **Overridden:** `gh api repos/mattpocock/sandcastle` returns a real repo (6,519★, MIT), and the dedicated deep-read verified the full `@ai-hero/sandcastle` API. Sand Castle is **real**.
2. **"The David Ondrej podcast `nQwJVHCtDDY` cannot be verified."** WebFetch of YouTube returned only the footer template (YouTube blocks scraping). **Overridden:** `yt-dlp --dump-json` returned full metadata (David Ondrej, 1:02:24, 2026-06-18, 245,765 views) and the subtitles produced the transcript this topic is built on. The podcast is **confirmed**.

## Confabulations caught & stripped (deep-read errors, not in primary sources)

| Claim | Status | Reality |
|---|---|---|
| Ralph "≈ $10.42/hour Sonnet" | **fabricated** | No such figure on ghuntley.com/ralph. Excluded. |
| Huntley "worked with Steve Yegge at Sourcegraph" | **unsupported** | Yegge's "Gas Town" is cited as a *concept*, not employment. Excluded. |
| Ralph named "because it made him want to *Ralph* (vomit)" | **fabricated** | No naming story in the source. Excluded. |
| "engineering-zoom-out" skill (Matt's `disable-model-invocation` example) | **not in repo** | No skill by that name in any of 36 folders; the *mechanism* is real (grill-me/to-prd/teach set `disable-model-invocation: true`). |
| "two-prd" skill | **mishearing** | The skill is **`to-prd`** (auto-sub heard "to-PRD" as "two-PRD"). |
| ZPD "≈101,000 citations" | **fabricated number** | Drop the figure; ZPD is genuinely one of the most-cited ed-psych concepts. |
| Steinberger tweet "6.5M views," "39/61 sentiment split" | **X-gated, unverifiable** | Stated as popularization without a number. |
| `mattpocock/skills` "32 active skills" (deep-read) | **overcount** | **25 active** (Eng 14 + Productivity 5 + Misc 4 + Personal 2); 36 incl. in-progress(7) + deprecated(4). |

## Corrections from the video itself (auto-subtitle / mishearing / imprecision)

- **"John Asterout" → John Ousterhout** (author of *A Philosophy of Software Design*).
- **"Jeffrey Huntley" → Geoffrey Huntley.** **"Stanberger" → Steinberger.** **"Opera" → obra** (superpowers owner). **"Whisper Flow" → Wispr Flow.**
- **"engineering zoom out" skill** — name not found in repo (mechanism real). **"two PRD" → to-prd.**
- **The AI/agent application of Ousterhout** (tactical/strategic) and **of Sutton** (Bitter Lesson) is the speaker's extension, not the original author's.
- **Scale Software (scalesoftware.ai)** in the description is **David Ondrej's** company (Katowice), **not Matt's**, and unrelated to **Scale AI** (scale.com, SF).
- **superpowers IS more popular than mattpocock/skills** (241.7K vs 150.8K★) — Matt's "probably the most popular" was correct; "opposite approach" is the overstatement (different defaults, same tooling).

## Verified-accurate (high confidence)

- `mattpocock/sandcastle` = `@ai-hero/sandcastle`, v0.12.0, MIT, 6,519★, 5 sandbox providers × 6 agent providers, `run()`/`fork()`, 3 branch strategies; GitHub-Actions files exist as **internal CI** (no published reusable action).
- `mattpocock/skills`, MIT, 150,757★; **teach** skill real + stateful + encodes ZPD/Knowledge-Skills-Wisdom + retrieval-practice (verified in SKILL.md); **grill-me** real (`disable-model-invocation: true`, delegates to `/grilling`); **to-prd** real; install `npx skills@latest add mattpocock/skills`.
- Ousterhout = Stanford prof / Tcl-Tk / Raft; tactical-vs-strategic is Ch. 3 of the book (2018/2021).
- Ralph = Geoffrey Huntley, ghuntley.com/ralph, **14 July 2025**, `while :; do cat PROMPT.md | claude-code ; done`, file-as-state, greenfield-only; companion repo 1,707★.
- Sutton = *The Bitter Lesson* (Mar 2019), 2024 Turing Award (w/ Barto).
- aihero.dev real; /skills resolves; /posts 404s on fetch.

## Don't-re-fabricate quick list

1. It's a **David Ondrej podcast** (third-party), **not** Matt's own upload, and **not** the **~96-min AI-Engineer workshop** (no Smart Zone / Brooks / tracer-bullets / 4-role architecture here).
2. **Sand Castle is real** = `@ai-hero/sandcastle`; its security is *by-construction*, and its GitHub Action is *internal CI*, not published.
3. **superpowers (obra/Jesse Vincent) has MORE stars than mattpocock/skills**; "opposite approach" = different defaults, not opposite tooling.
4. **Ralph = Geoffrey Huntley (July 2025)**; **Steinberger popularized**, didn't originate. Drop the fabricated $/hr, Sourcegraph, and vomit-naming details.
5. **Scale Software = David's, not Matt's.** **Wispr Flow**, not "Whisper Flow." **Ousterhout**, not "Asterout."
6. Tactical/strategic-applied-to-AI and the Bitter-Lesson-applied-to-harness are **speaker extensions**, not the source authors' claims.
