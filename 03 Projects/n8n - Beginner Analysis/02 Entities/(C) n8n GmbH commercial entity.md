# (C) n8n GmbH Commercial Entity + Jan Oberhauser

## Legal entity

- **Legal name:** n8n GmbH
- **Entity type:** GmbH (Gesellschaft mit beschränkter Haftung — German limited liability company; analog to US LLC)
- **HQ:** Berlin, Germany
- **Founded:** Aligned with project creation 2019 (n8n repo created 2019-06-22; legal entity formalization date not surfaced at imprint)
- **Operational age:** ~7 years at v56 probe (2nd-oldest subject in 56-wiki Storm Bear corpus after build-your-own-x v8)

## Authorship lineage

- **Founder + CEO:** Jan Oberhauser (sole managing director per imprint)
- **GitHub org:** `n8n-io` (n8n's company GitHub org)
- **Twitter / public presence:** Not enumerated at v56 probe (deferred)

## Funding (as much as surfaced at v56)

- **VC info:** Not disclosed at imprint level
- **Public funding history:** Q5 in OPEN-QUESTIONS.md — TechCrunch / Crunchbase research deferred to operator if relevant for Pattern #17 variant 3 funding-stage discriminator

## Commercial model — open-core with fair-code license

n8n GmbH operates a textbook **Pattern #31 Open-Core Commercial Entity** structure:

| Surface | License | Pricing |
|---|---|---|
| **n8n source** (self-host) | n8n Sustainable Use License (n8n SUL) — source-available non-OSI | Free for internal-business-use |
| **n8n.cloud** (managed SaaS) | Commercial subscription | Tiered pricing (Q4 deferred) |

This is **Pattern #31 11th data point** in the corpus.

## Sustainable Use License (n8n SUL) — full taxonomy

n8n SUL belongs to the broader **custom-non-OSI-commercial-restriction license family**, observed at corpus level **N=3 STRUCTURAL** with this v56 entry:

1. **omo v52 SUL-1.0** (Sustainable Use License Version 1.0) — Korean-Seoul T1 (code-yeongyu/oh-my-openagent)
2. **GitNexus v33 PolyForm-Noncommercial** — T5 (Pattern #72 stale-flagged)
3. **n8n v56 n8n-SUL** — T2 commercial-startup-mature (NEW v56)

**Family characteristics:**
- Source-available (NOT closed-source)
- Non-OSI compliant (NOT a recognized open-source license)
- Internal-business-use permitted (key escape hatch for small operators like Storm Bear)
- Hosting-as-service-to-third-parties restricted (commercial-protection clause)
- Custom-drafted (not standard PolyForm or BSL-like)

**Pattern Library impact at v56:**
- Pattern #29 sub-context **custom-non-OSI-commercial-restriction structural N=3** — promotion-candidate at next mini-audit under default ≥3-cross-tier criterion (T1 omo + T2 n8n + T5 GitNexus = 3 distinct tiers with 3 distinct license-name-instances; structurally-N=3 across 3 tiers)
- Could promote to formal sub-variant (e.g., 29-non-commercial-restriction-custom-license) under default ≥3-cross-tier OR meta-pattern-at-N=3-consolidation

## Storm Bear deployment implications under SUL

**ALLOWED for Storm Bear (internal-business-use):**
- Self-host n8n on personal/private server
- Use n8n for personal Scrum-coaching workflow automation
- Process internal team data through n8n workflows
- Build custom integrations for own use

**RESTRICTED for Storm Bear (hosting-as-service-to-third-parties):**
- Cannot offer "managed n8n service" to coaching clients commercially
- Cannot embed n8n as backend for client-facing SaaS without commercial license
- Cannot resell n8n functionality

**Resolution path if Storm Bear wants client-facing managed n8n:**
- Subscribe to **n8n.cloud commercial tier** (commercial license + hosted infrastructure)
- OR use **n8n Embed** offering if available (verify)

This SUL constraint is the critical Phase 0.9 criterion (b) qualification surfaced at v56 build.

## Commercial positioning relative to corpus peers

| Subject | Tier | License | Commercial entity | Operational age |
|---|---|---|---|---|
| n8n v56 | T2 | n8n SUL | n8n GmbH (Germany) | 7 years |
| ruflo v42 | T2 | MIT (per probe) | Ruflo Inc. (US) | ~1 year emerging |
| multica v15 | T2 | Apache 2.0 | Multica (US) | ~2 years |
| goclaw v4 | T2 | MIT | goclaw / Storm Bear v4 origin | ~6 months at v4 wiki probe |

n8n is the **most-mature T2 commercial entity in corpus by operational age** (7 years vs ruflo ~1 year + multica ~2 years + goclaw ~6 months) AND has the **most-restrictive license among T2 entrants** (SUL non-OSI vs others MIT/Apache OSI-permissive).

This positions n8n as the **mature commercial-startup-with-license-hedge** archetype within T2.

## Pattern strengthening at v56

- **Pattern #17 variant 3 commercial-startup ecosystem** — 7-year mature (joins ruflo v42 / Composio v50 / shannon v45 / others); n8n is OLDEST commercial-startup observation at this variant
- **Pattern #19 archetype 4** — solo-founder-CEO 7-year operational lineage strengthening
- **Pattern #31 Open-Core Commercial Entity** — 11th data point with Pro-docs-depth axis (estimate depth 3-4)
- **Pattern #50 Commercial-Funnel Companion Platform** — n8n.cloud managed = 50a Standard sub-variant strengthening

## Out-of-scope at v56

- VC funding round history (Q5)
- n8n.cloud tier pricing breakdown (Q4)
- Geographic-restriction analysis (Q6 — RU/BY sanctions clause)
- Employee count / team size
- Revenue / ARR signals
