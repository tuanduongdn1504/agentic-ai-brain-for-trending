# (C) Entity: Core product — ollama runtime + Modelfile

> **Entity 1 of 4.** Canonical 13-section entity page for the core product: ollama CLI + REST API + Modelfile format + model registry + 10+ `ollama launch <runtime>` bundled agent runtimes.

---

## 1. Identity

- **Name:** ollama (lowercase; package `ollama/ollama`)
- **GitHub:** github.com/ollama/ollama
- **Latest version:** v0.21.2 (2026-04-23)
- **License:** MIT
- **Primary language:** Go 64.7% + C 28.8% (llama.cpp) + TypeScript 3.5% + C++ 1.1%
- **Scope tier:** OUTSIDE-SCOPE — LLM-inference-runtime 9th sub-type (NEW at v46)
- **Scale:** 170K stars / 15.8K forks / 955 watchers / 2.2K open issues / 5,344 commits (X-large; largest non-aggregator OSS in Storm Bear corpus)

## 2. Tagline / positioning verbatim

> **"Start building with open models."**
>
> **GitHub desc:** "Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models."
>
> **ollama.com:** "the easiest way to build with open models"

## 3. What it does

Ollama is an **LLM inference runtime** that installs as a native binary on macOS / Windows / Linux / Docker + runs a local daemon on `http://localhost:11434` that serves open-weight LLMs via:

- **Native REST API** (13+ endpoints: /api/generate, /api/chat, /api/pull, /api/embeddings, etc.)
- **OpenAI-compatible API** (via `openai/` subdir; base URL `http://localhost:11434/v1`)
- **Anthropic-compatible API** (via `anthropic/` subdir; base URL `http://localhost:11434`)
- **Language SDKs** — official Python (`pip install ollama`) + JavaScript (`npm i ollama`) + 30+ community-maintained SDKs

**Plus:**
- Transparent local-cloud split via `:cloud` suffix (e.g., `ollama run kimi-k2.5:cloud`) — Ollama Cloud tier
- Modelfile declarative format for custom model packaging (weights + template + system prompt + params + LoRA adapter)
- OCI-like model registry at `ollama.com/library`
- **`ollama launch <runtime>` one-command bundled agent runtime installer + configurator** for 10+ coding agents / personal AI assistants / IDEs

## 4. Core primitives (RED primitive-count tier; citation-not-replication)

**CLI surface** (`cmd/cmd.go` 62.2 KB + `cmd/interactive.go` 21.4 KB; citation-not-replication applied):

- `ollama` (interactive REPL)
- `ollama run <model>` (chat with model)
- `ollama pull <model>` (pull from registry)
- `ollama push <model>` (push to registry)
- `ollama create <model> -f Modelfile` (create from Modelfile)
- `ollama list` / `ollama show` / `ollama rm` / `ollama cp` (model management)
- `ollama ps` (list running models)
- `ollama serve` (explicit server mode)
- `ollama signin` (Ollama Cloud auth)
- `ollama launch <runtime>` (runtime-bundled-agent-launcher; 10+ runtimes)
- Full CLI reference: docs.ollama.com/cli (cited, not enumerated)

**REST API endpoints** (docs/api.md 54.8 KB + openapi.yaml 56.2 KB; citation-not-replication):

- POST /api/generate / /api/chat / /api/embeddings
- POST /api/create / /api/pull / /api/push / /api/copy / DELETE /api/delete
- GET /api/tags / POST /api/show / GET /api/ps / GET /api/version
- POST /api/image-generation (experimental)

**Modelfile commands** (docs/modelfile.mdx 12.8 KB; citation-not-replication):

- `FROM` / `PARAMETER` / `TEMPLATE` / `SYSTEM` / `ADAPTER` / `LICENSE` / `MESSAGE`

**10+ bundled `ollama launch` runtimes** (cmd/launch/ 33 files):

Coding agents: Claude Code / Codex / Copilot CLI / OpenCode / Droid / Goose / **Pi (pi-mono v36)**
AI assistants: OpenClaw / Hermes
IDEs: VS Code / Cline

**Inference pipeline** (llama/ + runner/ + ml/ + llm/ subdirs):

Multi-backend:
- **llama.cpp** (CPU + CUDA + ROCm + Metal) via CGO bindings
- **MLX** (Apple Silicon native) via CMake + MLX_VERSION/MLX_C_VERSION pinned commit SHAs

**Supporting primitives:**
- `harmony/` — Harmony chat-template parser (gpt-oss family)
- `thinking/` — chain-of-thought parser (DeepSeek R1 / Qwen3-thinking)
- `tools/` — tool-use / function-calling parser
- `sample/` — sampling strategies
- `tokenizer/` + `kvcache/` + `convert/` + `quantization` (server/quantization.go 11.1 KB)

## 5. Distribution surface

**5 official install channels:**
- macOS: `curl -fsSL https://ollama.com/install.sh | sh` OR Ollama.dmg manual
- Windows: `irm https://ollama.com/install.ps1 | iex` OR OllamaSetup.exe manual
- Linux: `curl -fsSL https://ollama.com/install.sh | sh`
- Docker: `ollama/ollama` on Docker Hub
- Package managers: Pacman, Homebrew, Nix, Helm Chart, Gentoo, Flox, Guix

**Language SDKs:**
- `pip install ollama` (official Python)
- `npm i ollama` (official JS)
- 30+ community SDKs (README Libraries & SDKs section)

**Total: 13+ distribution surfaces at 170K-scale.** Pattern #2 corpus-first multi-OS-native-binary-at-infrastructure-scale observation.

## 6. Model registry

**ollama.com/library** — curated model registry with OCI-like manifest format.

Featured models (README §3 Get started):
- `gemma3` (Google Gemma 3)
- Additional families documented in GitHub description: Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen

**Cloud models** (ollama.com/search?c=cloud) — accessible via `:cloud` suffix:
- `kimi-k2.5:cloud`
- `glm-5:cloud` / `glm-5.1:cloud` / `glm-4.7-flash`
- `qwen3.5:cloud` / `qwen3.5`
- `minimax-m2.7:cloud`

**Custom models:** any GGUF file (llama.cpp format) + Modelfile → `ollama create my-model -f Modelfile`.

## 7. Architecture

**38 top-level subdirs + 6 cmd/ sub-subdirs + 5 docs/ sub-subdirs = 50+ architectural zones.**

Detailed in Cluster 2 (`(C) Architecture + 38-subdir cluster summary.md`). Summary:

- **API surface:** `api/` (native types + client) + `openai/` (OpenAI-compat) + `anthropic/` (Anthropic-compat) + `server/routes.go` 78.5KB (HTTP routes)
- **Inference:** `llama/` (llama.cpp integration) + `ml/` + `llm/` + `runner/` (4-subdir pipeline) + `harmony/` + `thinking/` + `tools/` (chat-format parsers)
- **Model lifecycle:** `parser/` (Modelfile) + `template/` (Go templates) + `convert/` (format conversion) + `manifest/` (OCI-like manifest) + `auth/` + `server/download.go` + `server/cloud_proxy.go` 14.5KB
- **CLI + launchers:** `cmd/` (main CLI) + `cmd/launch/` (33-file runtime-bundled-agent-launcher subsystem — Pattern #18 Layer 0 novel implementation)
- **Infrastructure:** `app/` (GUI tray) + `discover/` (GPU probe) + `envconfig/` + `kvcache/` + `fs/` + `format/` + `progress/` + `readline/` + `middleware/`

**Native build:** `CMakeLists.txt` 15.2 KB + `CMakePresets.json` 4.9 KB + vendored MLX_VERSION + MLX_C_VERSION commit-SHA pins outside Go module system.

## 8. Governance

- LICENSE MIT
- CONTRIBUTING.md 3.6 KB — **explicit anti-feature-expansion + backwards-compat discipline** (verbatim: "Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API) [may not be accepted]")
- SECURITY.md 1003 B — hello@ollama.com
- .golangci.yaml — Go-native lint discipline

**Absent:** AGENTS.md / CLAUDE.md / CODE_OF_CONDUCT / MAINTAINERS / GOVERNANCE / CITATION.cff.

Pattern #12 refined 3-factor formulation fit: HIGH maturity-ambition + commercial-runtime-infrastructure-stability maintainer-philosophy + X-large scale → medium-light governance with strong discipline-focus.

## 9. Commercial tier

**Ollama Cloud (docs/cloud.mdx 4.4 KB):**

| Tier | Price | Description |
|------|-------|------|
| Free | $0 | Basic cloud + local runtime |
| **Pro** | **$20/mo** or $200/yr | 3 cloud models simultaneous + 50× cloud usage vs Free |
| **Max** | **$100/mo** | 10 cloud models simultaneous + 5× usage vs Pro |

**Transparent local-cloud-split architecture** — same CLI / REST API / SDK work against local models OR `:cloud` suffix models (cloud_proxy.go 14.5 KB implements routing).

**Pattern #31 Open-Core Commercial Entity N=9 strengthening** — Ollama joins 8 prior commercial-entity open-core wikis. Pro-docs-depth 3/4 per v45 formalization.

## 10. Community

- Discord: discord.gg/ollama
- X (Twitter): @ollama
- Reddit: r/ollama
- Docker Hub: hub.docker.com/r/ollama/ollama
- Contact: hello@ollama.com

**130+ community integrations** documented in README (13 sub-categories; chat interfaces + desktop clients + code editors + libraries + frameworks + RAG + bots + CLI + productivity + observability + DB + infrastructure + mobile).

## 11. Novel observations (corpus-firsts)

1. **9th outside-scope sub-type: LLM-inference-runtime** (formal definition in Phase 4b deliverable)
2. **170K stars** = largest non-aggregator OSS in Storm Bear corpus
3. **Dual API-compat subdirs** (`openai/` + `anthropic/`) implementing 2 vendor APIs simultaneously — Pattern #28 structural inversion
4. **`ollama launch <runtime>` runtime-bundled-agent-launcher primitive** — Pattern #18 Layer 0 observation; 33 files in cmd/launch/ at infrastructure scale
5. **MLX_VERSION + MLX_C_VERSION vendored commit-SHA pins** outside Go module system — dual-inference-backend (llama.cpp + MLX) build discipline
6. **Transparent local-cloud proxy architecture** via `:cloud` suffix + cloud_proxy.go — zero-code-change commercial upsell
7. **Modelfile declarative format** — corpus-first model-packaging format at runtime archetype
8. **OCI-like manifest model registry** (ollama.com/library) — corpus-first commercial-runtime model distribution
9. **Pattern #57 Recursive Corpus Reference 3rd data point with compound-2-wiki sub-variant** — Pi integration doc cites pi-mono v36 + Karpathy autoresearch v10 in single doc
10. **Pattern #12 commercial-runtime-infrastructure-stability discipline** — explicit anti-feature-expansion governance at 170K stars

## 12. Storm Bear pilot relevance (LOW-MEDIUM)

**Direct pilot candidates:**
- **Privacy pilot** — run Llama 3 or Qwen3-coder locally for Scrum coaching workflows that touch VN client data (no API sending to Anthropic/OpenAI)
- **Cost-optimization pilot** — Ollama local free after hardware vs Claude API $$ for high-volume Scrum workloads; Ollama Cloud Pro $20/mo if GPU hardware insufficient
- **Claude Code integration pilot** — `ollama launch claude --model qwen3.5` lets Claude Code binary use local/cloud open models via Anthropic-compat (no Anthropic API key needed)

**Caveats:**
- 170K-star non-Scrum-specific tool; Storm Bear markdown-vault + Scrum-coach workflow doesn't critically depend on local-LLM infrastructure
- Requires 64GB+ RAM for 30B+ models locally (8GB+ for 7B models)
- EN-only docs (no VN localization)
- Integration overhead: Ollama is not Scrum-purpose-built; operator handles prompt engineering / context management

**Pilot ranking: LOW-MEDIUM (not in top-11 priority).** Storm Bear operator uses Claude API primarily; Ollama observational-and-optional-pilot if privacy-sensitive client engagement arrives.

**Observational value HIGH:**
- LLM-inference-runtime 9th outside-scope sub-type reference
- Pattern #47 conditional retirement trigger FIRES milestone
- Pattern #18 Layer 0 runtime-bundled-launcher observation
- Pattern #28 structural inversion reference
- Pattern #57 3rd data point + compound-cross-corpus-citation sub-variant
- Commercial-runtime-infrastructure-stability archetype as governance benchmark

## 13. Cross-references

**Sibling wikis:**
- v8 build-your-own-x (1st outside-scope)
- v20 fish-speech (foundation-model; produces weights ollama consumes)
- v22 LlamaFactory + v23 Unsloth (training-infra; trains weights ollama runs)
- v37 bizos (7th outside-scope sub-type)
- v44 magika (8th outside-scope sub-type; most-recent precedent)
- v10 autoresearch (Karpathy; cited by Ollama Pi integration docs verbatim)
- v36 pi-mono (Mario Zechner; cited by Ollama Pi integration docs as first-class bundled runtime)
- v41 browser-use (Pattern #47 conditional-retirement-trigger predecessor; first RED primitive-count precedent)
- v42 ruflo (EXTREME primitive-count precedent)
- v45 shannon (Pattern #31 N=8 + #50 N=7 immediate predecessor)

**Pattern Library:**
- PATTERN_LIBRARY.md entries:
  - Pattern #47 (conditional retirement FIRES)
  - Pattern #17 variant 3 (strengthening data point)
  - Pattern #18 (Layer 0 observation; potential formulation extension)
  - Pattern #28 (structural inversion observation)
  - Pattern #31 (N=9 strengthening)
  - Pattern #50 (N=8 strengthening)
  - Pattern #57 (3rd data point + compound sub-variant)
  - Outside-scope 9th sub-type catalog entry

**Other entities in this wiki:**
- `(C) Commercial ecosystem + Pattern 31 N9 + Pattern 50 N8.md` — commercial details
- `(C) Outside-scope 9th sub-type + Pattern 47 retirement fires + Pattern 28 inversion.md` — pattern implications
- `(C) Storm Bear meta — 35th consecutive.md` — vault-level observations
