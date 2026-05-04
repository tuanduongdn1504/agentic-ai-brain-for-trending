# (C) Skyvern-AI Commercial Entity + Pattern 31 Promotion

> **Type:** Entity — organizational + licensing + pattern promotion
> **Parent:** [[(C) index]]
> **Sources:** README LICENSE + skyvern.com + corpus cross-ref
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Skyvern-AI = **commercial entity founded around product** (OSS core + Skyvern Cloud simultaneous). Matches fish-speech v20's 39 AI INC archetype (commercial-entity-with-OSS-core). Pattern #31 **Open-Core Commercial Entity validates at N=2** → PROMOTE to CONFIRMED. AGPL-3.0 license protects against SaaS appropriation while preserving community access; proprietary anti-bot measures provide commercial moat.

## 2. Organizational profile

### Known facts

- **GitHub org:** Skyvern-AI
- **Domain:** skyvern.com
- **Managed product:** app.skyvern.com (Skyvern Cloud)
- **Contact:** founders@skyvern.com (plural)
- **Community:** Discord + Twitter @skyvernai + LinkedIn + GitHub issues
- **Created:** 2024-02-28
- **Scale:** 21.3K stars in ~2 years

### Unknown / inferred

- Specific founder names (not disclosed in README)
- Incorporation (LLC/Inc not disclosed)
- VC/YC funding (neither mentioned nor denied)
- Team size (small/medium inferred from "founders")

### Archetype placement

**Commercial-entity + Cloud-product archetype** — maps to or refines existing archetype #9 (Commercial-foundation-model entity, fish-speech).

**Proposed archetype refinement:**
- **#9 Commercial-entity with OSS-core + proprietary commercial tier** (generalized from "foundation-model-specific")
- Covers fish-speech (foundation model domain) + Skyvern (T5 browser-agent domain)

## 3. Pattern #31 Open-Core Commercial Entity → PROMOTION

### State trajectory

| Version | Count | Evidence |
|---------|-------|----------|
| v20 (fish-speech) | N=1 | 39 AI INC + custom research-license + commercial paid tier |
| **v24 (Skyvern)** | **N=2** | **Skyvern-AI + AGPL-3.0 + Skyvern Cloud anti-bot proprietary** |

### Structural criteria at N=2

Both share:
- Commercial entity founded around product
- OSS core with restrictive license (custom non-OSI / AGPL)
- Proprietary commercial tier with domain-specific differentiator
- OSS as lead-gen + community + credibility
- Commercial tier as revenue
- Not community-to-commercial transition (commercial from inception)
- Distinct from pre-existing-corp-opens-source (a) / community-formalized-LLC (b) / pure-OSS solo (c)

### Cross-category validation

| Sub-type | Framework | Commercial differentiator |
|----------|-----------|---------------------------|
| Outside-scope foundation-model | fish-speech v20 | Commercial use license (vs research-only OSS) |
| T5 browser-agent | Skyvern v24 | Anti-bot detection (vs OSS without) |

**Pattern spans 2 scope categories** — structurally unambiguous at N=2.

### Promotion criteria check

- ✅ N=2 observations
- ✅ 2 distinct scope categories (foundation-model + T5)
- ✅ Structurally unambiguous (same organizational archetype, same OSS+commercial monetization)
- Meets "structurally unambiguous at N=2" criterion

### Recommendation

**Pattern #31 PROMOTE to CONFIRMED at v24 Phase 5.**

### Confirmed formal statement

> **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24):** Distinct organizational archetype for frameworks where a commercial entity founds both OSS product + proprietary commercial tier simultaneously (not community-to-commercial transition). OSS core uses restrictive license (custom non-OSI, AGPL, or similar) to protect against vendor appropriation while preserving community access. Proprietary tier adds domain-specific differentiator (anti-distillation / anti-bot / enterprise features) unavailable in OSS. Distinct from: (a) pre-existing-corp-opens-source, (b) community-formalized-LLC, (c) pure-OSS solo. Observed at N=2 across 2 scope categories (foundation-model fish-speech v20 + T5 browser-agent Skyvern v24). Monetization: OSS as lead-gen + community + credibility; Cloud/enterprise as revenue.

## 4. AGPL-3.0 as strategic license

### Strategic rationale

**Why AGPL-3.0 (not MIT/Apache)?**
- **SaaS-trigger clause** — closes "SaaS loophole" in GPL-3.0
- Cloud vendor wrapping Skyvern as paid SaaS must disclose source
- Skyvern-AI themselves can offer Cloud because they own the code + add proprietary anti-bot (not modified AGPL code; separate proprietary layer on top)

**Why not proprietary-only?**
- Community adoption + developer trust + lead generation
- Open-source signal for enterprise procurement
- Contribution pipeline

**AGPL = threading needle** between community-openness and commercial-protection.

### Alternative corpus reference

- **Unsloth Studio v23 (AGPL-3.0 dual-license):** AGPL applied to UI component only; Apache core for library
- **Skyvern v24 (AGPL-3.0 single-license):** AGPL applied to entire repo; proprietary cloud is separate codebase

**Different strategies, same AGPL foundation.**

## 5. Pattern #29 License-Category Diversity — strengthening

### AGPL-3.0 corpus count

| # | Wiki | AGPL scope |
|---|------|-----------|
| 1 | Unsloth Studio v23 | UI component (dual-license) |
| 2 | **Skyvern v24** | **Full OSS repo (single-license)** |

### Non-permissive corpus post-v24

| License | Count | Wikis |
|---------|-------|-------|
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| AGPL-3.0 | 2 | Unsloth Studio v23 + Skyvern v24 |
| Custom non-OSI | 1 | fish-speech v20 |
| **Total non-permissive** | **5** | **21% of 24 wikis** |

**Non-permissive adoption accelerating** — 5 of 24 wikis = meaningful minority.

## 6. Pattern #46 Duo-Founder test (weak)

### Evidence

- **Unsloth v23:** Daniel Han + Michael Han + Unsloth team — named, explicit
- **Skyvern v24:** `founders@skyvern.com` plural — unnamed, inferred

### Verdict

**Stays candidate N=1** — Skyvern founders unnamed; inference not strong enough for N=2 validation. Weak strengthening only.

**Watch for:** Skyvern blog post / LinkedIn reveal of founder names. If duo confirmed, N=2 for Pattern #46.

## 7. Pattern #45 Dual-Licensing — Skyvern does NOT match

### Distinction

**Pattern #45 Dual-Licensing Strategy (Unsloth v23):**
- Same codebase, different licenses for different components
- Unsloth core = Apache-2.0 (permissive)
- Unsloth Studio = AGPL-3.0 (copyleft)
- Both components OSS-licensed

**Skyvern's structure:**
- OSS repo = AGPL-3.0 (single license, entire codebase)
- Skyvern Cloud = proprietary (separate codebase, closed-source)
- Not dual-license — **open-core** (Pattern #31)

### Clarification

- **Dual-license (Pattern #45):** multiple OSS licenses within single product
- **Open-core (Pattern #31):** OSS core + proprietary commercial extensions

**Pattern #31 and Pattern #45 are distinct structural patterns.** Skyvern = Pattern #31. Unsloth = both #31 (Apache core + AGPL UI is OSS dual-license) AND additionally open-core if they have proprietary Cloud tier (not disclosed in README).

**Actually** — Unsloth's case is more nuanced. Both AGPL-3.0 Studio and Apache core are OSS; no proprietary commercial tier disclosed. So Unsloth is **dual-license OSS** (Pattern #45), not open-core (Pattern #31). Skyvern = Pattern #31 (open-core), not Pattern #45.

**Two clean patterns.** Clarifies scope.

## 8. Anti-bot proprietary moat (Pattern #48 candidate)

### Commercial differentiator

Skyvern Cloud provides:
- **Anti-bot detection bypass** — Cloudflare / Akamai / reCAPTCHA / DataDome
- **Proxy networks** — IP rotation
- **CAPTCHA solvers**
- **Behavioral humanization**

OSS users hit bot-detection on commercial sites; Cloud users don't. Direct revenue driver.

### Pattern #48 registration

> **Pattern #48 Proprietary-Anti-Bot Commercial Moat (CANDIDATE N=1):** Open-core browser-automation frameworks use proprietary anti-bot measures as commercial differentiator. OSS core handles ideal-case automation; commercial Cloud handles adversarial-case (bot-detection) automation. Specific to browser-automation T5 sub-specialty.

### Validation path

Monitor for similar structures in competing browser-agent frameworks (browser-use, Agent-E, LaVague) as they commercialize. N=2 required.

## 9. Corpus archetype inventory post-v24

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
| 9 | **Commercial-entity with OSS-core + proprietary tier** (generalized) | **39 AI INC (fish-speech v20) + Skyvern-AI (v24)** |
| 10 | Duo-founder + team | Han brothers (Unsloth v23) |

**v24 observation:** Archetype #9 generalizes from foundation-model-specific to cross-scope (covers T5 browser-agent). Same archetype, 2 scope categories.

## 10. Edges + limitations

### Known limitations

- **Founders anonymous** — no names disclosed publicly
- **Funding unclear** — VC/YC/bootstrap status not in README
- **Anti-bot ethics** — bypassing bot-detection may violate TOS of target sites (Storm Bear operators should review use-case legality)
- **AGPL compliance complexity** — internal enterprise deployment may trigger source-disclosure (ambiguous)

## 11. Related concepts

- [[(C) Vision-DOM-Free Browser Automation + WebBench Benchmarks]] — methodology context
- [[(C) BabyAGI AutoGPT Lineage + Pattern 19 Community-Viral Strengthening]] — lineage
- [[(C) T5 Extends to N=4 + 4 Archetypes + Pattern Analysis]] — tier meta
- fish-speech v20 — Pattern #31 co-validator
- Unsloth v23 — AGPL peer (different license strategy)
- Parent: [[(C) index]]

## References

- README LICENSE section
- skyvern.com + app.skyvern.com (product)
- Corpus cross-reference

---

**Skyvern-AI commercial entity with OSS core + Skyvern Cloud proprietary tier. AGPL-3.0 protects against SaaS appropriation; proprietary anti-bot = commercial moat. Validates Pattern #31 Open-Core Commercial Entity at N=2 (with fish-speech v20) → PROMOTE to CONFIRMED. Pattern #29 AGPL N=2. Pattern #48 Anti-Bot Moat candidate registered. Pattern #45 Dual-Licensing distinction clarified (Skyvern = open-core, not dual-license).**
