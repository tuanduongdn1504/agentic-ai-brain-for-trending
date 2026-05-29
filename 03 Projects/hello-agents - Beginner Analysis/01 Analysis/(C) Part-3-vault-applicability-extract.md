# (C) hello-agents Part 3 — vault-applicability extract (Ch 8 / 9 / 12)

**Read 2026-05-29** (post-v111 ship) from `docs/chapter{8,9,12}/Chapter*-EN.md`. Purpose: not a chapter summary — a map of what Part 3's frameworks say about **the vault's own LLM Wiki Routine**, with concrete actions. The value is at the **conceptual/discipline layer**, not the implementation layer (the Qdrant/Neo4j/SQLite backends, HyDE, BFCL/GAIA harnesses are for building agent *products*, not a file-based Obsidian vault).

---

## The big picture: the vault already IS a cognitive-memory architecture

hello-agents Ch 8 grounds agent memory in cognitive science: **working → episodic → semantic** memory, with **consolidation** (promote short-term items past an importance threshold into long-term) and **forgetting** (importance / time / capacity-based eviction). The vault implements this almost exactly, just in Markdown:

| hello-agents (Ch 8) | Vault analog |
|---|---|
| **Working memory** (current task, TTL) | the live session context |
| **Episodic memory** (specific events, temporal) | per-wiki **project entries** (`03c-projects-*`) — each ship is an "event" |
| **Semantic memory** (abstract rules/concepts) | the **Pattern Library** (patterns/sub-mechanisms abstracted across wikis) |
| **Consolidation** (importance ≥0.7 → long-term) | **audits** promoting PROVISIONAL → CONFIRMED at N-thresholds |
| **Forgetting** (importance/time/capacity eviction) | routine §18 **forced-retire** (10–15-wiki distance) + §19 **CONSOLIDATION** |

**Verdict:** this is genuine architectural validation — the routine's episodic→semantic-via-audit design matches a cognitive-science-grounded agent-memory architecture. Good. The gaps below are all in the *forgetting/compaction* half, which is exactly where Ch 8/9 say systems fail.

---

## Finding 1 (Ch 9, highest-value) — the root CLAUDE.md shim is re-bloating toward the session-67 context-rot failure

Ch 9 names the vault's #1 documented problem: **Context Rot** — "as tokens increase, the model's ability to accurately recall information decreases… a performance gradient, not a cliff." The session-67 refactor (584 KB / 146 K-token CLAUDE.md → `_state/` chapter shim) was *already* a context-rot mitigation. **But the shim has re-bloated.** The PL state-block, "Latest activity," and "Weekly Update" each now carry ~6-deep `Prior: … Prior: … Prior:` chains — the exact accumulation pattern context-rot punishes.

Ch 9's prescriptions, all of which the vault espouses but the shim violates:
- **JIT (Just-in-Time) Context** — "maintain lightweight references; load detail on demand." The shim's job is to be pointers; instead it inlines full per-wiki narratives that already live verbatim in the chapter file.
- **Compaction over chaining** — "summarize at high fidelity, restart with the summary." The vault *chains* (`Prior: … Prior:`) instead of *compacting*.
- **Reserve ratio** — protect the load-bearing instructions (the actual rules, folder structure, prime directive) from being pushed down by transient ship-narrative.

**Action:** at the next audit (~v115), compact the shim — collapse the `Prior:` chains in the PL state-block + Latest activity to a 1–2-line current state + a pointer to the chapter file (the detail is already there). This is the session-67 lesson recurring; the prime directive is "don't repeat the same mistake twice."

## Finding 2 (Ch 12) — the 97.7% INCLUDE rate is a judge-calibration flag worth naming

The Phase 0.9 verdict is textbook **LLM-as-a-Judge**: Claude scoring subjects on a 4-dimensional rubric (a/b/c/d) → INCLUDE/SKIP. Ch 12 is explicit that LLM judges carry **biases** and that for comparative eval **"Win Rate ≈ 50% is the ideal."** A filter that INCLUDEs **42 of 43** is, by that lens, barely discriminating — a possible **leniency/verbosity bias** (and the verdicts trend STRONG/STRONGEST).

Honest counter-point: the rate is *partly* explained by **operator-curation** — subjects are hand-picked, so the filter sees a pre-filtered stream, not a random one. So it's not pure judge-leniency. But the vault already runs the right Ch 12 mitigations and should lean on them harder: the **CORPUS-FIRST claim pressure-test** and **fact-verification streak** are exactly the "normalize-then-compare" + "human/independent verification" mitigations Ch 12 prescribes. **Action:** keep treating a near-100% INCLUDE rate as a *calibration question*, not a trophy — and periodically run a genuine SKIP-candidate to verify the rubric still discriminates (the v84 OVERRIDE is the only recent non-PASS).

## Finding 3 (Ch 8) — the ~103-item Library-vocab PROVISIONAL backlog is a forgetting-failure

Ch 8: when a memory store exceeds capacity, **capacity-based eviction** fires (purge least-important) and **consolidation** promotes the important. The Library-vocab layer has **~103 PROVISIONAL items** with consolidation "RE-DEFERRED" across multiple audits (flagged CRITICAL #1 v2.4 debt). The routine *has* the mechanisms (§18 forced-retire, §19 consolidation) — they just aren't firing at the cadence the backlog demands. Ch 8's framing makes the cost concrete: an un-consolidated long-term store degrades retrieval for *everything*. **Action:** the dedicated v2.4 Library-vocab session is overdue; treat it as eviction+consolidation, not just cataloging.

## Finding 4 (Ch 9) — adopt the note-classification taxonomy for the Weekly Update

Ch 9's structured-note taxonomy — `task_state / conclusion / blocker / action / reference`, with **blocker = highest priority** — is a sharper version of the vault's Weekly Update bullets ("What's working / not working / sitting on / next action"). The one addition worth stealing: an explicit **`blocker`** category. The ~103-item Library-vocab consolidation is a standing *blocker* that keeps getting demoted into "what's not working"; naming it a blocker (highest priority) per the taxonomy would stop it sliding.

---

## What's NOT applicable (honest scoping)

- **Memory backends** (Qdrant vector + Neo4j graph + SQLite) — the vault's "store" is Markdown files + git; no need for a vector DB.
- **Retrieval algorithms** (HyDE, Multi-Query Expansion, hybrid TF-IDF+vector+graph) — overkill for `grep`/`awk` over a file tree; the *concept* (expand-retrieve-merge, metadata-rich entries) is already met by dated entries + the chapter index.
- **Benchmark harnesses** (BFCL / GAIA / AgentBench / WebArena) — these evaluate agent *products*; the vault's "eval" is the audit, and Ch 12's *rubric/judge-bias* layer is the transferable part, not the benchmarks.

## One-line takeaway

Part 3 doesn't hand the vault new machinery — it hands it **the right names and failure-mode vocabulary for what it's already doing**, and the names point at three real, deferred problems: shim context-rot (compact it), judge-leniency calibration (the INCLUDE rate), and the Library-vocab consolidation blocker (evict + consolidate). All three are v115-audit / v2.4 items already on the books; Part 3's contribution is making the *cost* of deferring them concrete.
