# OPEN-QUESTIONS — MiroFish - Beginner Analysis (v49)

Questions deferred for future deep-dive wikis OR future Pattern Library audits OR operator decisions.

---

## Source-code deep-dives deferred (GREEN-tier compression decision)

1. **ReportAgent toolset enumeration** — `services/report_agent.py` (99 KB; largest file in repo) cited but not extracted. What's the full toolset structure? Reflection-loop interaction patterns? Tool-call orchestration semantics?
2. **Zep tools enumeration** — `services/zep_tools.py` (66 KB) cited but not extracted. What's the full Zep wrapper API surface?
3. **OASIS profile generator schema** — `services/oasis_profile_generator.py` (50 KB). What persona attributes are generated? How does it map README "personalities, memory, behavioral logic" claim to concrete data structure?
4. **Simulation config generator schema** — `services/simulation_config_generator.py` (40 KB). How does the system auto-parse prediction requirements into OASIS-runnable configs?
5. **IPC protocol** — between Flask main + simulation subprocess. `services/simulation_ipc.py` (12 KB). What's the message format? Async / streaming / batch?
6. **"Thousands of agents" claim** — README marketing claim; actual per-simulation-round agent count not verified. Need runtime probe: instrument `simulation_runner.py` and verify with default config.

These are **not blocking** for v49 wiki. Open for future deep-dive wikis if Pattern Library observations call for it.

---

## Pattern Library candidates flagged for monitoring

1. **CAMEL-AI / OASIS lineage as Pattern #19 archetype-2 sub-classification (research-org-cluster vs individual-cluster)**
   - N=1 at v49; N=1 stale-risk-flagged
   - Re-evaluate at v54 (5-wiki window)
   - If 2nd corpus wiki cites CAMEL-AI/OASIS or similar research-org-cluster lineage, formalize 2a (individual) / 2b (research-org-cluster)

2. **Pattern #44 sub-variant 44e candidate: academic-individual-with-commercial-incubation**
   - N=1 at v49 (BaiFu + BUPT + Shanda)
   - Stale-risk-flagged
   - Re-evaluate at v54 (5-wiki window)
   - If 2nd similar-shape wiki appears, formalize 44e

3. **Pattern #31 pre-monetization sub-variant**
   - 10th data point at v49 with explicit pre-monetization positioning (no Pro tier; capital-backed; recruiting-pipeline as funnel)
   - Recommend formal sub-variant at next mini-audit
   - Possibly N=2+ already observable in prior corpus (re-scan needed)

4. **Pattern #50 recruiting-as-funnel-terminus**
   - N=1 at v49
   - Recommend formal-statement extension at next mini-audit (sub-axis: paid-tier / cloud-managed / sponsorship / **recruiting-pipeline NEW**)

5. **Pattern #29 AGPL-3.0-at-project-scope-at-T5 sub-variant**
   - N=3 default-criterion at T5 (Skyvern v24 + shannon v45 + MiroFish v49)
   - Recommend formal sub-variant at next mini-audit

6. **CN-author cross-tier presence** — 4-wiki cluster (TrendRadar v19 T4 + DeepTutor v38 T5 + dive-into-llms v39 T3 + MiroFish v49 T5)
   - NOT registered as Pattern #73-style regional meta-pattern (consolidation-forward)
   - Different from Korean / VN / Pakistani sub-variants confirmed in #73
   - Documented observation; flag if pattern emerges with more depth

---

## Storm Bear vault decisions

1. **License decision for vault publishing** — vault is currently private/limited-share. If/when published:
   - MIT / Apache-2.0 (maximum adoption)?
   - AGPL-3.0 (force-disclosure for SaaS forks)?
   - CC-BY for content + Apache-2.0 for skills (dual-licensing à la Unsloth)?
   - MiroFish v49 + Skyvern v24 + shannon v45 are AGPL-3.0 examples in corpus; provides reference if AGPL chosen
   - **DEFERRED — not blocking**; addressed in v27 diagnostic HIGH item #2 (publishing strategy formalization)

2. **i18n strategy for vault publishing** — vault is currently EN+VN bilingual for beginner guides, EN-primary for entity pages
   - MiroFish v49 demonstrates 3-tier i18n decomposition (LLM-instruction / UI-strings / documentation)
   - Vault should explicitly decompose: which tiers, which languages, what completeness target?
   - **DEFERRED**; not blocking; informs publishing-strategy decisions when v27 HIGH bundle executes

3. **Vault governance philosophy** — Pattern #12 v42 refined formulation reinforced by 6 counter-evidence wikis (claude-hud v35 + pi-mono v36 + ruflo v42 + aidevops v47 + gh-aw v48 + MiroFish v49)
   - Vault governance philosophy alignment: solo + pre-monetization + small-scale → light-governance is appropriate
   - When publishing scope ambition increases, governance depth should increase
   - **DEFERRED**; informs CLAUDE.md refactor

---

## Operator-facing backlog

**v27 diagnostic HIGH bundle: 29 SESSIONS DEFERRED** (5.8× threshold per routine v2.1 operator-facing-backlog discipline).

**STRONGLY recommended action**: execute v27 HIGH bundle before v50.

5 items in v27 bundle (per CLAUDE.md state block):
1. Vault CLAUDE.md refactor (templates available: spec-kit v17 + aidevops v47 + gh-aw v48 — 3-template-ensemble)
2. Storm Bear publishing strategy formalization
3. Vault skill-lock (skills-lock.json equivalent)
4. (other items per existing backlog)
5. Public-release decision

MiroFish v49 does NOT add new templates for vault refactor; AGENTS.md absent. Existing 3-template-ensemble is sufficient.

**Hybrid alternative**: 30-60 min mini-audit (combine carry-forward audit candidates: AGPL-3.0 sub-variant + recruiting-funnel-terminus extension + Pattern #66 OT sub-categorization + Pattern #18 4-layer + Pattern #22 22c scope-narrowing + Pattern #47 retirement) → v27 HIGH bundle (~7-9h total).

---

## Ethical / use-case observations

1. **Public opinion prediction is sensitive** — could be repurposed for influence campaigns. Beginner guide includes ethical framing.
2. **Personality + memory injection from real-world entity extraction creates digital effigies** — privacy concerns for non-public-figure data sources.
3. **Financial prediction is regulated** — beginner guide includes disclaimer: outputs are NOT investment advice.

These are **observations, not Storm Bear actions**. Vault doesn't deploy MiroFish; not Storm Bear's risk to manage.

---

## Routine v2.2 design candidates (5 items added at v49)

Cumulative ~250 routine-v2.x action items across v3-v49. v49 contributions:

1. **Domain-distance per-wiki applicability check** — formalize "domain-distant peer" framing criterion for Storm Bear meta-entity inclusion vs omission
2. **Pre-monetization commercial-product sub-variant** — Pattern #31 explicit pre-monetization sub-variant
3. **i18n decomposition discipline** — Phase 0 sub-check for 3-tier i18n surface (LLM-instruction / UI-strings / documentation)
4. **Recruiting-as-commercial-funnel-terminus** — Pattern #50 formal-statement extension
5. **AGPL-3.0-at-project-scope-at-T5 correlation hypothesis** — track for falsification

Routine v2.2 refactor is **DEFERRED**; not blocking. Routine v2.1 is structurally adequate; v2.2 is an optimization, not a fix.
