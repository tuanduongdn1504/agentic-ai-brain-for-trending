# LM Studio — the local host + OpenAI-compatible server

> **First-party:** [lmstudio.ai/docs](https://lmstudio.ai/docs) + [LM Studio blog](https://lmstudio.ai/blog). Verified in the [[source-provenance|LM Studio dive]] (read real docs).

## What it is

- A desktop app (macOS/Windows/Linux) to **discover, download, load, and chat with** local models, plus a **local server** so other tools can call them.
- Ships both a **GGUF (llama.cpp)** engine and an **MLX** engine, auto-selecting per model/build ([[mlx-runtime]]).

## The features Beto uses (C7 — CONFIRMED)

| Feature | Confirmed? | Detail |
|---|---|---|
| **Developer mode** | ✅ | Settings toggle; unlocks the developer tab + server. |
| **OpenAI-compatible server** | ✅ | Endpoints incl. `/v1/chat/completions`, `/v1/models`, embeddings, structured output (JSON schema), tool use. Default `http://localhost:1234/v1`. **This is the seam every other tool plugs into.** |
| **Developer tab (live logs)** | ✅ | Streams tokens + request logs in real time. |
| **Max concurrency** | ✅ | "Max Concurrent Predictions," **default 4** — run several sessions/agents against one loaded model. |
| **KV-cache quantization** | ✅ | Introduced ~v0.3.7 (Jan 2025). Beto's framing — *"faster but can hurt quality"* — is the **accurate** tradeoff. Off by default. |
| **Adjustable context window** | ✅ | Per-model load setting (bounded by memory — bigger context = more KV-cache VRAM). |

## LM Link (C9)

- **LM Link** (announced ~2026-06-04) lets you reach a model running on your desktop from a **lightweight device** (laptop, or iPhone via the **Locally** app) over a **Tailscale-backed, end-to-end-encrypted** connection. ([[locally-ai-lm-link]].)
- ⚠️ Beto's aside that **"your computer can actually be sleeping"** while you chat is **unsupported** — a sleeping Mac normally drops its network. It *might* work with Power Nap / a wake configuration, but no docs claim it. Treat as dubious; **verify empirically** before designing around it.

## Why LM Studio is the load-bearing piece for a builder

The **OpenAI-compatible endpoint is the vendor seam.** Any tool that speaks the OpenAI Chat Completions API — opencode, Claude Code (via a small proxy), your own app's SDK — can point at LM Studio by changing one `baseURL`. That is exactly the abstraction the operator's **Match-Explain vendor seam** ([[../mosh-ai-powered-apps/_index|Mosh A2 pattern]]) is built to exploit: add "LM Studio localhost" as one provider behind the seam and you have a **local tier** for free. See the pilot menu (method B1).

## Alternatives (for the file, not the video)

- **Ollama** — the CLI-first sibling; see [[../cowork-third-party-inference/setup-local-ollama|cowork-third-party-inference: local Ollama]]. Ollama also exposes an OpenAI-compatible endpoint. LM Studio is GUI-first; Ollama is script-first.
- **llama.cpp / llamafile** — lower-level; LM Studio wraps llama.cpp.

## Takeaways
- LM Studio's real value = a friendly GUI **plus** a standards-compatible local server.
- The server endpoint is the integration point — treat it as "OpenAI API, but localhost, but free, but your data never leaves."
- Don't rely on the sleep-mode chat behavior without testing it.

## See also
[[qwen3.6-27b]] · [[opencode-local-provider]] · [[locally-ai-lm-link]] · [[privacy-data-residency]]
