# (C) agentic-local-brain — Verdict

> **v234 · 2026-08-17 · `agent-creativity/agentic-local-brain`** · routine v2.7
> Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions`. No workflow, no subagent (the ~970 KB shim overflows every subagent >200 K → the standing v200→v233 self-throttle). Source hand-fetched; identity + landscape by WebSearch; collision by sanity-anchored hand-grep.

---

## Verdict

**GOAL-ALIGNED INCLUDE 3/4** — **(a) FAIL · (b) MODERATE *keys the tier* ⚠️STRONG-reviewable · (c) MODERATE ⚠️STRONG-reviewable · (d) STRONG**

**NO MINT.** Counts **46 / 11 UNCHANGED**. §C live standalones **49** unchanged. Surface **≈56** unchanged.

**Tier T5 Application** (local-first personal-knowledge-base app — the meetily v196 / AIRI v210 / Ghost-Downloader v219 consumer-prosumer tier), with a **T1 agent-skill facet** (`localbrain-collect`).

**Streak: v233 GA:91 → `GA:92 · OG:13 [7 ov]`** — 15 consecutive GA. **§35 CLEAR** (window {v232 GA, v233 GA, **v234 GA**} = 0 OG).

---

## Criteria

### (a) FAIL
`agent-creativity` — display name **Allen Xu**; an individual, 6 followers, whose other 8 public repos are mostly forks of database/Docker infrastructure tooling. **Not Anthropic.** Per **§41**, no rescue is taken from name, heritage, locale, or notability; the disclosed-individual axis stays answered NO. **#19 19a** — first `agent-creativity` / Allen-Xu author.

### (b) MODERATE — keys the tier
**For:** this is the vault's own founding pattern, productised. The `wiki compile` feature (topic clusters → LLM-synthesised articles + entity cards + wiki-links + **staleness tracking + automatic recompilation**) mechanises four jobs `CLAUDE.md` assigns to the maintainer by hand. It lands on the live **CC-memory-systems** thread, ships a real **Claude-consumable agent skill**, and its design gist makes an articulate **CLI-as-agent-protocol** argument that is directly on the agent-interface substrate.

**Held below STRONG by:** the DOMAIN is personal knowledge management, not Claude/agent substrate and not software-dev; **Claude is one of six** named agents (*"OpenClaw / Hermes / Claude / Qoder / Codex / Trae"*); it ships **no MCP**; and it is a **75★ / 92-commit / 0-release / two-weekend** entrant in a genre whose incumbents sit at 34k★ and 63k★ — nothing here is a credible tool adoption.

**Calibration is decisive:** **v134 obsidian-second-brain** took **(b) STRONG** for the same PKM domain — but v134 is a *Claude Code skill* (corpus-core medium), ~1,700★, 43 commands, explicitly Karpathy-lineage. v234 is a standalone Python app where Claude is one-of-six with no MCP. It must sit **below** v134 → **MODERATE**. Cleanly GA via §31; **no §40 needed** (v134 established that PKM + an agent skill + Karpathy lineage clears the MODERATE floor comfortably).

⚠️ **(b) STRONG is the reviewable alternative** (the "it *is* the vault's own pattern, mechanised" reading). ⚠️ An OFF-GOAL reading is **not** defensible — v134 set the floor.

### (c) MODERATE ⚠️STRONG-reviewable
Real breadth for the effort: 6 collectors · 3-tier extraction · a modern RAG stack (query expansion → RRF hybrid over FTS5+vectors → LLM reranking → context enrichment) · knowledge graph + HDBSCAN topic clustering · the wiki compiler · CLI **and** FastAPI dashboard · cron backups to local/OSS/S3 · cross-platform binaries · a versioned skill.

Held at MODERATE: **two weekends / 92 commits / 0 releases / 75★ / 1 watcher**; every hard part is an upstream library (ChromaDB, LiteLLM, HDBSCAN, FastAPI, Click, PyInstaller) — this is orchestration and glue; no benchmarks, no evals; and ⚠️ **NOT source-cloned**, so all internals are page/doc-stated.

### (d) STRONG
Dense, verified cross-refs: the Pattern #57 Karpathy-productization vector (**v94 consume / v118 generate / v134 generate-purest / v137 source→skill / v195 code-scoped**) · **v136 Odysseus** (closest storage-stack cousin: ChromaDB+fastembed memory, email/calendar/notes) · **v228 pi** (MCP-exclusion pole) · **v222 lobehub** / **v221 llm-space** (self-hosted + non-US-cloud egress) · **v233 ClawWork** (the fail-soft ↔ fail-closed contrast) · **v209** (agent-instruction-injection defence) · agent-skills substrate · #12 · #66 · #84 84c.

---

## Pattern outcome — NO MINT

Declined on **four independent grounds**:

1. **Not corpus-first for the domain.** **v134** (Obsidian second-brain skill, explicitly *"an evolution of Karpathy's LLM Wiki pattern"*) and **v118** (OpenHuman's Obsidian-compatible Memory Tree) both precede it in PKM. A "corpus-first PKM" claim would have been a straightforward over-claim — caught by the grep, not assumed.
2. **Domain-not-capability.** PKM is a domain; §C vocabulary is agent-capability-shaped (the meetily v196 / TimesFM v193 / AIRI v210 / little-book-rl v220 / Ghost-Downloader v219 discipline).
3. **Not world-first, and not the exemplar.** Khoj (~34k★, YC W24), AnythingLLM (~63k★), Quivr, PrivateGPT, Onyx, SurfSense, Reor, LocalRecall — plus a *named* 2026 category ("Karpathy-style LLM knowledge base apps") with its own awesome-list. At 75★ this is a minor entrant. The **Kilo Code v177 / agency-agents v185** "mint the world-class exemplar at N=1" precedent explicitly does not reach it; the applicable precedent is **v180** — interesting small project, weak anchor, declined, mint left for a cleaner exemplar.
4. **§28** anti-inflation.

**What it IS:** the **4th "generate" instance** on the already-registered **Pattern #57 sub-variant "Productized/Automated Karpathy-LLM-Wiki-Pattern at the Methodology-Influence Layer"** (v118 → v134 → *[v137 as a distinguished one-shot variant]* → **v234**). N-tally is **audit bookkeeping — recorded, NOT self-incremented**.

⚠️ **This lands directly on a question the corpus already deferred.** The **v137** entry deferred *"promote-broad-class-vs-split"* on this exact vector to the *"~v139–v140 audit"* — which never resolved it. v234 is a 4th data point, and a structurally new one: v118 = an agent harness's memory, v134 = a skill over *your existing* vault, v137 = a one-shot source→skill converter, **v234 = a standalone application with its own store that compiles and *maintains* the wiki as a product feature.** **Flagged to the badly-overdue audit.**

⚠️ **§C-mint alternative recorded, operator/audit-reviewable, NOT self-executed:**
> *"Local-First Personal-Knowledge-Base Application with an Auto-Compiled, Staleness-Tracked LLM Wiki" (N=1).*

Defensible only on the narrow observation that the staleness-tracking + auto-recompilation of *derived* articles is the one thing the 34k★/63k★ incumbents largely leave to the user. It **loses** on all four grounds above, and minting it would be drawing-the-circle-to-make-it-first (the **camofox v179** discipline). Recorded, declined.

---

## Secondary (recorded, NOT minted)

- **#19 19a** — first `agent-creativity` / Allen Xu author; first standalone **PKM application** subject (v134 = a skill over an existing vault; v136 = a chat workspace).
- **DEFERRED watch axis — "CLI-as-agent-protocol as a deliberate alternative to MCP."** The gist argues it explicitly: *"CLI is the greatest common denominator interaction protocol between different software"* — self-describing (`--help` is the prompt), self-contained, no auth/SDK/JSON. Second independent voice alongside **pi v228**'s MCP-exclusion pole, from the opposite end of the size spectrum. ⚠️ Cross-reference only — **no N-bump asserted** (runtime vs utility; different shapes).
- **#84 84c** provider-agnostic via LiteLLM — **NO N-bump**. ⚠️ Defaults to **DashScope (Alibaba)**; the llm-space v221 / lobehub v222 egress fence, more acute here because the payload is your private corpus.
- **Agent-skills substrate** cross-ref — `localbrain-collect` v0.7.1, an intent-recognition decision tree + the restraint rule *"DO NOT pass `--tags` or `--summary` by default"*. **NO N-bump.**
- **#12** LLM-routing artifacts — ships **both** `AGENTS.md` and `CLAUDE.md`. **NO N-bump.**
- **v233 ClawWork contrast** — fail-**soft** ingestion vs fail-**closed** evaluation. Two consecutive ships, opposite defaults, both correct.
- **Solo-dev-with-AI** data point (the tabularis v212 shape): *"two weekends, 110 commits"*, *"AI doesn't replace you—it lets one person do a team's work."* ⚠️ **110 (gist) vs 92 (repo page)** — unreconciled, flagged.
- **🔴 #66 — MODERATE-to-SEVERE, the load-bearing risk.** All four installers and the agent-skill install instruction use **plaintext `http://`** (`curl … | sh`, `irm … | iex`) from a public Alibaba OSS bucket → MITM = arbitrary RCE, and in the agent path, **arbitrary instruction injection into your agent** (the v209 attack class). Plus **0 releases** (nothing pinnable, no checksums), **email + personal-document ingestion**, **DashScope-by-default egress**, and a **contested name** in the wild (`braindead-dev/localbrain`, `mudler/LocalRecall`) making the bucket URL an easy typosquat target. Mitigating: MIT, no telemetry found, the app itself is a local Python program.

## NON-claims

NOT **#52** (75★ page-stated §37.4 — a smallness fact, not velocity) · NOT **#57 promotion** (an instance of an existing sub-variant; N = audit) · NOT **#18 B1-MCP** (ships no MCP and argues against it) · NOT **world-first** · NOT **corpus-first for PKM** (v134/v118 precede) · NOT the **genre exemplar** (Khoj / AnythingLLM) · NOT a new **top-level pattern** (max #85) · NOT **source-cloned** (flagged) · NOT **Anthropic-affiliated**.

---

## Verification note

Collision by **sanity-anchored hand-grep** — anchors `openwiki` (13/18), `supermemory` (9/16), `agentmemory` (19/56), `claude-context`, `Karpathy` (5/46) all hit richly, so the zero results are trustworthy: `agentic-local-brain` / `localbrain` / `local-brain` / `agent-creativity` / `khoj` / `danswer` / `privategpt` / `quivr` / `anythingllm` / `personal knowledge management` = **0**.

**Three errors caught by hand:**
1. **The "corpus-first PKM" over-claim** — the `second brain` / `PKM` hits looked incidental but resolved to **v134** and the registered Pattern-#57 generate-vector. Caught before it reached the verdict; it would have inverted the mint decision.
2. **The `http://` installer scheme** — re-verified with a second, scheme-specific fetch, because a summarising model normalising `http`→`https` is exactly the failure mode that would have buried the single most important finding.
3. **The commit count** — gist 110 vs page 92; flagged rather than quoted.

**`inflation_check` HELD** — 0 mints; the §C mint declined per §28 and recorded as the reviewable alternative; counts 46/11 unchanged; max #85; no N-bumps taken on #84 / #12 / #57 / agent-skills.

---

## Pilot

⚠️ **pilot-AVOID as a tool. Read-and-borrow only.** The plaintext-HTTP `curl|sh` install is disqualifying on its own; if a local PKM/RAG layer is ever actually wanted, Khoj or AnythingLLM are the serious choices; and the operator already runs the best instance of this pattern — this vault.

⭐ **A1 → B5 → D9**
- **A1** — read the design gist's CLI-as-agent-protocol argument + the graceful-degradation table (~30 min, zero install).
- **B5** — steal **staleness tracking + auto-recompilation** into the vault's own wiki discipline: derived artifacts (the §C registry, the shim head, Pattern Library rows) carry a source fingerprint and get **flagged stale** when sources change. The C22–C27 stale-row backlog and the "stale claims" lint duty are exactly this problem, currently hand-run and overdue.
- **D9** — adopt the **3-tier ladder** (user-provided → LLM → deterministic fallback) as the *ingestion-side* default in hireui's CV-parsing ADR, explicitly paired with **ClawWork v233's fail-closed eval gate**: **ingestion fails soft, evaluation fails closed.**

Also **A3** (the entity-card + wiki-link + cluster→article compile shape as a vault design reference) and **F22** (file the v137-deferred broad-class question with this 4th data point).

**Fence:** never run the `http://` installers. If ever trialled: source clone at a **pinned commit**, `pip install -e .`, **scratch machine**, **no email ingestion**, **no DashScope key** (point LiteLLM at a local or OpenAI endpoint), and never point it at candidate data (hireui CONSTITUTION I-2 / I-8 / GitNexus-first).
