# (C) ollama — Architecture + 38-subdir cluster summary

> **Source cluster 2 of 3.** Maps the 38-subdir Go monorepo, dual-API-compat layer implementation, inference-pipeline decomposition, Modelfile + model-registry mechanics, and `cmd/launch/` 33-file runtime-bundled-agent-launcher primitive. Citation-not-replication applied per Phase 0.9 RED primitive-count compression.

---

## 1. Monorepo layout (38 top-level subdirs)

**Entry point:**
- `main.go` (180 bytes) — minimal Cobra wrapper calling `cmd.NewCLI().ExecuteContext`

**Build tooling:**
- `CMakeLists.txt` (15.2 KB) — C++ build config for native runtime (MLX + llama.cpp compilation pipelines)
- `CMakePresets.json` (4.9 KB) — build-preset configurations
- `Dockerfile` (9.8 KB) — official container image build
- `Makefile.sync` (2.6 KB) — llama.cpp upstream sync automation
- `go.mod` + `go.sum` (42.7 KB) — Go module dependency graph
- `.golangci.yaml` (1.1 KB) — Go-specific lint discipline

**Version pinning (CORPUS-FIRST):**
- `MLX_VERSION` (41 B) — pinned Apple MLX commit SHA
- `MLX_C_VERSION` (41 B) — pinned MLX-C commit SHA

MLX vendored pins are first observed in Storm Bear corpus — runtime pins native-inference-library versions outside Go module system because the native libraries compile through CMake, not `go mod`.

**38 top-level subdirectories:**

| Subdir | Role | File count signal |
|--------|------|-------------------|
| `anthropic/` | Anthropic-compat API layer | 3 files ~83 KB |
| `api/` | Native REST API types + client | 6 files |
| `app/` | Desktop-app GUI wrapper (macOS tray / Windows tray) | — |
| `auth/` | Registry authentication | — |
| `cmd/` | CLI root + launchers + internal | 14 files + 6 subdirs |
| `convert/` | Model format conversion (HuggingFace → Ollama) | — |
| `discover/` | GPU discovery + hardware probe | — |
| `docs/` | User-facing documentation | 27 files + 5 subdirs |
| `envconfig/` | Environment-variable config parsing | — |
| `format/` | Output formatting utilities | — |
| `fs/` | Filesystem + GGUF file handling | — |
| `harmony/` | Harmony chat-template parser (new OpenAI response format?) | 2 files 33 KB |
| `integration/` | Integration tests | — |
| `internal/` | Internal implementation packages | — |
| `kvcache/` | KV cache management | — |
| `llama/` | **llama.cpp upstream integration + bindings** | — |
| `llm/` | Higher-level LLM abstractions | — |
| `logutil/` | Structured logging | — |
| `manifest/` | Model manifest parser (OCI-like model registry artifact format) | — |
| `middleware/` | HTTP middleware (auth, logging) | — |
| `ml/` | Lower-level ML primitives | — |
| `model/` | Model metadata types | — |
| `openai/` | OpenAI-compat API layer | 5 files ~158 KB |
| `parser/` | **Modelfile parser** | — |
| `progress/` | Progress-bar utilities | — |
| `readline/` | Interactive REPL readline | — |
| `runner/` | **Inference runner (per-model subprocess)** | — |
| `sample/` | Sampling strategies (temperature, top_p, top_k, etc.) | — |
| `scripts/` | Build/release scripts | — |
| `server/` | **Core server + HTTP routes + model management** | 29+ files |
| `template/` | **Go template renderer (Modelfile prompt templates)** | — |
| `thinking/` | Chain-of-thought parser | 4 files 19 KB |
| `tokenizer/` | Tokenizer implementation | — |
| `tools/` | **Tool-use (function calling) parser** | 4 files 48 KB |
| `types/` | Cross-cutting type definitions | — |
| `version/` | Version strings | — |
| `x/` | Experimental packages (Go convention) | — |

Total: 38 top-level subdirs + ~15 sub-subdirs = **50+ distinct architectural zones**. Far exceeds browser-use v41 (17 subdirs, RED inaugural) and approaches ruflo v42 (EXTREME ~500+ primitives) territory but at lower primitive-granularity because Go-monorepo organizes by architectural layer rather than by user-facing primitive.

## 2. `cmd/launch/` — runtime-bundled-agent-launcher implementation

**Most-structurally-novel subdir in corpus at v46.** 33 files implementing 10+ `ollama launch <runtime>` commands.

**Core orchestration:**
- `launch.go` (29.2 KB) — shared launch infrastructure
- `launch_test.go` (76.1 KB) — heaviest test file in corpus observed at v46 (3× typical)
- `models.go` (14.8 KB) — model-selector flow
- `registry.go` (11.5 KB) — runtime registry + metadata
- `selector_hooks.go` (3.4 KB) — runtime-selector UI hooks

**Runtime launchers (per-file):**

| File | Size | Runtime | Integration docs lines |
|------|------|---------|------------------------|
| `openclaw.go` | 27.4 KB | OpenClaw (WhatsApp/Telegram/Slack/Discord/iMessage AI assistant) | 96 lines |
| `vscode.go` | 16.8 KB | Visual Studio Code | — |
| `hermes.go` | 16.4 KB | Hermes Agent | — |
| `pi.go` | 10.2 KB | **Pi (pi-mono v36 Mario Zechner)** | 110 lines |
| `kimi.go` | 8.5 KB | Kimi (Moonshot) | — |
| `opencode.go` | 6.2 KB | OpenCode | — |
| `droid.go` | 5.0 KB | Factory.ai Droid | — |
| `codex.go` | 3.6 KB | OpenAI Codex CLI | — |
| `cline.go` | 2.3 KB | Cline (VS Code extension) | — |
| `claude.go` | 1.9 KB | **Claude Code** | 136 lines |
| `copilot.go` | 1.7 KB | GitHub Copilot CLI | — |

**Observed launcher-size ranking:** OpenClaw (27.4 KB) + VS Code (16.8 KB) + Hermes (16.4 KB) + Pi (10.2 KB) are heaviest; Claude (1.9 KB) + Copilot (1.7 KB) lightest.

**Launcher heaviness signal:** Heavy launchers do **provisioning + configuration + daemon-management + model-pull + onboarding-UI**; light launchers do **config-injection only** (e.g., Claude Code = just setting `ANTHROPIC_BASE_URL` + launching `claude --model <ollama-model>`).

**Pattern #18 Layer 0 observation — runtime-bundled-agent-launcher primitive:**

Ollama adds a new layer below Pattern #18's existing 3-layer taxonomy (from v42 formulation):
- **Layer 0 NEW — runtime-bundled-launcher:** `ollama launch <runtime>` orchestrates install + config + connection across 10+ agent runtimes (Ollama v46 first observation at infrastructure-runtime scale)
- Layer 1 MCP universal (OpenClaw + Hermes community-platform-scoped per v36 pi-mono refinement + ollama-MCP-Tier-1 per shannon v45)
- Layer 2 community-platform-scoped
- Layer 3 per-runtime

## 3. Dual API-compatibility layer deep-dive

**`openai/` subdir:**

| File | Size | Role |
|------|------|------|
| `openai.go` | 26.2 KB | OpenAI Chat Completions API endpoints (`/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/models`) |
| `responses.go` | 41.1 KB | OpenAI Responses API (newer message-based format, 2026-era) |
| `openai_test.go` | 21.3 KB | OpenAI-compat unit tests |
| `responses_test.go` | 65.7 KB | OpenAI Responses unit tests |
| `openai_encoding_format_test.go` | 3.9 KB | Encoding-format compat tests |

**`anthropic/` subdir:**

| File | Size | Role |
|------|------|------|
| `anthropic.go` | 31.9 KB | Anthropic Messages API endpoints (`/v1/messages`) |
| `anthropic_test.go` | 42.7 KB | Anthropic-compat unit tests |
| `trace.go` | 9.3 KB | Tracing / observability hooks |

**Integration points:**

- **OpenAI-compat** — any OpenAI-SDK consumer (LiteLLM, LangChain, LlamaIndex, etc.) sets `base_url: http://localhost:11434/v1` + model name → routes through `openai/` → routes to internal ollama chat pipeline
- **Anthropic-compat** — Claude Code sets `ANTHROPIC_BASE_URL=http://localhost:11434` → routes through `anthropic/` → routes to internal ollama chat pipeline

**Recent development (visible in `git log -n 10`):**

```
openai: map responses reasoning effort to think (#15789)
```

This commit maps OpenAI's `reasoning.effort` parameter to Ollama's internal `think` system-prompt mechanism — demonstrates ongoing active work to keep OpenAI-compat parity with upstream OpenAI API evolution.

**Pattern #28 inversion sub-observation:** Ollama implements 2 vendor-compat layers in parallel. OpenAI layer serves the vast Pattern-#28-prior-consumer ecosystem (LiteLLM + LangChain + ~20 other library/SDK wikis). Anthropic layer serves Claude Code specifically + any future Anthropic-SDK consumers. **Multi-API-compat-as-runtime** = corpus-first structural choice.

## 4. Inference pipeline decomposition

**4 subdirs span inference stack:**

| Subdir | Approximate role | Relation |
|--------|------------------|----------|
| `llama/` | llama.cpp upstream integration + CGO bindings + MLX backend | Lowest-level native integration |
| `runner/` | Per-model subprocess runner (spawned per loaded model) | Process-isolation layer |
| `ml/` | Low-level ML primitives (tensor ops, quantization helpers) | Utility layer |
| `llm/` | Higher-level LLM abstractions (chat + generate + embeddings) | API-facing layer |

**Key supporting subdirs:**

- `harmony/` (16.7 KB parser + 17.1 KB tests) — Harmony chat template format. gpt-oss family (OpenAI OSS models) uses Harmony format for messages + tool calls + channels (analysis/commentary/final).
- `thinking/` (5.4 KB parser + 6.7 KB tests + 3.4 KB template + 3.1 KB test) — chain-of-thought parser for reasoning models (DeepSeek R1, Qwen3-thinking, etc.)
- `tools/` (8.0 KB tools.go + 32.5 KB tests + 3.6 KB template + 4.2 KB test) — tool-use / function-calling parser
- `sample/` — sampling strategies (temperature, top_p, top_k, min_p, typical_p, etc.)
- `tokenizer/` — tokenizer loader + apply
- `kvcache/` — KV cache management across requests
- `discover/` — GPU/accelerator discovery (CUDA, ROCm, Metal, MLX)

**Multi-backend observation:** Ollama supports multiple inference backends natively:
- **llama.cpp** (CPU + CUDA + ROCm + Metal) — cross-platform default
- **MLX** (Apple Silicon native) — via MLX_VERSION + MLX_C_VERSION pinning + CMake build

This is corpus-first explicit multi-backend-inference-runtime observation (contrast fish-speech v20 which used SGLang single-backend; LlamaFactory v22 + Unsloth v23 training-infra had multiple training-backend choices but not inference-backend at runtime).

## 5. Modelfile format + model registry

**`parser/` subdir** — Modelfile parser (Dockerfile-inspired declarative format).

**docs/modelfile.mdx (12.8 KB)** documents Modelfile commands:

- `FROM <model>` — base model (e.g., `FROM llama3.2`, `FROM ./my-quantization.gguf`)
- `PARAMETER <name> <value>` — inference parameters (temperature, top_p, num_ctx, stop, etc.)
- `TEMPLATE "..."` — Go-template prompt format (uses `template/` subdir)
- `SYSTEM "..."` — default system message
- `ADAPTER <path>` — LoRA adapter
- `LICENSE "..."` — license text embedded in model
- `MESSAGE <role> "..."` — few-shot examples

Example (docs/modelfile.mdx):
```modelfile
FROM llama3.2

PARAMETER temperature 0.7
PARAMETER num_ctx 65536

SYSTEM "You are a helpful assistant specialized in Vietnamese language."
```

**Model registry (`manifest/` + `auth/` + `server/download.go` + `server/cloud_proxy.go`):**

- Ollama uses OCI-like manifest format for model distribution
- `ollama pull <model>` / `ollama push <model>` against ollama.com/library
- `manifest/` parses manifests; `auth/` handles registry authentication; `server/download.go` (11.6 KB) handles the download pipeline
- `server/cloud_proxy.go` (14.5 KB) — **transparent proxy layer** routing `:cloud` suffix model requests to Ollama Cloud servers

**Modelfile is corpus-first declarative-model-packaging format observation at outside-scope runtime archetype.** Distinct from Dockerfile (containerizes arbitrary OS userspace) or HuggingFace safetensors (raw weight format without packaging metadata) — Modelfile bundles weights + template + default params + system prompt + optional LoRA adapter.

## 6. `server/` — HTTP routes + model lifecycle

**`server/routes.go` = 78.5 KB** (largest single file in repo outside test files)

Key files in `server/`:

| File | Size | Role |
|------|------|------|
| `routes.go` | 78.5 KB | All HTTP route handlers + orchestration |
| `routes_generate_test.go` | 76.8 KB | Generate route tests |
| `routes_create_test.go` | 38.7 KB | Create model tests |
| `routes_cloud_test.go` | 33.0 KB | Cloud proxy tests |
| `quantization_test.go` | 28.3 KB | Quantization tests |
| `images.go` | 26.9 KB | Image-model handling (multimodal) |
| `create.go` | 22.0 KB | Model creation from Modelfile |
| `cloud_proxy.go` | 14.5 KB | Ollama Cloud tier proxy routing |
| `routes_debug_test.go` | 12.9 KB | Debug routes tests |
| `prompt_test.go` | 12.8 KB | Prompt-template tests |
| `images_test.go` | 11.8 KB | Image-model tests |
| `download.go` | 11.6 KB | Model-download pipeline |
| `quantization.go` | 11.1 KB | Quantization engine |
| `cloud_proxy_test.go` | 9.7 KB | Cloud proxy tests |

**Observations:**
- `routes.go` single-file architecture (78.5 KB) — not micro-module decomposition. Fits commercial-runtime-infrastructure pragmatic code style.
- Quantization engine (11.1 KB + 28.3 KB tests) — corpus-first explicit quantization as server-side capability (contrast training-infra wikis v22/v23 which do quantization at training time).
- Cloud proxy (14.5 KB + 9.7 KB + 33.0 KB routes tests) — proves Ollama Cloud is a transparent-proxy architecture (same CLI commands work local + cloud via `:cloud` suffix) rather than separate-API architecture.

## 7. REST API + SDK + integration documentation surface

**Native REST API (docs/api.md 54.8 KB + docs/openapi.yaml 56.2 KB):**

- 13+ endpoints enumerated in README cluster
- OpenAPI YAML schema = 56.2 KB (large, rigorous API contract)

**SDK ecosystem:**

- `ollama/ollama-python` (README line 43) — official Python SDK
- `ollama/ollama-js` (README line 44) — official JS SDK

**docs/integrations/ (20 files)** — dedicated integration docs per consumer runtime. Cluster summary 1 enumerated all 20.

## 8. Governance discipline (Pattern #12 refined)

**3 governance files:**

- `README.md` (18.7 KB) — user-facing + 60% community-integrations directory
- `CONTRIBUTING.md` (3.6 KB) — contributor discipline (see below)
- `SECURITY.md` (1003 B) — vulnerability reporting (email hello@ollama.com)

**CONTRIBUTING.md notable claims (lines 22-25):**

> **"Issues that may not be accepted"**
> - Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API)
> - Changes that add significant friction to the user experience
> - Changes that create a large future maintenance burden for maintainers and contributors

Plus "New features: new features (e.g. API fields, environment variables) add surface area to Ollama and make it harder to maintain in the long run as they cannot be removed without potentially breaking users in the future." — **explicit anti-feature-expansion discipline.**

**Commit message discipline** (CONTRIBUTING lines 52-74):

```
<package>: <short description>
```

Lowercase continuation of "This changes Ollama to...". Examples:
```
llm/backend/mlx: support the llama architecture
CONTRIBUTING: provide clarity on good commit messages, and bad
```

Bad examples explicitly called out: `feat: add more emoji`, `fix: was not using famous web framework`, `chore: generify code` — **rejects conventional-commits emoji/type prefixes in favor of package-affects prefix.**

**`.golangci.yaml` (1.1 KB)** — Go-native lint discipline.

**Pattern #12 Governance-Depth refined 3-factor formulation fit:**
- Maturity-ambition: HIGH (backwards-compat + anti-feature-expansion discipline)
- Maintainer-philosophy: commercial-runtime-infrastructure-stability
- Scale-tier: X-large (170K stars)

Medium-weight governance at X-large scale with strong discipline-focus > standard-commercial-startup-governance-depth. Reinforces v42 3-factor refinement (was "solo-vs-corporate predicts governance-depth" pre-refinement; now correctly "maturity-ambition + maintainer-philosophy + scale-tier").

## 9. Test discipline signal

Test files observed:

| Test file | Size | Signal |
|-----------|------|--------|
| `cmd/launch/openclaw_test.go` | 86.1 KB | Heaviest test in corpus |
| `cmd/launch/launch_test.go` | 76.1 KB | 2nd heaviest |
| `cmd/launch/integrations_test.go` | 50.5 KB | 3rd heaviest |
| `cmd/launch/droid_test.go` | 35.6 KB | 4th |
| `cmd/launch/pi_test.go` | 35.2 KB | 5th |
| `server/routes_generate_test.go` | 76.8 KB | — |
| `server/routes_create_test.go` | 38.7 KB | — |
| `server/routes_cloud_test.go` | 33.0 KB | — |
| `openai/responses_test.go` | 65.7 KB | — |
| `anthropic/anthropic_test.go` | 42.7 KB | — |

**Test-to-code ratio for launchers:** 86.1 KB test / 27.4 KB code for OpenClaw = **3.1:1 test:code ratio** — unusually high. Signals commercial-runtime-infrastructure-stability priority (breakage in launcher = production breakage for 10+ downstream agent runtimes).

## 10. Pattern delta from this cluster

| Pattern | Delta |
|---------|-------|
| #2 Distribution Evolution | 38-subdir Go monorepo + CMake native build + MLX vendored pins observation |
| #12 Governance-Depth (refined 3-factor) | **Commercial-runtime-infrastructure-stability** discipline explicitly codified (anti-feature-expansion + backwards-compat + package-prefixed commits + .golangci.yaml lint); reinforces 3-factor refinement |
| #17 variant 3 commercial-startup | Ollama, Inc. as ecosystem-layer runtime-infrastructure; data point |
| #18 Agent Runtime Standardization | **Layer 0 runtime-bundled-launcher** observation (potential formulation extension to 4-layer taxonomy at next audit); 33-file cmd/launch/ at 170K-scale = infrastructure-level implementation |
| #19 archetype 4 tool-lineage | llama.cpp + Georgi Gerganov credit only; fits |
| #22 AGENTS.md | Absent (outside-scope runtime archetype) |
| #28 Multi-Provider AI Support | **STRUCTURAL INVERSION** observation — provider-being-consumed + multi-API-compat-as-runtime; dual-compat implementation (openai/ + anthropic/) detailed |
| #31 Open-Core Commercial Entity | N=9 strengthening; Pro-docs-depth 3/4; cloud_proxy.go + :cloud suffix + transparent proxy architecture |
| #47 Vision-Based Browser Automation | **CONDITIONAL RETIREMENT TRIGGER FIRES** (scope-distinct confirmation at v46) |
| #50 Commercial-Funnel Companion | N=8 strengthening |
| #57 Recursive Corpus Reference | 3rd data point; compound-2-wiki sub-variant |

## 11. Corpus-firsts enumerated from this cluster

1. **MLX_VERSION + MLX_C_VERSION vendored commit-SHA pins** outside Go module — dual-inference-backend-build-discipline observation
2. **`cmd/launch/` 33-file runtime-bundled-agent-launcher subsystem** — Pattern #18 Layer 0 primitive
3. **Dual API-compat subdirs (openai/ + anthropic/) simultaneously** implementing 2 vendor APIs
4. **Test-to-code ratio 3:1 for runtime launchers** — commercial-runtime-infrastructure-stability signal
5. **78.5 KB single-file `server/routes.go`** — pragmatic routes-consolidation at X-large scale (contrast micro-module decomposition in framework wikis)
6. **Modelfile declarative format** — corpus-first model-packaging format at runtime archetype (parser/ + template/ subdirs)
7. **OCI-like manifest model registry** — corpus-first commercial-runtime model distribution architecture (ollama.com/library)
8. **Transparent local-cloud proxy architecture** (server/cloud_proxy.go + `:cloud` suffix) — zero-code-change commercial upsell pathway
9. **Harmony chat template parser subdir** (harmony/) — corpus-first dedicated parser for gpt-oss family Harmony format
10. **Explicit anti-feature-expansion CONTRIBUTING discipline** at 170K stars — commercial-runtime-infrastructure-stability governance
