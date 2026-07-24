# (C) code-review-graph — Pilot Methods Menu

**Wiki v226 · 2026-07-25 · MIT · `pip install code-review-graph` (v2.3.7) · Python 3.10+**

> **On-goal + directly, LOW-risk pilotable** — the fff v194 / codebase-memory-mcp v172 class, and arguably a *stronger* pilot for you: pure-`pip install` (no `curl|bash` compiled binary like codebase-memory-mcp v172, no remote tunnel like devspace v171), MIT, read-only graph query = safe surface, and its **entire value prop (token reduction for code review) maps onto your live `claude-api-cost-optimization` pilot thread**. hireui is a real ownable codebase **and is already "GitNexus-first"** (GitNexus v33 = a member of the same Library-vocab #23 family) → a genuine head-to-head is available.
>
> ⭐ **One-thing path: A1 → C11 → D16.** Read the blast-radius + MCP-tool design → `pip install` + `build` against a scratch clone, register into Claude Code, and **MEASURE the token delta** on 3 real review questions → bake it off against GitNexus on a hireui staging clone (read-only, `agent-*` branch, per hireui's CONSTITUTION).
>
> **Fence (load-bearing):** install-snapshot before install + `pip`-security-check `code-review-graph` + scratch/vault-clone or hireui-**staging** first (never prod) + review the 30 MCP tools before wiring into an agent + single-client config (Claude Code only) + **MEASURE the token delta before promoting** + the optional `wiki` extra uses a **local** Ollama model (no cloud) but the `google-embeddings` extra egresses to Google if enabled (prefer the local `embeddings` extra) + pin **v2.3.7** + **NOT source-cloned → treat as untrusted-until-inspected** + hireui per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).

---

## A — Read & learn (zero install, zero risk)

**A1 ⭐** — Read the **blast-radius / impact-analysis** design (callers + dependents + affected tests as graph traversal) and the **0.714-F1 benchmark** with its "recall = 1.0, circular by construction" self-caveat. Internalize *"answer review questions by traversing a pre-built graph, not by re-reading files."* This is the operative idea for cutting your own agent's code-review token spend.

**A2** — Read the **30 MCP tool** categories (query / traversal / semantic search / impact radius / review context / community detection / flow analysis / refactoring / wiki generation / architecture overview / change detection / multi-repo). Note which map onto your real code-review workflow.

**A3** — Study the **networkx-in-memory vs SQLite** choice (vs codebase-memory-mcp v172's SQLite store): fast to build + incremental (watchdog <2s) but not persisted across restarts. A useful design data-point for the vault's code-intel notes.

**A4** — Read the **igraph community-detection** (Leiden / betweenness) layer as a "find the modules + the central hub nodes of a codebase" technique — orthogonal to blast-radius.

**A5** — Read the compression-metric framing (per-question ~82× vs the profile's aggregate "6.8×") as a case study in reading a repo's OWN numbers critically (§37.4 discipline).

## B — Borrow patterns, zero install

**B6** — Put *"give the agent a pre-built structural graph + return only the relevant slice per question — never the raw file dump"* into the vault's code-intel / `CLAUDE.md` notes (composes with the "structured-surface-not-raw-dump" thread: browser-use v41 / codebase-memory-mcp v172 / fff v194 / PixelRAG v211).

**B7** — Borrow the **blast-radius-as-a-review-gate** idea: before approving a change, ask "what does the graph say this touches (callers / dependents / tests)?" — a discipline you can apply by hand or wire into a PR loop (composes with the loop-engineering v189 PR-babysitter thread).

**B8** — Borrow the **honest-benchmark discipline** (report precision/F1, disclose that recall is graph-bounded) into how the vault reports its own numbers.

**B9** — Note the **ollama-powered wiki-generation + Obsidian-vault export** as the LLM-Wiki-pattern applied to code — a direct sibling of openwiki v195 and a mirror of this vault; a candidate design if you ever want an auto-generated code companion for hireui.

## C — Hands-on, scratch (LOW risk, the real pilot)

**C10** — `install-snapshot` + `pip`-security-check → `pip install code-review-graph` in a **scratch venv**; `code-review-graph build` against a **throwaway clone of this vault's own code** (or any scratch repo) to see the graph + the incremental update loop.

**C11 ⭐** — Register the MCP server into **your own Claude Code** (single-client), point it at a scratch/vault clone, and **MEASURE the token delta** on ~3 real code-review questions with-vs-without the graph. **Pair with the ccusage → OTEL / claude-code-otel measurement layer** (the CC-observability pilot) so the token-reduction claim is *your* number, not the README's. This is the pilot that advances your cost-optimization thread with real data.

**C12** — Try the **community-detection** + **architecture-overview** tools on a scratch repo — do they surface a useful module map?

**C13** — Try the **optional local `embeddings` extra** (sentence-transformers) for hybrid graph+semantic search on the scratch repo (local, no cloud) — is the hybrid better than graph-only for your questions?

## D — hireui / Goal-#2 (fenced, behind hireui's CONSTITUTION)

**D14** — Read hireui's existing **GitNexus-first** setup (GitNexus v33 = a #23-family tool). code-review-graph is a direct **alternative/complement** — frame the comparison.

**D15** — On a **hireui staging clone** (`agent-*` branch, operator-installed per I-8, read-only), `build` code-review-graph over hireui and inspect the graph + blast-radius on a real hireui module.

**D16 ⭐** — **Bake-off code-review-graph vs GitNexus v33** on the hireui staging clone: same 3 review questions, measure token delta + answer quality + blast-radius accuracy. Decide whether to keep GitNexus, switch, or run both. A concrete Goal-#2 code-intel decision, on-goal, low-risk (read-only).

**D17** — If code-review-graph wins the bake-off, wire its **GitHub Action** into hireui's CI as a review-context provider (staging first) — composes with the loop-engineering v189 PR-babysitter + the freeCodeCamp Docker/CI-CD deploy-layer thread.

**D18** — Use its **multi-repo `crg-daemon`** if hireui is a monorepo (the memory note flags `/Users/Cvtot/monorepo/hireui`) — one daemon serving the whole monorepo's graph.

## E — Off-goal / personal

**E19** — Use the **wiki-generation** tool (local Ollama) to auto-generate an Obsidian companion for any codebase you're learning — a fast onboarding aid.

**E20** — Look at the author's portfolio (CrumbleUX VLM design-critique / MERIT / Jailbreak-Eval / GraphMinds) as landscape — a strong graph-engineering + AI-eval indie builder to watch (NOT a corpus subject; NOT #57).

## F — Vault-meta

**F21** — File the **#23 N=4→N=5** instance-strengthening (done in `_patterns/06` §F) + confirm the tally at the next audit.

**F22** — Note the **networkx-vs-SQLite store variant** + the **benchmarked-blast-radius** facet in the #23 registry row's variant list (a data-point for the eventual "code-graph store taxonomy" the family is accumulating: graph-in-memory [code-review-graph] vs SQLite [codebase-memory-mcp v172] vs the earlier graphify/GitNexus/codegraph variants).

**F23** — Record the **claude-context v40 vs code-review-graph** distinction (vector-first, excluded from #23, vs graph-primary-with-optional-vector, counted) as the clean line for future hybrid tools.

**F24** — Cross-ref the **ollama-wiki-generation + Obsidian export** to openwiki v195 + the vault's own LLM-Wiki pattern (a recurring "docs/wiki from a code graph" mini-thread).

---

### Ranking on the pilot ladder

Slots in as a **top-tier read-only capability pilot**, comparable to or ahead of **codebase-memory-mcp v172** (both read-only code-graph-via-MCP; code-review-graph is `pip`-only [no `curl|bash` binary] + MIT + maps directly onto the cost thread + a hireui GitNexus bake-off is available). Behind **SkillSpector v169** (lowest-risk, no config mutation) and **claude-tap v173** (protocol-inspector) only on absolute footprint; ahead of **devspace v171** (remote execute) and **Agent-Reach v174** (account-ban risk). The PILOT lever still stands (zero completed) — code-review-graph + the ccusage/OTel measurement layer is a clean way to advance both the cost-optimization thread and the standing pilot at once.
