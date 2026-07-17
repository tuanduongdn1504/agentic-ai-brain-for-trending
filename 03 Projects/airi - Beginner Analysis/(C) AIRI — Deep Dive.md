# (C) AIRI — Deep Dive (LLM Wiki v210)

**Subject:** `moeru-ai/airi` — "Project AIRI" (アイリ)
**Built:** 2026-07-17 · wiki **v210** · inline + hand-verified (no workflow — the ~205K shim overflows every subagent >200K, the v200→v209 self-throttle precedent)
**Source of truth:** repo README + raw README + `airi.moeru.ai` docs + WebSearch (identity/landscape). **NOT source-cloned** (WebFetch-only, per the shim-overflow constraint — flagged).

---

## 1. One sentence

AIRI is an **open-source, self-hosted, you-owned real-time AI companion / AI VTuber** — a browser-first (also desktop + mobile) "digital life form" with a **Live2D/VRM avatar, real-time voice chat, memory, and game-playing agents (Minecraft, Factorio)**, driven by **any of 30+ LLM providers behind one provider-agnostic seam (`xsAI`)** — an OSS attempt to recreate Neuro-sama and give everyone their own cyber companion.

Tagline (verbatim): *"💖🧸 Self hosted, you-owned Grok Companion, a container of souls of waifu, cyber livings to bring them into our worlds, wishing to achieve Neuro-sama's altitude. Capable of realtime voice chat, Minecraft, Factorio playing. Web / macOS / Windows supported."*

---

## 2. What it actually is (blunt)

**Domain: AI companionship / entertainment / VTuber.** This is an "AI waifu" / virtual-character companion app. Its purpose is to give a person a persistent, embodied, conversational AI character they own and run themselves — not a livestream you watch (Neuro-sama), not a walled chat product (Character.AI), but a self-hosted digital being that talks, emotes through an avatar, remembers, and can play games alongside you.

That domain is **off both of the operator's goals** (mastering agents for software development; hireui/TalentAxis recruitment). What makes AIRI a *worthwhile corpus subject anyway* is its **architecture** — it is a large, mature (~42.8k★), production-grade agentic system whose engineering touches several live goal threads (a clean provider-agnostic LLM seam, MCP-server tooling, memory systems, and perceive→reason→act agents). **The domain is off-goal; the architecture is the prize.** This is the exact shape of **meetily v196** (a consumer meeting-notetaker whose provider-agnostic `generate_summary()` was the on-goal value) and **OpenMontage v188** (an agentic video system whose agent-first engineering was the value).

---

## 3. Identity (hand-verified)

- **Org:** `moeru-ai` — an open-source **collective / org**, not a company; a dedicated sub-org **`@proj-airi`** holds the ecosystem sub-projects. Self-described as "a group of currently non-funded talented people … computer scientists, experts in multi-modal fields, designers, product managers, and popular open source contributors."
- **Founder / organizer:** **Neko** — GitHub `nekomeowww`, socials 絢香猫 / `@ayakaneko`. Started Project AIRI and self-sponsors the most-contributing members of `@proj-airi` and `@moeru-ai`. Does consulting/outsourcing in **AI infra, AI multi-modal, AI interactive, and multi-agent** fields.
- **NOT Anthropic.** Not a cultural-peer-of-the-operator registered axis. Per routine **§41**, a name/heritage/locale/notability inference is **not** an (a)-rescue → **(a) FAILs cleanly.** First `moeru-ai` / `nekomeowww` author in the corpus (#19 19a data-point).

---

## 4. Metrics & meta (all page-stated §37.4 — the GitHub API is mocked → NOT a #52 viral-velocity claim)

| Field | Value |
|---|---|
| Stars / forks | ~42.8k★ / ~4.3k forks |
| Releases | 79 (latest **v0.11.0**, 2026-07-08) |
| Commits | 4,000+ on main |
| License | **MIT** |
| Languages | TypeScript 72.3% · Vue 21.4% · GDScript 2.3% · C# 1.6% · JS/CSS |
| Recognition | Product Hunt featured · Trendshift listed |
| Status | early-stage, actively recruiting contributors; many headline features WIP |
| Notice | **"We do not have any officially minted cryptocurrency or token"** (anti-scam warning — a viral project's impersonation risk) |

---

## 5. Architecture — the "Brain / Ears / Mouth / Body" metaphor

AIRI organizes itself as an embodied being. This is the map to read for the on-goal patterns.

### 🧠 Brain (reasoning / logic / autonomy)
- **LLM reasoning via `xsAI`** — a **provider-agnostic abstraction over 30+ LLM providers** (see §6, the on-goal prize).
- **Game-playing agents** — **Minecraft (playing), Factorio (WIP + PoC), Kerbal Space Program (planned), Helldivers 2 co-play (WIP)**. These are **perceive→reason→act agents** operating in a game environment: the same autonomy loop as browser-use v41 / page-agent v199 / serve-sim v183, but the "world" is a game rather than a browser/simulator. (Externally this lineage is Voyager/MineDojo/Mineflayer — AIRI *orchestrates* it, doesn't invent the primitive.)
- **Chat surfaces** — Telegram + Discord integrations.
- **In-browser persistence** — **DuckDB WASM** + **pglite** (Postgres in WASM) run the database *inside the browser*.
- **Memory Alaya (WIP)** — the project's long-term memory system; plus `@proj-airi/memory-pgvector` (a pgvector-backed vector memory).
- **WebGPU local inference** — run models client-side.

### 👂 Ears (audio input)
- Browser audio input, Discord audio input, **client-side speech recognition**, **voice-activity detection (talking detection)**.

### 👄 Mouth (speech output)
- **Multi-provider TTS**: ElevenLabs · Azure Speech · OpenAI-compatible · Alibaba Cloud Model Studio · **local Kokoro TTS**.
- Fronted by **`unspeech`** — a universal ASR/TTS endpoint proxy (an OpenAI-compatible speech gateway; the audio analogue of the LLM seam).

### 🧍 Body (avatar / animation)
- **VRM** (3D) and **Live2D** (2D) model support, with auto-blink, auto-lookaround/gaze tracking, idle eye movement. Rendered via **Three.js**.

---

## 6. `xsAI` — the on-goal prize (provider-agnostic LLM seam)

The single most goal-relevant thing in AIRI. `xsai` is a **standalone TypeScript SDK** (published separately, part of `@proj-airi`) that abstracts **30+ LLM providers behind one interface**: OpenAI / Azure OpenAI / **Anthropic Claude** / Google Gemini / DeepSeek / Qwen / xAI / Groq / Mistral / Ollama / vLLM / SGLang / OpenRouter / AIHubMix / 302.AI / Cloudflare Workers AI / Together / Fireworks / Novita / Zhipu / SiliconFlow / Stepfun / Baichuan / Minimax / Moonshot / ModelScope / Player2 / Tencent Cloud / Xiaomi Mimo …

**Why this matters to the operator:** this is the **vendor-seam blueprint** — the exact pattern celebrated in **meetily v196**'s `generate_summary()` (one path, N providers, special-case only the truly-different one), the **mosh-ai A2 seam** pilot thread, and hireui's future first-LLM-feature seam. A software developer *mastering agents* learns from a clean 30-provider abstraction: how to define one call shape, where Claude's shape genuinely differs (`x-api-key` + `anthropic-version` + `/v1/messages`), and how to keep the app provider-agnostic while still exploiting per-provider features. Claude is **one of 30+** here (an aggregator, not Claude-centric) — hence (b) MODERATE, not STRONG.

Sister layer: **`unspeech`** does the same job for **speech** (universal ASR/TTS proxy) — the audio-domain sibling of the LLM seam.

---

## 7. `MCP Launcher` — the agent-substrate hook

`@proj-airi` ships **MCP Launcher** — a **Model Context Protocol server builder/launcher**. AIRI *consumes* MCP tools (to give the companion capabilities) and *builds* MCP servers via this launcher. This lands AIRI on the **#18 B1-MCP family** the vault studies (the OfficeCLI v206 / palmier-pro v192 / google_workspace_mcp v140 neighborhood) — but as a **builder/consumer**, not "one MCP server, many clients." Recorded as a cross-ref + a DEFERRED watch axis ("MCP-server builder/launcher"), NOT minted at N=1 as a sub-component of a companion app.

---

## 8. Delivery surfaces (monorepo)

| App | What | Where |
|---|---|---|
| `stage-web` | Browser version | airi.moeru.ai |
| `stage-tamagotchi` | Desktop app (Electron) | Win/macOS/Linux; native NVIDIA CUDA + Apple Metal |
| `stage-pocket` | Mobile PWA | iOS/Android via Capacitor |

**Packages:** `@proj-airi/stage-ui`, `duckdb-wasm`, `drizzle-duckdb-wasm` (Drizzle ORM driver for DuckDB-WASM), `memory-pgvector`, `server-sdk`, `server-runtime`.
**Ecosystem repos (@proj-airi):** `xsai` (LLM seam) · `xsai-transformers` (Transformers.js) · `unspeech` (ASR/TTS proxy) · `airi-factorio` · `airi-domekeeper` · `Velin` (Vue/Markdown-based prompt management) · `MCP Launcher`.
**Web tech:** WebGPU · WebAudio · Web Workers · WebAssembly · WebSocket · Three.js · HuggingFace Candle (Rust inference runtime). It deliberately went web-first "from the start" so the whole thing runs in a modern browser, while desktop/mobile builds unlock TCP-only features (Discord voice, Minecraft/Factorio).

---

## 9. The four live goal threads AIRI touches (why it's goal-*adjacent*, not off-everything)

1. **Provider-agnostic LLM seam** (`xsAI`, 30+ providers) → meetily v196 `generate_summary()` / mosh-ai A2 / hireui's future vendor-seam / Pattern #18 #8 Multi-Source LLM Aggregator.
2. **MCP-server tooling** (`MCP Launcher`) → the agent-substrate / #18 B1-MCP family.
3. **Memory systems** (Memory Alaya + memory-pgvector + in-browser DuckDB/pglite) → the CC-memory-systems pilot thread / agentmemory v66 / supermemory v132.
4. **Perceive→reason→act agents** (Minecraft/Factorio game agents) → the agent-autonomy / capability-layer cluster (browser-use v41 / page-agent v199 / serve-sim v183) — for *game* environments.

Plus a **speech-domain** tie: AIRI is the corpus's **3rd speech subject** (fish-speech v20 = a TTS model; meetily v196 = STT+summarize app; **AIRI v210 = a real-time TTS+STT companion** with a universal speech proxy).

---

## 10. Honest limitations & caveats

- **Domain is off both goals.** No hireui/recruitment use; no software-development use. Value is architectural study + borrowable patterns, *not* a product to adopt.
- **Much is WIP.** Memory Alaya (WIP), Factorio (WIP/PoC), KSP (planned), Helldivers 2 (WIP), plugin system (planned). Headline breadth > current depth.
- **The hard AI is upstream.** AIRI *orchestrates* third-party models (the 30+ LLMs, ElevenLabs/Azure/Kokoro TTS, ASR). Its own engineering is the runtime, the seams, the avatar/audio pipeline, and the game-agent glue.
- **NOT source-cloned** for this wiki (WebFetch-only, per the shim-overflow constraint) → package-internal claims are page/README-stated, not code-verified. Flagged.
- **NOT world-first.** Neuro-sama (the north star), Character.AI, ChatVRM/pixiv, Amica, **Open-LLM-VTuber** all populate this space. AIRI is a leading **OSS flagship** of the self-hosted AI-companion class, not the inventor of it.
- **Metrics page-stated** (§37.4, GitHub API mocked) → 42.8k★ is a snapshot, not a velocity → **NOT #52**.
- **#66 posture:** self-hosted MIT app that **holds your API keys** and runs games/Discord over TCP + local inference. Risk is *runtime trust* (a companion with your keys + mic + network access) and **crypto-scam impersonation** (the project's own no-token warning), not a postinstall supply-chain vector. Benign-to-moderate; BYO-keys, scratch machine, verify you cloned the real org.

---

## 11. Landscape (all non-corpus)

| Peer | Relation |
|---|---|
| **Neuro-sama** | The closed, single-instance north star AIRI recreates in OSS. |
| **Character.AI** | The walled chat-companion product AIRI opposes (self-hosted vs SaaS). |
| **Open-LLM-VTuber** | Closest direct OSS peer (Live2D voice companion, offline, desktop-pet). |
| **Amica** | Open 3D-character chat frontend (any LLM). |
| **ChatVRM / pixiv** | VRM-avatar-chat inspiration AIRI credits. |
| **LobeChat / Open WebUI** | Adjacent self-hosted chat platforms (not embodied/VTuber). |

None are corpus subjects → **NOT #57** (inspirations/peers ≠ corpus-subject-cites-corpus-subject recursion).

---

## 12. Cross-references into the corpus

- **meetily v196** — the exact precedent: off-goal consumer app, architecture-is-the-prize, provider-agnostic seam, NO MINT (domain-not-capability). AIRI is the same shape, bigger and further-off-domain.
- **fish-speech v20** — speech-domain sibling (TTS model). AIRI = 3rd speech subject.
- **Pattern #18 #8** Multi-Source LLM Aggregator — `xsAI` instance-strengthening.
- **#84 84c** provider-agnostic-by-design — `xsAI` (NO N-bump).
- **agentmemory v66 / supermemory v132 / codebase-memory-mcp v172** — memory-systems cross-ref (AIRI's in-browser DuckDB/pglite vector memory is a distinctive facet).
- **browser-use v41 / page-agent v199 / serve-sim v183** — the perceive→reason→act capability-layer cluster; AIRI adds a *game-environment* member.
- **OpenMontage v188 / agency-agents v185 / Kilo-Code v177** — the "mint the corpus-first world-class exemplar" precedent (the MINT-alternative case; see the Verdict).
- **The LLM-access-tooling family** cc-switch v73 / freellmapi v112 / CLIProxyAPI v207 / OmniRoute v208 — `xsAI` is the *SDK-library* member (an application's own seam, not a gateway service).

---

*Deep Dive by Claude (Opus 4.8) under the LLM Wiki Routine v2.7. Facts hand-verified; package internals page-stated (not source-cloned). Companion docs: `(C) AIRI — Verdict.md`, `(C) AIRI — Pilot Methods Menu.md`, `wiki.html`.*
