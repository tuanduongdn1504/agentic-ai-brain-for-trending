# (C) Commercial-Entity + AGPL + Anti-Bot Moat Cluster Summary

> **Cluster:** Skyvern-AI organizational + AGPL-3.0 + proprietary-anti-bot commercial strategy
> **Parent:** [[(C) index]]
> **Sources:** README LICENSE + skyvern.com + contact info + corpus cross-ref
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Skyvern-AI commercial entity** — company founded with commercial Cloud product from day 1
2. **AGPL-3.0 license** — 2nd AGPL in corpus
3. **Anti-bot proprietary moat** — OSS core + closed commercial differentiator (Pattern #31 promotion evidence)

## 2. Skyvern-AI organizational profile

### Known facts

- **Organization:** Skyvern-AI (GitHub org)
- **Domain:** skyvern.com (commercial SaaS)
- **Contact:** `founders@skyvern.com` — **plural "founders"** (duo or small team)
- **Managed product:** Skyvern Cloud (app.skyvern.com)
- **Community:** Discord + Twitter @skyvernai + LinkedIn + GitHub issues
- Incorporation: unclear (LLC/Inc not disclosed publicly)
- VC/YC funding: unclear (neither explicitly mentioned nor denied)

### Inferred archetype

**Commercial-entity + founders team archetype:**
- Company founded around product (Skyvern Cloud day 1)
- OSS repo as community + lead-generation
- Proprietary cloud tier as revenue
- Plural "founders" = duo or small team
- Commercial from start (not community-to-commercial transition)

### Position in corpus archetype inventory

| # | Archetype | Example |
|---|-----------|---------|
| 1 | Solo-community | Various |
| 2 | Solo-known-figure | Karpathy / Jesse Vincent |
| 3 | Founder-personal | Garry Tan (gstack) |
| 4 | Community-unattributed | GSD |
| 5 | LLC-formalized | BMad Code LLC |
| 6 | Solo-VN-author | Tody Le (codymaster) |
| 7 | Official-corporate | GitHub, ByteDance, Google |
| 8 | Academic-lab | hiyouga + Lab4AI |
| 9 | Commercial-foundation-model | 39 AI INC (fish-speech) |
| 10 | Duo-founder + team | Han brothers (Unsloth) |
| **11** | **Commercial-entity + Cloud-product** | **Skyvern-AI** ← NEW v24 |

Alternatively, Skyvern maps to existing archetype #9 (Commercial-foundation-model → generalize to Commercial-entity-with-OSS-core). Arguably same archetype, different product category.

**Proposed refinement:** Rename archetype #9 to **"Commercial-entity with OSS-core + proprietary commercial tier"** — covers both fish-speech (foundation model) and Skyvern (browser agent).

## 3. Pattern #46 Duo-Founder + Team — test at v24

### Evidence strengthening?

- **Unsloth v23:** Daniel Han + Michael Han + team (named)
- **Skyvern v24:** `founders@skyvern.com` plural (unnamed, inferred duo+)

**Strength:** Weak strengthening — Skyvern founders unnamed, inference only.
**Verdict:** Stays candidate N=1 formally (Unsloth only explicit). Skyvern may be 2nd data point pending name confirmation.

## 4. AGPL-3.0 license

### License specifics

- **AGPL-3.0** applied to full OSS repo
- **Anti-bot measures** proprietary (Cloud-only, not AGPL)
- **Telemetry opt-out** via `SKYVERN_TELEMETRY=false`

### AGPL-3.0 implications

- **SaaS trigger:** Deploying modified Skyvern as network service requires source disclosure
- **Protects against:** Cloud vendor wrapping Skyvern as paid SaaS without publishing modifications
- **Skyvern's own Cloud:** They can offer it because they own the code + add proprietary anti-bot (not modified AGPL code; separate proprietary layer)

### Pattern #29 License-Category Diversity (confirmed v21)

**Corpus AGPL-3.0 count post-v24:**

| Wiki | AGPL scope |
|------|-----------|
| Unsloth v23 | Studio UI component only (dual-license w/ Apache core) |
| **Skyvern v24** | **Full OSS repo (single-license, 2nd AGPL in corpus)** |

**Non-permissive licenses post-v24:**

| License | Count | Wikis |
|---------|-------|-------|
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| **AGPL-3.0** | **2** | **Unsloth Studio v23 + Skyvern v24** |
| Custom non-OSI | 1 | fish-speech v20 |
| **Total non-permissive** | **5** | **21% of 24 wikis** |

**AGPL specifically N=2 now.**

## 5. Pattern #31 Open-Core Commercial Entity — PROMOTION candidate

### State trajectory

| Version | Count | Evidence |
|---------|-------|----------|
| v20 (fish-speech) | N=1 | 39 AI INC + custom research-license + commercial tier |
| **v24 (Skyvern)** | **N=2** | **Skyvern-AI + AGPL-3.0 + Skyvern Cloud anti-bot proprietary** |

### Structural match criteria

Both frameworks share:
- OSS core with restrictive license (commercial-restricted)
- Proprietary commercial tier with differentiator (model-training-restriction / anti-bot)
- Research-lab-origin OR product-origin commercial entity
- OSS serves as lead-generation for commercial tier
- Open-core monetization model

### Distinct from (a)/(b)/(c)

- **(a) Pre-existing-corp opens source** (gws/Google, spec-kit/GitHub, deer-flow/ByteDance) — company exists independently of OSS product
- **(b) Community-formalized-LLC** (BMad Code LLC) — community first, formalized later
- **(c) Pure-OSS solo** (most corpus) — no commercial tier

**Skyvern + fish-speech = (d) Commercial-entity-with-OSS-core-product** — company founded around OSS + commercial product together.

### Promotion criteria check

- ✅ N=2 observations
- ✅ Structurally unambiguous at N=2 (same commercial-entity-with-OSS-core pattern)
- ✅ Across 2 sub-types (foundation-model outside-scope + T5 browser-agent)
- Meets "structurally unambiguous at N=2" criterion

### Recommendation

**Pattern #31 PROMOTE to CONFIRMED at v24 Phase 5.**

### Refined formal statement

> **Open-Core Commercial Entity (Pattern #31, CONFIRMED v24):** Distinct organizational archetype for frameworks where a commercial entity founds both the OSS product + proprietary commercial tier simultaneously (not community-to-commercial transition). OSS core uses restrictive license (custom non-OSI / AGPL / similar) to protect against vendor appropriation while preserving community access. Proprietary tier adds domain-specific differentiator (anti-distillation / anti-bot / enterprise features) unavailable in OSS. Distinct from: (a) pre-existing-corp-opens-source, (b) community-formalized-LLC, (c) pure-OSS solo. Observed at N=2 across 2 scope categories (foundation-model fish-speech v20 + T5 browser-agent Skyvern v24). Monetization: OSS as lead-gen + community + credibility; Cloud/enterprise as revenue.

## 6. Anti-bot proprietary moat (Pattern #48 candidate)

### What anti-bot means

Commercial websites deploy bot-detection:
- **Cloudflare Turnstile / Bot Management**
- **Akamai Bot Manager**
- **Google reCAPTCHA / hCaptcha**
- **PerimeterX / DataDome**
- **Device fingerprinting**
- **Behavioral analysis**

Skyvern Cloud bypasses via:
- Proxy networks (IP diversity)
- CAPTCHA solvers
- Automated human-like behavior
- Headers + fingerprint management

### Pattern #48 candidate (NEW v24)

> **Proprietary-Anti-Bot Commercial Moat:** Open-core frameworks in browser-automation domain use proprietary anti-bot measures as commercial differentiator. OSS core handles ideal-case automation; commercial Cloud handles adversarial-case (bot-detection) automation. Specific to browser-automation T5 sub-specialty.

**Status:** N=1 at v24. Register as candidate.

**Validation path:** Other browser-agent frameworks (browser-use, Agent-E, LaVague) may follow open-core with anti-bot moat. Monitor.

## 7. BabyAGI + AutoGPT community-viral lineage

### Citation

> *"Skyvern was inspired by the Task-Driven autonomous agent design popularized by BabyAGI and AutoGPT"*

### Pattern #19 community-viral archetype sub-variant hypothesis

**Pattern #19 archetypes (current model):**
1. Individual-author lineage
2. Methodology-lineage
3. Community-viral (current: no-lineage sub-archetype)
4. Research-paper-chain

**v24 observation:** Skyvern is community-viral-**lineage** — references community-viral predecessors (BabyAGI/AutoGPT) rather than no-lineage. Hypothesis:

- **3a: Community-viral no-lineage** — agency-agents v18 Reddit-born, no acknowledged ancestors
- **3b: Community-viral lineage** — Skyvern v24 acknowledges BabyAGI/AutoGPT-style community-viral ancestors (meta-lineage)

### Status

Registration: candidate for Pattern #19 sub-refinement. N=1 at v24.

## 8. Storm Bear operator relevance

### Use cases

- **Jira/Linear status scraping** across teams (Scrum metric collection)
- **Retrospective template auto-fill** from multiple tools
- **Dashboard data extraction** (DORA metrics, velocity charts)
- **Enterprise SaaS data extraction** when API unavailable
- **Meeting-notes extraction** from SaaS tools

### Licensing caveat for Storm Bear

**AGPL-3.0 impact:**
- Local self-hosted Scrum coach use: ✅ OK (no SaaS deployment)
- Running as internal service for team: ⚠️ AGPL may require source disclosure to internal users (ambiguous case)
- Running as public SaaS: 🔴 Must disclose source

**If Storm Bear wants anti-bot:** Skyvern Cloud ($) required. Commercial anti-bot not in OSS.

### Verdict

Storm Bear relevance: **MEDIUM** — legitimate browser-automation tool, potentially useful for metric collection, but AGPL-3.0 + proprietary anti-bot creates friction. Pattern observation value HIGH; direct pilot value MEDIUM.

## 9. Key observations

### Cluster-level

- **Commercial-entity archetype** with Cloud product from day 1
- **AGPL-3.0 license** protects against SaaS appropriation
- **Proprietary anti-bot** = commercial differentiator
- **Open-core model** with 2nd data point in corpus

### Cross-corpus

- **Pattern #31 Open-Core Commercial Entity PROMOTES to CONFIRMED** at N=2
- **Pattern #29 License-Category Diversity** — AGPL now N=2 (Unsloth + Skyvern); non-permissive N=5
- **Pattern #19** community-viral lineage sub-variant hypothesis registered
- **Pattern #48 candidate** (Proprietary-Anti-Bot Commercial Moat) registered at N=1
- **Commercial-from-day-1 entity** = new/refined archetype (11th or refinement of 9th)

## 10. References

- Parent: [[(C) index]]
- Source: README + LICENSE + skyvern.com + Discord/Twitter
- Sibling clusters: [[(C) README + positioning + benchmarks cluster summary]] + [[(C) Workflow builder + LLM-abstraction + cloud cluster summary]]
- Open-core peer: fish-speech v20 (Pattern #31 co-validator)
- AGPL peer: Unsloth Studio v23 (Pattern #29 co-data-point)

---

**Cluster summary: Skyvern-AI commercial entity with Cloud product from day 1 + AGPL-3.0 single-license OSS core + proprietary anti-bot moat. Pattern #31 Open-Core Commercial Entity PROMOTES to CONFIRMED at N=2 (fish-speech + Skyvern). Pattern #29 AGPL N=2. Pattern #19 community-viral-lineage sub-variant hypothesis. Pattern #48 candidate (Anti-Bot Commercial Moat) registered.**
