# Source & Provenance

**How this topic was built: one 11-hour Vietnamese video → yt-dlp captions → a 50-agent verification workflow → main-loop assembly and QA. Full audit trail, so any claim can be traced back.**

## The source

| Field | Value |
|---|---|
| Title | Khoá Học Copywriting 11 Tiếng Cho Người Mới \| Từ 0 Đến $1.000/Tháng Thực Chiến (MIỄN PHÍ) |
| Translation | "11-Hour Copywriting Course for Beginners \| From $0 to $1,000/month, Practical (FREE)" |
| URL | https://www.youtube.com/watch?v=zuIudgESKDk (`zuIudgESKDk`) |
| Channel | Trương Phương |
| Uploaded | 2026-07-07 |
| Duration | **11:20:22** (single video) |
| Views | ~32,574 (at ingest) |
| Language | Vietnamese |
| Category | Education (copywriting / marketing skills) |

## Ingestion

- **Path 1** (`/loop autopilot research <url>`), operator-submitted URL, 2026-07-18.
- **yt-dlp** pulled the `vi` auto-captions (6.8 MB VTT) → cleaned to plain text (dedupe rolling captions, strip timestamps) → **147,904 words / 16,864 lines / 646 KB** (`scratchpad/copywriting.txt`).
- **`notebook_id: none`** — NotebookLM was **not** used. At 148K words the single source would strain a NotebookLM bundle; the clean transcript was analysed directly. The transcript was split into **12 chunks (~12.5K words each)** for parallel digestion.
- Raw analysis: `raw/2026-07-18-copywriting-11h-course.md`.

## Analysis workflow

**Workflow `wf_1fc6cda8-8bf`** (dynamic, background) — **50 agents, 0 errors / 0 empty / 0 skipped, ~2.84M tokens, 362 tool calls, ~17 min**:

1. **Digest (12 agents)** — one per transcript chunk; extracted sections, named frameworks, techniques, factual claims (flagged checkable), copy examples, and ASR garbles. Structured JSON.
2. **Synthesise (1 agent)** — merged 12 digests → the through-line, the article outline, a 39-item framework inventory, the 0→$1,000 roadmap, and 24 claims to verify.
3. **Verify (24 agents, refute-first)** — each claim checked two ways: transcript fidelity (grep the VN transcript) + external truth (WebSearch), defaulting to skepticism. Produced [[claims-scorecard]].
4. **Draft (13 agents)** — one per article, each given the framework inventory + the verification verdicts so debunked claims would not be asserted.

**Main-loop follow-up (3 agents + manual QA):** 3 articles returned as under-developed stubs and were re-drafted to depth ([[psychology-persuasion-five-stages]], [[core-email-templates-pas-bab-educational]], [[customer-acquisition-niche-selection-lead-magnets-outreach]]); 6 invalid wikilinks fixed; the 60,000× line corrected; corpus-first confirmed by direct grep.

## Verification posture

- **Refute-first**: verifiers were told to try to disprove each claim and default to skeptical.
- **Two-axis**: a claim can be faithfully transcribed (SUPPORTED) yet externally FALSE (e.g. C4) — both axes recorded.
- **Distortion catch**: two claims (C6 Dan Henry, C14 "Zara") were extraction over-reaches caught by verification and corrected, not shipped — see [[caveats-and-corrections]].
- **ASR-aware**: because captions mangle "copywriting" and numbers, every quotable figure/name was checked against the transcript, not trusted from one caption line.

## Corpus placement

- **Corpus-first**: the wiki's **first copywriting / marketing-skills topic** and its first business-persuasion-craft subject — verified by grep (no prior `copywriting`/`marketing` topic).
- **Off the usual theme**: unlike the AI/agent/dev-tooling majority of the corpus, this is a human-skill course; ingested at the operator's explicit request as a new vertical.
- Second Vietnamese-source topic cluster alongside the VN dev/practitioner videos (e.g. data-structures, quanit, hoidanit).

## Key Takeaways

- One 11h video, analysed at ~148K words by a 50-agent refute-first workflow, then QA'd in the main loop.
- No NotebookLM; transcript read directly; `notebook_id: none`.
- The provenance itself is the guarantee: every claim traces to a chunk + a verification verdict.
