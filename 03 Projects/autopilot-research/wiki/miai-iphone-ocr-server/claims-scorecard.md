# Claims scorecard

12 substantive video claims, reconciled across Workflow `wf_d1421e99-019` (6 dives + 5 refute-first verifiers + critic, Haiku 4.5) + ~8 main-loop `gh api`/WebSearch/WebFetch anchors. Verdict rubric per `CLAUDE.md`.

| # | Claim | Verdict | Note |
|---|---|---|---|
| C1 | Apple Intelligence = local on-device model; offline; Writing Tools / Image Playground / Clean Up / Private Cloud Compute / summarization | **CONFIRMED** | Apple newsroom + security.apple.com PCC |
| C2 | Apple's **Foundation Models framework** lets apps add on-device AI in "three lines of code" | **CONFIRMED** | WWDC June 2025; `LanguageModelSession()` ≈ 3 lines; ~3B model, free for devs — *but not what the OCR app uses* |
| C3 | A dev shipped an OCR-server app (GitHub + App Store); port 8000; LAN REST API | **CONFIRMED** | `riddleling/iOS-OCR-Server`, MIT, 1,771★, App Store `id6749533041` |
| C4 | The OCR is done via **Apple Vision Framework** (and the video ties it to "Apple Intelligence") | **MISLEADING** | Mechanism (Vision) is right; **framing that credits Apple Intelligence/Foundation Models is wrong** — README: "solely Vision Framework, no LLM" |
| C5 | App settings: accurate/fast, language correction, auto-detect, port; monitor (CPU/per-core/memory/temp/battery) | **CONFIRMED** | Shown on-screen; maps to Vision `recognitionLevel`/`usesLanguageCorrection`; App Store v1.3.2 adds per-core CPU monitor. *(Main-loop override of agents' UNVERIFIED — see caveats)* |
| C6 | `/upload` returns bounding boxes + coords + text; drawn with OpenCV | **CONFIRMED** | README `ocr_boxes` (x,y,w,h + corners + text); `VNRecognizeTextRequest` |
| C7 | `/docOCR` "paragraph" mode returns structure as **Markdown incl. tables**; faster | **CORRECT-BUT-INCOMPLETE** | Structure/tables/MD real (`RecognizeDocumentsRequest`, iOS 26); **"faster" unquantified**; minor iOS-README vs Mac-tool output-format ambiguity |
| C8 | Invoice OK; prescription OK; **Vietnamese handwriting fails** ("not fine-tuned for Vietnamese") | **CONFIRMED** | Presenter's own demo; consistent with Vision coverage — Vietnamese isn't a supported recognition language; handwriting weak. *(Main-loop override of agents' UNVERIFIED)* |
| C9 | Enable **Guided Access** to lock the device to one app (stability) | **CONFIRMED** | Real iOS Accessibility feature; the app's **own README** recommends it (caveat: disables Emergency Services while active) |
| C10 | Free / no token / no cloud / private — all on-device | **CONFIRMED** | App free (optional $4.99 tip); Vision runs on Neural Engine on-device — a *genuine* "free," unlike revenue-title theater elsewhere in corpus |
| C11 | Same dev's Mac tool "**Doc OCR**"; Mac mini M4 → high-perf server | **CONFIRMED** | `riddleling/docOCR`, MIT, images → Markdown, macOS 26; M4 mini feasible (presenter says untested by him) |
| C14 | **Vietnam AI Innovation Challenge 2026**, 17-18-19 July, 2000+ builders | **CONFIRMED** | Real: July 17-19 2026, Da Nang; NIC + Meta + AI for Vietnam + Duy Tan Univ.; 2,000-3,000 devs |

### Not scored against the presenter

- **C12 — CAPTION GARBLE (corrected).** The transcript credits speed to *"chip A của Google."* The A-series chip + Neural Engine are **Apple's** (designed by Apple, made by TSMC). Almost certainly the presenter said "Apple"/"chip A" and the auto-caption mangled it. A transcript artifact, not a presenter error.
- **C13 — honest hedge, not a claim.** Multi-iPhone OCR "cluster/farm": the README lists it as a use case; the presenter **explicitly says he hasn't tried it** and asks viewers to report back. Correctly framed as speculative.

## Tally

**10 CONFIRMED · 1 CORRECT-BUT-INCOMPLETE · 1 MISLEADING · 0 FALSE · 0 FABRICATED** (+ 1 caption-garble + 1 honest-hedge + 1 provenance nuance).

## Read

A **high-integrity practitioner demo** — the toolchain is entirely real, everything works, "free" is genuinely free, and the presenter volunteers the weak spots himself. It sits alongside [[local-ai-coding-agents/_index]], [[github-copilot-cli-agents/_index]] and [[codesistency-mobile-app-course/_index]] at the honest end of the corpus honesty spectrum, and is the disciplined sibling of [[jasonlee-claude-mobile-app/_index]]. The **only** real ding is the intro conflating Apple Intelligence with the Vision framework that actually does the work ([[miai-iphone-ocr-server/apple-vision-vs-apple-intelligence]]).
