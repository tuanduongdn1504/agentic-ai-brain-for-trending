# (C) Phase 0 + Phase 0.9 verdict — dograh (v122) — **OPERATOR OVERRIDE**

**Routine:** v2.4. **Fetched:** 2026-05-30 (GitHub API + README + org page + AGENTS.md/CLAUDE.md + 2 SKILL.md). **Verdict:** STRICT **0/4 → SKIP**, force-built by **operator-elected OVERRIDE** (**3rd in corpus history** after v84 image-blaster + v116 Sana).

> **Version note:** built as **v122**, not v121 — `v121 CodexKit` shipped concurrently (commit `62d98a8`) during analysis. Streak base = "47+2\*".

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `dograh-hq/dograh` |
| License present | ✅ **BSD-2-Clause** (GitHub API `BSD-2-Clause`; clean single license) |
| Active / recently pushed | ✅ pushed 2026-05-29; created 2025-09-09 (~263 days); latest release v1.32.0 (2026-05-28) |
| Scale floor (≥1★) | ✅ **3,729★** / 773 forks (fork_ratio **0.21** — strong active-deployment) |
| Tier classification | **Corpus-outlier** — not in the agent-*for-coding* T1–T5 taxonomy. Forced-nearest = **T5 Application / T2 Service**. **CORPUS-FIRST voice-AI / telephony-agent platform** (first agent platform in the corpus for a non-software-dev domain). |

**Phase 0 = PASS on the mechanical gates, but FLAGGED out-of-domain.** Every prior corpus subject sits in the Claude-Code / agent-skills / autonomous-*coding* / LLM-tooling ecosystem. dograh is a voice/telephony agent platform — sales/support calling bots. It clears the mechanical floors but the *product domain* is the outlier.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **FAIL**

Owner = **dograh-hq** (`owner.type: Organization`) = **Zansat Technologies Private Limited**, a commercial startup "founded by exited founders, ex-CTOs, and YC alumni" (2024). India-linkage is plausible (the "Pvt Ltd" suffix + India/UAE go-to-market via the Cloudonix partnership) but HQ is unstated and founders are not publicly named. None of the corpus's (a) sub-axes apply:

- Not a VN/Asian *indie* cultural-peer ((a)-1…(a)-6): this is a VC-adjacent serial-/exit-founder commercial team, not a solo/indie builder at Storm Bear's scale-and-context. A possible India linkage is heritage-adjacent at best, and per the v98 / v112 / v113 precedents South-Asian-heritage commercial founders are **not** a registered (a) sub-axis and do not PASS (a).
- Not **(a)-7 Foundational-Vendor-Direct-Source** — the vault depends on Anthropic/Claude, not on dograh's voice platform. dograh is not a substrate the wiki routine runs on.

**(a) FAIL — clean.**

### (b) Goal-relevance / vault-utility — **FAIL**

Documented #1 goal: *"Master Claude and autonomous agents for software development."* dograh builds **voice agents for phone calls** (inbound/outbound telephony, call-transfer, IVR-style flows) — autonomous agents, yes, but for a *different domain* (sales/support calling), and the "for software development" qualifier is load-bearing.

- Not a vault tool, not a Scrum tool, not a coding assistant, not a dev-workflow utility.
- Storm Bear has no indicated voice-agent / telephony use case.
- Cost-of-trial is **MODERATE** to *stand up* (a Docker-Compose one-liner) but the platform is **useless to goal #1**, and doing anything real also needs telephony + STT/TTS/LLM provider credentials. Directness to goal #1 ≈ zero.

Weaker than the weakest recent INCLUDE — v112 freellmapi (a multi-provider LLM proxy) at least gave LLM inference for dev side-projects and scored (b) STRONG on "indirect-but-real dev-utility." A phone-calling-bot platform has no such dev-utility for Storm Bear.

**(b) FAIL.**

### (c) Instructive / exemplary — **WEAK (not a clean PASS)** — with a genuine but incidental thread

Two honest layers:

1. **The subject** (a voice-AI platform) teaches nothing transferable to the corpus's agent/skill/distribution/governance methodology — speech/telephony is a different field.
2. **The engineering exhaust** is the single genuinely-corpus-relevant thread: dograh's team operationalizes **Claude Code agent-skills as internal engineering discipline** —
   - `CLAUDE.md` is an 11-byte `@AGENTS.md` import (single-source-of-truth);
   - a **hierarchical `AGENTS.md` tree** (root → api → ui → deeper) with explicit parent/child ownership boundaries;
   - `.agents/skills/review-agents-md/SKILL.md` — a **drift-guard skill** auditing that tree against the live code (hierarchy tests: parent-fit / child-fit / no-duplication / downward-pointing / no-gaps / **no-drift**; finding-classes `stale` / `missing-child-agents` / `wrong-level` / `extra-detail`; "treat the repo as source of truth");
   - `.agents/skills/review-pr/SKILL.md` — a **domain-specific PR security/correctness audit** over 8 Dograh-specific failure modes (org-scoping, unauth routes, unsigned webhooks, SQL-layering, cache-staleness, unsafe migrations, SDK-bypass, secret-leaks), bucketed Blocker / Should-fix / Nit.

That exhaust *is* in the corpus's wheelhouse and is a useful real-world adoption specimen. **But it is exhaust, not the subject.** PASSing (c) on it would launder "this team uses Claude Code well internally" into "this voice-AI repo is instructive for our agent corpus" — and that would blow scope open, because a large and growing fraction of *all* repos now ship a `CLAUDE.md` + `AGENTS.md`. Disciplined call: note the thread, don't PASS on it.

**(c) WEAK** — off-domain at the subject layer; the one transferable thread is incidental dev-tooling. *(Marginally richer than Sana's orthogonal-WEAK — Sana had no agent surface at all — but still WEAK.)*

### (d) Corpus connectivity — **WEAK**

More threads than Sana's near-zero, but every one is product-domain or incidental:

- **MCP-native** — the *product* hosts/calls MCP tools (voice agents → MCP). A product-host flavor of Pattern #18's MCP sub-mechanism; tangential, voice-domain.
- **agentskills.io SKILL.md format used internally** — the 2 skills are SKILL.md-format, so dograh is a *format-adopter* — but for **internal dev tooling**, not as a published product/library. It therefore does **NOT** join the Pattern #57 57k product-implementer chain (honest non-claim).
- **`CLAUDE.md` + hierarchical `AGENTS.md`** — Library-vocab #12 LLM-routing-artifacts, a real N+1 (incidental).
- **`review-agents-md` drift-guard** — Pattern #81 Manifest-Drift **PROPER pole** (anti-drift; anchored v64 claude-seo), a real N+1 — and a nice contrast to the v66/v113 "names-the-drift-and-drifts-anyway" *inverse* pole (incidental).
- **BYOK across LLM/STT/TTS + Pipecat-based + pipecat/vllm/langfuse forks** — Pattern #84 cross-vendor-tolerance + #45 license — voice-domain flavor.

Component-/exhaust-level coincidences, not corpus connectivity in the sense the criterion means.

**(d) WEAK.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer / (a)-7 | **FAIL** |
| (b) goal-relevance / vault-utility | **FAIL** |
| (c) instructive | **WEAK** (off-domain subject; incidental agent-tooling thread) |
| (d) corpus connectivity | **WEAK** (incidental / product-domain only) |

**STRICT = 0 clear PASS → SKIP.** Honest placement on the override scale: **less out-of-scope than v116 Sana** (which had no agent surface at all) but **more out-of-scope than v84 image-blaster** (itself a Claude-Code agent-skill bundle). dograh is a non-agent-coding *product* whose only corpus-relevant surface is the Claude Code tooling its own team uses to build it.

**Operator decision (2026-05-30): OVERRIDE → INCLUDE.** Recorded honestly as the **3rd operator-elected Phase 0.9 OVERRIDE** in corpus history (v84 → v116 → v122). Per the Operator-Elected Override policy (routine v2.3 §5–§7), Option **B2 streak-with-override-asterisk**:

- Streak notation **"47+2\*" → "47+3\*"** (47 PASS + 3 overrides).
- The **post-v116 clean-PASS run (v117/v118/v119/v121 = 4)** is **BROKEN** — v122 is itself an override; post-override clean-PASS counter resets to **0**.
- **⚠️ Override-frequency check — 2-in-20 TRIPS (FIRST firing in corpus history):** v116 and v122 are both within the last 20 wiki-ships (v116→v122 = 6 ships: v116/v117/v118/v119/v121/v122; v120 was audit-only). Per §7 this **mandates** a Phase 0.9 STRICT systematic-miss-pattern review at the next audit. The **3-in-30** trigger does **NOT** fire (v84 is ~38 ships back; only 2 overrides in the last 30).

**Mandated next-audit task (§7):** examine the 3 override cases — v84 image-blaster (creative-tech skill) / v116 Sana (vision research model) / v122 dograh (voice platform) — for a common cause. **Working hypothesis:** all three are *notable repos the operator wanted captured that FAIL (a) cultural-peer + (b) goal-relevance* — i.e. the override valve is functioning as a "capture interesting off-scope subjects" channel, not as a rescue for STRICT misses. That is an *intake-channel* question, not a *criteria* defect, so the likely correct outcome is NOT a Phase 0.9 criteria redesign but a decision to either (i) formalize a lightweight **corpus-knowledge-outlier** track distinct from INCLUDE (no streak/override accounting), (ii) tighten OVERRIDE documentation discipline, or (iii) accept the 2-in-20 frequency as the cost of a deliberate escape valve.

**Honest framing carried to every artifact:** dograh is corpus-knowledge-of-an-outlier. It is NOT a pilot candidate, NOT goal-aligned, and contributes NO change to Pattern Library state. All derived observations carry the **OVERRIDE-INCLUDE-EVIDENCE-QUALITY-CAVEAT** (§18).
