# (C) Phase-0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `DeusData/codebase-memory-mcp` — *"The fastest and most efficient code intelligence engine for AI coding agents."*
**Ship:** v172 · 2026-06-20 · routine v2.6 §31 (two-tier INCLUDE, keyed on (b))

---

## Verdict line

**GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG. Tier: T2 Service.**

The §31 tier is keyed on **(b) goal-relevance only.** (b) STRONG → **GOAL-ALIGNED INCLUDE**. (a)'s FAIL is non-decisive.

---

## (a) — author cultural-peer axis: **FAIL**

"DeusData" is a bare GitHub **org/brand**: **no disclosed individual identity, no stated affiliation.** Not Anthropic; the only major-vendor (a) carve-out — **(a)-7 "Foundational-Vendor-Direct-Source" — is Anthropic-only.** There is not even a personal name to (mis)infer heritage from (so this is a *cleaner* FAIL than v170/v171, where a name inference had to be explicitly rejected).

Precedent-consistent with the recent run of clean (a) FAILs that all shipped GOAL-ALIGNED via (b): v140 Google, v143 ByteDance, v169 NVIDIA (corporate-not-Anthropic); v170 individual-dev, v171 indie-dev (individual / name-inference). **No (a)-rescue, no axis minted.**

## (b) — goal-#1 relevance: **STRONG**

Goal #1 = *"master Claude and autonomous agents for software development."*

- codebase-memory-mcp is **MCP infrastructure for coding agents** — core Claude/agent substrate.
- It **natively supports Claude Code** (first of 11 auto-configured hosts).
- It attacks the agent's **central cost bottleneck** — token spend on reading code — head-on (claimed ~99.2% reduction).
- It is **directly pilotable into the vault** and into **hireui** (index a real codebase so Claude navigates it cheaply), and sits on the operator's active **CC-memory-systems** + **multi-agent-orchestration** pilot threads.

**STRONG, not STRONGEST** — it is third-party (not the vault's own work / not an Anthropic substrate) and a **read-only augmentation** of agents that already exist. STRONGEST is reserved for Anthropic core substrate or the agent itself.

**(b) MODERATE+ ⇒ GOAL-ALIGNED INCLUDE.** This is the decisive axis.

## (c) — engineered-surface maturity: **STRONG**

C/C++ single static binary (zero runtime deps); 14 MCP tools; SQLite graph + read-only Cypher + Louvain community detection; hybrid LSP (9 langs) + 158 tree-sitter grammars; git-polling watcher; optional 3D UI; 35 releases (v0.8.1); SLSA-L3 + keyless Sigstore + VirusTotal 0/72 + CodeQL; 8+ distribution channels. Mature, not a prototype.

## (d) — pattern/synthesis value: **STRONG**

A clean §C capability standalone (the codegraph v70 species, now N=2) on a clean Pattern #18 B1-MCP variant instance (the variant is N≈9; sub-archetype B formal since v72, pure instance-strengthening). Unambiguous home; nothing forced. (Full reasoning: the PRIMARY doc.)

---

## §31 tier determination (the v169-cascade guard)

> **Decision rule:** INCLUDE with (b) MODERATE+ → **GOAL-ALIGNED**; INCLUDE with (b) FAIL → OFF-GOAL CAPTURE.

(b) = STRONG → **GOAL-ALIGNED INCLUDE.** The **v169 cascade error** — concluding "(a) FAIL ⇒ OFF-GOAL" — is explicitly **not** repeated: the v172 verification ran three independent lenses, **all** of which keyed the tier on (b), and the anti-inflation critic re-confirmed it. v168 ponytail (a FAIL · b STRONG) and v171 devspace (a FAIL · b STRONG) both shipped GOAL-ALIGNED on this exact shape.

## Streak / ceiling

- Streak `GA:33 · OG:11 [7 ov]` → **`GA:34 · OG:11 [7 ov]`** (34th GOAL-ALIGNED PASS; not an override; "49+3\*" frozen @v125).
- **§35 ceiling CLEAR** — rolling-3-ship window {v170 GA, v171 GA, **v172 GA**} = 0 OFF-GOAL. No ceiling-override.
- **19 consecutive goal-aligned ships v153→v172.**
- Override-frequency (2-in-20 / 3-in-30): v153→v172 = zero operator overrides.

## Pilot tag

**GOAL-ALIGNED ⇒ a legitimate goal-#1 pilot candidate.** HIGH-VALUE, **lower-risk than v171 devspace** (read-only, 100% local, no remote tunnel/write/execute), but **heavier install than v169 SkillSpector** (`curl | bash` of a compiled binary + auto-config of 11 agents). **Pilot order: SkillSpector first → codebase-memory-mcp second → devspace last.** Fence: install-snapshot + verify SLSA/Sigstore + single-client config + scratch repo + pin v0.8.1 (see the main wiki §9).
