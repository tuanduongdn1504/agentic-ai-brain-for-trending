# (C) v229 voicebox — Deep Dive

> **Subject:** `jamiepine/voicebox` — "The open-source AI voice studio. Clone, dictate, create." (voicebox.sh)
> **Ship:** v229 · **Date:** 2026-08-08 · **Author of wiki:** Claude (Storm Bear's vault)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **Pattern outcome:** NO NEW MINT — a genuine non-port **N=3** of the palmier-pro v192 §C standalone (see the Verdict doc).
> ⚠️ **Provenance:** NOT source-cloned. Hand-verified from the rendered repo page + raw `README.md` + raw `CHANGELOG.md` + landscape/identity WebSearch + vault collision greps (the v200→v228 self-throttle — the ~205K shim overflows every subagent >200K, so the deep-dive workflow is not run; the load-bearing corpus claims ARE hand-verified). Facts below are page/README/changelog-stated unless marked hand-verified.

---

## 1. One-paragraph what-it-is

**Voicebox** is an **open-source, local-first "AI voice studio"** by **Jamie Pine** (the creator of Spacedrive). It bundles three things a person normally pays two SaaS tools for — **voice cloning + text-to-speech generation** (the ElevenLabs half) and **speech-to-text dictation** (the Wispr Flow half) — into one desktop app that runs **entirely on your own machine, no audio ever leaving it**. It clones a voice from a few seconds of audio (or picks from 50+ presets), speaks in **23 languages across 7 TTS engines**, dictates into any app via a global hotkey with auto-paste, composes multi-track "Stories," and — the corpus-relevant part — ships a **built-in first-party Model Context Protocol (MCP) server** so that **any MCP-aware coding agent (Claude Code, Cursor, Windsurf, Cline, VS Code MCP extensions) can call into your local Voicebox install** to speak (in a voice you cloned), transcribe, and browse captures/profiles.

---

## 2. Identity & provenance (hand-verified)

| Field | Value | Source |
|---|---|---|
| Repo | `jamiepine/voicebox` | repo page |
| Tagline | "The open-source AI voice studio. Clone, dictate, create." | repo desc + `voicebox.sh` |
| Author | **Jamie Pine** (`jamiepine`) — Canadian dev, **Vancouver BC**; creator of **Spacedrive** (a well-known OSS file-explorer) + CEO of Spacedrive Technology Inc.; works with Rust/AI/UI, open-source focus | WebSearch (GitHub profile / X `@jamiepine`) |
| **Anthropic?** | **NO.** Jamie Pine / Spacedrive Technology Inc., not Anthropic. Famous-OSS-author (Spacedrive) is **not** an (a)-rescue (§41). First `jamiepine` / Spacedrive-lineage author in the corpus → **#19 19a**. | hand-reasoned |
| License | **MIT** | README + repo page |
| Stars / forks | **~49.7k★ / ~6.1k forks** page-stated (§37.4 — GitHub API mocked → **NOT a verified #52 claim**; ⚠️ historical snapshots conflict: ~22k late-Apr → ~26.5k → ~27k → ~49.7k now = fast-growing over ~3.5 months, but velocity unestablishable under §37.4) | repo page + press snapshots |
| Latest version | **v0.5.0** (2026-04-22, per the fetched CHANGELOG); earliest **v0.1.0** (2026-01-27); ⚠️ the CHANGELOG may lag the repo — pin `v0.5.0` and treat as untrusted-until-inspected | CHANGELOG |
| Topics | `ai`, `cuda`, `mlx`, `qwen3-tts`, `qwen3-tts-ui`, `voice-ai`, `voice-clone`, `whisper` | repo page |

---

## 3. Architecture / tech stack (README-stated)

- **Desktop shell:** **Tauri (Rust)** → joins the corpus's Tauri-desktop cluster (cc-switch v73 / CodexPlusPlus v117 / OpenHuman v118 / PilotDeck v175 / meetily v196 / tabularis v212 = LV-C7).
- **Frontend:** React + TypeScript + Tailwind CSS; **Zustand** state.
- **Backend:** **FastAPI (Python)**.
- **Database:** SQLite.
- **Inference:** **MLX** (Apple Silicon) / **PyTorch** (CUDA / ROCm / XPU / CPU / DirectML).
- **Audio effects:** **Pedalboard** (pitch shift, reverb, delay, chorus, compression, filters).
- **Platforms:** macOS (Apple Silicon via MLX, Intel via PyTorch), Windows (CUDA / DirectML), Linux (CUDA / ROCm / CPU), + Docker Compose. DMG/MSI installers.
- **Install (dev):** `git clone` → `just setup` (creates a Python venv, installs deps) → `just dev` (backend + app). Prereqs: Bun, Rust, Python 3.11+, Tauri deps, Xcode on macOS.

### The AI substrate — all UPSTREAM models it orchestrates (load-bearing for (c))

- **7 TTS engines:** Qwen3-TTS, Qwen CustomVoice (10 langs, delivery control), LuxTTS (lightweight, 48 kHz), Chatterbox Multilingual (23 langs) + Chatterbox Turbo (paralinguistic tags), TADA/HumeAI (long-form coherent), Kokoro (82M model, 50 preset voices).
- **STT:** **OpenAI Whisper** (Base → Turbo tiers), running **locally** via MLX or PyTorch.
- **Local LLM:** **Qwen3 (0.6B / 1.7B / 4B)** bundled locally — backs **dictation refinement, voice-personality rewriting, and the `Compose` feature** ("one LLM in the app, one model cache, one GPU-memory footprint"). ⚠️ **This is NOT Claude** — a local Alibaba Qwen model. Claude appears only as an MCP *client* (below).

**The honest (c) caveat:** the hard AI is **all third-party** (Qwen3-TTS = Alibaba; Whisper = OpenAI; Kokoro / Chatterbox / TADA-HumeAI; Qwen3 LLM = Alibaba). Voicebox is the **integration / orchestration / desktop-UI / MCP-server layer** over those models — not novel model research. That layer is genuinely substantial (7-engine abstraction, multi-backend inference routing, a stories multi-track editor, Pedalboard effects, a global-hotkey dictation pipeline with auto-paste, an MCP server + stdio shim, cross-platform packaging) — but the "voice quality" is upstream.

---

## 4. The MCP server — the corpus-relevant core (README + CHANGELOG, verbatim where quoted)

Introduced in **v0.5.0** ("Voicebox ships a built-in **Model Context Protocol** server at `http://127.0.0.1:17493/mcp`"), it:

- Mounts a **FastMCP** server at **`/mcp`** with **HTTP + stdio transports**; stdio-only clients point at the bundled **`voicebox-mcp`** binary (the stdio shim).
- Exposes **4 tools:** `voicebox.speak`, `voicebox.transcribe`, `voicebox.list_captures`, `voicebox.list_profiles`.
- README: *"any MCP-aware agent (Claude Code, Cursor, Windsurf, Cline, VS Code MCP extensions) can speak, transcribe, and browse captures and profiles"* — in *"a voice you've cloned."* CHANGELOG: *"…any MCP-aware agent — can call into your local Voicebox install."*
- Agents can invoke voice output **with optional personality rewriting** (routed through the local Qwen3 LLM).

**Why this matters:** voicebox's *primary function* is a **human-usable voice studio** you drive yourself (clone/dictate/create — the ElevenLabs + Wispr Flow alternative). The MCP server is a **secondary access path** that exposes that studio TO a coding agent → **product-first**, exactly the shape of **palmier-pro v192** (a human video editor + a first-party MCP server) and **tabularis v212** (a human SQL GUI + a first-party MCP server). See the Verdict doc for the N=3 finding.

---

## 5. Privacy & the ethics gap (load-bearing for the fence)

- **Privacy (README):** *"Complete privacy — models, voice data, and captures never leave your machine."* Every dictation / recording / uploaded file lands in a **Captures** tab (original audio + transcript, preserved). Local-first is a genuine positive for the *user's own* data.
- **⚠️ Consent / deepfake gap (hand-verified):** the README contains **no explicit consent language or ethics note** (both raw-README fetches confirm this). Press: *"Voicebox Clones Any Voice From 3 Seconds of Audio, Runs Locally for Free, and Has No Consent Lock"* (techtimes, 2026-05-19). Cloning an arbitrary person's voice from a few seconds of audio, with no consent gate, is a real **impersonation / voice-fraud / deepfake** misuse surface — a #66 DUAL-USE note that governs any pilot (see the Pilot Methods Menu).

---

## 6. Roadmap (README-stated)

Windows/Linux auto-paste parity; STT expansion (Parakeet v3, Qwen3-ASR); streaming transcription; end-to-end speech LLMs; voice design from text; mobile companion apps.

---

## 7. Corpus connectedness (the (d) map)

- **The product-first-MCP-retrofit §C standalone (palmier-pro v192):** N=1 palmier-pro (video editor) → N=2 tabularis v212 (SQL GUI) → **N=3 voicebox (voice studio)** = the genuinely-independent, cross-author, cross-domain, NON-PORT 3rd instance the v212 audit was explicitly waiting for. **← headline; see Verdict.**
- **First-party-MCP-server-for-coding-agents cluster:** google_workspace_mcp v140 / palmier-pro v192 / tabularis v212 / OfficeCLI v206 / firecrawl v214 (the agent-tool-first ones) — voicebox is on the *product-first* side.
- **Speech/voice cluster:** **fish-speech v20** (TTS *model* — the TTS precedent) · **meetily v196** (privacy-first, on-device **Whisper/Parakeet STT**, Tauri desktop, "no cloud" — the **closest sibling**) · **video-use v198** (ElevenLabs-Scribe transcript editing — voicebox is the *local OSS alternative to ElevenLabs*) · **AIRI v210** (AI companion *with a voice* — voicebox *gives an agent a voice*). → voicebox = the corpus's ~**5th speech-domain subject** and **FIRST voice-cloning / TTS-voice-studio** subject.
- **Local-first / data-residency thread:** meetily v196 / OpenHuman v118 / local-AI-coding-agents / the "redact local, reason cloud" candidate-LLM-legibility ADR.
- **Tauri-desktop LV-C7 cluster** + **local-LLM thread** (Qwen3 local; DeepSeek-TUI v72 / GLM-5 v176).
- **#18 B1-MCP** (one FastMCP server, 4+ named clients) · **#84 84c** (cross-harness MCP clients; NO N-bump) · **#66** DUAL-USE (the consent gap).
- **Spacedrive** cross-ref (Jamie Pine's flagship; Rust/Tauri lineage; first corpus subject from this author).

---

## 8. Non-claims (kept honest)

- **NOT #52** (49.7k★ page-stated §37.4 + conflicting historical snapshots → velocity unestablishable).
- **NOT #57** (orchestrates Qwen3-TTS/Whisper/Kokoro/Chatterbox/HumeAI-TADA/Qwen3 + names Claude Code/Cursor/Windsurf/Cline as MCP clients + compares to ElevenLabs/Wispr Flow — none are corpus subjects; mentions/deps ≠ recursion).
- **NOT world-first** — voice cloning / TTS / dictation are saturated categories (ElevenLabs, Wispr Flow, countless TTS tools); voicebox = the **local-first OSS all-in-one** flavor, NOT a world-first.
- **NOT the first model-subject** (fish-speech v20 precedes; voicebox *orchestrates* models, builds none).
- **NOT a new top-level pattern** (max stays #85).
- **NOT source-cloned** (flagged).
