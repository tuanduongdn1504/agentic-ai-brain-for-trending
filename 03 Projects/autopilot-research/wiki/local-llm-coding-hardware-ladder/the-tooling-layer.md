# The tooling layer — hosts, endpoints, and wiring an agent to a local model

> All four hosts here are, per [[apple-mlx-stack|Apple]], largely wrappers over the same MLX foundation on Apple silicon. Choose on **cache strategy, resource overhead, and API surface** — not on inference speed claims.

## The four hosts in this bundle

| Host | Used by | Distinguishing feature |
|---|---|---|
| **Ollama** | Quân IT (anchor) | Now ships a **GUI** app *and* a hosted **Ollama Cloud** tier. First-party integration docs. |
| **LM Studio** | Zen van Riel, Tech With Tim | Big model-browser UI; **device linking**; OpenAI **and** Anthropic-compatible endpoints |
| **OMLX** | WEBdoze, Samuel Gregory | **SSD-persisted two-tier KV cache** — the prefill fix. Menu-bar app |
| **MLX LM server** | Apple (first-party) | The reference implementation. `pip install mlx-lm`, OpenAI-compatible, continuous batching |

## OMLX — the most interesting thing in the bundle

**Verified in full** ([github.com/jundot/omlx](https://github.com/jundot/omlx)) — Apache-2.0, maintained by an **individual developer** (jundot / Jun Kim). **New to this corpus** (0 prior mentions).

Why it matters: it attacks [[why-agentic-differs-from-chat|prefill]] directly.

- Block-based KV cache management **inspired by vLLM**, with **prefix sharing** and copy-on-write.
- **Two tiers:** hot in-memory cache with write-back; when it fills, blocks are **offloaded to SSD in safetensors format** via a `PagedSSDCacheManager`.
- **Persists across restarts:** *"On the next request with a matching prefix, they're restored from disk instead of recomputed from scratch — **even after a server restart**."*
- **Continuous batching**, managed from the menu bar.
- **Drop-in replacement for OpenAI *and* Anthropic APIs** — `POST /v1/messages`, streaming usage stats, Anthropic adaptive thinking, vision inputs (base64/URL). Default `localhost:8000`.

Samuel Gregory's rationale for choosing it over LM Studio is resource discipline, not benchmarks: LM Studio is *"becoming very bloated... I want to preserve my RAM for my LLMs. I don't want applications running."*

⚠️ One published third-party comparison cites oMLX at ~47 tok/s vs LM Studio's ~16 on the same task. **Do not quote that figure** — it is a single blog benchmark, not reproduced here, and it scopes oMLX as Apple-silicon-only.

## Ollama — confirmed, with one correction

**Confirmed:** desktop GUI (DMG on the download page), and **Ollama Cloud** paid tiers (**Pro $20/mo, Max $100/mo**). The cloud catalogue **does include Kimi K3**, priced $3.00 / 1M input, $0.30 / 1M cached input, $15.00 / 1M output.

❌ **CORRECTION — the integrations list.** The anchor reads a list off-screen including *Codex, GitHub Copilot, and Xcode*. Ollama's actual integrations index (`docs.ollama.com/integrations`) lists:

> **Claude Code · OpenCode · DeepSeek Harness · OpenClaw · Hermes Agent · VS Code**

Codex, Copilot and Xcode **do not appear**. Note that three of the six that *do* appear are existing corpus topics — [[../deepseek-harness/_index|deepseek-harness]], [[../hermes-agent/_index|hermes-agent]], and OpenClaw.

## Wiring Claude Code to a local model

**Confirmed first-party** ([code.claude.com/docs/en/llm-gateway-connect](https://code.claude.com/docs/en/llm-gateway-connect)):

- `ANTHROPIC_BASE_URL` — points Claude Code at a gateway or custom server
- `ANTHROPIC_AUTH_TOKEN` (bearer) **or** `ANTHROPIC_API_KEY` (`x-api-key`) — pick one

LM Studio's docs confirm **Anthropic-compatible endpoints** supporting the Messages API, enabling *"Claude-style Messages API flows against your local LM Studio server."* Zen van Riel picks the Anthropic-compatible endpoint over the OpenAI one precisely because that is what Claude Code expects.

⚠️ The literal path `/v1/messages` is confirmed for **OMLX** but not explicitly stated in LM Studio's fetched docs. Check your host's own docs rather than assuming the path.

### But two sources say don't use Claude Code for this

- **Samuel Gregory:** *"Claude Code is kind of known for its context blowing... I want to preserve context cuz I've got only limited hardware."* Despite demoing with Claude Code, **he runs local models in OpenCode**.
- **Zen van Riel:** Claude Code's system prompt (**4,200 tokens**, Anthropic-documented) means *"it's not really a free lunch"* — and he calls out the genre: *"I feel like most of the people promoting this are not using it themselves, because unless you have a very powerful machine, this is going to be extremely slow as your repository grows in size."*
- **Apple** demos **OpenCode**, not Claude Code.

**Three of seven sources, including the vendor, route around Claude Code for local models.** If you are memory-constrained, a leaner harness is the higher-leverage change than a bigger model.

## The other wiring paths

**VS Code native** (Tech With Tim) — Command Palette → *Manage language models* → Add models → **custom endpoint** → chat completions. Fill in ID, name, URL; set capabilities (**tool calling**, vision) and max input/output tokens. Requires a recent VS Code.

**Continue extension** — used *only* to get **autocomplete**, which VS Code's native feature didn't cover: add a model with `roles: [autocomplete]`. The standard local setup is **two models** — a ~1.5 B autocomplete model plus a large tool-use chat model.

**Xcode** (Apple) — Settings → **Intelligence** → app chat provider → locally hosted provider → set the port.

**LM Studio device linking** (Zen van Riel) — run the model on a Linux/GPU box and consume it from a MacBook over an encrypted link, so the client machine needs no VRAM at all. Combined with Tailscale (Samuel Gregory), the model can be reached from outside the home network. **This decouples the ladder in [[the-hardware-ladder]] entirely** — the constraint moves to whichever machine actually hosts the weights.

## Non-negotiable: the chat model must support tool use

Tech With Tim: *"If it doesn't have tool use, it's not going to be able to actually call the tools to create the files."* Without it you have a chatbot, not an agent. Apple says the same — start the server *"with a model that supports tool calling."*

## Key Takeaways

- **Ollama / LM Studio / vLLM are built on MLX** (Apple, first-party). Pick on cache strategy and overhead, not engine.
- **OMLX (Apache-2.0, solo-maintained) is the notable find** — SSD-persistent, restart-surviving prefix cache is a direct attack on the prefill bottleneck.
- **Ollama Cloud is real** (Pro $20 / Max $100 per month) and carries Kimi K3 — but the anchor's integrations list is **wrong**; Codex/Copilot/Xcode are not on it.
- **`ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`/`ANTHROPIC_API_KEY`** is the documented redirect path.
- **Three of seven sources — including Apple — avoid Claude Code for local models** in favour of OpenCode, on context-overhead grounds.
- **Remote hosting (LM Studio link / Tailscale) sidesteps the client hardware question entirely.**
- **No tool use, no agent.**

## See also
[[why-agentic-differs-from-chat]] · [[apple-mlx-stack]] · [[the-hardware-ladder]] · [[quality-ceiling-and-failure-modes]] · [[../local-ai-coding-agents/lm-studio|local-ai-coding-agents/lm-studio]] · [[../local-ai-coding-agents/opencode-local-provider|local-ai-coding-agents/opencode-local-provider]]
