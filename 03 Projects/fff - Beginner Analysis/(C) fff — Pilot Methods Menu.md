# (C) fff — Pilot Methods Menu (v194)

> **24 ways to apply `dmtrKovalenko/fff` to your working flow**, laddered from zero-risk reading → zero-install pattern-stealing → low-risk hands-on trial → the real hireui (Goal-#2) payoff → off-goal/personal → vault-meta.
> **Why this is one of the most directly-pilotable subjects in the corpus:** your Claude Code searches *this very vault's* files constantly, hireui is a real ownable codebase, and fff sits on your live `claude-api-cost-optimization` thread. The MCP server drops into Claude Code in minutes; and the single highest-ROI move needs **zero install** (method B7).
> **Honest framing first:** fff's bet — that agents benefit from fuzzy + frecency ranking over exact ripgrep — is plausible but **not settled by public research**. So the pilot is *measurement-first*: prove the token/latency delta on your own repos before trusting it. And the RAM tradeoff is real (see the fence).

**⭐ One-thing path:** **B7 → C11 → C13** — steal the search-discipline into your `CLAUDE.md` for free today (B7), then install `fff-mcp` against a scratch clone of the vault and eyeball the results (C11), then run the same 3 real search tasks with fff on vs off and **measure the tool-call + token delta** (C13). If the delta is real, promote to the vault proper; if not, you've spent an hour and learned it. Everything else is optional depth.

---

## A. Read + learn (zero install, zero risk)

**A1 — Read the Deep Dive §3–§4 as an "agent search internals" primer.** You now know *why* your agent's grep habits cost tokens (process spawns, re-reading `.gitignore`, no frecency, no cross-query memory) and what a resident index buys. ~20 min; pure understanding.

**A2 — Study the `MCP_INSTRUCTIONS` block (Deep Dive §3.2) as a distilled skill.** Five rules — bare identifiers, no gratuitous regex, *stop after 2 greps and READ*, multi-pattern OR, structured constraints — are the accumulated scar tissue of running an agent over big codebases. Read them as *lessons about how you already prompt Claude to search*.

**A3 — Read the output-shaping design (Deep Dive §3.3).** Frecency labels, the "(NNKB — use offset)" coaching tag, def-body auto-expansion to skip follow-up Reads — a masterclass in *designing a tool's output to steer the agent's next action and minimize context*. Directly transferable to any tool you build for hireui.

**A4 — Read the frecency + decay mechanics (Deep Dive §4.4).** "Frequency + recency" (Firefox 2008), exponential decay with a 10-day (human) vs 3-day (AI) half-life, git-touch warm-up. A clean, reusable ranking idea for *any* "what's relevant right now" list.

---

## B. Borrow patterns by hand (zero install — highest ROI, lowest risk)

**B5 — Adopt "search bare identifiers, never gratuitous regex" as a standing rule.** Add it to your vault's `CLAUDE.md` search guidance even without fff — it's a free reduction in wasted grep calls on the vault's huge `_state/`/`_patterns/` chapters.

**B6 — Adopt the "stop after 2 greps → READ the top result" discipline.** This is the single cheapest token-saver here and it composes with your `claude-api-cost-optimization` spec. Encode it as a one-liner in `CLAUDE.md`.

**⭐ B7 — Steal the whole search discipline into your `CLAUDE.md`, verbatim, today.** Paste an adapted `MCP_INSTRUCTIONS` (bare-identifiers / no-regex / 2-greps-then-read / multi-pattern-OR / structured-constraints) as a "how to search this vault" block. **Zero install, works immediately, applies to every Claude Code session over the vault and hireui.** This is the highest-ROI move on the whole menu.

**B8 — Borrow the output-shaping ideas for any hireui agent-tool.** When you eventually spec hireui's first MCP tool (per the v192 palmier-pro `ToolExecutor` template), copy fff's tricks: return frecency/relevance labels, coach large-payload reads ("use offset"), auto-expand just enough context to skip a follow-up call. Bank it in the hireui MCP spec now.

**B9 — Borrow the frecency-ranking idea for a vault "hot pages" surface.** A tiny script that ranks `03 Projects/` + `_state/` files by git-touch recency+frequency would give you (and your agent) a "what's active right now" list — the same idea fff applies to search results, applied to your own corpus.

---

## C. Low-risk hands-on trial (install; read-only search = safe)

> **Fence for all of C/D:** run `/install-snapshot` first; the `install-mcp.sh` is already **pinned to `v0.9.6` + SHA-256-checksummed** (read it — it's honest), but prefer `brew install dmtrKovalenko/fff/fff-mcp` or `cargo install` over piping to bash; run `fff-mcp` with **`--no-update-check`**; pin `v0.9.6`; trial on a **scratch clone** before the real vault/hireui. ⚠️ You're on macOS — the MCP binary is native (darwin-arm64/x64 prebuilt), no Neovim/Rust toolchain needed.

**C10 — Install `fff-mcp` and read the server's own instructions.** `brew install dmtrKovalenko/fff/fff-mcp`, then run `fff-mcp --healthcheck` in a scratch repo. Confirm it discovers the git root and scans. Zero agent wiring yet — just prove the binary works.

**C11 — Wire `fff-mcp` into Claude Code against a scratch clone of THIS vault.** Add it as an MCP server pointed at a throwaway copy of the KJ OS vault. Ask Claude to "find where the v182 audit changed the code-graph count" using fff's `grep`/`find_files`. Read-only search over your own huge markdown corpus — the ideal safe first test. The vault's `_state/` + `_patterns/` chapters are exactly the "search the same big tree many times" workload fff is built for.

**C12 — Compare fff `grep`/`multi_grep` vs the built-in Grep on one gnarly query.** Pick a real search you've done (e.g. every mention of a pattern name across `_patterns/` + `03 Projects/`). Run it with the built-in tool, then with fff (`multi_grep` for name variants). Note: fewer roundtrips? typo-resistance help? def-body context that saved a Read?

**⭐ C13 — Measure the delta (the point of the whole pilot).** Take **3 representative real search tasks** over the vault. Run each twice — Claude Code with fff off, then on — and record **tool-call count + tokens + wall-clock** (pair with your `ccusage`/OTel observability pilot). This turns "faster/cheaper" from a claim into a number *for your repos*. Promote fff only if the delta is real.

**C14 — Try it on hireui's structure without touching hireui's rules yet.** Point `fff-mcp` at a **scratch clone** of hireui and run the searches your agent actually does on it (find a screen, grep a token name, locate an API route). Gauge whether the frecency ranking surfaces the right files on a real, unfamiliar-to-the-agent codebase.

**C15 — Test the failure modes yourself.** Reproduce the honest caveats on a scratch clone: watch resident memory as the cache fills (issue #437), time the initial scan on a big repo (issue #477), and confirm `--max-cached-files` caps RAM. Know the sharp edges before they surprise you in a real session.

---

## D. hireui / Goal-#2 application (per hireui's CONSTITUTION)

> **hireui rules apply:** operator installs the MCP server (I-8), agent work on an `agent-*` branch (I-2), GitNexus-first, run hireui-rooted. hireui has *no LLM spend yet* — so fff here is "build the search substrate right," not a cost retrofit.

**D16 — Operator-install `fff-mcp` for hireui's Claude Code and measure on a real ticket.** With fff wired in (per I-8), run one real hireui ticket (e.g. a Candidate-Detail search-heavy refactor) on an `agent-*` branch and record the tool-call/token delta vs your baseline. A completed, measured hireui pilot = a concrete Goal-#2 artifact.

**D17 — Use fff to accelerate the Candidate-Detail refactor spike.** That spike is search-heavy (finding drifted tokens, orphaned styles, half-migrated components across the app). fff's `multi_grep` over token-name variants + git-aware `git:modified` scoping is a natural fit for "find every place this token leaked."

**D18 — Pair fff with GitNexus, don't replace it.** hireui is GitNexus-first (structural/graph queries). fff is the *lexical/fuzzy* complement — "find the file / grep the identifier" fast, while GitNexus answers "what calls this / what's the graph." Spec them as **orthogonal**: GitNexus for structure, fff for fast lexical reach. (This mirrors the Deep Dive §9 mechanism table.)

**D19 — Fold fff's search-discipline into hireui's `CLAUDE.md`.** Same as B7 but scoped to hireui — encode bare-identifiers / stop-after-2-greps into hireui's agent guidance so every agent session on it is cheaper. Zero-install, composes with the responsible-AI + cost-optimization specs already queued for hireui.

**D20 — Prototype a tiny hireui `Result<T>`-style search tool from the Node SDK.** If you want an *in-app* search feature (not just agent search), `@ff-labs/fff-node`'s `FileFinder` + `Result<T>` pattern is a clean, typed template. Low-priority, but it's the "build custom agent tools/CLIs on top of fff" path the README advertises.

---

## E. Off-goal / personal

**E21 — Install `fff.nvim` if you use Neovim.** The original picker (drop-in for telescope/fzf-lua/snacks.picker): frecency-ranked, typo-resistant, git-aware, with a def-classifier. Personal-productivity, off the software-agent goal, but it's the polished origin of everything above.

**E22 — Look at `odiff` (the author's SIMD image-diff library).** If you ever need fast visual-regression diffing (e.g. the Candidate-Detail Figma-handoff drift you track), odiff (Zig, SIMD-first, ~3.1k★) is by the same author and in the same "make-it-really-fast" spirit. Cross-reference to your ai-web-design / Taste-Skill redesign gate.

---

## F. Vault-meta / follow-ups

**F23 — Add fff to the pilot ladder + watch for a 2nd instance (N=2 promotion).** The §C standalone is at N=1. If another "resident in-process fuzzy-search library for agents" appears, it promotes. Log it as a watch axis alongside the code-search family (§C#23 graph + claude-context vector + this lexical member).

**F24 — Reconcile the "search substrate" picture across the corpus.** You now have three orthogonal agent-code-search mechanisms in the corpus: **graph** (§C#23: graphify/GitNexus/codegraph/codebase-memory-mcp), **vector** (claude-context v40), and **lexical/fuzzy** (fff v194). A short synthesis note ("when to use which for a coding agent") is a genuinely useful vault artifact and directly informs the hireui GitNexus+fff pairing (D18).

---

## The fence (mandatory, condensed)
`install-snapshot` first · prefer `brew`/`cargo` over `curl|bash` (though the script IS pinned + SHA-256-checksummed) · run with `--no-update-check` · pin `v0.9.6` · `npm-security-check` before any `@ff-labs/*` npm install · **scratch clone before the real vault/hireui** · cap RAM with `--max-cached-files` on big repos · **measure the delta before promoting** (C13) · hireui per its CONSTITUTION (I-8 operator-installs / I-2 `agent-*` branch / GitNexus-first) · read-only search is the safe surface — fff never writes your files.

---

*Companion docs: `(C) fff — Deep Dive.md` and `(C) fff — Verdict.md`. Corpus entry v194; source-verified at commit `1cd8d31`.*
