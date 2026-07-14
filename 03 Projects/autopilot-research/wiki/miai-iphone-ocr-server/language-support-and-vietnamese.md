# Language support & the Vietnamese limitation

The video's most honest moment — and the most important caveat for a Vietnamese (or hireui) audience.

## What the demo shows (claim C8)

- **Printed invoice (hóa đơn):** recognized, fast. ✅
- **Prescription (đơn thuốc):** all drug names read correctly. ✅
- **Vietnamese handwriting (chữ viết tay):** **recognized WRONG.** ❌
- Presenter's explanation: *"model này không phải là fine-tune cho tiếng Việt"* — "this model isn't fine-tuned for Vietnamese; I'm just borrowing it."

Verdict: **C8 CONFIRMED** (the presenter honestly reports his own on-screen results) — and the behavior is exactly what Apple's language coverage predicts.

## Why it behaves this way (the deeper, verified reason)

The presenter frames it as a *fine-tuning* gap. The more accurate framing is a **language-coverage** gap:

- Apple Vision's **`VNRecognizeTextRequest`** historically supports a **limited, explicit language list** — around en, fr, it, de, es, pt, zh (plus more in newer revisions/`.accurate`). **Vietnamese (`vi`) is not in the classic documented list.** Query it at runtime with [`supportedRecognitionLanguages(for:revision:)`](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:)).
- **Printed Vietnamese still works reasonably** because it's **Latin script** — the recognizer handles the base letters even without official `vi` support; diacritics (dấu) are where it slips.
- **Handwriting is the hard case twice over:** handwriting recognition is only supported for a *subset* of languages, and Vietnamese isn't among them. Independent comparisons put Apple Vision at **~72% on handwriting** vs ~91% for Google Cloud Vision; specialized Vietnamese-handwriting OCR reaches ~99%. So a Vietnamese handwriting miss is **expected**, not a bug.
- **Separate, easy to confuse:** Apple *Intelligence* (the LLM) added Vietnamese support in the iOS 26.x cycle — but that's a **different system** and does **not** power this app's OCR. Vietnamese Apple-Intelligence support ≠ Vietnamese Vision-OCR support.

## Implication

- For **printed, structured Vietnamese** (invoices, prescriptions, menus, and — relevant to hireui — **typed CVs**) the tool is "khá ổn" (pretty OK), as the presenter says, good enough to then hand structured text to a downstream extractor.
- For **handwriting** or **diacritic-critical** text, don't rely on it — this is precisely where a cloud OCR (Google Cloud Vision, Azure, or a Vietnamese-specific model) still wins, and where the residency-vs-accuracy trade-off in [[miai-iphone-ocr-server/data-residency-and-hireui]] has to be made explicitly.

## Key Takeaways

- **Printed Vietnamese: usable. Vietnamese handwriting: don't trust it.** The presenter says so himself.
- The real reason is **Vietnamese isn't an officially supported Vision recognition language** — it works for print only because it's Latin script.
- **Apple Intelligence Vietnamese support ≠ Vision-OCR Vietnamese support** — different frameworks.
- Any hireui use must **eval OCR quality on real Vietnamese CVs first** — the residency win is only worth it if accuracy clears the bar.

Sources: [VNRecognizeTextRequest](https://developer.apple.com/documentation/vision/vnrecognizetextrequest) + [supportedRecognitionLanguages](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:)) + [RecognizeDocumentsRequest (26 langs)](https://developer.apple.com/documentation/vision/recognizedocumentsrequest); Apple Developer Forums thread 121048 (historical language list).
