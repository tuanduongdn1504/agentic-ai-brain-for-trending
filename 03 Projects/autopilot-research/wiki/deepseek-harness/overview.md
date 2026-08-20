# What DeepSeek Harness is

> Source bundle: 6 videos, 2026-08-17 → 2026-08-20. Verified against github.com/deepseek-ai/deepseek-harness on 2026-08-20.

## The one-line version

**DeepSeek Harness (`dsh`) is an open-source agent harness in which every product capability above the Node runtime is a hot-swappable plugin — including the model adapter, the tool registry, the agent loop, the sandbox policy, and the web UI itself.** Its GitHub "About" string is exactly: *"DeepSeek Harness: Everything is a Plugin."*

Verified facts as of **2026-08-20**: **169.1k stars / 18.1k forks**, **MIT** license, README self-labels **developer preview** with the warning *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES."*

## What a harness is (and why this framing matters)

The Cef Experience gives the cleanest primitive account in the bundle: an LLM is a black box that consumes text and emits text, and *"as far as the LLM is concerned, it's not capable of executing functions or calling tools."* Tool definitions go into the system prompt; the model emits a tool name and arguments; **the environment — the harness — actually executes them** and appends results to context, looping until the model stops.

Turing Post draws the consequence the whole bundle turns on: *"Put the same model inside two harnesses, and you can get two different assistants."* The harness decides what enters context, which tools exist, what gets stored, and when the model gets another turn.

This reframing is the actual thesis. Turing Post: *"We spend so much time comparing models that we often treat the surrounding system as just packaging. DeepSeek is treating it as the architecture."*

## The two features every source independently identifies

Five of six sources converge on the same pair, with no cross-citation between them:

1. **Everything is a plugin** — see [[deepseek-harness/everything-is-a-plugin]]
2. **The trajectory** (full append-only trace of what the model saw) — see [[deepseek-harness/trajectory-and-observability]]

The Vietnamese source states the pair most bluntly: *"Một là plugin, hai là hot reload"* — then corrects himself to the accurate pairing: *"một là hot reload plugin, hai là everything is plugin."*

## Runtime shape

- **Node.js** application, TypeScript. The VN source read **97.1% TypeScript** off the GitHub language bar (see [[deepseek-harness/caveats-and-corrections]] on why this number needs a language-basis caveat).
- Launch: `npx` the package, which serves a **web UI on localhost**. Cef reports port **3080**; the VN source reports *"port 3000 gì đấy"* (port 3000-something) — unresolved minor divergence.
- **Profiles**: the VN source documents `dsh profile web` and a **headless** profile (*"nó dùng theo kiểu CLI ấy, nó không có giao diện gì hết"*) — CLI-shaped, no TUI, but still plugin-capable.
- **Model-agnostic.** Every source stresses this. Providers observed in the bundle: DeepSeek direct, OpenRouter, OpenAI, Anthropic, Bedrock, Ollama/local, any OpenAI-compatible endpoint. Better Stack notes their own config example ships with a Claude Sonnet entry in it.
- **Modes**: `standard` / `PTC` / `minimal` / `creator`. See [[deepseek-harness/creator-mode-and-self-modification]].
- **Permission tiers**: read-only / workspace-write / full-access.

## What it is *not*

Turing Post checks the word "everything" and reports the honest boundary: *"There is still a small core disk kernel underneath, followed by node, the operating system, and the hardware. Everything means nearly every product capability above that kernel."*

And it is not self-improving in the strong sense. See [[deepseek-harness/creator-mode-and-self-modification]] for the persistence limits that three sources describe differently.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/cordis-and-the-paper]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[harness-engineering/_index]] · [[claude-code-plugins-stack/_index]] · [[local-ai-coding-agents/_index]]
