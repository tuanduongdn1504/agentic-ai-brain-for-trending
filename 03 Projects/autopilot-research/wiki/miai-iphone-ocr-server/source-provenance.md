# Source provenance & methodology

## The video

- **Title:** "Hô biến iPhone thành local OCR server giá 0 đồng" (Turn an iPhone into a free local OCR server)
- **URL:** https://www.youtube.com/watch?v=NvPoE9cNJVg (`NvPoE9cNJVg`)
- **Channel:** Mì AI · **Uploaded:** 2026-07-14 (same day as ingest) · **Duration:** 19:26 · **Views at ingest:** 373 · **Language:** Vietnamese

## Channel / presenter

- **Mì AI = Nguyễn Chiến Thắng** — Vietnamese banker-educator; Director of the IT Development Center, Saigon Hanoi Bank; Mì AI community ~60K; GitHub [`thangnch`](https://github.com/thangnch). Same channel/person verified in [[miai-cv-matching-agent/_index]] (2026-07-05). ([miai.vn/nguyen-chien-thang-mi-ai](https://www.miai.vn/nguyen-chien-thang-mi-ai/))

## The app author (subject)

- **Ling, Wei-Cheng (凌偉誠)** — GitHub [`riddleling`](https://github.com/riddleling), Kaohsiung, Taiwan; `riddle.apple@gmail.com`.
- Apps: [`iOS-OCR-Server`](https://github.com/riddleling/iOS-OCR-Server) (MIT, 1,771★, 2025-08-01) · [`docOCR`](https://github.com/riddleling/docOCR) (MIT, 2026-05-26) · `macocr` · `winocr` · `OcrBoard` · `dococr-skill`. App Store: ["OCR Server" `id6749533041`](https://apps.apple.com/us/app/ocr-server/id6749533041).

## Event mentioned

- **Vietnam AI Innovation Challenge 2026** — July 17-19, 2026, Da Nang; organized by National Innovation Center (NIC) + Meta + AI for Vietnam + Duy Tan University; 2,000-3,000 developers; launched 2026-05-28. ([vir.com.vn](https://vir.com.vn/nic-launches-vietnams-first-nationwide-ai-hackathon-153742.html) · [vietnamnet.vn](https://vietnamnet.vn/en/vietnam-launches-first-national-ai-native-hackathon-2520844.html))

## Apple first-party sources

- Vision: [VNRecognizeTextRequest](https://developer.apple.com/documentation/vision/vnrecognizetextrequest) · [recognitionLevel](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/recognitionlevel) · [supportedRecognitionLanguages](https://developer.apple.com/documentation/vision/vnrecognizetextrequest/supportedrecognitionlanguages(for:revision:)) · [RecognizeDocumentsRequest](https://developer.apple.com/documentation/vision/recognizedocumentsrequest) · [DocumentObservation](https://developer.apple.com/documentation/vision/documentobservation) · [recognize-tables](https://developer.apple.com/documentation/Vision/recognize-tables-within-a-document) · [WWDC25 s.272 "Read documents…"](https://developer.apple.com/videos/play/wwdc2025/272/)
- Foundation Models / Apple Intelligence: [FoundationModels](https://developer.apple.com/documentation/FoundationModels) · [WWDC25 s.286](https://developer.apple.com/videos/play/wwdc2025/286/) · [apple.com/newsroom Apple Intelligence](https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/) · [Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/)
- Guided Access: [support.apple.com/111795](https://support.apple.com/en-us/111795)

## Methodology

- **Path 5 yt-dlp-only.** VN `vi` auto-captions → `python3.12` VTT dedupe → ~3.7K-word transcript, **read in full in the main loop**. Broken `python3` shim → brew `python3.12` (per project CLAUDE.md). No NotebookLM.
- **Verification:** Workflow **`wf_d1421e99-019`** — 12 agents (6 cluster dives + 5 refute-first verifiers + 1 completeness critic), pipeline (dive→refute per cluster) + barrier critic, ~566K tokens, 223 tool calls, **0 errors**, 1 empty (`app-repo` first stage didn't emit — fully covered by main-loop anchors). All agents on **Haiku 4.5**.
- **Main-loop anchors (~8):** `gh api repos/riddleling/{iOS-OCR-Server,docOCR}` + `users/riddleling`; WebFetch of the iOS-OCR-Server README; WebSearch for the app, `RecognizeDocumentsRequest`, Foundation Models "three lines," Vietnamese Vision support. These grounded the app identity, developer nationality, license/stars/dates, the Vision-vs-Apple-Intelligence distinction, and drove the two Rule-12 overrides (C5, C8) documented in [[miai-iphone-ocr-server/caveats-and-corrections]].
- **Scope:** wrote only inside `03 Projects/autopilot-research/` (Storm Bear scope clamp).

## Corpus cross-references

[[miai-cv-matching-agent/_index]] (same channel; CV-parsing domain) · [[local-ai-coding-agents/privacy-data-residency]] (residency pole) · [[jasonlee-claude-mobile-app/receipt-scanning-with-claude-vision]] (cloud-vision sibling) · [[google-ai-studio-github-import/pricing-privacy-data]] (residency spectrum) · [[mosh-ai-powered-apps/_index]] (vendor seam) · [[api-security-7-techniques/hireui-security-posture]] (PII posture) · [[teach-skill-ai-tutor/codex-skills-feature-verified]] (the `dococr-skill` Codex skill).
