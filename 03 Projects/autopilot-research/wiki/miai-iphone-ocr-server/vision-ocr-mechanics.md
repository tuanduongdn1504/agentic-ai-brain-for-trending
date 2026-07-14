# Vision OCR mechanics: the two engines behind the two endpoints

How the app's `/upload` and `/docOCR` actually work, verified against Apple docs.

## `/upload` → `VNRecognizeTextRequest` (classic, since iOS 13)

- **API:** [`VNRecognizeTextRequest`](https://developer.apple.com/documentation/vision/vnrecognizetextrequest) — Apple's on-device text-recognition request, shipping since **iOS 13 (2019)**.
- **Recognition level** ([`recognitionLevel`](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/recognitionlevel)) — the video's "accurate vs fast" setting is this exact property:
  - `.accurate` — neural-network path, slower (~seconds), higher quality, broader language support.
  - `.fast` — character-recognition path, near-instant, Latin-focused, lower quality.
- **Language options:** `usesLanguageCorrection` (post-recognition spell/word correction — the video's "language correction" toggle) and automatic language detection (the "auto-detect" toggle).
- **Output:** `VNRecognizedTextObservation` per detected region → a recognized **string** + a **normalized bounding box** (0–1) with corner coordinates. The app serializes these into the `ocr_boxes` JSON array (`x,y,w,h` + corners + `text`) that the video draws with **OpenCV**. This is claim **C6 — CONFIRMED**.

## `/docOCR` → `RecognizeDocumentsRequest` (new, WWDC 2025 / iOS 26)

- **API:** [`RecognizeDocumentsRequest`](https://developer.apple.com/documentation/vision/recognizedocumentsrequest) → produces a [`DocumentObservation`](https://developer.apple.com/documentation/vision/documentobservation). Introduced at **WWDC 2025** ([session 272, "Read documents using the Vision framework"](https://developer.apple.com/videos/play/wwdc2025/272/)); available **iOS/iPadOS/macOS 26**.
- **What's different:** instead of a flat list of text lines, it returns a **hierarchical document model** — a container holding **text, paragraphs, lists, tables, and barcodes**, plus data detectors (emails, phone numbers, URLs). Recognizes **26 languages**.
- **Tables** ([recognize-tables docs](https://developer.apple.com/documentation/Vision/recognize-tables-within-a-document)): a 2D array of cells addressable by row/column, with per-cell row/column ranges (a cell can span multiple rows/cols) and a table bounding region. This is exactly the **Markdown table** the video reconstructs from a café menu (claim **C7**).
- The Mac `docOCR` tool explicitly converts this structure to **Markdown**. On iOS, the `/docOCR` endpoint's structured output is what the video renders as MD (the app added "recognizing lists and tables" in a 2026-05-28 commit).

### C7 nuance (why it's CORRECT-BUT-INCOMPLETE, not fully CONFIRMED)

- **Structure + tables + Markdown = real and confirmed.**
- **"Faster than box mode"** is the presenter's on-screen impression, **not quantified** in any public source — plausible (document-aware batching) but unbenchmarked.
- There's a minor doc-vs-demo ambiguity: the iOS README's `/docOCR` sample shows a text field, while the *Mac* `docOCR` tool is the one explicitly documented to emit Markdown. The video clearly shows the iOS `/docOCR` producing MD-structured output with a table, so the endpoint does structure detection — but the exact output-format contract isn't fully pinned in the README.

## Silicon: it runs on the Apple Neural Engine

- Both requests execute **on-device** on the **Apple Neural Engine** (part of the A-series chip on iPhone/iPad, M-series on Mac). This is what makes it fast and offline. The video's caption crediting *"chip A của Google"* is a **transcription garble** — the A-series chip is **Apple's** (designed by Apple, made by TSMC), not Google's. See [[miai-iphone-ocr-server/caveats-and-corrections]].

## Key Takeaways

- **`/upload` = `VNRecognizeTextRequest`** — old, ubiquitous, returns text + boxes; "accurate/fast" = `recognitionLevel`.
- **`/docOCR` = `RecognizeDocumentsRequest`** — new at WWDC 2025 (iOS 26), returns hierarchical structure incl. **tables**, which is what enables Markdown output.
- **Tables are a first-class Apple API feature now** (2D cell model with spans) — not a hack.
- Everything runs on the **Neural Engine, on-device** — the source of the speed and the privacy.

Sources: developer.apple.com Vision docs (linked inline) + WWDC25 session 272.
