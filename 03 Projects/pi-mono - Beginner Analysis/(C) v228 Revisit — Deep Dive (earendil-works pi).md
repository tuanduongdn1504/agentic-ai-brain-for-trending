# Pi Agent Harness — v228 corpus-recursive REVISIT of v36 pi-mono (Deep Dive)

**Wiki:** v228 · **Date:** 2026-08-08 · **Routine:** v2.7 · **Author-Claude:** Storm Bear vault
**Subject:** `earendil-works/pi` (was `badlogic/pi-mono` = corpus subject **v36**, 2026-04-23)
**Source-verified at commit** `e47b8e3` (shallow clone, 2026-08-08) · **version** `0.84.1` (lockstep) · **license** MIT
**Framing:** the **3rd corpus-recursive REVISIT** in wiki history (after v78 ECC↺v1, v185 agency-agents↺v18). This is not a fresh subject — it is v36 re-examined ~3.5 months later, capturing an ownership move + a large architecture evolution.

> **Verify-first note** (per `feedback_wiki_verify_independently_check_collisions`): all corpus-fact / collision / identity / mint claims below are **hand-verified** — collision grep of the latest-tip tree (no `pi`/`earendil` *subject* folder exists v201→v227; Pi appears only as a *dependency* of llm-space v221 and a *cited harness*), the ownership move independently WebSearch-confirmed (Ronacher/Earendil), and the source read from a real clone. Produced **INLINE, no workflow/subagent** — the ~1MB shim overflows every subagent (the v200→v227 documented self-throttle).

---

## 0. One-paragraph thesis

`earendil-works/pi` is the **minimal, self-extensible, multi-provider terminal coding agent** ("harness") that the corpus first met as `badlogic/pi-mono` at **v36** (Mario Zechner, Austrian solo author, libGDX creator). Since then two things happened. **(1) It got a company:** on **2026-04-08 Mario Zechner + Pi joined Earendil**, a venture-backed **public-benefit corporation** co-founded by **Armin Ronacher** (creator of Flask/Jinja/Sentry, a longtime Pi user); the repo moved `badlogic/pi-mono → earendil-works/pi`, the npm scope moved `@mariozechner/* → @earendil-works/*`, and **the core stayed MIT** under open-core stewardship (Earendil also runs a cloud agent platform, *Lefos*). **(2) It grew up architecturally:** the v36 monolithic CLI is now a **client/server-capable runtime** with a transport-neutral **CBOR wire protocol for remote sessions**, an **SDK/RPC embedding path**, **pluggable session backends**, a **built-in evals harness**, **vendor-neutral telemetry contracts**, and a genuinely serious **supply-chain-hardening** posture — while **doubling to ~85K★** and **keeping its two defining stances intact**: radical minimalism ("no MCP, no sub-agents, no plan-mode; ask pi to build it or install a package") and the OSS-session-donation flywheel.

**Why this matters to the vault:** Pi is Goal #1 dead-center (an open coding agent for software dev) and remains the operator's cleanest *Claude-Code alternative + multi-provider escape-hatch*. But the highest-ROI takeaways from the revisit are **borrowable engineering playbooks** — supply-chain hardening, agent containerization, an evals discipline, and the "you don't need MCP" design lens — not "adopt the product."

---

## 1. Identity, ownership, provenance (hand-verified)

| Field | v36 (`badlogic/pi-mono`, 2026-04-23) | v228 (`earendil-works/pi`, 2026-08-08) |
|---|---|---|
| Owner / org | `badlogic` (Mario Zechner, solo) | **`earendil-works`** (Earendil Inc.) |
| npm scope | `@mariozechner/*` | **`@earendil-works/*`** |
| Company | none (solo OSS) | **Earendil** — venture-backed **public-benefit corporation**, co-founder **Armin Ronacher**; open-core; cloud platform *Lefos* |
| Lead author | Mario Zechner (libGDX creator) | Mario Zechner (joined Earendil 2026-04-08) |
| License | MIT | **MIT** (preserved through the move) |
| Stars (page-stated §37.4) | 38,950 | **~85.4K** (2.2×) |
| Version (lockstep) | v0.69.0 | **v0.84.1** (2026-08-07); "minor = breaking, patch = fixes+additions, **no major releases**" |
| Primary lang | TypeScript 96.3% | TypeScript (biome + vitest + tsgo native-preview) |

**Independent confirmation of the move** (WebSearch, not relied on from the corpus pin alone): Armin Ronacher's own post *["Mario and Earendil"](https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/)* (2026-04-08), *[Pragmatic Engineer — "Building Pi, and what makes self-modifying software so fascinating"](https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying)*, *[implicator.ai — "Pi is not a Claude Code rival, it is a harness rebellion"](https://www.implicator.ai/pi-is-not-a-claude-code-rival-it-is-a-harness-rebellion/)*. The `earendil-works/pi` ↔ `badlogic/pi-mono` identity is further corroborated inside the corpus: **llm-space v221** (ByteDance DeerFlow team) is *built on `@earendil-works/pi-agent-core` and openly credits it* — a corpus record already noting "`earendil-works/pi` = `badlogic/pi-mono` = corpus subject v36."

**Criterion (a) — Anthropic / cultural-peer?** **FAIL, cleanly.** Earendil Inc. and Mario Zechner and Armin Ronacher are **not Anthropic**. Under routine **§41** (v2.7), "famous framework author" (Ronacher = Flask; Zechner = libGDX) is **explicitly not an (a)-rescue** — a notability inference is insufficient. First `earendil-works`-org subject → a **#19 19a** first-institution data-point. (No name/heritage/locale rescue is even attempted; the tier keys on (b) per §31.)

---

## 2. What Pi is (source-verified, `packages/coding-agent/README.md` @ `e47b8e3`)

> *"Pi is a minimal terminal coding harness. Adapt pi to your workflows, not the other way around, without having to fork and modify pi internals."*

- **Extend, don't fork:** four extension primitives — TypeScript **Extensions**, **Skills** (Claude-Code/Codex-compatible SKILL.md), **Prompt Templates**, **Themes** — bundled into shareable **Pi Packages** (npm/git).
- **Powerful defaults, deliberately spartan core:** default model tools are just **`read`, `write`, `edit`, `bash`** (v36 shipped 7; `grep/find/ls` still exist, e.g. `pi --tools read,grep,find,ls` read-only mode). "Pi ships with powerful defaults but **skips features like sub agents and plan mode**. Instead, you can ask pi to build what you want or install a third-party pi package."
- **Four run modes** (the client/server evolution surfaced to the user): **interactive** TUI · **print/JSON** (headless) · **RPC** (process integration) · **SDK** (embed pi in your own app).
- **Rich session model:** branching (`/tree`, `/fork`, `/clone`), compaction (`/compact`), export/import (HTML/JSONL), `/share` (private GitHub gist + shareable HTML), `/resume`, per-session cost/token/cache accounting in the footer.
- **Actively developed:** v0.84.x changelog (2026-08-06/07) adds fullscreen TUI, Mermaid + LaTeX transcript rendering, per-directory `AGENTS.override.md`, `pi auth check`, Qwen/Baseten providers — many via **external community PRs** (#7659, #7715, #7725, #7733…), so the contributor gate is letting real outside work through. PR numbers ~7700+ = very high volume.

---

## 3. The architecture delta (v36 monolith → v228 client/server runtime)

The v36 wiki documented a **7-package** monorepo (`pi-ai`, `pi-agent-core`, `pi-coding-agent`, `pi-mom`, `pi-pods`, `pi-tui`, `pi-web-ui`). The v228 clone shows a **~10-package** monorepo with a very different shape (source: `packages/`, root `package.json` @ `e47b8e3`):

| Package (`@earendil-works/*`) | v0.84.1 role | New since v36? |
|---|---|---|
| `pi-ai` | Unified multi-provider LLM API + **automatic model discovery** + a `pi-ai` CLI | present (grown to ~30+ providers) |
| `pi-agent-core` | General-purpose agent runtime — **transport abstraction**, state mgmt, attachments | present (gained transport abstraction) |
| `pi-coding-agent` | Interactive coding CLI (`pi`) — read/bash/edit/write + sessions | present (the flagship) |
| `pi-tui` | Terminal UI library, differential rendering | present |
| **`pi-protocol`** | **Transport-neutral CBOR protocol for *remote* pi sessions** | **NEW** |
| **`pi-client`** | Transport-neutral client for remote pi sessions (framed CBOR bytes) | **NEW** |
| **`pi-server`** | Experimental server package for pi | **NEW** |
| **`pi-session-backend-sqlite-node`** | Node SQLite **session backend** (pluggable persistence) | **NEW** |
| **`pi-evals`** | Built-in **evaluation harness** (`npm run eval`) | **NEW** |
| **`pi-telemetry`** | **Vendor-neutral telemetry contracts** + reference adapter + conformance tests + typed schemas | **NEW** |

**Dropped / spun-off since v36:** `pi-mom` (Slack bot) → now a separate repo **`earendil-works/pi-chat`**; `pi-pods` (GPU inference infra) → gone; `pi-web-ui` → gone (folded into client/tui). The monorepo **tightened around the coding-agent core** and grew a **distributed-runtime spine**.

**The headline technical shift = a remote-session client/server split.** Pi is no longer only a local monolith; `pi-protocol` defines a transport-neutral **CBOR** wire format, `pi-client` speaks it, `pi-server` (experimental) hosts it, and `pi-agent-core` now has a **transport abstraction** with pluggable **session backends**. This is the machinery that lets one drive a Pi session *remotely* and is the plausible substrate under Earendil's cloud platform (*Lefos*). It moves Pi from "a CLI" to "a **runtime you can embed, host, and drive over a wire**" (interactive / print-JSON / RPC / SDK).

**Also new:** a first-class **evals** package (author→run→measure discipline baked into the monorepo) and **vendor-neutral telemetry contracts** (typed schemas + conformance tests, provider-agnostic). Both map onto the vault's live prompt-eval and CC-observability/OTel threads.

---

## 4. Security posture + supply-chain hardening (the standout maturation)

**Supply-chain hardening** (README §"Supply-chain hardening" + root `package.json` scripts, source-verified — the single most disciplined supply-chain posture in the corpus):
- Direct external deps **pinned to exact versions**; internal workspace deps version-ranged.
- `.npmrc`: `save-exact=true` + **`min-release-age=2`** (refuse same-day dependency releases during resolution — a real, unusual defense against just-published malicious versions).
- `package-lock.json` is ground truth; **pre-commit blocks lockfile commits** unless `PI_ALLOW_LOCKFILE_CHANGE=1`.
- The published CLI ships **`npm-shrinkwrap.json`** (pins transitive deps for end users), generated from the root lockfile and `--check`-verified in `npm run check`.
- **`--ignore-scripts` everywhere** — documented installs, `pi update --self`, CI (`npm ci --ignore-scripts`); a scheduled GitHub workflow runs `npm audit --omit=dev` + `npm audit signatures`.
- Shrinkwrap has an **explicit allowlist for dependency lifecycle scripts**; a new lifecycle-script dep **fails checks until reviewed**.
- Release smoke tests build/pack into **isolated npm + Bun installs outside the repo** before tagging.

**Runtime security model** (`SECURITY.md`, verbatim posture): Pi **intentionally has no built-in sandbox or permission system** — it runs inside the user's trust boundary. The threat model is honest and narrow: files writable by the user (incl. `AGENTS.md`, skills, extensions, `~/.pi`) are *inside* the trust boundary, so **prompt injection and malicious trusted skills/extensions are explicitly out-of-scope** ("this cannot be protected against"). Containment is the user's job — the README documents **three patterns**:
- **Gondolin** — a local Linux **micro-VM**: keep `pi` + provider auth on the host, route built-in tools and `!` shell commands into the VM.
- **Plain Docker** — run the whole `pi` process in a container.
- **OpenShell** — run `pi` in a policy-controlled sandbox.

Notably, the dev dependencies include **`@anthropic-ai/sandbox-runtime`** (0.0.26) — Anthropic's sandbox runtime is used by the Gondolin example extension. So even the MCP-rejecting harness reaches for an Anthropic-published isolation primitive.

---

## 5. The two invariants that survived the move

**(a) Radical minimalism — "you don't need MCP."** Source-verified, `docs/usage.md`: *"It intentionally does not include built-in MCP, sub-agents, permission popups, plan mode, to-dos, or background bash."* `coding-agent/README.md:498`: **"No MCP.** Build CLI tools with READMEs (see Skills), or build an extension that adds MCP support. [Why?]"** linking Mario's essay *"what if you don't need MCP?"* (2025-11-02). At v36 this was logged as **"the first T1-scale MCP-exclusion counter-evidence"** with a watch-flag. At v228, at **~85K★**, it is now an explicit, philosophy-backed, blog-defended stance — the corpus's **strongest MCP-exclusion counter-pole**, standing directly against the vault's own MCP-heavy §C#23 code-graph family and B1-MCP running set. Pi's alternative primitive stack: **CLI-tools-with-READMEs + Skills + TypeScript extensions**.

**(b) The OSS-session-donation flywheel.** Still front-and-center: `badlogic/pi-share-hf` + the public HuggingFace dataset `badlogicgames/pi-mono` — *"Public OSS session data helps improve coding agents with real-world tasks… instead of toy benchmarks."* Mario keeps publishing his own work sessions. This is Pi's distinctive data-flywheel thesis (real traces > synthetic benchmarks), and it persists through the commercialization.

**Governance also persisted + hardened:** new-contributor issues/PRs **auto-close by default** (maintainers review daily); the corpus-first **`lgtm`/`lgtmi`** maintainer-approval keywords (Pattern #69 anchor) remain; `AGENTS.md` now adds **parallel-session git-safety rules** ("Multiple pi sessions may be running in this cwd at the same time… never `git add -A`/`git reset --hard`/`git stash`") — a multi-agent-safety governance addition; long-term plans live in **RFCs** at `rfc.earendil.com`.

---

## 6. Providers (pi-ai, source-verified) — ~30+, Claude first-class

Subscriptions: **Anthropic Claude Pro/Max**, OpenAI ChatGPT Plus/Pro (Codex), GitHub Copilot. API keys: **Anthropic**, Ant Ling, OpenAI, Azure OpenAI, DeepSeek, NVIDIA NIM, Google Gemini, Google Vertex, Amazon Bedrock, Mistral, Groq, Cerebras, Cloudflare AI Gateway/Workers AI, xAI, OpenRouter, Vercel AI Gateway, ZAI (Global + China), OpenCode Zen/Go, Hugging Face, Fireworks, Together AI, Baseten, Kimi For Coding, MiniMax, Xiaomi MiMo (+ regional token plans), Qwen Token Plan, plus **local**: llama.cpp router, and any OpenAI-compatible endpoint (Ollama/vLLM/LM Studio). Internally, providers share wire implementations (`anthropic-messages`, `openai-responses`, `openai-completions`); **automatic model discovery** refreshes catalogs (`models.generated.ts` from `generate-models`). Claude is a first-class citizen (subscription + API key + the `anthropic-messages` protocol reused by Kimi/Fireworks) — this is the multi-provider escape-hatch the v36 pilot flagged, now broader (~20+ → ~30+).

---

## 7. Corpus placement

- **Tier:** coding-agent-**product** — the same class as **Kilo Code v177 / grok-build v215 / openinterpreter v223 / larksuite-cli v143 / CodePilot v161 / OpenHands v30** (and AutoGPT). Pi is the **OG open minimalist harness of this cluster**, predating every one of those coding-agent-product §C entries (it was v36). v36 labeled it **T1 "Agent-as-assistant"**; the corpus has since evolved a "coding-agent-products" cluster (flagged to the overdue ~v221 audit). Tier reconciliation is an **audit** item — not decided unilaterally here.
- **Corpus-recursive links:** **llm-space v221 is built on `pi-agent-core` and credits it (a #57 downstream dependency)**; Pi is a *cited/supported harness* across **cc-switch v73, open-design v83, i-have-adhd v225, openinterpreter v223**, the **harness-engineering** flagship, and the **adaptive-engineering-beyond-harness** memory (Rajiv Chandegra cites Pi as "minimal + extensible"). **devspace v171** (§C "self-hosted MCP bridge that turns a hosted chat host into a local coding agent") is the remote-session cousin — but the *opposite* MCP stance.
- **Pattern threads touched:** #18 (MCP-exclusion, now strongest in corpus), #66 (supply-chain — a rare *positive* exemplar), #69 (`lgtm`/`lgtmi` maintainer-gate, its anchor), #28/#84 (multi-provider ~30+ + auto-discovery), #17/#20/#27 (solo-flagship → open-core-company trajectory).

*(Verdict, pattern outcome, and the mint-declined reasoning are in the companion `(C) v228 Revisit — Verdict + Pattern Outcome.md`. The application menu is in `(C) v228 Revisit — Pilot Methods Menu.md`.)*

---

*(C) Claude-generated 2026-08-08 under routine v2.7 — v228 corpus-recursive REVISIT of v36 pi-mono. Source-verified at `earendil-works/pi@e47b8e3`. §37.4: star counts are page-stated (GitHub API mocked in this environment) → NOT a Pattern #52 velocity claim.*
