# The app: iOS-OCR-Server (+ the docOCR ecosystem)

The app the video uses, verified by direct `gh api` + App Store + README fetches.

## iOS-OCR-Server ("OCR Server")

- **Repo:** [`github.com/riddleling/iOS-OCR-Server`](https://github.com/riddleling/iOS-OCR-Server) — **MIT**, Swift, **1,771★**, created **2025-08-01**, last push 2026-06-04.
- **App Store:** ["OCR Server", `id6749533041`](https://apps.apple.com/us/app/ocr-server/id6749533041) — **free** (with an optional **$4.99 "Buy me a coffee"** in-app tip). App version ~1.3.x.
- **Description (verbatim):** *"An iOS OCR Server Using Apple's Vision Framework."*
- **What it is:** a **SwiftNIO HTTP server that runs on the iPhone/iPad itself**, binding **port 8000** on all interfaces so any device on the LAN can POST an image and get OCR back. ~500 lines of Swift glue between SwiftNIO and Vision. (Show HN: [news.ycombinator.com/item?id=44879659](https://news.ycombinator.com/item?id=44879659).)
- **Naming nit:** the presenter calls it "iPhone OCR Server"; the actual product name is just **"OCR Server"** (repo `iOS-OCR-Server`). Minor.
- **Not brand-new:** created **Aug 2025** (~11 months before the video). The video is fresh; the app is established.

### Endpoints (from README)

| Endpoint | Returns | Apple API behind it |
|---|---|---|
| `POST /upload` | JSON with `ocr_boxes` — each detected region's `x,y,w,h` + four corner coords + `text` | `VNRecognizeTextRequest` |
| `POST /docOCR` | Document-structure text (paragraphs, lists, **tables**) — the "paragraph" mode | `RecognizeDocumentsRequest` (iOS 26) |

### Settings (shown on-screen in the video; map to documented Vision options)

- **Recognition level: `accurate` vs `fast`** → Vision `VNRequestTextRecognitionLevel.accurate` (slower, ML-based, more languages) / `.fast` (near-instant, Latin-focused).
- **Language correction** → Vision `usesLanguageCorrection`.
- **Auto-detect language** → Vision automatic language detection.
- **Port** (default 8000, editable).
- **Monitor view** — per-core CPU, memory, temperature, battery (App Store v1.3.2 changelog explicitly adds "per-core CPU usage monitoring on the Monitor page"; the fuller set is shown on-screen).
- **Guided Access** — the README *itself* recommends enabling it (see [[miai-iphone-ocr-server/caveats-and-corrections]]).

## docOCR — the Mac sibling (the video's "Doc OCR")

- **Repo:** [`github.com/riddleling/docOCR`](https://github.com/riddleling/docOCR) — **MIT**, Swift, 34★, created **2026-05-26**.
- **Description:** *"macOS CLI and HTTP OCR tool for converting document images to **Markdown**."* Uses `RecognizeDocumentsRequest` (macOS 26). Runs as both a CLI and an HTTP server.
- This is exactly the video's Mac-mini-M4 idea: an Apple-Silicon Mac (M4 mini = 16-core Neural Engine, ~38 TOPS) as a higher-throughput local OCR-to-Markdown server. The presenter says he only tested the iPhone; the Mac tool is real and unverified-by-him but documented.

## The full OCR ecosystem by the same developer

Riddleling has built a **cross-platform OCR tool family** — useful context, and it means this isn't a one-off:

| Repo | Platform | What |
|---|---|---|
| `iOS-OCR-Server` | iOS/iPadOS | the video's app (Vision, HTTP :8000) |
| `docOCR` | macOS | CLI + HTTP, images → Markdown (Vision `RecognizeDocumentsRequest`) |
| `macocr` | macOS 13+ | Rust CLI OCR (Vision), 57★ |
| `winocr` | Windows 10+ | Rust CLI over `Windows.Media.Ocr` |
| `OcrBoard` | Windows | hotkey client that sends screen regions to `macocr`/`iOS-OCR-Server` |
| `dococr-skill` | — | a **Codex skill** wrapping docOCR for local macOS OCR-to-Markdown |

Note `dococr-skill` — an OpenAI **Codex Agent Skill** for driving docOCR, which ties into [[teach-skill-ai-tutor/codex-skills-feature-verified]] and the broader Agent-Skills spec thread.

## Developer

- **Ling, Wei-Cheng (凌偉誠)** — GitHub [`riddleling`](https://github.com/riddleling), based in **Kaohsiung, Taiwan**; bio "🕹️復古電玩愛好者" (retro-gaming enthusiast). Contact `riddle.apple@gmail.com`.
- The presenter jokingly calls him *"pháp sư Trung Hoa" / "anh Trung Quốc"* ("Chinese"). Factually he's **Taiwanese** — a common VN colloquialism, corrected in [[miai-iphone-ocr-server/caveats-and-corrections]].

## Key Takeaways

- The app is real, MIT, free, on the App Store, and **established since Aug 2025** with 1,771★.
- **`/upload` = boxes; `/docOCR` = structured Markdown** — two distinct Vision APIs behind two endpoints.
- The Mac tool `docOCR` (images → Markdown) is real and is the scriptable one for a server build.
- It's part of a **whole cross-platform OCR toolkit** (macOS/Windows/iOS + a Codex skill) by one Taiwanese developer.

Sources: `gh api repos/riddleling/{iOS-OCR-Server,docOCR}` + `users/riddleling`; [README](https://raw.githubusercontent.com/riddleling/iOS-OCR-Server/main/README.md); [App Store](https://apps.apple.com/us/app/ocr-server/id6749533041).
