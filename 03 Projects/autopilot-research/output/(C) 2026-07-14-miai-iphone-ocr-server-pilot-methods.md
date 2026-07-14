# (C) hireui pilot methods — on-device Apple Vision OCR (miai-iphone-ocr-server)

**Source topic:** [[miai-iphone-ocr-server/_index]] · **Date:** 2026-07-14 · **Status:** proposed, NOT committed (awaiting operator)

**Thesis:** OCR is the front door of hireui's CV/document ingestion. Apple's **on-device Vision OCR** (`riddleling/docOCR` on a Mac, or `iOS-OCR-Server` on a phone) can transcribe candidate documents **without any PII leaving hardware you control** — the strongest data-residency posture (mirror of [[local-ai-coding-agents/privacy-data-residency]]). The catch is accuracy on **Vietnamese + handwriting**. So the pilot is an **eval gated ahead of an install**, not a rollout.

Tags: 🔒 residency · 💰 cost · 🧪 eval · 🚢 ship · 🧩 architecture. All hireui work follows the repo CONSTITUTION (I-2 `agent-*` branches, I-8 operator-only skills, GitNexus-first) — see [[external|Storm Bear: hireui pilot target]].

---

## Tier A — this-week, zero-cost, decision-driving

- **A1 🔒🧪 OCR accuracy eval on a representative CV set (the gate).** Assemble a **sanitized/synthetic** set (~30–50 docs): typed CVs, scanned CVs, Vietnamese + English, a couple of handwriting samples. Run each through `docOCR` (Mac, HTTP `/docOCR` → Markdown) and score field-extraction accuracy (name / email / phone / dates / skills). **Decision output:** does typed-CV accuracy clear the bar? Where does it fail (Vietnamese diacritics? handwriting?). This single number decides everything below. Eval-first per [[prompt-evaluation/_index]] + [[ai-engineering/_index]].
- **A2 🔒🧩 Write the residency ADR.** "Candidate document images are OCR'd on-device (local Vision), only extracted/redacted text egresses." Capture the GDPR/PDPL/EU-AI-Act argument (high-risk employment use — see [[miai-cv-matching-agent/_index]] regulatory article) and the Apple-hardware lock-in trade-off vs portable OSS OCR (Tesseract/PaddleOCR/docTR). Cheap, high-leverage, reusable.
- **A3 💰 Cost sanity note.** On-device OCR = **$0/page** vs cloud OCR per-page fees; fold into the [[claude-api-cost-optimization/_index]] tiering picture (OCR is the pre-LLM step, not the LLM cost).

## Tier B — behind the vendor seam (if A1 clears the bar)

- **B1 🧩 OCR as a swappable microservice behind the [[mosh-ai-powered-apps/_index]] A2 seam.** `scan → OCR provider → structured text → LLM Match-Explain`. Implement the provider interface once; back it with `docOCR` (local) first, keep cloud OCR as an alternate impl. Makes local-vs-cloud a one-line switch, not a rewrite.
- **B2 🔒 Redact-before-egress step.** After local OCR, strip/mask PII (national ID, DOB, photo) *before* any text reaches a cloud LLM — the "redact local, reason cloud" hybrid from [[local-ai-coding-agents/privacy-data-residency]]. This is the shape that makes residency real even when the reasoning model is cloud Claude.
- **B3 🧪 Feed OCR output into the Match-Explain eval harness.** Use the [[miai-cv-matching-agent/_index]] matching feature as the downstream consumer; measure end-to-end (OCR error → match-quality) so OCR accuracy is judged by its effect on the actual product output, not in isolation.

## Tier C — hybrid / fallback (if A1 shows gaps)

- **C1 🧩 Hybrid routing.** Typed docs → local Vision OCR; handwriting/low-confidence → cloud OCR or manual review. Route on a confidence threshold; log which path each doc took (auditable).
- **C2 🧪 Bake-off datapoint** vs a portable OSS OCR (PaddleOCR/docTR) on the *same* A1 set — decides whether Apple-hardware lock-in is worth it over a Linux-portable stack that runs on the existing [[fullstack-docker-cicd/_index]] deploy substrate.

## Tier D — deployment shape (only if B clears)

- **D1 🚢 A Mac mini M4 as an internal OCR node** running `docOCR` HTTP, on the LAN, behind the app's backend — the video's own idea, made production. Weigh against the residency ADR (A2): a Mac in the deploy path vs a container in [[fullstack-docker-cicd/_index]].

---

## Skip-list (explicitly do NOT do)

- ❌ **Don't put an iPhone in production.** The phone is the demo; `docOCR` on a Mac is the deployable shape.
- ❌ **Don't rely on it for Vietnamese handwriting** — verified weak ([[miai-iphone-ocr-server/language-support-and-vietnamese]]).
- ❌ **Don't assume "Apple Intelligence" adds understanding** — this is transcription (Vision), not comprehension ([[miai-iphone-ocr-server/apple-vision-vs-apple-intelligence]]); the LLM step is separate.
- ❌ **Don't OCR real candidate PII during the spike** — synthetic/consented data only, per the [[api-security-7-techniques/hireui-security-posture]] posture.

## Headline recommendation

**A1 (accuracy eval) → A2 (residency ADR) this week.** Everything else is gated on A1's number. If typed-CV extraction clears the bar, proceed to B1/B2 (seam + redact); if not, C1 hybrid. The prize is **residency**, and it's only real if accuracy is adequate — so measure before you build.
