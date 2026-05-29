# (C) Phase 0 + Phase 0.9 INCLUDE verdict — OpenHuman (v118)

**Routine:** v2.4. **Fetched:** 2026-05-29. **Verdict:** **STRONG INCLUDE 3/4** ((a) FAIL + (b)(c) STRONG + (d) STRONGEST). 2nd consecutive clean PASS after the v116 Sana OVERRIDE.

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `tinyhumansai/openhuman` |
| License present | ✅ **GPL-3.0** (GitHub API + README agree) |
| Active / recently pushed | ✅ pushed 2026-05-29; created 2026-02-18 (~100 days; v0.56.0 release) |
| Scale floor (≥1★) | ✅ **29,402★** |
| Tier classification | **Agent harness (T1/T2)** — desktop agentic assistant with persistent memory; sibling to v107 claude-code-harness + v99 cmux + Tauri-desktop v73/v117 |

**Phase 0 = PASS.** Squarely in-scope: a Claude-Code-compatible autonomous agent harness with a persistent-memory layer + MCP + `.claude/`/`AGENTS.md` artifacts.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **FAIL**

Steven Enamakel (@senamakel) — **Dubai-located**, bio "Builder & Hustler", founder of the org **tinyhumansai**; account 2017, 50 repos, 213 followers; linktr.ee/enamakel. Indian-heritage-diaspora name, Gulf-located, running a commercial org with a hosted backend + subscription.

Not a VN/Asian-LOCATED cultural-peer. Consistent with the diaspora-founder FAIL precedents v98 mukul975 (Indian-Berlin), v112 tashfeenahmed (Pakistani-Dublin), v113 rohitg00 (Indian-London). **Dubai/UAE/Gulf is a corpus-novel locale but N=1** — per the (a)-8 South-American N=1-retirement precedent, **no new (a) sub-axis coined** (avoid cascade-dilution; note as an observation only). **(a) FAIL.**

### (b) Goal-relevance / vault-utility — **STRONG**

This is the strongest (b) in several wikis, because OpenHuman sits at the intersection of *both* of the operator's anchors:
- **Goal #1 (Claude + autonomous agents):** via the agentmemory backend it can give **Claude Code** (which Storm Bear uses) persistent, cross-tool memory; it's a working agent harness over the operator's actual tools (GitHub/Notion/Linear/Slack/Calendar).
- **Vault methodology (Karpathy LLM-wiki):** the Memory Tree (≤3k-token Markdown chunks + hierarchical summary trees + Obsidian vault) is a productized, auto-ingesting version of the exact pattern this vault runs by hand.

**Tempered from STRONGEST**, honestly, by: managed-by-default backend (model routing + web search + OAuth proxied through OpenHuman-hosted servers on a paid subscription), early-beta status, and a 118-service OAuth trust surface. Cost-of-trial is MODERATE-HIGH and the "Private" framing is caveated (below). High directness → **STRONG**, not WEAK; real caveats → not STRONGEST.

### (c) Instructive / exemplary — **STRONG**

A genuine reference design for **productizing the LLM-wiki / persistent-memory pattern**: Memory Tree (canonicalize → chunk ≤3k → score → summary tree → SQLite + Markdown), TokenJuice compression (HTML→MD, dedup, summarize, CJK-safe, "up to 80%"), Composio connector layer for 118 services, model routing by workload. Directly instructive for the vault's own methodology and for anyone building agent memory. **STRONG** (arguably STRONGEST on methodology-relevance, held at STRONG because it's early-beta and product-purpose differs from the vault).

### (d) Corpus connectivity — **STRONGEST**

Exceptional density:
- **Karpathy obsidian-wiki / LLM-wiki** — the corpus's foundational Pattern 1, explicitly cited → corpus-recursive at the methodology-influence layer (cf. v94 Understand-Anything, v78 ECC).
- **agentmemory** (`rohitg00/agentmemory`) backend → v66 agentmemory + Pattern #85 Platform-Primitive Foundation. *(rohitg00 is also the v113 author; v66↔this-agentmemory identity flagged for audit.)*
- **Claude Code / Cursor / Codex / OpenCode** multi-harness → Pattern #84 cross-vendor ecosystem-tolerance.
- **.claude/ + AGENTS.md + CLAUDE.md + .agents/ + MCP Registry** → Library-vocab #12 + Pattern #18 B1 MCP + agentskills.io adjacency.
- **TokenJuice** → v97 distill + Token-Economy-Quantification.
- **Tauri desktop** → v73 cc-switch + v117 CodexPlusPlus (LV-C7 cluster → N=3).
- agent harness → v107, v99. Pattern #52 HIGH-NOT-EXTREME; Pattern #82.

**(d) STRONGEST.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer | **FAIL** (Dubai/Indian-heritage diaspora founder; Gulf N=1, no new axis) |
| (b) goal-relevance / vault-utility | **STRONG** (Claude-Code memory ∩ Karpathy-wiki methodology; tempered by managed-default + beta) |
| (c) instructive | **STRONG** (productized LLM-wiki/persistent-memory reference design) |
| (d) corpus connectivity | **STRONGEST** (Karpathy lineage + agentmemory v66 + multi-harness + MCP + TokenJuice + Tauri) |

**STRONG INCLUDE 3/4.** (a) FAILs honestly (mirrors v113); INCLUDE rests on (b)(c)(d) with (d) STRONGEST.

**Finding-2 calibration note:** (a) genuinely FAILED (Dubai diaspora founder, not laundered to a soft PASS); (b) deliberately held at STRONG not STRONGEST because the managed-by-default backend undercuts the "Private" pitch and it's early-beta. Healthy rubric discrimination.

**Streak:** "45+2\*" → **"46+2\*"** (46 PASS + 2 OVERRIDE; v118 = 2nd consecutive clean PASS after the v116 Sana override). Pre-existing 44-vs-45-PASS discrepancy + 2-data-point override-frequency review remain flagged for the ~v119–v120 audit.

**Pilot:** **HIGH-RELEVANCE but fenced/careful** — the most methodology-relevant pilot candidate since v94, because it productizes the vault's own Karpathy-LLM-wiki pattern AND can back Claude Code with memory. BUT: pilot ONLY in BYO-models/local mode, `install-snapshot` first, and do NOT OAuth sensitive accounts initially — the managed default proxies model calls + search + 118 OAuth flows through OpenHuman-hosted servers, and it's early-beta. Tempting, trust-carefully. Product purpose (personal-assistant auto-memory) differs from the vault (curated research corpus) — study the technique + the Claude-Code memory backend; it does NOT replace the vault.
