# MoneyPrinterTurbo — Wiki (v123)

> `harry0703/MoneyPrinterTurbo` · **"利用AI大模型，一键生成高清短视频 / Generate short videos with one click using AI LLM."** · A faceless short-video generator: give it a topic/keyword and it auto-produces the script (via one of 13 LLM providers), pulls royalty-free stock footage, generates voiceover + subtitles + background music, and composites a 1080p TikTok/Shorts video — exposed as both a Streamlit WebUI and a FastAPI service.

**(C) Claude-generated wiki page.** Fetched 2026-05-30 (GitHub API + README + README-en + owner profile + root-contents listing). Routine v2.4, wiki #123. **⚠️ WEAK INCLUDE 1/4 — the include rests entirely on (a) cultural-peer; (b) goal-relevance FAILs (this is a faceless-video tool, not a software-dev/agent subject). Corpus-knowledge of a popular cultural-peer subject, NOT goal-#1 progress. See the verdict doc in `01 Analysis/`.**

---

## Identity

| Field | Value |
|---|---|
| Repo | [`harry0703/MoneyPrinterTurbo`](https://github.com/harry0703/MoneyPrinterTurbo) |
| What | **Self-hostable AI faceless short-video generator** (topic → script → footage → voiceover → subtitles → BGM → composite) |
| Tier / archetype | **T5 Application** — NEW sub-archetype candidate **"AI Media-Generation Pipeline App (faceless short-video)"** PROVISIONAL N=1 (corpus-first in-scope standalone AI-video app) |
| Stars / forks | **70,294★ / 10,136 forks** (fork_ratio **0.144**) — mega-scale |
| Watchers / open issues | 463 subscribers / 17 open |
| Created / pushed | 2024-03-11 / 2026-05-30 (**~810 days** old at fetch) |
| Velocity | **~86.8 stars/day → Pattern #52 SUSTAINED-MODERATE-HIGH** (25–150/d), sustained over 810 days; mega-cumulative (70K★) at a moderate daily rate — near the LONG-SUSTAINED-MEDIUM boundary |
| License | **MIT** (GitHub API agrees; clean single license) |
| Language | **Python 97.9%** (~533 MB repo) |
| Stack | **Streamlit** (WebUI) + **FastAPI** (API, OpenAPI/Redoc) + **MoviePy** (compositing) + ffmpeg + ImageMagick + transformers/Whisper (subtitles); MVC |
| Distribution | `webui.sh` / `webui.bat`; **Docker / docker-compose** (CPU + GPU variants); `config.example.toml` |
| Default branch | `main` |
| Author | **harry0703** (`owner.type: User`) — solo indie dev, inferred **China-Mainland / Chinese-heritage** (Chinese-primary README; Chinese project descriptions; 1.5k followers, 7 repos, Pro). Also authors AudioNotes (audio/video → structured markdown notes). |
| Topics | ai, automation, chatgpt, moviepy, python, shortvideo, tiktok |
| LLM providers (13) | OpenAI · Moonshot · Azure · gpt4free · one-api · Qwen (通义千问) · Google Gemini · Ollama · DeepSeek · MiniMax · ERNIE/文心一言 · Pollinations · ModelScope (selected via `config.toml`) |

## What it is

MoneyPrinterTurbo automates the whole faceless-video assembly line. You supply a topic (or your own script); it uses an LLM to write the narration/copy, pulls matching **royalty-free stock footage** (plus optional local clips), synthesizes a **voiceover** (multiple voices with preview), generates **subtitles** (either fast "edge" mode or a local **Whisper** model), layers **background music**, and composites a finished **1080p** short in 9:16 or 16:9 — with **batch generation** and adjustable clip duration. It ships an MVC architecture: a **Streamlit** web UI for humans and a **FastAPI** service for programmatic/batch use. Chinese and English are both supported; the README is Chinese-primary.

The LLM is **one pluggable component** (the script step): you choose one of **13 providers** in `config.toml` and set its key. The rest of the value is the media pipeline (footage retrieval, TTS, Whisper subtitles, MoviePy compositing), not the LLM.

It is **not** a coding agent, a Claude-Code tool, an agent-skill, or anything in the agentskills.io / autonomous-software-development space the corpus tracks — the repo root has **zero** agent artifacts (no `CLAUDE.md`, `AGENTS.md`, `.claude`, `SKILL.md`, MCP). It is a content-generation application that happens to call LLMs.

## Why it's in the corpus — and why it's a WEAK include

It clears Phase 0.9 STRICT at **1/4**, carried entirely by **(a)**:

- **(a) PASS (inferred)** — harry0703 is an inferred China-Mainland solo indie developer (Chinese-primary README, solo account), an Asian-cluster cultural-peer (like v100 Easydict / v117 CodexPlusPlus inferred-PASS). Extends the China-Mainland cluster (v82/v94/v100/v117/v119 + v123).
- **(b) FAIL** — a faceless short-video generator serves no part of the documented #1 goal ("master Claude and autonomous agents *for software development*"); no vault/Scrum/dev-workflow utility.
- **(c) WEAK** — competent MVC + a 13-provider LLM abstraction, but off the corpus's agent/skill methodology domain.
- **(d) WEAK** — Pattern #84 cross-vendor + China-cluster, but zero agent/skill/Claude/MCP surface.

**The honest frame:** the corpus's prior faceless-content subject (v5x `automate-faceless-content`) was classified **OUTSIDE-SCOPE**. The *only* thing making MoneyPrinterTurbo a WEAK INCLUDE rather than a SKIP is the **(a) cultural-peer PASS** — the exact **v80 SmartMacroAI** pattern (1/4, (a)-only, included). So it legitimately clears the gate (≥1 PASS = INCLUDE), but it is **corpus-knowledge of a hugely-popular cultural-peer subject, not goal-#1 progress** — and the 2nd off-goal-domain subject in a row (after v122 dograh). The mandated ~v124 Phase 0.9 audit should note this "(a)-rescue" as N=2 (with v80).

## Pattern Library contribution (modest, no state change)

- **PRIMARY:** NEW **T5 sub-archetype "AI Media-Generation Pipeline App"** PROVISIONAL N=1 (corpus-first in-scope standalone AI-video app; distinct from v84 image-blaster's skill-bundle form and the outside-scope v5x faceless course).
- **SECONDARY (administrative):** #52 SUSTAINED-MODERATE-HIGH N+1 (mega-cumulative/long-sustained profile); #84 cross-vendor N+1 (13 providers); China-Mainland cluster N+1; #82 (thin); #45 MIT.
- **ZERO new Library-vocab minted (§28).** State UNCHANGED. Streak "47+3\*" → "48+3\*".

## Honest non-claims

- **NOT** a Pattern #18 #8 "Multi-Source LLM Aggregator" (a consumer app with multi-provider config ≠ a dedicated aggregator/proxy/switcher like cc-switch / freellmapi / CodexPlusPlus — counting it would dilute #8's just-CONFIRMED-N=3).
- **NOT** an agent / skill / Claude-Code / agentskills.io / MCP subject; **NOT** a Karpathy LLM-wiki subject.
- **NOT** a Pattern #52 EXTREME-VIRAL instance (86.8/d is SUSTAINED-MODERATE-HIGH, despite the 70K★ cumulative).
- **NO** new top-level Pattern; **NO** Pattern Library state change; **NOT** a pilot.

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` for the full gate decision + the "(a)-rescue N=2" audit input, and `01 Analysis/(C) Pattern-Library-Phase-4b-T5-AI-Media-Generation-Pipeline-N1.md` for the sub-archetype registration + honest non-claims.*
