# (C) fff — Deep Dive (v194)

> **Subject:** [`dmtrKovalenko/fff`](https://github.com/dmtrKovalenko/fff) — *"A file search toolkit for humans and AI agents. Really fast."*
> **What it is:** a resident, in-process **Rust file-search library** (explicitly *not* a CLI) — typo-resistant fuzzy path + content search, frecency-ranked file access, a background watcher, and a lightweight in-memory content index — delivered to AI coding agents through an **MCP server**, a **Pi agent extension**, a **Neovim plugin**, and **C / Node / Bun / Python** SDKs.
> **License:** MIT ("& open source forever"), © 2025 Dmitriy Kovalenko · **Stars:** ~9.5k (page-stated §37.4) · **Version:** stable `v0.9.6` (2026-06-21), HEAD `0.9.7-nightly.1cd8d31` · **Source-verified at commit** `1cd8d31` (2026-07-02).
> **Corpus:** v194 · GOAL-ALIGNED INCLUDE 3/4 · Tier T2 Service · 1 NEW §C standalone (N=1, corpus-first for the surface).
> Cloned + source-read by hand (README, AGENTS.md, `crates/fff-mcp/`, `install-mcp.sh`, Cargo workspace) + an 8-agent read-only research workflow (`wf_6be03459-b4f`, ~1.36M tokens). All load-bearing claims cross-checked against the source.

---

## 1. The one-sentence thesis

Ripgrep and fzf are **command-line programs**: every call forks a new process, re-reads `.gitignore`, re-stats directories, and rebuilds its in-memory state before it can answer. That is fine when you grep once from a shell. It is **wasteful when an editor or an AI agent runs hundreds of searches per session.** fff keeps the index and the file cache resident in **one long-lived process** and exposes the same Rust core through thin layers — so you pay the walk-and-index cost **once**, and every subsequent search hits warm memory.

For an AI coding agent, the payoff is two-sided:
- **Latency:** on a 500k-file Chromium checkout, the README claims the difference between **3–9 SECONDS per ripgrep spawn** and **sub-10 ms per fff query** (author-stated; see §8 for the honest caveat).
- **Tokens / context:** *"Fewer grep roundtrips, less wasted context, faster answers."* The MCP server ships a carefully prompt-engineered system message and token-efficient output shaping specifically to keep an agent from flailing (see §3–§4). This is the reason fff belongs in this vault at all — it lands squarely on the **claude-api-cost-optimization** thread.

> It began life as a Neovim plugin (`fff.nvim`) people loved, then generalized: *"plenty of AI harnesses and code editors need the same thing: accurate, fast file search as a **library**. That is what fff is."*

---

## 2. Architecture — one Rust core, many thin layers

fff is a **7-crate Cargo workspace** plus a set of language-binding packages. Everything performance-critical lives in Rust; each surface is a thin adapter over the same core.

```
crates/
  fff-core        (published as `fff-search`)  ← the engine: index, scoring, grep, watcher
  fff-grep                                     ← content-search modes (plain / regex / fuzzy)
  fff-query-parser                             ← the constraint query language (git:modified, globs, !excludes)
  fff-c           → libfff_c.{so,dylib,dll}    ← stable C ABI; the base for every non-Rust binding
  fff-mcp         → the `fff-mcp` binary       ← MCP server (stdio) for AI agents
  fff-nvim        (mlua/luajit)                ← Neovim plugin bindings
  fff-python      (PyO3, abi3 wheel)           ← Python bindings
packages/
  fff-node / fff-bun  (@ff-labs/fff-node)      ← TypeScript SDK over the C library
  pi-fff              (@ff-labs/pi-fff)        ← Pi agent extension
  fff-bin-*  ×8 platforms                      ← prebuilt binaries (darwin/linux/win × arm64/x64, musl+gnu)
```

**Runtime shape** (from `crates/fff-mcp/src/main.rs`, hand-read):
- A **single resident `FilePicker`** is created once (`FilePicker::new_with_shared_state`) — held for the process lifetime, *not* one-per-request.
- It **discovers the git root** (`git2::Repository::discover`) and indexes from there; falls back to the given base path if there's no repo.
- A **background scan** runs at startup (non-blocking — the server answers the MCP handshake immediately and blocks the first query on scan-ready).
- A **background file-system watcher** keeps the index live (disable with `--no-watch`).
- **`mimalloc`** is the global allocator.
- Release profile is tuned hard: `opt-level = 3`, `lto = "fat"`, `codegen-units = 1`, `strip = "debuginfo"`.

**Two on-disk databases** (LMDB via the `heed` crate):
- **Frecency DB** — per-file access-timestamp history for ranking.
- **Query-history DB** — previous search queries (for combo-boosting).

---

## 3. The agent-facing surface — the MCP server (the load-bearing part)

This is the part that matters most for the vault, and I read it directly (`crates/fff-mcp/src/server.rs` + `main.rs`).

### 3.1 Three tools (code-accurate names)

| Tool | Job | Notable design |
|---|---|---|
| **`grep`** | Search file **contents**. "The DEFAULT search tool." | Auto-detects regex metacharacters → regex mode, else plain-text (SIMD). On **0 matches** it runs a **3-stage fallback**: drop the first non-constraint word → fuzzy fallback → file-path fallback. |
| **`find_files`** | Fuzzy search on file **names / paths**. | Frecency-aware. **Auto-retry**: if a 3+-word query returns 0, it retries with the first 2 words. Emits `→ Read <file> (exact match!)` next-action hints. |
| **`multi_grep`** | Content search matching **ANY** of multiple patterns (OR logic). | Literal patterns only ("NEVER escape special characters"); backed by SIMD Aho-Corasick — faster than regex alternation. |

> ⚠️ **Doc-vs-code nuance (documented faithfully):** the README's *MCP* section loosely calls the tools `ffgrep` / `fffind` / `fff-multi-grep` — those are the **Pi extension's** tool names. The **MCP server** registers them as **`find_files`, `grep`, `multi_grep`** (`#[tool(name=...)]` at `server.rs:422/538/575`). Use the code-accurate names.

All three: default `max_results` 20, opaque **cursor pagination**, and output modes `content` (default) / `files_with_matches` / `count` / `usage`. Transport is **stdio**; **no authentication** (the stdio process boundary is the security boundary). Idle-exit after **900 s** of inactivity (`--idle-timeout-secs`). The server runs in **`FFFMode::Ai`**.

### 3.2 The system prompt is a portable "how to search a codebase" discipline

`fff-mcp` hands the agent a `MCP_INSTRUCTIONS` block during the MCP handshake (`main.rs:19–93`). It is, in effect, a small skill for search behavior — and **you can borrow it verbatim without installing anything** (see the Pilot Menu, method B7). The hard-won rules:

1. **Search BARE IDENTIFIERS only.** `InProgressQuote` finds the definition *and* all usages. `load.*metadata.*InProgressQuote` (regex spanning tokens) → 0 results. `ctx.data::<ActorAuth>` (code syntax) → 0. `struct ActorAuth` (keywords narrow, misses enums/traits) → worse.
2. **NEVER use regex unless you truly need alternation.** Plain text is faster and more reliable; `.*`/`\d+`/`\s+` almost always return 0 within single lines. For OR, use `multi_grep`.
3. **Stop searching after 2 greps — READ the code.** *"More greps != better understanding."* (This is literally token-spend discipline encoded in the tool's instructions.)
4. **Use `multi_grep` for name variants** — one call for `['ActorAuth','PopulatedActorAuth','actor_auth']` instead of 3 sequential greps.
5. **Constraints are structured, not bare words:** `*.rs`, `src/`, `schema.rs`, `!test/`. `quote TODO` searches for the *literal text* "quote TODO"; `quotes/ TODO` filters to the directory.

### 3.3 Output is shaped for tokens and next-actions

From `crates/fff-mcp/src/output.rs` (hand-read):
- Files carry human-readable **frecency labels**: `hot` (≥100), `warm` (≥50), `frequent` (≥10), plus a `git:<status>` tag.
- Files **≥20 KB** get appended `(NNKB - use offset to read relevant section)` — the tool coaches the agent to do offset reads instead of dumping a big file into context.
- Grep results **auto-expand definition bodies** (struct fields, fn signatures; `|` marks def-body context, `[def]` marks definition files) — *"often provides enough information WITHOUT a follow-up Read call."*
- Bounded output caps (`MAX_LINE_LEN` 180, def-expand caps 5–8) so results never flood the context window.

The whole surface is engineered to (a) find the right file fast and (b) minimize the tokens spent doing it — the "less wasted context" claim is real in the code, not just marketing.

---

## 4. The core algorithms — the "knowledge" deep dive

This is what makes fff a genuinely instructive engineering artifact, not just another wrapper. (Source: `crates/fff-core`, `fff-grep`, `fff-query-parser`; algorithm details from the source-read workflow, cross-checked against `Cargo.toml` deps.)

### 4.1 Fuzzy path matching (frizbee-derived SIMD)
- Uses **`neo_frizbee`** (0.10.3) — a SIMD fuzzy matcher derived from **[frizbee](https://github.com/saghen/frizbee)**, the matcher behind the Neovim completion engine **blink.cmp**. frizbee is a **SIMD Smith-Waterman** implementation ("similar algorithm to FZF/FZY," ~6× fzf's throughput per its own README).
- Paths are stored in a **16-byte SIMD-chunk arena** (matching NEON/SSE2 register width), with 4 inline chunks per path (~85% of paths need no heap alloc), and **chunk-level deduplication** across the corpus (identical 16-byte chunks share one arena slot → big CPU-cache win).
- The final score is a **saturating sum of ~11 components**: base fuzzy score + frecency boost + git-status boost + distance penalty + filename bonus + special-filename bonus + current-file penalty + combo-match boost + path-alignment bonus. Ranking is more than "does it match" — it's "how likely is this the file you want."
- Sorting uses a **partial-sort optimization** (`select_nth_unstable`) when you need <50% of a >100-item result set.

### 4.2 Content grep — three modes, auto-selected
- **Plain** — SIMD `memmem` substring search (`memchr` crate); the default and fastest.
- **Regex** — the Rust `regex` crate (the same engine ripgrep uses), with fallback to plain text on invalid regex.
- **Fuzzy** — **Smith-Waterman per line** (via `neo_frizbee`) — this is what makes content search *typo-resistant*: `shcema` still finds `schema`. Auto-fallback: a plain search that returns 0 retries as fuzzy.

### 4.3 Multi-pattern OR search
- **SIMD Aho-Corasick** (`aho_corasick` crate) — a trie with failure links that finds *any of N patterns* in one linear pass (O(m+n+k)). Far faster than 20 separate ripgrep runs or a giant regex alternation. This is what powers `multi_grep`.

### 4.4 Frecency ("frequency + recency")
- The idea originates in **Firefox 3 (2008)** for the AwesomeBar: rank by a blend of how *often* and how *recently* something is used.
- fff stores up to **128 access timestamps per file** (LMDB via `heed`), purges entries older than **30 days**, and applies **exponential decay**:
  - **Normal mode:** decay constant `ln(2)/10` → **10-day half-life**.
  - **AI mode:** a faster decay (`ln(2)/3` → **3-day half-life**) + AI-specific modification thresholds — the agent's "recently touched" window is sharper than a human editor's.
- **Warm-up from git touch history:** files with recent git activity get a frecency head-start at startup, so ranking is useful before you've opened anything.

### 4.5 The query language (`fff-query-parser`)
A small constraint grammar shared by every surface: `git:modified` (or `staged`/`deleted`/`renamed`/`untracked`/`ignored`), directory scoping (`test/`), exclusions (`!test/`, `!*.spec.ts`), extension filters (`*.rs`, `*.{c,h}`), single-file grep (`src/main.rs`), and full globs via **[zlob](https://github.com/dmtrKovalenko/zlob)** (Kovalenko's own Zig-based, SIMD-first, gitignore-aware glob + parallel FS walker). Mix freely: `git:modified src/**/*.rs !src/**/mod.rs user controller`.

### 4.6 Performance engineering (the durable lessons)
- **`mimalloc`** allocator (thread-local heaps, free-list sharding; the allocator CPython 3.13+ adopted).
- **Contiguous arena string storage** — one bump-allocated block, O(1) allocs, near-zero fragmentation, excellent cache locality.
- **Memory-mapped content cache** — files are kept resident (or lazily `mmap`'d and released after each grep beyond the cache budget, default 30,000 files). ~**360 bytes per indexed file** → ~36 MB for a 100k-file repo; ~26 MB on a 14k-file repo; a few hundred MB on Chromium (500k). *This RAM-for-speed trade is the entire mechanism, and the project says so plainly.*
- **`rayon`** parallel search pipeline that isn't contended by orchestration logic; **SIMD-first** everywhere.
- **Platform-specific FS syscalls** (`getdents64` on Linux, the NTFS API on Windows) and a **background watcher** (`notify` + `notify-debouncer-full`, 50 ms debounce; FSEvents on macOS, `ReadDirectoryChangesW` on Windows, per-dir inotify on Linux) that talks to **libgit2 directly** (`git2`) instead of spawning `git`.

---

## 5. Multi-language SDK surface

The same core, four ways beyond Rust:
- **C ABI** (`crates/fff-c/include/fff.h`): a stable C99 surface with a **versioned `FffCreateOptions` struct** (`FFF_CREATE_OPTIONS_VERSION = 2`) that evolves without ABI breaks; explicit memory-ownership rules (free `FffResult*` with `fff_free_result`, strings with `fff_free_string`). Bind from C/C++, Zig, Go (cgo), Python (ctypes), anything with C FFI. The **top-level Rust/Lua/C/Bun APIs are declared frozen** ("can not be changed under any circumstance").
- **Node/Bun** (`@ff-labs/fff-node`): a `FileFinder` with `create({ basePath, aiMode })`, `waitForScan`, `fileSearch`, `grep`, `multiGrep`, `glob`; every method returns a `Result<T>` (`{ok:true,value} | {ok:false,error}`). Its `glob` is claimed 10–100× faster than Node/Bun's built-in.
- **Python** (`fff-search`, PyO3, `abi3` wheel for 3.10+, `py.typed`): `FileFinder` context manager, sync `wait_for_scan_blocking` + async `wait_for_scan` coroutine, `search`/`glob`/`grep`/`multi_grep`, typed result objects.
- **"AI mode"** (`aiMode: true` / `ai_mode`) is a real flag across all surfaces: it switches grep parsing to `AiGrepConfig`, uses the faster frecency decay + AI modification thresholds, drives event-driven per-file frecency updates from the watcher, and shapes output for token efficiency.

---

## 6. Distribution & install (source-read for the pilot fence)

- **curl | bash one-liner** (`install-mcp.sh`, hand-read): `set -eo pipefail`, a **pinned release tag (`v0.9.6`)**, and **SHA-256 checksums for all six platform binaries baked into the script and verified** before install. Downloads the prebuilt `fff-mcp` from GitHub releases (`dmtrKovalenko/fff.nvim/releases`) into `~/.local/bin` (**no sudo**). This is a *responsibly built* installer, not a blind pipe-to-bash — the integrity check is real.
- **Homebrew:** `brew install dmtrKovalenko/fff/fff-mcp` (formula auto-bumped on every stable release).
- **Prebuilt binaries** for 8 platform targets (also inside `@ff-labs/fff-bin-*` npm packages); **Cargo** (`fff-search`), **PyPI** (`fff-search`), **npm/Bun** (`@ff-labs/fff-node`), **Pi** (`pi install npm:@ff-labs/pi-fff`), **Neovim** (lazy.nvim / vim.pack, downloads a prebuilt binary or `cargo build`s).
- **Recommended agent wiring:** drop `For any file search or grep in the current git-indexed directory, use fff tools.` into your `CLAUDE.md`.

---

## 7. Author & lineage

- **Dmitriy Kovalenko** (GitHub [@dmtrKovalenko](https://github.com/dmtrKovalenko), X @neogoose_btw) — an **independent, performance-focused OSS developer** (~1.7k followers; personal site dmtrkovalenko.dev, *"your unFriendly Software Engineer"*). Member of **LightSourceAI** (GraphQL N+1 optimization + Claude-integration plugins; independent, not a FAANG). **No Anthropic affiliation** (confirmed).
- **Confirmed prior work:** **date-io** (the date-library abstraction that MUI's date pickers are built on), **odiff** (a Zig SIMD-first image-diff library, ~3.1k★), **fframes**, and fff itself.
- ⚠️ **Corrections (do not repeat these earlier guesses):** an initial read attributed *"MUI-X date pickers"* and *"react-imask"* to him — **neither is confirmed.** He authored `date-io` (used by MUI pickers) but is **not** a listed MUI-X maintainer, and react-imask is a different author's project. Attribute only the confirmed projects above.
- **Lineage:** fff descends from `fff.nvim` (the Neovim picker, positioned as a drop-in replacement for telescope / fzf-lua / snacks.picker) and reuses Kovalenko's own **zlob** (glob) + the community's **frizbee** (fuzzy) + BurntSushi's `regex`/`ignore` (ripgrep's crates). No corpus subject is cited as an influence (→ no Pattern #57 recursion).

---

## 8. Honest caveats (read before piloting)

- **"This project does not have a traditional test suite"** — the author's own words in `AGENTS.md` ("limited coverage, primarily integration testing"; inline Rust unit tests + ad-hoc Neovim e2e). For a perf/correctness-critical search library, that's a real gap.
- **Benchmark is warm-cache-vs-cold-spawn.** The "sub-10 ms vs 3–9 s" and the `chart.png` "vs built-in AI file-search tools" are **author-stated**, methodology unpublished, not independently replicated. The comparison is *directionally* fair for the resident-process use case (the README itself says "if you run one grep from bash, `rg` is still the right tool"), but treat the exact numbers as marketing.
- **Adoption breadth is author-stated.** The README says it "powers file search in opencode, nushell, and many more." A web check found **community** opencode plugins (16★ / 8★, not confirmed-native) and **no** nushell reference. Real, but treat "powers opencode/nushell" as author-stated, not independently confirmed.
- **RAM tradeoff is the whole point — and it bites.** Cache accumulation is a reported issue (GitHub #437 "Cache gets completely filled"); the initial scan can block (#477, `pi-fff` blocking). Budget-cap it (`--max-cached-files`, default 30k) and expect resident memory to scale with repo size.
- **Maturity:** `v0.9.x` (pre-1.0), nightly release cadence, ~40% of the `fff-search` crate documented on docs.rs. Pin a commit/tag for reproducibility.
- **Runtime network call:** the MCP server does a **startup update-check** (a network ping); disable with `--no-update-check`. No telemetry/exfiltration found beyond that.
- **Star count is page-stated** (§37.4, this environment mocks the GitHub API) → **not** a Pattern #52 viral-velocity claim.

---

## 9. Where it sits vs the corpus's other code-search subjects

fff is **mechanistically distinct** from everything the corpus already has (this is why it earns a new §C standalone — see the Verdict):

| Subject | Mechanism | Surface | Deps |
|---|---|---|---|
| **fff (v194)** | **lexical + fuzzy (Smith-Waterman) + frecency**, resident in-process **library** | local filesystem | **zero external** (self-contained Rust) |
| §C#23 code knowledge-graph (graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172) | AST / graph / FTS5 | local codebase (pre-indexed graph) | SQLite (+ embeddings for v172) |
| claude-context v40 | **vector / embedding** semantic search + BM25 | local codebase | needs an embedding provider + vector DB |
| Agent-Reach v174 §C | **external web/social** read+search | Twitter/Reddit/YouTube/GitHub… | per-platform backends |
| ripgrep / fzf / ast-grep | exact regex / interactive fuzzy / AST pattern | local — but **CLIs** (subprocess spawn) | — |

The landscape research found **no direct peer** at fff's exact positioning ("the only in-process library for fuzzy file discovery with frecency ranking, delivered to agents"). Its bet — *that agents benefit from fuzzy + frecency ranking, not just exact ripgrep* — is plausible but **not yet settled by public SOTA research**. That honest uncertainty is worth holding onto.

---

*Companion docs: `(C) fff — Verdict.md` (the 4-criteria call + pattern outcome) and `(C) fff — Pilot Methods Menu.md` (24 ways to apply this to your workflow). Source-verified at commit `1cd8d31`; corpus entry v194.*
