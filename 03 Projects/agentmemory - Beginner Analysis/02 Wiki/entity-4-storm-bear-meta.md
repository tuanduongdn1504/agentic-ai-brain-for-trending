# Entity 4 — Storm Bear meta-entity

> **Type:** Storm Bear meta-entity (Phase 0.9 STRONG INCLUDE — 4/4 STRICT PASS)
> **Cross-references:** [Entity 1 core](./entity-1-agentmemory-core.md) / [Entity 3 quality tension](./entity-3-distribution-and-quality-tension.md) / [CLAUDE.md Phase 0.9](../CLAUDE.md)

## Why this entity exists

Most wiki subjects get a Storm-Bear-relevance *paragraph* in the beginner guide. agentmemory gets a full **meta-entity** because it is the **most directly-deployable subject in the recent corpus** for the vault's exact situation: the Storm Bear vault is a persistent knowledge system that runs *on Claude Code*, maintains a `memory/` directory and CLAUDE.md working memory *by hand*, and agentmemory is *literally a tool that automates exactly that*.

## Phase 0.9 STRICT inclusion check — 4/4 PASS

| Criterion | Result | Evidence |
|---|---|---|
| **(a) Author archetype peer** | **PASS** | Rohit Ghumare — solo individual engineer, personal-email attribution, open-source tool. Structural peer to Storm Bear (solo developer + Scrum coach building and publishing a personal vault). Not corporate / not large-team / not pseudonymous / not academic. |
| **(b) Operational tool for vault** | **STRONG PASS** | agentmemory is persistent memory for Claude Code — the vault's **primary operating substrate**. The vault *already* maintains a `memory/` directory + CLAUDE.md working memory manually; agentmemory's 12-hook auto-capture would automate it. Not speculative-operational — **direct-operational**. |
| **(c) Methodology-influence-node** | **PASS** | The 4-tier consolidation model (Working/Episodic/Semantic/Procedural) + Ebbinghaus decay + triple-stream RRF search are memory-architecture methodologies *directly applicable* to how the vault structures its own memory — and could inform routine v2.3's memory discipline. |
| **(d) In-corpus reference** | **PASS** | Integrates deepest with Claude Code (the most-corpus-cited product, per v65). Structural **sibling to vault project graphify** — agentmemory's knowledge-graph search stream is the same primitive family graphify is built around. |

**Decision: 4/4 STRICT PASS → STRONG INCLUDE.** This is the **widest criteria-coverage in the post-amendment Phase 0.9 window** — v65 was 3/4, and most prior PASSes were 1-2/4. Categorized STRONG (not STRONGEST) because criterion (d) is *structural-sibling* depth, not the "documents THE most-corpus-cited product's internals" depth that earned v65 its STRONGEST rating.

**Streak:** v64 SKIP (RESET) → v65 STRONG PASS (1) → **v66 STRONG PASS (2)**. 10-instance window v57-v66 = 8 PASS / 2 SKIP = **80% INCLUDE rate**.

## The vault's current memory problem — stated honestly

The Storm Bear vault's memory today:
- **CLAUDE.md** — a hand-curated working-memory shim (refactored at session 67 because it had grown to 584 KB / ~146K tokens and was thrashing agents)
- **`_state/` chapter files** — bulk state, manually maintained, manually sized to fit in agent context
- **`memory/` directory** — the auto-memory system, written to by hand following the memory-management discipline
- **PATTERN_LIBRARY.md + chapters** — manually accumulated cross-wiki synthesis

This *is* the "Built-in CLAUDE.md" column of agentmemory's own competitive table — the approach agentmemory positions itself *against*. The README's claim — *"22K+ tokens at 240 observations"* for the manual approach — is a description of a real failure mode the vault has *already hit* (the 584 KB CLAUDE.md refactor is the evidence).

So the question is not academic.

## Should the vault deploy agentmemory? — pilot evaluation

agentmemory is a **strong pilot candidate** — arguably the highest-relevance pilot subject since the pilot framework began. But the Entity 3 risk register is real. Honest assessment:

### The case FOR a pilot

- **Exact-fit use case.** Auto-capture of vault work sessions (which wiki was built, what Pattern Library decisions were made, what the iteration log said) is precisely what the vault currently does by hand in iteration logs and `_state/` updates.
- **The `PreCompact` hook** directly addresses a known vault pain — context loss during long wiki-build sessions.
- **Local-first, free, offline.** Default embedding is local `all-MiniLM-L6-v2`; no API key required; Apache-2.0; SaaS "deliberately excluded." No vendor lock-in, no recurring cost.
- **The 4-tier model is a thinking tool even if not deployed** — Working/Episodic/Semantic/Procedural is a *better vocabulary* for the vault's own memory tiers than the current ad-hoc `_state/` + `memory/` + CLAUDE.md split.

### The case AGAINST (the risk register)

- **35 days old.** Pre-1.0, 34 releases in 5 weeks, breaking changes most weeks. Pinned to an old iii-engine because newer ones broke it.
- **Recent RCE.** v0.8.2 fixed an RCE and a memory-store-bound-to-`0.0.0.0`. The v0.9.x design is credible, but the track record is 5 weeks long.
- **It ingests everything.** A memory tool captures every prompt, every tool call, every file path. For a vault that is a *personal knowledge base*, the privacy-filtering (secrets/`<private>` stripped) must be trusted — and trust at 35 days old is thin.
- **DESIGN.md contamination** signals quality-control gaps in exactly the kind of unreviewed-artifact way that should make a careful operator pause.

### Recommended pilot shape (if pursued)

A **bounded, low-blast-radius pilot** — *not* a vault-wide deployment:
1. Run agentmemory **against a throwaay scratch project**, not the live vault, first — verify the privacy-filtering claim empirically before it sees vault content.
2. If that passes, run it **read-mostly on the vault** for 1-2 wiki builds — let it auto-capture, but keep CLAUDE.md / `_state/` as the authoritative manual record. Compare what agentmemory *would have* surfaced against what the manual iteration log captured.
3. **Decision gate:** does agentmemory's recall beat `grep` over the vault for "what did we decide about Pattern #18 at v53"? If yes, deepen. If no, the manual system wins and the 4-tier *vocabulary* is the takeaway.

**Verdict: pilot-worthy, but as a fenced experiment, not a substrate swap.** The architecture earns the pilot; the 35-day track record earns the fence.

## What the vault should take regardless of the pilot

Even if agentmemory is never deployed, the **4-tier consolidation vocabulary is worth adopting as a thinking tool** for the vault's own memory:

| agentmemory tier | Vault analogue today | Could be sharpened to |
|---|---|---|
| Working | raw build-session activity | (ephemeral — not currently retained) |
| Episodic | `01 Analysis/(C) iteration-log.md` per wiki | "what happened in build vN" |
| Semantic | `_state/` chapters + PATTERN_LIBRARY.md | "what the corpus knows" |
| Procedural | `05 Skills/llm-wiki-routine-v2.2.md` | "how the vault builds wikis" |

The vault already *has* these tiers — it just doesn't *name* them. agentmemory's contribution to the vault's methodology (criterion (c)) is the **naming**, and the **decay/strengthen/evict** discipline: the vault has no mechanism for *forgetting* stale state, and the 584 KB CLAUDE.md refactor is what happens without one. Routine v2.3 could borrow "auto-evict when stale" as an explicit `_state/` discipline.

## Pattern Library implications snapshot

- **Phase 0.9 — 4/4 STRICT PASS, STRONG INCLUDE** — widest criteria-coverage in the post-amendment window; streak advances to 2; 10-instance window holds at 80%.
- **Pilot candidacy** — highest-relevance pilot subject in recent corpus; recommended as a *fenced* pilot (scratch project → read-mostly vault → decision gate), not a substrate swap. Adds to the pilot queue (joins the 8 pending candidates noted in vault CLAUDE.md).
- **Routine v2.3 input** — "auto-evict when stale" as a candidate `_state/` discipline; the 4-tier vocabulary as a candidate memory-organization frame.
- **Pattern #57 Recursive Corpus Reference** — agentmemory's competitive table explicitly names the vault's own current method ("Built-in CLAUDE.md"); the graph stream is a graphify sibling.

## Why this entity matters

This entity answers the question Entity 1 set up and Entity 3 risk-rated: **the vault has a real memory problem, agentmemory is a real candidate solution, and the honest answer is "pilot it behind a fence."** It is also the cleanest Phase 0.9 4/4 STRICT PASS the post-amendment window has produced — useful calibration evidence that the STRICT amendment correctly *includes* a subject when all four criteria genuinely converge, rather than only firing on corpus-recursive edge cases.
