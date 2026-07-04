# (C) meetily — Deep Dive

*v196 wiki ship · 2026-07-04 · source-verified at commit `0281737` (the v0.4.0 merge, 2026-06-05) · this file is Claude-authored (`(C)` prefix per vault rule)*

> `Zackriya-Solutions/meetily` — **"Privacy-First AI Meeting Assistant."** A self-contained **Tauri 2.x desktop app** (Rust core + Next.js/React UI) that captures mic + system audio, transcribes it **locally** (Whisper.cpp / whisper-rs **or** NVIDIA Parakeet), and summarizes it with **your choice of LLM** (Ollama local / Claude / Groq / OpenRouter / any OpenAI-compatible endpoint) — **entirely on your machine, no cloud, no meeting bot**. MIT (Community Edition) + a commercial PRO tier. Author = **Zackriya Solutions**, an AI-automation consultancy in Bengaluru, India (+ Atlanta) — **not Anthropic**.

---

## 1. What it is, in one paragraph

Most meeting-AI tools (Otter, Fireflies, Fathom, Zoom AI Companion, tl;dv, Read.ai) work by sending a **bot** into your call and uploading everything to **their** cloud. Meetily refuses both moves. It runs as a native desktop app, records the audio your machine already hears (microphone **and** system output, mixed), runs speech-to-text **on-device**, and only ever touches a network if *you* point the summary step at a cloud LLM (and even that is optional — Ollama runs the summary locally too). The pitch is **data sovereignty**: "your sensitive discussions shouldn't live on servers you don't control." For a Scrum coach recording standups/retros, or a recruiter taking interview notes, that's the whole value proposition.

The interesting part for *this* vault isn't the meeting-notetaker domain — it's the **engineering underneath**: a clean, source-verified, **provider-agnostic LLM-client** and a **map-reduce summarization engine** that are a near-perfect blueprint for hireui's first LLM feature.

---

## 2. Identity, license, maturity (hand-verified)

| Fact | Value | How verified |
|---|---|---|
| Repo | `github.com/Zackriya-Solutions/meetily` (canonical) | `git remote get-url origin` |
| Author | **Zackriya Solutions** — AI-automation agency, Bengaluru IN + Atlanta US | web + org page; **NOT Anthropic** |
| License | **MIT** (Community Edition); commercial **PRO** (~$10/user/mo) + Enterprise | `LICENSE.md` = MIT; README PRO section |
| Version | **v0.4.0** (2026-06-05) | `package.json` + tag `v0.4.0` |
| History | **556 commits**, first commit **2024-12-26**, ~18 months | `git rev-list --count HEAD` + `git log --reverse` |
| Tags | 12: v0.0.1 (2025-02) → v0.2.0 (2025-12) → v0.3.0 (2026-03) → v0.4.0 (2026-06) | `git log` per tag |
| Languages | Rust ~46% · TypeScript ~30% · C++ ~10% | GitHub page-stated |
| Stars | **~9.5k–14k across sources** (page-stated, §37.4 — **NOT** API-verified) | Trendshift #21958; unverified |

> ⚠️ **One research agent claimed "50 commits / 3 months old."** Wrong — it mistook the recent v0.3.0→v0.4.0 window for the whole project. Hand-verified: **556 commits since Dec 2024**. A second agent's star counts disagreed (9.5k / 12.9k / 14.2k) — all page-stated, so **no Pattern #52 velocity claim**.

> ⚠️ **Repo-rename artifact.** The README badges, the Releases links, **and the Tauri auto-updater endpoint** all still point at the OLD org path `Zackriya-Solutions/meeting-minutes`. The canonical repo is `meetily` (verified via `git remote`). This is a real staleness note (see §7), not two repos.

---

## 3. Architecture (source-read, ~325 files)

Meetily is a single Tauri binary. Rust owns everything heavy; Next.js is the UI shell talking to it over Tauri commands.

```
┌──────────────────────────── Tauri desktop app ────────────────────────────┐
│  Next.js 14 / React 18 UI  ──(Tauri commands, ~100+)──▶  Rust core          │
│                                                                             │
│   Rust core (frontend/src-tauri/src, 147 .rs files):                        │
│   ├─ audio/         two-path pipeline: RECORD (RMS-ducked mix) ‖ VAD→STT     │
│   │   └─ devices/platform/{windows WASAPI, macos ScreenCaptureKit, linux}   │
│   ├─ audio_v2/      modern rewrite — SCAFFOLDING ONLY (not wired in yet)     │
│   ├─ whisper_engine / parakeet_engine   pluggable STT (a trait)             │
│   ├─ summary/       the LLM subsystem (the pilot gold — §4)                  │
│   ├─ anthropic/ groq/ ollama/ openrouter/ openai/   per-provider bits       │
│   ├─ database/      SQLite via sqlx, 5 repositories                         │
│   ├─ api/           in-app command surface (no separate server)             │
│   └─ analytics/     PostHog, opt-in default-OFF (§7)                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Audio (the crown jewel, but off-topic for us).** One raw mic+system stream fans into **two consumers**: a *recording* path (professional mixing — RMS-based ducking, clipping prevention, EBU R128 loudness) and a *transcription* path (Voice-Activity-Detection filters silence, sends only speech to the STT engine). Platform-specific capture: WASAPI (Windows), ScreenCaptureKit + CoreAudio (macOS), ALSA (Linux). There's a 235-line `BLUETOOTH_PLAYBACK_NOTICE.md` documenting a real macOS 48kHz↔Bluetooth-resampling bug (device-by-device table) — a signal of genuine engineering depth, not a toy.

**Transcription is pluggable.** A `TranscriptionProvider` trait (`transcribe(audio, language) → {text, confidence, is_partial}`) with two implementations: **Whisper** (via a `Zackriya-Solutions/whisper.cpp` fork, a git submodule) and **NVIDIA Parakeet** (the community `istupakov` ONNX build, via the `ort` ONNX-Runtime crate). Parakeet is the fast path (README: "4× faster than Whisper Large-V3" — page-stated, unbenchmarked here); Whisper is the accuracy path.

**Honest structural caveats:** `audio_v2/` is a **rewrite that isn't wired in** (`ModernAudioSystem` with TODO stubs, marked "Phase 2") — dead-ish scaffolding sitting beside the active `audio/`. There's a **stale `"main": "electron/main.js"`** field in `package.json` — a fossil from a pre-Tauri Electron era, non-functional now. Audio-layer Rust **test coverage is essentially absent** (some tests exist in `summary/` and `analytics/`).

---

## 4. The pilot gold: the LLM subsystem (`summary/`)

This is why the wiki is worth building for *this* operator. Two files carry it.

### 4a. `llm_client.rs` — the provider-agnostic dispatcher (346 lines)

One function, `generate_summary(...)`, fans out to **7 providers** (`OpenAI`, `Claude`, `Groq`, `Ollama`, `OpenRouter`, `BuiltInAI` local sidecar, `CustomOpenAI`) via a single `match`. The elegant part:

- **6 of 7 providers share ONE OpenAI-chat-completions code path** — same `ChatRequest {model, messages, max_tokens?, temperature?, top_p?}`, same `ChatResponse.choices[0].message.content`, only the URL + auth header differ (`Authorization: Bearer …`). Ollama, Groq, OpenRouter, OpenAI, CustomOpenAI all ride it.
- **Claude gets its own shape** because its API genuinely differs: `x-api-key` + `anthropic-version: 2023-06-01` header, a `ClaudeRequest {system, model, max_tokens, messages}` body posted to `/v1/messages`, and a `ClaudeChatResponse.content[0].text` parse. This is the correct "abstract the 90% shared, special-case the 10% that's really different" discipline.
- **`BuiltInAI` bails out early** to a **local llama sidecar** (`summary_engine/`) — no HTTP at all, a spawned process with a JSON `Generate` request.
- Cancellation is first-class: `tokio::select!` races the request against a `CancellationToken`.

> **Two doc-vs-code nuances I caught (both minor, both real):** (1) the request timeout is `Duration::from_secs(300)` but the timeout **error string still says "60 seconds"** (`llm_client.rs:8` vs `:272`/`:285`) — stale copy. (2) For Claude, `max_tokens` is **hardcoded to 2048** (`:248`) while the OpenAI-path providers pass `max_tokens` through only for `CustomOpenAI` (else `None`). So Claude summaries are capped at 2048 output tokens regardless of transcript size. Worth knowing before you trust it on a 2-hour meeting.

The `anthropic/anthropic.rs` module (4.9K) is **NOT** duplicate generation logic — it only **lists available Claude models**. Generation lives solely in `llm_client.rs`. Clean separation: one module dispatches the protocol, one fetches capabilities.

### 4b. `processor.rs` + `service.rs` — the summarization engine (856 + 979 lines)

- **Chunking is conditional on provider + length.** Cloud providers (or transcripts under a ~4000-token threshold) get a **single pass**. Ollama / BuiltInAI (local, smaller context) get a **multi-level map-reduce**: Pass 1 summarizes each chunk independently ("You are an expert meeting summarizer"), Pass 2 synthesizes the chunk-summaries, Pass 3 fills the template section-by-section.
- **Chunk sizing is disciplined:** `chunk_text(text, token_threshold − 300, 100)` — reserve 300 tokens for prompt overhead, keep a **100-token overlap** between chunks so context isn't cut mid-thought. Token estimate is a cheap `char_count × 0.35`.
- **Dynamic per-provider token budgeting** (`service.rs`): Ollama fetches the model's real `context_size` from `/api/show` (with cached-aside + TTL, fallback 4096/8192); cloud providers get "effectively unlimited"; BuiltInAI reads a model registry.
- **English-summary cache reuse** (`language_detection.rs` via `whatlang`, 23 languages): if you switch the output language, it reuses the cached English summary and just **translates** rather than re-summarizing from scratch. There's also an **FNV-1a content fingerprint** cache so an unchanged transcript isn't re-summarized (the same idea as openwiki v195's content-snapshot no-op guard you just studied).

### 4c. Templates are declarative JSON

A meeting template is just JSON: `{name, description, sections: [{title, instruction, format, item_format?}]}`. Two are compiled into the binary (`daily_standup`, `standard_meeting`); more ship as files (`retrospective`, `project_sync`, `psychatric_session`). `standard_meeting.json`'s Action-Items section even specifies a markdown table with **transcript-segment references + timestamps**. Adding a new summary format = adding a JSON file, no code change. **This is the same "skill/template as data, not code" idea the vault runs** — and directly reusable for hireui report formats.

---

## 5. Feature boundary — free vs PRO (README-stated)

**Community Edition (MIT, free forever):** local Whisper + Parakeet transcription · simultaneous mic+system mixing · import & re-transcribe existing audio (beta) · multi-provider summaries incl. custom OpenAI-compatible endpoint · GPU acceleration (Metal/CoreML/CUDA/Vulkan/OpenBLAS/hipBLAS, auto-detected at build) · multi-language transcription · meeting templates · BlockNote rich-text notes · SQLite local storage. **macOS + Windows prebuilt; Linux build-from-source.**

**PRO ($10/user/mo, "a different codebase"):** enhanced-accuracy transcription models · custom summary templates · advanced exports (PDF/DOCX/Markdown) · auto-detect-and-join meetings · **speaker diarization** (planned) · chat-with-meetings (coming) · calendar integration (coming) · self-hosted team deployment · GDPR audit trails · priority support.

> Note the README's PRO roadmap says "diarization mid-June" and elsewhere "June 2025" — the dates are inconsistent (v0.4.0 itself is dated June **2026**). Treat PRO roadmap dates as soft.

---

## 6. Upstream credits (all non-corpus)

- **Whisper.cpp** (ggml-org/ggerganov, MIT) — the C/C++ Whisper implementation; meetily forks it.
- **whisper-rs** (tazz4843, Unlicense) — Rust bindings + VAD + DTW token timestamps.
- **NVIDIA Parakeet TDT 0.6B v3** (multilingual ASR) + the **istupakov** ONNX conversion on HuggingFace (community, not NVIDIA-official).
- **Screenpipe** (mediar-ai) — meetily "borrowed some code" for audio capture.
- **transcribe-rs**, **Tauri 2.6.2**, **BlockNote 0.36**, **cpal**, **ebur128**, **nnnoiseless** (RNNoise), **symphonia**.

None are corpus subjects → this is **not** a Pattern #57 (corpus-recursive) case.

---

## 7. Security / supply-chain / privacy — blunt read (BENIGN-to-MODERATE)

- **Distribution: code-signed + notarized** macOS (Developer ID + hardened runtime) and Windows (signed). Shipped via GitHub releases. **No published SHA-256 checksum** → verify via Gatekeeper signature, not a hash.
- **Auto-updater** points at `…/meeting-minutes/releases/latest/download/latest.json` (the OLD repo name), checks on every launch, with an embedded public key. The stale repo path is a **redirect/staleness risk** to note, not a proven vuln.
- **Analytics — I corrected the workflow's overclaim.** A research agent flagged "**CRITICAL: analytics on by default**" because `analytics/commands.rs:14` hardcodes `enabled: true`. That reading is **wrong**: `init_analytics()` is **only called** by the frontend (`AnalyticsProvider.tsx:57`) when the opt-in store value `analyticsOptedIn` is `true`, and that value **defaults to `false`** with an explicit forced-off migration key (`:41-53`). So **"off by default" is accurate** — the Rust `enabled:true` just means "once you've opted in and this command runs, the client is on." What *is* real: the **PostHog project write-key is exposed in the public repo** (`:12`) — low-risk (client SDK write-keys are meant to be public and can't read data back), but worth flagging; and even when enabled, meeting titles / file paths / device names are **stripped** before send (a `SENSITIVE_ANALYTICS_KEYS` sanitizer, with unit tests).
- **API-key storage:** Claude/OpenAI keys go through the Tauri settings store, not plaintext in source.
- **Legacy FastAPI backend** (`backend/`) is **archived + unsupported** (README + CLAUDE.md say so explicitly); its old unauthenticated dev CORS is obsolete context, not a shipped surface.
- **macOS permissions** (mic + screen-capture entitlements) are correctly declared.
- **Net:** genuinely privacy-respecting for a consumer app. The only network calls are: (1) the opt-in PostHog analytics (default off), (2) whatever BYO-key cloud LLM *you* pick for summaries, (3) the updater, (4) model downloads. Transcription + audio never leave the device.

---

## 8. Landscape — is meetily the leader?

No single winner in open-source local-first meeting assistants:

- **meetily** — leads on **Windows parity + zero-setup + bot-free capture + MIT**. No CLI/API/**MCP** (a real limitation for agent integration).
- **Hyprnote / Anarlog** (`fastrepl/anarlog`, ~8.8k★, MIT) — leads on **developer integration**: ships a **CLI + REST API + MCP server**, calendar sync, cross-meeting search. macOS/Linux (Windows on roadmap). **If you wanted to wire a meeting assistant into a Claude Code loop, this — not meetily — is the one**, because it exposes MCP.
- **Screenpipe** (mediar-ai, YC, ~7k★, **SSPL** — not truly OSS for commercial use) — 24/7 continuous capture, broader than meetings.
- **Cloud commercial** (Otter/Fireflies/Fathom/tl;dv/Read.ai/Granola) — dominate on convenience, lose on privacy (bot joins + cloud upload).

meetily's differentiators are **real** (Windows + simplicity + genuine local-first + MIT), but it is a *product in a crowded consumer category*, not a category-defining agent tool.

---

## 9. Corpus placement (why it earns a wiki but not a §C mint)

meetily is the corpus's **FIRST AI-meeting-assistant subject** and its **2nd speech-domain subject** (after **fish-speech v20**, which was TTS — meetily is the STT/transcription mirror). Collision grep across `_state/` + `_patterns/` + `03 Projects/` is **clean** (no prior meeting/notetaker/transcription/Whisper-app/Zackriya subject).

But **corpus-first-for-a-DOMAIN ≠ a mintable §C capability class.** This is exactly the **TimesFM v193 / GLM-5 v176 / DeepSpec v186** situation: a single off-domain, goal-*adjacent* subject enters the corpus as a **knowledge data-point + a deferred watch axis**, not a new §C standalone (§C vocab is agent-*capability*-shaped; a consumer meeting-notetaker is an end-user-app vertical). The verdict, tier, and pattern outcome are in the companion **(C) meetily — Verdict.md**. The applied-pilot menu (24 methods) is in **(C) meetily — Pilot Methods Menu.md** — that's the part you asked for.
