# (C) All Hands AI Team + Open-Core Commercial + Governance

> **Entity type:** Organizational entity (the company + founders + governance)
> **Wiki:** v30 OpenHands
> **Source grounding:** COMMUNITY.md + openhands.dev product/company page + ICLR 2025 + Nov 2025 SDK paper author lists
> **Status:** Entity page complete

---

## 1. Identity

**All Hands AI** is the commercial entity wrapping the OpenHands OSS project. It satisfies the 4 criteria of Pattern #31 Open-Core Commercial Entity (confirmed v24) and strengthens that pattern from N=2 to N=3 at v30.

The company is uniquely structured in the Storm Bear corpus as an **academic-commercial fusion** — 3 named co-founders spanning UIUC + CMU + industry, backed by $18.8M in disclosed funding, publishing peer-reviewed research at top ML venues while running a revenue-generating enterprise tier.

## 2. Founders (named in COMMUNITY.md)

### Xingyao Wang

- **Academic affiliation:** UIUC PhD candidate (per COMMUNITY.md)
- **Research credentials:** SWE-bench research contributor (per COMMUNITY.md)
- **Likely commercial role:** Co-founder + Research/CTO lead (1st author on both ICLR 2025 + Nov 2025 SDK papers)
- **Corpus-level significance:** First academic-PhD-candidate-co-founder in Storm Bear corpus (prior [v22 LlamaFactory hiyouga](../../../LlamaFactory%20-%20Beginner%20Analysis/) = solo academic-lab affiliation; v30 OpenHands = PhD + faculty combo)

### Graham Neubig

- **Academic affiliation:** CMU Professor (tenured faculty, per COMMUNITY.md)
- **Research credentials:** Multiple first-tier NLP/ML publications (public record at CMU NLP)
- **Commercial role:** Co-founder + Research advisor (senior author position on ICLR 2025 paper)
- **Corpus-level significance:** First tenured-faculty-co-founder in Storm Bear corpus. Tenure provides institutional stability orthogonal to startup risk.

### Robert Brennan

- **Primary affiliation:** Software engineering industry (per COMMUNITY.md — no academic credentials listed)
- **Role:** Co-founder + Engineering lead (inferred — balances academic co-founders with shipping discipline)
- **Corpus-level significance:** Completes the academic-commercial-fusion triangle (theorist + researcher + engineer)

## 3. Paper co-authors — research lineage strength

### ICLR 2025 paper (23+ co-authors)

Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig

### Nov 2025 SDK paper (11 co-authors)

Xingyao Wang, Simon Rosenberg, Juan Michelini, Calvin Smith, Hoang Tran, Engel Nyst, Rohit Malhotra, Xuhui Zhou, Valerie Chen, Robert Brennan, Graham Neubig

### Authors appearing on BOTH papers

- Xingyao Wang (1st author both)
- Hoang (H.) Tran (v2407 "Hoang H. Tran" / v2511 "Hoang Tran" — likely same person)
- Robert Brennan
- Graham Neubig

**Corpus observation:** 4-person persistence across 2 papers spanning 16 months = stable academic-commercial core team.

**Non-overlapping authors:**
- ICLR 2025-only (19+): likely spans multiple institutions (CMU + UIUC + research labs + other universities — affiliations not retrieved in WebFetch)
- Nov 2025 SDK-only (7): likely All Hands AI employees + close collaborators

## 4. All Hands AI as corporate entity

### Corporate facts retrieved

| Fact | Source | Verification status |
|------|--------|-------------------|
| Company name "All Hands AI" | openhands.dev | ✅ Verified |
| Product: OpenHands OSS + Cloud + Enterprise | README + openhands.dev | ✅ Verified |
| $18.8M funding disclosed | openhands.dev testimonial section (WebFetch) | 🟡 Unverified by filing; disclosed publicly |
| Location / HQ | Not retrieved | ❌ To verify |
| Year founded | Not retrieved | 🟡 Inferred 2024 (OpenDevin paper submission July 2024 + OpenDevin→OpenHands rebrand) |
| Legal entity type (LLC / Inc / C-corp) | Not retrieved | ❌ To verify |
| Investors / VC | Not specified in retrieved pages | ❌ To verify |

**Honest uncertainty:** Several corporate facts are not retrievable from public probe — flagged per CLAUDE.md NEVER fabricate rule.

### Open-core structure

**OSS core (MIT-licensed):**
- `openhands` — main OSS codebase
- `agent-server` Docker images
- SDK (`software-agent-sdk`)
- CLI

**Separate-license enterprise directory:**
- Enterprise features (Kubernetes deployment / RBAC / Slack+Jira+Linear integrations / multi-user collaboration)
- License: NOT MIT (unspecified; likely proprietary commercial-license)
- GitHub repo license field shows `NOASSERTION` — reflects split-license structure

**Corpus comparison — license splits:**
- [v20 fish-speech](../../../fish-speech%20-%20Beginner%20Analysis/): Custom non-OSI (single license, research-only gate)
- [v23 Unsloth](../../../Unsloth%20-%20Beginner%20Analysis/): Apache-2.0 core + AGPL Studio UI (dual-OSS, Pattern #45)
- [v24 Skyvern](../../../Skyvern%20-%20Beginner%20Analysis/): AGPL-3.0 OSS + Skyvern Cloud proprietary
- **v30 OpenHands:** **MIT core + separate-license enterprise dir (in-repo split)**

v30 OpenHands' in-repo dual-licensing by directory is **novel in corpus** — all prior examples split by product/service boundary, not by directory within same repo.

## 5. Pattern #31 Open-Core Commercial Entity — N=3 strengthening

### Satisfies all 4 confirmed-pattern criteria

1. ✅ **Commercial entity founded around product** — All Hands AI founded alongside OpenHands (not community-to-commercial transition; OpenDevin→OpenHands rebrand aligns with commercial launch)
2. ✅ **OSS core with standard/permissive license** — MIT (more permissive than fish-speech custom or Skyvern AGPL; still open-core-compatible)
3. ✅ **Proprietary commercial tier with domain-specific differentiator** — Enterprise tier Kubernetes + RBAC + Slack/Jira/Linear
4. ✅ **OSS as lead-gen + credibility + commercial tier as revenue** — explicit openhands.dev positioning

### Sub-type diversity at Pattern #31 N=3

| # | Wiki | Scope | License variant |
|---|------|-------|----------------|
| 1 | v20 fish-speech | Outside-scope foundation-model | Custom non-OSI |
| 2 | v24 Skyvern | T5 browser-agent | AGPL-3.0 single |
| 3 | **v30 OpenHands** | **T5 SWE-agent** | **MIT core + separate enterprise** |

Pattern #31 now has **3 distinct scope sub-types + 3 license variants** at N=3 — broadening structural validity.

## 6. Community governance — benevolent dictator model

### Core values (COMMUNITY.md verbatim)

- **High Openness:** *"We welcome anyone and everyone into our community by default."*
- **High Agency:** *"Members are encouraged to contribute through PRs, events, feedback, or questions."*

### Governance structure

- **Benevolent dictator model** — explicit in COMMUNITY.md
- **Transparent planning** — *"our plans, our work, our successes, and our failures are all public record"*
- **Slack primary channel** — `dub.sh/openhands`
- **Open participation framing** — *"engineers, academics, and enthusiasts reimagining software development for an AI-powered world"*

### Corpus-level significance — first explicit BDM at scale

| Framework | Governance model |
|-----------|------------------|
| v11 BMAD | Commercial LLC + community contributions (no formal doc) |
| v13 gws | Official Google corporate |
| v17 spec-kit | Official GitHub/Microsoft + 9-article constitution |
| v22 LlamaFactory | Solo maintainer (implicit BDM) |
| **v30 OpenHands** | **Explicit benevolent dictator model (documented in COMMUNITY.md)** |

v30 is **first corpus wiki with explicit BDM documentation at 71.7K stars scale.** Prior BDMs were solo-implicit (codymaster / graphify / crawl4ai) or corporate-formal (spec-kit / gws).

## 7. Adoption claim — "Trusted Users"

### Named in README

TikTok, VMware, Amazon, Netflix, Google, NVIDIA, Apple

### Interpretation

**Established by this evidence:**
- Some form of deployment at each named organization
- Company confidence to publish the list (marketing claim, likely permissioned)

**Not established:**
- Scale of deployment (pilot vs org-wide)
- Revenue from any specific named user
- Whether usage is open-source self-hosted or paid enterprise tier

**Corpus-level significance:** First T5 wiki with named FAANG+ enterprise adoption. Prior T5 peers had internal (ByteDance deer-flow) or no-named users (paperclip / Skyvern).

## 8. Adoption + scale metrics

- **71.7K stars** (#5 in corpus) in 25 months = ~2,867 stars/month
- **9,030 forks** (12.6% — high engagement ratio)
- **101 releases** (active velocity)
- **2.1K contributions + 188+ contributors** (ICLR 2025 paper data)
- **315 MB repo** (largest T5 by 2×+)
- **433 watchers** (high-engagement subscriber count)
- **410 open issues** (substantial; reflects active bug-reporting community vs stale project)

## 9. Storm Bear operator takeaway

**For evaluating OpenHands adoption:**
- **Pros:** Commercial entity stability ($18.8M + 3 co-founders + 2 peer-reviewed papers) + MIT core + ICLR 2025 credibility + named enterprise users
- **Cons:** Early-stage startup funding risk + no Vietnamese localization + benevolent-dictator continuity depends on 3-person core
- **Use case fit:** Review PRs / Triage Incidents / Migrate Code workflows align with Scrum engineering team support
- **Adoption path:** Start with OSS self-hosted Docker → consider Cloud free tier if GitHub integration needed → enterprise only if multi-team VN client

## 10. References

- `COMMUNITY.md` (OpenHands/OpenHands)
- openhands.dev (company product + mission page)
- ICLR 2025 paper: arXiv 2407.16741
- SDK paper: arXiv 2511.03690 (Nov 5, 2025)
- GitHub API: `api.github.com/repos/OpenHands/OpenHands`
- Sibling entity: [(C) Action-Observation Agent Loop + Docker Sandbox + SDK](./(C)%20Action-Observation%20Agent%20Loop%20+%20Docker%20Sandbox%20+%20SDK.md)
- Sibling entity: [(C) Pattern 31 42 44 Strengthening + Academic-Commercial Fusion Archetype](./(C)%20Pattern%2031%2042%2044%20Strengthening%20+%20Academic-Commercial%20Fusion%20Archetype.md)
- Sibling cluster: [(C) Cluster — All Hands AI + research lineage + community](./(C)%20Cluster%20—%20All%20Hands%20AI%20+%20research%20lineage%20+%20community.md)
