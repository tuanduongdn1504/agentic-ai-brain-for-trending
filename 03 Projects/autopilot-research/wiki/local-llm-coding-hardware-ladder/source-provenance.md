# Source provenance

## The seven sources

| # | Title | Channel | Uploaded | Len | Views @ ingest | Lang | How selected |
|---|---|---|---|---|---|---|---|
| 1 | Thử local LLM, coding trên Mac mini M4, 64GB ram \| quanIT | **Quân IT** | 2026-08-19 | 48:34 | 1,755 | `vi-orig` | **operator anchor** |
| 2 | M4 Pro Mac Mini 24GB RAM vs Local LLMs: Can It Handle It? | WEBdoze | 2026-05-22 | 16:45 | 7,291 | `en-orig` | yt-search rubric |
| 3 | Local AI Coding is Finally Good Enough | ForrestKnight | 2026-06-18 | 21:57 | 179,582 | `en-orig` | yt-search rubric |
| 4 | Finally, The CORRECT Way to Run Local AI on a Mac | Samuel Gregory | 2026-06-30 | 08:36 | 59,285 | `en-orig` | yt-search rubric |
| 5 | The Unbeatable Local AI Coding Workflow (Full 2026 Setup) | Zen van Riel | 2026-03-01 | 16:11 | 259,982 | `en-orig` | yt-search rubric |
| 6 | The Best LOCAL Agentic Coding Workflow (Complete Guide) | Tech With Tim | 2026-06-10 | 33:16 | 179,322 | `en-orig` | yt-search rubric |
| 7 | **WWDC26: Run local agentic AI on the Mac using MLX** | **Apple Developer** | 2026-06-08 | 13:37 | 493,366 | `en-orig` | **main-loop addition** |

**Total:** 27,896 words / 329 timestamped paragraphs. All seven transcripts read **in full in the main loop**. **NotebookLM: none** — a claims scorecard cannot grade a paraphrase.

## Method

- **Path 1** (`/loop`), anchored bundle. Query: `local LLM coding agent Mac mini M4 64GB RAM offline`, selected after testing three candidate queries.
- Selection by `bin/autopilot-drain.py --dry-run` (anchor probe → yt-search ×15 → recency/views/duration filter → rank). **Anchor validation: PASS 1/1, overlap 100%.**
- Captions: `yt-dlp --write-auto-subs --sub-langs <orig>` → `bin/vtt-to-md.py` → timestamped markdown.
- Raw analysis: `raw/2026-08-20-local-llm-coding-apple-silicon-hardware-ladder.md`.

## Why source #7 was added by hand

The drain rubric ranks on recency, views, duration and engagement. **It has no notion of authority.** It cannot prefer a vendor engineer explaining the silicon over a YouTuber benchmarking it.

Apple's WWDC26 session 232 surfaced during query testing (493K views) but did not win a slot. The completeness critic was explicitly asked whether a first-party Apple source existed that would settle the MLX and unified-memory questions better than any YouTuber — and it does. It was pulled in the main loop and became the **single best-sourced article in the topic** ([[apple-mlx-stack]]): it supplied the prefill mechanism, the M5 4× matmul figure, continuous batching, distributed inference, and the statement that Ollama/LM Studio/vLLM all sit on MLX.

**Standing lesson for this project:** an engagement-ranked rubric systematically under-weights primary/vendor sources, because vendor documentation sessions don't compete with tutorials on watch metrics. **On any topic with a first-party owner, check for the vendor's own material before compiling** — the rubric will not do it for you.

## Verification

**Workflow `wf_9dd08c75-e02`** — 24 agents (6 grouped claim verifiers → 17 refute-first adversarial passes → 1 completeness critic). **1,409,555 tokens · 387 tool calls · 336 s · 0 errors / 0 empty / 0 skipped.** All agents ran on Haiku 4.5.

Structure: `pipeline()` over six claim groups, each verifier's CONFIRMED/FALSE findings fanned out immediately to independent refuters instructed to *default to refuted if they could not reproduce the evidence from a primary source*.

**Plus 7 main-loop checks by Opus**, which produced 3 of the topic's most load-bearing facts:
- **Qwen3.6-27B exists** (agent said it didn't) — 2026-04-22, Apache-2.0
- **Warp open-sourced the client only**, AGPL-3.0, Oz stays proprietary
- **The M4 memory ladder** — base M4 caps at 32 GB, so the anchor's 64 GB mini is an M4 Pro at 273 GB/s
- Plus RTX 5090 = 1,792 GB/s, and independent corpus collision greps

**The refute-first stage paid for itself once**: the `verify:qwen-models` agent denied Qwen3.5 existed; its own refuter overturned it against the official model card. See [[caveats-and-corrections]] §C.

## Corpus collisions (checked by grep in the main loop, not agent-asserted)

| Term | Files in corpus before this topic |
|---|---|
| **OMLX / oMLX** | **0** — new to the corpus |
| LM Studio | 14 |
| Ollama | 41 |
| Qwen | 27 |
| MLX | 12 |
| "unified memory" | 5 |
| "KV cache" | 4 |

**New to the corpus:** OMLX; the SSD-persistent prefix-cache pattern; LM Studio device linking; VS Code native custom-endpoint model management; the type-checker-invisible bug class; the silent-hang-on-small-context failure; the model-identity-follows-system-prompt trap; Apple's four-layer MLX stack as a first-party source.

## Creator prior

Second Quân IT topic. His first — [[../quanit-becoming-ai-engineer-2026/_index|quanit-becoming-ai-engineer-2026]] — graded **0 FALSE / 0 FABRICATED / 1 MISLEADING / 1 UNVERIFIABLE**: sound verdicts, overstated specifics. **This ingest reproduces that profile exactly** — his one FALSE is a misread on-screen list; his analytical verdict and his self-diagnosis of the context failure are both correct.

## Deepen candidates

1. **⭐ An M5-generation agentic-coding test against a real repository.** The largest open question in the topic. Apple claims 4× matmul on M5 for exactly this bottleneck; nobody has measured it on a large codebase. Samuel Gregory and Tech With Tim both own M5 Max machines.
2. **Apple WWDC26 session 233** — *"Explore distributed inference and training with MLX"*, referenced by session 232. Would deepen [[apple-mlx-stack]].
3. **OMLX hands-on** — the SSD-persistent prefix cache is the most promising prefill mitigation in the bundle and has zero corpus coverage. Apache-2.0, solo-maintained (supply-chain caution applies).
4. **Alex Ziskind** — appeared repeatedly across all three test queries with large hardware-benchmark reach (*"Mac Studio vs. Mini"*, *"$10,000 Mac Studio vs. $10 AI Agent"*), never won a slot. A dedicated bandwidth/TCO bundle.
5. **Asad Tinkers, "The Ultimate Local Mac Agentic AI Coding Workflow"** (951 views) — **below `MIN_VIEWS=1000`, so the rubric structurally cannot select it.** Needs an anchor. Same structural blind spot logged in the deepseek-harness ingest.

## See also
[[_index]] · [[claims-scorecard]] · [[caveats-and-corrections]] · [[apple-mlx-stack]]
