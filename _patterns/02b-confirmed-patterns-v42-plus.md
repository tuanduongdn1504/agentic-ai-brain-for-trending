### Promoted at v36 mini-audit (#69 + #73 + #59)

#### ✅ #69 Agent-PR Fast-Track Governance Protocol (PROMOTED v36 mini-audit under structural-N=2 criterion)
**Status at v36 mini-audit:** PROMOTED to CONFIRMED. Registered as candidate v31 awesome-mcp-servers (N=1 stale-risk-flagged at registration); strengthened v36 pi-mono to structurally-unambiguous N=2. v31 prediction validated.

**Evidence at N=2 with sub-variant diversity:**

| # | Wiki | Sub-variant | Authored-by | Mechanism |
|---|------|-------------|-------------|-----------|
| 69a | awesome-mcp-servers v31 | `🤖🤖🤖` title suffix | Contributor (agent-authored PRs) | Opt-in PR title marker |
| 69b | pi-mono v36 | `lgtm` / `lgtmi` | Maintainer (approval gating) | Explicit approval command disambiguates LGTM-as-vibe vs LGTM-as-authorization |

**Formal statement (promoted):**
> Frameworks with high contributor + agent activity adopt explicit agent-PR fast-track governance protocols — workflow-level primitives that route automated-agent-authored or agent-reviewed PRs distinctly from human-authored ones. Two structural sub-variants: **(a) contributor-side disclosure** (title/body marker); **(b) maintainer-side approval gating** (explicit approval command). Protocols emerge in high-throughput repos where ambient agent activity + PR volume create signal-to-noise problems. Active-workflow-primitive successor to retired Pattern #23 AI-Disclosure (passive declaration).

**Cross-references:** Pattern #23 (RETIRED v27) / Pattern #7 Marketplace Emergence / Pattern #12 Governance-Depth Correlation.

**Confidence:** Medium-High. N=2 at structurally-distinct sub-variants. N=3+ expected within v40-v45.

---

#### ✅ #73 Regional-Archetype-Registry T1 Meta-Pattern (PROMOTED v36 mini-audit under meta-pattern-at-N=3-consolidation criterion)
**Status at v36 mini-audit:** PROMOTED to CONFIRMED under routine v2.1 criterion 5 (meta-pattern-at-N=3-consolidation). **2nd meta-pattern-at-N=3 promotion in corpus history** (first was #68 Awesome-List-Genre at v31 mini-audit).

**Evidence at N=3 across 3 distinct regions:**

| Sub-variant | Region | Wikis | Distinguishing features |
|-------------|--------|-------|-------------------------|
| **73a Korean** | Korea | OMC v27 (Yeachan Heo) | Korean README primary; Korean collaborator clustering; Korean OSS tradition |
| **73b VN** | Vietnam + VN-diaspora | codymaster v12 (Tody Le VN-in-VN) + claude-howto v32 (Luong Nguyen VN-diaspora Paris) | 2 sub-sub-variants; 742× scale divergence |
| **73c Pakistani** | Pakistan | claude-code-best-practice v34 (Shayan Rais Karachi) | Claude Community Ambassador; multi-channel distribution |

**Formal statement (promoted as meta-pattern):**
> T1 Agent-as-assistant frameworks exhibit observable regional-archetype diversity distinct from US-anglophone default. Meta-pattern wraps 3 structurally-distinct sub-variants: Korean (73a), VN (73b), Pakistani (73c). Each displays characteristic combinations of: (a) primary-language README prominence, (b) regional-collaborator clustering, (c) local OSS tradition inheritance, (d) audience-targeting + distribution-channel choices, (e) commercial-vs-community positioning defaults. Meta-pattern absorbs prior #55 Korean + #70 VN as sub-classifications. Additional sub-variants expected as T1 grows (Austrian 73d observational at v36 pi-mono; Indian cross-tier deferred from v33 GitNexus).

**Absorptions at promotion:**
- **#55 Korean Regional Archetype T1** (stale-candidate) → absorbed as 73a — **first stale-to-retired-via-absorption pathway in corpus**
- **#70 VN-Regional-Archetype T1** (confirmed at v32 mini-audit) → absorbed as 73b — **first confirmed-pattern absorption in corpus**

**Cross-references:** Pattern #17 Ecosystem-Layer / Pattern #27 Community-Viral / Pattern #20 Solo-Scale Ceiling / Pattern #68 Awesome-List-Genre Meta-Pattern (sibling at N=3).

**Confidence:** Medium-High. N=3 at 3 structurally-distinct regions. 4th sub-variant expected v40-v50.

---

#### ✅ #59 Claude Code Plugin Marketplace Native (PROMOTED v36 mini-audit under structural-N=2 criterion)
**Status at v36 mini-audit:** PROMOTED to CONFIRMED [BONUS promotion]. Registered as candidate v27 oh-my-claudecode (N=1); strengthened v35 claude-hud to structurally-unambiguous N=2.

**Evidence at N=2:**

| # | Wiki | Sub-variant | Distribution model |
|---|------|-------------|--------------------|
| 59a | oh-my-claudecode v27 | Marketplace + npm companion | Plugin marketplace primary + `oh-my-claude-sisyphus@latest` secondary |
| 59b | claude-hud v35 | Marketplace-only | Plugin marketplace exclusive; no alternative install |

**Formal statement (promoted):**
> T1 Agent-as-assistant frameworks increasingly adopt Claude Code plugin marketplace as native primary install mechanism. Two sub-variants: **(a) marketplace + companion package manager**; **(b) marketplace-only** (plugin marketplace is the distribution surface). Claude-Code-specific T1-tier sub-pattern of Pattern #7 Marketplace Emergence.

**Cross-references:** Pattern #7 Marketplace Emergence (parent) / Pattern #2 Distribution Evolution.

**Confidence:** Medium-High. N=2 at structural sub-variants. N=3+ expected within 5-10 wikis as Claude Code plugin marketplace matures.

---

### Promoted at v42 mini-audit (#58)

#### ✅ #58 Branding-Package Divergence (PROMOTED v42 mini-audit under structural-N=2 criterion)
**Status at v42 mini-audit:** PROMOTED to CONFIRMED via un-stale pathway. Registered as candidate v27 oh-my-claudecode (N=1 stale-risk-flagged at registration); stale-risk-tracked through v28-v41 without confirmatory evidence; STRENGTHENED v42 ruflo to structurally-unambiguous N=2. **Longest un-stale gap for confirmation in corpus at 15 wikis (v27→v42); prior longest was #42/#44 at 9 wikis (v22→v30).**

**Evidence at N=2 with sub-variant diversity:**

| # | Wiki | Sub-variant | Mechanism | Package strategy |
|---|------|-------------|-----------|------------------|
| 58a | oh-my-claudecode v27 | **rename-without-npm-rename** | Repo/plugin/commands branded `oh-my-claudecode`; npm package name `oh-my-claude-sisyphus` (frozen for distribution continuity) | Single npm package with divergent name (brand evolved post-publish) |
| 58b | ruflo v42 | **rebrand-with-transitional-preserve** | Project rebranded from `Claude Flow` → `Ruflo`; npm maintains 3 parallel packages: `claude-flow@3.5.80` (original, frozen name) + `ruflo@3.5.80` (new brand) + `@claude-flow/cli@3.5.65` (sibling workspace) | Triple-package parallel distribution preserving original + adding new + workspace split |

**Structural parallel + distinction:**

Both demonstrate brand-name-in-README divergence from primary-npm-package-name. 58a is single-package divergence (one package, brand mismatch); 58b is multi-package parallel distribution (original preserved, new added, workspace CLI split). Different sub-variants of same phenomenon: **npm distribution-identity cannot be cheaply renamed once adoption is established**, so brand evolution manifests through sub-variant strategies: rename-without-replacement (58a) or preserve-plus-add (58b).

**Formal statement (promoted):**
> Framework uses different name for repo/brand-identity vs primary npm package distribution. Creates user-onboarding confusion risk BUT preserves distribution continuity where brand renaming without breaking dependencies is desired. Two structural sub-variants observed:
>
> **58a rename-without-npm-rename** — repo/plugin/commands renamed; original npm package name frozen (single package). Example: oh-my-claudecode v27 (`oh-my-claudecode` brand, `oh-my-claude-sisyphus` npm).
>
> **58b rebrand-with-transitional-preserve** — new primary name deployed as additional npm package while original preserved for install-command continuity; may include workspace split. Example: ruflo v42 (Claude Flow → Ruflo; `claude-flow` + `ruflo` + `@claude-flow/cli` triple-package parallel).
>
> Pattern emerges when framework: (a) gains adoption under original name, (b) evolves brand identity, (c) cannot afford to break existing `npm install X` install paths referenced in community tutorials/docs. Distinct from Pattern #2 Distribution Evolution (framework adds distribution surfaces); #58 is specifically identity-divergence at the package-manager level.

**Cross-references:**
- **Pattern #2 Distribution Evolution (confirmed):** Both distribution-layer; #2 = adding surfaces, #58 = naming identity divergence at primary surface.
- **Pattern #7 Marketplace Emergence (confirmed v11):** Adjacent — marketplaces are alternative distribution channels where brand-name divergence is less sticky.
- **Pattern #59 Plugin Marketplace Native (promoted v36):** Claude Code plugin marketplace sidesteps npm-package-identity-constraint; frameworks distributing via marketplace (59a + 59b) avoid #58's npm-frozen-name problem.
- **Pattern #17 Ecosystem-Layer Organizations (confirmed v15):** Ecosystem-portfolio publishers (RuvNet at ruflo) face multi-package naming decisions that can produce #58; ecosystem-layer orgs more exposed to 58b sub-variant.

**Confidence:** Medium-High. N=2 at 2 structurally-distinct sub-variants. Both observations independently discovered (v27 + v42 are 15 wikis apart; no cross-contamination). Promotion is conservative (not meta-pattern consolidation — just structural-N=2).

**Prediction:** N=3+ plausible within v45-v55 as ecosystem matures. Candidate observations: frameworks that have gone through rebrand (e.g., during commercialization transitions; major-version renames).

---

### Promoted at v42-deferred mini-audit (#46 + #48)

Back-to-back with v42 mini-audit ~40 min earlier same session. Closes the 3 v41-deferred mini-audit actions that were explicitly scoped out of the v42 mini-audit. 2 structural-N=2 promotions (first pair-promotion under same criterion in corpus); 1 candidate-level refinement (#47 3-point architectural spectrum; see Active Candidates section for #47's updated entry).

#### ✅ #46 Duo-Founder Archetype (PROMOTED v42-deferred mini-audit under structural-N=2 criterion)
**Status at v42-deferred mini-audit:** PROMOTED to CONFIRMED via un-stale pathway. Prior status path: v23 registration (N=1 Han brothers Unsloth) → v29 audit STALE-CANDIDATE (retroactive from v28 threshold) → v41 UN-STALE at N=2 (Magnus/Gregor browser-use joins) → v42-deferred PROMOTED.

**Evidence at N=2 with sub-variant diversity:**

| # | Wiki | Founders | Sub-variant | Mechanism | Commercial entity |
|---|------|----------|-------------|-----------|-------------------|
| 46a | Unsloth v23 | Daniel Han + Michael Han | **family-duo** (likely brothers; shared surname) | Family-founded; co-located; Apache core + AGPL Studio UI | Unsloth AI (commercial funnel) |
| 46b | browser-use v41 | Magnus Müller + Gregor Žunič | **professional-duo** (independent backgrounds; bi-located Zurich + SF) | Partnership-founded; geographically-distributed; MIT + Cloud | Browser-Use Inc. (commercial funnel) |

**5-dimension structural parallel:**
1. 2-person founding teams (not solo, not team-of-3+, not corporate, not LLC) ✅
2. Early-stage commercial entities ✅
3. >50K-star community-viral scale (Unsloth 62.2K; browser-use 89.9K) ✅
4. Commercial funnel (Unsloth AI commercial; Browser-Use Cloud) ✅
5. Performance-differentiated positioning ✅

**Formal statement (promoted):**
> 2-person founding teams demonstrably reach >50K-star community-viral scale in agent-space, representing an organizational archetype structurally distinct from: (a) solo-founder (Pattern #17 variant 1), (b) 3+-founder teams (e.g., OpenHands v30 3-co-founder academic-industry triangle), (c) LLC formalization (BMAD v11), (d) pre-existing corporate entities (spec-kit v17 GitHub; markitdown v28 Microsoft), (e) academic-lab affiliations (Pattern #44).
>
> **Sub-variants observed:**
>
> **46a family-duo** — shared context (family relationship, surname-match or known-family-link, typically co-located). Example: Unsloth v23 (Daniel Han + Michael Han).
>
> **46b professional-duo** — independent backgrounds (different surnames; potentially bi-located across geographies; professional-only relationship). Example: browser-use v41 (Magnus Müller + Gregor Žunič; Zurich + SF).
>
> Both sub-variants achieve commercial-entity status with OSS core + commercial-funnel pattern (Pattern #31 + Pattern #50 co-present in observed N=2).

**Cross-references:**
- **Pattern #17 Ecosystem-Layer Organizations (CONFIRMED v15):** #46 is organizational archetype at founding-team level; #17 is at ecosystem-portfolio level. Not all #46 duos become #17 ecosystem-layer orgs.
- **Pattern #20 Solo-Scale Ceiling Dictionary:** #46 is a distinct archetype row (2-person-founding) vs solo-founder archetype. >50K observations demonstrate 2-person-founding is viable at community-viral scale.
- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24 → N=6):** Both #46 observations fit #31 (OSS core + commercial entity); may correlate that duo-founder archetype gravitates to open-core.
- **Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v31 mini-audit):** Both #46 observations exhibit #50 (Cloud-as-upsell-funnel); correlation may firm up at N=3.

**Confidence:** Medium-High. N=2 at 2 structurally-distinct sub-variants (46a family + 46b professional). Both observations at >50K-star scale (structural signal that duo-founder is viable at community-viral scale, not niche-small).

**Prediction:** N=3+ plausible within v43-v55. Candidate observations: any framework with 2 named co-founders and small team (distinct from LLC/corporate/academic). 46b professional-duo likely to grow with remote-first AI startup proliferation.

#### ✅ #48 Proprietary Anti-Bot Commercial Moat (PROMOTED v42-deferred mini-audit under structural-N=2 criterion)
**Status at v42-deferred mini-audit:** PROMOTED to CONFIRMED. Prior status path: v24 registration (N=1 Skyvern) → v29 audit REFINED via crawl4ai counter-evidence (scope narrowed to "proprietary-commercial-gated anti-bot specifically"; NOT "all anti-bot in agent-space") → v41 N=2 STRUCTURALLY-UNAMBIGUOUS (browser-use MIT joins Skyvern AGPL-3.0; 9/9 structural dimensions match across maximally-divergent licenses) → v42-deferred PROMOTED.

**Evidence at N=2 with 9-dimension structural parallel:**

| # | Wiki | License | Commercial entity | Cloud tier | Anti-bot gated? |
|---|------|---------|-------------------|------------|-----------------|
| 48-a | Skyvern v24 | **AGPL-3.0** (maximum copyleft) | Skyvern-AI | Skyvern Cloud (paid) | ✅ proprietary gated behind Cloud |
| 48-b | browser-use v41 | **MIT** (maximum permissive) | Browser-Use Inc. | Browser-Use Cloud (paid) | ✅ proprietary gated behind Cloud |

**9-dimension structural parallel:**
1. Browser-agent tier T5 commercial entities ✅ both
2. OSS core + Cloud commercial tier ✅ both
3. Anti-bot detection gated behind Cloud ✅ both
4. Cloud positioned as "production" path ✅ both
5. Separate pricing pages ✅ both
6. Proprietary tech stack in Cloud (not in OSS) ✅ both
7. Anti-bot as differentiation from OSS-only competitors ✅ both
8. Independent funding/commercial models (different orgs) ✅ both
9. OSS cannot reproduce Cloud's anti-bot even with full source access ✅ both (structural isolation)

**Structurally-unambiguous signal:** License-permissiveness does NOT determine gating. AGPL-3.0 Skyvern + MIT browser-use — at maximally-divergent license poles — gate equivalently. Pattern is **commercial-strategy-driven, NOT license-driven**. License-axis invariance is a structural-strong signal (stronger than typical structural-N=2 promotions).

**Counter-evidence reconciliation (crawl4ai v29):**
crawl4ai demonstrates OSS-disclosed 3-tier anti-bot at 64K stars with distinct commercial model (4-tier sponsorship without proprietary moat). v29 audit correctly scoped #48 to "proprietary-commercial-gated anti-bot specifically." crawl4ai exemplifies the OPPOSITE strategy (OSS-disclosed anti-bot = Pattern #64 candidate; different monetization class).

Corpus now has 3 distinct browser-anti-bot strategies with clean boundaries:
- **#48 (CONFIRMED) — Proprietary commercial-gated:** Skyvern AGPL-3.0 core + Cloud tier; browser-use MIT core + Cloud tier
- **#64 (CANDIDATE) — OSS-disclosed, no commercial moat:** crawl4ai v0.8.5 OSS anti-bot + sponsorship-tier monetization
- Future candidates from non-browser verticals with analogous moats

**Formal statement (promoted):**
> Browser-agent commercial entities with OSS core + commercial Cloud tier consistently gate anti-bot detection capability behind the commercial tier as primary differentiation moat. License permissiveness (MIT vs AGPL) does not determine the gating decision — commercial strategy does. Structural invariant across maximally-divergent licenses.
>
> **Structurally distinct from OSS-disclosed anti-bot strategy** (see Pattern #64 Open-Source Anti-Bot Detection candidate + crawl4ai v29 precedent): #48 frames anti-bot as commercial-gated moat; #64 frames anti-bot as OSS-disclosed capability with non-moat monetization. Both coexist as distinct archetypes; frameworks choose one or the other based on commercial strategy, not capability.
>
> **Required dimensions for future #48 observations:** (a) browser-agent tier T5 commercial entity, (b) OSS core with commercial Cloud tier, (c) anti-bot specifically gated behind Cloud (not in OSS), (d) Cloud positioned as production path, (e) proprietary tech-stack in Cloud reproducibility-protected even with full OSS source access.

**Cross-references:**
- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24 → N=6 at v42):** #48 is sub-pattern within #31 specific to browser-agent vertical; commercial differentiation mechanism varies across #31 verticals (anti-bot for browser-agent; enterprise-directory for SWE-agent OpenHands; feature-delta SaaS for code-bridge GitNexus). #48 codifies the browser-vertical-specific form.
- **Pattern #47 Vision-Based Browser Automation (CANDIDATE, refined at this audit):** Orthogonal axis — #47 is architectural (DOM vs vision); #48 is commercial (OSS-disclosed vs gated). Browser-agent frameworks position independently on both.
- **Pattern #64 Open-Source Anti-Bot Detection (CANDIDATE):** Counter-archetype to #48. N=1 at crawl4ai v29; awaiting 2nd observation. If #64 reaches N=2, corpus documents both browser-anti-bot poles with equal structural rigor.
- **Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v31 mini-audit):** Adjacent commercial pattern; #50 is about Cloud-as-upsell-funnel structurally; #48 is about specific-capability-gating mechanism within Cloud.

**Confidence:** High. N=2 with 9/9 structural-dimension match across maximally-divergent licenses is maximally-strong structural-N=2 evidence in corpus — stronger than typical structural-N=2 promotions due to license-axis-invariance sharpening the commercial-strategy-driven claim.

**Prediction:** N=3 likely within v43-v50 as browser-agent commercialization continues. Candidate observations: Agent-E, LaVague, AutoBrowse, upcoming browser-agent commercial entrants. If/when N=3 reached, #48 becomes CONFIRMED across 3 independent commercial entities (default 3-observation criterion).

**Structural firsts contributed at v42-deferred mini-audit:** Maximally-divergent-orthogonal-axis-invariance (license-axis AGPL vs MIT) as structural-N=2 signal-strength enhancer — first such invariance-test in corpus. Registered for routine v2.2 consideration as signal-strength enhancer criterion.

---

### v44 direct updates (2026-04-24) — 8TH CONSECUTIVE ZERO-REGISTRATION WIKI + PATTERN #42 N=3 WITH 3-CS-CONFERENCE-CLASS DIVERSIFICATION + PATTERN #17 VARIANT 2 5-DATA-POINT MILESTONE + PATTERN #44 SUB-VARIANT 44d CORPORATE-RESEARCH-LAB + PATTERN #2 CORPUS-MAXIMUM + OUTSIDE-SCOPE 8TH SUB-TYPE ML-SECURITY-CLASSIFIER + GOOGLE 2ND CORPUS ENTRANT + 18 CORPUS-FIRSTS

magika v44 = 44th wiki. `google/magika` = "Detect file content types with deep learning." **16.6K stars (medium scale) / 986 forks (5.9%) / 104 open issues / 62 watchers / Apache-2.0 / Python 33.1% + Rust 26.3% + TypeScript 18.4% + Svelte 4.9% + Go 3.9% / v1.0.2 (2026-02-27 latest) / Apache-2.0**. Authored by **Google Research (Anti-Abuse team) — 12 authors including Elie Bursztein (senior); Yanick Fratantonio (first)**. Published at **ICSE 2025** (International Conference on Software Engineering, A*-ranked Software Engineering venue) + arXiv [2409.13768](https://arxiv.org/abs/2409.13768). ~3 MB ONNX model trained on ~100M samples across **216 content types** with ~99% avg accuracy and ~2ms inference on single CPU. Deployed at Google infrastructure-scale: Gmail + Drive + Safe Browsing — **"hundreds billions samples on a weekly basis"**. Third-party integrations: VirusTotal + abuse.ch. 5-language multi-binding (Rust CLI + Python + JS+WASM + Go + Rust crate) + 6+-channel distribution (pipx/brew/curl/pip/npm/cargo/docker). **"Not an official Google project" disclaimer** = Google-Research-OSS archetype distinct from Google-corporate-official (gws v13).

**Scope classification:** OUTSIDE-SCOPE — **ML-security-classifier (8TH outside-scope sub-type NEW)**. Distinct from 7 prior sub-types (education-aggregator absorbed / foundation-model / prompt-leak-archive / training-infrastructure / design-template-aggregator absorbed / MCP-server-aggregator absorbed / business-OS-as-product OT#74). 7 formal criteria for classification: ML-model-centered + infrastructure-scale + security-adjacent + not-agent-framework + not-training-infra + not-foundation-model + peer-reviewed-research-lineage.

**Evidence strengthening:**

- **#42 Academic-Published Peer-Reviewed Framework (CONFIRMED v31 mini-audit)** — **N=3 STRENGTHENING with 3-CS-conference-class diversification** (ACL 2024 LlamaFactory NLP + ICLR 2025 OpenHands ML + **ICSE 2025 magika Software Engineering NEW**). All 3 venues A*-ranked. First SE-class data point in pattern. **Formulation-extension candidate at next audit**: acknowledge 3-CS-conference-class breadth explicitly with 4 family sub-categories (NLP / ML / SE / Security).
- **#44 Academic-Lab Affiliation Archetype (CONFIRMED v31 mini-audit)** — **NEW sub-variant 44d corporate-research-lab** (Google Research Anti-Abuse team). Distinct from 44a-c academic-university variants (Lab4AI / UIUC+CMU / HKU / SJTU+NUS+Huawei). First corporate-research-lab observation in pattern. Proposes explicit sub-variant formalization at next audit (private-industry-employer + corporate-research-specific-incentives + infrastructure-scale-deployment + professional-engineering-staff-continuity).
- **#17 Ecosystem-Layer Organizations variant 2 big-tech-curator (CONFIRMED v15)** — **5-DATA-POINT MILESTONE (corpus-first confirmed-variant at 5 data points)**. Microsoft 3 (v6 + v28 + v34) + Google 2 (v13 gws + v44 magika). Proposes sub-distinction 2a corporate-official (gws) vs 2b corporate-research-OSS (magika) at next audit; Google bridges both sub-distinctions.
- **#2 Distribution Evolution (CONFIRMED v1)** — **CORPUS-MAXIMUM STRENGTHENING**. 5-language multi-binding (exceeds pi-mono v36 4-language monorepo) + 6+-channel distribution (exceeds all prior) + hybrid Python-wheel-embeds-Rust-binary + pure-Python-fallback (corpus-first hybrid) + 4-platform cross-compilation via cargo-dist self-updating installer + GitHub Attestations. Corpus-maximum distribution sophistication at v44.
- **#12 Governance-Depth (REFINED v42 → 3-factor model: maturity-ambition + maintainer-philosophy + scale-tier)** — Google corporate baseline confirms refined formulation: OpenSSF Best Practices badge #8706 + CodeQL + Scorecard + Dependabot + 19 GitHub workflows + CITATION.cff + .gemini Gemini Code Assist + CLA. Strong governance at medium-scale (16.6K) demonstrates organization+maintainer-philosophy dominance over scale-correlation.
- **#58 Branding-Package Divergence OBSERVATION-TRACK (promoted v42 mini-audit; this OT is separate 3rd episodic watch)** — `website/` (Svelte) + `website-ng/` (Astro migration-in-progress) duality = 3rd episodic observation after OMC v27 + ruflo v42. Sub-variant 58c website-transition-within-same-repo observational. Stays OT (episodic; no architectural pattern emerging).
- **#27 Community-Viral Scale Path (CONFIRMED v21)** — observational sub-distinction: industrial-deployment-scale ("hundreds billions samples weekly at Google internal routing") is distinct from star-count community-viral-scale (magika is medium 16.6K community-viral metric). Within-pattern observation; not new candidate.
- **#31 Open-Core Commercial Entity (CONFIRMED)** — observational counter-evidence: Google-Research-OSS (fully-OSS + no-commercial-tier + no-commercial-moat) does NOT invalidate #31 (which is about commercial entities with OSS+commercial split). Google-Research-OSS operates on different model: corporate-research-lab + fully-OSS + infrastructure-deployment-via-internal-consumer. Observational within-pattern note.

**Observational observations (within-pattern notes; not new candidates):**
- CITATION.cff (corpus-first Citation File Format) — within #42 academic-citation-discipline
- In-repo paper PDF `assets/2025_icse_magika.pdf` (corpus-first) — within #42
- .gemini/config.yaml Gemini Code Assist config (corpus-first) — within #12 Google-internal-tooling
- OpenSSF Best Practices + CodeQL + Scorecard + Dependabot 4-layer security stack — within #12
- 9-model-version evolution bundled CHANGELOG (corpus-first ML-model-artifact) — within #42
- Per-content-type adaptive threshold system (corpus-first classifier primitive) — within #2
- Limited-byte-subset inference for near-constant time — within #2
- Python-wheel-embeds-Rust-binary + pure-Python-fallback hybrid — within #2 corpus-max
- Google-Research-OSS archetype (corporate-research-lab fully-OSS no-commercial-moat) — within #17 variant 2 sub-distinction 2b + #44 sub-variant 44d
- Fully-local browser-ML-inference via TensorflowJS + ONNX WASM — within #2
- 19 GitHub workflows at medium-scale outside-scope — within #12
- "Not an official Google project" disclaimer at Google-authored repo — within #17 variant 2 sub-distinction

**New candidates registered at v44:** **ZERO** (consolidation-forward discipline; 8-consecutive-wiki zero-new-active-candidates streak extends v37-v44 — NEW corpus-longest-streak-record).

**Un-stale check results:** Pattern #45 Dual-Licensing negative (magika single Apache-2.0); Pattern #52 Extreme-Viral-Velocity negative (16.6K not extreme); all 3 stale candidates remain stale.

**Tier status post-v44:**
- **Outside-scope: 9 wikis across 8 sub-types (5 standalone-distinct + 3 absorbed into Pattern #68)**
- All 5 Storm Bear tiers multi-entrant validated (unchanged)
- T1: 13 / T2: 3 / T3: 3 / T4: 7 / T5: 8 / **Outside-scope: 9 (8 sub-types)**

**Post-v44 counts:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = **72 full / 57 active**. **Ratio 20:37 = 0.54:1 UNPRECEDENTED preserved unchanged from post-v43.** 0.41 buffer below 0.95:1 mini-audit trigger (unchanged).

**5th v2.1-era routine execution — all discipline mechanisms exercised cleanly:**
- Phase 0.5 expanded pattern pre-check: un-stale all 3 negative
- Phase 0.6 overlap pre-check: all observations routed within-existing-pattern
- Phase 0.9 Storm Bear meta-entity applicability: 33rd consecutive
- Consolidation-forward discipline: 0 new active candidates target achieved
- N=1 stale-risk-flagging at registration: N/A (no registrations)
- Counter-evidence: Pattern #31 fully-OSS-no-commercial-tier observational (not refinement)
- Fact-verification: Pattern #42 / #17 variant 2 / #44 44d references verified against PATTERN_LIBRARY.md

**18 corpus-firsts at v44:**
1. ICSE 2025 3rd CS-conference-class venue (Pattern #42 breadth)
2. Pattern #44 sub-variant 44d corporate-research-lab (Google Research first observation)
3. Pattern #17 variant 2 5-data-point milestone (corpus-first confirmed-variant-at-5)
4. ML-security-classifier 8th outside-scope sub-type formalization
5. Corpus-maximum Pattern #2 distribution (5 bindings + 6+ channels + hybrid wheel)
6. Python-wheel-embeds-Rust-binary + pure-Python-fallback hybrid
7. In-repo ICSE 2025 paper PDF (`assets/2025_icse_magika.pdf`)
8. CITATION.cff explicit Citation File Format
9. .gemini/config.yaml Gemini Code Assist config
10. 4-layer security tooling stack (OpenSSF + CodeQL + Scorecard + Dependabot)
11. 9-model-version evolution bundled artifact
12. Per-content-type adaptive threshold system (classifier primitive)
13. Google-Research-OSS archetype documentation (corporate-research-lab fully-OSS no-commercial-moat)
14. "Not an official Google project" disclaimer at Google-authored repo
15. **8-consecutive-wiki zero-new-active-candidates streak** (v37-v44)
16. Fully-local browser-ML-inference via TensorflowJS + ONNX WASM at OSS scale
17. Google 2-entrant corpus organizational archetype
18. 5-language multi-binding at ML-classifier scope

**⚠️ v27 diagnostic HIGH bundle deferred 23 sessions** (v28/v29/v30/v31/v31-mini/v32/v32-mini/v33/v34/v34-action/v35/v36/v37/v38/v39/v40/v41/v42/v42-deferred/v43/**v44**/next) — BLOCKING-RECOMMENDATION 4.6× threshold-exceeded. Pattern Library is NOT bottleneck at v44 (ratio 0.54:1 unprecedented healthy); operator-facing vault work remains next-highest-ROI.

**Full v44 wiki:** `03 Projects/magika - Beginner Analysis/` — see `(C) Outside-scope 8th sub-type + Pattern 42 N=3 + 17 variant 2 N=5 + 44 sub-variant 44d.md` for full Phase 4b deliverable.

---

### v45 direct updates (2026-04-24) — 9TH CONSECUTIVE ZERO-REGISTRATION WIKI (CORPUS-LONGEST STREAK) + PATTERN #31 N=8 STRENGTHENING + PATTERN #50 N=7 STRENGTHENING + PATTERN #29 AGPL 3RD PROJECT-SCOPE + PATTERN #58 5TH OBSERVATION + T5 N=9 AI-PENTESTER NEW SUB-ARCHETYPE + 34TH CONSECUTIVE STORM BEAR META + 30 CORPUS-FIRSTS

shannon v45 = 45th wiki. `KeygraphHQ/shannon` = "Shannon — autonomous, white-box AI pentester for web applications and APIs." **40.1K stars / 4.4K forks (11.0%) / 195 watchers / 17 open issues / AGPL-3.0 (Shannon Lite) + commercial (Shannon Pro) / TypeScript monorepo pnpm-workspaces (`apps/cli` + `apps/worker`) / main branch / v1.1.0 (2026-04-21 latest) / Trendshift badge repository 15604**. Organization: **Keygraph** (commercial startup; homepage keygraph.io; SOC 2 Type I certified). Product line: Shannon Lite (AGPL-3.0 OSS this repo) + **Shannon Pro (commercial all-in-one AppSec platform with SAST/SCA/secrets/business-logic/pentesting correlation + Tower managed vCISO service)**. Customers: Optexity, Scowtt Inc., Mesmer. Core principle: *"POC or it didn't happen"* / *"No Exploit, No Report."* Published XBOW 96.15% hint-free benchmark result.

**Scope classification:** **T5 Agent-as-application — 9TH T5 ENTRANT + NEW AI-pentester sub-archetype.** 100% T5 archetype-diversity-per-wiki preserved at N=9 (prior 8 sub-archetypes: research-deer-flow v9 / ML-autoresearch v10 / orchestration-paperclip v14 / browser-Skyvern v24 / SWE-OpenHands v30 / education-DeepTutor v38 / browser-browser-use v41 / personal-productivity-rowboat v43).

**Evidence strengthening:**

- **#31 Open-Core Commercial Entity (CONFIRMED v24, N=7 at v43)** — **N=8 STRENGTHENING.** Keygraph 2-tier structure (Shannon Lite AGPL-3.0 OSS + Shannon Pro commercial) with **corpus-first dedicated Pro-tier documentation file SHANNON-PRO.md 26KB** (most-detailed Pro-tier docs in corpus across 45 wikis). Observational sub-variant candidate: "mature-open-core with dedicated Pro-tier documentation file" (N=1 at v45; watch for N=2).
- **#50 Commercial-Funnel Companion Platform (CONFIRMED v31 mini-audit, N=6 at v43)** — **N=7 STRENGTHENING.** Keygraph + Tower managed vCISO service + Shannon Pro = comprehensive companion-platform funnel stack (SOC 2 Type I + case studies + homepage keygraph.io). Ties ruflo v42 / rowboat v43 for corpus-most-elaborate funnel sophistication.
- **#29 License-Category Diversity (CONFIRMED v21)** — **AGPL-3.0 3RD project-scope data point** (Skyvern v24 project-scope + shannon v45 project-scope = **N=2 structural AGPL-at-project-scope**; Unsloth Studio v23 remains component-scope AGPL). AGPL project-scope sub-category reaches structural-N=2 — formalization-candidate at next mini-audit.
- **#58 Branding-Package Divergence (PROMOTED v42 mini-audit)** — **5TH OBSERVATION data point.** `claude-code-router` router-mode sunset with public Discussion #301 notice = feature-deprecation-with-public-discussion-notice sub-variant (feature-lifecycle-within-repo). Distinct from prior: OMC v27 (branding) / ruflo v42 (package-vs-display) / rowboat v43 (website/website-ng) / magika v44 (website-transition).
- **#17 Ecosystem-Layer Organizations variant 3 commercial-startup (CONFIRMED v15)** — **16th-17th data point strengthening.** Keygraph ecosystem = Shannon Lite OSS + Shannon Pro commercial + Tower managed vCISO + SOC 2 Type I + customer case studies (Optexity / Scowtt / Mesmer) + keygraph.io homepage funnel. Reinforces variant 3 commercial-startup ecosystem playbook with security-domain instance.
- **#12 Governance-Depth (REFINED v42 → 3-factor model: maturity-ambition + maintainer-philosophy + scale-tier)** — **strengthening-of-refinement.** Shannon governance primitives (README 39KB + CLAUDE.md 15KB + SHANNON-PRO.md 26KB + COVERAGE.md + LICENSE AGPL 33KB + .env.example + `.github/workflows/release.yml`) at medium-large commercial-startup scope demonstrate strong-governance correlating with maturity-ambition + commercial-startup maintainer-philosophy (not raw scale alone). Reinforces 3-factor refinement.
- **#28 Multi-Provider AI Support (CONFIRMED v25)** — **5-provider data point strengthening.** Anthropic direct + Claude Code OAuth + AWS Bedrock + Google Vertex + Custom-Base-URL-via-LiteLLM = 5 provider paths. Documents *"Only Claude models officially supported"* scope narrowing (provider-diversity ≠ model-diversity at security-critical domain).
- **#27 Community-Viral Scale Path (CONFIRMED v21)** — **20th+ observational data point.** 40.1K stars / ~16 months ≈ 2.5K stars/month = organic-commercial steady-growth sub-path (NOT extreme-viral). Security-domain commercial-startup organic sub-path observation.
- **#22 AGENTS.md (CONFIRMED v17)** — **T5 absence observation data point.** shannon has CLAUDE.md 15KB present but NO AGENTS.md file — T5 absence-continuation observation (consistent with CLAUDE.md-present-AGENTS.md-absent pattern at rowboat v43 YC-startup T5).
- **#18 Agent Runtime Standardization / MCP layer (CONFIRMED v15, MCP-extended at v42 mini-audit)** — **MCP selective-adoption observation.** Shannon Pro uses MCP selectively for TOTP via dedicated MCP server tool (Tier 1 basic 1-5 tools consumer). Confirms pi-mono v36's ~70-75% MCP adoption observation — MCP adoption is scoped not universal.
- **#20 Solo-Scale Ceiling dictionary (CONFIRMED v21 reformulated)** — NEW ROW observation: commercial-startup + open-core-2-tier + AGPL + dedicated-Pro-docs archetype at 40K-in-16-months scale.

**Scope-respect discipline observations (neither strengthening nor counter-evidence):**

- **Pattern #47 Vision-Based Browser Automation (REFINED v29 + v41 + v42-deferred 3-point spectrum)** — shannon uses browser automation BUT **NOT vision-primary** (shannon is DOM-based + CLI-based pentesting, structurally closer to crawl4ai DOM-only variant than Skyvern vision-primary). **Does NOT satisfy un-stale trigger for #47** — #47 remains N=1 Skyvern-unique vision-primary pole with conditional-retirement at v46 if no 2nd vision-primary data point by then. Scope-lock respected.
- **Pattern #48 Proprietary Anti-Bot Commercial Moat (PROMOTED v42-deferred mini-audit)** — shannon is **security-testing domain NOT browser-anti-bot commercial gating**. Pattern #48 scope locked to browser-agent commercial anti-bot/CAPTCHA/stealth/proxies gating; shannon's AGPL + Pro-tier gating is different domain (security-pentesting). **Does NOT strengthen #48** — scope-distinct observation. Scope-lock respected.

**Observational observations (within-pattern notes; not new candidates):**

- XBOW 96.15% hint-free security-domain benchmark — first pentesting-domain benchmark in corpus (within Pattern #8 research-benchmark observational; prior benchmarks WebBench Skyvern / SWE-Bench OpenHands / ML-research-paper chains)
- Static-dynamic correlation pipeline architectural pattern (Pro commercial-only observational)
- Code Property Graph (CPG) at T5 (Pro commercial-only observational)
- Temporal.io workflow durability at T5 (corpus-first) — within-#2 orchestration-architecture observation
- 4 security-tool integrations (Nmap + Subfinder + WhatWeb + Schemathesis) — within-#18 external-tool layer
- Self-hosted runner model with customer data plane + Keygraph control plane split (Pro commercial-only observational)
- Autonomous 2FA/TOTP/SSO login handling — within-#18 MCP layer observation (TOTP via dedicated MCP server in Pro)
- sample-reports/ directory with OWASP Juice Shop + c{api}tal + crAPI real pentest reports (corpus-first proof-of-capability artifact in repo)
- Issues-only-no-PRs governance at 40K scale — within-#12 governance-convention observation
- SOC 2 Type I at T5 commercial-startup — within-#17 variant 3 ecosystem primitive
- Per-invocation ephemeral Docker container + per-scan task queue architecture
- Workspaces + git-checkpoint-resume per-agent (each specialized agent checkpointed; resumable from any failure point)
- Claude Agent SDK as reasoning core with maxTurns=10_000 + bypassPermissions
- "POC or it didn't happen" / "No Exploit, No Report" principle — methodology philosophy, not architectural pattern

**New candidates registered at v45:** **ZERO** (consolidation-forward discipline; 9-consecutive-wiki zero-new-active-candidates streak extends v37-v45 — **NEW corpus-longest-streak-record**, extends v44's 8-streak).

**Un-stale check results:** All 5 stale candidates checked negative — #14 Alignment-Theory (shannon no alignment-theory framing) / #16 Skill Dependency Locking (no skill lockfile beyond pnpm-lock) / #21 SDD Methodology Emergence (shannon not SDD) / #23 AI-Disclosure Policy (no explicit policy) / #25 Personality-Driven Agent Design (agents domain-specialized not personality-driven). All 5 stay stale. Disciplined negative results.

**Tier status post-v45:**
- T5 extends to N=9 with NEW AI-pentester sub-archetype (100% archetype-diversity-per-wiki preserved at N=9)
- All 5 Storm Bear tiers multi-entrant validated (unchanged)
- T1: 13 / T2: 3 / T3: 3 / T4: 7 / **T5: 9 (9 distinct sub-archetypes)** / Outside-scope: 9 (8 sub-types)

**Post-v45 counts:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = **72 full / 57 active**. **Ratio 20:37 = 0.54:1 UNPRECEDENTED preserved unchanged from post-v44 — 9TH CONSECUTIVE WIKI at 0.54:1 (longest-stable-ratio streak in corpus at post-unprecedented-best level).** 0.41 buffer below 0.95:1 mini-audit trigger (unchanged).

**5th+ v2.1-era routine execution — all discipline mechanisms exercised cleanly:**
- Phase 0.5 expanded pattern pre-check: un-stale all 5 negative
- Phase 0.6 overlap pre-check: 10 candidate attempts all routed to within-existing-pattern strengthening (0 standalone registrations)
- Phase 0.9 Storm Bear meta-entity applicability: 34th consecutive (v10-v45)
- Phase 0.9 primitive-count flagging: YELLOW (~120-150 primitives; 4th YELLOW application after pi-mono v36 / bizos v37 / DeepTutor v38)
- Consolidation-forward discipline: 0 new active candidates target achieved (9-streak extends)
- N=1 stale-risk-flagging at registration: N/A (no registrations)
- Counter-evidence: Pattern #47 + #48 scope-respect discipline (neither strengthen nor invalidate; scope-locks respected)
- Fact-verification: Pattern #31 / #50 / #29 / #58 / #17 / #12 / #28 references verified against PATTERN_LIBRARY.md pre-merge

**30 corpus-firsts at v45:**
1. T5 9th entrant + AI-pentester sub-archetype (NEW)
2. T5 with white-box source-code-aware dynamic testing
3. T5 with Temporal.io workflow durability orchestration
4. T5 with 4 security-tool integrations (Nmap + Subfinder + WhatWeb + Schemathesis)
5. XBOW hint-free security-domain benchmark 96.15% (first pentesting-domain eval in corpus)
6. Dedicated Pro-tier documentation file SHANNON-PRO.md 26KB (most-detailed Pro-tier docs)
7. Tower managed vCISO service tier (first at T5)
8. SOC 2 Type I explicit at T5 commercial-startup
9. Static-dynamic correlation pipeline architectural pattern (Pro commercial observational)
10. Code Property Graph (CPG) at T5 (Pro commercial observational)
11. Self-hosted runner model (customer data plane + Keygraph control plane split)
12. sample-reports/ directory with real pentest reports (OWASP Juice Shop + c{api}tal + crAPI)
13. Per-invocation ephemeral Docker container + per-scan task queue
14. Workspaces + git-checkpoint-resume per-agent architecture
15. Claude Agent SDK maxTurns=10_000 + bypassPermissions
16. Autonomous 2FA/TOTP/SSO handling (TOTP via dedicated MCP server in Pro)
17. Pipelined parallel processing 10-agent architecture (5 vuln + 5 exploit concurrent)
18. "POC or it didn't happen" / "No Exploit, No Report" principle
19. Issues-only-no-PRs governance at 40K scale
20. 13 specialized agents × 5 attack domains × 2 phases taxonomy (Injection / XSS / SSRF / Auth / Authz × vuln-analysis + exploitation + shared)
21. AGPL-3.0 2nd project-scope data point reaching structural-N=2 (Skyvern + shannon)
22. Pattern #31 N=8 (8th Open-Core data point)
23. Pattern #50 N=7 (7th Commercial-Funnel-Companion data point)
24. Pattern #58 5th observation (feature-deprecation-with-public-discussion-notice sub-variant)
25. 9-consecutive-wiki zero-new-active-candidates streak (v37-v45 NEW LONGEST)
26. 34th consecutive Storm Bear meta-entity (v10-v45)
27. 27+ consecutive wikis at ~2h velocity plateau (v6-v45; 4th YELLOW application)
28. Security-testing domain commercial-startup organic steady-growth sub-path (~2.5K stars/month)
29. Business-logic invariant-discovery + fuzzer-generation + exploit-synthesis 4-phase pipeline (Pro commercial observational)
30. Keygraph 2-entrant corpus security-commercial archetype (Shannon Lite + Shannon Pro same company different product-tier)

**⚠️ v27 diagnostic HIGH bundle deferred 24 sessions** (v28/v29/v30/v31/v31-mini/v32/v32-mini/v33/v34/v34-action/v35/v36/v37/v38/v39/v40/v41/v42/v42-deferred/v43/v44/**v45**/next) — BLOCKING-RECOMMENDATION 4.8× threshold-exceeded. Pattern Library is NOT bottleneck at v45 (ratio 0.54:1 unprecedented preserved 9-streak); operator-facing vault work remains overwhelming next-highest-ROI action. Shannon's 2-tier Lite/Pro + SHANNON-PRO.md dedicated-docs + Tower managed service patterns add commercial-playbook observational context for Storm Bear potential commercialization (if ever relevant).

**Full v45 wiki:** `03 Projects/shannon - Beginner Analysis/` — see `(C) T5 9-way + Pattern 31 N=8 + 50 N=7 + AI-pentester.md` for full Phase 4b deliverable.

---

### v45 HARVEST MINI-AUDIT (2026-04-24, 3rd mini-audit within single session) — 4 FORMAL-STATEMENT REFINEMENTS (#17 variant 2 sub-distinction 2a/2b + #42 venue-diversity N=3 + #44 sub-variant 44d + #31 Pro-docs-depth 0-4 sub-signal)

**Trigger:** Operator-approved multi-wiki-harvest mini-audit consolidating accumulated refinements across v43 rowboat + v44 magika + v45 shannon (9-consecutive-wiki zero-registration streak). **3rd mini-audit within single session** (v42 mini-audit → v42-deferred mini-audit → v45 harvest mini-audit — NEW corpus-first).

**Pre-audit state:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = **0.54:1** (unprecedented; preserved 9 consecutive wikis).

**Post-audit state:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = **0.54:1 UNCHANGED** (all refinements; zero status transitions).

**⚠️ Verification discrepancy caught at audit entry:** v44 magika wiki claimed "Microsoft 3 (v6+v28+v34) + Google 2 = 5 data points" for Pattern #17 variant 2. **Fact-check:** v34 = `claude-code-best-practice` (Shayan Rais Pakistani solo T1), NOT Microsoft. The v44 deliverable itself flagged uncertainty with empty cells. **Corrected count:** Microsoft 2 (v6+v28) + Google 2 (v13+v44) = 4 data points across 2 big-tech orgs. Audit proceeded with sub-distinction 2a/2b formalization using corrected count.

**Actions (4 — all formal-statement refinements, zero status changes):**

1. **#17 Ecosystem-Layer Organizations variant 2 → REFINED with sub-distinction 2a corporate-official vs 2b corporate-research-OSS.** N=3 at 2a (gws v13 + markitdown v28 + ai-agents-for-beginners v6) + N=1 at 2b (magika v44). Variant 2 / variant 5 overlap acknowledged (not mutually exclusive; Microsoft v6+v28 appear at both on different axes). **First within-variant sub-type formalization in library.**
2. **#42 Academic-Published Peer-Reviewed Framework → REFINED with venue-diversity sub-taxonomy at N=3 across 3 CS-conference-classes.** ACL 2024 NLP (LlamaFactory v22) + ICLR 2025 ML (OpenHands v30) + ICSE 2025 SE (magika v44) all A*-ranked. **First dual-criterion-satisfaction pattern** (originally promoted v31 mini-audit under structural-N=2; now also satisfies default 3-observation criterion).
3. **#44 Academic-Lab Affiliation → REFINED with sub-variant 44d corporate-research-lab formalization.** Sub-variant enumeration extends from 3 (44a-c) to 4 (44a-d). Google Research Anti-Abuse team (magika v44) = N=1 observational; promotion-path at N=2. **Broadest sub-variant enumeration in library** (ties Pattern #17's 5 variants with 44a-d plus pattern-level = 5-layer).
4. **#31 Open-Core Commercial Entity → REFINED with Pro-docs-depth 0-4 sub-signal axis.** shannon v45 SHANNON-PRO.md 26KB = corpus-first depth-4 observation. N=8 data points tabulated: depth 1 (N=3) / depth 2 (N=4) / depth 3 (N=2) / depth 4 (N=1). **First sub-signal axis in pattern library** (ordinal 0-4 scale distinct from categorical sub-variants).

**Structural firsts at v45 harvest mini-audit:**

- **3rd mini-audit within single session** (prior max 2 back-to-back at v42 + v42-deferred)
- **First multi-wiki-harvest audit** (v43 + v44 + v45 consolidated)
- **First sub-signal axis in library** (#31 Pro-docs-depth ordinal 0-4)
- **First within-variant sub-type formalization** (#17 variant 2 → 2a/2b)
- **5th sub-variant enumeration in library** (#44 extends 44a-c → 44a-d; ties Pattern #17)
- **Most refinements per audit in corpus** (4; prior max 2)
- **First dual-criterion-satisfaction pattern** (#42 satisfies both structural-N=2 + default-3-observation)
- **First cross-pattern same-archetype correlation formalized** (44d ↔ 17-variant-2b same archetype from different axes)
- **First audit-layer fact-verification correcting wiki-layer error** (v44 Microsoft-3 claim → Microsoft-2+Google-2=4)

**Audit document:** `04 Reviews/(C) 2026-04-24 Pattern Library mini-audit post-v45 (v43+v44+v45 harvest).md`

**Next trigger:** candidate count ≥25 OR v50 wiki OR ratio >0.95:1 (mini) / >1.05:1 (full).

---

### v47 HARVEST MINI-AUDIT (2026-04-25, session 56 — 5TH MINI-AUDIT WITHIN SINGLE SESSION CHAIN, UNPRECEDENTED CORPUS-FIRST) — 3 FORMULATION EXTENSIONS (#22 sub-variant 22c + 3-layer governance hierarchy / #28 verification-not-routing 3rd sub-axis NEW / #18 runtime-primacy-choice 8th refinement)

**Trigger:** Operator-approved 3-action formulation-extension harvest from v47 marcusquinn/aidevops direct-update observations. Pre-approved scope: 3 formal-statement extensions on confirmed patterns (all strengthen existing CONFIRMED patterns with new sub-variants/sub-axes/sub-observations). **5th mini-audit within single session chain — UNPRECEDENTED corpus-first** (extends session 51+52+54+55 quartet to quintet within 24-hour cycle).

**Pre-audit state:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = **0.513:1** (FIRST sub-0.55:1 in corpus; preserved 11 wikis v37-v47 + 4 prior mini-audits = 11+4=15 cycles total, but ratio 0.513:1 specifically held since session 55 = 12th consecutive cycle counted forward from first sub-0.55:1 establishment).

**3 actions executed (all formal-statement extensions; zero status changes):**

1. **Pattern #22 AGENTS.md as Industry Standard → REFINED** with sub-variant 22c authoritative-with-shim + 3-layer governance hierarchy framing. Stays CONFIRMED. New sub-variant 22c at N=1 stale-risk-flagged (aidevops v47 corpus-first AGENTS.md-authoritative inversion: verbatim "All instructions, documentation, and operational guidance are maintained in AGENTS.md as the single source of truth" + Layer 0 shims [CLAUDE.md 440B + AGENT.md 420B] + Layer 1 root AGENTS.md 3KB + Layer 2 .agents/AGENTS.md 18KB).
2. **Pattern #28 Multi-Provider AI Support → REFINED** with verification-not-routing 3rd sub-axis (28-verification NEW) alongside existing routing/abstraction + native-multi-provider sub-axes. Stays CONFIRMED. New sub-axis 28-verification at N=1 stale-risk-flagged (aidevops v47 corpus-first cross-provider verification-as-safety mechanism for destructive operations; vendor-difference is NEW structural-requirement property in library).
3. **Pattern #18 Agent Runtime Standardization → REFINED** with runtime-primacy-choice sub-observation acknowledging 3-runtime-primacy diversity (Claude-Code-primary majority + OpenCode-primary aidevops v47 N=1 + Codex-primary observed via oh-my-codex sibling). Stays CONFIRMED. OpenCode-primary registered at N=1 within Pattern #18 stale-risk-flagged. Pattern #18 now has **8 refinements** (most-refined pattern in library).

**Post-audit state UNCHANGED on counts:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio **0.513:1 PRESERVED 12th consecutive cycle** (largest buffer 0.437 below 0.95:1 mini-audit trigger preserved).

**5 structural firsts:**

1. **5th mini-audit within single session chain — UNPRECEDENTED corpus-first.** Extends session 51 v42 mini-audit → session 52 v42-deferred → session 54 v45 harvest → session 55 v46 conditional retirement quartet to quintet. Demonstrates audit infrastructure mature enough for sustained rapid-cadence library maintenance.
2. **Pattern #28 first 3-axis taxonomy in library** — 2-axis (routing-abstraction + native) → 3-axis (+ verification-not-routing). Multi-axis classification rare in library.
3. **Pattern #22 first 3-layer governance hierarchy formalization** — prior 22a/22b sub-variants single-file size-based; 22c introduces multi-file authority-tier framing.
4. **Pattern #18 first runtime-primacy-choice sub-observation** — 3-runtime-primacy diversity acknowledged. 8th refinement; most-refined pattern in library.
5. **3 N=1 stale-risk-tracking entries registered simultaneously with synchronized v52/v57 review cadence** — 22c + 28-verification + OpenCode-primary all share +5/+10 review thresholds.

**Cross-pattern coupled-design observation registered (NEW v47 HARVEST):**

aidevops v47 simultaneously establishes Pattern #22 22c (AGENTS.md-authoritative + CLAUDE.md-shim) AND Pattern #18 OpenCode-primary runtime-primacy-choice. These choices appear coupled: multi-runtime targeting via runtime-agnostic AGENTS.md authority + de-emphasis of Claude-Code-specific CLAUDE.md align with OpenCode-primary recommendation. **Hypothesis (registered observationally; not yet pattern):** frameworks targeting multi-runtime ecosystems may converge on AGENTS.md-authoritative governance as runtime-agnostic single-source-of-truth. Monitor v48-v52 for whether 2nd AGENTS.md-authoritative wiki ALSO has non-default runtime-primacy.

**Audit document:** `04 Reviews/(C) 2026-04-25 Pattern Library mini-audit post-v47 (formulation extensions harvest).md`

**Next trigger:** candidate count ≥28 OR v52 wiki OR ratio >0.95:1 (mini) / >1.05:1 (full).

---

### Promoted at v50 mini-audit (#57)

#### ✅ #57 Recursive Corpus Reference (PROMOTED v50 mini-audit — 2nd default-criterion promotion in corpus history; FIRST sub-0.50:1 ratio achieved at this audit close)
**Status at v50 mini-audit:** PROMOTED to CONFIRMED via **default ≥3-observations-across-2+-tiers criterion**. 5 data points spanning 3 tiers (outside-scope + T1 + T5). 2 sub-variants formalized at promotion (57a direct citation N=4 / 57b aggregator-mediated multi-citation N=1 NEW v50). **2nd default-criterion promotion in corpus history** (1st was Pattern #50 N=3 default-criterion at v40); FIRST default-criterion promotion within v42-v50 mini-audit cluster (prior 6 mini-audits used structural-N=2 / refinement / retirement / extension never default-criterion).

**Status history:** Registered candidate v27 oh-my-claudecode (Yeachan Heo cites obra/superpowers v2 + everything-claude-code v1 in README "Inspired by"). Stale-check at v32 NEGATIVE (no 2nd citation observed). Multi-data-point accumulation v37-v50: v37 bizos / v44 magika / v46 ollama / v47 aidevops / v50 awesome-claude-skills = 5 data points. Total observation period: **23 wikis (v27 → v50)** — demonstrates default-criterion promotion path is reachable but typically requires sustained corpus-observation period (vs structural-N=2 promotions which often resolve within 5-10 wikis of registration).

**Evidence (5 data points; 3 tiers):**

| # | Citing wiki | Citing-tier | Cited corpus subject | Cited-tier | Mechanism (sub-variant) |
|---|-------------|-------------|----------------------|------------|--------------------------|
| 1 | v27 oh-my-claudecode | T1 | v1 ECC + v2 obra/superpowers (README "Inspired by") | T1 | 57a direct citation |
| 2 | v37 bizos | outside-scope | v25 awesome-design-md (CREDITS.md) | outside-scope | 57a direct citation |
| 3 | v44 magika | outside-scope | v22 LlamaFactory (paper citation chain) | outside-scope | 57a direct citation |
| 4 | v46 ollama | outside-scope | v36 pi-mono + v10 autoresearch (`docs/integrations/pi.mdx`) | T1 + T5 | 57a direct citation (compound 2-wiki) |
| 5 | v47 aidevops | T1 | v25 awesome-design-md + Google Stitch DESIGN.md (CREDITS.md) | outside-scope | 57a direct citation |
| 6 | **v50 awesome-claude-skills** | **outside-scope** | **v2 obra/superpowers (5×) + anthropics/skills (5×)** | **T1 + (general)** | **57b aggregator-mediated multi-citation NEW** |
| 7 | **v15 multica → v51 vercel-labs/agent-skills** | **T2 → T1** | **vercel-labs/agent-skills (cited as `"Vercel agent-skills import (first)"` in multica v15 wiki entry; v51 builds Vercel wiki later)** | **T1** | **57c forward-citation-then-wiki sub-variant NEW v51** |
| 8 | **v27 OMC → v52 oh-my-openagent** | **T1 → T1** | **oh-my-opencode (cited as 1 of 5 inspirational sources in OMC v27 wiki entry; v52 builds omo wiki later)** | **T1** | **57c forward-citation-then-wiki sub-variant N=2 STRUCTURAL v52** |
| 9 | **v52 omo → v2 obra/superpowers** | **T1 → T1** | **obra/superpowers (omo `docs/superpowers/` subdirectory cites/integrates Storm Bear v2 wiki subject directly)** | **T1** | **57a direct citation (5th data point)** |

**Tier-diversity verification:** Citing-wikis span 4 tiers (outside-scope + T1 + T2 + T1 v52 NEW). Cited-corpus-subjects span 3 tiers (outside-scope + T1 + T5). Citing↔cited pairs span 5+ distinct tier combinations explicit. **Default ≥3-observations-across-2+-tiers criterion met decisively (8 obs × 3 tiers); 57c sub-variant reaches structural-N=2 at v52.**

**Formal statement (post-v50 mini-audit promotion):**

> Pattern #57 Recursive Corpus Reference: New corpus subject explicitly cites prior Storm Bear corpus item(s) as intellectual influence, design pattern source, integration target, or aggregator entry — creating self-referential corpus lineage graph that transitions corpus from isolated observations to internally-connected bibliography. Meta-structural pattern — not about framework features but about corpus topology.
>
> **3 sub-variants observed (post-v51):**
>
> - **57a Direct citation** — Author of citing wiki directly references prior corpus subject in repo governance files (README "Inspired by" / CREDITS.md / docs integration / paper citation chain). Single-citation per author-intentional pair. Citation flow: forward in time relative to wiki-build sequence (citing wiki built AFTER cited subject's wiki). **N=4 corpus data points** (oh-my-claudecode v27 → ECC v1 + obra/superpowers v2; bizos v37 → awesome-design-md v25; magika v44 → LlamaFactory v22; ollama v46 → pi-mono v36 + autoresearch v10; aidevops v47 → awesome-design-md v25).
> - **57b Aggregator-mediated multi-citation** (NEW v50) — Aggregator curates lists where prior corpus subject appears alongside many entries; recursion emerges from selection topology rather than authorial citation intent. Author may be unaware of corpus membership. High-multiplicity citation (e.g., 5× per cited subject) indicates structural amplification at aggregator scale. **N=1 corpus data point** (awesome-claude-skills v50 → obra/superpowers v2 cited 5× + anthropics/skills cited 5×).
> - **57c Forward-citation-then-wiki NEW v51 STRENGTHENS to N=2 STRUCTURAL v52** — Subject B is cited in earlier wiki C as a dependency or reference; later wiki D builds B's wiki. Citation flow REVERSED in time relative to wiki-build sequence (cited subject's wiki built AFTER citation in earlier wiki). Mechanistically distinct from 57a (intra-wiki authorial intent forward-in-time) + 57b (aggregator-mediated). Functions as **external validity signal of corpus-selection discipline** — independent agent-ecosystem judgment retroactively validates Storm Bear's selection criteria. **N=2 corpus data points (structural)**: (1) multica v15 wiki entry cited "Vercel agent-skills import (first)" as dependency in skills-lock.json; Storm Bear vault later built v51 wiki of vercel-labs/agent-skills 36 wikis after multica v15. (2) **OMC v27 wiki entry cited "oh-my-opencode" as 1 of 5 inspirational sources alongside claude-hud + Superpowers v2 + everything-claude-code v1 + Ouroboros; Storm Bear vault later built v52 wiki of oh-my-opencode (renamed to oh-my-openagent) 25 wikis after OMC v27 (NEW v52)**. **Promotion-candidate at next mini-audit under structural-N=2 criterion.** Two distinct sub-cases: skills-lock.json formal dependency (v51) + narrative inspiration source list (v52); both validated. Mechanism survives long temporal gaps (36 wikis + 25 wikis).
>
> **Corpus base rate post-v52: 8/52 ≈ 15%** (up from 6/51 = 12% post-v51). Aggregator-genre wikis amplify Pattern #57 frequency via 57b; long-running corpus accumulates 57c via dependency-citation in earlier non-aggregator wikis.

**N=1 stale-risk-flag at registration:**
- 57b aggregator-mediated multi-citation — registered v50, +5-wiki check at v55, +10-wiki retirement review at v60. Promotion-ready at structural-N=2 if 2nd hybrid awesome-list-genre subject emerges.
- **57c forward-citation-then-wiki NEW v51 → STRUCTURAL N=2 ACHIEVED v52** — registered v51 (N=1 multica→vercel-labs); 2nd data point arrived v52 (OMC v27 → oh-my-openagent v52); **stale-risk-flag REMOVED via N=2 promotion-candidate at next mini-audit under structural-N=2 criterion**. Two distinct sub-cases preserved (skills-lock.json formal dependency + narrative inspiration source list).

**Significance (8 structural firsts at v50 mini-audit; #57 promotion contributes to firsts 1-4):**

- **First confirmed-promotion under default-criterion within v42-v50 mini-audit cluster** — prior 6 mini-audits (sessions 51 / 52 / 54 / 55 / 56) used structural-N=2 criterion or were retirements/extensions. Pattern #57 promotion validates default-3-cross-tier criterion is actively reachable after sustained candidate observation.
- **2nd default-criterion promotion in corpus history** — first was #50 N=3 default-criterion at v40 (claude-context). Pattern #57 is 2nd default-criterion promotion overall.
- **First aggregator-mediated mechanism formalized in library** — 57b sub-variant introduces "selection-topology recursion" as distinct from "authorial-intent recursion." May generalize to future patterns where aggregator amplification differs structurally from direct citation.
- **First sub-0.50:1 ratio in corpus history achieved** — promotion ratio resolution 18:38 = 0.474:1 shatters prior best 0.513:1 by 0.039 points.
- **Corpus-internal bibliography graph reaches density milestone** — at promotion, 5 confirmed corpus-internal recursive edges across 50 wikis = 10% base rate. Storm Bear corpus is now empirically self-connected at structural threshold (>5 edges) demonstrating Karpathy LLM Wiki "knowledge compounds" pattern with measurable graph density.
- **Pattern #57 is library's first 2-sub-variant taxonomy with mechanistically-distinct sub-variants** — 57a authorial-intent vs 57b selection-topology. Distinct mechanisms (not just categorical sub-types or ordinal sub-signals). Library-vocabulary item #12 NEW (mechanistically-distinct sub-variants).

**Cross-references:**

- **Pattern #19 Intellectual Lineage Archetypes (CONFIRMED v20):** strong correlate — Pattern #57 is the corpus-internal manifestation of Pattern #19's individual-author-lineage and methodology-lineage archetypes. When citing wiki references a prior corpus subject, lineage archetype is necessarily corpus-internal.
- **Pattern #68 Awesome-List-Genre (CONFIRMED v31, refined this audit):** orthogonal but co-occurring at v50 — awesome-list-genre wikis (Pattern #68 sub-type c) exhibit higher Pattern #57 frequency via 57b aggregator-mediated multi-citation. May be true generally for sub-type a + b as well; observable at future Pattern #68 wikis.
- **Pattern #17 Ecosystem-Layer Organizations (CONFIRMED v15):** Yeachan v27 + Marcus Quinn v47 + Composio v50 ecosystem-layer-individuals/orgs all exhibit Pattern #57 + Pattern #17 simultaneously; ecosystem-layer scale amplifies Pattern #57 occurrence.
- **Pattern #50 Commercial-Funnel Companion (CONFIRMED v31, refined this audit):** at v50 awesome-claude-skills, Pattern #57 + Pattern #50 + Pattern #68 hybrid sub-variant all co-occur — first 3-pattern-coupled-observation in corpus.

**Confidence:** High. 5 data points across 3 tiers + 2 mechanistically distinct sub-variants. N=4 minimum for default-criterion (3-cross-tier) decisively exceeded.

**Prediction:** N=8+ expected within v51-v60 if corpus continues at half-century-velocity pace. Aggregator-genre wikis (Pattern #68 universe) likely contribute disproportionately to 57b sub-variant accumulation. Watch list: any future awesome-list-genre wiki almost certainly exhibits 57b at multi-citation density.

---

### v50 MINI-AUDIT (2026-04-25, session 60 — 6TH MINI-AUDIT WITHIN v42-v50 CYCLE) — 1 PROMOTION (#57 default-criterion) + 3 FORMAL-STATEMENT EXTENSIONS (#68 hybrid sub-variant + #50 3-sub-variant taxonomy + #29 absent-LICENSE 3-sub-context taxonomy)

**Wiki source for 4 actions:** v50 awesome-claude-skills direct-update observations + carry-forward from v45-v49 mini-audit accumulations. 4 pre-approved actions: 1 promotion (Pattern #57 CANDIDATE → CONFIRMED via default ≥3-observations-across-2+-tiers criterion) + 3 formal-statement extensions on confirmed patterns (#68 hybrid sub-variant + #50 3-sub-variant taxonomy + #29 absent-LICENSE 3-sub-context taxonomy).

**Pre-audit state:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = **0.513:1** (held 14 consecutive wikis v37-v50 + 5 prior mini-audits; UNPRECEDENTED stability streak).

**Post-audit state:** **38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active**. Ratio 18:38 = **0.474:1 — FIRST SUB-0.50:1 RATIO IN CORPUS HISTORY** (shatters prior best 0.513:1 by 0.039 points). NEW LARGEST buffer below 0.95:1 mini-audit trigger: **0.476** (was 0.437 held 14 cycles).

**Net state transitions:** +1 confirmed (#57 promotion) / -1 candidate (#57 leaves candidate). 3 formal-statement extensions without status changes.

**Pattern #57 promotion details:** See "Promoted at v50 mini-audit (#57)" section above.

**Pattern #68 hybrid sub-variant formal-statement extension:** Audience sub-type c (AI-runtime-infrastructure-directory) reaches structural-N=2 (awesome-mcp-servers v31 + awesome-claude-skills v50). NEW orthogonal form-factor sub-variant axis introduced: pure-aggregator (N=3: build-your-own-x v8 + awesome-design-md v25 + awesome-mcp-servers v31) vs hybrid aggregator+bundled-skill-library (N=1 stale-flagged: awesome-claude-skills v50 — curates ~120 external skills + ships 864 SKILL.md in-repo + bundles `connect-apps-plugin/` commercial-product entry). **First 2-axis-orthogonal sub-variant taxonomy in Pattern #68** (audience axis × form-factor axis = 2D classification space). N=1 stale-risk-flag at registration: hybrid sub-variant — registered v50, +5 v55, +10 v60. See Pattern #68 confirmed entry for updated formal statement.

**Pattern #50 3-sub-variant taxonomy formal-statement extension:** N=9 multi-data-point accumulation v25-v50 formalized as 3-sub-variant taxonomy: **50a Standard commercial-tier funnel** (N=7 across all corpus #50 default observations) / **50b Recruiting-as-funnel-terminus NEW v49** (N=1 stale-flagged: MiroFish v49 mirofish@shanda.com pre-monetization positioning) / **50c Aggregator-with-commercial-product-entry-bundled-in-repo NEW v50** (N=1 stale-flagged: awesome-claude-skills v50 connect-apps-plugin bundled in OSS aggregator + 96.3% commercial-coupling). **First 3-sub-variant taxonomy in Pattern #50 with per-variant N-tracking.** N=1 stale-risk-flags: 50b — registered v49, +5 v54, +10 v59; 50c — registered v50, +5 v55, +10 v60. **Cross-pattern coupled-design observation** (2nd in corpus): #50 50c ↔ #68 hybrid sub-variant co-occur at v50 awesome-claude-skills (sub-variant 50c mechanically requires Pattern #68 hybrid form). See Pattern #50 confirmed entry for updated formal statement.

**Pattern #29 absent-LICENSE 3-sub-context taxonomy formal-statement extension:** Multi-data-point accumulation across v37 + v39 + v50 formalized as 3-sub-context taxonomy: **29-absent-1 Absent-LICENSE + README-proprietary-claim** (N=1: bizos v37 cold-start commercial-positioning) / **29-absent-2 Absent-LICENSE + no-license-claim** (N=1: dive-into-llms v39 academic-public-welfare) / **29-absent-3 Absent-LICENSE + README-OSI-license-claim + per-skill-license-variation NEW v50** (N=1 stale-flagged: awesome-claude-skills v50 aggregator-mixed-license; corpus-first 4-tier-license-presence-in-single-repo observation: root absent / README badge + section claim Apache-2.0 / per-skill LICENSE.txt in 9 of 31 top-level skills / YAML frontmatter `license:` field in skill-creator only). **First 3-sub-context taxonomy in Pattern #29 absent-LICENSE sub-category + first 4-tier-license-presence-in-single-repo observation in corpus.** N=1 stale-risk-flag at registration: 29-absent-3 — registered v50, +5 v55, +10 v60. **AGPL-3.0-at-project-scope sub-variant formalization promotion-candidate carry-forward** from v49 (N=3 default-criterion at T5 with Skyvern v24 + shannon v45 + MiroFish v49). See Pattern #29 confirmed entry for updated formal statement.

**8 structural firsts at v50 mini-audit:**

1. **FIRST sub-0.50:1 ratio in corpus history.** 18:38 = 0.474:1. Confirmed-pattern count exceeds 2× active-candidate count for first time in corpus. Library reaches structural-maturity threshold predicted at v36 mini-audit.
2. **FIRST default-criterion promotion within v42-v50 mini-audit cluster** — Pattern #57 promotion via default ≥3-observations-across-2+-tiers criterion.
3. **2nd default-criterion promotion in corpus history** (1st was #50 at v40).
4. **Pattern #57 first 2-sub-variant taxonomy with mechanistically-distinct sub-variants** — 57a authorial-intent vs 57b selection-topology. 12th library-vocabulary structural form NEW.
5. **Pattern #68 first 2-axis-orthogonal sub-variant taxonomy** — audience × form-factor axes.
6. **Pattern #50 first 3-sub-variant taxonomy with per-variant N-tracking**.
7. **Pattern #29 absent-LICENSE first 3-sub-context taxonomy + 4-tier-license-presence corpus-first observation**.
8. **6th mini-audit within v42-v50 cycle** — extends rapid-cadence library maintenance precedent.

**3 N=1 stale-risk entries registered with synchronized v55/v60 review cadence:** 57b aggregator-mediated multi-citation + 50c aggregator-with-commercial-product-entry-bundled-in-repo + 29-absent-3 aggregator-mixed-license. All registered v50, +5 v55, +10 v60.

**2nd cross-pattern coupled-design observation in corpus:** #50 50c ↔ #68 hybrid (1st was #22 22c ↔ #18 OpenCode-primary at session 56 v47 mini-audit). Library-vocabulary item #9 (cross-pattern coupled-design correlations) acquires 2nd data point.

**Audit document:** `04 Reviews/(C) 2026-04-25 Pattern Library mini-audit post-v50 (4 pre-approved actions).md`

**Promotion candidates carried forward to next mini-audit:** Pattern #29 AGPL-3.0-at-project-scope sub-variant formalization (carry-forward from v49) + Pattern #66 OT sub-categorization (carry-forward from v48) + Pattern #18 4-layer formal-statement-update with Layer 0 sub-types (carry-forward from v48) + Pattern #22 22c sub-variant scope-narrowing (carry-forward from v48) + Pattern #68 sub-type c structural-N=2 sub-pattern-formalization (NEW from this audit).

**Next trigger:** candidate count ≥28 (currently 18; 10-candidate runway) OR v55 wiki (5-wiki natural cadence from v50) OR ratio >0.95:1 (mini) / >1.05:1 (full).

⚠️ **v27 diagnostic HIGH bundle: 30 sessions deferred** (BLOCKING-RECOMMENDATION threshold exceeded 6×). Pattern Library health is decisively firmly-not-bottleneck at 0.474:1 with 0.476 buffer (NEW largest in corpus history); operator-facing vault work is overwhelmingly next-highest-ROI action.

---

### v49 MiroFish direct updates (2026-04-25) — 9 STRENGTHENING DATA POINTS + ZERO NEW CANDIDATES + ZERO OTs (13-consecutive-wiki streak v37-v49 NEW LONGEST)

**Wiki:** `666ghj/MiroFish` — multi-agent prediction-simulation engine; T5 Agent-as-application 10th entrant + multi-agent-prediction-simulation sub-archetype T5j NEW (100% T5 archetype-diversity-per-wiki preserved at N=10).

**State:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio **19:37 = 0.513:1 PRESERVED 13TH CONSECUTIVE WIKI** (largest buffer 0.437 below 0.95:1 mini-audit trigger preserved).

**9 patterns strengthened (no status transitions; consolidation-forward 13-streak preserved):**

1. **Pattern #29 License-Category Diversity 4th project-scope AGPL-3.0 data point** — Skyvern v24 + shannon v45 + MiroFish v49 = N=3 default-criterion at T5 (Unsloth Studio v23 component-scope distinct). Sub-variant formalization candidate at next mini-audit: **AGPL-3.0-at-project-scope-at-T5** with 100% commercial-or-commercial-adjacent positioning correlation (forces fork-disclosure as commercial moat protection).

2. **Pattern #19 archetype 2 CAMEL-AI / OASIS CORPUS-FIRST research-organization-cluster citation** — README explicit: *"MiroFish's simulation engine is powered by OASIS, We sincerely thank the CAMEL-AI team for their open-source contributions!"* Backend deps `camel-oasis==0.2.5` + `camel-ai==0.2.78` pinned. **Consolidation-forward decision: NOT registered as 5th archetype-2 node at N=1** (per N=1 stale-risk-flagging at registration since v32). Stale-flag: re-evaluate at v54 (5-wiki window). If 2nd corpus wiki cites CAMEL-AI / OASIS or similar research-org-cluster lineage, formalize Pattern #19 archetype-2 sub-classification: 2a individual-influence-nodes (Karpathy + Lam + Lance Martin) vs 2b research-organization-cluster nodes (Anthropic-team-cluster joins this; CAMEL-AI candidate).

3. **Pattern #44 academic-individual-with-commercial-incubation observation N=1** — BaiFu loose-BUPT-affiliation + Shanda Group strategic incubation + solo-author = candidate 5th sub-variant 44e (distinct from 44a-d institutional / multi-institutional / corporate-research-lab). **Consolidation-forward: NOT registered at N=1**; stale-flagged for v54.

4. **Pattern #31 Open-Core Commercial Entity 10th data point + pre-monetization sub-variant observation CORPUS-FIRST** — Shanda Group capital-backed + recruiting-pipeline-as-funnel + mirofish.ai brand + NO observable Pro tier + NO closed-beta + NO paid SaaS endpoint = pre-monetization positioning. Distinct from prior 9 #31 data points which all had observable Pro/paid tier. Sub-variant formalization candidate at next mini-audit (need N=2+ for promotion; observable in some prior wikis — re-scan candidate).

5. **Pattern #50 Commercial-Funnel Companion Platform 9th data point + recruiting-as-funnel-terminus sub-variant CORPUS-FIRST** — 5-channel multi-region community Discord + X + Instagram (Western) + QQ Group + Bilibili (CN-native) = corpus-strongest CN+Western dual-region community at T5. Funnel terminates in `mirofish@shanda.com` recruiting email NOT paid-tier-signup. **Recruiting-pipeline as commercial funnel terminus is corpus-first.** Formal-statement extension candidate at next mini-audit: funnel-terminus diversity sub-axis (paid-tier / cloud-managed / sponsorship / **recruiting-pipeline NEW**).

6. **Pattern #28 Multi-Provider AI Support 13th+ data point + 2-tier LLM routing observation** — internal-env-switch sub-variant (per v40 formalization). 2-tier routing via `LLM_*` primary + `LLM_BOOST_*` accelerator config (corpus-first explicit env-based 2-tier routing visible in `.env.example`). OpenAI SDK format vendor-agnostic with Qwen-via-Bailian default per README.

7. **Pattern #18 MCP-exclusion 4th T5-scope data point** — MiroFish at 57K T5 has NO MCP integration + NO Claude Code integration. Joins pi-mono v36 T1 + DeepTutor v38 T5 + ollama v46 outside-scope as 4th MCP-exclusion observation. Standalone-application-domain-focused MCP-rejection sub-variant. MCP-exclusion now N=4 across 3 tiers (T1 + T5 + outside-scope); pattern formulation extension candidate if a 5th data point arrives.

8. **Pattern #22 AGENTS.md T5-application abstention 3rd data point** — rowboat v43 + shannon v45 + MiroFish v49 = 3 T5 wikis with NO AGENTS.md. T5-application abstention sub-pattern strengthened; consistent with T5 standalone-app archetype where AGENTS.md primarily benefits multi-runtime contributor onboarding (less relevant for self-contained applications).

9. **Pattern #12 Governance-Depth refined v42 3-factor formulation 6TH counter-evidence wiki — HOLDS strongly** — MiroFish solo + commercial-incubation + 5-month + 57K stars + light-minimal governance (only LICENSE + 2 READMEs + Docker + .env.example + package.json — 7 governance primitives; NO AGENTS / CONTRIBUTING / SECURITY / CHANGELOG / CODE_OF_CONDUCT / SUPPORT). Fits refined formulation: maintainer-philosophy (solo product-iteration) + maturity-ambition (pre-monetization-product-velocity) + scale-tier (medium-large but pre-1.0) → light governance. v42 refined formulation now **6-counter-evidence-wiki-validated** (claude-hud v35 + pi-mono v36 + ruflo v42 + aidevops v47 + gh-aw v48 + MiroFish v49).

**Additional observations (not standalone strengthening but worth tracking):**

- **Pattern #2 Distribution Evolution Vue 3 + D3 at T5 corpus-first observation** — frontend-stack diversity; prior T5 dominated by React/Next.js; CN-ecosystem context (Vue dominant in Alibaba/Tencent/ByteDance)
- **Pattern #27 Community-Viral 22nd+ observation** — ~11.5K stars/month sustained-community-viral CN-author-amplified for 5 months; sustained ≠ extreme-burst — negative un-stale on **#52 Extreme-Viral-Velocity** (stays stale)
- **CN-author cross-tier presence** — 4-wiki CN-cluster across tiers (TrendRadar v19 T4 + DeepTutor v38 T5 + dive-into-llms v39 T3 + MiroFish v49 T5); not registered as Pattern #73-style regional meta-pattern (consolidation-forward); documented observation
- **Personal-account-vs-commercial-brand divergence sub-observation** — `666ghj/MiroFish` repo (personal) + `mirofish.ai` (brand) + `mirofish@shanda.com` (legal-employer); distinct from Pattern #58 branding-vs-package-name divergence; not registered (N=1)

**Phase 0.5 overlap pre-check execution:** 14 candidate observations evaluated; 14 of 14 routed to within-pattern strengthening per consolidation-forward discipline. **Zero standalone candidate registrations.**

**Stale-candidate negative un-stale checks:** #45 + #46 + #52 + #71 + #72 — all negative.

**Promotion candidates accumulated for next mini-audit (cumulative across v45-v49):**
- Pattern #29 AGPL-3.0-at-project-scope-at-T5 sub-variant formalization (NEW from v49 — N=3 default-criterion)
- Pattern #50 recruiting-as-funnel-terminus sub-axis formal-statement extension (NEW from v49)
- Pattern #66 OT sub-categorization (event-based vs by-design) — pending from v48
- Pattern #18 4-layer formal-statement-update with Layer 0 sub-types (a vertical-aggregation ollama + b horizontal-aggregation gh-aw) — pending from v48
- Pattern #22 22c sub-variant scope-narrowing (solo-multi-runtime-platform-specific) — pending from v48

⚠️ **v27 diagnostic HIGH bundle backlog ESCALATED to 29 SESSIONS DEFERRED** (BLOCKING-RECOMMENDATION threshold exceeded 5.8×). MiroFish v49 does NOT add new vault-refactor templates (no AGENTS.md / no governance docs); existing 3-template-ensemble (spec-kit v17 + aidevops v47 + gh-aw v48) sufficient. **STRONGLY RECOMMENDED execute v27 HIGH bundle before v50.**

**38th consecutive Storm Bear meta-entity (v10-v49)** with explicit "domain-distant peer + Pattern #12 baseline reinforcement" framing. Per-wiki applicability check applied; 3 indirect lessons identified (Pattern #12 v42 reinforcement + Pattern #29 AGPL license-decision landscape + i18n architecture aspirational-vs-actual lesson). Streak preserved without artificial-streak-inflation.

---

### v50 awesome-claude-skills direct updates (2026-04-25, session 59) — CORPUS HALF-CENTURY MILESTONE — 11 STRENGTHENING DATA POINTS + ZERO NEW CANDIDATES + ZERO OTs (14-CONSECUTIVE-WIKI ZERO-REGISTRATION STREAK NEW LONGEST extends v49 13-streak)

**Wiki:** `ComposioHQ/awesome-claude-skills` — Claude Skills hybrid aggregator + bundled in-repo skill-library + commercial-product-entry shipping inside OSS aggregator. **OUTSIDE-SCOPE — Pattern #68 awesome-list-genre meta-pattern 4TH DATA POINT** with audience sub-type c (AI-runtime-infrastructure-directory) reaching N=2 (joins awesome-mcp-servers v31). **CORPUS HALF-CENTURY MILESTONE.**

**State:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio **19:37 = 0.513:1 PRESERVED 14TH CONSECUTIVE WIKI** (largest buffer 0.437 below 0.95:1 mini-audit trigger preserved 14 cycles — UNPRECEDENTED stability streak).

**11 strengthenings (consolidation-forward; zero registrations):**

1. **Pattern #68 Awesome-list-genre meta-pattern 4th data point** — sub-type c (AI-runtime-infrastructure-directory) reaches N=2 (awesome-mcp-servers v31 + awesome-claude-skills v50). Sub-type c structurally-unambiguous within Pattern #68 — sub-type-formalization candidate at next mini-audit (wait for sub-types a or b to also reach N=2). NEW HYBRID SUB-VARIANT (corpus-first observational at N=1): aggregator-with-bundled-in-repo-skills + commercial-product-entry-as-bundled-skill. Prior 3 Pattern #68 entries (build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31) were pure-aggregator pointing to external repos; v50 ships 864 SKILL.md in-repo simultaneously with curating ~120 external skills. Do NOT register hybrid as standalone (consolidation-forward).

2. **Pattern #50 Commercial-Funnel Companion N=9 — CORPUS-STRONGEST observation** — 5 commercial surfaces (platform.composio.dev / dashboard.composio.dev / composio.dev/toolkits / rube.app/mcp / agentskb.com sister) + 3 distinct UTM-tracked campaigns in single README + cross-channel attribution discipline (`utm_medium=Youtube` on GitHub README banner) + **96.3% of in-repo skills (832 of 864) require commercial Rube MCP product to function**. 3 corpus-first sub-variant observations: (a) commercial-product-as-fulfillment-layer-for-aggregated-skills; (b) commercial-product-entry-as-bundled-skill (`connect-apps-plugin/` ships INSIDE OSS aggregator); (c) aggregator-as-marketing-attribution-channel (UTM-tracked GitHub→dashboard funnel). Formal-statement extension candidate at next mini-audit.

3. **Pattern #57 Recursive Corpus Reference 5th data point** — corpus-first **aggregator-mediated multi-citation** sub-variant. README cites `obra/superpowers` (Storm Bear v2 wiki subject) **5×** in single document (test-driven-development / brainstorming / root-cause-tracing / finishing-a-development-branch / using-git-worktrees) + `anthropics/skills` (referenced in v40 claude-context + others) **5×** (docx / pdf / pptx / xlsx / web-artifacts-builder). 10 Pattern-#57-relevant citations in single README across 2 corpus-resonant external repos. Base rate update: 5/50 = 10% (up from 4/49 ≈ 8%; aggregators amplify Pattern #57 frequency). **Promotion-candidate at next mini-audit** under default ≥3-observations-across-2+-tiers criterion (currently 5 observations × 4 tiers represented: outside-scope + T1 + T4 + T5).

4. **Pattern #29 License-Category Diversity 4th absent-LICENSE sub-context** — "absent-LICENSE-at-root-with-README-Apache-2.0-claim" CORPUS-FIRST. README badge + `## License` section claim Apache-2.0; NO LICENSE file at root (verified via `/bin/ls`). Corpus-first 4-tier-license-presence-in-single-repo observation: (1) root LICENSE: ABSENT; (2) README claim: Apache-2.0; (3) per-skill LICENSE.txt: present in 9 of 31 top-level skills (Anthropic-imported); (4) YAML frontmatter `license:` field: present in skill-creator only. 4 absent-LICENSE sub-contexts now observed across corpus (commercial-cold-start bizos v37 / academic-public-welfare dive-into-llms v39 / TBD-3rd / absent-LICENSE-with-README-claim v50). Sub-variant formalization candidate at next mini-audit.

5. **Pattern #59 Plugin Marketplace Native — corpus-first directory-scoped marketplace.json** — `composio-skills/.claude-plugin/marketplace.json` (v2.0.0; schema-referenced) inside aggregator subdirectory. Distinct from prior #59 sub-variants (59a marketplace+npm OMC v27 / 59b marketplace-only claude-hud v35). NEW SUB-VARIANT: marketplace-as-aggregator-subdirectory. Plus `connect-apps-plugin/.claude-plugin/plugin.json` separate manifest within same repo. Two manifest forms in single repo at 56K stars.

6. **Pattern #22 AGENTS.md aggregator-genre absence pattern** — 4/4 awesome-list-genre wikis lack AGENTS.md / CLAUDE.md at root (build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31 / awesome-claude-skills v50). Awesome-list-genre exhibits structural absences distinct from in-product wikis. Genre-specific absence pattern preserved at N=4.

7. **Pattern #18 MCP Standardization corpus-first explicit MCP-requirement field in skill YAML at scale** — 832 of 864 SKILL.md files declare `requires: mcp: [rube]` in YAML frontmatter. Layer-1 MCP-universal-adoption reinforced at aggregator scale. Corpus-first observation of structured MCP-dependency declaration in skill metadata.

8. **Pattern #19 archetype 4 no-individual-lineage** — Composio cites no individual-author lineage (corporate-startup positioning); only org-level branding + 3 contact emails. Strengthens at corporate-org level. Awesome-list-genre + corporate-startup combined absence of individual lineage (4/4 awesome-list-genre wikis exhibit this).

9. **Pattern #27 Community-Viral Scale Path ~22nd observation** — aggregator-amplified-commercial-viral sustained sub-path: 56,200 stars / ~6 months ≈ 9.4K stars/month. Distinct from extreme-viral-burst (#52 stays stale). Aggregator-genre + commercial-startup amplifies organic-community traction.

10. **Pattern #17 Ecosystem-Layer Organizations variant 3 commercial-startup ~19th data point — STRONGEST single-org evidence at v50** — Composio Inc. with 70 public repos + 5 commercial surfaces + 3-year operational history (created 2023-03-21) + sister product AgentsKB. Strongest variant-3 single-org evidence observed in corpus through v50.

11. **Pattern #2 Distribution Evolution** — 4 distribution surfaces documented: clone+copy to `~/.config/claude-code/skills/` / Claude.ai marketplace UI / `claude --plugin-dir ./connect-apps-plugin` local-dir-plugin install / Skills API programmatic via `skills=["skill-id"]`.

**Other observations (not registered)**:
- **EXTREME primitive-count tier 5th in corpus** (864 SKILL.md / 905 dirs / 832-entry composio-skills wrapper catalog). Sub-tier observation: skill-catalog-density (homogeneous SKILL.md primitive at scale; vs heterogeneous EXTREME at ruflo v42 / aidevops v47). Routine v2.2 candidate input: EXTREME tier sub-stratification proposal.
- **Probe-vs-clone gap**: initial probe estimated ~30 in-repo + ~30 external; clone revealed 864 SKILL.md / 832 wrappers. 28× gap. Routine v2.2 candidate input: aggregator-genre clone-first-count-second protocol.

**Promotion candidates accumulated for next mini-audit (cumulative across v45-v50):**
- Pattern #57 Recursive Corpus Reference promotion to CONFIRMED (NEW from v50 — 5 data points across 4 tiers; meets default ≥3-observations criterion)
- Pattern #50 formal-statement extension to acknowledge multi-surface + UTM-tracking + commercial-product-as-fulfillment-layer + commercial-product-entry-as-bundled-skill sub-variants (NEW from v50)
- Pattern #29 absent-LICENSE-with-README-claim sub-variant formalization (NEW from v50; 4 sub-contexts now observed)
- Pattern #29 AGPL-3.0-at-project-scope-at-T5 sub-variant formalization (carry-forward from v49)
- Pattern #50 recruiting-as-funnel-terminus sub-axis formal-statement extension (carry-forward from v49)
- Pattern #66 OT sub-categorization (carry-forward from v48)
- Pattern #18 4-layer formal-statement-update with Layer 0 sub-types (carry-forward from v48)
- Pattern #22 22c sub-variant scope-narrowing (carry-forward from v48)

**Storm Bear meta-entity 39th consecutive (v10-v50)** with "Claude-Skills aggregator as Storm Bear skill-shopping list + Pattern #57 corpus-touches-its-own-member observation + 50-wiki milestone reflection" framing. Per-wiki applicability check passed on 4/4 criteria. 5-skill clone-and-copy pilot table actionable in 30-60 min for vault automation (file-organizer / content-research-writer / meeting-insights-analyzer / changelog-generator / skill-creator).

**T-tier impact**: Outside-scope extends to 13 entries (build-your-own-x v8 / fish-speech v20 / system-prompts-leaks v21 / LlamaFactory v22 / Unsloth v23 / awesome-design-md v25 / awesome-mcp-servers v31 / bizos v37 / magika v44 / ollama v46 / awesome-claude-skills v50 / MiroFish v49 / ECC v1 — verify count). T1=14 / T2=3 / T3=3 / T4=8 / T5=9 / outside-scope=13.

**Velocity:** ~3h within EXTREME tolerance (v47 aidevops baseline ~3h-3h 30min). 28+ consecutive wikis at velocity plateau (v6-v50). 8th v2.1-era execution.

**v27 diagnostic HIGH bundle**: ESCALATED to **30 SESSIONS DEFERRED** (BLOCKING-RECOMMENDATION threshold exceeded 6×). v50 awesome-claude-skills provides **2 concrete reference assets**: (a) 864-SKILL.md catalog architecture (item #1 vault CLAUDE.md refactor — scale reference); (b) `composio-skills/.claude-plugin/marketplace.json` template (item #2 Storm Bear publishing strategy — concrete starter template). **STRONGLY RECOMMENDED execute v27 HIGH bundle before v51.** 50-wiki corpus half-century milestone is natural cadence-break.

**Corpus half-century milestone summary at v50:**
- 50 wikis in 8 days (v1 ECC 2026-04-17 → v50 awesome-claude-skills 2026-04-25)
- ~6.25 wikis/day average velocity
- 73 patterns total (37 confirmed + 19 active + 3 stale + 9 retired + 5 OT)
- Pattern Library ratio 0.513:1 preserved 14 cycles — UNPRECEDENTED stability
- 14-consecutive-wiki zero-new-active-candidates streak (v37-v50; new corpus record)
- 39 consecutive Storm Bear meta-entities (v10-v50)
- 28+ consecutive wikis at ~2h velocity plateau (v6-v50)
- All 5 tiers + outside-scope multi-validated
- 5 explicit Pattern #57 recursive corpus references (10% base rate)

---

### v46 CONDITIONAL-RETIREMENT MINI-AUDIT (2026-04-25, session 55 — 4TH mini-audit within single session chain) — 1 RETIREMENT-VIA-PRE-REGISTERED-TRIGGER + OBSERVATION-TRACK REPLACEMENT (#47)

**Trigger:** Pattern #47's pre-registered conditional retirement trigger fires at v46 per session 52 v42-deferred mini-audit registration. Trigger condition (verbatim from registration): *"If no 2nd vision-primary data point by v46, retire Pattern #47 + replace with OBSERVATION-TRACK 'Browser-Agent Architectural-Approach 3-point spectrum'."* Trigger window v42-v46 scope-reviewed: zero vision-primary data points arrived (ruflo v42 / rowboat v43 / magika v44 / shannon v45 DOM-based per scope-respect / ollama v46 non-browser). Trigger fires deterministically.

**Pre-audit state:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = 0.54:1.
**Post-audit state:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = **0.513:1 (FIRST SUB-0.55:1 in corpus history).**

**Single action executed:**

- **Pattern #47 Vision-Based Browser Automation → RETIRED** via pre-registered conditional retirement trigger firing per session 52 specification. Pattern retired at final N=1 (Skyvern v24 sole vision-primary data point). Replaced with **NEW OBSERVATION-TRACK "Browser-Agent Architectural-Approach 3-point spectrum"** preserving 3-point architectural-diversity vocabulary at N=1-per-point (vision-primary Skyvern + hybrid browser-use + DOM-only crawl4ai).

**7 structural firsts:**

1. **FIRST pre-registered conditional retirement trigger to FIRE in corpus history** — v2.1 mechanism empirically validated at +4 wikis past session 52 registration
2. **5th retirement in corpus** (9 total; 4th retirement-mechanism type)
3. **4th retirement mechanism type introduced** — conditional-retirement-via-preregistered-trigger
4. **FIRST retirement-to-OBSERVATION-TRACK pathway** — preserves architectural-diversity vocabulary while releasing candidate-tracking obligation
5. **FIRST SUB-0.55:1 RATIO** in corpus (19:37 = 0.513:1)
6. **4th mini-audit within single session chain** (session 51+52+54+55 quartet at time)
7. **Single-action mini-audit** — smallest audit scope in corpus

**Audit document:** `04 Reviews/(C) 2026-04-25 Pattern Library mini-audit post-v46 (Pattern 47 conditional retirement).md`

---

### Promoted at v53 mini-audit (#38 + Pattern #57 57c + Pattern #18 OpenCode-primary)

#### ✅ #38 Prompt-Leak-Archive Genre / AI-tool-disclosure-archive (PROMOTED v53 mini-audit — NEW 6th structural-promotion criterion: sister-archive-structural-N=2; first sister-archive structural pair in corpus)

**Status at v53 mini-audit:** PROMOTED to CONFIRMED via NEW 6th structural-promotion criterion **sister-archive-structural-N=2**. Two CANDIDATE-status archives (38a + 38b) sharing 5+ structural features AND differing on 6 mechanism-distinct sub-variant axes promote jointly. **First sister-archive structural pair in corpus.** Prior 5 structural-promotion criteria extended to 6.

**Status history:** Registered candidate v21 system-prompts-leaks (38a multi-tool-prompt-archive at N=1); sustained as candidate through v22-v52 without 2nd structurally-coherent archive. **STRUCTURAL N=2 reached at v53 learn-coding-agent (38b single-tool-internals-deep-dive).** Total observation period: **32 wikis (v21 → v53)** — comparable to Pattern #57 23-wiki observation period for default-criterion promotion at v50.

**Evidence at N=2 STRUCTURAL with 2 mechanism-distinct sub-variants:**

| # | Wiki | Sub-variant | Subject scope | Author | Monetization | Extraction method | Geographic origin |
|---|------|-------------|---------------|--------|---------------|--------------------|--------------------|
| 38a | system-prompts-leaks v21 (`x1xhlol/system-prompts-and-models-of-ai-tools`) | **multi-tool-prompt-archive** | 31 AI tools (broad) | Pseudonymous (x1xhlol / lucknitelol / NotLucknite multi-handle) | 6-channel commercial-funded (Patreon + Ko-fi + BTC + LTC + ETH + SOL token + ZeroLeaks commercial derivative) | Opaque | Global pseudonymous |
| 38b | learn-coding-agent v53 (`sanbuphy/learn-coding-agent`) NEW | **single-tool-internals-deep-dive** | Claude Code v2.1.88 only (narrow; 1 tool) | Named-low-identity (Sanbu, CN) | Zero monetization | Documented "publicly available online references and discussions" | CN |

**5-dimension shared structural features (sister-archive criteria):**

1. **Content type:** Extracts of closed-source commercial AI tool internals (NOT originals)
2. **Source type:** Closed-source commercial AI tools (proprietary)
3. **Legal position:** Gray zone (default-copyright + non-commercial-restriction OR DMCA-style takedown clause)
4. **Author archetype:** Low-accountability (pseudonymous OR named-low-identity)
5. **Extraction method:** Community-amalgam (broad sourcing without per-source attribution)

**6 sub-variant divergence axes (mechanism-distinct):**

Subject scope (broad vs narrow) / content type (input-side prompts vs operational+roadmap internals) / author identity (pseudonymous-multi-handle vs named-low-identity-public) / monetization (multi-channel commercial-funded vs zero) / extraction method (opaque vs documented public-sources) / geographic origin (global pseudonymous vs CN).

**NEW 6th structural-promotion criterion: sister-archive-structural-N=2**

Prior 5 structural-promotion criteria in library:
1. Default ≥3-observations-across-2+-tiers (e.g., #50 at v40, #57 at v50)
2. Structural-N=2 (e.g., #57 at v50; #58 at v42; #46 + #48 at v42-deferred)
3. Spectrum-pattern-at-N=2 (e.g., #51 at v29)
4. Variant-within-pattern-at-N=2 (e.g., #17 variant 5 at v29)
5. Meta-pattern-at-N=3-consolidation (e.g., #68 at v31; #73 at v36)

**6th criterion introduced at v53 mini-audit:**

6. **Sister-archive-structural-N=2** — Two CANDIDATE-status archives that share 5+ structural features AND differ on 5+ mechanism-distinct sub-variant axes. Sister-archive promotion requires: (a) BOTH N=1 archives independently registered as candidates; (b) shared core mechanism (extracts of closed-source / gray legal / low-accountability author); (c) mechanism-distinct sub-variants (subject scope / content type / author identity / monetization / extraction method); (d) sub-variant divergences are NOT pattern-invalidating (they extend formulation breadth, don't fragment it). Distinct from generic structural-N=2 because BOTH archives must already be N=1 candidates (vs structural-N=2 typically promotes N=2 of new pattern at first observation).

**Formal statement (post-v53 mini-audit promotion; broadened from "prompt-leak-archive" to "AI-tool-disclosure-archive genre"):**

> Pattern #38 AI-tool-disclosure-archive genre (formerly "prompt-leak-archive"): Repositories aggregating extracts of closed-source commercial AI tool internals. **Two CONFIRMED sub-variants identified (post-v53 mini-audit promotion):**
>
> - **38a multi-tool-prompt-archive** — broad subject scope (multiple AI tools); system prompts as primary content; pseudonymous author; commercial-derivative-funded monetization; opaque extraction. N=1: system-prompts-leaks v21 (x1xhlol; 31 AI tools).
> - **38b single-tool-internals-deep-dive NEW v53** — narrow subject scope (single AI tool); architecture/telemetry/codenames/killswitches/roadmap as primary content; named-low-identity author; zero-monetization; documented community-amalgam extraction. N=1: learn-coding-agent v53 (Sanbu; Claude Code v2.1.88 internals).
>
> **5 shared structural features (sister-archive promotion criteria):** (a) content = extracts not originals; (b) sources = closed-source commercial AI tools; (c) legal position = gray zone; (d) low-accountability author archetype; (e) extraction methods typically community-amalgam.
>
> **6 sub-variant divergence axes:** subject scope / content type / author identity / monetization / extraction method / geographic origin.

**Significance (4 structural firsts at this promotion):**

- NEW 6th structural-promotion criterion in library: sister-archive-structural-N=2
- Pattern #38 first CANDIDATE → CONFIRMED promotion under sister-archive-structural-N=2 criterion
- First sister-archive structural pair in corpus (38a + 38b)
- First genre-name broadening at promotion (extends from "Prompt-Leak-Archive Genre" to "AI-tool-disclosure-archive genre" to accommodate sub-variant 38b's broader content scope)

**Cross-references:**

- **Pattern #29 sub-context 29-absent-4 NEW v53 (REFINED at v53 mini-audit):** Pattern #38 38b co-occurs with Pattern #29 29-absent-4 at v53 learn-coding-agent (both NEW at v53; coupled-design observation candidate).
- **Pattern #19 archetype 4 no-explicit-individual-lineage:** Both 38a + 38b exhibit Pattern #19 archetype 4. Sister-archive genre may correlate with archetype 4 lineage (community-amalgam extraction → no individual lineage citation).
- **Pattern #36 Pseudonymous Researcher Archetype (candidate v21):** 38a co-occurs with #36; 38b does NOT. #36 may scope-narrow to 38a sub-variant.
- **Pattern #37 Crypto-Donation-Funded Scale Path (candidate v21):** 38a co-occurs with #37; 38b does NOT. #37 may scope-narrow to 38a sub-variant.
- **Pattern #40 Derivative-Security-Service Perverse-Incentive (candidate v21):** 38a co-occurs with #40; 38b does NOT. #40 may scope-narrow to 38a sub-variant.

**Confidence:** High. N=2 structural with 5+ shared features AND 6 mechanism-distinct sub-variant axes. Both archives independently registered (v21 + v53 = 32-wiki gap; no cross-contamination). Sister-archive criterion is conservative.

**Prediction:** N=3+ plausible within v54-v65 as more closed-source AI tool internals are reverse-engineered. Candidate observations: leaked training data archives / leaked benchmark archives / leaked deployment configs / leaked agent prompt-engineering techniques.

#### ✅ Pattern #57 sub-variant 57c forward-citation-then-wiki — STRUCTURAL-N=2 PROMOTION (within already-CONFIRMED Pattern #57)

**Status at v53 mini-audit:** STRUCTURAL-N=2 PROMOTION to CONFIRMED sub-variant within already-CONFIRMED Pattern #57. **First sub-variant promotion within already-confirmed pattern in corpus history.** Pattern #57 was promoted to CONFIRMED at v50 mini-audit via default ≥3-observations-across-2+-tiers criterion; this audit promotes the 57c sub-variant within. 57c becomes 3rd CONFIRMED sub-variant within Pattern #57 (joins 57a Direct citation N=5 + 57b Aggregator-mediated multi-citation N=1).

**Status history of 57c:** Registered as sub-variant candidate v51 (multica v15 → vercel-labs v51 N=1; 36-wiki gap; skills-lock.json formal dependency); STRUCTURAL N=2 reached at v52 (OMC v27 → oh-my-openagent v52; 25-wiki gap; narrative inspiration source list).

**Evidence (N=2 structural):**

| # | Earlier-citation wiki | Cited subject | Later-built wiki | Temporal gap | Mechanism |
|---|-----------------------|---------------|------------------|---------------|-----------|
| 57c-1 | multica v15 (T2) wiki entry | "Vercel agent-skills import (first)" cited as dependency in skills-lock.json | vercel-labs/agent-skills v51 (T1) | **36 wikis** | skills-lock.json formal dependency citation |
| 57c-2 | OMC v27 (T1) wiki entry | "oh-my-opencode" cited as 1 of 5 inspirational sources | oh-my-openagent (omo) v52 (T1) | **25 wikis** | Narrative inspiration source list |

**Mechanism distinction from 57a + 57b:**

- **57a Direct citation:** Citing wiki built AFTER cited subject's wiki. Citation flow forward in time.
- **57b Aggregator-mediated multi-citation:** Aggregator curates lists where prior corpus subject appears alongside many entries.
- **57c Forward-citation-then-wiki:** Subject B cited in earlier wiki C as dependency or reference; LATER wiki D builds B's wiki. **Citation flow REVERSED in time** relative to wiki-build sequence. Functions as **external validity signal of corpus-selection discipline** — independent agent-ecosystem judgment retroactively validates Storm Bear's selection criteria.

**Updated Pattern #57 confirmed sub-variant taxonomy (post-v53 mini-audit):**

> **3 CONFIRMED sub-variants observed (post-v53 mini-audit):**
>
> - **57a Direct citation** (N=5; CONFIRMED at v50 mini-audit promotion; +1 at v52 omo) — Author of citing wiki directly references prior corpus subject in repo governance files. Citation flow forward in time.
> - **57b Aggregator-mediated multi-citation** (N=1 stale-flagged at v50 registration; +5 v55, +10 v60) — Aggregator curates lists where prior corpus subject appears alongside many entries.
> - **57c Forward-citation-then-wiki** (N=2 STRUCTURAL CONFIRMED at v53 mini-audit promotion) — Subject B cited in earlier wiki C as dependency or reference; LATER wiki D builds B's wiki. Citation flow REVERSED in time. External validity signal of corpus-selection discipline. N=2: multica v15 → vercel-labs v51 (36-wiki gap; skills-lock.json formal dependency); OMC v27 → oh-my-openagent v52 (25-wiki gap; narrative inspiration source list).

**Significance:**

- 3rd CONFIRMED sub-variant within Pattern #57 — first pattern in library to acquire 3 CONFIRMED sub-variants via post-promotion sub-variant promotion
- First sub-variant promotion within already-confirmed pattern in corpus history
- External validity signal mechanism formalized — 57c demonstrates corpus-selection discipline is independently validated by ecosystem; mechanism survives long temporal gaps (25-36 wikis between citation and wiki-build)
- Two distinct sub-cases within 57c structurally validated: skills-lock.json formal dependency citation (v51) + narrative inspiration source list (v52)

**Confidence:** High. N=2 structural with mechanistically-coherent formulation. Two distinct sub-cases preserved.

#### ✅ Pattern #18 OpenCode-primary sub-observation — UN-STALE + STRUCTURAL-N=2 PROMOTION (within already-CONFIRMED Pattern #18; v2.1 mechanism EMPIRICALLY VALIDATED)

**Status at v53 mini-audit:** UN-STALE + STRUCTURAL-N=2 PROMOTION to CONFIRMED sub-observation within already-CONFIRMED Pattern #18. **v2.1 pre-registered stale-check threshold mechanism EMPIRICALLY VALIDATED** — registered at session 56 v47 HARVEST mini-audit with v52 stale-check window; **fired at exactly v52 with 2nd data point** (omo). **2nd v2.1 pre-registered conditional mechanism to fire empirically** (1st was Pattern #47 conditional retirement at v46). Pattern #18 reaches **9 refinements** (most-refined pattern in library extends from 8).

**Status history:** Registered N=1 sub-observation at session 56 v47 HARVEST mini-audit (aidevops v47 OpenCode-primary; stale-risk-flagged with +5-wiki check at v52). STRUCTURAL N=2 reached at v52 omo (joins aidevops v47); v2.1 pre-registered stale-check threshold fires at exactly v52 with 2nd data point.

**Evidence (N=2 structural):**

| # | Wiki | OpenCode-primacy mechanism | Tier |
|---|------|------------------------------|------|
| OpenCode-1 | aidevops v47 (Marcus Quinn) | README verbatim "Recommended setup: OpenCode + Claude models." Designed and tested for OpenCode first; Claude Code secondary | T1 |
| OpenCode-2 | omo v52 (YeonGyu-Kim / Sionic AI) | omo IS OpenCode plugin — `@opencode-ai/plugin` + `@opencode-ai/sdk` dependencies verified in package.json; framework architecturally extends OpenCode runtime | T1 |

**Updated Pattern #18 runtime-primacy-choice sub-observation (post-v53 mini-audit):**

> **Runtime-primacy-choice sub-observation (CONFIRMED at v53 mini-audit; promoted from N=1 v47 → N=2 STRUCTURAL via empirical v2.1 stale-check threshold firing at v52):**
>
> Runtime-primacy is a **deliberate framework design choice** independent of Layer 1 (MCP), Layer 2 (community-platform identifiers), and Layer 3 (agent-execution implementation).
>
> **3 runtime-primacy choices observed at v53:**
> 1. Claude-Code-primary — default; majority of corpus T1 frameworks
> 2. **OpenCode-primary CONFIRMED at v53** (N=2 STRUCTURAL): aidevops v47 (Marcus Quinn) + omo v52 (YeonGyu-Kim). Mechanism: explicit OpenCode-as-recommended-tested-first OR architecturally-extending-OpenCode-runtime.
> 3. Codex-primary — N=1 sibling-repo observation (oh-my-codex sibling product to OMC v27)

**Significance:**

- 2nd v2.1 pre-registered conditional mechanism to fire empirically (after Pattern #47 conditional retirement at v46). v2.1 mechanism robust across both retirement-trigger AND promotion-trigger contexts.
- Pattern #18 reaches 9 refinements — most-refined pattern in library extends from 8. Track: v17 / v18 / v19 / v20 / v31 / v36 / v42 / v47 / v53 NEW.
- 3-runtime-primacy diversity now CONFIRMED at structural-N=2 for OpenCode-primary specifically — corpus is decisively no longer Claude-Code-monoculture.
- Cross-pattern coupled-design observation (registered v47): aidevops v47 22c authoritative-with-shim + OpenCode-primary co-occur. omo v52 has OpenCode-primary WITHOUT 22c (uses 22a auto-generated via /init-deep). Coupling is observational, not necessary.

**Confidence:** High. N=2 structural with mechanistically-coherent formulation. Both data points are T1 frameworks. v2.1 pre-registered stale-check threshold fired at exact registered window — empirical validation of mechanism.

---

### Promoted at v63 mini-audit (#21)

#### ✅ #21 SDD Methodology Emergence (PROMOTED v63 mini-audit under criterion #2 structural-unambiguity-at-N=2)
**Status at v63 mini-audit:** PROMOTED to CONFIRMED via criterion #2 (structural-unambiguity-at-N=2). **Longest stale-to-promotion arc in corpus history at 36 wikis** (v25 stale-flag → v63 promotion). **1st un-stale-via-independence-test promotion in corpus.**

**Status history:**
- v17 spec-kit candidate registration (N=2 baseline with GSD v5 SDD-feature-shaped predecessor)
- v22 mini-audit flagged approaching-stale (4 wikis without 3rd SDD framework)
- v25 audit STALE-CANDIDATE flag confirmed (8 wikis without 3rd SDD framework)
- v54 gsd-2 mini-audit considered un-stale → REJECTED (gsd-2 = same lineage as GSD v5)
- v58 OpenSpec ship → implicit N=3 evidence (fact-verification gap: not added to evidence list at v58→v60 audit transition)
- v60 mini-audit re-considered un-stale via gsd-2 → REJECTED via lineage-grounds (correctly held line); re-evaluation criterion explicitly opened: "v60+ wiki OR if INDEPENDENT SDD-centered framework emerges at T2-T5"
- **v61 cc-sdd ship → INDEPENDENT 4th-lineage evidence (gotalab solo-Japanese + Kiro IDE intellectual lineage — corpus-first external-IDE-methodology lineage)**
- **v63 mini-audit (this entry) → fact-verification gap closed (OpenSpec v58 added to evidence list) + UN-STALE + PROMOTE under criterion #2**

**Evidence at N=4 across 4 distinct organizational archetypes:**

| # | Wiki | Tier | Org archetype | Methodology shape |
|---|------|------|---------------|-------------------|
| 21a | GSD v5 + gsd-2 v54 | T1 | Solo-product-line (gsd-build) | Feature-shaped SDD (single lineage; v5 + v54 = predecessor + successor) |
| 21b | spec-kit v17 | T1 | Corporate (Microsoft / GitHub) | 9-article constitution + 80+ marketplace + AI-disclosure policy |
| 21c | OpenSpec v58 | T1 | Pseudonymous-org (Fission-AI) | Per-tool format translation 30+ tools |
| 21d | **cc-sdd v61** | T1 | **Solo-international Japanese (gotalab)** | **Multi-platform Skills harness + Kiro IDE methodology lineage + adversarial subagent review architecture** |

**Formal statement (promoted):**
> Spec-Driven Development emerges as recurring T1 methodology choice across structurally-distinct organizational archetypes — observed in solo-product-line (gsd-build), corporate-official (Microsoft GitHub), pseudonymous-org (Fission-AI), and solo-international-individual (gotalab Japanese) implementations. Each implementation centers specifications-as-contracts between system components with markdown specs expressing intent + boundaries while tests/builds/lint provide mechanical validation. Implementations vary in: (a) approval-gate granularity (informal feature-shape vs 3-explicit-phase-gates vs constitution-articles), (b) deployment mechanism (single-tool vs per-tool format translation vs multi-platform Skills format translation), (c) workflow primitive count (3-step vs 6-step), (d) review architecture (cooperative vs adversarial-subagent). Cross-archetype emergence falsifies "zeitgeist-timed phenomenon past peak" stale-rationale; SDD methodology continues to attract independent implementers at v17 → v54 → v58 → v61 cadence. **All 4 implementations T1 currently** — cross-tier promotion under criterion #1 default ≥3-cross-tier reserved for future T2-T5 SDD framework emergence.

**Cross-references:**
- Pattern #19 Intellectual Lineage Archetypes (CONFIRMED v20) — cc-sdd v61 introduces external-IDE-methodology lineage as new lineage type (registered separately as Pattern #75 candidate at v63)
- Pattern #18 protocol-translation Layer 2 — OpenSpec v58 per-tool format translation + cc-sdd v61 install-time per-platform skill format translation are deployment-mechanism-axis observations (cc-sdd at 8 platforms install-time-per-platform-skill-format-translator registered as Pattern #18 sub-archetype within Layer 2 at v63)
- Pattern #51 Vibe-Coding Spectrum — all 4 SDD frameworks are anti-vibe-pole observations (spec-kit v17 pure anti-vibe via 9-article constitution; cc-sdd v61 anti-vibe-with-pragmatic-acknowledgment sub-pole — counter-evidence narrowing v60+v61 window)
- Pattern #57 57c-anti-pattern-foil — mattpocock v57 + OpenSpec v58 cite spec-kit as anti-pattern-foil; cc-sdd v61 does NOT cite spec-kit/OpenSpec/GSD by name (no 57c contribution)
- Pattern #73 Regional-Archetype-Registry T1 — cc-sdd v61 introduces 73d Japanese sub-variant (added within Pattern #73 family at v63)
- Pattern #74 EARS-Format Requirements (NEW candidate at v63) — cc-sdd v61 first corpus EARS reference; sibling within Pattern #21 family
- Pattern #76 Adversarial Subagent Review Architecture (NEW candidate at v63) — cc-sdd v61 first corpus framework-level adversarial-review; orthogonal to SDD methodology

**Confidence:** High. N=4 across 4 organizational archetypes. Formal statement structurally-coherent. All-T1 limitation acknowledged with clear cross-tier promotion path (criterion #1 if T2-T5 SDD framework emerges).

**Stale-risk-flag (post-promotion observational watch):** None — promotion under structural-unambiguity criterion at N=4 is robust. If SDD framework emergence stops within next 10 wikis (v62-v71), reformulate as historical-trend pattern.

---

### Promoted at v66 EARLY mini-audit (#78)

#### ✅ #78 Living-Domain-Standards Tracking (PROMOTED v66 EARLY-OPERATOR-ELECTED mini-audit under criterion #2 structural-unambiguity-at-N=2 with 78a + 78b sub-mechanisms)
**Status at v66 EARLY-OPERATOR-ELECTED mini-audit (2026-05-14):** PROMOTED to CONFIRMED via criterion #2 (structural-unambiguity-at-N=2). **FASTEST PROMOTION ARC in corpus history at 2 wikis** (v64 candidate-registration N=1 stale-risk-flag → v65 N=2 evidence within 1 wiki → v66 EARLY mini-audit promotion within 1 wiki of N=2). **TIED-FASTEST 1-wiki un-stale cycle in corpus history with v62→v63 Pattern #76 1-wiki counter-evidence (Library-vocabulary item #10 evidence).**

**Status history:**
- v64 claude-seo wiki ship → candidate registration N=1 stale-risk-flagged (Agrici Daniel SEO-domain external-authority standards tracker with deprecation-aware schemas; 8 dated deprecation events + 4+ versioned external authority citations + CHANGELOG-as-absorption-ledger)
- v65 claude-code-system-prompts wiki ship → N=2 evidence within 1 wiki (Piebald-AI single-vendor-product-internals archive: 211 KB CHANGELOG / 1,896 lines / 176 versions since v2.0.14 with per-version commit-hash + token-delta + per-prompt change-description; updated within minutes of each Claude Code release)
- **v66 EARLY-OPERATOR-ELECTED mini-audit (this entry) → PROMOTE under criterion #2** with 78a + 78b registered as sub-mechanisms within confirmed Pattern #78

**Evidence at N=2 across 2 maximally-distinct sub-mechanisms:**

| # | Wiki | Sub-mechanism | Tier | Author archetype | Authority type | CHANGELOG scope |
|---|------|---------------|------|------------------|----------------|----------------|
| 78a | v64 claude-seo | **multi-vendor-industry-domain-standards** | T1 | Solo-individual (AgriciDaniel) | 4+ distinct authorities (Google QRG + Schema.org + CWV + ISO) | Release notes per version (8 dated deprecation events) |
| 78b | v65 claude-code-system-prompts | **single-vendor-product-internals-archive** | T1 NEW sub-archetype (reverse-engineering reference archive) | Corporate-org (Piebald-AI) | Single-vendor (Anthropic Claude Code only) | 211 KB / 1,896 lines / 176 versions / per-prompt change-description |

**10-axis structural distinction between 78a + 78b confirms non-coincidental sub-mechanisms:**

| Axis | 78a multi-vendor-industry-domain | 78b single-vendor-product-internals |
|------|----------------------------------|-------------------------------------|
| 1. Authority type | Multi-source industry domain | Single-vendor product |
| 2. Cardinality | 4+ distinct authoritative sources | 1 vendor product |
| 3. Tracking granularity | Per-release notes | Per-version commit-hash + token-delta + per-prompt change-description |
| 4. Version cadence | Yearly+ (Google QRG / Schema.org major releases) | Within-minutes-to-hours per Claude Code release |
| 5. Absorption mechanism | CHANGELOG-as-absorption-ledger | Automated extraction script (`tools/updatePrompts.js`) |
| 6. Reverse-engineering requirement | NO — external standards are public | YES — vendor source artifacts extracted from compiled distribution |
| 7. Vendor relationship | Tracks-external-authorities | Tracks-vendor-internals (sub-DMCA tolerance) |
| 8. Author archetype | Solo-individual + AI Workflow Architect | Corporate-org + commercial agentic-IDE company |
| 9. CHANGELOG size | ~moderate (release-note tier) | 211 KB / 1,896 lines (archive-tier) |
| 10. Granularity per change | Standards-version + deprecation-event | Per-prompt + token-delta + per-version |

**Formal statement (promoted):**
> Frameworks or reference archives codify continuously-evolving external authority standards via explicit deprecation-aware schemas + dated standards-version tracking — distinct from coding-methodology codification (Pattern #21 SDD), distinct from progressive disclosure (Pattern #28 LOAD-vs-TRACK), distinct from one-time leak archives (Pattern #21 System Prompts Leaks). Two sub-mechanisms emerge at N=2 with maximally-distinct structural axes:
>
> - **78a multi-vendor-industry-domain-standards** — tracks 3+ distinct authoritative sources at industry-domain level (regulatory + standards-body + measurement-framework + ISO-style codes) with CHANGELOG-as-absorption-ledger discipline. Per-release notes track which external standard moved when. Example: SEO domain tracking Google Quality Rater Guidelines + Schema.org + Core Web Vitals + ISO country codes.
>
> - **78b single-vendor-product-internals-archive** — tracks a single closed-source product's internal artifacts via continuous-reverse-engineering with automated extraction + per-release update cadence. Per-version commit-hash + token-delta + per-prompt change-description granularity. Example: continuous archive of Claude Code system prompts with within-minutes update cadence.
>
> The agent or archive INTERNALIZES the external standards' (or product internals') versioning system rather than reasoning from a frozen snapshot. Sub-mechanism choice correlates with author archetype + competitive-context: 78a aligns with solo-individual + multi-vendor-industry tracking; 78b aligns with corporate-org + single-vendor-product-internals via competitor-tolerated reverse-engineering.

**Cross-references:**
- Pattern #19 Intellectual-Lineage-Archetypes — ecosystem-portfolio-builder sub-archetype (PROMOTED at v66 EARLY mini-audit) includes both 78a author AgriciDaniel and 78b author Piebald-AI as portfolio-builder examples; sister within Pattern #19 family
- Pattern #21 System Prompts Leaks (CONFIRMED v63) — Pattern #78 78b mechanism is distinct from Pattern #21 (one-time exfiltration); Pattern #78 78b is continuous-extraction with automated tooling
- Pattern #28 Multi-Provider AI Support — distinct: Pattern #28 is LOAD-vs-RUN-with-multi-providers; Pattern #78 is TRACK-external-versions discipline
- Pattern #57 Recursive Corpus Reference (CONFIRMED v50) — 57c-product sub-variant registered at v66 EARLY mini-audit captures Claude Code product becoming corpus-foundation-PRODUCT inheritance; reinforces Pattern #78 78b authority pattern at meta-level
- Pattern #66 Supply-Chain (OT) — meta-supply-chain-awareness sub-category registered at v66 EARLY mini-audit captures the supply-chain-awareness layer of vendor-product-internals tracking; orthogonal to Pattern #78 (Pattern #66 is supply-chain mechanism; Pattern #78 is standards-tracking discipline)
- Pattern #79 Continuous-Reverse-Engineering Reference Archive (CANDIDATE N=1 stale-risk-flagged v65) — distinct EXTRACTION methodology, NOT promoted with Pattern #78; Pattern #79 captures the methodology of building the archive; Pattern #78 78b captures the standards-tracking discipline applied via that methodology

**Confidence:** High. N=2 with maximally-distinct structural axes (10-axis differentiation between sub-mechanisms). Formal statement structurally-coherent. Sub-mechanism registration at promotion (78a + 78b) per routine v2.2 discipline; stale-checks scheduled at v67 (+2 wikis from promotion).

**Stale-risk-flag (post-promotion observational watch):**
- **78a multi-vendor-industry-domain-standards** sub-mechanism — N=1 within Pattern #78; v67 stale-check for 2nd 78a-shape subject (medical-coding skill tracking ICD-10/ICD-11 / GDPR-compliance agent tracking case-law / financial-reporting agent tracking GAAP/IFRS / etc.). Risk: 78a may stay SEO-domain-specific.
- **78b single-vendor-product-internals-archive** sub-mechanism — N=1 within Pattern #78; v67 stale-check for 2nd 78b-shape subject (third-party Cursor system-prompt archive / third-party Codex CLI system-prompt archive / third-party Windsurf reference archive). Risk: 78b may stay Claude-Code-specific.
- **Sub-mechanism reorganization at v68-v69:** If 78a OR 78b fails to reach N=2 within 4 wikis post-promotion, reformulate Pattern #78 to retain only the strengthening sub-mechanism + retire the other to observational status.

**Library-vocabulary item #10 evidence (1-wiki Rapid-Pattern-Evolution):** Pattern #78 1-wiki un-stale cycle (v64→v65) is the SECOND instance of 1-wiki pattern evolution in corpus history (after v62→v63 Pattern #76 1-wiki counter-evidence cycle). N=2 evidence for Library-vocabulary item #10 codified at routine v2.2.

---

### Promoted at v69 OVERDUE-NATURAL-CADENCE mini-audit (#83)

#### ✅ #83 Honest-Deficiency-Disclosure Discipline (PROMOTED v69 OVERDUE-NATURAL-CADENCE mini-audit under criterion #1 default ≥3-cross-tier with N=5 cross-archetype evidence; 5 sub-mechanisms 83a/83b/83c/83d/83e registered at promotion)

**Status at v69 OVERDUE-NATURAL-CADENCE mini-audit (2026-05-19):** PROMOTED to CONFIRMED via criterion #1 (default ≥3-cross-tier, N=5 evidence v64+v65+v67+v68+v69 with HIGH confidence). **2nd PROMOTION-from-pre-eligible-state in corpus history** (after Pattern #19 + #78 at v66 EARLY mini-audit). **5-wiki accumulation arc** (v64 N=1 registration v66 audit → v67 N=3 PROMOTION-ELIGIBLE proposal-document → v68 N=4 consolidation → v69 N=5 consolidation with multi-surface saturation → v69 OVERDUE-NATURAL-CADENCE audit PROMOTION).

**Status history:**
- v66 EARLY-OPERATOR-ELECTED mini-audit registration → CANDIDATE N=2 stale-risk-flagged (v64 claude-seo + v65 claude-code-system-prompts evidence)
- v67 opencode-antigravity-auth wiki ship → N=3 PROMOTION-ELIGIBLE (5 distinct disclosure surfaces in single subject; corpus-first multi-surface saturation); proposal-document filed at `03 Projects/opencode-antigravity-auth - Beginner Analysis/01 Analysis/(C) Pattern-83 Honest-Deficiency-Disclosure N=3 promotion proposal.md`
- v68 vercel-labs/zero wiki ship → N=4 consolidation evidence (2 disclosure surfaces: README pre-1.0 + AGENTS.md §Safety; consolidates v67 PROMOTION-ELIGIBLE verdict)
- v69 CloakBrowser wiki ship → N=5 consolidation evidence (5 disclosure surfaces in single subject — SECOND multi-surface saturation in corpus history after v67)
- **v69 OVERDUE-NATURAL-CADENCE mini-audit (this entry) → PROMOTE under criterion #1** with 5 sub-mechanisms 83a / 83b / 83c / 83d / 83e registered

**Evidence at N=5 across maximally-distinct sub-mechanisms + tier diversity:**

| # | Wiki | Subject | Sub-mechanism | Tier | Disclosure surfaces |
|---|------|---------|---------------|------|--------------------|
| 83a | v64 claude-seo | Solo SEO-vertical T1 | **security-disclosure** | T1 | 1 surface: README VULN-list (10 named v1.9.6 security fixes with severity tags + acknowledgment of prior exposure period) |
| 83b | v65 claude-code-system-prompts | Corporate-org T1 reverse-engineering archive | **methodology-disclosure** | T1 | 2 surfaces: Piebald-AI extraction-methodology disclosure + accuracy-tolerance disclosure ("±20 tokens tolerance from runtime") |
| 83c | v67 opencode-antigravity-auth | T4 Bridge OAuth-credential-plugin | **legal-operational-disclosure** | T4 | **5 surfaces (corpus-first multi-surface saturation):** README CAUTION block + Legal collapsed footer + Intended Use disclaimer + docs/ANTIGRAVITY_API_SPEC status banner + CHANGELOG honest detection-pattern naming |
| 83d | v68 vercel-labs/zero | T1 programming-language | **experimental-status-disclosure** | T1 | 2 surfaces: README "Zero is pre-1 and intentionally unstable... Security vulnerabilities should be expected" + AGENTS.md §Safety repeats + specific failure modes |
| 83e | v69 CloakBrowser | T2 Service stealth-browser | **license-axis-as-disclosure-surface** | T2 | **5 surfaces (2nd multi-surface saturation):** BINARY-LICENSE security disclaimer + CHANGELOG #217 path-traversal security fix + $100 max-aggregate-liability cap + Acceptable Use enumeration + macOS platform-tier-disparity README acknowledgment |

**Cross-tier distribution:** T1 (3×: 83a + 83b + 83d) + T2 (1×: 83e) + T4 (1×: 83c) = **3 distinct tiers** with N=5 ≥ criterion #1 (default ≥3-cross-tier) requirement.

**Cross-archetype diversity (maximally distinct):**
- Solo-individual (83a AgriciDaniel) + Corporate-org (83b Piebald-AI / 83c NoeFabris / 83d Vercel Labs) + Anonymous-corporate (83e CloakHQ) = 3 distinct author archetypes
- T1 domain-vertical (83a) + T1 reverse-engineering archive (83b) + T4 OAuth bridge (83c) + T1 programming-language (83d) + T2 stealth service (83e) = 5 distinct sub-archetypes

**5 sub-mechanism formal definitions (registered at promotion):**

- **83a security-disclosure** — Framework explicitly discloses prior security exposure periods, named CVE-equivalent vulnerabilities, severity tags, or post-exposure remediation timelines on user-facing surface. Does NOT minimize via aggregation or vague "minor security update" framing. Example: v64 claude-seo README VULN-list 10 named v1.9.6 fixes.

- **83b methodology-disclosure** — Framework or reference archive explicitly discloses extraction methodology, accuracy tolerances, or knowledge-source limitations as part of trust-building. Distinct from vague "as accurate as possible" — provides numerical or categorical bounds. Example: v65 claude-code-system-prompts "±20 tokens tolerance from runtime" + "Maintained by Piebald AI, not by Anthropic."

- **83c legal-operational-disclosure** — Framework explicitly discloses legal exposure, ToS violations, account-banning risk, or intended-use boundaries on multiple user-facing surfaces. Often includes explicit non-production framing + user-acknowledgment-block. Example: v67 opencode-antigravity-auth README CAUTION + Legal + Intended Use + docs API status banner + CHANGELOG honest detection-naming.

- **83d experimental-status-disclosure** — Framework explicitly discloses pre-1.0 instability, breaking-change probability, or production-readiness limitations as prominent README banner (not buried in CHANGELOG). Often paired with specific failure-mode enumeration. Example: v68 vercel-labs/zero "Zero is pre-1 and intentionally unstable... Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure."

- **83e license-axis-as-disclosure-surface** — License itself serves as primary disclosure surface, with explicit prohibited-use enumeration + bounded liability + indemnification + acceptable-use boundaries. Distinct from generic "AS IS" disclaimer — names specific prohibited mechanisms. Example: v69 CloakBrowser BINARY-LICENSE Acceptable Use enumeration (4 prohibited uses) + $100 max-aggregate-liability cap.

**Formal statement (promoted):**
> Framework, reference archive, or service explicitly discloses limitations, accuracy boundaries, prior security exposure periods, methodology gaps, experimental-status instability, legal exposure, or license-bounded prohibited uses on user-facing surfaces (README / CHANGELOG / release notes / LICENSE) rather than minimizing, normalizing, or obscuring. Disclosure is non-minimized (does not aggregate "minor security update" or vague "limitations" framing). Distinct from formal anti-vibe discipline (Pattern #51) — Pattern #51 is upfront-positioning; Pattern #83 is ongoing-disclosure of specific deficiencies.
>
> Five sub-mechanisms emerge at N=5 with maximally-distinct disclosure-axes:
> - **83a security-disclosure** — explicit prior security exposure + named CVE-equivalent disclosures
> - **83b methodology-disclosure** — extraction methodology + accuracy tolerance + source-limitation framing
> - **83c legal-operational-disclosure** — ToS violations + account-banning risk + intended-use boundaries
> - **83d experimental-status-disclosure** — pre-1.0 instability + production-readiness limitations
> - **83e license-axis-as-disclosure-surface** — license itself enumerates prohibited uses + bounded liability + acceptable-use boundaries
>
> Sub-mechanism choice correlates with archetype + competitive-context: 83a aligns with security-focused solo / 83b with reverse-engineering archive vs vendor / 83c with adversarial-platform-relationship plugins / 83d with pre-1.0 experimental products / 83e with dual-use legal-defensive products.

**Multi-surface saturation sub-archetype (emergent at v67 + v69):**

A subject exhibits MULTI-SURFACE SATURATION when 5+ disclosure surfaces appear within the single subject simultaneously. **Corpus-first:** v67 opencode-antigravity-auth (5 surfaces: README CAUTION + Legal + Intended Use + docs API status banner + CHANGELOG). **Second instance:** v69 CloakBrowser (5 surfaces: BINARY-LICENSE + CHANGELOG #217 + $100 cap + Acceptable Use + macOS disparity).

At N=2 multi-surface saturation, this is registered as a Pattern #83 SUB-ARCHETYPE called *multi-surface saturation*. Potential promotion to formal sub-variant at N=3 emergence per criterion 4 variant-within-pattern-at-N=2.

**Cross-references:**
- Pattern #51 Vibe-Adjacent Positioning Spectrum (CONFIRMED) — Pattern #83 is disclosure-discipline subset/sister, not absorbed. Pattern #51 is upfront-positioning; Pattern #83 is ongoing-disclosure of specific deficiencies.
- Pattern #45 Dual-Licensing Discipline (CONFIRMED v60) — Pattern #45 sub-typology 45c "Artifact-Scope-Split with Acceptable-Use-Enumeration" (CloakBrowser v69) overlaps with Pattern #83 sub-mechanism 83e (both about license-axis as disclosure surface). NOT absorbed — Pattern #45 is license-shape mechanism; Pattern #83 is disclosure-discipline.
- Pattern #66 meta-supply-chain-awareness (CONFIRMED) — orthogonal. Pattern #66 is supply-chain attribution; Pattern #83 is deficiency disclosure.
- Pattern #84 Cross-Vendor Ecosystem-Tolerance (CANDIDATE) — Pattern #83 83c sub-mechanism evidence overlaps with Pattern #84 84a tool-tolerance. NOT absorbed — Pattern #83 is disclosure-discipline; Pattern #84 is vendor-business-decision dynamic.

**Confidence:** HIGH. N=5 with cross-tier diversity (T1 + T2 + T4) and 5 maximally-distinct sub-mechanisms (security / methodology / legal-operational / experimental-status / license-axis). Formal statement structurally-coherent. Sub-mechanism registration at promotion (83a-e) per routine v2.2 discipline; sub-typology formalization decision deferred to v70+ audit.

**Sub-typology formalization at v70+ audit:**
- 83a/b/c/d/e sub-mechanisms are observationally distinct. v70+ audit should decide whether to formalize 83a-e as separate sub-variants of Pattern #83 OR retain as observational sub-mechanisms within single Pattern #83 entry.
- Multi-surface saturation sub-archetype (N=2 at v67 + v69) is candidate for formal sub-archetype registration at v70+ audit per criterion 4.

**Stale-risk-flag (post-promotion observational watch):**
- 83a/b/c/d/e sub-mechanisms each at N=1 within Pattern #83. v70+ stale-checks for 2nd-shape evidence per sub-mechanism.
- If any sub-mechanism fails to reach N=2 within 4 wikis post-promotion (v73), reformulate Pattern #83 to retire the unsupported sub-mechanism.

**Library-vocabulary item #10 evidence (1-wiki Rapid-Pattern-Evolution):** Pattern #83 v66→v67 1-wiki promotion-readiness cycle (4-day gap from candidate registration to PROMOTION-ELIGIBLE proposal-document) is the THIRD instance of 1-wiki pattern evolution in corpus history (after Pattern #76 v62→v63 + Pattern #78 v64→v65). N=3 evidence for Library-vocabulary item #10.

**Audit document:** `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE; LARGEST batch corpus-history; Pattern #83 N=5 PROMOTION + 23 other items).md` § "Decision A1"

---

### Promoted at v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (#84)

#### ✅ #84 Cross-Vendor Ecosystem-Tolerance (PROMOTED v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit under criterion #1 default ≥3-cross-tier + criterion #4 variant-within-pattern-at-N=2 with N=3 cross-archetype evidence; 3 sub-mechanisms 84a/84b/84c registered at promotion)

**Status at v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (2026-05-19):** PROMOTED to CONFIRMED via criterion #1 (default ≥3-cross-tier, N=3 evidence v62+v65+v71) + criterion #4 (variant-within-pattern, 3 sub-mechanisms emerge: 84a Tool-tolerance + 84b Usage-enforcement + 84c Provider-Agnostic-By-Design) with HIGH confidence. **3rd PROMOTION-from-pre-eligible-state in corpus history** (after Pattern #19 + #78 at v66 EARLY mini-audit, Pattern #83 at v69 OVERDUE-NATURAL-CADENCE mini-audit). **6-wiki accumulation arc** (v62 codex-plugin-cc 84a first evidence → v65 claude-code-system-prompts 84b N=2 → v66 EARLY audit candidate registration → v67 84a/84b sub-mechanism refinement → v71 agents-best-practices N=3 PROMOTION-ELIGIBLE with 84c proposal-document → v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER audit PROMOTION).

**Status history:**
- v62 codex-plugin-cc wiki ship (2026-04-18) → N=1 first evidence (Tool-tolerance: OpenAI publishes Apache-2.0 plugin FOR Anthropic Claude Code rival platform; sub-DMCA threshold maintained)
- v65 claude-code-system-prompts wiki ship (2026-05-14) → N=2 strengthening (Usage-enforcement-axis emerges: Piebald-AI reverse-engineering archive; Anthropic apparent tolerance with no DMCA despite competitive context + 10,176 stars)
- v66 EARLY-OPERATOR-ELECTED mini-audit registration → CANDIDATE N=2 stale-risk-flagged
- v67 opencode-antigravity-auth wiki ship → REFINEMENT evidence (84a/84b sub-mechanism candidates registered: artifact-tolerance vs usage-enforcement split)
- v71 agents-best-practices wiki ship → N=3 PROMOTION-ELIGIBLE with 84c sub-typology proposed (Provider-Agnostic-By-Design = author-design-choice meta-archetype vs prior 84a/84b ecosystem-norm meta-archetype); proposal-document filed at `03 Projects/agents-best-practices - Beginner Analysis/01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`
- **v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (this entry) → PROMOTE under criterion #1 + criterion #4** with 3 sub-mechanisms 84a / 84b / 84c registered

**Evidence at N=3 across maximally-distinct sub-mechanisms + tier diversity:**

| # | Wiki | Subject | Sub-mechanism | Tier | Meta-archetype | Mechanism evidence |
|---|------|---------|---------------|------|----------------|--------------------|
| 84a | v62 codex-plugin-cc | T4 Bridge OpenAI→Claude Code plugin | **Tool-tolerance** | T4 | ecosystem-norm | OpenAI publishes Apache-2.0 plugin explicitly FOR Anthropic Claude Code; no DMCA; sub-DMCA threshold maintained |
| 84b | v65 claude-code-system-prompts | T1 reverse-engineering reference archive | **Usage-enforcement** | T1 | ecosystem-norm | Piebald-AI reverse-engineers Anthropic Claude Code internals; Anthropic apparent tolerance with no DMCA against artifact despite 10,176-star visibility; vendor enforcement layer separated from artifact-takedown layer |
| 84c | v71 agents-best-practices | T1 Assistant Skill | **Provider-Agnostic-By-Design (NEW)** | T1 | author-design-choice | Individual author deliberately synthesizes BOTH OpenAI AND Anthropic agentic patterns equally; framework runs identically on both platforms; intellectual synthesis from BOTH vendor corpora equally; vendor-tolerance is inherent rather than tested-after-publication |

**Cross-tier distribution:** T1 (2×: 84b + 84c) + T4 (1×: 84a) = **2 distinct tiers** with N=3 ≥ criterion #1 (default ≥3-cross-tier) requirement satisfied (alongside cross-archetype distribution).

**Cross-archetype diversity (maximally distinct):**
- Vendor-published plugin (84a OpenAI corporate-org) + Community reverse-engineering archive (84b Piebald-AI corporate-org) + Individual-author synthesis (84c DenisSergeevitch solo-individual) = 3 distinct author archetypes
- T4 cross-vendor Bridge (84a) + T1 reverse-engineering archive (84b) + T1 provider-agnostic Assistant Skill (84c) = 3 distinct sub-archetypes

**3 sub-mechanism formal definitions (registered at promotion):**

- **84a Tool-tolerance** — Vendor does NOT challenge the cross-vendor artifact at the tool/artifact layer (no DMCA, no enforcement against repo, npm package, or distribution channel). Sub-DMCA threshold maintained despite competitive context. Tolerance is an externally-applied norm; the vendor *could* have challenged but chose not to. Example: v62 codex-plugin-cc — OpenAI publishes Apache-2.0 plugin explicitly targeting Anthropic's Claude Code platform; no legal challenge from Anthropic.

- **84b Usage-enforcement** — Vendor tolerates at the artifact layer but may enforce at the account/usage layer (bans, shadow-bans, verification challenges, validation_required errors). Artifact-takedown and usage-enforcement are separated as distinct enforcement layers. Example: v65 claude-code-system-prompts — Piebald-AI archive tolerated as artifact; v67 opencode-antigravity-auth refinement evidence — Google enforces against accounts but not against the npm package.

- **84c Provider-Agnostic-By-Design (NEW v72)** — Subject is created with explicit intent to synthesize/serve multiple vendor ecosystems equally; vendor-tolerance is inherent rather than tested-after-publication. Meta-archetype shift: vendor-tolerance becomes an internal design principle (author-design-choice) rather than an externally-applied ecosystem norm. Author intentionality is the distinguishing axis. Example: v71 agents-best-practices — DenisSergeevitch synthesizes Anthropic 5-guide corpus + OpenAI 5-guide corpus into unified 15-reference framework running identically on Claude Code + Codex + OpenAI Agents.

**Formal statement (promoted):**
> Agentic-AI ecosystem operates under cross-vendor tolerance dynamics manifesting via three distinct sub-mechanisms. (84a) Vendors tolerate cross-vendor artifacts at the artifact layer (no DMCA, no take-down against rival-platform plugins, reverse-engineering archives, or compatibility shims). (84b) Vendors may separate artifact-tolerance from usage-enforcement — accounts may be banned while artifacts remain unchallenged. (84c) Individual authors design provider-agnostic frameworks that synthesize multiple vendor corpora equally, making cross-vendor tolerance an inherent internal design choice rather than an externally-applied ecosystem norm.
>
> Three sub-mechanisms with meta-archetype distinction:
> - **84a Tool-tolerance** — vendor-applied artifact-layer tolerance (ecosystem-norm meta-archetype)
> - **84b Usage-enforcement** — vendor-applied account-layer enforcement separated from artifact-layer (ecosystem-norm meta-archetype)
> - **84c Provider-Agnostic-By-Design** — author-applied internal design principle for multi-vendor synthesis (author-design-choice meta-archetype)
>
> Meta-archetype shift from 84a/b to 84c (ecosystem-norm → author-design-choice) is the corpus-first author-intentionality axis added at v71 + v72 audit. Sub-mechanism choice correlates with author position: vendor-organization adopts 84a/b posture; solo-author adopts 84c posture.

**Cross-references:**
- Pattern #18 Agent Runtime Standardization (CONFIRMED) — Pattern #84 is vendor-business-decision layer; Pattern #18 is product-design layer. Orthogonal but co-occur in cross-vendor artifacts.
- Pattern #78 Living-Domain-Standards Tracking (CONFIRMED) — Pattern #78 v71 78a evidence (triple-standard + dual-vendor) co-occurs with Pattern #84 84c (provider-agnostic-by-design); the LDS-tracking discipline enables provider-agnostic synthesis. Observational coupling, not necessary.
- Pattern #83 Honest-Deficiency-Disclosure (CONFIRMED v69) — Pattern #83 83c sub-mechanism evidence overlaps with Pattern #84 84a tool-tolerance (v67 opencode-antigravity-auth ToS-disclosure within cross-vendor context). NOT absorbed — Pattern #83 is disclosure-discipline; Pattern #84 is vendor-business-decision dynamic.
- Pattern #66 Supply-Chain Isolation (CONFIRMED) — orthogonal. Pattern #66 is supply-chain attribution; Pattern #84 is cross-vendor tolerance dynamic.

**Confidence:** HIGH. N=3 with cross-tier (T1 + T4) + cross-archetype (vendor-corp + community-corp + solo-individual) + 3 maximally-distinct sub-mechanisms (Tool-tolerance / Usage-enforcement / Provider-Agnostic-By-Design) and meta-archetype distinction (ecosystem-norm vs author-design-choice). Formal statement structurally-coherent. Sub-mechanism registration at promotion (84a/b/c) per routine v2.2 discipline.

**Stale-risk-flag (post-promotion observational watch):**
- 84a/b/c sub-mechanisms each at N=1 within Pattern #84. v75+ stale-checks for 2nd-shape evidence per sub-mechanism.
- If any sub-mechanism fails to reach N=2 within 4 wikis post-promotion (v76), reformulate Pattern #84 to retire the unsupported sub-mechanism.
- Pattern #84 84c is the corpus-first meta-archetype shift; if v75+ adds no additional author-design-choice evidence, 84c sub-mechanism downgrades to within-84a/b refinement rather than separate sub-mechanism.

**Library-vocabulary item #10 evidence (1-wiki Rapid-Pattern-Evolution):** Pattern #84 v66→v67 1-wiki refinement cycle (84a/84b sub-mechanism candidates emerge within 4 days of candidate registration) is the FOURTH instance of 1-wiki pattern evolution in corpus history (after Pattern #76 v62→v63 + Pattern #78 v64→v65 + Pattern #83 v66→v67). N=4 evidence for Library-vocabulary item #10.

**Audit document:** `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v70-v71 (PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER; Pattern #84 + Pattern #18 sub-mechanism B PROMOTIONS + 22 other items).md` § "Decision A1"

---

### Promoted sub-archetype at v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (Pattern #18 sub-mechanism B)

#### ✅ Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" PROMOTED to formal sub-archetype with protocol-variants B1 MCP + B2 CDP + B3 placeholder

**Status at v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (2026-05-19):** PROMOTED from within-pattern sub-mechanism to formal sub-archetype within Pattern #18 shared-backend-service. **Promotion vehicle: NEW 6th Phase 4b vehicle (sub-mechanism formalization proposal-document)** introduced at v70 codegraph wiki — first sub-mechanism-promotion-via-proposal-document in corpus history. **FIRST 4-layer Pattern hierarchy formalized in corpus:** Pattern #18 (top-level) → sub-archetype shared-backend-service (registered v69 audit) → sub-mechanism B one-binary-many-CLIENTS (PROMOTED v72) → protocol-variants B1/B2/B3.

**Status history:**
- v66 agentmemory wiki ship (2026-05-14) → Pattern #18 sub-archetype shared-backend-service registered (sub-mechanism A: one-backend-many-IDENTITIES + sub-mechanism B: one-binary-many-CLIENTS sister observation)
- v69 OVERDUE-NATURAL-CADENCE mini-audit → sub-archetype shared-backend-service confirmed; sub-mechanisms A + B distinguished at audit
- v69 CloakBrowser wiki ship (2026-05-18→19) → sub-mechanism B N=2 (CDP variant; CloakBrowser-as-cloakserve)
- v70 codegraph wiki ship (2026-05-19) → sub-mechanism B N=3 (MCP variant strengthening; protocol-variants taxonomy emerges); proposal-document filed at `03 Projects/codegraph - Beginner Analysis/01 Analysis/(C) Pattern-18 sub-mechanism B one-binary-many-CLIENTS N=3 protocol-variants formalization.md`
- **v72 PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER mini-audit (this entry) → PROMOTE sub-mechanism B to formal sub-archetype** with protocol-variants B1 MCP + B2 CDP + B3 placeholder registered

**Evidence at N=3 across 2 protocol-variants:**

| Wiki | Subject | Protocol | Protocol-variant | Client count | Tool/endpoint count |
|------|---------|----------|------------------|--------------|---------------------|
| v66 (2026-05-14) | agentmemory | MCP | **B1** | 15+ agent platforms | 51 MCP tools |
| v69 (2026-05-18→19) | CloakBrowser | CDP | **B2** | Multiple framework clients (Playwright Python + Playwright npm + native CDP) | N/A (CDP endpoint) |
| v70 (2026-05-19) | codegraph | MCP | **B1** | 4 agent platforms (Claude Code + Cursor + Codex CLI + OpenCode) | 8 MCP tools |

**Promotion criteria evaluation:**
- ✅ **Criterion 1:** N=3 across T2 Service (×3); cross-tier not satisfied (all T2) but cross-protocol-variant satisfied + cross-substrate-archetype satisfied — PARTIAL PASS via cross-archetype dimension
- ✅ **Criterion 4 (variant-within-pattern-at-N=2):** B1 MCP N=2 (agentmemory + codegraph) + B2 CDP N=1 (CloakBrowser) — STRONG PASS for sub-mechanism B; protocol-variants establish criterion 4 evidence within sub-mechanism
- ✅ **NEW criterion (cross-archetype counting, v2.2):** memory-substrate (agentmemory) + browser-substrate (CloakBrowser) + code-knowledge-substrate (codegraph) — 3 distinct substrate-archetypes — STRONG PASS

**3 protocol-variant formal definitions (registered at promotion):**

- **B1 MCP variant** — one-binary-many-CLIENTS via Model Context Protocol; one MCP server binary serves multiple agent platforms as MCP clients via stdio or SSE transport. N=2 evidence: agentmemory v66 (51 tools / 15+ platforms), codegraph v70 (8 tools / 4 platforms). v72 stale-check: not applicable (already at promotion); v76 N=3 within-variant check.

- **B2 CDP variant** — one-binary-many-CLIENTS via Chrome DevTools Protocol; one browser binary serves multiple framework clients via CDP endpoint (HTTP/WebSocket). N=1 evidence: CloakBrowser v69 (Playwright Python + Playwright npm + native CDP). v75 N=2 within-variant stale-check.

- **B3 placeholder** — Reserved for future protocol-variants (gRPC, WebSocket-RPC, custom-RPC, HTTP-streaming, JSON-RPC, etc.). v77 stale-check; if no B3 evidence by v77, remove placeholder and reformulate as N-variants-fixed rather than N-variants-open taxonomy.

**4-layer Pattern hierarchy (corpus-first):**

```
Pattern #18 Agent Runtime Standardization (top-level CONFIRMED)
└── sub-archetype: shared-backend-service (registered v69 audit)
    ├── sub-mechanism A: one-backend-many-IDENTITIES (v67 Opencode↔Antigravity)
    └── sub-mechanism B: one-binary-many-CLIENTS (PROMOTED v72; N=3 across protocol-variants)
        ├── protocol-variant B1: MCP (N=2; agentmemory + codegraph)
        ├── protocol-variant B2: CDP (N=1; CloakBrowser)
        └── protocol-variant B3: placeholder (future protocols)
```

**Routine v2.3 codification implication:** n-layer pattern hierarchy support (4-layer at v70/v72) is now corpus-validated. v2.3 must support n-layer hierarchies as routine feature including: (a) protocol-variant registration as criterion 4 evidence within sub-mechanism, (b) placeholder-variant registration with stale-check schedule, (c) sub-archetype-promotion via proposal-document as NEW 6th Phase 4b vehicle.

**Cross-references:**
- Pattern #18 sub-archetype shared-backend-service sub-mechanism A "one-backend-many-IDENTITIES" (v67 Opencode↔Antigravity) — sister sub-mechanism; both share the "one binary, many clients" structural property at different layers (A: many account identities, B: many client implementations).
- Pattern #85 Platform-Primitive Foundation (CANDIDATE N=1 v66 agentmemory) — co-occurs with Pattern #18 sub-mechanism B at agentmemory subject (iii-foundation enables one-binary-many-clients cheaply). Library-vocabulary item #9 Cross-Pattern Coupled-Design evidence.
- Pattern #84 Cross-Vendor Ecosystem-Tolerance (PROMOTED v72, sister entry above) — orthogonal. Pattern #18 is product-design layer; Pattern #84 is vendor-business-decision layer.

**Confidence:** HIGH. N=3 with cross-protocol-variant + cross-substrate-archetype diversity and corpus-first 4-layer Pattern hierarchy formalization. Sub-mechanism promotion-via-proposal-document is NEW 6th Phase 4b vehicle established at v70/v72.

**Audit document:** `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v70-v71 (PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER; Pattern #84 + Pattern #18 sub-mechanism B PROMOTIONS + 22 other items).md` § "Decision A2"

---


## Promoted at v86 3-WIKI-DEFERRAL-CARRY-OVER + PROMOTION-DRIVEN + LARGEST-BATCH-IN-CORPUS-HISTORY mini-audit (#88)

### Pattern #88 — Anti-Slop-Curation (domain-general)

> **Renamed/generalized at v110 audit 2026-05-29** from "Anti-Slop-**Design**-Curation" to domain-general **"Anti-Slop-Curation"** with two sub-domains: **88-design** (CONFIRMED; v81/v82/v83/v85/v105) + **88-text/prose** (NEW, N=1; v108 humanizer canonical anchor — MEGA-viral 21K★, 30-pattern enumerated AI-writing ruleset). The 88a/b/c sub-typology (framing / named-rules / machinery) is **orthogonal to domain** and applies to both sub-domains unchanged. Scope-broadening of an already-CONFIRMED pattern (no new top-level pattern minted). **88-text/prose N=2 watch.**

**Status:** CONFIRMED at v86 audit 2026-05-22 (PROMOTED from observation-track at N=3 with formal 3-variant sub-typology taxonomy). **Domain-generalized at v110 audit 2026-05-29 (design → domain-general; +text/prose sub-domain).**

**Definition:** Design-curation practice that explicitly names and enforces resistance to LLM-generated low-quality default aesthetic output ("AI slop") — distinct from general anti-LLM positioning (which is broader and includes anti-vibe-coding, anti-magic-glue-app, etc.) — by enumerating forbidden patterns + providing CSS/HTML/component-technique alternatives + sometimes integrating enforcement machinery (P0/P1/P2 gates, denylists, build-validators).

**Evidence at PROMOTION (N=3 cross-instance arc):**

- **v81 Leonxlnx/taste-skill** (sub-typology a "framing-only"): "Anti-Slop Frontend Framework for AI Agents" + anti-slop framing-anchor + 12-skill bundle organization with aesthetic-variants as anti-slop sub-variants. Framing as identity but no enumerated forbidden-list or enforcement-machinery yet.

- **v82 alchaincyf/huashu-design** (sub-typology b "named-rules-with-enumeration"): Named "Anti AI-slop Rules" section + explicit forbidden-list (no fake-stats, no invented metrics, no generic emoji icons) + CSS-technique enumeration (specific font-stacks + color-palettes + spacing-rhythms). Co-existent PRO-VIBE + Anti-Slop framing within same subject = orthogonality-validation evidence.

- **v83 nexu-io/open-design** (sub-typology c "machinery-with-enforcement"): "Anti-AI-slop machinery" named section with P0/P1/P2 gates + Honest-placeholders-over-fake-stats discipline + Anti-AI-slop checklist + Junior-Designer workflow (borrowed from huashu-design) + Five-dim critique with "Innovation" as explicit anti-slop critique axis + integrated machinery.

**3-variant sub-typology taxonomy:**

- **88a framing-only** (v81 anchor) — anti-slop positioning as identity framing; no operational enforcement
- **88b named-rules-with-enumeration** (v82) — explicit forbidden-list + CSS-technique recommendations as rule-set
- **88c machinery-with-enforcement** (v83) — P0/P1/P2 gates + honest-placeholders discipline + integrated build-machinery

**3-instance arc within 2 calendar days** = TIES Pattern #83 83f promotion-arc-speed CORPUS-RECORD (v74+v76+v77 = 3-arc within 3 wikis).

**Cross-references:**
- Pattern #51 PRO-VIBE positioning (CONFIRMED) — ORTHOGONAL axis to Pattern #88 Anti-Slop-Design-Curation. v82 huashu CO-EXISTENT evidence validates orthogonality (PRO-VIBE = methodology framing; Anti-Slop = design-aesthetic-quality framing). Pattern #51 sub-pole "PRO-VIBE-explicit" registered at v77; sub-pole "PRO-VIBE+Anti-Slop CO-EXISTENT" candidate at v82.
- Pattern #66 Supply-Chain Isolation (CONFIRMED) — Pattern #88 sub-typology c "machinery-with-enforcement" overlaps with Pattern #66 at build-validator + denylist machinery layer. Careful framing required at v90 audit (Pattern #88 = design-aesthetic-output enforcement; Pattern #66 = supply-chain trust enforcement).
- Pattern #82 Quantitative-Marketing (PROMOTED v66) — Pattern #88 sub-typology b "named-rules-with-enumeration" explicitly rejects "fake stats" + "invented metrics" = NEGATIVE-stance toward Pattern #82-style claims. Adversarial cross-pattern interaction.

**Honest dissent / caveats:**
- 3-instance arc within 2 calendar days = unusually fast = risk of "trend-following" subjects within design-skill cluster rather than independent cross-vertical recurrence
- All 3 instances in T1 design-skill cluster + 2/3 Asian-LOCATED (huashu Chinese + open-design unknown but anti-slop framing prominent) — possible T1-design-skill vertical overfit
- "Anti-slop" boundary-vs-other-anti-LLM-framings not yet sharply defined (overlaps with anti-vibe-coding Pattern #51 + anti-magic-glue-app)
- v90 audit should pressure-test cross-vertical applicability (T2 Service? T3 Education? non-design verticals?)

**Confidence:** MEDIUM-HIGH. N=3 with formal 3-variant sub-typology + orthogonality-validation against Pattern #51 + co-occurrence-validation against Pattern #66/#82 + 3-arc-in-2-days promotion-arc-speed CORPUS-RECORD-TIE. Caveats above downgrade from HIGH to MEDIUM-HIGH.

**Audit document:** `04 Reviews/(C) 2026-05-22 Pattern Library mini-audit post-v83-v84-v85 (3-WIKI-DEFERRAL-CARRY-OVER + PROMOTION-DRIVEN + LARGEST batch corpus-history; Pattern #88 Anti-Slop NEW + Pattern #52 N=2 + Library-vocab #12 + #14 + 30 other items).md`

**Phase 4b proposal-document:** `03 Projects/open-design - Beginner Analysis/01 Analysis/(C) Anti-Slop-Design-Curation-N3-PROMOTION-LOCKED-IN-with-machinery-sub-typology.md`

---

## Pattern #52 sub-class N=2 PROMOTION at v86 audit (sub-class-only; Pattern #52 top-level already CONFIRMED via v75 audit)

### Pattern #52 Multi-Month-Sustained EXTREME-VIRAL sub-class — CONFIRMED N=2 at v86 audit

**Sub-class definition:** Pattern #52 (velocity-class) sub-class characterized by **stars-per-day > 300 AND sustained-window ≥ 90 days** — distinct from EXTREME-VIRAL pulse (>300/d × <90d short launch-window).

**Evidence at PROMOTION (N=2 cross-instance):**

- **v78 affaan-m/ECC** (N=1 anchor): 187,238 stars / 122 days = **1,535 stars/day** sustained over 4-month window. PROMOTION-LOCKED-IN at v85 audit deferred to v86.

- **v85 nextlevelbuilder/ui-ux-pro-max-skill** (N=2 confirmation): 81,352 stars / 174 days = **467 stars/day** sustained over 6-month window (LONGER sustenance than v78 anchor at 3.3× lower per-day rate).

**Cross-instance comparison:**

| Metric | v78 ECC | v85 ui-ux-pro-max | Ratio/Notes |
|--------|---------|-------------------|-------------|
| Stars/day | 1,535 | 467 | v78 much higher per-day rate (3.3×) |
| Sustained-days | 122 | 174 | v85 LONGER sustenance window |
| Total stars | 187K | 81K | v78 much higher absolute count |
| Owner archetype | Solo + community | VN org | Different archetypes |
| Vertical | Multi-Harness Operator System | T1 design-skill | Different T1 sub-archetypes |
| Velocity trajectory | Sustained high-magnitude | Sustained moderate-magnitude | Same sub-class, different magnitudes |

Both qualify under sub-class threshold (>300/d × ≥90d) but at DIFFERENT magnitudes within the sub-class.

**5-of-5 promotion criteria PASS HIGH-confidence:**

1. Cross-instance recurrence at N≥2 ✅ PASS
2. Sub-class threshold met ✅ PASS
3. Mechanism distinction from pulse-class ✅ PASS
4. Variant-within-pattern strengthening ✅ PASS
5. HIGH-confidence verdict ✅ PASS

**Pattern #52 sub-class taxonomy at v86 (formal 5-variant):**

1. EXTREME-VIRAL pulse (>300/d × <90d) — CONFIRMED
2. HIGH-NOT-EXTREME (150-300/d) — CONFIRMED (N=4 PROMOTED v75)
3. SUSTAINED-MODERATE-HIGH (25-150/d) — CONFIRMED
4. LONG-SUSTAINED-MEDIUM (60-150/d × 1000+d) — PROVISIONAL N=1 (v74 Raschka)
5. **Multi-Month-Sustained EXTREME-VIRAL (>300/d × 90+d) — CONFIRMED N=2 NEW at v86 (v78 + v85)**

**Honest dissent / caveats:**
- 3.3× velocity ratio across N=1 + N=2 = wide-magnitude range within single sub-class; v90 should pressure-test sustenance-definition (≥90 days at what cumulative-velocity?)
- Both instances in T1 territory (operator-system + design-skill) → possible T1-vertical overfit; cross-vertical applicability open at N=2
- Sustained-window definition is implicit; if last 60d of v85 dropped to 100/d, would that still qualify as "sustained"?

**Confidence:** HIGH (per 5-of-5 criteria PASS).

**Audit document:** `04 Reviews/(C) 2026-05-22 Pattern Library mini-audit post-v83-v84-v85 ...md`

**Phase 4b proposal-document:** `03 Projects/ui-ux-pro-max-skill - Beginner Analysis/01 Analysis/(C) Pattern-52-N2-Multi-Month-Sustained-EXTREME-VIRAL-promotion.md`

---

## Library-vocab items PROMOTED at v86 audit (3 items: #12 + #14 + #15)

### Library-vocab #12 LLM-routing artifacts — CONFIRMED N=5

5-variant taxonomy:
1. **NOTICE.md** (v75 impeccable) — 2-source derivative-attribution chain
2. **HARNESSES.md** (v75 impeccable) — harness-tolerance routing description
3. **AGENTS.md** (v76 agent-skills-standard) — 3-tier hierarchical-lookup router
4. **llms.txt** (v77 easy-vibe + v81 taste-skill, N=2 strengthening within item) — curriculum-stage / skill-bundle routing
5. **skill.json** (v85 ui-ux-pro-max-skill) — formal Claude-Code-skill manifest with 18-platform enumeration

### Library-vocab #14 Org-Brand-and-Product-Brand-Split via 2-Custom-Domain — CONFIRMED N=3

- v82 huashu-design: huasheng.ai + bookai.top
- v83 open-design: nexu.io + open-design.ai
- v85 ui-ux-pro-max-skill: nextlevelbuilder.io + uupm.cc

T1-design-skill + Asian-LOCATED overfit caveat applied; v90 cross-vertical pressure-test required.

### Library-vocab #15 Operator-Elected-Phase-0-9-Override-with-Honest-Documentation-Trail — CONFIRMED N=1 ONE-TIME-EXCEPTION

Codifies v84 OVERRIDE policy + ONE-TIME-EXCEPTION annotation:
- Override-trigger conditions: Phase 0.9 STRICT verdict = 0-PASS or 1-WEAK-only with operator force-build
- Override-artifact-trail: project CLAUDE.md OVERRIDE-block + Phase 4b proposal-document + root CLAUDE.md Storm Bear streak block
- Streak-notation: Option B2 "N+1*" format
- Override-frequency threshold: 2-in-20 wikis OR 3-in-30 wikis = v2.3 Phase 0.9 redesign trigger
- ONE-TIME-EXCEPTION annotation: v84 declared one-time; Phase 0.9 STRICT remains LOAD-BEARING; future 0-PASS defaults to SKIP

---

## QUADRUPLE PROMOTION at v101 1-WIKI-DEFERRAL-CARRY-OVER + PROMOTION-DRIVEN mini-audit (Pattern #84 84d + Library-vocab #20 Token-Economy-Quantification + T1 Domain-Vertical-Skill-Collection sub-archetype + Pattern #57 57k)

### Pattern #84 sub-typology 84d Hardware-Substrate-Tolerance — CONFIRMED at N=4 STRONGER

**Status at v101 audit (2026-05-28)**: PROMOTED to CONFIRMED Pattern #84 sub-typology (sibling-level to 84a Tool-tolerance + 84b Usage-enforcement + 84c Provider-Agnostic-By-Design).

**Definition**: Cross-vendor ecosystem-tolerance variant where the subject achieves tolerance ACROSS hardware/substrate boundaries (Apple Silicon MPS + WASM-software-substrate + native-macOS Apple-dev-toolchain + bundled fine-tuned models) rather than across vendor/distribution boundaries (84a/b/c).

**Evidence at PROMOTION (N=4 cross-substrate arc)**:

| Wiki | Subject | Substrate-tolerance mechanism | Sub-sub-mechanism |
|---|---|---|---|
| v79 (2026-05-20) | thu-vu92/autoresearch_folktales | Apple Silicon MPS (PyTorch + Metal) | **84d.1** PyTorch-MPS substrate-tolerance |
| v94 (2026-05-25) | Lum1104/Understand-Anything | WASM-Tree-sitter substrate-tolerance workaround | **84d.2** WASM-software-substrate |
| v97 (2026-05-25) | samuelfaj/distill | MLX-Apple-Silicon-native bundled fine-tuned model | **84d.3** MLX-Apple-native bundled-fine-tuned-model |
| v99 (2026-05-27) | manaflow-ai/cmux | native macOS Swift+AppKit + libghostty embed | **84d.4** Native-macOS-Apple-dev-toolchain with embedded-library |

**Cross-substrate spread**: 4-variant distinct substrate-tolerance mechanisms = full coverage of major macOS / cross-platform substrate-axes.

**Pattern #84 hierarchy after v101 promotion**:

```
Pattern #84 Cross-Vendor Ecosystem-Tolerance (top-level; PROMOTED v72)
├── 84a Tool-tolerance (v62)
├── 84b Usage-enforcement (v65)
├── 84c Provider-Agnostic-By-Design (PROMOTED v72)
│   ├── 84c.1 Marketplace-Plugin-Install (CONFIRMED v96 at N=6)
│   ├── 84c.2 CLI-Generated-Formats (PROVISIONAL N=2)
│   └── 84c.3 Provider-Agnostic via Log-Parsing at Observability Layer (PROVISIONAL N=1)
└── 84d Hardware-Substrate-Tolerance (CONFIRMED v101 at N=4 — NEW)
    ├── 84d.1 PyTorch-MPS substrate-tolerance (v79)
    ├── 84d.2 WASM-software-substrate-tolerance (v94)
    ├── 84d.3 MLX-Apple-native bundled-fine-tuned-model (v97)
    └── 84d.4 Native-macOS-Apple-dev-toolchain with embedded-library (v99)
```

**Distinction from 84c**: 84c provider-agnostic addresses vendor/distribution layer (which CLI/which IDE/which marketplace); 84d hardware-substrate-tolerance addresses hardware/substrate layer (which GPU/which compute-runtime/which OS-toolchain). Orthogonal measurement-axes within Pattern #84.

**Confidence**: HIGH. 4-instance arc + cross-substrate spread is structurally complete coverage of macOS-tier substrate axes. Note 84d is sibling-level to 84a/b/c (sub-typology layer), NOT sub-sub-mechanism within 84c.

**Promotion-arc velocity**: 4-instance arc within 38 calendar days (v79 2026-05-20 → v99 2026-05-27).

**Honest dissent / caveats**:
- All 4 instances at macOS-centric substrate-axes; cross-OS substrate-tolerance (Windows / Linux native) not represented at v101
- 84d.2 WASM-software-substrate is the structural outlier (software substrate vs hardware substrate); arguably belongs in distinct sub-sub-mechanism but per 4-variant promotion at N=4, retained within 84d taxonomy
- v105+ pressure-test required for cross-OS evidence (e.g. CUDA-NVIDIA substrate-tolerance subject)

**Audit document**: `04 Reviews/(C) 2026-05-28 Pattern Library mini-audit v101 (1-WIKI-DEFERRAL-CARRY-OVER + PROMOTION-DRIVEN; Pattern #84 84d + Token-Economy-Quantification + T1 Domain-Vertical-Skill-Collection + Pattern #57 57k QUADRUPLE PROMOTION + 46 other items).md`

---

### Library-vocab #20 Token-Economy-Quantification — CONFIRMED N=3

**Status at v101 audit (2026-05-28)**: PROMOTED to CONFIRMED Library-vocab item.

**Definition**: Explicit quantification of token-cost-impact as a primary design-discriminator axis at communication-style / runtime / data-structure layer — distinct from general "efficient design" framing because token-cost is explicitly named, quantified, and used as a primary comparison-axis for design-choice tradeoffs.

**Evidence at PROMOTION (3-axis cross-mechanism)**:

| Wiki | Subject | Mechanism-axis | Quantification |
|---|---|---|---|
| v87 (2026-05-22) | bsquang/claude-comstyle | composition-axis | per-style %-token-impact rating (65-75% fewer to +20-40% more) at 13-communication-style taxonomy |
| v97 (2026-05-25) | samuelfaj/distill | runtime-axis | product-level %-token-saving ("99% saved" claim; bundled-local-LLM compression pipeline) |
| v98 (2026-05-25) | mukul975/Anthropic-Cybersecurity-Skills | data-structure-axis | progressive-disclosure-per-skill (~30-tokens-scan + 500-2,000-tokens-full-load) at 754-skill scale |

**Cross-axis spread at N=3**:
- Cross-author: bsquang + samuelfaj + mukul975 (3 distinct authors)
- Cross-vertical: T1 Prompt-Style + T2 CLI-Service + T1 Domain-Vertical-Skill-Collection (3 distinct verticals)
- Cross-mechanism-axis: composition + runtime + data-structure (3 distinct quantification mechanisms)
- Cross-scale: 28★ + 559★ + 8,735★ (3-tier scale-stratification micro + low-mid + mid)

**Confidence**: HIGH. All cross-axis spread requirements PASS per routine v2.3 §2.

**Cross-references**:
- Library-vocab #18 Coupled-Design Density Not Scale-Dependent — orthogonal to #20; #18 measures pattern-density at single subject across scales; #20 measures token-cost-quantification as design-axis
- Pattern #66 Supply-Chain Isolation — overlaps at v98 (progressive-disclosure functions as supply-chain coverage discipline) but #20 is distinct measurement-axis (cost-quantification not trust-attribution)

**Honest dissent / caveats**:
- 3-axis evidence is structurally distinct but loose — composition (v87) + runtime (v97) + data-structure (v98) span 3 distinct architectural layers; could fragment into 3 separate Library-vocab items at v110+ if cross-axis observations diverge further
- v97 "99% saved" is a quantitative-marketing claim (Pattern #82); part of token-quantification is also marketing-framing; v105 pressure-test should distinguish design-discipline-quantification from marketing-claim-quantification

**Audit document**: `04 Reviews/(C) 2026-05-28 Pattern Library mini-audit v101 ...md`

---

### T1 Assistant Skill sub-archetype: Domain-Vertical-Skill-Collection — CONFIRMED at N=3

**Status at v101 audit (2026-05-28)**: PROMOTED to CONFIRMED T1 sub-archetype (administrative-only at N=3).

**Definition**: T1 Assistant Skill subjects that codify a complete domain-vertical via N-skill collection at single repo scope, with explicit per-skill metadata (frontmatter / SKILL.md / category mapping) and cross-skill routing artifact (AGENTS.md / _INDEX.md / similar).

**Evidence at PROMOTION (3-vertical cross-domain)**:

| Wiki | Subject | Domain-vertical | Skill count |
|---|---|---|---|
| v64 (2026-05-13) | claude-seo | SEO-vertical | ~24 skills |
| v90 (2026-05-22) | Imbad0202/academic-research-skills | academic-research-vertical | 4 nested versioned sub-skills × 42 agents |
| v98 (2026-05-25) | mukul975/Anthropic-Cybersecurity-Skills | cybersecurity-vertical | 754 skills × 26 domains × 26+ AI platforms |

**Cross-axis spread at N=3**:
- Cross-author: 3 distinct authors (claude-seo team + Imbad0202 + mukul975)
- Cross-vertical: 3 distinct domain-verticals (SEO + academic + cybersecurity)
- Cross-scale: ~24-skill / 4-nested-sub-skill-with-42-agents / 754-skill = 3-tier scale-stratification

**Confidence**: HIGH. Cross-vertical spread is the load-bearing criterion; 3 distinct verticals with explicit domain-codification at each.

**Distinction from other T1 sub-archetypes**:
- T1 single-artifact (v63 Karpathy + others): single skill or single methodology-package
- T1 design-language (v75 + v81 + v82 + v83 + v85): design-skill cluster at single subject
- T1 multi-skill-brand-portfolio (v81): N skills as brand-product variants
- T1 standards-layer (v76): standards-framework for N-domain
- T1 Domain-Vertical-Skill-Collection (THIS PROMOTION): N skills codifying a complete domain-vertical at single repo

**Honest dissent / caveats**:
- v90 academic-research-skills uses nested-versioned-sub-skill structure (4 sub-skills × 42 agents); structurally distinct from v64 single-tier + v98 single-tier-flat; sub-typology candidate at v105 if more nested-structure-subjects emerge
- All 3 evidence points use Claude-Code-skill format (`.claude/skills/` + SKILL.md); sub-archetype may be CC-skill-specific or generalize to other harness formats — v105 pressure-test

**Audit document**: `04 Reviews/(C) 2026-05-28 Pattern Library mini-audit v101 ...md`

---

### Pattern #57 sub-variant 57k Standards-Conformance-Layer Corpus-Recursive Chain (5-Implementer) — CONFIRMED at N=3 PROMOTION

**Status at v101 audit (2026-05-28)**: PROMOTED to CONFIRMED Pattern #57 sub-variant (first sub-variant PROMOTION to CONFIRMED within Pattern #57's sub-variant taxonomy).

**Definition**: Pattern #57 sub-variant where N implementers each conform to a shared external authoritative standard (here: agentskills.io standard with SKILL.md spec) — distinct from prior 57c-d-e-f-g-h-i-j sub-variants because recursion anchors at external standard-conformance layer (not at corpus-subject-as-anchor).

**Evidence at PROMOTION (5-implementer agentskills.io standard chain across 8 calendar days)**:

| Implementer | Wiki | Date | Vertical | Scale | Geography | Primary Language |
|---|---|---|---|---|---|---|
| HoangNguyen0403/agent-skills-standard (anchor; first third-party implementer) | v76 | 2026-05-19 | Standards-meta | 496★ | Hanoi Vietnam | TypeScript |
| anthropics/skills (authoritative reference; SKILL.md spec + template) | v93 | 2026-05-23 | Foundational-vendor reference | 139,442★ | Anthropic PBC SF | Python |
| mukul975/Anthropic-Cybersecurity-Skills | v98 | 2026-05-25 | Cybersecurity-vertical | 8,735★ | Berlin (Indian-diaspora) | Python |
| manaflow-ai/cmux | v99 | 2026-05-27 | Native-terminal-multiplexer-vertical | 19,853★ | SF | Swift |
| tisfeng/Easydict | v100 | 2026-05-27 | Translation-utility-vertical | 13,310★ | China-Mainland | Swift |

**Cross-axis spread at N=5** (well above N=3 threshold):
- Cross-author: 5 distinct authors
- Cross-vertical: 5 distinct verticals
- Cross-scale: 496★ → 139,442★ (~280× range)
- Cross-geography: 5 distinct geographies (Vietnam + SF + Berlin + SF + China-Mainland)
- Cross-language: 4 distinct primary languages (TypeScript + Python ×2 + Swift ×2)

**Promotion-arc velocity**: 5-implementer-in-8-calendar-days (v76 2026-05-19 → v100 2026-05-27). **CORPUS-FIRST in v60+ window for a standards-conformance-layer chain at this arc-velocity**.

**Confidence**: HIGH. All cross-axis spread requirements PASS robustly (N=5 well above N=3 threshold).

**Distinction from prior Pattern #57 sub-variants**:
- 57c-product (corpus-subject citation density): recursion at product-citation layer
- 57e (multi-source derivative attribution via NOTICE.md): recursion at attribution-chain layer
- 57f (anchor self-reference v78 ECC): recursion at same-subject-at-delta layer
- 57g (second-order derivative via intermediate adapter v79): recursion at derivative-chain layer
- 57h (reverse-engineering of anchor v82 huashu): recursion at reverse-engineering layer
- 57i (multi-tier corpus-recursive citation v83 open-design): recursion at multi-tier-citation density
- 57j (antigravity-corpus-recursive sub-chain v85): recursion at sub-chain layer
- **57k (standards-conformance 5-implementer chain v76→v100): recursion at EXTERNAL standard-conformance layer** = structurally distinct because anchor is external standard (agentskills.io) not corpus subject

**v2.4 codification candidate**: "Authoritative-Standard-Conformance Chain Rapid-Adoption Discipline" — 5-implementer arc within 8 calendar days suggests an unusually fast standards-adoption process worth formalizing as routine v2.4 observation.

**Honest dissent / caveats**:
- All 5 implementers chose agentskills.io standard specifically; the 5-implementer chain is contingent on this single standard's adoption pattern, not a generalizable phenomenon yet
- 8-calendar-day arc-velocity = unusually fast = possibly a "novelty-burst" rather than sustained adoption; v105+ N=6-7 watch will test sustained-adoption hypothesis
- Cross-language Swift-primary clustering at v99+v100 (both Swift) = possible same-substrate clustering bias

**Audit document**: `04 Reviews/(C) 2026-05-28 Pattern Library mini-audit v101 ...md`

---

## Promoted at v120 mini-audit (Pattern #18 sub-archetype #8 "Multi-Source LLM Aggregator")

**Promotion:** Pattern #18 **sub-archetype #8 "Multi-Source LLM Aggregator"** → **CONFIRMED N=3** (was PROVISIONAL N=2 since the v115 audit).

**Definition:** a tool whose core function is to put *multiple* LLM/coding-agent providers behind a single point of control, by one of two mechanisms:
- **8a — config-switcher:** rewrites a runtime config to switch the single *active* provider. Anchors: **v73 cc-switch** (Tauri-2 desktop; switches Claude Code providers) + **v117 CodexPlusPlus** (Tauri-2 desktop; rewrites `~/.codex/config.toml` to point Codex at a custom OpenAI-compatible endpoint). N=2.
- **8b — live-routing-proxy:** all providers live behind one endpoint with fallover/routing. Anchor: **v112 freellmapi** (headless OpenAI-compatible proxy aggregating ~12 free-tier providers). N=1.

**Evidence (N=3):** v73 (8a) + v112 (8b) + v117 (8a) — 3 authors, 2 sub-variants, 2 deployment models (desktop GUI vs headless proxy), 2 target agents (Claude Code vs Codex). Genuine cross-instance spread at the top-level "multi-source aggregation" claim.

**Honest caveat (recorded, does NOT block promotion):** both **8a** instances (v73 + v117) are **Tauri-2 desktop apps** — the *8a sub-variant* may be narrowing toward "Tauri-desktop config-switcher" (a possible stack-coincidence; tracked separately in the Library-vocab registry LV-C7 as the "Tauri-Desktop-Management-GUI" N=2 sub-claim). The **top-level #8** promotion is justified independently because 8b (v112, headless) supplies genuine mechanism + deployment diversity. If a 3rd 8a instance is again Tauri-desktop, revisit whether 8a should be relabeled. Promotion is at the #8 (sub-archetype) layer within the already-CONFIRMED Pattern #18 — **top-level confirmed-pattern count UNCHANGED at 46.**

**Relieves:** the v2.4-deferred "multi-runtime-aggregator (v73 N=1 only)" item (cleared at v115 → N=2; CONFIRMED here at N=3).

**Audit document**: `04 Reviews/(C) 2026-05-30 Pattern Library mini-audit v120 ...md`

---
