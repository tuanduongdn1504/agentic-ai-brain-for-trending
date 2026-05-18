# CloakBrowser (CloakHQ) — Project CLAUDE.md

📍 **Status:** Active wiki build — **v69** (2026-05-18)
📍 **Routine:** `05 Skills/llm-wiki-routine-v2.2.md`
📍 **Subject:** [github.com/CloakHQ/CloakBrowser](https://github.com/CloakHQ/CloakBrowser)
📍 **Homepage:** [cloakbrowser.dev](https://cloakbrowser.dev/)

---

## Wiki framing decision (Phase 0 — important)

**CloakBrowser is a bot-detection-evasion tool** (stealth Chromium with C++ source-level fingerprint patches). The BINARY-LICENSE includes an explicit Acceptable Use section prohibiting credential stuffing, brute-force, unauthorized auth bypass, and fraud.

**This wiki is KNOWLEDGE-BASE DOCUMENTATION** consistent with how the corpus documents other agent browser/scraper tools (browser-use v34, crawl4ai v29, Skyvern v24). It maps:
- architecture + project shape + tier/archetype classification
- Pattern Library implications (cross-wiki synthesis)
- license-axis observations (the central v69 contribution)
- legitimate-use framing for the beginner guide (authorized red-team / accessibility research / academic research / privacy-preserving browsing)

**This wiki will NOT provide:**
- tactical evasion techniques against specific anti-fraud / anti-bot services
- step-by-step instructions optimized for circumventing protections without authorization
- operational guidance that would primarily benefit prohibited-use scenarios

The beginner guide (Phase 4a) emphasizes ToS / legal / ethical considerations explicitly. The Pattern Library work (Phase 4b) is about license-axis sub-typology, not evasion mechanics.

---

## Phase 0 outputs (verified 2026-05-18)

### Subject identity

- **Tagline (verbatim):** *"Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed."*
- **Created:** 2026-02-22 → wiki build 2026-05-18 = **86 days old**
- **Author:** CloakHQ (anonymous-corporate; `cloakhq@pm.me` contact)
- **License:** **MIT wrapper + Proprietary Binary License with Acceptable Use restrictions** (NEW corpus license-shape)
- **Stats at v69 wiki build:** 14,851 stars / 1,163 forks / 77 watchers / 77 open issues / 171 commits / 28+ releases (v0.1.0 2026-02-22 → v0.3.28 2026-05-11)
- **Latest release:** v0.3.28 on 2026-05-11 (Chromium 146.0.7680.177.4 with 57 source-level fingerprint patches)

### Org structure (CloakHQ, 6 public repos)

| Repo | Stars | License | Role |
|------|-------|---------|------|
| **CloakBrowser** ← THIS SUBJECT | 14.9k | MIT wrapper + proprietary binary | Primary product |
| CloakBrowser-Manager | 376 | (Python) | Web profile manager (sister product) |
| chromium-stealth-builds | — | (binary distribution) | Binary artifact distribution |
| crawl4ai (FORK) | — | Apache-2.0 | **FORK of v29 corpus subject** crawl4ai for integration |
| crawlee-python (FORK) | — | Apache-2.0 | **FORK of dependency framework** for integration |
| awesome-playwright (FORK) | — | CC0-1.0 | Forked discovery list |

**Observation:** 3 original repos + 3 forks. The fork-pattern is corpus-first — maintaining patched forks of dependency frameworks as integration strategy. → **Phase 4b OC-G candidate.**

### Subject classification (13-axis, v2.2 enhanced)

| Axis | Value |
|------|-------|
| **Tier** | **T2 Service** — provides binary + Python/JS wrapper SDK; closest match to browser-use v34 (T2 Service) and crawl4ai v29 (T2 Service) |
| **Archetype** | **anonymous-corporate-stealth-product** — corpus-first (pm.me email, no public individual identity, dual-use product warranting anonymity) |
| **Scale tier** | **medium** (14.9K stars at 86 days; HIGH velocity but not corpus-record) |
| **Primary lang** | **Python 53.1% + TypeScript 43.2% + JavaScript 2.9%** (dual SDK: Python + JS via npm) |
| **Packaging tool** | dual: `pip install cloakbrowser` (Python) + `npm install cloakbrowser` (JS); binary auto-downloaded ~200MB per platform |
| **Origin story** | corpus-first **purpose-built-for-stealth** subject (vs prior corpus subjects with stealth as feature) |
| **Methodology** | C++ source-level binary patches (vs prior corpus runtime/JS injection approaches in browser-use, Skyvern, crawl4ai) |
| **Governance file count** | **2 governance docs** (LICENSE MIT + BINARY-LICENSE.md proprietary) — corpus-first explicit dual-license artifact split |
| **Agent/skill count** | N/A (subject is browser binary + SDK, not skill collection) — but `ai-agents` topic + framework integrations for browser-use + crawl4ai |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | **ungoogled-chromium** (upstream attribution in BINARY-LICENSE) + Chromium / The Chromium Authors / Google BSD-3-Clause |
| **Agent platforms supported** | drop-in for Playwright + Puppeteer + Selenium; framework integrations for browser-use + Crawl4AI + Scrapy + Crawlee + AWS Lambda + BrowserBase |
| **Living-Domain-Standards Tracking** | NO — CloakBrowser establishes own anti-detection standards rather than codifying external ones |

### Velocity-screen + engagement-signal (v2.2 NEW)

| Metric | Value | Corpus context |
|--------|-------|---------------|
| Age | **86 days** | sub-90-day post-launch window |
| Stars | 14,851 | medium-tier |
| Forks | 1,163 | moderate |
| Watchers | 77 | very low |
| Open issues | 77 | low |
| Commits | 171 | moderate (2 commits/day) |
| Releases | 28+ (v0.1.0 → v0.3.28) | very high release cadence (~1 release every 3 days) |
| **`stars_per_day`** | **172.7** | **HIGH but BELOW Pattern #52 EXTREME-VIRAL threshold (>300/day in <90 days)** — does NOT trigger Pattern #52; observational HIGH-velocity-not-extreme |
| `fork_ratio` (forks/stars) | 0.078 (7.8%) | moderate; closer to "actual usage" than drive-by-stars |
| `watchers_ratio` (watchers/stars) | 0.0052 | very low — drive-by-stars pattern visible (similar to zero v68 0.0043, opencode-antigravity-auth v67 0.0001 CORPUS-RECORD LOW) |
| `open_issues_ratio` | 0.0052 | low |
| **commits/day** | **~2.0** | sustained-but-not-extreme |
| **releases/day** | **~0.33** (1 every 3 days) | extreme release cadence (similar to zero v68 1.5/day) |

**Velocity verdict:** HIGH-not-EXTREME — Pattern #52 does NOT trigger (172/day vs >300 threshold). Add to v69 audit batch as Pattern #52 sub-threshold observational data point (a 14.9K-stars/86-days subject that DOES NOT meet Pattern #52 criterion clarifies threshold).

### Pattern Library pre-check (Phase 0.5 expanded v2.2)

- **Pattern #45 Dual-Licensing Discipline (CONFIRMED v60 mini-audit, N=2):** **STRONG N=3 strengthening evidence + NEW sub-typology variant.** Prior corpus exemplars (Pattern #45):
  - **45a:** Unsloth v23 Apache-2.0 + Commercial-shield (corpus N=1)
  - **45b:** AutoGPT v59 MIT + PolyForm-Shield (corpus N=2)
  - **45c (NEW at v69):** CloakBrowser MIT wrapper + Proprietary Binary License with explicit Acceptable Use enumeration (corpus N=3)
  - 45c distinguishing mechanism: license axis splits ARTIFACT (wrapper OSS vs binary proprietary) + Acceptable Use clause explicitly enumerates prohibited use cases (credential stuffing / brute-force / fraud / unauthorized auth) — corpus-first.
  - → **Phase 4b PRIMARY: Pattern #45 NEW sub-typology 45c registration**

- **Pattern #83 Honest-Deficiency-Disclosure Discipline (CANDIDATE N=3 PROMOTION-ELIGIBLE at v67 → N=4 consolidation at v68 → N=5 at v69):** STRONG consolidation evidence. Multi-surface disclosure (5+ surfaces in single subject):
  - BINARY-LICENSE explicit security disclaimer
  - CHANGELOG #217 path-traversal security fix acknowledged
  - "no warranty / no liability / max $100" framings
  - Acceptable Use prohibited-actions enumeration
  - "CloakHQ does not endorse, encourage, or support any illegal use" framing
  - **N=5 consolidates v67 PROMOTION-ELIGIBLE verdict; no separate proposal-document needed (v67 already filed).**

- **Pattern #19 ecosystem-portfolio-builder (CONFIRMED N=4 at v66):** WEAK strengthening — CloakHQ has 6 repos but 3 are forks; original-product cluster is small (3 repos). Closer to product-suite-portfolio than founder-portfolio. **Sister observation** but not direct N+1.

- **Pattern #52 EXTREME-VIRAL-Velocity (CONFIRMED v63):** **COUNTER-EVIDENCE / threshold-clarifying data point.** CloakBrowser at 172/day for 86 days does NOT meet >300/day threshold but is HIGH-velocity. → add to v69 audit Pattern #52 sustained-velocity-test batch as **sub-threshold-control case** (confirms threshold discriminates).

- **Pattern #66 meta-supply-chain-awareness (CONFIRMED):** STRENGTHENING evidence — ungoogled-chromium upstream explicitly attributed in BINARY-LICENSE + telemetry-disclaimer + "built on Chromium by The Chromium Authors under BSD 3-Clause" upstream chain documented.

- **Pattern #57 Cross-Wiki-Citation:** STRENGTHENING via explicit framework-integration mention of **browser-use (v34 corpus subject)** + **crawl4ai (v29 corpus subject)** in README. **2 corpus subjects directly named** in primary README — anchors Phase 0.9 (d) criterion strongly.

- **NEW observational candidate OC-G: Fork-as-Integration-Strategy** — org maintains forks of dependency frameworks (CloakHQ forks crawl4ai + crawlee-python + awesome-playwright) for integration-with-patches. Corpus-first.

- **NEW observational candidate OC-H: Anonymous-Corporate-Author for Dual-Use Tools** — pm.me hosted email, no individual identity disclosed (likely defensive against legal exposure given dual-use product). Corpus-first.

- **NEW observational candidate OC-I: Detection-Evasion-As-Product-Axis** — purpose-built stealth (not feature in larger product). Distinct from corpus prior subjects browser-use v34 / crawl4ai v29 / Skyvern v24 which treat stealth as one feature among many.

- **NEW observational candidate OC-J: Acceptable-Use Enumeration as Risk-Mitigation Layer** — BINARY-LICENSE enumerates specific prohibited uses (rare in OSS license shapes); legal scaffolding density is corpus-broadest.

### Storm Bear meta-entity Phase 0.9 STRICT (decision pre-registered)

**Verdict: 1/4 STRICT PASS = WEAK INCLUDE** (SECOND consecutive WEAK in post-amendment window after v68)

| Criterion | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| (a) Author archetype peer | **FAIL** | CloakHQ is anonymous-corporate (pm.me email, no individual identity); not solo-engineer-coach peer to vault operator |
| (b) Operational tool for Scrum-coaching | **FAIL** | Stealth browser binary; not Scrum-coaching tool; specific use case mismatch + acceptable-use restrictions make operational deployment inappropriate for vault context |
| (c) Methodology-influence-node | **FAIL** | CloakBrowser does not influence vault routine v2.1+ maintenance; no methodology citation chain |
| (d) In-corpus sibling reference | **PASS** | README explicitly cites framework integrations for **browser-use (v34 corpus subject)** and **Crawl4AI (v29 corpus subject)**; 2 named corpus subjects in primary README |

→ **WEAK INCLUDE (1/4)** — meets minimum bar per routine v2.2 strength categorization. Entity 4 = Storm Bear meta-entity.

**Streak effect:** Post-v64-RESET window now 5 consecutive PASS:
- v65 STRONGEST 3/4 STRICT
- v66 STRONG 4/4 STRICT
- v67 MODERATE 2/4 STRICT
- v68 WEAK 1/4 STRICT
- **v69 WEAK 1/4 STRICT — SECOND consecutive WEAK**

13-instance Phase 0.9 post-amendment window v57-v69 = 11 PASS / 2 SKIP = **84.6% INCLUDE rate** (slight uptick from v68 83.3%).

### Sibling detection

| Sibling | Relation | Why |
|---------|----------|-----|
| **v29 crawl4ai** | **STRONG sibling** | README explicit framework integration; CloakHQ org maintains FORK of crawl4ai; same scraping/automation problem-domain |
| **v34 browser-use** | **STRONG sibling** | README explicit framework integration; same browser-automation-for-agents problem-domain; CloakBrowser positions as drop-in compatibility |
| v24 Skyvern | scraping/automation sibling | shared problem-domain (browser automation for agents); Skyvern at T2 Service tier |
| v23 Unsloth | **Pattern #45 N=1 sibling (45a)** | Both dual-licensed; Unsloth is Apache+commercial-shield, CloakBrowser is MIT+proprietary-binary-with-acceptable-use |
| v59 AutoGPT | **Pattern #45 N=2 sibling (45b)** | Both dual-licensed; AutoGPT is MIT+PolyForm-Shield, CloakBrowser introduces 45c sub-typology |
| v68 vercel-labs/zero | adjacent v2.2 sibling | Same v2.2-routine wiki neighbor; both have Pattern #83 honest-deficiency-disclosure evidence + indemnification clauses |

### Tier placement decision

**T2 Service** — definitive (no PROVISIONAL needed unlike v68). Rationale:
- Provides binary distribution + Python/JS wrapper SDK as installable libraries (T2 Service signature)
- Matches existing corpus T2 subjects: browser-use v34 / crawl4ai v29 / Skyvern v24
- NOT T1 Augmentation (not skill collection)
- NOT T4 Bridge (not API/protocol translator; drop-in compatibility is a binary substitution, not bridge mechanism)

**Sub-archetype:** corpus-first **anonymous-corporate-stealth-product** — observational sub-archetype within T2 Service. Pattern #19 may evolve sub-pattern at audit.

### Phase 4b PRIMARY routing pre-registration

**PRIMARY:** **Pattern #45 Dual-Licensing NEW sub-typology 45c registration** — wrapper-OSS + binary-proprietary-with-acceptable-use-restrictions (3rd Pattern #45 mechanism). Proposal-document at `01 Analysis/`.

**SECONDARY:**
- Pattern #83 N=5 consolidation evidence (no new proposal-document — v67 already filed)
- NEW observational candidate OC-G: Fork-as-Integration-Strategy
- NEW observational candidate OC-H: Anonymous-Corporate-Author for Dual-Use Tools
- NEW observational candidate OC-I: Detection-Evasion-As-Product-Axis
- NEW observational candidate OC-J: Acceptable-Use Enumeration as Risk-Mitigation Layer
- Pattern #52 sub-threshold-control case (HIGH-velocity-NOT-extreme; clarifies threshold)

### Consolidation guard — ELEVATED concern

**Pre-build state (post-v68 zero wiki 2026-05-18):**
- 43 confirmed / 31 active / 0.721 ratio
- Active count ≥30 trigger REACHED at v67 + MAINTAINED at v68 → now **3rd CONSECUTIVE WIKI past trigger at v69**
- Ratio still < 0.95 (full warning threshold) — **PROCEED normally per routine v2.2**
- v68 audit batch ~20 items LARGEST in corpus history — **operationally overdue + elevating**
- **This wiki proceeds; iteration log will recommend audit BEFORE v70**

**Per routine v2.2 protocol:** PROCEED with elevated audit recommendation. v69 audit batch will accumulate to ~24-25 items (~20 from v68 + 5 new from v69) — extending the LARGEST-batch record.

---

## Cross-references

- **Routine:** [llm-wiki-routine-v2.2.md](../../05 Skills/llm-wiki-routine-v2.2.md)
- **Ingest methodology:** [llm-wiki-ingest.md](../../05 Skills/llm-wiki-ingest.md)
- **Pattern Library:** [PATTERN_LIBRARY.md](../../PATTERN_LIBRARY.md)
- **Strongest sibling:** [v29 crawl4ai](../crawl4ai - Beginner Analysis/CLAUDE.md) + [v34 browser-use](../browser-use - Beginner Analysis/CLAUDE.md)
- **Pattern #45 N=1 sibling:** [v23 Unsloth](../Unsloth - Beginner Analysis/CLAUDE.md)
- **Pattern #45 N=2 sibling:** [v59 AutoGPT](../AutoGPT - Beginner Analysis/CLAUDE.md)
- **Recent v2.2 sibling:** [v68 vercel-labs/zero](../zero - Beginner Analysis/CLAUDE.md)

---

## Phase status

- [x] Phase 0 — Pre-flight + probe complete
- [x] Phase 1 — Scaffold
- [x] Phase 2 — Source ingestion (3 clusters)
- [x] Phase 3 — Entity pages (4 entities; Storm Bear meta included per WEAK INCLUDE 1/4)
- [x] Phase 4a — Beginner bilingual guide (`03 Published/`) — legitimate-use framing
- [x] Phase 4b — Pattern #45 NEW sub-typology 45c registration (`01 Analysis/`)
- [x] Phase 5 — Iteration log + Pattern Library updates
- [x] Phase 6 — Vault sync (`_state/03c-projects-v61-v69.md` / root `CLAUDE.md` / `_goals/02-version-log.md` / `PATTERN_LIBRARY.md`)

**v69 wiki build COMPLETE 2026-05-19** (build span 2026-05-18 → 2026-05-19).
