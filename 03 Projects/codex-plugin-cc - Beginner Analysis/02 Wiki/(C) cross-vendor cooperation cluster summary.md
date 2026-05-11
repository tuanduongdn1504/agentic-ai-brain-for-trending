# Cluster 3 — Cross-vendor cooperation + corporate publication context

> **Sources:** OpenAI corporate context + Apache-2.0 license + cross-vendor strategic positioning observations.
> **Wiki:** codex-plugin-cc v62.

---

## 1. The cross-vendor cooperation observation (CORPUS-FIRST)

**OpenAI publishes Apache-2.0 plugin FOR Anthropic Claude Code rival platform.**

This is unprecedented in Storm Bear corpus across 61 prior wikis:
- No prior corpus subject had a major AI provider publishing plugin for rival's IDE
- Microsoft (spec-kit v17 + markitdown v28) publishes for own ecosystem (GitHub / Microsoft tools)
- spec-kit's 80+ marketplace = own marketplace, not rival's
- Cursor / Windsurf / Codex CLI = competing IDEs without cross-publishing observed

**Strategic interpretation candidates:**
1. **Marketshare protection** — developers using Claude Code retain access to OpenAI tooling
2. **Developer UX optimization** — meet developers where they work (Claude Code's UX advantage acknowledged)
3. **Distribution acquisition** — gain footprint in Claude Code marketplace audience
4. **Symmetric-cooperation expectation** — invitation for Anthropic to publish Claude tools for Codex CLI
5. **Codex commodification** — position Codex as backend service callable from any host (not platform-locked)

## 2. Apache-2.0 license observation

OpenAI ships Apache-2.0 (not MIT, not BSD, not proprietary).

**Apache-2.0 distinguishing features vs MIT:**
- Explicit patent grant (covers contributor patents)
- Notice file required (`NOTICE` shipped — corpus-observable)
- Slightly more bureaucratic but commercial-friendly

**License-axis observation:** Apache-2.0 increasingly common at corporate-org corpus level:
- spec-kit v17 (Microsoft) — Apache-2.0
- magika v44 (Google Research) — Apache-2.0
- codex-plugin-cc v62 (OpenAI) — Apache-2.0

3-corporate-org corpus pattern: **Apache-2.0 as corporate-AI-tool default license.** vs MIT-default for solo / community / startup tier.

## 3. Pattern #19 corporate-strategic archetype refresh

Pre-v62 Pattern #19 corporate-strategic observations:
- spec-kit v17 (Microsoft GitHub)
- markitdown v28 (Microsoft Microsoft)
- = 2 products, 1 organizational archetype (Microsoft)

Post-v62:
- + codex-plugin-cc v62 (OpenAI)
- = 3 products, **2 distinct corporate orgs** (Microsoft 2-product + OpenAI 1-product)

**Pattern #19 corporate-org-archetype now has corpus-first-cross-org evidence at N=2 distinct orgs.** Promotion-eligibility check: structural-N=2 across distinct orgs.

## 4. Corporate publication strategy observations

| Aspect | Microsoft pattern (v17/v28) | OpenAI pattern (v62) |
|---|---|---|
| **Target ecosystem** | Own (GitHub / Microsoft tools) | **Rival (Anthropic Claude Code)** |
| **Distribution** | Own ecosystem channels + Apache-2.0 OSS | Rival ecosystem (Claude Code marketplace) + Apache-2.0 OSS |
| **Authentication model** | Within own platform | **Cross-vendor (separate auth required)** |
| **Strategic motive** | Ecosystem dominance via tooling | **Marketshare retention via cross-publication** |

## 5. Pattern #76 narrative shift

Pattern #76 was registered N=1 stale-flagged at v63 EARLY mini-audit (2026-05-07) based on cc-sdd v61 evidence (separate `kiro-review` subagent + auto-debug + completion gate).

codex-plugin-cc v62 ships `/codex:adversarial-review` 1 wiki later. Initial impression: 2nd N evidence. Closer reading reveals:
- cc-sdd: separate-role architectural primitive (3 distinct subagents in adversarial pipeline)
- codex-plugin-cc: prompt-framing variant within same review function (1 review-skill, 2 prompt-templates)

**Mechanism distinction is fundamental:** architectural-role-separation requires runtime architecture changes; prompt-framing requires only prompt-template additions. Same outcome category (adversarial-review behavior) via different implementation strata.

**Counter-evidence-driven refinement** narrows Pattern #76 to "adversarial-review-via-architectural-role-separation specifically." NEW sister candidate (or sub-variant) for "adversarial-review-via-prompt-framing variant" stale-flagged at codex-plugin-cc v62 N=1.

## 6. Pattern #57 Recursive Corpus Reference check

codex-plugin-cc README/docs explicit cross-corpus citations:
- Claude Code (host): IMPLICIT via plugin marketplace install commands; no textual citation as "tool"
- anthropics/skills protocol: IMPLICIT via plugin schema compatibility
- Codex CLI: own product, not cross-corpus

**Verdict:** Pattern #57 implicit-citation-via-host-platform observation. Distinct from explicit textual citations (e.g., 57c forward-citation). codex-plugin-cc is N=1 implicit-host-platform citation observation; does NOT extend 57a/b/c family without explicit textual reference.

## 7. Background-task surface as new primitive

`/codex:rescue --background` + `/codex:status` + `/codex:result` + `/codex:cancel` = 4-command background-task lifecycle.

Prior corpus subjects with long-running task primitives:
- cc-sdd v61 `/kiro-impl` autonomous mode (implicit; no surfaced status command)
- BMAD v11 persona-flow (implicit)
- aidevops v47 multi-step DevOps work (implicit)

**codex-plugin-cc is corpus-first explicit-4-command-background-job-lifecycle surface.** Distinct from polling-API patterns (e.g., webhook callbacks); explicit user-invokable primitives at slash-command granularity.

**NEW Pattern candidate?** Background-Task-Lifecycle-Primitive-Set. N=1 stale-flagged at codex-plugin-cc v62. 2nd corpus subject with explicit 4-command lifecycle would un-stale-flag.

## 8. Storm Bear pilot relevance discussion

If cc-sdd pilot (currently #1) measures "adversarial-review catch-rate" via cc-sdd's separate-role architecture, pilot-rank insertion question for codex-plugin-cc:

**codex-plugin-cc as pilot:**
- Pros: Apache-2.0 + corporate-trust + ChatGPT subscription Storm Bear has + adversarial-review prompt variant comparison vs cc-sdd architecture
- Cons: ChatGPT subscription cost + cross-vendor auth overhead + single-platform Claude-Code-only (no broader leverage)

**Recommendation:** codex-plugin-cc pilot best as **comparison-pilot** to cc-sdd (run both adversarial-reviews on same code → measure detection-quality, ergonomics, cost differences). NOT standalone pilot priority.

Suggested pilot-ranking insertion: **#1.5** (post-cc-sdd, parallel comparison opportunity).

## 9. Operator-deployment imbalance reduction note

Storm Bear vault has noted "7 ranked pilots accumulated / 0 deployed." codex-plugin-cc adds another pilot to ranked list (#1.5 if comparison-with-cc-sdd, or #4 if standalone). 

Without pilot deployment, accumulation:effective-pilot ratio worsens. v62 wiki adds 1 more potential pilot to backlog without deploying any. Goal #2 ("Tôi muốn build software with these tools") only resolved via actual pilot deployment.

## 10. Cross-wiki standards check

- ❌ OpenClaw runtime: NOT mentioned
- ❌ Hermes runtime: NOT mentioned
- ❌ MCP: NOT integrated
- ❌ AGENTS.md: NOT shipped
- ✅ anthropics/skills protocol: IMPLICIT via plugin schema (not textually cited)
- ✅ Claude Code plugin marketplace: USED (corporate-scale Pattern #59 evidence)

## 11. Pattern advancement check post-v62

- **Pattern #76 counter-evidence-driven refinement** — NARROW to architectural-role-separation specifically; NEW sister candidate prompt-framing-variant
- **Pattern #19 corporate-strategic archetype N=2 cross-org structural** — Microsoft + OpenAI distinct orgs; promotion-eligibility check
- **NEW Pattern #77 candidate: Cross-Vendor Cooperative Plugin Publication** — N=1 stale-flagged (corpus-first; OpenAI for Claude Code)
- **NEW Pattern candidate: Background-Task-Lifecycle-Primitive-Set** — N=1 stale-flagged (4-command rescue/status/result/cancel surface)
- **Pattern #18 Layer 2 cross-vendor-bridge-as-plugin sub-archetype** — N=1 stale-flagged (3rd Layer 2 sub-archetype)
- **Pattern #59 corporate-scale strengthening** — N=3 plugin marketplace observations (OMC v27 + claude-hud v35 + codex-plugin-cc v62); corporate-scale sub-variant N=1
- **Pattern #57 implicit-host-platform citation observation** — N=1 (does NOT extend 57a/b/c explicit-textual family)
