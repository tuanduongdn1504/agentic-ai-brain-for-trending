# Source Provenance — api-types

## The bundle (6 videos)

A 6-video NotebookLM bundle: 1 operator-submitted **anchor** (force-included) + 5 picked by the drain's search/scoring rubric.

| # | Channel | Title | Lang | Uploaded | Length | Views | URL |
|---|---|---|---|---|---|---|---|
| 1 ⚓ | **LetDiv – Học Lập Trình Đảm Bảo** | 7 Loại API Bạn Phải Biết: Giải Thích Đơn Giản 9 Phút! | VN | 2026-07-17 | 12:38 | ~8.2K | https://www.youtube.com/watch?v=RsgyCswZBGA |
| 2 | **Codist** | Every Type of API Simply Explained in 9 Minutes! | EN | 2025-09-27 | 9:53 | ~991K | https://www.youtube.com/watch?v=pBASqUbZgkY |
| 3 | **Learn with Whiteboard** | Difference Between REST API vs Web API vs SOAP API Explained | EN | 2023-05-12 | 7:24 | ~490K | https://www.youtube.com/watch?v=2mqN7ZhDsUA |
| 4 | **Ulbi TV** | Что такое Rest API (http)? Soap? GraphQL? Websockets? RPC (gRPC, tRPC) | RU | 2023-10-02 | 57:30 | ~972K | https://www.youtube.com/watch?v=XaTwnKLQi4A |
| 5 | **Be A Better Dev** | REST API (HTTP) vs Websockets — Concept Overview With Example | EN | 2021-11-18 | 7:07 | ~321K | https://www.youtube.com/watch?v=fG4dkrlaZAA |
| 6 | **ByteByteGo** | What Is GraphQL? REST vs. GraphQL | EN | 2022-11-10 | 5:14 | ~530K | https://www.youtube.com/watch?v=yWzKJPw_VzM |

⚓ = operator-submitted anchor (the origin of this topic).

## Who covers what

- **REST fundamentals + taxonomy:** LetDiv, Codist, Learn with Whiteboard, Ulbi TV
- **SOAP / enterprise:** LetDiv, Learn with Whiteboard, Codist
- **GraphQL (incl. the contrarian caution):** ByteByteGo (the skeptic), LetDiv, Codist, Ulbi TV
- **gRPC / RPC / tRPC:** Codist, LetDiv, Ulbi TV (tRPC is Ulbi TV's addition)
- **WebSocket / polling / real-time:** Be A Better Dev, Ulbi TV
- **Webhook:** LetDiv, Codist
- **WebRTC:** noted across the anchor + summary

## Ingestion

- **Trigger:** `/loop autopilot research` (Path 1), operator-submitted anchor → queued in `raw/topics-queue.md` → drained.
- **Pipeline:** `bin/autopilot-drain.py` — anchor force-include (validated PASS 1/1) → `yt-dlp ytsearch` (top-15) → score/diversity select (top-6, recency filter relaxed since canonical explainers predate the 6-month window) → NotebookLM bundle → 1 summary + 4 asks (Trends / Outliers / Gaps / Takeaways).
- **NotebookLM notebook:** `ed17cc3d-952c-4fe0-9572-27a418d0f390`
- **Raw analysis:** `raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md` (18KB)

## Verification & compile

- **Workflow:** `wf_640f115f-0a8` — 25 agents (11 refute-first claim verifiers + 1 corpus-collision grep + 12 article drafters + 1 completeness critic). **0 errors / 0 empty / 0 skipped.** ~1.28M tokens, 158 tool calls, ~5.2 min. All agents Haiku 4.5 (disclosed).
- **Main-loop finalize (Opus):** authored [[claims-scorecard]] / [[caveats-and-corrections]] / this file / [[_index]]; QA'd article prose; deterministically fixed + filesystem-validated every wiki-link (157 checked); updated `wiki/_master-index.md` + `raw/_inventory.md`.
- **Loop log:** `loop-log/(C) 2026-07-21-<HH>-autopilot-loop.md`

## Caveats on provenance

- Mixed-language bundle (VN + EN + RU). NotebookLM handles multilingual sources; the digest is English paraphrase, **not** verbatim quotes — attributions are to who advanced an idea, not exact wording.
- View counts / upload dates captured at ingest (2026-07-21) via `yt-dlp`; treat as approximate.

## Key Takeaways

- 6 videos, 5 channels + 1 VN anchor, spanning 2021–2026 and 3 languages — high-view canonical explainers (ByteByteGo, Codist) anchored on the operator's LetDiv video.
- Deterministic ingest (drain script) + adversarial verification (25-agent workflow) + Opus main-loop QA — fully reproducible from the notebook id + raw file + workflow id above.
- ByteByteGo is the load-bearing skeptic (the GraphQL cautions); Ulbi TV is the broadest single source (57 min, adds tRPC).
