# Source Provenance

## The 6-video bundle

| # | Video ID | Title (as published) | Speaker / Channel | Date | Len | Views* |
|---|---|---|---|---|---|---|
| ⭐ anchor | [`n97BCfyFIvw`](https://www.youtube.com/watch?v=n97BCfyFIvw) | "The engineer of the future is the person who is able to choose what is worth doing." | **Addy Osmani** / AI Engineer | 2026-07-14 | 18:26 | ~24.9K |
| 2 | [`g8um2AEf5ZA`](https://www.youtube.com/watch?v=g8um2AEf5ZA) | AI Dev 26 x SF: The Future of Software Engineering | **Andrew Ng** / DeepLearningAI | 2026-05-20 | 19:21 | ~53K |
| 3 | [`LCEmiRjPEtQ`](https://www.youtube.com/watch?v=LCEmiRjPEtQ) | Software Is Changing (Again) | **Andrej Karpathy** / Y Combinator | 2025-06-19† | 39:31 | ~2.5M |
| 4 | [`8h9j2rskP14`](https://www.youtube.com/watch?v=8h9j2rskP14) | The next era of AI coding | **Michael Truell** / Cursor | 2026-05-12 | 9:38 | ~105K |
| 5 | [`ubrfeaLEVVA`](https://www.youtube.com/watch?v=ubrfeaLEVVA) | Software Engineering + AI = ? | **Gergely Orosz** / Sonar Summit 2026 | 2026-03-04 | 36:51 | ~669 |
| 6 | [`R9K2574YEAg`](https://www.youtube.com/watch?v=R9K2574YEAg) | The Future of AI Agents: What Will Interrupt 2027 Look Like? | **Harrison Chase** / LangChain (Interrupt 26) | 2026-05-21 | 22:10 | ~42K |

\* View counts at ingest (2026-07-22). † Karpathy's talk (YC page: recorded June 17 2025) is ~13 months older than the rest — the canonical foundation the newer talks build on.

## Ingest method (Path 1 `/loop autopilot research <video>`)

- **Selection:** operator-submitted anchor `n97BCfyFIvw` (FORCE-INCLUDE) + 5 yt-search siblings on "future of software engineering role AI agents keynote," chosen to triangulate Osmani's thesis across distinct vantage points (authority / mechanism / trajectory / field-evidence / systems).
- **Fetch:** `yt-dlp --write-auto-subs --write-subs --sub-langs "en.*" --sub-format vtt --cookies-from-browser chrome` — all 6 fetched cleanly, **no 429 / bot-gate**. Larger of `.en` vs `.en-orig` chosen per video → `bin/vtt-to-md.py` → **~27.4K words** total, **read in full in the main loop.**
- **NotebookLM:** none (`notebook_id: none`).
- **Raw capture:** `raw/2026-07-22-engineer-of-the-future-osmani-aie-keynote-bundle.md`.
- **Transcripts:** session-local scratchpad (`scratchpad/md/*.md`) — not committed.

## Verification

- **Workflow `wf_dabc1f67-f9f`** — 15 refute-first claim-cluster verifiers (WebSearch/WebFetch, "default to UNVERIFIABLE if thin") + 1 corpus-collision agent. **16 agents; 0 errors / 0 empty / 0 skipped; ~711K tokens; 253 web tool calls; ~4.9 min; all Haiku 4.5.**
- Main-loop Opus authored all articles from full transcript context, folding in verdicts (maker/checker split — verifiers independent of the author).
- Scorecard: [[engineer-of-the-future/claims-scorecard]] (53 claims: 29 C / 21 CBI / 1 MIS / 2 UNV / 0 FALSE / 0 FAB). Corrections: [[engineer-of-the-future/caveats-and-corrections]].
- **Collision result:** no duplication — distinct from [[workflow-ai-coding/_index]] (different 6-talk synthesis, May 2026) and [[harness-engineering/_index]] (discipline layer). Cross-link targets confirmed on disk.

## Provenance caveats

- **Speaker attribution** for talks 4 & 5 (Truell; Orosz) and the venue/keynote-title specifics were **web-confirmed**, not taken from captions alone.
- **Model-tier note:** workflow ran all agents on Haiku 4.5; every load-bearing correction was cross-checked against the verifier evidence + sources before shipping. No per-agent model override was attempted.
- PII discipline: individuals identified by their public professional identity (talk speakers / named creators); no private info added.

## See also

- [[engineer-of-the-future/_index]] · [[engineer-of-the-future/convergent-thesis]] · [[engineer-of-the-future/claims-scorecard]] · [[engineer-of-the-future/caveats-and-corrections]]
