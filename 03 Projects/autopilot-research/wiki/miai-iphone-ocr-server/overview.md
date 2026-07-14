# Overview — iPhone as a free local OCR server

Source: Mì AI, [`NvPoE9cNJVg`](https://www.youtube.com/watch?v=NvPoE9cNJVg) (2026-07-14, 19:26, VN). Raw: `raw/2026-07-14-miai-iphone-ocr-server.md`.

## What the video actually does

- Installs a **third-party App Store app** on an iPhone that starts an **HTTP OCR server on the device** (default **port 8000**, LAN-reachable).
- From a laptop, writes ~5 lines of Python (`requests.post` a file to `http://<phone-ip>:8000/upload`) and gets back **text + bounding boxes**; draws the boxes with **OpenCV**.
- Switches to the `/docOCR` endpoint ("paragraph mode") and gets back **document structure as Markdown**, including a **reconstructed table** (a café menu).
- Tests three images: a **printed invoice** (works, fast), a **prescription** (all drug names read), and **Vietnamese handwriting** (fails).
- Notes the same developer ships a **Mac tool** (`docOCR`) and floats a Mac-mini-M4 build for a higher-performance server.

## The stack (verified)

| Layer | What it is | Verified |
|---|---|---|
| App | [`riddleling/iOS-OCR-Server`](https://github.com/riddleling/iOS-OCR-Server) → "OCR Server" ([App Store](https://apps.apple.com/us/app/ocr-server/id6749533041)) | ✅ MIT, Swift, 1,771★, created 2025-08-01 |
| Server | SwiftNIO HTTP server on the phone, port 8000, endpoints `/upload` + `/docOCR` | ✅ README + Show HN |
| OCR (boxes) | Apple Vision `VNRecognizeTextRequest` (recognitionLevel `.accurate`/`.fast`) | ✅ developer.apple.com |
| OCR (structure) | Apple Vision `RecognizeDocumentsRequest` — **new at WWDC 2025 / iOS 26** (paragraphs, lists, **tables**) | ✅ developer.apple.com + WWDC25 s.272 |
| Silicon | Apple **A-series** chip + **Neural Engine** (on-device inference) | ✅ (video caption said "Google" — a garble) |
| Mac sibling | [`riddleling/docOCR`](https://github.com/riddleling/docOCR) — images → Markdown, CLI + HTTP | ✅ MIT, Swift, created 2026-05-26 |

## Honesty read

This is a **high-integrity practitioner demo** — the same tier as [[local-ai-coding-agents/_index]], [[github-copilot-cli-agents/_index]] and [[codesistency-mobile-app-course/_index]], and the honest cousin of the same channel's rigorous [[miai-cv-matching-agent/_index]]. Every tool is real, the whole thing works, and the presenter *volunteers* the weak spots (Vietnamese handwriting fails; the multi-iPhone cluster is "I haven't tried this").

The **single soft spot** is the framing: the intro credits *"tận dụng trí khôn của Apple Intelligence"* ("harnessing Apple Intelligence") and says the Vision framework "lets apps use the foundation model underneath." In fact the OCR is 100% the **classic Vision framework** — the app's own README states it "relies **solely** on Vision Framework… neither Apple Intelligence nor any language model is mentioned." Vision text recognition predates Apple Intelligence by six years (iOS 13, 2019). See [[miai-iphone-ocr-server/apple-vision-vs-apple-intelligence]].

## Why this topic is in the corpus

OCR is the **front door of document/CV parsing** — the exact hireui domain. And this is the **on-device / data-residency** version of it: candidate documents never leave the device. It is the OCR analogue of [[local-ai-coding-agents/privacy-data-residency]] and the on-device counterpart to the cloud-vision parsing in [[jasonlee-claude-mobile-app/receipt-scanning-with-claude-vision]]. See [[miai-iphone-ocr-server/data-residency-and-hireui]].

## Key Takeaways

- **Real, free, works.** An iPhone/iPad/Mac becomes a zero-cost local OCR REST server via an MIT App Store app — no cloud, no token.
- **It's Vision, not Apple Intelligence.** The OCR engine is the classic Vision framework (2019), not the 2025 Foundation Models LLM — the video conflates them.
- **Two modes:** `/upload` = text + boxes (`VNRecognizeTextRequest`); `/docOCR` = structured Markdown incl. tables (`RecognizeDocumentsRequest`, new iOS 26).
- **Vietnamese caveat:** printed Vietnamese works; **handwriting fails** — Vietnamese isn't an officially-supported Vision recognition language.
- **The operator value is data residency**, not novelty: on-device OCR keeps candidate PII off any cloud.
