# (C) Autopilot Overnight Drain — 2026-07-21-13

> **Mode:** Path A (mechanical Python orchestrator)
> **Trigger:** unattended (launchd UserAgent)
> **Started:** 2026-07-21 13:??

---

## Raw run log

```
[13:37:35] === Autopilot drain start 2026-07-21 ===
[13:37:35] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[13:37:35] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[13:37:35] pending topics: 1
[13:37:35]   1. API types explained (REST, SOAP, GraphQL, gRPC, WebSocket, webhook) (+ 1 anchor)
[13:37:35] will drain: 1
[13:37:35] --- Drain: API types explained (REST, SOAP, GraphQL, gRPC, WebSocket, webhook)
[13:37:35]   query: API types explained REST SOAP GraphQL gRPC websocket webhook
[13:37:35]   slug:  api-types-explained-rest-soap-graphql-grpc-websock
[13:37:35]   anchors: 1 URL(s) declared — will force-include
[13:37:35]   step 0/5: probe anchor URLs
[13:37:38]     ✓ anchor: [20260717] 7 Loại API Bạn Phải Biết: Giải Thích Đơn Giản 9 Phút! — LetDiv - Học Lập Trình Đảm Bảo (8,223 views)
[13:37:38]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[13:38:01]     got 14 videos
[13:38:01]   step 2/5: select top sources
[13:38:01]   only 0 pass recency filter; relaxing
[13:38:01]     picked 6 (1 anchor + 5 yt-search):
[13:38:01]       1. [ANCHOR] [20260717] 7 Loại API Bạn Phải Biết: Giải Thích Đơn Giản 9 Phút! — LetDiv - Học Lập Trình Đảm Bảo (8,223 views)
[13:38:01]       2. [20250927] Every Type of API Simply Explained in 9 Minutes! — Codist (991,046 views)
[13:38:01]       3. [20230512] Difference Between REST API vs Web API vs SOAP API Explained — Learn with Whiteboard (489,737 views)
[13:38:01]       4. [20231002] Что такое Rest API (http)? Soap? GraphQL? Websockets? RPC (g — Ulbi TV (972,345 views)
[13:38:01]       5. [20211118] REST API (HTTP) vs Websockets - Concept Overview With Exampl — Be A Better Dev (320,770 views)
[13:38:01]       6. [20221110] What Is GraphQL? REST vs. GraphQL — ByteByteGo (530,138 views)
[13:38:01]   anchor validation: PASS (1/1 declared anchors in bundle, overlap=100%)
[13:38:01]   step 3/5: notebooklm bundle
[13:38:06]     notebook: ed17cc3d-952c-4fe0-9572-27a418d0f390
[13:38:43]     added 6/6 sources
[13:38:43]   step 4/5: wait for ready
[13:38:47]   step 5/5: analysis (1 summary + 4 asks)
[13:38:54]     asking: Trends
[13:39:17]     asking: Outliers
[13:39:36]     asking: Gaps
[13:39:59]     asking: Takeaways
[13:40:14]   ✅ wrote /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-07-21-api-types-explained-rest-soap-graphql-grpc-websock.md (18,356 bytes)
[13:40:14] --- updating queue (1 drained)
[13:40:14]   queue updated
[13:40:14] === Done. drained=1 of 1 ===
```
