# The real payload: on-device OCR & data residency (for hireui)

The video treats "free" as the headline. For the operator, the headline is **where the candidate's document goes** — which is nowhere.

## The insight

OCR is the **front door of CV/document ingestion**. A recruitment SaaS (hireui) receives candidate CVs and IDs as **PDFs and image scans** full of PII (name, DOB, address, photo, sometimes national ID). The moment you send that image to a **cloud OCR API** (Google Cloud Vision, AWS Textract, Azure), the PII **egresses** to a third party and its region/retention/training terms.

**On-device Vision OCR inverts this:** the image is transcribed on hardware you control (an iPhone/iPad, or a Mac mini) and **only extracted text — or better, redacted text — leaves the device.** Candidate PII in the raw scan never touches a cloud.

This is the **OCR analogue of [[local-ai-coding-agents/privacy-data-residency]]** — local inference turns a compliance liability into an auditable internal control, giving the **strongest** GDPR / Vietnam PDPL / EU-AI-Act-high-risk posture. It sits at the opposite pole from [[google-ai-studio-github-import/pricing-privacy-data]] (managed cloud, weakest residency).

## Where it fits the hireui architecture

- **Same domain, same channel:** this is Nguyễn Chiến Thắng's channel — the OCR here is the **missing document-ingestion front end** for his own [[miai-cv-matching-agent/_index]] (which reads CV PDFs but doesn't solve scanned/image CVs).
- **Behind the vendor seam:** an OCR step slots in as a microservice behind the [[mosh-ai-powered-apps/_index]] A2 vendor seam — `scan → local OCR → (redact) → structured text → LLM Match-Explain`. The OCR provider becomes swappable (local vs cloud) at one boundary.
- **The scriptable target is `docOCR` on a Mac**, not the iPhone: a Mac mini M4 running [`riddleling/docOCR`](https://github.com/riddleling/docOCR) is an internal HTTP OCR-to-Markdown service — MIT-licensed, free, on Apple Silicon you own. Markdown output feeds an LLM cleanly.

## The honest trade-off (don't skip this)

- **Accuracy ceiling:** Apple Vision is weak on **Vietnamese** and on **handwriting** (see [[miai-iphone-ocr-server/language-support-and-vietnamese]]). hireui serves Vietnamese candidates. So residency is only a win **if OCR quality clears the bar** for the CV formats hireui actually receives.
- **The pilot is therefore an eval, not an install:** measure Apple Vision `docOCR` field-extraction accuracy on a representative, **consented/synthetic** CV set (typed + scanned + Vietnamese) *before* committing. If it clears the bar for typed CVs but not handwriting, use a **hybrid**: local OCR for typed docs, cloud (or manual) for the rest — the same "redact local, reason cloud" shape recommended in [[local-ai-coding-agents/privacy-data-residency]].
- **Apple platform lock-in:** this path needs Apple hardware (a Mac mini) in the loop — a real ops constraint vs a portable Linux OCR (Tesseract, PaddleOCR, docTR). Weigh residency + zero-cost + quality against portability.

## Key Takeaways

- **The value isn't "free" — it's residency.** On-device OCR = candidate PII never egresses; strongest GDPR/PDPL/EU-AI-Act posture.
- It's the **OCR front-end** the corpus's [[miai-cv-matching-agent/_index]] is missing, and slots behind the [[mosh-ai-powered-apps/_index]] seam.
- **`docOCR` on a Mac mini** (MIT, free) is the deployable shape; iPhone is the demo.
- **Gate it on an eval:** Vietnamese/handwriting accuracy decides whether the residency win is usable. Hybrid local+cloud is the fallback.

→ Concrete pilot steps: `output/(C) 2026-07-14-miai-iphone-ocr-server-pilot-methods.md`.
