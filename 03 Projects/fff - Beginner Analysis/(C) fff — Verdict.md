# (C) fff — Verdict (v194)

> **Subject:** `dmtrKovalenko/fff` — a resident in-process fuzzy file+content search **library** for humans and AI coding agents (MCP server + Pi extension + Neovim plugin + C/Node/Bun/Python SDKs). MIT, © 2025 Dmitriy Kovalenko, ~9.5k★ (page-stated), v0.9.6, source-verified at `1cd8d31`.
> **Verdict:** **GOAL-ALIGNED INCLUDE 3/4** · **1 NEW §C standalone (N=1, corpus-first for the surface)** · counts UNCHANGED **46 patterns / 11 CONFIRMED Library-vocab** · Tier **T2 Service**.
> Verdict produced **INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. The read-only workflow (`wf_6be03459-b4f`, 8 agents) did source-reading + upstream research **only**; every corpus / collision / identity / pattern claim below was checked **by hand** (grep of `_state/` + `_patterns/` + `03 Projects/`; direct source reads of the MCP crate + install script + manifests).

---

## The four criteria

### (a) Cultural-peer axis — **FAIL** (clean)
Dmitriy Kovalenko is a **notable independent OSS developer** (date-io, odiff, fframes, fff; ~1.7k followers; member of LightSourceAI), **not Anthropic**. "Notable framework author" is **not a registered (a) axis** — this reinforces, but does **not** reopen, the disclosed-builder (a)-axis question held operator-reviewable at N=3 (v182: Waishnav v171 / Neo Reid v174 / Jack Le v181; + Evan Bacon v183 / Addy Osmani v184). No Anthropic affiliation, no heritage/name rescue. First `dmtrKovalenko` author → a **#19 19a** institutional/individual data-point. Clean FAIL.

### (b) Goal-relevance — **STRONG** (keys the tier)
fff is **agent-capability + token-efficiency substrate for AI CODING AGENTS**, Claude-Code-first-class among its supported clients (Claude Code / Codex / OpenCode / Cursor / Cline). It gives a coding agent **faster, more token-efficient, frecency-and-git-aware file/content search** than the built-in ripgrep-based Grep/Glob, and lands directly on two live threads:
- **`claude-api-cost-optimization`** — *"fewer grep roundtrips, less wasted context"*; the `MCP_INSTRUCTIONS` ("stop after 2 greps", def-body auto-expand to skip follow-up Reads) and the output shaping ("use offset to read relevant section") are literally token-spend discipline.
- **the agent-capability substrate** — the vault's own Claude Code searches *this very vault's* files constantly, and hireui is a real, ownable codebase → **directly, safely pilotable**.

**STRONG-not-STRONGEST** because it is third-party, it *augments* an agent's search (a capability layer, not the agent itself, not Anthropic substrate), and Claude is one of ~5 supported clients. Calibrates to **Agent-Reach v174 (b) STRONG** (a read+search capability layer — same shape, different surface: external web/social vs local filesystem) and **codebase-memory-mcp v172 (b) STRONG** (an MCP server that cuts the agent's token-spend on reading code). §31 keys GOAL-ALIGNED on (b) MODERATE+ regardless of (a).

### (c) Engineering quality — **STRONG** (with honest caveats foregrounded)
Production-grade Rust: a 7-crate workspace + a 4-language SDK (stable C ABI / Node / Bun / Python) + an MCP server + a Neovim plugin; **neo_frizbee SIMD Smith-Waterman** fuzzy, **SIMD Aho-Corasick** multi-pattern, SIMD `memmem` plain + Rust-regex; **LMDB (heed) frecency** with per-mode exponential decay, **mimalloc**, **contiguous arena** string storage w/ 16-byte chunk dedup, **mmap content cache** (~360 B/file), **rayon** parallel pipeline, **libgit2-direct** git status, a debounced background watcher, platform-specific FS syscalls; a **pinned + SHA-256-checksummed** installer; an auto-bumped Homebrew formula; 8 prebuilt platform binaries; a frozen top-level API contract. **Honest caveats (all documented in the Deep Dive §8):** the author's own AGENTS.md says *"this project does not have a traditional test suite"* (limited unit + integration coverage) — a real gap for a correctness-critical library; the headline benchmark is **warm-cache-vs-cold-spawn** and author-stated (unpublished methodology); adoption breadth ("powers opencode, nushell") is author-stated, not independently confirmed (community opencode plugins found; no nushell reference); real RAM-tradeoff issues (#437 cache fills, #477 scan blocking); `v0.9.x` pre-1.0 / nightly cadence; a startup update-check network call. STRONG stands, with the gaps in plain view.

### (d) Corpus connectivity — **STRONG**
- **Agent read+search / capability-layer web:** Agent-Reach v174 §C (the closest cousin — search reach *for* an agent; external vs local), camofox-browser v179 §C, serve-sim v183 §C.
- **Code-search family (all mechanistically distinct):** §C#23 code knowledge-graph (graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172 — AST/graph/FTS5), claude-context v40 (vector/embedding). fff is the **lexical/fuzzy+frecency** member none of them cover.
- **Token-efficiency:** codebase-memory-mcp v172 (token-reduction via a graph — the orthogonal-mechanism cousin), the `claude-api-cost-optimization` pilot thread, Library-vocab #20 Token-Economy-Quantification.
- **MCP distribution:** Pattern #18 B1-MCP (agentmemory v66 / codegraph v70 / codebase-memory-mcp v172 / google_workspace_mcp v140 / devspace v171 / cortex-hub v181).
- **Editor-picker heritage / upstream deps:** telescope/fzf-lua/snacks.picker + frizbee (blink.cmp) + zlob + ripgrep's crates (all non-corpus).

---

## Pattern outcome — **1 NEW §C standalone (N=1, CORPUS-FIRST for the surface)**

**Title:** *"Resident In-Process Fuzzy File+Content Search Library for AI Coding Agents (lexical + Smith-Waterman-fuzzy + frecency-ranked + git-aware; a long-lived indexed process, not a CLI subprocess; delivered via MCP + multi-language SDKs)."*

**Why a mint, and why corpus-first:** the by-hand collision grep is decisive — **no prior `fff` / Kovalenko / file-search / fuzzy-finder / fzf / ripgrep-replacement / frecency subject exists anywhere in the corpus** (word-boundary grep empty; zero `fzf`/`frecency`/`file-finder` hits in `_patterns/`). The nearest neighbors are each a **different mechanism**: §C#23 is a code *knowledge-graph* (AST/graph/FTS5), claude-context v40 is *vector/embedding*, Agent-Reach v174 is *external web/social*, and ripgrep/fzf/ast-grep are *CLIs*. fff's defining **conjunction** — (local lexical + typo-resistant fuzzy content search) × (frecency + git-awareness) × (a **resident in-process library**, not a subprocess-spawned CLI) × (delivered to agents via MCP + a multi-language SDK) — is genuinely new to the corpus, and the landscape research found **no direct peer** at this positioning.

**Scope honestly bounded:** corpus-first **for the local-file-search-SDK-for-agents surface** — **NOT world-first** (fzf / ripgrep / frizbee / telescope precede as tools; the novelty is the *resident-library-for-agents* packaging + the lexical-fuzzy+frecency+git conjunction). Mint at **N=1** per the **serve-sim v183 / Agent-Reach v174 / camofox v179** precedent (a corpus-first capability-layer standalone at N=1 when the surface is genuinely new and the anchor is a strong real subject — here: 9.5k★, production Rust, notable author, no direct peer). §28 ≤2-new-standalones cap honored (1 mint).

**⚠️ NO-MINT alternative recorded (operator/audit-reviewable)** — the camofox v179 / ai-berkshire v187 discipline: *"fff is a lexical-search mechanism variant within a broader 'agent code-search tooling' family (graph §C#23 + vector claude-context v40 + this) — different mechanism, shared job (give the agent code/file search) → file as instance-strengthening rather than a fresh standalone."* I lean **MINT** because (1) the mechanism is genuinely distinct and un-represented, (2) the anchor is strong with no direct peer, (3) it is a huge, universally-relevant capability, and (4) §C has **no existing "agent code-search meta-class" standalone to strengthen** (the existing rows are all mechanistically specific). Either reading leaves **counts UNCHANGED 46/11**.

---

## Secondary observations (NOT minted)
- **Pattern #18 B1-MCP instance-strengthening** — `fff-mcp` is a one-server-many-clients MCP server (5 clients) → the B1-MCP running set (N≈10 after cortex-hub v181) gains an instance (**N≈11**; exact tally is audit bookkeeping). The §C standalone = *capability*; #18 B1 = *distribution structure* → different axes, no double-count (the v140/v171/v172 precedent).
- **#84 84c provider-agnostic** — one MCP server + one C-ABI core consumed by 5+ agents and 4 languages; **NOT** the ponytail v168 "14-platform native-rule-file distribution" mechanism → **NO N-bump** (the v86 rule).
- **Library-vocab #20 Token-Economy-Quantification — QUALIFIED-ADJACENT** — "fewer roundtrips / less wasted context" + the output-shaping token discipline + the "sub-10 ms vs 3–9 s" claim are token/latency-relevant but page-stated/unreplicated → **N stays 4**, bump DEFERRED (the v168/v172/v175 precedent).
- **#66 supply-chain — BENIGN** — MIT; a pinned-tag + SHA-256-checksummed installer (a real integrity mitigation); no sudo, `~/.local/bin`. Real notes: startup update-check network call (`--no-update-check`), home-dir scanning default-on in the *nvim* plugin (the MCP server indexes the git-root), RAM accumulation (#437), scan-blocking (#477). The "risk" is resource use + a network ping, not security.
- **#19 19a** — first `dmtrKovalenko` author data-point.

## NON-claims
- **NOT Pattern #52** — stars page-stated (§37.4), nightly cadence, benchmark author-stated/unreplicated → viral-velocity unestablishable.
- **NOT world-first** — fzf / ripgrep / frizbee / telescope precede as tools; the claim is scoped to *corpus-first for the surface*.
- **NOT a code knowledge-graph (§C#23) / vector-search (claude-context v40) / web-search (Agent-Reach v174)** — distinct mechanism.
- **NOT #57** — derives from frizbee / zlob / ripgrep's crates and is used-by opencode/nushell — none are corpus subjects; integration/mentions ≠ recursion.
- **NOT a new top-level pattern** (max stays #85).

---

## Tier, streak, counts
- **Tier: T2 Service** (self-hosted local developer tool / MCP server; same family as codegraph v70 / codebase-memory-mcp v172 / agentmemory v66 / Agent-Reach v174 / camofox v179).
- **Streak:** GA:54 → **GA:55** — v194 is unambiguously goal-aligned (real agent-capability substrate). **§35 CLEAR:** rolling-3 window {v192 GA, v193 GA, **v194 GA**} = 0 OG (and even under the strict off-domain-model reading of v193 → {v192 GA, v193 OG, v194 GA} = 1 OG ≤ 1, still clear — and a clean goal-aligned v194 *resolves* any v193 strict-reading breach concern). **41 consecutive goal-aligned ships v153→v194** (GA reading).
- **Counts UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab.** §C **live standalones 35 → 36** (per the shim running count; exact §C tally is an overdue-audit reconcile item). Tracked PROVISIONAL surface ≈42 → **≈43**.

## inflation_check — discipline HELD
1 mint (≤2 cap); N=1 honestly scoped to corpus-first-for-the-surface (NOT world-first); NO-MINT alternative recorded operator-reviewable; max top-level pattern stays #85; counts 46/11 UNCHANGED; no double-count (#18 B1 vs the §C standalone are different axes); no N-bumps on #84 or #20; the author over-claim (MUI-X pickers / react-imask) caught and corrected; adoption + benchmark claims kept as author-stated caveats, not asserted as fact.

---

*Companion docs: `(C) fff — Deep Dive.md` and `(C) fff — Pilot Methods Menu.md`. Corpus entry v194; shipped on branch `wiki/v194-fff`.*
