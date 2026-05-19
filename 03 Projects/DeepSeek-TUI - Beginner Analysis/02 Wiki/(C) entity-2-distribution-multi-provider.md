# Entity 2 — Distribution + Multi-Provider Ecosystem

## 1. One-liner (VI/EN)

**EN:** DeepSeek-TUI's distribution architecture — 5 packaging methods (corpus-record), 9-provider matrix (Pattern #84 84c FIRST POST-PROMOTION strengthening), 4-locale i18n, 2-binary dispatcher-companion split, China-friendly install paths.

**VI:** Kiến trúc phân phối của DeepSeek-TUI — 5 phương thức đóng gói (kỷ lục corpus), ma trận 9 nhà cung cấp (Pattern #84 84c — bằng chứng tăng cường ĐẦU TIÊN SAU PROMOTION), i18n 4 ngôn ngữ, kiến trúc 2-binary dispatcher-companion, đường cài đặt thân thiện với Trung Quốc.

## 2. When to use / NOT to use

This entity covers DEPLOYMENT decisions. Use this entity reference when:
- Choosing install path (npm vs cargo vs Homebrew vs Docker vs direct)
- Switching providers (DeepSeek default ↔ NVIDIA NIM ↔ OpenRouter ↔ Ollama)
- Deploying in mainland China (Tencent Cloud / CNB / Lighthouse HK)
- Evaluating provider lock-in vs Pattern #84 84c provider-agnostic-by-design
- Comparing to other coding-agent distribution architectures (v66 agentmemory / v70 codegraph / v71 agents-best-practices)

## 3. Entity vs sibling concepts

| Distribution dimension | DeepSeek-TUI (v72) | Claude Code | v66 agentmemory | v71 agents-best-practices |
|------------------------|---------------------|-------------|-----------------|---------------------------|
| Packaging methods | **5** | 1 (npm) | 3 (npm+pip+docker) | 2 (npm+git) |
| Provider matrix | **9** | 1 (Anthropic) | 1+ (provider-flexible) | Provider-agnostic (declarative skill) |
| Locales | **4** | 1 (EN) | 1 (EN) | 1 (EN) |
| Binary architecture | 2-binary split | Single binary | MCP server binary | Markdown-only |
| OS-level sandbox | 3-platform | App-level | None | N/A |

## 4. Sub-types / Categorization

**By packaging method:**
- **Wrapper:** npm (downloads release binaries) / Homebrew (downloads binaries via tap)
- **Native build:** Cargo (compiles from crates.io source)
- **Container:** Docker (GHCR pre-built image)
- **Direct:** GitHub Releases (manual binary download)

**By provider relationship:**
- **Primary vendor (default):** DeepSeek (deepseek-v4-pro / deepseek-v4-flash)
- **Hosted alternatives:** NVIDIA NIM / AtlasCloud / OpenRouter / Novita / Fireworks (5 hosted alternatives)
- **Generic compatibility:** Any OpenAI-compatible endpoint via `OPENAI_BASE_URL`
- **Self-hosted:** SGLang / vLLM / Ollama (3 self-hosted)

**By locale coverage:**
- **CJK trio:** EN + zh-Hans + ja
- **Latin extension:** pt-BR (Brazilian Portuguese) — extending corpus beyond CJK-only norm

## 5. Anatomy

```
DeepSeek-TUI Distribution Map
│
├── PRIMARY VENDOR (DeepSeek)
│   ├── api.deepseek.com (global)
│   ├── api.deepseek.com (CN preset)
│   └── legacy: api.deepseeki.com (typo host, backward compat)
│
├── HOSTED ALTERNATIVES (5)
│   ├── NVIDIA NIM
│   ├── AtlasCloud
│   ├── OpenRouter (aggregator — 200+ models)
│   ├── Novita
│   └── Fireworks
│
├── GENERIC OPENAI-COMPATIBLE
│   └── OPENAI_BASE_URL=<endpoint> (e.g., glm-5 via 3rd-party)
│
└── SELF-HOSTED (3)
    ├── SGLang (SGLANG_BASE_URL=...)
    ├── vLLM (VLLM_BASE_URL=...)
    └── Ollama (default localhost)
```

```
Install Path Decision Tree
│
├── Have Node? → npm install -g deepseek-tui
├── Have Rust toolchain? → cargo install deepseek-tui-cli + deepseek-tui
├── On macOS? → brew tap Hmbown/deepseek-tui && brew install deepseek-tui
├── Container env? → ghcr.io/hmbown/deepseek-tui:latest
└── Air-gapped? → GitHub Releases direct download (verify SHA-256)
```

## 6. Mechanism / How it works

**npm install path:**
1. `npm install -g deepseek-tui` invokes postinstall script
2. Script detects OS + arch (Linux x64/ARM64, macOS x64/ARM64, Windows x64)
3. Downloads matching prebuilt Rust binaries from GitHub Releases
4. Verifies SHA-256 against manifest
5. Places `deepseek` + `deepseek-tui` on PATH

**Cargo install path:**
1. `cargo install deepseek-tui-cli --locked` builds CLI dispatcher from crates.io source
2. `cargo install deepseek-tui --locked` builds TUI runtime from crates.io source
3. Requires Rust 1.88+ (let_chains + 2024 edition)
4. Both binaries placed in `~/.cargo/bin/`

**Provider switching:**
1. `deepseek auth set --provider <name> --api-key "$KEY"` writes provider+key to `~/.deepseek/config.toml`
2. `deepseek --provider <name>` launches with provider selected
3. Inside TUI, `/provider <name>` switches live; `/model <id>` opens provider-aware picker
4. All providers use OpenAI-compatible streaming client (Pattern #78 + #84 84c)

**Update path:**
- `deepseek update` (release-binary updater; canonical)
- `npm install -g deepseek-tui@latest` (npm wrapper)
- `brew update && brew upgrade deepseek-tui` (Homebrew)
- `cargo install <crate> --locked --force` (Cargo)

## 7. Out-of-box list

**Binaries delivered:**
- `deepseek` — CLI dispatcher
- `deepseek-tui` — TUI runtime

**Subcommands of `deepseek`:**
- `deepseek` (default — launches TUI)
- `deepseek -p "<PROMPT>"` — one-shot
- `deepseek exec --output-format stream-json <PROMPT>` — stream-JSON
- `deepseek exec --resume <ID|PREFIX> <PROMPT>` — non-interactive resume
- `deepseek exec --continue <PROMPT>` — non-interactive continue
- `deepseek serve --http` — HTTP/SSE runtime API
- `deepseek doctor` — verify setup
- `deepseek auth set/clear/status` — credential management
- `deepseek mcp ...` — MCP server management
- `deepseek update` — release-binary update
- `deepseek --version` — version info

**11 bundled skill packs** (see entity-1 §7 for full list).

## 8. Configuration

**Primary config file:** `~/.deepseek/config.toml` (precedence: config > keyring > env var)

**Environment variables:**
- `DEEPSEEK_API_KEY` — DeepSeek API key
- `OPENAI_BASE_URL` — Generic OpenAI-compatible endpoint
- `SGLANG_BASE_URL` — Self-hosted SGLang
- `VLLM_BASE_URL` — Self-hosted vLLM
- `DEEPSEEK_TUI_RELEASE_BASE_URL` — Mirrored release assets

**Auto-detection at first launch:**
- System locale → UI language selection
- DEEPSEEK_API_KEY → save to config or prompt

**`config.example.toml` is 36 KB** — extensive configurable surface for approval modes, themes, models, providers, locales, mouse-capture, sub-agent caps, RLM timeouts, etc.

## 9. Recipes

### Minimal — npm install

```bash
npm install -g deepseek-tui
deepseek
```

### Common — install on macOS via Homebrew

```bash
brew tap Hmbown/deepseek-tui
brew install deepseek-tui
deepseek --version
```

### Common — install on Linux ARM64 (Raspberry Pi)

```bash
npm install -g deepseek-tui   # works from v0.8.8+ on glibc-based ARM64 Linux
deepseek --version
```

### Common — Docker

```bash
docker volume create deepseek-tui-home
docker run --rm -it \
  -e DEEPSEEK_API_KEY="$DEEPSEEK_API_KEY" \
  -v deepseek-tui-home:/home/deepseek/.deepseek \
  -v "$PWD:/workspace" \
  -w /workspace \
  ghcr.io/hmbown/deepseek-tui:latest
```

### Advanced — mainland China install (Cargo mirror)

```toml
# ~/.cargo/config.toml
[source.crates-io]
replace-with = "tuna"

[source.tuna]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"
```

```bash
cargo install deepseek-tui-cli --locked
cargo install deepseek-tui     --locked
```

### Advanced — switch to OpenRouter (non-DeepSeek model)

```bash
deepseek auth set --provider openrouter --api-key "$OR_KEY"
deepseek --provider openrouter --model deepseek/deepseek-v4-pro
```

### Advanced — self-hosted vLLM

```bash
VLLM_BASE_URL="http://localhost:8000/v1" \
  deepseek --provider vllm --model deepseek-v4-flash
```

### Advanced — Tencent Cloud / CNB remote-first path

See `docs/TENCENT_CLOUD_REMOTE_FIRST.md` + `docs/TENCENT_LIGHTHOUSE_HK.md`. Always-on workspace controlled from phone via CNB mirror + Tencent Lighthouse HK + Feishu/Lark long-connection bridge + optional EdgeOne for public HTTPS edge.

### Advanced — install from source

```bash
git clone https://github.com/Hmbown/deepseek-tui.com
cd DeepSeek-TUI
cargo install --path crates/cli --locked   # requires Rust 1.88+
cargo install --path crates/tui --locked
```

Both binaries required. Cross-compilation notes: `docs/INSTALL.md`.

## 10. Advanced patterns

- **Multi-provider failover:** Configure multiple providers in `~/.deepseek/config.toml`; `/provider <name>` switches live without restart
- **Air-gapped deployment:** Direct download + SHA-256 verification + container image; no network calls except API endpoint
- **Locale-aware cost display:** Setting session locale to `zh-Hans` triggers CNY display alongside USD
- **CNB mirror integration:** Use `DEEPSEEK_TUI_RELEASE_BASE_URL` to point npm wrapper at mirrored binaries
- **Scoop on Windows:** Listed in Scoop's main bucket BUT manifest updates independently — may lag GitHub/npm/Cargo release. Use npm or direct GitHub for newest version

## 11. Combination patterns

| Combination | Use case |
|-------------|----------|
| **npm install + DeepSeek hosted** | Default beginner path |
| **Cargo install + Ollama self-hosted** | Privacy-first / offline-first |
| **Docker + OpenRouter** | Container CI/CD with model flexibility |
| **Homebrew + multi-provider config** | macOS power-user with provider portfolio |
| **Tencent Cloud + CNB mirror + Feishu bridge** | Mainland-China-native remote-first workflow |
| **HTTP serve + npm front-end** | Headless backend with web/IDE clients consuming the API |

## 12. Anti-patterns / common mistakes

- **Installing only one binary** — Both `deepseek` AND `deepseek-tui` are required. AGENTS.md: "installing only the CLI leaves the TUI stale and your fix won't appear to run."
- **Manual binary download without SHA-256 verification** — README warns: "verify the SHA-256 manifest and avoid look-alike repositories or search-result mirrors"
- **Using Scoop without `scoop update` first** — Scoop manifest lags GitHub/npm/Cargo
- **Using `cargo +nightly`** — Crate must compile on stable Rust
- **Mixing provider credentials** — Use `deepseek auth status` to see active credential source; saved config keys take precedence over keyring/env
- **Trusting `DEEPSEEK_API_KEY` env over saved config** — Saved config wins; if `deepseek doctor` says rejected key came from `DEEPSEEK_API_KEY`, remove stale export from shell startup

## 13. Related tools + cross-references + citations

### Vault cross-references

- **v71 agents-best-practices** — Provider-agnostic-by-design (84c) sister; both subjects exemplify 84c sub-mechanism at different scales (v71 dual-vendor synthesis / v72 9-provider matrix)
- **v66 agentmemory** — Pattern #18 sub-mechanism B B1 MCP variant sister; both have MCP-aware architecture
- **v70 codegraph** — Pattern #18 sub-mechanism B B1 MCP variant + multi-agent-installer-pattern OC-L sister; 2-binary architecture distinct mechanism
- **v62 codex-plugin-cc** — Pattern #84 84a tool-tolerance precedent (OpenAI plugin for Anthropic Claude Code = ecosystem norm); DeepSeek-TUI 84c is author-design-choice meta-archetype

### Pattern Library tags

- Pattern #84 84c FIRST POST-PROMOTION strengthening (9-provider matrix)
- Pattern #78 within-pattern (6-layer LDS: DeepSeek API + OpenAI-spec + MCP + LSP + Rust 2024 + OSC)
- Pattern #18 sub-mechanism C candidate (dispatcher-companion-binary-split)
- Pattern #52 HIGH-NOT-EXTREME sub-class N=2 (32K stars at 120 days = 267/d)
- 5-packaging-method corpus-record
- 4-locale corpus-record (T1 subjects)

### External references

- DeepSeek API platform: https://platform.deepseek.com/api_keys
- npm package: https://www.npmjs.com/package/deepseek-tui
- Cargo package: https://crates.io/crates/deepseek-tui-cli + https://crates.io/crates/deepseek-tui
- Docker image: ghcr.io/hmbown/deepseek-tui:latest
- DeepWiki index: https://deepwiki.com/Hmbown/DeepSeek-TUI
- Tencent Cloud docs: `docs/TENCENT_CLOUD_REMOTE_FIRST.md`
- Scoop manifest: Scoop's main bucket
