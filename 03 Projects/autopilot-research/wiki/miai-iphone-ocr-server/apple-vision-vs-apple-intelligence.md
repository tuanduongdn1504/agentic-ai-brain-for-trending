# Vision framework ≠ Apple Intelligence / Foundation Models (the headline correction)

The video's **single misleading framing**, and the most useful thing to get right about this whole topic.

## What the video says

- Intro: *"hôm nay chúng ta sẽ cùng nhau tận dụng cái trí khôn của Apple, Apple Intelligent … để làm một cái OCR server"* — "today we'll harness the intelligence of Apple, Apple Intelligence … to make an OCR server."
- Architecture slide (correct): the layer under the app is labeled **"Apple Vision Framework."**
- But the narration then says the Vision framework is *"một framework mà Apple cho mọi người để dùng được cái foundation model của ông ở dưới"* — "a framework Apple gives you to use its foundation model underneath."

That last sentence is the error: **the Vision framework is not a wrapper over the Foundation Models LLM.** They are two separate frameworks.

## The ground truth

The app's own README settles it: it *"relies **solely** on Vision Framework"* — **"neither Apple Intelligence nor any language model is mentioned."** ([README](https://raw.githubusercontent.com/riddleling/iOS-OCR-Server/main/README.md))

| | **Vision framework** | **Foundation Models framework / Apple Intelligence** |
|---|---|---|
| What | Computer-vision image analysis (incl. text recognition/OCR) | On-device generative **LLM** (~3B params) |
| Shipped | **iOS 13, 2019** (text recognition) | **WWDC June 2025** (developer API) |
| Does the OCR here? | **Yes** — `VNRecognizeTextRequest` + `RecognizeDocumentsRequest` | **No** — not used by this app at all |
| Output | Text + bounding boxes + document structure | Free-form / structured *generated* text |
| Marketing hook | (none in this app) | "add on-device AI in **three lines of code**" (`@Generable`) |

Both run **on-device on the Neural Engine**, both are free — which is why the *outcome* the video promises (free, private, no-cloud OCR) is entirely true. Only the *attribution* is wrong.

## Why the distinction matters (not pedantry)

1. **Reproducibility.** Anyone copying this doesn't need Apple Intelligence, an iPhone 15 Pro+, or iOS 26 for the basic `/upload` box mode — `VNRecognizeTextRequest` works back to iOS 13 on far older hardware. (The `/docOCR` structured mode *does* need the newer `RecognizeDocumentsRequest`; see [[miai-iphone-ocr-server/vision-ocr-mechanics]].)
2. **Capability expectations.** Vision OCR *transcribes* pixels; it does not *understand* them. It won't summarize a CV or answer questions — that's the LLM's job (and where a hireui pipeline would hand off from OCR to Claude). Conflating the two oversells what the box does.
3. **The corpus already tracks Foundation Models** as a real, separate thing: it's the on-device model referenced in [[local-ai-coding-agents/_index]] ("watch-not-build: Apple Foundation on-device") — verified real (WWDC 2025, `LanguageModelSession()`, ~3 lines), just **not what this OCR app uses**.

## Verdict

- The **Foundation Models "three lines of code" claim (C2) is CONFIRMED** as a standalone Apple fact.
- The **OCR-via-Vision claim (C4) is CONFIRMED as the mechanism**, but the **video's framing that ties the OCR to Apple Intelligence is MISLEADING** — the actual engine is the classic Vision framework, and the app uses no LLM.

## Key Takeaways

- **The OCR is Vision, full stop.** No Apple Intelligence, no Foundation Models LLM in this app.
- Vision (2019) and Foundation Models (2025) are **separate frameworks**; the video merges them.
- The *result* (free, on-device, private) is real; only the *how* is mis-labeled.
- Practical upshot: `/upload` box OCR runs on old hardware/iOS; only the structured `/docOCR` needs iOS 26.

Sources: [developer.apple.com/documentation/vision/vnrecognizetextrequest](https://developer.apple.com/documentation/vision/vnrecognizetextrequest) · [FoundationModels](https://developer.apple.com/documentation/FoundationModels) · [WWDC25 s.286](https://developer.apple.com/videos/play/wwdc2025/286/) · [iOS-OCR-Server README](https://raw.githubusercontent.com/riddleling/iOS-OCR-Server/main/README.md).
