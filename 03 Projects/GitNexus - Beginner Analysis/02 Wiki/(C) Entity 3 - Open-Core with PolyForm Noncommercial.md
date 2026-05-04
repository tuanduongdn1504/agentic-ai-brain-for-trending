# (C) Entity — Open-Core Structure with PolyForm Noncommercial License

> **Category:** Commercial-model + licensing
> **Tier:** T4 bridge (open-core economic structure)
> **Wiki:** v33
> **Date:** 2026-04-23

---

## 1. One-line summary

GitNexus operates as open-core with PolyForm Noncommercial 1.0.0 as the OSS-gate license and akonlabs.com as the commercial tier — introducing the first standardized non-OSI commercial-gate license to the Storm Bear corpus, extending Pattern #31 to 4 data points across 4 structurally-distinct license approaches, and anchoring new candidate Pattern #72 (PolyForm Noncommercial Commercial-Gate License).

## 2. PolyForm Noncommercial 1.0.0 — license mechanics

### Source
- **Origin:** polyformproject.org — collaborative project drafting license templates for non-OSI uses
- **Version 1.0.0** (not custom-written; standard family)
- **Related variants:** PolyForm Shield / PolyForm Small Business / PolyForm Strict / PolyForm Internal Use / PolyForm Free Trial

### What PolyForm Noncommercial 1.0.0 permits (free of charge)
- **"Any noncommercial purpose"**
- Personal uses: research, experiment, testing for public knowledge benefit; hobby projects; amateur pursuits
- Organizations qualifying as noncommercial: charities, educational institutions, government bodies (regardless of funding source)
- **Key qualifier:** absence of "anticipated commercial application"

### What PolyForm Noncommercial 1.0.0 restricts
- **All commercial use** — requires separate license agreement
- **Distribution commercial** — cannot sell software or derivatives
- **No sublicensing** — cannot transfer licenses

### Patent clause
- Patent license included for claims licensor can license
- **Termination on patent litigation** — license terminates if licensee claims software infringes any patent

### Derivative works
- Permitted under noncommercial purposes
- Commercial derivatives require separate agreement

## 3. Open-core structure

### OSS tier (free noncommercial)
- PolyForm Noncommercial 1.0.0
- Features: 14 languages + 16 MCP tools + 5 editor integrations + Sigstore Docker + K8s deployment + wiki generation + blast-radius + multi-file rename + process-grouped search

### Commercial tier (akonlabs.com Enterprise)
Delta from OSS (per README):
- **PR Review** — automated code review on PRs
- **Auto-updating code wiki** — continuous refresh
- **Auto-reindexing** — event-driven graph updates
- **Multi-repo support expanded** (OSS has group operations; Enterprise may have operational tooling around them)
- **OCaml support** — 15th language (OSS-gated)
- **Priority feature requests** — commercial support entitlement

### Commercial contact
- `founders@akonlabs.com` (plural — team)
- Discord: discord.gg/AAsRVT6fGb (separate from community Discord)
- **Website:** akonlabs.com (SaaS + Self-hosted options)

## 4. Structural position in Pattern #31 (CONFIRMED v24, N=3 post-v30)

### 4 data points post-v33

| # | Wiki | Version | Commercial entity | OSS license | Enterprise delta |
|---|------|---------|-------------------|-------------|------------------|
| 1 | fish-speech | v20 | 39 AI, INC. | Fish Audio Research License (custom non-OSI) | Commercial license required for commercial use |
| 2 | Skyvern | v24 | Skyvern-AI | AGPL-3.0 | Skyvern Cloud managed tier + proprietary anti-bot |
| 3 | OpenHands | v30 | All Hands AI | MIT + separate in-repo enterprise directory | Enterprise bundle in-repo + cloud managed |
| 4 | **GitNexus** | **v33** | **akonlabs.com** | **PolyForm Noncommercial 1.0.0** | **PR Review + auto-wiki + auto-reindex + OCaml + priority features** |

### 4 structurally-distinct license approaches now observed

| Approach | Mechanism | Example |
|----------|-----------|---------|
| Custom research-only | Bespoke-written license with research-only scope | fish-speech v20 |
| Network-copyleft | AGPL source-disclosure for network services | Skyvern v24 |
| Permissive + separate enterprise | MIT core + proprietary enterprise bundle in-repo | OpenHands v30 |
| **Standardized non-OSI commercial-gate** | **PolyForm Noncommercial 1.0.0 standard license + separate commercial agreement** | **GitNexus v33** |

### Cross-pattern diversity

Pattern #31 data points span:
- **4 scope contexts:** foundation-model (fish-speech) / browser-agent (Skyvern) / SWE-agent (OpenHands) / code-bridge (GitNexus)
- **4 license strategies:** custom-research / network-copyleft / permissive+enterprise / standard-noncommercial
- **4 commercial-tier mechanisms:** separate research-license / cloud-managed+proprietary / enterprise-bundle / enterprise-features-SaaS
- **4 commercial-entity archetypes:** single-product commercial (39 AI) / VC-funded commercial (Skyvern-AI) / academic-commercial fusion (All Hands AI UIUC+CMU) / independent commercial (akonlabs.com)

**Pattern #31 structurally validates at N=4 across 4 orthogonal axes** — robust CONFIRMED status.

## 5. Pattern #72 (NEW candidate — PolyForm Noncommercial Commercial-Gate License)

### Formal statement
PolyForm Noncommercial 1.0.0 is a standardized non-OSI license family specifically designed to gate commercial use while enabling noncommercial research, personal use, and qualifying organizations. Used as OSS-tier license with commercial-tier delivered via separate agreement.

### Registration status
- **NEW v33, N=1, stale-risk-flagged at registration** (per v2.1 Phase 0.5 discipline)
- **Distinct from:**
  - Pattern #29 License-Category Diversity (CONFIRMED v21) — diversity observation across categories
  - Pattern #33 Non-OSI Custom License (candidate) — custom-written licenses
  - Pattern #31 Open-Core Commercial Entity (CONFIRMED v24) — parent pattern (GitNexus strengthens #31 regardless)

### Rationale for registering as NEW
- PolyForm is STANDARDIZED license (polyformproject.org) — not custom-written (distinct from #33)
- Specifically DESIGNED for commercial-gating (unlike AGPL which gates through network-copyleft strategy)
- Emerging license-family approach in OSS ecosystem; corpus may see 2nd PolyForm-family adoption in future wikis

### Stale-risk trajectory
- **+5 wiki check:** v38 — re-evaluate if 2nd PolyForm-family observation emerges
- **+10 wiki retire:** v43 — retire if still N=1
- **Un-stale trigger:** any future PolyForm-family adoption OR similar standardized non-OSI family (PolyForm Shield / Small Business / Strict / etc.)

### Related candidate decisions not taken

- **NOT registered:** "Browser-native knowledge-graph runtime" (too niche; single observation)
- **NOT registered:** "Indian-Regional-Archetype-T4" (cross-tier premature; consolidation-forward deferred)
- **NOT registered:** "CS-student author archetype" (could be single-observation outlier; re-evaluate if 2nd CS-student framework)

## 6. Commercial entity profile — akonlabs.com

### Positioning
- SaaS + Self-hosted delivery models
- Team attribution: `founders@akonlabs.com` (plural)
- Separate Discord for commercial inquiries
- Website: akonlabs.com (referenced in README, not deep-probed)

### Archetype
- **Independent commercial entity** (not VC-funded disclosed; not academic-fusion disclosed)
- **Single-product company** — akonlabs monetizes GitNexus Enterprise tier
- **Founder-led** (Abhigyan + possibly co-founders; "founders@" plural suggests 2+)

### Relationship to OSS project
- OSS GitNexus is PolyForm Noncommercial
- akonlabs Enterprise is closed commercial offering
- **Same product, different tier** — NOT separate companion platform (like getdesign.md v25)
- Pattern #31 open-core architecture (not Pattern #50 commercial-funnel companion)

### Maturity signals
- Dedicated commercial Discord
- `founders@` email suggests incorporated entity
- Website exists (referenced; not fully probed)
- **Early-stage signals:** no public disclosed team size; no public funding announcements; repo is primary traffic driver

### Comparison with prior open-core entities

| Entity | Wiki | Size | Relationship to OSS |
|--------|------|------|---------------------|
| 39 AI, INC. | fish-speech v20 | Unknown; Asian | Commercial derivative of OSS foundation model |
| Skyvern-AI | Skyvern v24 | VC-funded (not all details public) | Skyvern Cloud managed SaaS |
| All Hands AI | OpenHands v30 | Academic-commercial fusion (UIUC + CMU + industry) | Enterprise bundle in-repo + cloud |
| akonlabs | GitNexus v33 | Early-stage (few signals); founders-plural | Enterprise SaaS + Self-hosted, same product |

## 7. Commercial-gate mechanics

### Who pays?
- Users with "anticipated commercial application"
- Specifically: commercial software developers using GitNexus to build commercial products
- NOT: personal hobby coders, students, academic researchers, nonprofits, government

### What does "anticipated commercial application" mean?
- License text (per polyformproject.org) specifies: the absence of anticipated commercial application
- **Ambiguity:** "Anticipated" is judgment-call — does a student building a commercial side-project fall under commercial?
- **Safe interpretation:** if monetization via paid product/service is intended, pay for commercial license
- **Gray zone:** pre-revenue startup using GitNexus for personal developer productivity

### How to get a commercial license
- Contact `founders@akonlabs.com`
- Negotiate terms (not publicly disclosed; typical SaaS + Self-hosted pricing models)
- Separate agreement (not through GitHub Sponsors or standard e-commerce)

### Storm Bear operator implications
- **Personal vault exploration:** unambiguously permitted (hobby/personal use)
- **Paid Scrum consulting using vault:** likely commercial use — requires commercial license
- **Pre-revenue evaluation:** gray zone — if just evaluating, probably fine; if building commercial product, clarify with akonlabs
- **Recommended action:** email founders@akonlabs.com with specific use case before commercial adoption

## 8. Governance depth correlation (Pattern #12)

- akonlabs = early-stage commercial entity + solo CS-student-author
- **Governance remains solo-style** despite commercial-entity presence
- **Observation:** commercial-entity maturity affects OSS governance depth
- Microsoft (markitdown v28) corporate-heavy governance: CLA + COC + Security + Devcontainer
- akonlabs-solo-founder governance-light: CONTRIBUTING + LICENSE (no SECURITY / COC / AGENTS)
- **Pattern #12 refinement observation:** commercial-entity EXISTENCE doesn't automatically push governance depth; maturity of commercial entity matters

## 9. Cross-wiki references

- [[fish-speech - Beginner Analysis]] v20 — Pattern #31 #1 data point; custom research license
- [[Skyvern - Beginner Analysis]] v24 — Pattern #31 #2 data point; AGPL-3.0
- [[OpenHands - Beginner Analysis]] v30 — Pattern #31 #3 data point; MIT + enterprise directory
- [[Unsloth - Beginner Analysis]] v23 — Pattern #45 Dual-Licensing candidate (Apache core + AGPL UI); distinct from Pattern #31 and PolyForm
- [[TrendRadar - Beginner Analysis]] v19 — Pattern #29 License-Category Diversity GPL-3.0 data point
- [[system-prompts-leaks - Beginner Analysis]] v21 — Pattern #29 GPL-3.0 ambiguous-provenance observation

## 10. Pattern Library observations

- **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24, N=3 post-v30)** — **4TH DATA POINT (N=4)**; structural validation across 4 scope contexts + 4 license approaches + 4 commercial-tier mechanisms + 4 commercial-entity archetypes
- **Pattern #29 License-Category Diversity (CONFIRMED v21)** — PolyForm Noncommercial 1.0.0 extends license-category range (categories: MIT + Apache + ISC + GPL + AGPL + Fish-Audio-custom + PolyForm-Noncommercial)
- **Pattern #33 Non-OSI Custom License (candidate)** — GitNexus is NOT custom-license (PolyForm is standardized); does NOT strengthen #33; stays N=1 (fish-speech only)
- **Pattern #12 Governance Depth Correlates with Organization (CONFIRMED v13)** — observation: commercial-entity maturity affects governance depth; akonlabs early-stage = solo-style governance retained
- **Pattern #72 (NEW)** — PolyForm Noncommercial Commercial-Gate License; N=1 stale-risk-flagged at registration

## 11. Operator decision-tree

```
Am I using GitNexus?
├─ Personal exploration? → ✅ PolyForm OSS free
├─ Academic research? → ✅ PolyForm OSS free
├─ Nonprofit/charity/government? → ✅ PolyForm OSS free
├─ Commercial software development? → ⚠️ Commercial license required
│   └─ Contact founders@akonlabs.com
└─ Unclear? → ⚠️ Email to clarify
```

Storm Bear operator:
```
Am I using GitNexus for...
├─ Indexing Storm Bear vault for personal Claude Code workflow? → ✅ Free (personal use)
├─ Demonstrating vault knowledge-graph to readers of blog/wiki? → ✅ Free (amateur/hobby)
├─ Paid Scrum consulting where GitNexus informs client work? → ⚠️ Commercial; email akonlabs
├─ Packaging GitNexus-powered tool for sale? → ⚠️ Commercial license required
└─ Storm Bear knowledge-base as commercial product? → ⚠️ Clarify with akonlabs
```

## 12. Alternative OSS knowledge-graph tools

For operators needing commercial-friendly licensing:
- **graphify v16** — MIT, Python, no commercial gate
- **Custom tree-sitter + NetworkX stack** — build your own (effort-heavy)
- **Neo4j + embeddings** — commercial-friendly but setup-heavy

For operators wanting browser-native + MCP + willing to pay:
- **GitNexus + akonlabs.com Enterprise** — polished + supported

## 13. Long-term trajectory

### Indicators of commercial-entity maturity
- Separate commercial Discord ✓
- `founders@` plural email ✓
- Enterprise feature delta documented ✓
- Sigstore supply-chain signing ✓
- Active development + sustained ~3K stars/month ✓

### Indicators of commercial-entity early-stage
- No public team page ✓ (not disclosed)
- No public funding announcements ✓ (not disclosed)
- Single-product company ✓
- Solo-style OSS governance ✓
- Young project (8.5 months) ✓

### Risk factors
- **Author bus factor:** Abhigyan solo-student; mitigated partially by akonlabs team
- **Commercial-entity dissolution risk:** early-stage; could pivot / shutter; OSS project remains but commercial support disappears
- **PolyForm Noncommercial license durability:** license is version-pinned (1.0.0); future PolyForm versions could adjust terms

## 14. Meta-observations

- **PolyForm Noncommercial is NEW category** — first standardized non-OSI commercial-gate in corpus
- **License ecosystem is maturing** — custom-license (fish-speech) → network-copyleft (AGPL) → permissive+enterprise (MIT+dir) → **standardized non-OSI family (PolyForm)** represents 4-point progression of commercial-gate strategies
- **Pattern #31 diversification** — N=4 validates open-core across orthogonal license axes; now a well-characterized pattern family
- **Commercial-gate is MAINSTREAMING** — PolyForm adoption signals that non-OSI licensing is acceptable in serious projects (28.5K stars with this license is evidence of community acceptance)

## 15. Next-audit consolidation opportunities

At next audit, consider:
1. **Pattern #31 license-approach taxonomy** — formal sub-type registry within confirmed Pattern #31 (4 approaches observed)
2. **Pattern #72 promotion criteria** — if 2nd PolyForm-family adoption emerges, promote under structurally-unambiguous-at-N=2
3. **Open-core meta-pattern** — consider if Pattern #31 + #50 + #72 consolidate into license-economy meta-pattern
4. **License-category observation registry** — similar to Pattern #17 5-variant table, formalize Pattern #29 categorical diversity table
