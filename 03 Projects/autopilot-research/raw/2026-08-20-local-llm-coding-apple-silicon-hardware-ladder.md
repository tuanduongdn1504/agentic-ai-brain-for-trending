# Local LLM coding on Apple Silicon — the 64GB Mac mini M4 middle of the hardware ladder

> **Ingested:** 2026-08-20 · path 1 (`/loop`, anchored bundle via `bin/autopilot-drain.py --dry-run` selection)
> **Anchor:** operator-submitted `GBf_mKxGqtk` — anchor validation **PASS 1/1 (100%)**
> **Transcripts:** yt-dlp original-language auto-captions → `bin/vtt-to-md.py`, all six read in full in the main loop. **NotebookLM: none** (a claims scorecard cannot grade a paraphrase).
> **Total corpus:** 25,820 words / 300 timestamped paragraphs across 6 videos.

---

## Why this bundle exists

This is **not** a new-subject ingest. It is a **targeted test of a standing corpus claim.**

`wiki/local-ai-coding-agents/` (2026-07-11, Code with Beto) left the hardware question with **two endpoints and nothing between them**:

- 18 GB MacBook — **could not run** Qwen3.6-27B
- 96 GB M3 Ultra Mac Studio — **ran it comfortably**
- `hardware-economics-and-tco.md` concluded **"≥24 GB is a practical minimum"**

The operator submitted a 48-minute hands-on at **64 GB — the untested middle rung** — and the drain rubric filled the remaining slots with a **24 GB** data point and three workflow/quality takes. The bundle therefore spans the whole ladder.

**Headline finding: the corpus's framing is the wrong axis.** RAM is necessary but not sufficient. Every source in this bundle independently lands on the same mechanism: **for *agentic* coding the binding constraint is KV cache, which scales with context, which scales with repository size and with the harness's own system prompt.** A machine that comfortably *chats* with a model can fail at *agentic coding* with the same model. See "The correction" below.

---

## The six sources

| # | Source | Channel | Date | Len | Views @ ingest | Hardware under test |
|---|---|---|---|---|---|---|
| 1 | **[ANCHOR]** Thử local LLM, coding trên Mac mini M4, 64GB ram | **Quân IT** (VN) | 2026-08-19 | 48:34 | 1,755 | **Mac mini M4, 64 GB** |
| 2 | M4 Pro Mac Mini 24GB RAM vs Local LLMs: Can It Handle It? | WEBdoze (Dragos) | 2026-05-22 | 16:45 | 7,291 | **Mac mini M4 Pro, 24 GB** |
| 3 | Local AI Coding is Finally Good Enough | ForrestKnight | 2026-06-18 | 21:57 | 179,582 | Threadripper 9980X + Radeon AI Pro R9700 32 GB VRAM + 128 GB DDR5 |
| 4 | Finally, The CORRECT Way to Run Local AI on a Mac | Samuel Gregory | 2026-06-30 | 08:36 | 59,285 | M5 Max, 128 GB |
| 5 | The Unbeatable Local AI Coding Workflow (Full 2026 Setup) | Zen van Riel | 2026-03-01 | 16:11 | 259,982 | RTX 5090, 32 GB VRAM (Linux) + MacBook client |
| 6 | The Best LOCAL Agentic Coding Workflow (Complete Guide) | Tech With Tim | 2026-06-10 | 33:16 | 179,322 | M5 Max, 64 GB |

**Disclosures present in the sources:** #3 is an **AMD-sponsored** video (ForrestKnight states the partnership on camera and links AMD in the description). #6 carries **two** sponsor reads (here.now hosting; WhisperFlow dictation) plus an affiliate link. #5 promotes the author's paid AI-engineering community. Treat hardware recommendations in #3 and tooling picks in #6 accordingly — the *measurements* still stand, the *framing* is paid.

---

## 1. ANCHOR — Quân IT, 64 GB Mac mini M4 (VN)

The only source in the bundle testing a **large, real, multi-service production codebase.** He explicitly rejects toy demos: *"mấy cái ông YouTube mà cứ build mấy cái game nhỏ nhỏ build con rắn"* — YouTubers who just build little snake games — *"nó không giải quyết được cái bài toán thực tế"* (it doesn't solve the real problem).

**Setup**
- Mac mini M4, **64 GB unified memory**, ~400 GB free storage. States he invested "65 củ" (≈65 million VND) in the machine.
- Ollama as the host (notes it now has a **GUI** and an **Ollama Cloud** tier, which he says hosts Kimi K3). Mentions LM Studio as the no-CLI alternative.
- Ollama ships **built-in integrations** — he shows a list including Claude Code, OpenCode, Codex, Copilot, VS Code, Xcode.
- Models: a `qwen coder 30B` (~18 GB, downloaded ~8 months prior), then a **Qwen 3.5** build advertising a **1M context window**.
- Drives it through **Claude Code** pointed at the local endpoint via environment variable.
- Restarts the machine first to free RAM; runs only OBS + one window.

**Test target:** a large repo — many services, GitHub Actions, CI/CD, git submodules, Grafana dashboards. Two tasks: (a) comprehend the codebase, (b) a deliberately non-critical Grafana "no data" dashboard investigation.

**What happened**
- **First response to `hello`: 2 min 45 s.** He attributes it to cold-loading weights into RAM and accepts it: *"nếu mà mất 1 phút mấy thì mình cũng ok... so với việc phải trả vài trăm đô cho Claude Code"* — a minute-plus is fine versus paying several hundred dollars a month.
- RAM occupancy jumped to ~80-something percent.
- **Thermals/acoustics:** the mini ran *"rất là nóng"* (very hot) and audibly spun up — *"con Mac mini này hồi xưa... nó im re mà bây giờ nó hú lên"* (it used to be dead silent, now it howls). Screen recording visibly stuttered (*"nó giật"*).
- **Repeated API errors.** He first suspects the endpoint, then correctly diagnoses it: *"cái context của mình nó bị lớn quá"* — the context got too large and blew the model's window. Re-prompting with a short prompt worked.
- **Context window:** default max 256 K; he set 256 K and notes it is *"khoảng 1/4"* — about a quarter — of Claude Code's.
- **It partially worked.** Claude Code launched a background general-purpose subagent against the local model, read the repo, and *correctly* connected "Grafana dashboard" → deploy monitoring → GCP cloud logging. He confirms on camera: *"nó hiểu nè"* — it understands.
- Tested **vision**: pasted a dashboard screenshot; Qwen 3.5 advertises vision + tools + thinking. Got `invalid tool parameter` errors.
- **Security observation (his own, unprompted):** the agent requested access to **iCloud Drive** and **Music** — *"nó đòi access hết luôn"* (it wants access to everything) — which he flags as *"hơi bị nguy hiểm"* (rather dangerous), noting it should only need the project folder. He denies it, and the denial is what produces the final "no data" answer.
- Claude Code emitted a warning that **Qwen is not a model this version recognises**, which he connects to auto-compact and context-window assumptions breaking.

**His verdict (explicit, twice):** at this point in time, locally-hosted open models are **not good enough** for his production environment. His stated bar is **parity with Sonnet**, not with the frontier: *"ít nhất là nó cũng phải ngang ngửa được với con Sonnet thì mới đủ trình."* He is content to trade speed for cost — the quality is what fails.

**Aside worth keeping — the architecture-not-the-model thesis.** Before any benchmarking he argues that most of Claude Code's power is **not** the model: it's prompt analysis, subagent launching, logging subagent results, context management, compaction, and per-session note-taking. *"Với con Sonnet là đủ rồi không cần phải tới [Fable]"* — Sonnet is enough, he doesn't need the top model; the strength is *"các cái setup xung quanh nó, architecture đó."* This is an independent re-derivation of the corpus's own harness-over-model thesis, from a source that had no contact with it.

**Stated next steps:** cloud-hosted open models (Kimi K3, which he says is much cheaper than the frontier), OpenCode, Kimi's native CLI, and an Unsloth quantization run. He notes a 1-bit K3 quant is ~610–665 GB total memory and that he'd need his 3-node, ~1 TB-RAM server cluster for it — not the mini.

---

## 2. The 24 GB rung — WEBdoze

Directly below the anchor. **Result: failure, at a much smaller workload.**

- M4 Pro Mac mini, **24 GB**. Uses **OMLX** (an MLX-based LM Studio alternative) driving the **Pi** agent.
- Model 1: a ~9 B parameter 4-bit MLX build with MTP. Calls 9 B *"the sweet spot"* for 24 GB.
- Raised context to **132 K**; memory sat at ~20 GB of 24 GB — leaving almost nothing for the OS and the screen recorder.
- Task: a small **Astro** marketing site — menu, footer, testimonials, README, SVGs. Far lighter than the anchor's repo.
- Throughput decayed **70 → 20 → 18 tokens/sec** as context filled. He names the cause: *"the context is already at 35K. That's why it's that slow."*
- Fell back to a **4 B, 4-bit** model — faster, and he notes it beat a Gemini flash model on the same task.
- **Outcome: it got stuck generating the hero SVG, sat for 20 minutes, and "went dark."**
- His conclusion: *"M4 Pro Mac Mini is not powerful enough even to run a four bits and four billion parameter model"* — and he links this straight to cloud pricing: *"that's why the prices are increasing to the API request, because you need powerful machines to run these things locally."*

**This is the load-bearing counter-evidence.** The corpus called 24 GB a "practical minimum." At 24 GB, with an agent attached, a **4-billion-parameter 4-bit** model did not finish a static marketing page.

---

## 3–6. The mechanism, corroborated four ways

Every remaining source independently identifies **context/KV cache as the real constraint** — not parameter count.

**Samuel Gregory (M5 Max, 128 GB)** — the cleanest statement of the multiplier:
> a **36 GB** model, once context is loaded, was consuming **~80 GB of RAM**. *"Even though the model's 36, this is how the context indeed has an impact on the amount of RAM that you need."*

He has landed on **OMLX** over Ollama and LM Studio, for a specific reason: it persists the **KV cache to SSD in safetensors format**, two-tier (hot blocks in RAM, cold blocks on SSD, LRU eviction), and restores previously-seen prefixes **across requests and server restarts** so they are never recomputed. He calls LM Studio *"very bloated"* and wants RAM reserved for weights, not for the app. Notes Ollama's MLX support was, at the time, roughly one model.

He also flags the harness itself as the problem: *"Claude Code is kind of known for its context blowing... I want to preserve context cuz I've got only limited hardware"* — and says that despite demoing with Claude Code, **he actually runs local models in OpenCode.**

**Zen van Riel (RTX 5090, 32 GB VRAM)** — the sharpest version, and an explicit call-out of this exact genre of video:
- Fully-on-GPU: **100–140 tokens/sec**. Spill a single layer to system RAM and *"the performance will be much worse... just because you can fit a model on your system by putting some of the parameters on your system RAM doesn't mean it's actually going to be usable in practice."*
- *"Especially for agent coding, you're going to be using very big context windows, where the compute cost basically scales exponentially."*
- Connects Claude Code to **LM Studio's Anthropic-compatible `/v1/messages` endpoint** by overriding the Anthropic base URL and API key. (LM Studio also exposes an OpenAI-compatible endpoint; he picks the Anthropic one because that is what Claude Code expects.)
- **The call-out:** Claude Code injects a large system prompt, so the first response is slow. *"This is what a lot of YouTube videos are actually missing... I feel like most of the people promoting this are not using it themselves, because unless you have a very powerful machine, this is going to be extremely slow as your repository grows in size."*
- **Silent-failure trap:** with LM Studio's default context (~4 K), the request **hangs indefinitely with no clear error message**, because Claude Code's system prompt alone overruns it. He raises it to 80 K, later 200 K.
- **Identity trap:** the local model reports that it is *Sonnet* — because Claude Code's system prompt says so. *"They don't always have self-awareness of the model that they actually are."* Correspondingly, Claude Code's own token counter (45 K / 200 K) reflects its assumption of Sonnet 4.6, **not** the local model's real configuration.
- **Mitigation he recommends:** force **subagents** per task — each gets a fresh context window and reports back — *"I definitely recommend you to work with sub-agents more than ever if you're doing local AI coding."* Runs in a dev container with bypass-permissions so he can walk away.
- Honest outcome: ~30 minutes for a dashboard, real bugs, and a **hallucinated hardcoded "NVIDIA RTX 3080"** in the output.

**Tech With Tim (M5 Max, 64 GB)** — the tutorial, and the source of the ladder table:
- Frames the whole selection problem on VRAM / unified memory. On Mac, **~75–80% of unified memory is usable** for the model; the rest is OS and other processes.
- Cheat sheet as stated: 8 GB → 7 B · 12–16 GB → 14 B · 24 GB → 32 B · 64 GB+ → 70 B.
- **Bandwidth is the other axis:** quotes RTX 4090 at **1,008 GB/s** vs M4 Max at **546 GB/s** — *"with Mac, you're going to have bigger models generally, but if you have a dedicated GPU... they're going to be a lot faster because the memory bandwidth is typically quicker."*
- Spill penalty: a model that overflows VRAM into system memory or disk is *"like 100 times slower."*
- Setup path is **LM Studio + VS Code's new native "Manage language models" custom-endpoint** feature (chat completions), plus the **Continue** extension purely to get autocomplete. Two models: a ~1.5 B autocomplete model and a large tool-use chat model.
- **Requires tool use** in the chat model or agentic editing is impossible.
- Real result, on his 64 GB machine: asked for a chess game **in React**, got **plain JS instead**, ~600 lines — and **the game didn't load**. He shipped the tutorial anyway with *"clearly there's some bug."*
- Self-reported interference: *"my fan is now spinning up... my performance is going to be a little bit degraded because I am recording my screen."* Separately, a 25-second response at 82 tokens/sec because screen recording was competing for memory.
- His honest scope: *"if you're on a plane... if you're out of credits... smaller inline edits, creating some functions, not trying to do like super complex prompts, this works and it works pretty well."*

**ForrestKnight (AMD workstation, 32 GB VRAM + 128 GB RAM)** — the only source testing **real production codebases**, and the most rigorous:
- Codebases: **Excalidraw** (TypeScript) and **Warp** (Rust, recently open-sourced). Tasks pulled from **actual GitHub issues/feature requests**, two per codebase (one pattern-following, one architecture-touching). Baseline: **Opus 4.7**.
- Motivation is explicitly **regulatory, not economic**: ITAR-controlled defence code, HIPAA, IP-sensitive work, hedge funds where *"no code or data can leave the building."* He concedes upfront that if you *can* use a subsidised frontier model, *"do it. Why not?"*
- **Easy tasks: local passed.** Highlighter mode and `/clearhistory` both worked.
- **The quality gap is architectural, not functional.** On the highlighter, Opus modelled it as a real property on the data model; Qwen produced a visually identical result that *stops being a highlighter once the stroke exists.* Same output, worse model.
- **The most valuable single finding in the bundle:** on the star-shape task Qwen 3 Coder Next generalised diamond and star collision handling into one helper that **always uses star points** — so diamond collision now runs through star geometry. *"That is a bug, a bug that the type checker will not catch because the code works, it passes all the checks... If you're a vibe coder, job well done."*
- **Hard task: local hit a ceiling.** Qwen 3 Coder Next failed to compile the Warp bookmarks feature with **47 errors**, tried repeatedly, and quit: *"Given the complexity, let me stop here... needs to be fixed by someone familiar with the Warp code base's UI API."* (Opus also only half-delivered — it inserted the bookmarked command without executing it, and created an unintegrated panel type.)
- **Speed:** local took **at least 5× longer** than Opus.
- **His verdict is narrower than his title.** "Good enough" is explicitly redefined: *"good enough when you look at it from a standpoint of being able to help you in your work as a software developer, **not comparing it to a frontier model**."* Operating instructions: treat local models like frontier models from *one to two years ago* — be very specific, and **break tasks into much smaller ones**, fed one at a time.

---

## The correction this bundle forces on the corpus

`wiki/local-ai-coding-agents/hardware-economics-and-tco.md` currently says **"≥24 GB is a practical minimum"** and presents a quant→machine table keyed on **model weights**. That table is right about *loading a model* and wrong about *agentic coding*, and the bundle shows exactly why.

**The missing variable.** Required memory is not `weights`. It is:

```
weights  +  KV cache(context)  +  harness system prompt  +  OS/app headroom
```

…where `context` is driven by **repository size**, and the harness contributes a large fixed floor before your code is even read. The corpus already names KV cache as "the hidden cost" — but then still publishes a table keyed on weights alone, and still calls 24 GB a minimum.

**The evidence, arranged on the ladder:**

| Rung | Source | Model | Workload | Outcome |
|---|---|---|---|---|
| 18 GB MacBook | Beto (corpus v-2026-07-11) | Qwen3.6-27B | — | **Could not run** |
| **24 GB** M4 Pro | WEBdoze | **4 B, 4-bit** | small Astro site | **Stalled 20 min, died** |
| 32 GB VRAM | Zen van Riel | Qwen 3.5 35B MoE | greenfield Next.js | Works fully on GPU; *"much worse"* on any spill |
| 32 GB VRAM + 128 GB | ForrestKnight | Qwen3.6-27B / Coder Next | **real** Excalidraw + Warp | Easy tasks pass; hard task **47 compile errors, gave up**; 5× slower |
| **64 GB** M4 mini | **Quân IT (anchor)** | Qwen 3.5 | **large multi-service repo** | Hot, loud, laggy, context-blown API errors; **"not good enough"** |
| 64 GB M5 Max | Tech With Tim | Qwen3.6 35B A3B | toy chess game | Produced ~600 lines; **wrong language, didn't run** |
| 128 GB M5 Max | Samuel Gregory | 36 GB model | — | **~80 GB RAM consumed** once context loaded |
| 96 GB M3 Ultra | Beto (corpus) | Qwen3.6-27B | small feature | *"Good enough"* |

Read down that column: **the two sources that ran real production repositories are the two that returned negative verdicts**, at 64 GB and at 128 GB-class hardware respectively. The positive verdicts cluster on greenfield and toy workloads. Beto's "good enough" at 96 GB and ForrestKnight's "good enough" are *not* the same claim as "good enough on your repo."

**The corrected rule of thumb:** the question "is N GB enough?" is unanswerable without naming the workload. State it as a pair — *(memory, repository size)* — or don't state it.

---

## Claims to verify

Source-attributed claims requiring external checking before they enter the wiki:

| ID | Claim | Source |
|---|---|---|
| C1 | LM Studio exposes an **Anthropic-compatible `/v1/messages`** endpoint alongside an OpenAI-compatible one | #5 |
| C2 | Claude Code can be redirected to a local server via `ANTHROPIC_BASE_URL` + auth-token env vars | #1, #5 |
| C3 | **OMLX** exists as an MLX-based local server with SSD-persisted, two-tier LRU KV cache | #2, #4 |
| C4 | Qwen3.6 max context = **262,144** tokens | #4, #6 |
| C5 | LM Studio's **default** context window is ~4,000 tokens | #5, #4 |
| C6 | RTX 4090 = **1,008 GB/s**; M4 Max = **546 GB/s** memory bandwidth | #6 |
| C7 | ~**75–80%** of Mac unified memory is usable for model + context | #6 |
| C8 | **Warp** open-sourced its codebase (~1–2 months before 2026-06-18) | #3 |
| C9 | Qwen3 Coder Next ≈ **80 B MoE, ~3 B active** parameters | #3, #6 |
| C10 | **Ollama** now ships a GUI **and** a hosted "Ollama Cloud" tier; cloud catalogue includes Kimi K3 | #1 |
| C11 | Ollama ships first-party integration docs for Claude Code / OpenCode / Codex / Copilot / VS Code / Xcode | #1 |
| C12 | A 1-bit Kimi K3 quant totals ≈ **610–665 GB** of combined RAM+VRAM | #1 |
| C13 | VRAM ladder: 8→7 B · 12–16→14 B · 24→32 B · 64+→70 B | #6 |
| C14 | Claude Code emits a *"not a model this version recognises"* warning for third-party models, affecting auto-compact | #1 |
| C15 | Quân IT's Mac mini M4 64 GB ≈ 65 million VND | #1 |

Unverifiable-by-design (single-operator observation, recorded as testimony not fact): the 2 min 45 s cold start, the thermal/acoustic behaviour, the iCloud/Music access prompt, the 47 compile errors, all token/sec figures.

---

## Corpus placement

- **Tests and corrects:** `wiki/local-ai-coding-agents/` — specifically `hardware-economics-and-tco.md`.
- **Second Quân IT topic:** sibling to `wiki/quanit-becoming-ai-engineer-2026/` (which carries 1 MISLEADING verdict — creator reliability prior available for comparison).
- **Independent re-derivation:** the anchor's harness-over-model thesis re-derives, from a cold start, the corpus's own position.
- **New for the corpus:** OMLX; LM Studio link/remote-model feature; VS Code native custom-endpoint model management; the type-checker-invisible bug class; the silent-hang-on-small-context failure mode; the model-identity-follows-system-prompt trap.
