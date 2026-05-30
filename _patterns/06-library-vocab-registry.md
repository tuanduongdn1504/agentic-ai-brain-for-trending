# Library-vocab Registry (maintained master list)

**Created:** 2026-05-29 (v2.4 dedicated Library-vocab consolidation session, post-v115 audit).
**Status:** AUTHORITATIVE. This is the **single source of truth** for Library-vocab observational items. Per routine v2.4, Library-vocab items are tracked HERE and nowhere else — per-wiki narratives may *note* an observation but must *file* it into this registry (into a cluster or as a tracked standalone). No more loose "NEW candidate X" minting in wiki narratives that never gets tracked.

**Why this file exists:** through v114 the Library-vocab "PROVISIONAL" layer was reported as "~108 items." The v2.4 consolidation established that **~108 was a phantom count** — the running *sum of per-wiki "NEW candidate" mentions*, most never tracked again, many near-duplicate or one-off. There was never a maintained list. This file replaces the phantom count with a real, maintainable registry: **8 CONFIRMED + 7 themed clusters + a short live-standalone list + a retired set.**

---

## A. CONFIRMED Library-vocab items (8) — authoritative, unchanged at consolidation

| # | Item | N | Anchors | Gist |
|---|---|---|---|---|
| #12 | **LLM-routing artifacts** | N=5+ | v75→v114 | Distinct artifact-type family that routes/instructs AI agents: NOTICE.md / HARNESSES.md / AGENTS.md / CLAUDE.md / GEMINI.md / copilot-instructions.md / llms.txt / skill.json / skills-lock.json. CORPUS-RECORD single-subject density: v94 (~14 artifacts); v114 5-artifact instance (AGENTS+CLAUDE+GEMINI+copilot-instructions+llms.txt). |
| #14 | **Org-Brand / Product-Brand Split via 2-Custom-Domain** | N=3 | v82+v83+v85 | Separate org domain + product domain as a positioning move. |
| #15 | **Operator-Elected Phase-0.9 Override w/ Honest Documentation-Trail** | N=1 (ONE-TIME-EXCEPTION) | v84 | The override protocol itself (Option B2 streak notation). Frozen as a one-time-exception meta-item. |
| #16 | **Engagement-Deficit-Extreme (with active forks)** | N=4 | v67+v76+…(PROMOTED v90) | Corpus-record-low engagement signals (issues/subscribers) alongside active forks. |
| #17 | **Try-Once-and-Move-On Profile** | N=4 | v79+…(PROMOTED v90) | High fork-ratio + zero sustained-engagement = exploratory clone-and-drop. |
| #18 | **Coupled-Design Density Not Scale-Dependent** | N=4 | v79+v87+v88+v89 (PROMOTED v90) | Per-wiki pattern-coupling count is uncorrelated with subject scale; micro-scale subjects match mega-scale. |
| #19 | **Deliberately-Narrow Distribution Profile** | N=3 | v79+v80+v87 (PROMOTED v90) | Sustained scope-narrowing against the usual expansion trajectory. |
| #20 | **Token-Economy-Quantification** | N=4 | v87+v97+v98+(PROMOTED v101) | Token-impact as an explicit measurement axis (composition / runtime / data-structure / per-skill). |

*(Pattern #19 sub-mechanism "VN-Community Multi-Profile-Type" N=5 and Pattern #84 84d Hardware-Substrate-Tolerance N=4 are CONFIRMED at the **Pattern** layer, not here — see `02b-confirmed-patterns-v42-plus.md`.)*

---

## B. Tracked clusters (7) — the new PROVISIONAL structure

Each cluster is ONE tracked entry. Members are individual observations grouped by shared structural theme. A cluster promotes toward CONFIRMED only if a coherent sub-claim reaches N=3 cross-author + cross-vertical (routine §2). New per-wiki observations file into the matching cluster rather than minting standalones.

**LV-C1 — Vendor-Direct Skill-Authoring & Distribution.** Members: Product-Vendor-Official-Skills-for-Own-Product (v114, CORPUS-FIRST), Vendor-Skill-Embeds-Recommendation-Bias (v114), Multi-Registry-Distribution (v89), Canonical-Snippet-Auto-Insertion (v88), Clone-as-Sibling-Directory (v88), Zero-Dependency-Bridge-Tool (v88). *Theme:* how skills/tools are authored + pushed into agents. (a)-7-sister framing for the v114 vendor-direct item lives here. Cluster status: live, N=watch.

**LV-C2 — Cost / Capacity Economics of Free-or-Cheap Inference.** Members: Free-Tier-Stacking-as-Capacity-Aggregation (v112), Cost-Attribution-via-LiteLLM (v89), Cost-Attribution-via-External-Pricing-Service (v109), Quota-Arbitrage-Across-Vendor-Internal-Surfaces (v67), Sticky-Session-Model-Affinity (v112), **API-Relay/Middle-Layer-Reseller-Economy (v117 CodexPlusPlus; JOJO Code/AIGoCode/PackyCode sponsor a config-switcher that points a coding agent at relay endpoints — filed at v120 audit)**. *Promotable sub-claim:* **"Cost-Attribution-via-External-Service" N=2** (LiteLLM v89 + pricing-service v109) → PROMOTION-ELIGIBLE at N=3 (NOT advanced by v117 — relay-reseller-economy is a distinct sub-theme, not cost-attribution). (#13 OSS-with-hosted-Pro-SaaS-tier-on-MIT-base = RETIRED v96; historical member.)

**LV-C3 — Doc-Coherence: Anti-Drift vs Drift-Exhibited.** Members: "names-the-drift-and-drifts-anyway" inverse-pole **N=2** (v66 agentmemory + v113 ai-engineering-from-scratch; sub-observation of Pattern #81), Self-Referential-Methodology-Demonstration (v87), Marketing-Site-vs-README-Divergence (v80). *Cross-ref:* Pattern #81-proper (Manifest-Drift-as-First-Class-CI-Concern, v64 claude-seo) is the opposite pole and lives at the Pattern layer. Cluster status: live; the N=2 inverse-pole is the strongest member (N=3 watch).

**LV-C4 — Cadence / Velocity micro-signals.** Members: High-Development-Cadence-relative-to-Star-Velocity **N=2** (v89+v107), High-Release-Cadence-at-Micro-Scale (v89), Release-Cadence-Discipline (v88). *Cross-ref:* Pattern #52 (velocity sub-classes) + #16/#17 (CONFIRMED) cover the headline engagement/velocity vocabulary; this cluster holds the residual cadence one-offs. Status: live, N=watch.

**LV-C5 — Design-Skill Composition Vocabulary.** Members: Compositional-Mix-&-Match (v87), Universal-Modifier-Composable (v87), Multi-Attribute-Style-Schema (v87), Visual-Directions-Taxonomy **N=2** (v81+v83), CO-EXISTENT-framing-axes **N=2** (v82+v83). *Theme:* design-skill-local composition vocabulary. Largely vertical-bound (design-skill cluster); unlikely to cross-promote. Status: live but vertical-capped.

**LV-C6 — Session / Prompt-Persistence & Autonomy.** Members: Tri-Layer-Prompt-Persistence (v88), Local-Conversation-Plus-Bridge-Summaries (v88), Auto-Execution-Mode-Prerequisite (v88), Autonomy-vs-Session-Handoff-Continuum (v79). *Theme:* teleport/harness-local session+autonomy vocabulary. Status: live, N=watch.

**LV-C7 — Packaging / Runtime-Substrate one-offs.** Members: Single-Tool-No-Fallback-Packaging (v79), Rust-for-Observability-Perf (v89), Bun-primary (v84, OVERRIDE-caveat), **Tauri-Desktop Management-GUI for a Coding Agent N=2 (v73 cc-switch + v117 CodexPlusPlus — both Tauri-2 desktop control-planes that manage *another* coding agent's config/providers; filed at v120 audit)**. *v120 audit note (honest downgrade):* the ship-time "LV-C7 Tauri-desktop-harness → N=3 (incl. v118 OpenHuman)" claim is **CORRECTED to N=2** — v118 OpenHuman is a Tauri desktop app but a **standalone agent assistant**, NOT a management-GUI-for-another-agent, so it is **adjacent, not a clean 3rd instance**; the "archetype-vs-Tauri-stack-popularity" check (flagged at v117/v118) resolves toward *don't promote* — "uses Tauri" is incidental; the tight claim is the management-GUI-for-another-agent shape (v73+v117 only). *Cross-ref:* Pattern #84 84d Hardware-Substrate-Tolerance (CONFIRMED N=4) covers the structural substrate-tolerance claim. Status: live; N=2 management-GUI sub-claim is the strongest member (N=3 watch — needs a 3rd management-GUI, not just a 3rd Tauri app).

---

## C. Live standalone candidates (not yet clustered)

| Item | N | Anchor | Status |
|---|---|---|---|
| **Brand-Named Third-Party Repo + Affiliation Disclaimer** | **N=2** | **v98 Anthropic-Cybersecurity-Skills + v119 nature-skills** | **filed v120 audit; famous brand in repo/skill names (Anthropic / Nature) + explicit "not affiliated" disclaimer; cross-brand + cross-vertical (cybersecurity / scientific-publishing) + cross-author; PROMOTION-ELIGIBLE at N=3; distinct from (a)-7 Foundational-Vendor-Direct-Source (vendor IS owner) and v114 Product-Vendor-Official-Skills-for-Own-Product (vendor ships own skills) — here the brand owner is uninvolved + explicitly disclaimed** |
| Pure-Markdown-MEGA-Viral Single-Purpose Skill | N=2 | v87 (micro) + v108 (MEGA) | watch (scale-spread but single theme) |
| voice-calibration personalization | N=1 | v108 | 5-wiki stale-watch (→ ~v113-window; re-check ~v118) |
| Integrated OSS Book + Self-Developed Companion Framework (T3 sub-archetype candidate) | N=1 | v111 | held at OC; T3 sub-typology watch (with v113) |
| From-Scratch-then-Ship Curriculum w/ agentskills.io Artifact Emission (T3 sub-archetype candidate) | N=1 | v113 | held at OC; T3 sub-typology watch (with v111) |

*(The two T3 sub-archetype candidates are tracked here for visibility but live structurally at the tier-sub-archetype layer; if a 3rd T3 education sub-archetype appears, formalize a T3 sub-typology — see v115 audit §F.)*

---

## D. RETIRED at v2.4 consolidation (forced-retire by routine §2 rule)

**Rule applied:** any N=1 standalone Library-vocab candidate first-registered at or before **v99** (15 wikis before v114) and never strengthened to N=2 is FORCED-RETIRED (routine §2 "15-wiki forced retire if still N=1-only"). Retired items are **re-registerable** if a genuine 2nd instance later appears.

Forced-retired (the v79–v89 N=1 long-tail, non-exhaustive — these were never maintained as discrete entries, which is the finding):
- v79 batch: Method-Preserved-Despite-Throughput-Collapse · Human-Asleep-as-Design-Target · Size-Independent-Quality-Metric · VN-Diaspora-vs-VN-Located (absorbed by Pattern #19 N=5 CONFIRMED).
- v80 batch: LLM-Inversion-Architecture · Cultural-Distribution-Channel-Diversity · Hybrid-Donation-Channel-Localization · LLM-Integration-at-Any-Layer-As-Inclusion-Criterion.
- v88/v89 misc N=1: 3-Locale-Chinese-Variant (absorbed by Pattern #19) · Multi-Language-Natural-Language-Trigger.
- #13 OSS-with-hosted-Pro-SaaS-tier-on-MIT-base — RETIRED at v96 (recorded; historical member of LV-C2).
- The unnamed/loose long-tail counted toward "~108": treated as retired-by-rule (never discrete entries).

---

## E. Standing anti-re-accumulation rules (routine v2.4)

1. **Single registry.** This file is the only tracked location. Wiki narratives may NOTE an observation but must FILE it here (cluster or standalone) or omit it.
2. **Registration cap.** A wiki may register at most **2 genuinely-NEW standalone** Library-vocab candidates; further observations must join an existing cluster or be omitted. (Formalizes the v115 freeze.)
3. **Auto-retire.** Any standalone N=1 not strengthened within 15 wikis is auto-retired at the next audit (mechanically checked against this file).
4. **Count discipline.** Report the **tracked-registry count** (8 CONFIRMED + 7 clusters + N live standalones), NOT the cumulative-mention sum. The "~108" figure is officially deprecated as a non-maintenance artifact.
5. **Filing is an ACT, not a claim (NEW, v120 audit).** "File it into the registry" means **edit this file in the same session as the wiki ship** — not write "filed into LV-Cx" in the wiki narrative and move on. **v120 audit FINDING:** v116–v119 narratives *claimed* to file observations (LV-C2 relay-economy, LV-C7 Tauri-desktop) but the registry was **never actually edited** — the exact "note that never gets tracked" failure mode §28 exists to prevent, reproduced one level up. The cap (rule 2) and count-discipline (rule 4) held; the filing step did not. Remediated at the v120 audit (the v116–v119 observations are now actually filed above). Going forward: no wiki ship is "done" until its registry observations are written into this file.

---

## F. Consolidated count (post-v2.4)

- **8 CONFIRMED** (unchanged).
- **7 tracked clusters** (LV-C1…LV-C7) absorbing ~25 named live observations; **+ v120-audit filings**: LV-C2 API-Relay-Reseller-Economy (v117), LV-C7 Tauri-Desktop-Management-GUI-for-a-Coding-Agent N=2 (v73+v117).
- **~5 live standalones** (section C) — **+ Brand-Named Third-Party Repo + Affiliation Disclaimer N=2 (v98+v119), filed v120**.
- **Forced-retired long-tail** (section D) — collapses the phantom "~108."
- **Tracked PROVISIONAL surface ≈ 12 entries** (7 clusters + 5 standalones), up from ~11 (the v120 Brand-Named+Disclaimer standalone). This is the maintainable layer going forward.

**PROMOTION-ELIGIBLE sub-claims (N=2 → N=3 watch):** LV-C2 "Cost-Attribution-via-External-Service" (v89+v109); LV-C7 "Tauri-Desktop-Management-GUI-for-a-Coding-Agent" (v73+v117); section-C "Brand-Named Third-Party Repo + Affiliation Disclaimer" (v98+v119). **No new CONFIRMED Library-vocab promotions at v120** (the Pattern-layer promotion this audit = Pattern #18 sub-archetype #8 → CONFIRMED N=3, recorded in `02b-confirmed-patterns-v42-plus.md`). Library-vocab CONFIRMED count unchanged at 8.
