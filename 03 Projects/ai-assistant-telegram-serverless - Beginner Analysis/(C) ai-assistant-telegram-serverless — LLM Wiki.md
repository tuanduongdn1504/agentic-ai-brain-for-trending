# (C) a.i-assistant-chatbot-telegram-serverless — LLM Wiki

> **Subject:** `badpaybad/a.i-assistant-chatbot-telegram-serverles` (repo slug is spelled "serverles", missing a final **s**) · MIT · author **Nguyen Phan Du** (GitHub `badpaybad`, commits as `dunp`)
> **Ship:** v180 (2026-06-22) · **Tier:** T2 Service (self-hosted personal agent framework) · **Verdict:** GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) MODERATE · (c) MODERATE · (d) STRONG] · **Pattern outcome: NO MINT** (corpus-knowledge data-point; counts 46/10 unchanged)
> **Source of truth:** cloned + source-verified at commit `4070f21` (2026-06-21). Facts below are read from the source, not parroted from the (Vietnamese) README. Verdict + collision record → `01 Analysis/`.
> **Browsable HTML companion:** https://claude.ai/code/artifact/776784bb-65e4-48e9-92ed-0830e69d52b6

---

## 1. What it is (one paragraph)

This is a **self-hosted "PC A.I Agentic framework"** — a personal AI assistant you run on **your own Ubuntu PC** (no server, no domain, no managed database) and **command entirely through a Telegram chat**. README headline (translated from Vietnamese): *"Turn your PC into an AI chatbot assistant … runs fully automatically on your private PC, no server, no domain, no database server; secure, data stays with you; 24/7."* You send a chat message; Telegram delivers it to a webhook on your PC (exposed via a **free Cloudflare Tunnel** subdomain); a **FastAPI** app routes it through an **LLM orchestration layer** that picks/combines **skills** (run a bash command, automate a browser, create a Jira issue, OCR/summarize a document, search Google Drive…), executes them locally, and replies in the same Telegram chat. The LLM is **Google Gemini by default**, with a bundled **local Gemma-4 server** (and a peripheral Ollama path) for users who want everything on-device.

**Mental model:** *AutoGPT-style "your PC is the agent," but the entire user interface is a Telegram chat instead of a web UI or terminal, and it's wired to be serverless via a tunnel.*

---

## 2. Why it exists (the problem it solves)

The author's bet is that you don't need cloud infrastructure to have a capable personal agent:

1. **No server / no domain / no DB server.** The PC you already own is the runtime. A Cloudflare Tunnel hands you a free HTTPS subdomain so Telegram can call your webhook; the app re-registers that webhook on every startup. SQLite is the only database.
2. **No custom UI to build.** Telegram (and optionally Discord) *is* the front-end. You "develop no chat UI — you just wait for the Telegram webhook callback, call the LLM, and send the reply" (README, paraphrased).
3. **Data stays on your machine.** Because it runs locally and can use a local LLM (Gemma-4 / Ollama), the privacy story is "nothing leaves the PC" — modulo the Gemini default and the Cloudflare relay.
4. **Natural-language control of your computer.** You don't need to know shell commands: you describe intent in chat, an LLM generates the bash, and the PC runs it (with prompt-level safety guards — see §7).

---

## 3. Architecture (source-verified)

### 3.1 Request flow
```
Telegram chat ──webhook──▶ Cloudflare Tunnel ──▶ FastAPI (program.py, :8088)
                                                      │
                                            orchestrationcontext.skills_decision()
                                                      │  (LLM picks/combines skills)
                                   ┌──────────────────┼───────────────────────┐
                                 skill: cli       skill: browser           skill: jira ...
                                 (bash exec)      (Playwright RAG)         (create issue)
                                                      │
                                              reply ──▶ bot_telegram.send_telegram_message()
```

### 3.2 The core modules (root + `knowledgebase/`)
| Module | Role |
|---|---|
| `program.py` (489 ln) | FastAPI entrypoint; webhook handler; starts the Cloudflare tunnel as a subprocess; per-`chat_id` history (`deque`) |
| `knowledgebase/orchestrationcontext.py` (407 ln) | **The heart.** Builds context (summaries + recent messages + current message + URLs + scraped content + files), runs `skills_decision()`, dispatches to a skill |
| `knowledgebase/orchestrationbuildprompt.py` (+ `.md`) | Builds the dynamic system prompt by reading each skill's `readme.md` and stitching short-/long-term memory in |
| `gemini_dynamic.py` (131 ln) | A "decide tool-calls dynamically" path (built-in `google_search` tool) — **note: its multi-tool loop is a `# todo` stub**, currently a single Gemini call |
| `knowledgebase/dbvectorconnect.py` (311 ln) | **Long-term memory** — `LocalVectorDB` over **FAISS**, embeddings via `gemini-embedding-001` (3072-d) / `text-embedding-004` / **local `fasttext`** (300-d) |
| `knowledgebase/dbcontext.py` / `dbconnect.py` | Shared **SQLite** with JSON-query helpers |
| `knowledgebase/summarychat.py` (+ `.md`) | Rolling chat summarization (short-term → summary memory) |
| `bot_telegram.py` (228 ln) / `bot_discord.py` | Chat transports; `my_telethon.py` (Telethon) reads messages from **all groups your account is in** and can summarize unread into Saved Messages |
| `gemma4/` (program.py, manager.py, tools.py) | A **local Gemma-4 server that re-implements the Gemini `v1beta generateContent` API** — point the Gemini client's base URL at it to run fully local (README: AMD iGPU 780M / 16 GB / ROCm) |

### 3.3 The skills system
A skill = a subfolder under `skills/` with a small contract. README documents two shapes:
```
skills/<name>/                 skills/<name>/        (gemini_dynamic variant)
├── main.py                    ├── system_instruction.md
├── readme.md                 ├── readme.md
└── config.py                  └── skill.md
```
The orchestrator reads each skill's `readme.md` to decide routing, and can **combine** skills. Shipped skills (`skills/`):
- **cli** — generate + run bash on Ubuntu (email via swaks, file ops, system info, logs, monitoring, cron). *Runs arbitrary shell* (see §7).
- **browser** — Playwright-based page RAG (`PlaywrightRAG.py`) + `DINOv2` image embedding.
- **jira** — auto-create Jira issues / track progress when chat trends toward bug reports or feature requests.
- **googledrive**, **filesfolders** — cloud + local file access.
- **new_feature_dev** — the author's **`tot-dev`** spec-first dev methodology as a skill (see §4).
- **common_question_answer** — the default fallback skill when orchestration finds no match.
- **zalo** (708 ln), **toan4** — Vietnamese-ecosystem / domain-specific surfaces.

> **Notable design detail:** for several skills the `.md` file is itself a **meta-prompt that instructs an LLM to generate the skill's `.py`** (e.g. `skills/cli/tool_call_cli.md` is a full natural-language spec for producing `tool_call_cli.py`). Skills are partly self-bootstrapping — "add a skill by writing a readme and letting the LLM build the code." (Interesting; N=1 here — recorded, not a corpus pattern.)

---

## 4. The second layer: the `tot-dev` methodology

The repo ships **four byte-identical rule files** — `.clinerules`, `.cursorrules`, `.geminirules`, `.windsurfrules` (551 bytes each) — that all point a coding agent at **`.agent/tot-dev.md`**. That file is the author's own **spec-first agent-coding methodology**: a strict **`whattodo.md` (intent/SRS) → `howtodo.md` (design, user must confirm) → code** workflow, KISS + DRY, kebab-case Vietnamese-no-accent folder naming, and "protect these core dirs." It governs the vendored **`TreeOfThought/`** sub-project (a separate full-stack .NET/Angular/Flutter app + face-recognition ML — see §6). The repo also bundles `_bmad.zip` (the BMAD method) and `antigravity-help.md`.

So there are really two things in one repo: **(1)** the Telegram PC-agent framework (the headline), and **(2)** a personal spec-first coding-agent methodology + a large unrelated app the methodology was written for.

---

## 5. The LLM story (honest version)

- **Default = Google Gemini.** Every core module imports `google.genai` and `GEMINI_APIKEY`; default model `gemini-2.0-flash`. The framework speaks the **Gemini protocol**, not a vendor-neutral interface.
- **"Use Ollama instead" is mostly aspirational for the core.** `ollama` is imported only in the peripheral `voice_assistant/program.py` and appears as a comment elsewhere — **the orchestration path does not call Ollama.**
- **The real local-LLM path is `gemma4/`** — a FastAPI server that re-implements Gemini's `v1beta generateContent`/files API, so you can point the same Gemini client at `http://0.0.0.0:8000/...` and run Gemma-4 locally. This is a clever decoupling (multi-LLM **via API-compatibility**, not via an abstraction layer), but it means "multi-LLM" in practice = "Gemini protocol + a local server that speaks it."
- **It does not use Claude.** Relevant for the corpus verdict (§ Analysis): this is a competitor-LLM-ecosystem (Gemini) project.

---

## 6. Scale & maturity — read the line counts honestly

- **Headline totals are inflated.** `find` reports ~20.7K Python lines and **~435K JS lines** — but **~431K of the JS and most of the bulk live in `TreeOfThought/`** (1,072 files: a *separate* .NET/Angular/Flutter/face-recognition project the author vendored in as the `tot-dev` reference codebase), plus `cnc/`, `games/`, `cameraip/`.
- **The actual core agent framework is ~8.2K lines of Python** (root + `knowledgebase/` + `skills/` + `gemma4/` + `domain_handlers/`). Substantial for a personal project, but not the 20K/435K the totals suggest.
- **Traction is small:** **6 stars / 2 forks**, single author, MIT.
- **Several pieces are unfinished:** the `gemini_dynamic` tool-call loop is a `todo` stub; `domain_handlers/ngoc_ddd.py` is a personal domain handler; skill coverage is uneven (some skills have empty/terse readmes).

This is a **working, broad, personal "kitchen-sink" framework**, dev-quality rather than a polished product.

---

## 7. Security & dual-use surface (read before piloting)

This framework is, by design, a remote-controlled agent over your machine. The attack/abuse surface is real:
1. **Natural-language → arbitrary bash.** The `cli` skill has Gemini generate shell commands and runs them via `asyncio.create_subprocess_shell` on your PC. Guards are *prompt-level* (the meta-prompt tells Gemini to avoid `sudo rm -rf /`, refuse to read source/secret files, 15s timeout) — i.e. mitigations live in an LLM prompt, not an OS sandbox. Prompt-injection from a scraped URL or a group message could steer it.
2. **Reads all your group messages.** `my_telethon.py` uses your Telegram **user** API (`TELEGRAM_API_ID/HASH`) to ingest messages from every group you've joined.
3. **GUI/browser automation + OCR of your screen** (Playwright/Puppeteer/PyAutoGUI/easyocr).
4. **Cloudflare Tunnel** publishes a webhook endpoint to the public internet.
5. **Secrets in `config.py`** (Telegram token, Gemini key, Discord token, Telegram API id/hash) — a plaintext local file.

**If piloted:** scratch Ubuntu VM only, throwaway bot + throwaway Gemini key, local-only LLM (gemma4) to keep data on-box, never point it at an account with real groups, and read the `cli` skill before enabling it.

---

## 8. Corpus placement (one-line)

A **self-hosted, Telegram-fronted, serverless-on-your-own-PC personal agentic framework** — the same *family* as the corpus's self-contained agent platforms (**OpenHuman v118**, **PilotDeck v175**, **AutoGPT**, **ECC v1**), distinguished only by its **delivery surface** (a consumer chat app as the complete control plane) and its **serverless-via-tunnel** deployment. That delivery facet is a **recurring real-world class** (cf. QwenPaw, opencode-telegram-bot, AI-Telegram-Assistant — none in the corpus) but is **recorded as a deferred candidate axis, not minted** at N=1 on a 6★ single-author instance. See `01 Analysis/` for the full INCLUDE verdict, the NO-MINT reasoning, and the collision record.
