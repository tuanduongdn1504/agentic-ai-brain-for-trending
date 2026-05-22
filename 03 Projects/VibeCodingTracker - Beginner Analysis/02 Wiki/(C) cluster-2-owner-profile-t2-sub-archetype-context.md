# (C) Cluster 2 — Owner profile Wei Lee + T2 Service tier sub-archetype N=4 context

**Source**: [GitHub profile `Mai0313`](https://github.com/Mai0313) (fetched 2026-05-22) + corpus state references for T2 Service tier prior instances v66 + v70 + v85.

## Owner profile — Wei Lee (Mai0313)

| Field | Value |
|---|---|
| GitHub username | Mai0313 |
| Full name | **Wei Lee** |
| Bio | *"SWE @google | Formerly @mediatek"* + interests: *"firmware + AI/ML + multi-agent systems + open source"* |
| Current role | **Google SWE — Firmware for Pixel SoCs (TF-A/RF-A)** |
| Previous role | **MediaTek ML Engineer — AI for semiconductor design** |
| Organization | Google (current); MediaTek (former) |
| Location | Not explicit in profile |
| Website | Not visible |
| Followers / Following | 11 / 4 |
| Public repos | 39 |
| Packages | 41 |
| Stars-collected | 272 |

### Achievement badges (signal-rich)

- **Arctic Code Vault Contributor** (GitHub's 2020 snapshot — author was active by 2019-2020 = multi-year track record)
- **Galaxy Brain** (high-quality answers in Discussions)
- **Pair Extraordinaire (×2)** (collaborative commit signal)
- **Pull Shark (×3)** (multiple merged PR signal)
- **Quickdraw** (fast issue/PR-handling)
- **YOLO** (commit without PR; solo-development signal)
- **Public Sponsor** (sponsors other OSS authors — community-investment signal)
- **Developer Program Member, Pro tier** (GitHub Pro subscription)

This is a **senior-tech-community-engagement profile** — multiple multi-instance achievements + Public Sponsor + Pro tier = sustained investment in OSS ecosystem.

### Top pinned repositories (engagement signal)

| Repo | Stars | Note |
|---|---|---|
| **microsoft/autogen** | 58.3k | Pinned (likely contributor or heavy user) |
| **ag2ai/ag2** | 4.6k | Pinned (the "Open-Source AgentOS" — successor/fork of autogen) |
| **langchain-ai/langchain** | 137k | Pinned (the major LLM-framework) |

3 of his top pins are **major multi-agent / LLM frameworks**. Matches bio interest in "multi-agent systems". This indicates **deep engagement with the agentic-AI framework ecosystem** — not just a user but likely a contributor or close-observer of these projects.

This profile context **strengthens vct as authentically grounded**: an author who pins autogen + ag2 + langchain and builds an observability tool for AI-coding-agents is building from a position of deep ecosystem familiarity.

### Technical stack (polyglot)

C + Python + Rust + TypeScript + Go + Shell visible in repo language stats. **6-language polyglot** — consistent with senior-corporate-engineer profile (Google SWE working on Pixel firmware would touch C + Shell + Python + possibly Rust/Go for tooling; AI/ML background adds Python + TypeScript framework familiarity).

### Taiwan-or-Chinese-ethnic-background inference

Multiple signals:
1. **Chinese name "Wei Lee"** (李偉 / 李為 / common transliteration)
2. **MediaTek background** — Taiwan-based semiconductor giant; while MediaTek employs international staff, Taiwan-origin is statistically dominant
3. **Traditional Chinese (zh-TW) README** — author maintains Traditional Chinese as a first-class locale = serves Taiwan/HK readers natively
4. **Simplified Chinese (zh-CN) README** — author also serves Mainland China readers
5. **GH handle "Mai0313"** — "Mai" common Chinese-surname romanization

**Strongly inferred: Taiwanese-or-Chinese-diaspora-ethnic-background**. Cannot be conclusively determined without explicit location field, but the evidence is convergent. For Phase 0.9 (a) purposes, **STRONG cultural-peer signal in Asian-LOCATED cluster** (NOT VN-direct; distinct corporate-engineer profile type).

### Pattern #19 sub-mechanism candidate — NOT registered at v89

A "Taiwan-tech-corporate-engineer-with-deep-multi-agent-framework-engagement" sub-mechanism candidate exists at the observational level — but it is **NOT registered as a formal Pattern #19 sub-mechanism candidate at v89**.

**Rationale**: Pattern #19's PROVISIONAL N=1 graveyard reached 12 candidates after v88 (with 11 still at N=1). Adding another candidate would worsen to 13 and further increase v90 CONSOLIDATION pressure that was already CRITICAL at v88.

**Operational decision**: log Wei Lee profile as observation in this wiki for v90 audit reference, but do NOT register as formal sub-mechanism. v90 CONSOLIDATION proposal (5-VN-sub-mechanisms → 1 unified "VN-Community Multi-Profile-Type" sub-mechanism CONFIRMED N=5) takes precedence over additional candidate registration.

This demonstrates **disciplined restraint on candidate-layer growth** when graveyard accumulation outpaces sub-mechanism consolidation — itself a routine v2.3 codification candidate ("Candidate-Layer Growth-Restraint Discipline").

## T2 Service tier sub-archetype N=4 context

v89 is the **4th T2 Service in 89-wiki corpus + 4th distinct sub-archetype**:

| Wiki | Subject | T2 sub-archetype |
|---|---|---|
| v66 | agentmemory | Memory/Persistence backend for agents |
| v70 | codegraph | Code-Indexing / Knowledge-Graph for AI-coding-agents |
| v85 | ui-ux-pro-max-skill | Design-Skill / Design-Language Service |
| **v89** | **VibeCodingTracker** | **Observability/Metering Tool — AI-agent usage + cost-tracking** |

**T2 Service tier reaches N=4 sub-archetype diversity at v89**. This is structurally significant:

| Tier | Sub-archetype diversity in v60+ window |
|---|---|
| T1 Assistant Skill | 5+ sub-archetypes (design-skill cluster v75/v81/v82/v83/v85 + standards-layer v76 + multi-skill-portfolio v81 + linear-workflow-pipeline v84 + prompt-style-library v87 + ...) |
| T2 Service | **4 sub-archetypes** (v66 + v70 + v85 + v89) — concentrated diversity |
| T3 Education | 3+ sub-archetypes (v74 educational-book-companion + v77 community-curriculum + ...) |
| T4 Bridge | 3 sub-archetypes formalization-candidate at v90 (v62 + v67 + v88) |
| T5 Application | sub-archetypes from v9 + v80 |

T2 Service tier sub-archetype diversity is the 2nd-richest in v60+ window after T1 Assistant Skill — but T2 is structurally more diverse (memory + indexing + design + observability span 4 fundamentally different functional domains, vs T1's mostly-design-skill cluster).

### Comparison across T2 sub-archetypes

| Wiki | Tier | Primary lang | Distribution | Operates-as |
|---|---|---|---|---|
| v66 agentmemory | T2 | TypeScript | npm | Backend service (agent calls into it) |
| v70 codegraph | T2 | TypeScript | CLI + index store | Backend service (agent queries it) |
| v85 ui-ux-pro-max | T2 | Python | npx + skill bundle | Skill bundle (agent uses it) |
| **v89 vct** | **T2** | **Rust** | **5-registry CLI** | **Operator-facing CLI (NOT agent-facing)** |

v89 introduces a **novel T2 axis**: the tool operates at the **operator layer** (the developer runs vct themselves) rather than at the **agent layer** (agents consume the T2 service). This is structurally distinct from v66 + v70 + v85 which are all agent-consumed.

The **operator-facing T2 axis** opens a new sub-typology dimension. Future N=2 evidence (e.g. another developer-facing observability/monitoring tool for AI-agents) would justify formalizing operator-facing-T2 as a sub-typology.

## 7-wiki Asian-LOCATED cluster + 5-wiki VN sub-cluster (unchanged at v89)

**Asian-LOCATED cluster progression**:

| Position | Wiki | Subject | Locale | Profile |
|---|---|---|---|---|
| 1 | v76 | agent-skills-standard | VN-Hanoi explicit | Senior SE employed |
| 2 | v80 | SmartMacroAI | VN-Hanoi explicit | Solo freelance |
| 3 | v82 | huashu-design | China-Mainland | Solo influencer |
| 4 | v85 | ui-ux-pro-max-skill | VN-org explicit | 6-month-old indie org |
| 5 | v87 | claude-comstyle | VN-solo inferred | Small-solo 2-product |
| 6 | v88 | teleport | VN-Hanoi explicit | Multi-org founder |
| **7** | **v89** | **VibeCodingTracker** | **Taiwan-or-Chinese-diaspora inferred** | **Google-SWE + ex-MediaTek senior corporate engineer** |

**Asian cluster at v89**: **7-wiki density = NEW CORPUS-RECORD-HIGH** (was 6 at v88).

**VN sub-cluster unchanged at 5-wiki** (v89 = Taiwan-or-diaspora, NOT VN-direct).

### Asian-cluster profile-diversity axis (extended at v89)

| Profile-type | Wiki anchors |
|---|---|
| VN-Hanoi employed Senior SE | v76 |
| VN-Hanoi solo freelance | v80 |
| China-Mainland solo influencer | v82 |
| VN-org indie | v85 |
| VN-solo small-portfolio | v87 |
| VN-Hanoi multi-org founder | v88 |
| **Taiwan-or-diaspora senior corporate engineer (Google + MediaTek)** | **v89 (NEW)** |

**7-profile-type-diversity within 7-wiki Asian cluster** = Library-vocab "Diverse Profile-Type Distribution within Single-Locale Cluster" strengthens to N=2 (v88 candidate + v89 strengthening with broader Asian-cluster scope).

## 4-consecutive clean Phase 0.9 PASS post-v84 OVERRIDE NEW CORPUS-RECORD

Streak progression:

| Wiki | Verdict | Streak |
|---|---|---|
| v84 image-blaster | OPERATOR-ELECTED OVERRIDE (one-time-exception) | 19+1*OVERRIDE |
| v85 ui-ux-pro-max-skill | STRONGEST 4/4 | 20+1* (1-consecutive clean) |
| v87 claude-comstyle | STRONG 3-4/4 with (b) STRONGEST | 21+1* (2-consecutive clean) |
| v88 teleport | STRONGEST 4/4 with (a)(b) STRONGEST | 22+1* (3-consecutive clean) |
| **v89 VibeCodingTracker** | **STRONG 3-4/4 (4× STRONG balanced)** | **23+1* (4-consecutive clean = NEW CORPUS-RECORD)** |

**Streak notation**: extends to **"23 PASS (v65-v83 + v85 + v87 + v88 + v89) + 1 OVERRIDE (v84) = '23+1*'"** (Option B2).

**25-instance window v65-v89**: 23 PASS / 1 OVERRIDE / 1 implied = **92.0% INCLUDE rate** (uptick from v88's 91.7%).

**Strength distribution v65-v89**: STRONGEST × 9 + STRONG × 6 (+v89) + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONG climbs from 5 to 6; STRONGEST still leads by 3).

**Override-frequency**: 1-in-25 = **well below** 2-in-20 / 3-in-30 v2.3-trigger thresholds. Operator-elected-override discipline holds robustly.

## v89 contributions summary

- 1 PRIMARY: NEW T2 sub-archetype "AI-Agent Observability/Metering Tool" PROVISIONAL N=1
- 6 NEW CORPUS-FIRST observations (Rust-primary T2 + LiteLLM cost-attribution + 5-distribution-channel + 3-locale Chinese-variant + high-release-cadence + log-parsing-observability sub-sub-mechanism)
- 7-wiki Asian-LOCATED cluster CORPUS-RECORD extension
- 4-consecutive-clean-PASS NEW CORPUS-RECORD streak extension
- 3 Library-vocab N=4 STRENGTHENING (Engagement-Deficit + Try-Once + Coupled-Design-Density-Not-Scale-Dependent)
- 0 Pattern #19 sub-mechanism candidates registered (graveyard discipline)
