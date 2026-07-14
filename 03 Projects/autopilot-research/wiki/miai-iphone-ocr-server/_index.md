# miai-iphone-ocr-server

> **Topic index.** A Mì AI video turns an **iPhone / iPad / Mac into a free, fully local OCR server** using a third-party App Store app built on Apple's on-device **Vision framework**, then calls it over LAN by REST API. Verified claim-by-claim.

**Source:** Mì AI (Nguyễn Chiến Thắng), *"Hô biến iPhone thành local OCR server giá 0 đồng"* — [`NvPoE9cNJVg`](https://www.youtube.com/watch?v=NvPoE9cNJVg), uploaded **2026-07-14** (same day as ingest), 19:26, Vietnamese, 373 views at ingest.
**Raw:** `raw/2026-07-14-miai-iphone-ocr-server.md` (full VN transcript, read in full in main loop).
**Compiled:** 2026-07-14 (path 5 yt-dlp; verified via Workflow `wf_d1421e99-019` — 12 agents, 6 dives + 5 refute-first verifiers + 1 critic, ~566K tokens, 223 tool calls, 0 errors, 1 empty [app-repo, fully covered by main-loop anchors] — all on Haiku 4.5, reconciled against ~8 main-loop `gh api`/WebSearch/WebFetch anchors).

---

## The one-paragraph version

The app is **[`riddleling/iOS-OCR-Server`](https://github.com/riddleling/iOS-OCR-Server)** ("OCR Server" on the [App Store](https://apps.apple.com/us/app/ocr-server/id6749533041), free) — a SwiftNIO HTTP server that runs *on the phone*, binds **port 8000**, and exposes two REST endpoints: **`/upload`** (returns text + bounding boxes, via `VNRecognizeTextRequest`) and **`/docOCR`** (returns document structure incl. tables, via the new iOS-26 `RecognizeDocumentsRequest`). Everything runs **on-device on the Apple Neural Engine** — no cloud, no token, no API key, genuinely free. The demo works on printed Vietnamese invoices/prescriptions and reconstructs a menu table as Markdown; it fails on Vietnamese **handwriting**. The **one correction that matters:** the OCR is done entirely by Apple's classic **Vision framework** (shipping since iOS 13/2019) — the app uses **no Apple Intelligence and no Foundation Models LLM** despite the video's intro framing.

## Articles

- [[miai-iphone-ocr-server/overview]] — what the video shows, the stack, honesty read
- [[miai-iphone-ocr-server/the-app-ios-ocr-server]] — the real app, its Mac sibling `docOCR`, the developer, the OCR-tool ecosystem, endpoints & settings
- [[miai-iphone-ocr-server/apple-vision-vs-apple-intelligence]] — **the headline conflation**: Vision framework ≠ Apple Intelligence / Foundation Models
- [[miai-iphone-ocr-server/vision-ocr-mechanics]] — `VNRecognizeTextRequest` (accurate/fast, boxes) + `RecognizeDocumentsRequest` (iOS 26, tables → Markdown)
- [[miai-iphone-ocr-server/language-support-and-vietnamese]] — the Vietnamese + handwriting limitation and *why* (a coverage gap, not just fine-tuning)
- [[miai-iphone-ocr-server/data-residency-and-hireui]] — the real payload for the operator: on-device OCR = candidate PII never egresses
- [[miai-iphone-ocr-server/claims-scorecard]] — the 12-claim scorecard (10 CONFIRMED / 1 incomplete / 1 misleading / 0 false / 0 fabricated)
- [[miai-iphone-ocr-server/caveats-and-corrections]] — chip garble, Taiwanese-not-Chinese, free-with-tip, version skew, the two main-loop overrides
- [[miai-iphone-ocr-server/source-provenance]] — channel, developer, event, methodology, all source URLs

## Cross-links

- [[local-ai-coding-agents/privacy-data-residency]] — the **same data-residency pole** (local inference = PII never leaves the machine); this is the OCR analogue
- [[miai-cv-matching-agent/_index]] — **same channel** (Nguyễn Chiến Thắng); OCR is the missing document-ingestion **front end** for that CV-matching agent
- [[jasonlee-claude-mobile-app/receipt-scanning-with-claude-vision]] — the **cloud-vision** sibling (receipt/CV parsing via Claude vision); this is the on-device counterpart
- [[api-security-7-techniques/hireui-security-posture]] — PII-handling / data-flow posture
- [[mosh-ai-powered-apps/_index]] — the vendor-seam pattern an OCR microservice would sit behind
- [[google-ai-studio-github-import/pricing-privacy-data]] — residency spectrum (AI Studio free = weakest pole; local OCR = strongest)

**hireui pilot deliverable:** `output/(C) 2026-07-14-miai-iphone-ocr-server-pilot-methods.md`
