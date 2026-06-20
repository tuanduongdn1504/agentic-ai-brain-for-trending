# (C) codebase-memory-mcp — LLM Wiki (v172)

> **Ship:** v172 · 2026-06-20 · branch `wiki/v172-codebase-memory-mcp` off `wiki/v171-devspace` (based at `fdf1331` = v171, which is itself unmerged — branching off `main` would orphan the v168→v171 cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** **1 NEW Library-vocab §C standalone (NOT corpus-first, N=2)** — *"Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP (SQLite + Cypher + LSP; token-reduction; 100% local)."* Anchors: **codegraph v70** (the un-registered *first* instance) + **codebase-memory-mcp v172** (the genuine 2nd cross-author instance). Plus a **clean Pattern #18 sub-archetype B / B1-MCP variant instance-strengthening → N≈9** (one-server-many-MCP-clients; sub-archetype B formal since v72, B1-MCP reconciled to N=7 at v151, + devspace v171 + this). Secondary scoped observations only (#84 / #66 / #20 / #19). NO new top-level pattern (max stays **#85**). Counts UNCHANGED (**46 / 10**); tracked PROVISIONAL §C surface ≈29 → ≈30 (+1 standalone).
> **Tier:** **T2 Service** (a self-hosted local code-intelligence MCP server / developer tool you install + run; **direct kin to codegraph v70** — same species — and to agentmemory v66).
> ✅ **Stays on the goal-#1 substrate core** — second consecutive core-substrate ship after v171 devspace. codebase-memory-mcp is dead-center on *"master Claude and autonomous agents for software development"*: it is MCP infrastructure that gives a coding agent a *queryable graph of your codebase* so it stops re-reading files.
>
> ⚠️ **(a) FAIL is genuine, not a downgrade.** "DeusData" is a bare GitHub org/brand with no disclosed individual identity — not Anthropic, not a registered cultural-peer (a)-axis. The tier keys on **(b)**, which is STRONG → GOAL-ALIGNED regardless. The v169 cascade error ("(a) FAIL → OFF-GOAL") is explicitly guarded against. See §5.
>
> 🔬 **Verdict adversarially verified** (3 distinct lenses + an anti-inflation critic). The critic returned AMEND on ONE point only: the capability had been loosely called a "RE-REGISTER of OC-K," but OC-K was never actually in the Library-vocab registry (a v2.4 phantom-count casualty), so the honest framing is a **new §C standalone at N=2** that credits codegraph v70 as the first instance. Everything else CONFIRMED.

---

## 1. What it is

`DeusData/codebase-memory-mcp` — tagline, verbatim:

> *"The fastest and most efficient code intelligence engine for AI coding agents."*

codebase-memory-mcp is a **self-hosted, 100%-local MCP (Model Context Protocol) server** that indexes a codebase into a persistent **knowledge graph** (SQLite-backed). Instead of an AI coding agent reading your files one-by-one (expensive in tokens, slow), the agent **queries the graph** — "who calls `main`?", "what changed in this diff?", "give me the architecture" — and gets a structured answer in **sub-millisecond** time.

The headline pitch is a **token-economy** one: the README claims **~99.2% token reduction** versus file-by-file exploration — roughly **~412,000 → ~3,400 tokens** across five typical queries — and a full index of the Linux kernel (28M LOC, 75K files) in about **3 minutes**.

It is written in **C (88.2%) + C++ (10.5%)**, shipped as a **single static binary with zero runtime dependencies**, supports **158 languages** via vendored tree-sitter grammars, and **auto-detects and configures 11 coding agents** (Claude Code first). License **MIT**, latest **v0.8.1** (2026-06-12).

This is the corpus's **second** subject of this exact shape — a pre-indexed, read-only code knowledge-graph that coding agents query over MCP. The **first** was **codegraph v70** (`@colbymchenry/codegraph`, *"Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local"*). codebase-memory-mcp is the **same species**, by a different author, at a larger and more security-hardened scale. (See §3 and §6.)

## 2. What it exposes (the MCP tool surface — 14 tools)

| Tool | What it does |
|---|---|
| `index_repository` | Index a codebase into a knowledge graph |
| `index_status` | Report indexing progress / state |
| `list_projects` / `delete_project` | Manage indexed projects |
| `search_graph` | Structured search by label, name pattern, file scope |
| `query_graph` | **Read-only openCypher** graph queries (MATCH/WHERE/aggregates/traversal — no writes) |
| `get_graph_schema` | Return the graph's node/edge schema |
| `trace_path` | BFS traversal of the call graph (who calls what) |
| `detect_changes` | Map a git diff to the affected symbols |
| `get_architecture` | Codebase overview with routes and hotspots |
| `get_code_snippet` | Retrieve source by fully-qualified name |
| `search_code` | Grep-like text search within indexed files |
| `manage_adr` | Persist & retrieve **Architecture Decision Records** in the graph |
| `ingest_traces` | Validate `HTTP_CALLS` edges against **runtime trace data** |

A representative Cypher query (verbatim from the README):

```cypher
MATCH (f:Function)-[:CALLS]->(g) WHERE f.name = 'main' RETURN g.name
```

Two tools stand out as more than "read-the-graph": **`manage_adr`** persists architecture decisions *into* the graph (the index becomes a small institutional-memory store, not just a code mirror), and **`ingest_traces`** fuses *runtime* observations into the static graph (validating HTTP call edges with real traffic). Both push the tool past "code search" toward "code memory."

## 3. The distinctive contribution (why it mints a §C standalone — and why it is NOT corpus-first)

The corpus's MCP servers split by **what they do for the agent**:

| Subject | MCP role | Relationship to this subject |
|---|---|---|
| **agentmemory** (v66) | conversational/agent **memory** backend (51 tools) | adjacent — memory, not *code* graph |
| **codegraph** (v70) | **pre-indexed code knowledge graph** (8 tools, tree-sitter → SQLite FTS5 → symbol/edge graph) | **same species — the first instance** |
| **supermemory** (v132), **nature-MCP** (v119) | memory / domain data | adjacent — augment a local agent |
| **google_workspace_mcp** (v140) | Workspace tools, tiered | adjacent — SaaS reach |
| **devspace** (v171) | file + shell + git over your machine | opposite vector — *manufactures* an agent |
| **codebase-memory-mcp** (v172) | **pre-indexed read-only code knowledge graph** (14 tools, C-binary, 158 langs, Cypher, hybrid LSP) | **the genuine 2nd instance of the codegraph v70 species** |

So the capability — *"a coding agent queries a pre-built, read-only graph of the codebase instead of reading files"* — is **not new to the corpus**. codegraph v70 did it first. At v70 it was flagged as an observational candidate (**OC-K, "Pre-Indexed-Context-Layer as agent augmentation strategy," N=1**) but, like most v70-era candidates, it was **never carried into the v2.4 Library-vocab registry** (the "~108 phantom count" the v2.4 consolidation cleaned up). The capability therefore has **no registry slot today**.

codebase-memory-mcp supplies the **clean 2nd, cross-author instance** that makes the capability worth tracking. The disciplined move (per §28) is to **mint a new §C standalone at N=2** — *not* a fresh corpus-first N=1 (which would wrongly erase codegraph v70's priority), and *not* a "re-registration of OC-K" (there is nothing in the registry to re-register). N=2 entry, anchors codegraph v70 + codebase-memory-mcp v172, **PROMOTION-ELIGIBLE at N=3.**

The standalone is the **capability**. The fact that it serves **11 MCP clients from one binary** is a separate axis (distribution structure) handled by Pattern #18 (§6) — no double-count.

## 4. How it works (architecture)

A RAM-first, multi-pass pipeline compiled into one static C binary:

- **Discover** — file discovery honoring a layered ignore stack: hardcoded (`.git`, `node_modules`) → `.gitignore` hierarchy → project-specific `.cbmignore` (gitignore syntax).
- **Pipeline (multi-pass indexing)** — structure → definitions → calls → HTTP linking. Infrastructure-as-code (Dockerfiles, Kubernetes manifests, Kustomize overlays) become **first-class graph nodes**, not just text.
- **Store** — SQLite-backed graph with traversal + **Louvain community detection** (clusters the graph into modules/communities). LZ4 compression in-pipeline; memory released after indexing.
- **Hybrid LSP** — lightweight semantic type-resolution for **9 languages** (Python, TypeScript/JavaScript, PHP, C#, Go, C/C++, Java, Kotlin, Rust) — resolves imports, generics, inheritance, stdlib — **without** spawning an external language-server process. (158 languages get tree-sitter structural parsing; 9 get the deeper type-aware layer.)
- **Cypher Engine** — a read-only openCypher executor (MATCH/WHERE/aggregates/relationship traversal; no writes).
- **Watcher** — background auto-sync via git polling; incremental re-index on change.
- **UI** — optional embedded HTTP server for a **3D graph visualization** at `localhost:9749`.

**Team-shared graph artifacts.** You can commit `.codebase-memory/graph.db.zst` (a zstd-compressed SQLite snapshot) to your repo; teammates **skip re-indexing** and incremental indexing fills their local diffs. The knowledge graph becomes a **git-tracked, shareable artifact** — a notable difference from a purely per-machine index.

**Install / use.** One-line `curl … | bash` (macOS/Linux) or PowerShell (Windows); also via **AUR, npm, PyPI, Homebrew, Scoop, Winget, Chocolatey, and `go install`**. Then: restart your agent and say *"Index this project."*

**Security / provenance** (notably mature — see §6 Pattern #66): VirusTotal **0/72**, **SLSA Level 3** provenance, **keyless Sigstore cosign** signatures, SHA-256 checksums, **CodeQL SAST** blocking on alerts, and **100% local processing** — code never leaves the machine.

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** The author is **"DeusData"** — a bare GitHub **org/brand** with **no disclosed individual identity** and **no stated affiliation**. It is not Anthropic and not any registered cultural-peer (a)-axis; the only major-vendor (a) carve-out, **(a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only.** Unlike v171 devspace (which at least disclosed an indie-founder identity), DeusData offers *no* identity to assess — there isn't even a name to (wrongly) infer heritage from. **(a) FAILs cleanly; no rescue, no axis minted** — consistent with v140 Google / v143 ByteDance / v169 NVIDIA (corporate-not-Anthropic) and v170/v171 (individual / name-inference) FAILs.
- **(b) STRONG.** Goal #1 = *"master Claude and autonomous agents for software development."* codebase-memory-mcp is **MCP infrastructure for coding agents** — core Claude/agent substrate. It **natively supports Claude Code** (first of 11 auto-configured hosts), it directly attacks the agent's central bottleneck (**token economy** — reading code is the dominant cost in agentic coding), and it is **directly pilotable into the vault** (index this vault's own code, or a real project like hireui, so Claude navigates it token-efficiently). Held at **STRONG (not STRONGEST)** because it is third-party (not the vault's own work / not an Anthropic substrate) and is a **read-only augmentation** of agents that already exist — STRONGEST is reserved for Anthropic core substrate or the agent itself.
- **(c) STRONG.** A mature, heavily-engineered surface: **C/C++ single static binary, zero runtime deps**; 14 MCP tools; SQLite graph store + read-only Cypher engine + Louvain community detection; hybrid LSP (9 langs) + 158 tree-sitter grammars; git-polling watcher; optional 3D UI; **35 releases** (v0.8.1); an unusually strong supply-chain posture (**SLSA L3 + keyless Sigstore + VirusTotal 0/72 + CodeQL**); and **8+ distribution channels**. Not a prototype.
- **(d) STRONG.** A clean **§C capability standalone** (the codegraph v70 species, now N=2) on top of a clean **Pattern #18 B1-MCP variant instance** (the variant is N≈9; see §6) — the pattern home is unambiguous and nothing is forced.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is **STRONG** (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s FAIL does **not** make a (b)-STRONG subject off-goal — that was the v169 cascade error, and the v172 verification confirmed all three independent lenses keyed correctly on (b).

## 6. Pattern Library outcome

**PRIMARY — 1 NEW Library-vocab §C standalone (NOT corpus-first, N=2):**

> **"Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP (SQLite + Cypher + LSP; token-reduction; 100% local)."**
> **Anchors:** codegraph v70 (`@colbymchenry` — the un-registered *first* instance; its v70-era OC-K observation was a v2.4 phantom-count casualty, never entered into the registry) + codebase-memory-mcp v172 (`@DeusData` — the genuine 2nd cross-author instance).

The capability is **not corpus-first** — codegraph v70 did it first. The §C entry is created now because the **2nd clean cross-author instance** makes a coherent, recurring capability worth a registry slot, and N=2 honestly credits v70's priority (vs a fresh-N=1 mint, which would erase it). **§28: 1 new standalone (≤2 cap honored). PROMOTION-ELIGIBLE at N=3** (a genuine 3rd pre-indexed-read-only-code-graph-for-agents). Time-aware stale-watch: ≥15 wikis AND ≥30 days (§39) — protected by the N=2 standing in any case.

**SECONDARY — clean Pattern #18 sub-archetype B / B1-MCP variant instance-strengthening → N≈9 (tracked at the #18 layer, NOT this standalone):** codebase-memory-mcp **auto-detects and configures 11 MCP clients from one binary** (Claude Code, Codex CLI, Gemini CLI, Zed, OpenCode, Antigravity, Aider, KiloCode, VS Code, OpenClaw, Kiro) = textbook *one-server-many-MCP-clients*. Sub-archetype B ("one-binary-many-CLIENTS") has been **FORMAL since the v72 audit**, and its **B1-MCP variant was reconciled to N=7 at the v151 audit** (agentmemory v66 / codegraph v70 / nature-skills v119 / supermemory v132 / google_workspace_mcp v140 / financial-services v141 / Scrapling v149); + devspace v171 + codebase-memory-mcp v172 → **N≈9** (exact post-v151 tally is an audit bookkeeping item — the v151 "filing-is-an-act" note). This is the **distribution structure**; the §C standalone is the **capability**. Different axes (the v140 / v171 precedent) → both recorded, no double-count. ⚠️ **Correction vs the loose v171 framing:** the sub-mechanism-B → formal-sub-archetype promotion already HAPPENED at v72 (it is **not** "long-deferred"), and a B1-MCP→own-sub-archetype split was **DECLINED at v151** (anti-inflation; B1 already captures the shape). So this is **pure instance-strengthening, NOT a pending promotion** — the stale "Pattern #18 sub-mechanism B promotion deferred" line carried in the v167 audit / v171 shim should be struck at the next audit.

**SECONDARY observations (NOT minted):**

- **Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation.** Auto-detecting + writing MCP config (with optional instruction-injection + non-blocking pre-tool hooks) into 11 agents = provider-agnostic by design. Scoped note, **NOT an N-bump** (the v86 audit's discipline: a single new count-increment / "most agents yet" is not, by itself, a CORPUS-RECORD mint). Also explicitly **NOT** the ponytail "14-platform native-rule-file distribution" mechanism — that framing was a build-workflow contamination caught + rejected at v169; do not repeat it.
- **Pattern #66 (supply-chain / security-conscious design) — cross-reference (notably strong).** SLSA Level 3 + keyless Sigstore cosign + VirusTotal 0/72 + SHA-256 checksums + CodeQL SAST blocking + 100%-local. This is one of the **most mature supply-chain postures** the corpus has seen for an installable agent tool — directly relevant because the install vector is a `curl | bash` of a compiled binary. Cross-referenced, **not** an N-bump of #66.
- **Library-vocab #20 "Token-Economy-Quantification" — QUALIFIED-ADJACENT (N stays 4).** The 99.2% / 412k→3.4k claim is a real, explicit token-economy quantification (a runtime/data-structure footprint axis), **but** it rests on a **single 5-query micro-scenario, page-stated, no independent replication** → logged QUALIFIED-ADJACENT with the **N-bump DEFERRED to audit**, per the **v168 ponytail conservative precedent** (anti-inflation). It does *not* advance #20 to N=5 at ship time.
- **Pattern #19 sub-archetype 19a (founder/ecosystem-portfolio) — minimal data-point.** "DeusData" is an org with no disclosed individual or visible portfolio; recorded as a thin data-point of a CONFIRMED pattern, no new sub-mechanism.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Max confirmed stays **#85**; the capability lives at the §C-standalone tier per §28 (the same anti-inflation that rejected #86/#88 at v168).
- **NOT Pattern #52 (viral velocity).** ≈**8.4k★ / 642 forks / 35 releases** (v0.8.1, 2026-06-12) are **page-stated, NOT API-verified** (§37.4 — this sandbox mocks the GitHub API). **No API-verified creation date → velocity unestablishable → explicitly not a #52 claim.** (Its direct kin codegraph v70 measured ~42 stars/day, *below* the >300/day EXTREME threshold — a useful sister data-point that this family is not, on the evidence, #52-tier.)
- **NOT Pattern #57 (corpus-recursion).** The 11-host integration list includes corpus subjects (OpenCode ~ v67, OpenClaw ~ v164 oc-claw, Codex) — but it lists them as **integration targets it augments**, not as **source material / influences it cites.** Mentions ≠ recursion (the v171 discipline).
- **NOT a re-classification / new tier.** A clean #18 B1-MCP instance + a §C capability standalone — nothing more.

**Counts UNCHANGED: 46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL §C surface ≈29 → **≈30** (+1 standalone). Pattern #18 B1-MCP variant → **N≈9** (sub-archetype B formal since v72; pure instance-strengthening, no pending promotion).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** ≈**8.4k★ / 642 forks / 35 releases** *(as of 2026-06-20 page render, github.com/DeusData/codebase-memory-mcp — confidence: stated, NOT API-verified)*. **MIT** license. Languages **C 88.2% / C++ 10.5%** (page-stated). Latest release **v0.8.1, 2026-06-12** (adds Java + Kotlin Hybrid LSP) — page-stated.
- **No API-verified creation date** → age & velocity **unestablishable** → **explicitly NOT a Pattern #52 claim.**
- **Author identity:** "DeusData" — a GitHub org/brand. **No disclosed individual, no stated affiliation** (confidence: stated — the *absence* of identity is itself what the repo page shows). The (a) FAIL does not depend on resolving who DeusData is (a non-Anthropic org/brand FAILs (a) regardless).
- **README contents** (§2 tool surface, §4 architecture, the Cypher example, the 99.2%/412k→3.4k figures, the security posture) are page-verified from the rendered README + repo page at ship time. Performance numbers (3-min kernel index, sub-ms queries) are vendor-stated benchmarks, not independently reproduced (recorded honestly).

## 8. Streak / state

- **Streak:** `GA:33 · OG:11 [7 ov]` → **`GA:34 · OG:11 [7 ov]`** (34th GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v170 GA, v171 GA, **v172 GA**} = **0 OG → STAYS CLEAR.** No ceiling-override needed or taken.
- **19 consecutive goal-aligned ships v153→v172.** v168/v169/v170 varied the domain off the v153→v166 operating/monitoring niche; **v171 returned to the goal-#1 substrate core** (MCP infra) and **v172 stays there** (a 2nd consecutive core-substrate ship, the codegraph v70 species).
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Max pattern #85. PROVISIONAL §C surface ≈29 → ≈30. Pattern #18 B1-MCP variant → N≈9 (pure instance-strengthening; sub-archetype B formal since v72).
- **Override-frequency triggers (2-in-20 / 3-in-30):** v153→v172 = **zero** operator overrides (clean).
- **Build note:** verdict produced **inline** but **adversarially verified by a 3-lens + critic workflow** (avoiding the v169 shared-premise cascade by giving each lens a distinct question; all three independently keyed the tier on (b)). The critic's one AMEND — "RE-REGISTER OC-K" → "MINT NEW §C standalone at N=2" — is incorporated above.

## 9. Pilot note

codebase-memory-mcp is a **HIGH-VALUE on-goal pilot candidate** and **lower-risk than v171 devspace** — but a **heavier install than v169 SkillSpector.**

- **Why high-value & on-thread:** it is directly pilotable into the vault and into **hireui** (index a real codebase so Claude navigates it token-efficiently). It is also squarely on the operator's **CC-memory-systems pilot thread** — a pre-indexed code knowledge-graph *is* a code-memory system (the "L-level" code-memory analogue of this very wiki's text-memory), and on the **multi-agent-orchestration / hireui** threads (give parallel agents a shared, git-tracked graph instead of each re-reading files).
- **Why lower-risk than devspace:** it is **read-only** (read-only Cypher; no writes), **100% local** (code never leaves the machine), and exposes **no remote tunnel, no shell-execute, no git-write** over your machine. The blast radius is far smaller than devspace's remote read/write/EXECUTE bridge.
- **Why not zero-risk (the install vector):** the default install is `curl … | bash` of a **compiled C static binary, system-wide**, from a **single org (DeusData) with no disclosed identity**, and it **auto-writes MCP config into 11 agents** (with optional pre-tool hooks). That is a meaningful install footprint.
- **Pilot fence (if attempted):**
  1. `install-snapshot` first (capture what the installer writes system-wide + into agent configs).
  2. Prefer a **package-manager install** (npm/Homebrew) over `curl | bash`, and **verify the SLSA-L3 provenance + Sigstore signature** the project publishes (it makes this unusually checkable).
  3. **Configure a single client** (Claude Code only) rather than letting it auto-configure all 11; review the injected config + any pre-tool hooks.
  4. Point it at a **scratch repo or a single project** first (not the whole machine); pin **v0.8.1**.
- **Ranking:** **SkillSpector (v169) remains the lowest-risk *first* pilot** (read-only Python scanner, no compiled-binary footprint). **codebase-memory-mcp is the natural SECOND pilot** (read-only + local, real on-goal value, but a heavier compiled-binary install that mutates agent configs). **devspace (v171) is last** (highest value *and* highest risk — remote read/write/execute). The PILOT lever still formally stands (zero piloted).

## Suggested next action

Review + merge the `wiki/v172-codebase-memory-mcp` branch (based on v171/`fdf1331`, itself unmerged — merging v172 brings the v168→v172 cumulative state along). Then the highest-value open move is the **standing PILOT lever**, now with a clean low-risk ladder: pilot **SkillSpector `--no-llm` over `05 Skills/`** first (lowest-risk loop-proof), then **codebase-memory-mcp read-only over the vault's own code or hireui** behind the §9 fence (the natural 2nd pilot — directly on the CC-memory-systems thread), keeping **devspace LOCAL-ONLY** as the high-value/high-risk finale.
