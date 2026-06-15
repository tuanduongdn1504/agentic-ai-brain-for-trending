# (C) ai-maestro — Phase 4b Pattern Library analysis (v163)

**Verdict context:** GOAL-ALIGNED INCLUDE 3/4. **§28 cap used at 0 new §C standalones. NO confirmed-count change: 46 patterns / 10 Library-vocab CONFIRMED.** Ships into the v158-audit-CONFIRMED Pattern Library.

---

## PRIMARY (tier layer, `02b` / registry `06` §F): the v150 Paseo orchestration-PLATFORM standalone → **N=2**

**Library-vocab §C "Multi-Vendor Coding-Agent Orchestration Platform" (minted at v150 Paseo as "Cross-Device Multi-Vendor Coding-Agent Orchestration Platform (agent-of-agents via a skill suite)") → N=1 → N=2.** ai-maestro is the genuine 2nd instance: a self-hosted platform that **orchestrates heterogeneous vendor coding agents as units** (Claude Code/Codex/Aider/Cursor/OpenClaw/Hermes/Droid), from one control plane, drivable across multiple locations. **PROMOTION-ELIGIBLE at N=3.**

### This completes the SECOND bucket of the v162 orchestration-theme decomposition
The v162 AoE ship decomposed the long-held "AI-agent orchestration theme = HETEROGENEOUS → HELD" finding (v151/v158) into three buckets. v163 ai-maestro lands cleanly in the **platform** bucket and brings it to N=2:

| Bucket | Members | N | Status |
|---|---|---|---|
| **Session-hosting multiplexer (human-driven)** | v99 cmux + v162 AoE | **N=2** | PROMOTION-ELIGIBLE (registered v162, rename DEFERRED) |
| **Multi-vendor orchestration PLATFORM** | v150 Paseo + **v163 ai-maestro** | **N=2** | PROMOTION-ELIGIBLE (this ship; confirm/rename DEFERRED) |
| Agent-team-architecture generator | v131 harness | N=1 | adjacent |

Both N=2 buckets are now PROMOTION-ELIGIBLE and both DEFERRED to the overdue audit — which **strengthens the case for actually running it.**

### The disciplined call (the v158/v162 "don't generalize-to-fit" rule)
Paseo's standalone name carries the parenthetical "**(agent-of-agents via a skill suite)**" — that is *Paseo's specific mechanism* (`/paseo-*` skills make one agent orchestrate others). ai-maestro orchestrates via a **dashboard + AMP agent-to-agent messaging + a peer mesh**, NOT a skill suite. So:
- **Read narrowly** (must have an agent-of-agents skill suite) → ai-maestro is a distinct sub-flavor.
- **Read broadly** (multi-vendor orchestration platform) → ai-maestro is a clean 2nd instance.

This is *exactly* the v162-AoE / v158-CodexBar situation. The disciplined move: **register the broad "Multi-Vendor Coding-Agent Orchestration Platform" class at N=2** with two recorded sub-flavors, and **DEFER to the audit** whether to (a) CONFIRM the broad class (dropping the "via a skill suite" parenthetical from the Paseo name — a RENAME), or (b) keep two distinct sub-flavors. **Do NOT pre-decide; do NOT generalize the definition just to fit the 2nd instance.** Sub-flavors recorded:
- **(a) agent-of-agents-via-skill-suite** — v150 Paseo (`/paseo-handoff` / `/paseo-loop` / `/paseo-advisor` / `/paseo-committee`; human orchestrates via a skill that drives other agents; cross-DEVICE: phone/desktop/web/CLI client surfaces).
- **(b) agent-to-agent-messaging-mesh** — v163 ai-maestro (AMP agent-to-agent peer messaging + persistent memory + code-graph baked in; multi-MACHINE peer mesh, no central server; dashboard + gateways).

---

## SECONDARY — observations (NOT minted)

- **AMP (Agent Messaging Protocol) — agent-TO-agent peer messaging.** The product's raison d'être (the README origin: "I became the human mailman between them"). Distinct from the corpus's existing **T4c Operator-Notification-Bridge** (operator-notification, v88 teleport) — AMP is *agent-to-agent*, email-like, cryptographically signed, cross-machine. A genuinely distinctive mechanism + a **candidate future §C standalone** ("agent-to-agent peer messaging for AI coding agents") and the defining sub-flavor distinguishing ai-maestro from Paseo. **NOT minted** (one subject, a sub-feature of the platform; the v162-ACP discipline — don't mint a standalone for one feature of one subject). Promotion path: a 2nd subject with first-class agent-to-agent messaging.
- **Home-grown 3-protocol suite AMP / AID / AAP** (messaging / identity / actions). Like v162's ACP, these are protocols made architecturally first-class — but **home-grown, not consumed standards**, and at 1 subject. If a 2nd subject adopts the AMP/AID/AAP suite, the home for it is a **Pattern #18 sub-mechanism-B protocol-variant candidate** (the MCP=B1 / CDP=B2 / ACP=B3-candidate precedent), NOT a §C standalone. Observation.
- **Corpus-recursive capability absorption (a nice convergence, observation only).** ai-maestro bakes in (i) **persistent memory** via CozoDB — echoes **v66 agentmemory** (Pattern #85 agent-memory-system) + v132 supermemory; and (ii) a **code graph** via ts-morph + delta indexing — echoes **v70 codegraph**. The orchestration platform is becoming the *integration point* for capabilities the corpus previously catalogued as standalone subjects. **NOT minted and NOT double-counted** — these are components, not the product; counting them as v66/v70 instances would inflate. Recorded as a corpus-recursive observation worth the audit noting (platforms-absorb-prior-standalones may itself be a forming meta-observation).
- **T4c Operator-Notification-Bridge via Messaging Platform → N+1** — Slack / Discord / Email / WhatsApp gateways + AMP cross-machine push (v88 teleport). Observation.
- **Pattern #84 84c cross-tool → N+1** — 7+ named agents (Claude Code / Codex / Aider / Cursor / OpenClaw / Hermes / Droid), agent-agnostic by design ("we don't lock you in").
- **Pattern #57 agentskills.io-adjacent** — ships a **Claude Code plugin (5 skills + 32 CLI scripts)** + a Plugin Builder repo (`23blocks-OS/ai-maestro-plugins`). PRODUCT surface (not internal dev-exhaust — the v122 distinction inverted: Claude integration *is* part of the product). Modest; **NOT** a `npx skills add` 57k implementer claim (an installed plugin).
- **Pattern #66 supply-chain** — `curl -fsSL … | sh` install + cryptographic message/identity signatures + a content-security gateway screening 34 prompt-injection patterns. A *security-forward* posture for the niche (most subjects are curl|bash-and-trust); the injection-screening is a pilot-relevant plus, the curl|bash + self-hosted-mesh + gateway breadth is the pilot-fence.
- **Multi-machine peer mesh** (no central server, machines auto-discover, "every machine is equal") — distinctive infrastructure that distinguishes ai-maestro's sub-flavor from Paseo's cross-device-client model. Observation.
- **LolaBot framework** (`23blocks-OS/lolabot`, an open-source "batteries-included Chief of Staff" agent template) + Canvas skill — bundled ecosystem; a **cited-to-subject-elevation watch** (a separate repo by the same org, like the v135 open-slide / v91 precedent).
- **Pattern #45** — MIT.

## NOT
- **NOT #18 #8** (orchestrates/messages **agents**, doesn't aggregate LLM **providers**).
- **NOT the v158 observability sub-archetype** (orchestrates / messages / runs; dashboard status is a sub-feature, not the product).
- **NOT LV-C7 #22** (Next.js *web* orchestration platform, not a Tauri desktop provider/account-config management-GUI).
- **NOT the cmux/AoE session-multiplexer species** (platform, not a human-driven session host — agent-to-agent messaging + memory + mesh are the difference).
- **NOT a #52 claim** (no reliable creation date; NOT API-verified §37.4).

## §28 bookkeeping
- New §C standalones this ship: **0** (Paseo platform standalone → N=2 = strengthening; registry `06` §F running-log + §C row updated N=1→N=2, rule-5: filing is an act).
- Confirmed-count: **UNCHANGED — 46 patterns / 10 Library-vocab CONFIRMED.** Tracked PROVISIONAL surface UNCHANGED (the platform standalone was already a tracked PROVISIONAL at N=1).
- Audit now owes (carried + new): **TWO** N=2 orchestration buckets to confirm/rename (session-multiplexer cmux+AoE; platform Paseo+ai-maestro) + the AMP agent-to-agent-messaging sub-flavor/standalone decision + ACP/AMP-AID-AAP as Pattern #18 sub-mechanism-B protocol-variant candidates + the standing LV-C7 / observability calls + the platforms-absorb-prior-standalones meta-observation.
