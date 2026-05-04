# (C) Pattern 47 + 48 Resolution + Browser T5 N=2 + Skyvern structural pair

> **Type:** Entity — pattern resolution + structural pair analysis
> **Parent:** [[(C) index]]
> **Sources:** v24 Skyvern registration of #47 + #48, v29 crawl4ai refinement, v41 browser-use source verification (DomService 1,081 LOC + agent.use_vision default / CLOUD.md stealth language / README FAQ CAPTCHA), T5 corpus inventory v9-v41
> **Status:** ✅ Phase 3 entity page — PRIMARY PATTERN RESOLUTION DOCUMENT

---

## 1. Summary

v41 browser-use resolves **two candidates registered at Skyvern v24 + refined at crawl4ai v29**:

- **Pattern #47 Vision-Based Browser Automation** → **REFINED via counter-evidence** (3-point architectural spectrum; browser-use hybrid is distinct from vision-primary Skyvern). **Pattern #47 stays candidate at N=1** (Skyvern is the only structurally-criterial vision-primary observation). Hybrid DOM+vision documented as scope-narrowing counter-evidence, NOT as promotion-supporting data point.
- **Pattern #48 Proprietary Anti-Bot Commercial Moat** → **PROMOTE TO CONFIRMED at N=2 structurally-unambiguous** (Skyvern + browser-use both gate anti-bot/CAPTCHA/stealth/proxies behind commercial Cloud tier).

Additionally: **browser T5 sub-tier N=2** with structurally-orthogonal archetypes (Skyvern commercial-entity AGPL vs browser-use commercial-startup MIT). T5 extends to **N=7 with 7 distinct archetypes at 100% diversity-per-wiki preserved**.

## 2. Pattern #47 resolution — REFINED via counter-evidence

### v24 registration (Skyvern N=1)

Original formulation: *"Vision + LLM replaces DOM/XPath for browser automation; screenshots + LLM reasoning decide actions instead of brittle CSS selectors"*

### v29 refinement (crawl4ai counter-evidence)

crawl4ai is DOM-based web scraping with post-hoc LLM analysis. This demonstrated Pattern #47 was over-broad: not all vision-absent-or-reduced browser automation adopts vision-primary approach. Pattern #47 narrowed to: *"vision-based as architectural alternative to DOM — vision-PRIMARY specifically"*

### v41 verification of browser-use

Source-level evidence:
- `browser_use/dom/service.py` = 45.1KB, 1,081 LOC (major DOM subsystem)
- `browser_use/dom/views.py` = 32.2KB (Pydantic models for DOM tree)
- `browser_use/dom/serializer/` = SerializedDOMState + ClickableElementDetector + DOMTreeSerializer
- `browser_use/dom/enhanced_snapshot.py` = 7.2KB (AX-tree + computed-styles integration)
- Default: `use_vision: bool | Literal['auto'] = True` — vision ON but screenshot-tool excluded when `use_vision != 'auto'`
- `highlight_elements=True` Browser param — DOM elements annotated in screenshots (DOM drives visual markup, not vice-versa)

**Conclusion: browser-use is HYBRID** — DOM-tree + AX-tree indexing is primary signal; vision is augmentation layer. Agent assigns numeric indices to clickable elements (`browser-use click 5`), which is DOM-based referencing.

### 3-point architectural spectrum

| Approach | Primary decision signal | Secondary signal | Corpus data points |
|----------|------------------------|------------------|--------------------|
| **Vision-PRIMARY** (DOM-free-by-design) | Screenshot + LLM coordinate-reasoning | LLM retry logic | Skyvern v24 (N=1) |
| **Hybrid DOM+vision** | DOM tree + AX-tree + element indices | Screenshot augmentation (opt-out toggle) | **browser-use v41 (N=1 NEW)** |
| **DOM-only (no LLM-in-loop)** | Deterministic CSS/XPath selectors | Post-hoc LLM on extracted content | crawl4ai v29 (N=1) |

### Pattern #47 status post-v41

**Decision: Pattern #47 stays CANDIDATE at N=1 (Skyvern).** Rationale:
- Pattern #47's narrowed scope ("vision-PRIMARY specifically") is **still Skyvern-unique** at v41
- browser-use is **counter-evidence** that narrows scope further (#47 ≠ "non-DOM-only browser automation in general"; #47 ≠ hybrid), not confirming evidence
- Promoting #47 with browser-use as 2nd data point would dilute structural meaning — these are architecturally distinct

**Consolidation-forward discipline:** Do NOT register "Pattern Hybrid DOM+Vision" as new candidate at N=1. Document hybrid as:
1. Observational-counter-evidence narrowing Pattern #47 scope
2. **OBSERVATION-TRACK or watch-list for future N=2** — if a future wiki observes hybrid architecture (e.g., another commercial browser-agent or an emerging corpus entrant), reconsider registration

**Stale-risk flagging:** Pattern #47 N=1 since v24 (now 17 wikis post-registration). **Exceeds +10 retirement threshold.** Recommend next mini-audit considers retirement-or-refinement for Pattern #47 given single data point + strong counter-evidence base. Pattern might better reframe as "3-point architectural-methodology-axis observation" (not singular pattern).

### Refined Pattern #47 formulation (proposal)

Two options for next mini-audit:

**Option A: Retire + replace with axis observation**
> Pattern #47 RETIRED. Replaced with **observation-track: "Browser automation architectural-methodology axis"** documenting 3-point spectrum (vision-primary / hybrid / DOM-only). Not a promotable pattern until 2+ data points at a single pole.

**Option B: Refine + stay candidate at N=1 with watch-list**
> Pattern #47 remains candidate at N=1 Skyvern vision-primary. Formulation: *"T5 browser-agent abandons DOM/XPath in favor of vision + LLM as primary decision layer."* Watch-list for N=2 at the vision-primary pole (not hybrid, not DOM-only).

**Recommended: Option B** — preserves Skyvern's unique observation; hybrid/DOM-only remain as documented counter-evidence. If 2nd vision-primary browser-agent enters corpus, #47 promotes naturally.

## 3. Pattern #48 resolution — PROMOTE TO CONFIRMED AT N=2

### v24 registration (Skyvern N=1)

Original formulation: *"Open-core with proprietary anti-bot as commercial differentiator"*

### v29 refinement (crawl4ai counter-evidence)

crawl4ai ships OSS 3-tier anti-bot + proxy escalation (visible in source). Pattern #48 narrowed to: *"proprietary-commercial-gated anti-bot specifically"* (distinguishes from OSS-available anti-bot implementations)

### v41 structural-unambiguity-at-N=2 analysis

| Dimension | Skyvern v24 | browser-use v41 | Structurally equivalent? |
|-----------|-------------|------------------|--------------------------|
| OSS license | AGPL-3.0 | MIT | Different (permissiveness); both OSS |
| OSS tier has anti-bot? | **No** | **No** | ✅ Same (absence) |
| OSS tier has CAPTCHA bypass? | **No** | **No** | ✅ Same |
| OSS tier has stealth fingerprint? | **No** | **No** | ✅ Same |
| OSS tier has residential proxies? | **No** | **No** | ✅ Same |
| Cloud tier has anti-bot? | **Yes (proprietary)** | **Yes (proprietary)** | ✅ Same |
| Cloud tier has CAPTCHA bypass? | **Yes** | **Yes** | ✅ Same |
| Cloud tier has stealth fingerprint? | **Yes** | **Yes (chromium fork)** | ✅ Same |
| Cloud tier has residential proxies? | **Yes** | **Yes (country-code routing)** | ✅ Same |
| Stated rationale? | Commercial differentiator | *"better browser fingerprinting and proxies... use Browser Use Cloud"* | ✅ Same (explicit commercial gate) |

**All 9 structural dimensions match. Criterion 2 (structural-unambiguity-at-N=2) satisfied.**

### Vendor independence verification

- **Skyvern-AI** = commercial entity, Skyvern Cloud
- **Browser-Use (Zurich/SF team)** = separate commercial entity, cloud.browser-use.com

**2 independent commercial companies, 2 structurally-identical anti-bot commercial gates. Not a copy-cat pattern (both likely arose independently from same market pressures).**

### Market-rationale hypothesis

Why is anti-bot consistently commercial-gated across T5 browser-agents?
1. **Technical maintenance cost** — anti-bot requires constant evolution vs evolving bot-detection heuristics (Cloudflare, DataDome, PerimeterX). High-ongoing-R&D.
2. **Liability asymmetry** — OSS anti-bot in library form would make maintainers responsible for enabling ToS violations; Cloud tier keeps liability with operator
3. **Natural commercial moat** — unlike feature differentiation, anti-bot is operationally-scaled (proxy pool, IP rotation, device farms)
4. **Legal gray area** — anti-bot bypass is ToS-adjacent; commercial customers accept T&Cs accepting risk transfer

### Promotion proposal for next mini-audit

**Pattern #48 Proprietary Anti-Bot Commercial Moat → CONFIRMED at N=2 (structurally-unambiguous).**

Refined statement:
> *"T5 browser-agent open-core commercial entities intentionally gate anti-bot detection / CAPTCHA bypass / stealth fingerprinting / proxy infrastructure behind commercial Cloud tier. OSS tier ships only local-Chromium + core-agent-logic. Pattern serves multiple simultaneous functions: (a) commercial moat via operationally-scaled infrastructure, (b) liability transfer to Cloud operator, (c) ongoing-R&D cost isolation from library-contributor community."*
>
> **N=2 (Skyvern + browser-use). Distinguishes from:**
> - Pattern #31 (open-core umbrella) — #48 is specific commercial-gate mechanism within #31
> - Pattern #50 (commercial-funnel marketing architecture) — #48 is feature-gate, #50 is upsell-architecture
> - Solid-OSS-anti-bot (crawl4ai v29 counter-evidence) — #48 specifically commercial-gated, not OSS-available

## 4. T5 7-way structural map post-v41

### All 7 T5 entrants + browser-T5 sub-tier N=2

| # | Wiki | Tier | Archetype | Methodology | License | Stars |
|---|------|------|-----------|-------------|---------|-------|
| 1 | deer-flow v9 | T5 | Corporate (ByteDance) | SuperAgent long-horizon | MIT | 62K |
| 2 | autoresearch v10 | T5 | Solo-known (Karpathy) | program.md + git-based ML | MIT | 74K |
| 3 | paperclip v14 | T5 | Community-platform | Constitutional governance + 9 primitives | MIT | 55.9K |
| 4 | Skyvern v24 | T5 | Commercial-entity | **Vision-primary browser** | **AGPL-3.0** | 21.3K |
| 5 | OpenHands v30 | T5 | Academic-commercial fusion | SWE-agent + 5 deployment surfaces | MIT + separate enterprise | 71.7K |
| 6 | DeepTutor v38 | T5 | Academic-lab | Education-agent + research-paper-chain | (per v38) | (per v38) |
| 7 | **browser-use v41** | **T5** | **Commercial-startup (2-founder)** | **Hybrid DOM+vision browser** | **MIT** | **89.9K** |

**Archetype diversity: 7 wikis × 7 distinct archetypes = 100% diversity-per-wiki preserved through v41.**

### Browser T5 sub-tier N=2 structural pair

| Axis | Skyvern v24 | browser-use v41 | Divergence |
|------|-------------|------------------|-----------|
| Organizational archetype | Commercial-entity (plural-founders) | Commercial-startup (2-named-founders Zurich/SF) | Similar commercial-entity family; specific variant differs |
| License | AGPL-3.0 (copyleft-network) | MIT (permissive-max) | **Maximally divergent license choice within same archetype family** |
| Primary methodology | **Vision-primary browser automation** | **Hybrid DOM+vision browser automation** | **Maximally divergent architectural philosophy within same problem-domain** |
| Scale | 21.3K | **89.9K (4.2× larger)** | Significant scale divergence |
| Age | Feb 2024 | ~2024 (author copyright) | Similar age cohort |
| Commercial model | Open-core + Skyvern Cloud | Open-core + Browser-Use Cloud + **browsermerch** | browser-use adds physical-merch monetization |
| Anti-bot | Cloud-gated | Cloud-gated | ✅ Same (Pattern #48 promotion evidence) |
| Multi-LLM | 10+ providers | 15+ providers + LiteLLM (115 total) | browser-use broader |
| Benchmark | WebBench 64.4% + WebVoyager 85.8% | BU Bench V1 (100 tasks, open-source repo) | Different benchmark strategies |
| AGENTS.md | Minimal | **37.4KB** (corpus-largest at T5 commercial-startup) | browser-use substantially heavier |
| MCP support | None documented at v24 | Bidirectional server+client + DXT | browser-use distinctively MCP-integrated |
| Integrations | Zapier / Make / N8N | n8n / Make / Zapier + 1Password + 1000+ Cloud integrations | Similar low-code + browser-use has 1Password + larger Cloud integration layer |

**Structural pair observation:** Two commercial-entities chose **maximally divergent licenses** (AGPL-3.0 vs MIT) and **maximally divergent architectural philosophies** (vision-primary vs hybrid DOM+vision) within the **same problem domain** at **same T5 tier**. Both reached viable scale (21K and 89.9K respectively). **Browser automation as problem domain admits multiple winning architectures simultaneously.**

### Scale-divergence within-archetype observation

browser-use at 89.9K = 4.2× Skyvern at 21.3K. Same archetype family (commercial-entity browser-agent), same tier (T5), same problem domain. **Scale does not correlate with archetype in this sub-tier.**

Possible scale-divergence drivers:
1. **License permissiveness** — MIT attracts more consumption than AGPL-3.0 (network-copyleft deters SaaS adoption without source-disclosure)
2. **Multi-LLM breadth** — 115 providers vs ~10 = broader developer reach
3. **MCP integration** — bidirectional MCP + DXT creates Claude Desktop one-click install pathway
4. **Hybrid architecture pragmatism** — DOM indices are easier-to-reason-about debug-artifact than vision-only (developer adoption friction lower)
5. **2-founder active social presence** (Magnus @mamagnus00 + Gregor @gregpr07) vs "founders@skyvern.com" collective attribution
6. **ChatBrowserUse proprietary model + pricing visibility** ($0.20/1M in README FAQ) — commercial-clarity

**Observational value:** Within-archetype scale divergence is pattern-adjacent; not yet a confirmable pattern. Watch-list.

## 5. Pattern #46 Duo-Founder un-stale analysis

### Prior state

- **v28 stale-flag:** Han brothers (Unsloth v23) = N=1 since v23
- **v29 audit:** stale-flagged; retroactive +5-wiki threshold crossed

### v41 browser-use evidence

**Public founders (from README footer + pyproject.toml):**
- **Gregor Zunic** (pyproject authors field + LICENSE copyright) — San Francisco
- **Magnus (@mamagnus00)** (README Twitter badge) — Zurich

**"Made with ❤️ in Zurich and San Francisco"** = explicit bi-location 2-founder signal.

### N=2 structurally-unambiguous check

| Axis | Han brothers (Unsloth v23) | Magnus + Gregor (browser-use v41) |
|------|----------------------------|-----------------------------------|
| Founder count | 2 | 2 |
| Both engineers? | Yes (both technical) | Yes (both technical inferred from founder-level codebase engagement) |
| Bi-location? | Not disclosed | **Yes (Zurich + SF)** |
| Same-family? | Yes (brothers) | No (presumed; not disclosed) |
| Commercial entity? | Yes (Unsloth AI) | Yes (Browser Use) |
| OSS agent-adjacent product? | **Yes (training infra)** | **Yes (browser agent infra)** |
| Scale reached? | 62.2K | 89.9K |

**Structurally unambiguous?** Both are 2-engineer-founder teams building OSS agent/ML infrastructure with commercial company. Different family/location specifics don't break structural equivalence.

**Criterion 2 (structural-N=2) met with observation caveat:** Sub-variant axes exist (family-relationship / bi-location / same-discipline-vs-complementary). Promotion should acknowledge sub-variants.

### Un-stale proposal

- **Un-stale at v41** ✅
- **Promotion-candidate for next mini-audit** under Criterion 2
- **Sub-variant axes to document at promotion:**
  - 46a: **family-founded** (Han brothers Unsloth v23)
  - 46b: **partnership-founded-bi-location** (Magnus/Gregor browser-use v41)
  - Future sub-variants possible (co-founder with non-engineering partner; same-university-cohort; etc.)

**UN-STALE mechanism first use at v41** (post-v30 OpenHands un-stale of #42 + #44 established pattern).

## 6. Zero-new-active-candidate streak

| Wiki | New active candidates | Running streak |
|------|-----------------------|----------------|
| v37 bizos | 0 | 1 |
| v38 DeepTutor | 0 | 2 |
| v39 | 0 | 3 |
| v40 claude-context | 0 | 4 |
| **v41 browser-use** | **0 (target)** | **5** |

**v41 registration decisions:**
- Hybrid DOM+vision: NOT registered (counter-evidence observation on #47, not new candidate)
- BrowserMerch monetization: NOT registered (within-#31 observation note)
- Bidirectional MCP server+client: NOT registered (within-#18 strengthening)
- `cdp-use` + `bubus` + own-tooling ecosystem: NOT registered (within-#17 variant 3 strengthening)
- `bu-30b-a3b-preview` OSS model: NOT registered (watch-list; N=1)
- AGENTS.md 37KB + explicit versioning: NOT registered (within-#22 strengthening)
- Tabs-not-spaces Python style: NOT registered (one-off stylistic observation; not pattern)
- 15-min session cap: NOT registered (within-Cloud-sub-observation of #48)
- Auto-eval judge: NOT registered (within-Cloud-sub-observation of #50)
- Skills marketplace Cloud-only: NOT registered (within-#50 strengthening)
- Pattern #48 promotion: promotion of existing candidate, not new registration
- Pattern #46 un-stale: un-stale of existing stale, not new registration

**5 consecutive wikis with zero new active candidates confirmed at v41.** Consolidation-forward discipline demonstrated strongly across 5 wikis.

**Ratio preservation:**
- Pre-v41: 34 confirmed + 23 active + 4 stale + 8 retired + 4 OT = 73 full / 57 active (ratio 0.68:1)
- Post-v41 (with proposed changes): 34 confirmed + 23 active + 3 stale (#46 un-staled) + 8 retired + 4 OT = **72 full / 57 active** (ratio 0.68:1 preserved)
- After next mini-audit (if #48 promoted + #46 promoted): 36 confirmed + 21 active + 3 stale + 8 retired + 4 OT = **72 full / 57 active** (ratio 21:36 = **0.58:1**, biggest ratio improvement since v31 mini-audit)

## 7. Pattern Library strengthening inventory at v41

Without any new candidate registrations, v41 provides strengthening for:

| Pattern | Pre-v41 | Post-v41 | Significance |
|---------|---------|----------|--------------|
| #8 Research-Benchmark | 12 data points | **13** | BU Bench V1 open-source benchmark repo; 2nd browser benchmark |
| #17 Ecosystem-Layer v3 commercial-startup | ~12 data points | **13-14** | browser-use + browsermerch + SDK + cdp-use + bubus = 5-product ecosystem |
| #18 MCP Agent Runtime | ~11 data points | **12** | Bidirectional server+client + DXT packaging |
| #22 AGENTS.md | (several) | (strengthened) | 37KB = corpus-largest explicit AGENTS.md at T5 commercial-startup; explicit "Version 2" header |
| #27 Community-Viral Scale Path | ~16 data points | **17** | 89.9K in ~18mo ≈ 5K/month sustained |
| #28 Multi-Provider AI Support | 8 data points | **9** | 15 native + LiteLLM = 115 provider surface; OCI adapter corpus-first |
| #31 Open-Core Commercial Entity | 4 data points | **5** | MIT-at-89.9K = most-permissive at largest-scale |
| #50 Commercial-Funnel Companion Platform | 3 data points | **4** | Browser-Use Cloud 4th; AGENTS.md-embedded upsell = sub-observation |
| #48 Proprietary Anti-Bot Commercial Moat | 1 candidate | **CONFIRMED at N=2** (proposed at next mini-audit) | Skyvern + browser-use structurally-unambiguous |
| #46 Duo-Founder | STALE N=1 | **UN-STALE N=2** + promotion-candidate | Han brothers + Magnus/Gregor |

**Corpus-first observations (promoted to open-questions / watch-list, not pattern registrations):**
1. Physical-merch monetization at T5 open-core (browsermerch)
2. Browser-agent company releases OSS model weights alongside proprietary hosted API (bu-30b-a3b-preview)
3. AGENTS.md explicit "Version 2" semantic-versioning header
4. Dual-API-version simultaneous active-maintenance (v2 + v3)
5. Dual-language SDK Python + TypeScript
6. CDP-WebSocket open-access at commercial-tier (agent-agnostic browser infrastructure positioning)
7. Zero-friction OSS→Cloud migration via decorator (`@sandbox`)
8. AGENTS.md-embedded LLM-directed commercial-upsell instructions
9. 15-min Cloud session cap (technical + commercial gate)
10. Auto-eval judge at commercial tier
11. OCI LLM adapter corpus-first
12. 9 system-prompt variants with model-aware dispatch
13. Tabs-not-spaces Python indentation at 89.9K stars
14. Bi-location 2-founder team Zurich/SF

## 8. Cross-references

- [[(C) Core product — Agent + Browser + Tools + Hybrid DOM+Vision + 15 LLM providers]] — hybrid architecture detail (Entity 1)
- [[(C) Browser-Use Cloud + commercial-funnel + stealth gated + browsermerch]] — commercial-gate evidence (Entity 2)
- [[(C) Storm Bear meta-entity 30th consecutive + vault-adjacent lessons]] — operator-impact meta (Entity 4)
- Sibling pattern-founders: Skyvern v24 (#47 + #48 original registration)
- Sibling pattern-refiner: crawl4ai v29 (#47 + #48 narrowing counter-evidence)
- Sibling un-stale-partner: Unsloth v23 (#46 original N=1)
- Sibling T5 peers: deer-flow v9 / autoresearch v10 / paperclip v14 / OpenHands v30 / DeepTutor v38
- Phase 4b deliverable: [[03 Published/(C) T5 7-way + Pattern 47 + 48 resolution + browser T5 N=2|published phase 4b]]

---

**Pattern #47 stays candidate N=1 (Skyvern vision-primary unique); browser-use documented as counter-evidence narrowing scope; 3-point architectural spectrum formalized (vision-primary / hybrid / DOM-only). Pattern #48 PROMOTES to CONFIRMED at N=2 structurally-unambiguous (Skyvern + browser-use). Pattern #46 UN-STALES to N=2 + promotion-candidate (Han brothers + Magnus/Gregor). 5-wiki zero-new-active-candidate streak preserved. T5 extends to N=7 with 100% archetype diversity maintained. Browser T5 sub-tier N=2 = structural pair with maximally-divergent license + architectural choices (AGPL+vision-primary vs MIT+hybrid-DOM+vision).**
