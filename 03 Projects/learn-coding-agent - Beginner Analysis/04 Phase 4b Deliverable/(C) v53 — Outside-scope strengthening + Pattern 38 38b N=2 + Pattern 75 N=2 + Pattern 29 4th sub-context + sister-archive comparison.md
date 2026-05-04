# v53 Phase 4b deliverable

> **Mode:** OUTSIDE-SCOPE STRENGTHENING + Pattern #38 sister-archive comparison + Pattern #29 sub-context formalization + Pattern #75 N=2 mechanism-divergence
> **Wiki #53 — learn-coding-agent (sanbuphy)**
> **Routine v2.1 — 10th v2.1-era execution**

---

## Part 1 — Pattern #38 38b sub-variant promotion-candidate analysis

### Pre-v53 state of Pattern #38

🟡 #38 Prompt-Leak-Archive Genre — CANDIDATE since v21 (single observation: system-prompts-leaks v21 N=1).

**v21 Formal statement (verbatim from PATTERN_LIBRARY.md line 3171-3172):**
> Prompt-leak-archive genre: repositories aggregating system prompts extracted from closed-source commercial AI tools. Characterized by: (a) content = extracts not originals; (b) sources = closed-source commercial; (c) legal position = gray zone; (d) author often pseudonymous; (e) monetization = patronage + commercial derivative common; (f) extraction methods typically not documented.

**Required for promotion:** 2+ similar archives.

**Prediction (v21):** May remain rare due to legal-complexity barriers. Related genres (leaked training data, leaked benchmark data) may emerge.

### v53 evidence

learn-coding-agent v53 = `sanbuphy/learn-coding-agent`:
- 11,735 stars / 19,741 forks (CORPUS-RECORD 168.2% fork inversion)
- 4 READMEs (EN+CN+JA+KO) + 20 docs/ deep-dive reports
- Subject: Claude Code v2.1.88 internals (single AI tool, deep-dive)
- Author: Sanbu / sanbuphy (CN, named-but-low-identity, 279 GitHub repos, blog aispacewalk.cn)
- Compiled "entirely from publicly available online references and discussions"
- License: None formal; "research-only + Commercial use strictly prohibited" via README only
- Status: ABANDONED 2026-04-01 (24+ days stale)

### Sub-variant taxonomy proposal

| Sub-variant | Wiki | Subject scope | Content type | Author identity | Monetization | Extraction method |
|-------------|------|---------------|--------------|-----------------|--------------|-------------------|
| **38a multi-tool-prompt-archive** | system-prompts-leaks v21 | 31 AI tools (broad) | System prompts | Pseudonymous (x1xhlol multi-handle) | 6-channel (Patreon + Ko-fi + crypto + ZeroLeaks commercial) | Opaque (not documented) |
| **38b single-tool-internals-deep-dive NEW v53** | learn-coding-agent v53 | 1 AI tool (Claude Code v2.1.88) | Architecture + telemetry + codenames + killswitches + roadmap | Named-but-low-identity (Sanbu / Mars-humor) | Zero monetization signals | Documented "publicly available online references and discussions" |

### Structural-N=2 promotion criterion check (v2.1)

| Criterion | Status |
|-----------|--------|
| N=2 distinct sub-variants identified | ✅ |
| Both fit broader formal statement | ✅ (both = extracts of closed-source commercial AI tools, gray legal position) |
| Sub-variants structurally distinct (subject scope) | ✅ (multi-tool vs single-tool) |
| Cross-corpus distance | ✅ (v21 → v53 = 32 wikis apart; substantial separation) |
| Authorship divergence | ⚠️ (pseudonymous vs named-low-identity — meaningful but bridgeable under "low-accountability author archetype") |
| Monetization divergence | ⚠️ (6-channel commercial vs zero — meaningful divergence) |
| Extraction-method divergence | ⚠️ (opaque vs documented-public-sources — meaningful divergence) |

### Recommendation for next mini-audit

**Promotion-candidate at next mini-audit under structural-N=2-sub-variant criterion.** Mini-audit can:

- **(a) PROMOTE #38 to CONFIRMED** with both 38a + 38b sub-variants formalized in pattern statement
- **(b) GENERALIZE #38 formal statement** to broader "AI-tool-disclosure-archive genre" wrapping both extracted-prompts (38a) and reverse-engineered-internals (38b)
- **(c) STAY CANDIDATE** if sub-variant divergences (authorship + monetization + extraction-method) deemed too large for unification

**Storm Bear recommendation:** Operator overlap-resolution required at mini-audit. Both v21 and v53 share the substantive core (gray-legal-archive of closed-source commercial AI tool internals); divergences are in author/monetization profile not in pattern essence. **Lean (a) PROMOTE with 2-sub-variant explicit formalization**, but defer to operator judgment.

---

## Part 2 — Pattern #75 N=2 mechanism-divergence analysis

### Pre-v53 state of Pattern #75

🟡 #75 Template-Use Fork-Star Anomaly at Cold-Start — OBSERVATION-TRACK NEW v37 (bizos N=1).

**v37 evidence:** bizos at 2-day-old + 138% fork-to-star inversion + clear template-use mechanism (Next.js business OS template designed for cloning + own-deploy).

### v53 evidence

learn-coding-agent v53: **168.2% fork-to-star inversion** (19,741 forks vs 11,735 stars) at 25-day-old.

This is **NEW CORPUS-RECORD inversion ratio**, exceeding bizos v37's 138% by 30 percentage points.

### Mechanism comparison (CRITICAL)

| Wiki | Inversion ratio | Repo age | Subject type | Mechanism |
|------|-----------------|----------|--------------|-----------|
| bizos v37 | 138% | 2 days | Commercial app (Next.js business OS template) | **Template-use** (CLEAR) |
| **learn-coding-agent v53** | **168.2% (NEW RECORD)** | **25 days (abandoned day-2)** | **Research archive (markdown-only, no code)** | **MECHANISM UNCLEAR** |

### Possible mechanisms for v53

1. **CN-class-assignment-fork** — CN academic culture sometimes uses GitHub forks for course assignments. Plausible given CN-author + CN-language docs.
2. **Mass-fork-bot** — CN GitHub ecosystem has documented fork-farm bot activity. Plausible at 19,741 in 25 days.
3. **Fork-as-bookmark CN-culture** — Some CN GitHub users prefer fork-instead-of-star for bookmarking. Plausible.
4. **Self-host-mirror anticipation** — Users may fork in anticipation of original takedown (DMCA-style). Plausible given research-only license + Anthropic-internals disclosure.
5. **Fork-to-translate / fork-to-adapt** — 19 language groups beyond original 4 may have forked for translation. Less plausible.

### Why mechanism caveat matters for pattern formalization

If bizos = template-use and v53 = different mechanism (CN-cultural / bot / anticipation-fork), Pattern #75 cannot be unified as single pattern at N=2.

**Options for mini-audit:**
- **(a) PROMOTE** if mechanisms unifiable as broader "fork-amplified-cold-start anomaly" (mechanism-agnostic framing)
- **(b) SPLIT** into 75a template-use + 75b CN-cultural-or-bot-amplification
- **(c) STAY OBSERVATION-TRACK** at N=2 with explicit mechanism-divergence flag (most-conservative)

**Storm Bear recommendation:** **(c) STAY OBSERVATION-TRACK** at v53. Insufficient evidence to promote OR split. Wait for N=3 to disambiguate mechanism.

### Why this matters more broadly

168.2% inversion at abandoned-archive with markdown-only content is structurally surprising. May reveal a **CN-OSS engagement pattern** distinct from Western OSS engagement norms — potential observational track for future cross-corpus pattern emergence.

---

## Part 3 — Pattern #29 NEW 29-absent-4 sub-context formalization

### Pre-v53 state of Pattern #29

✅ #29 License-Category-Diversity — CONFIRMED at v21. Post-v52: 4 sub-contexts in absent-LICENSE category formalized.

### v53 NEW sub-context

**29-absent-4 research-only-non-commercial-restriction-without-LICENSE-file + Copyright-disclaimer**

### Evidence

README §"Copyright & Disclaimer" (verbatim):
```
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

- No LICENSE file
- Informal commercial-restriction in README only (goodwill signal, not legal-license weight)
- DMCA-style takedown clause (acknowledges potential third-party rights infringement)
- Default copyright applies (Berne Convention default = all rights reserved by author)

### Updated 4-sub-context taxonomy

| Sub-context | Wikis | Description |
|-------------|-------|-------------|
| 29-absent-1 | bizos v37 | Commercial-cold-start + README-proprietary-claim |
| 29-absent-2 | dive-into-llms v39 | Academic-public-welfare + no-claim |
| 29-absent-3 | awesome-claude-skills v50 + vercel-labs v51 | README-OSI-license-claim-without-LICENSE-file |
| **29-absent-4 NEW v53** | **learn-coding-agent v53** | **Research-only-non-commercial-restriction-without-LICENSE-file + Copyright-disclaimer** |

### Cross-corpus license-philosophy cluster

learn-coding-agent's 29-absent-4 (informal commercial-restriction) is part of broader non-commercial-restriction license-philosophy cluster:

| Wiki | License | Form |
|------|---------|------|
| oh-my-openagent v52 | SUL-1.0 (Sustainable Use License) | Formal license-text |
| GitNexus v33 | PolyForm Noncommercial 1.0.0 | Formal license-text |
| **learn-coding-agent v53** | **None formal; README-only declaration** | **Informal goodwill-signal** |

All three restrict commercial use; differ in formality. v53 is least-formal (informal-README-only) of the three.

### Recommendation

Sub-context formalization-candidate at next mini-audit. Mini-audit decides whether to formally enumerate 29-absent-4 in Pattern #29 statement.

---

## Part 4 — 5-doc deep analysis content summary

(See C2 cluster summary for full per-doc detail. This section is brief synthesis for Phase 4b strategic context.)

### Substantive structural insights from Sanbu's analysis

1. **Telemetry pipeline as architectural choice** — two-tier (1P + Datadog) with disk-persisted retry is robust-engineering approach typical of telemetry-mature commercial products. The no-UI-opt-out asymmetry favors data-collection over user-control.

2. **Animal-codename system as security-engineering** — random-word-pair flag naming + canary-string scanning + String.fromCharCode runtime-construction = sophisticated leak-prevention infrastructure. Suggests Anthropic treats codename leaks as material competitive risk.

3. **Internal vs external prompt asymmetry as product-tier discrimination** — materially-different prompts + tool access between ant and external users is standard SaaS-tier-product engineering. External users get the "free tier" of the prompt-engineering investment; ant employees test the optimized version.

4. **Undercover mode as policy-codified-in-software** — instructing model to write commits "as a human developer would" + no force-OFF = policy decision (don't leak codenames) implemented at prompt-injection level. Raises OSS-attribution-norm questions but is internally rational from a leak-prevention perspective.

5. **Remote killswitch infrastructure as risk-management** — hourly polling + accept-or-die + GrowthBook flag-without-consent enables Anthropic to remotely respond to any production incident (security bug, capability misuse, etc.). User-consent is sacrificed for infrastructure-control.

6. **KAIROS as future-product direction** — `<tick>` heartbeats + autonomous-mode + push-notifications + GitHub-PR-subscriptions = clear product evolution toward always-on autonomous agent. Aligns with broader industry direction (Devin, OpenHands T5 v30, etc.).

### Storm Bear pattern-cross-references

- Numbat next-model + KAIROS autonomous mode → Pattern #18 Layer 0 evolution direction; vault should plan for Numbat migration + KAIROS-aware infrastructure
- Internal-vs-external prompt asymmetry → reinforces vault rule "verify Claude Code outputs for important decisions"
- Telemetry no-UI-opt-out → reinforces operator awareness of vault git-remote SHA256 fingerprinting

---

## Part 5 — Sister-archive comparison: v21 system-prompts-leaks ↔ v53 learn-coding-agent

| Dimension | v21 system-prompts-leaks | v53 learn-coding-agent |
|-----------|--------------------------|------------------------|
| Repo | x1xhlol/system-prompts-and-models-of-ai-tools | sanbuphy/learn-coding-agent |
| Repo title | "FULL [31 AI tools]. System Prompts, Internal Tools & AI Models" | "Claude Code Architecture Study" |
| Subject scope | 31 AI tools (broad) | 1 AI tool (Claude Code v2.1.88) |
| Content type | System prompts (extracted) | Architecture + telemetry + codenames + killswitches + roadmap |
| Stars | 135.5K (#2 in corpus, only behind build-your-own-x 491K) | 11.7K (medium tier) |
| Forks | 34K (#1 in corpus) | 19.7K (CORPUS-RECORD 168.2% inversion) |
| Repo age | 13 months | 25 days (abandoned day-2) |
| Author | x1xhlol (pseudonymous, multi-handle: lucknitelol Patreon/Ko-fi + NotLucknite X) | Sanbu / sanbuphy (named GitHub, low-identity, Mars-humor) |
| Author region | Unknown | China (CN-blog active) |
| Maintenance status | Active | ABANDONED day-2 |
| License | GPL-3.0 (controversial application — Pattern #39) | None formal; "Commercial use prohibited" only |
| Monetization | 6-channel: Patreon + Ko-fi + BTC + LTC + ETH + Solana + ZeroLeaks commercial | Zero monetization signals |
| ZeroLeaks-style perverse-incentive | YES (Pattern #40) | No |
| i18n | EN-only | Quadrilingual EN+CN+JA+KO |
| Pattern #38 sub-variant | 38a multi-tool-prompt-archive | 38b single-tool-internals-deep-dive |
| Pattern #29 contribution | License application (GPL-3.0 controversial) | Sub-context (29-absent-4 informal) |
| Pattern #75 contribution | None (low fork-to-star ratio) | N=2 mechanism-divergence-flagged |
| Outside-scope sub-type registered | Prompt-leak-archive genre (#38) | Strengthens #38 with sub-variant 38b |
| Storm Bear pilot relevance | OBSERVATIONAL only (AVOID due to perverse-incentive) | REFERENCE-ONLY (commercial-blocked) |
| Beginner guide ethical framing | "AVOID" pilot tier first introduced | Operational caveats prominent + "REFERENCE-ONLY" |

### Key takeaway from sister-archive comparison

Both v21 and v53 are gray-legal archives of closed-source commercial AI tool internals. They share Pattern #38 family but differ in:
- **Subject narrowness** (31 tools vs 1 tool)
- **Author profile** (pseudonymous vs named-low-identity)
- **Monetization** (commercial-derivative-funded vs zero)
- **Maintenance** (active vs abandoned-day-2)

Both demonstrate the **structural existence of a gray-legal-archive ecosystem** for closed-source commercial AI tool internals. v21 + v53 = N=2 sufficient for sub-variant taxonomy at next mini-audit.

---

## Part 6 — Adversarial-Anthropic-positioning N=2 observational documentation

### v52 omo evidence

oh-my-openagent v52 (post-v52 wiki) had explicit adversarial-Anthropic competitive-positioning:
- "Anthropic blocked OpenCode because of us" framing
- "Claude Code's a nice prison" anti-lock-in framing

Mechanism: **competitive-positioning anti-lock-in** (omo competes with Claude Code by enabling OpenCode runtime; positions Claude Code as restrictive)

### v53 evidence

learn-coding-agent v53 documents Anthropic's hidden behaviors:
- Telemetry-without-UI-opt-out
- Undercover-mode (no force-OFF)
- Remote-killswitches (accept-or-die)
- GrowthBook-flag-without-consent
- Internal-vs-external prompt asymmetry (external users get inferior product)

Mechanism: **reverse-engineering-disclosure** (v53 doesn't compete; it documents internals to inform users; positions Anthropic's behaviors as disclosure-worthy)

### Mechanism-divergence

| Wiki | Mechanism | Stance | Output |
|------|-----------|--------|--------|
| omo v52 | Competitive-positioning anti-lock-in | We are alternative to Claude Code | Tool product |
| **learn-coding-agent v53** | **Reverse-engineering-disclosure** | **Here's what Claude Code does internally** | **Research archive** |

→ Mechanisms differ. Insufficient for new pattern candidate (consolidation-forward discipline). **Document N=2 observational; do NOT register standalone candidate.**

### Why this matters

Both v52 and v53 represent **community pushback against Anthropic's product positioning**. v52 = "we'll compete"; v53 = "we'll disclose." Together they may be early signal of broader community-Anthropic-tension trajectory. If N=3+ wikis emerge with adversarial-Anthropic-positioning, mini-audit could formalize as new pattern. Currently insufficient evidence.

---

## Part 7 — Storm Bear operational caveats summary

(See E4 entity page for full detail. This section is brief Phase 4b strategic recap.)

### Top 6 caveats Storm Bear operator should know about Claude Code daily-use

1. **Telemetry no UI-opt-out** for direct API users — env fingerprint + repo-URL hash + tool inputs (truncated) + file extensions sent to Anthropic + Datadog every event
2. **Remote killswitches mid-session** — hourly polling; reject = `gracefulShutdownSync(1)` exit; save vault state frequently
3. **GrowthBook A/B without consent** — Storm Bear sessions may behave differently across days based on opaque experiment groups
4. **External users inferior prompts** — "Be extra concise" vs internal "Err on side of more explanation"; ~29-30% Capybara v8 false-claims rate; verify-before-act
5. **Numbat / KAIROS / voice / 17 unreleased tools coming** — plan vault Pattern #18 evolution
6. **Repo URL fingerprinted (SHA256-first-16-char)** — server-side correlation possible; Storm Bear vault git remote is fingerprinted; unavoidable for direct API

---

## Part 8 — Pattern Library state at v53 + 17 promotion-candidates accumulated

### Pre-v53 state (post-v52)

- 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio 18:38 = **0.474:1** (largest buffer 0.476 below 0.95:1 mini-audit trigger; preserved 2 cycles)

### Post-v53 state

- **38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active**
- **Ratio 18:38 = 0.474:1 PRESERVED 3RD POST-v50-MINI-AUDIT CYCLE** (largest buffer in corpus history maintained 3 consecutive wikis: v51 + v52 + v53)
- **17-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK** (v37-v53) — NEW LONGEST in corpus history (extends v52's 16-streak)

### 17+ promotion-candidates accumulated post-v53 (cumulative across v45-v53)

**v53 NEW (3):**
- #38 38b structural-N=2 (single-tool-internals-deep-dive)
- #29 29-absent-4 sub-context (research-only-non-commercial-restriction)
- #75 N=2 mechanism-divergence-flagged (DO NOT auto-promote)

**v52 carry (5):**
- #57 57c structural-N=2 (forward-citation-then-wiki)
- #18 OpenCode-primary structural-N=2
- #29 SUL-1.0 sub-context
- #58 58c sub-variant
- #50 50d sub-variant

**v51 carry (9):**
- #22 22d identical-mirror
- #57 57c (now superseded by v52 N=2 evidence)
- #29 29-absent-3
- #29 AGPL-at-project-scope
- #50 50b
- #66 OT sub-categorization
- #18 4-layer
- #22 22c scope-narrowing
- #47 retirement (carry-forward)

**Total: 17+ promotion-candidates** at next mini-audit.

### Mini-audit warranted

**Operator-trigger required.** Estimated effort: ~30-60 min for 17 candidates.

---

## Part 9 — Velocity + discipline plateau

### v2.1-era execution status

- **10th v2.1-era routine execution** (v32 + v33 + v34 + v36 + v37 + v44 + v50 + v51 + v52 + v53)
- All 5 v2.1 discipline mechanisms exercised cleanly:
  - Overlap pre-check (12 candidate observations evaluated; all routed to within-existing-pattern)
  - Un-stale check (all 3 stale candidates negative; disciplined)
  - Counter-evidence handling (Pattern #27 cold-start sub-path observation; not registered standalone)
  - Consolidation-forward discipline (12/12 rejections — text-book application)
  - N=1 stale-risk-flagging (N/A; zero new registrations)

### Velocity plateau

- **34 consecutive wikis at velocity plateau** (v6-v53)
- v53 GREEN primitive-count tier (~24 primitives — 4 READMEs + 20 deep-dive reports)
- Estimated time: ~2h baseline preserved (within +/-10% normal variation)

### Discipline streak preservation

- 17-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK (NEW LONGEST in corpus)
- 42nd consecutive Storm Bear meta-entity (v10-v53)
- Pattern Library ratio 0.474:1 PRESERVED 3 CONSECUTIVE CYCLES (largest buffer in corpus history)

---

## Part 10 — Closing strategic context

### v53 corpus contribution summary

- **Pattern #38 strengthens to N=2** with NEW sub-variant 38b (single-tool-internals-deep-dive) — promotion-candidate at next mini-audit
- **Pattern #29 absent-LICENSE 4th sub-context** formalization-candidate (29-absent-4 research-only-non-commercial-restriction)
- **Pattern #75 strengthens to N=2** with mechanism-divergence caveat (DO NOT auto-promote)
- **8+ patterns strengthened** without status change (#19 / #22 / #12 / #27 / #18 / #57-negative / cross-tier CN / archive-genre i18n)
- **Adversarial-Anthropic-positioning** N=2 observational documented (omo v52 + v53; mechanisms differ; consolidation-forward)
- **17-consecutive-wiki zero-registration streak NEW LONGEST** in corpus history
- **CORPUS-RECORD 168.2% fork-to-star inversion** (NEW corpus first; exceeds bizos v37 138%)
- **42nd consecutive Storm Bear meta-entity** (per-wiki applicability check PASS)

### Storm Bear operator caveats

- 6 operational caveats for daily Claude Code use (E4 entity page)
- Reference-only (research-only license blocks commercial Scrum coaching re-use)
- Sample-verify Sanbu's claims (not Anthropic-confirmed)
- Static abandoned-day-2 archive (may be partially stale at 25+ days)

### v27 diagnostic HIGH bundle backlog

- **33 SESSIONS DEFERRED** post-v53 (v28-v53 inclusive)
- 6.6× routine v2.1 5-session threshold
- 18th consecutive force-continuation (v36-v53)
- BLOCKING-RECOMMENDATION escalated
- v53 contributes operational-awareness reference but NOT vault-refactor template (research-only license blocks adoption of any structural pattern from this archive)
- **STRONGLY RECOMMENDED**: Execute v27 diagnostic HIGH bundle before v54 (~6-8h session) OR run mini-audit at next operator-trigger to action 17+ accumulated promotion-candidates (~30-60 min)

### Forecast for v54+

- Pattern Library ratio 0.474:1 with 0.476 buffer = no audit needed at v54 unless +9 candidates emerge
- 17-streak likely sustainable at v54 if next wiki is well-pre-checked
- v27 backlog at 33 sessions is decisively the next-highest-ROI action

---

## Cross-references

- E1 — Core archive (5-doc + roadmap)
- E2 — Pattern implications (#38 / #29 / #75 detailed analysis)
- E3 — Sanbu / abandoned-day-2 mystery / fork-inversion analysis
- E4 — 42nd Storm Bear meta-entity (operational caveats)
- C1, C2, C3 — Cluster summaries
- 03 Beginner Guide — Bilingual VN+EN with operational caveats
- system-prompts-leaks v21 — Sister-archive parent of Pattern #38
- bizos v37 — Sister-observation parent of Pattern #75
- PATTERN_LIBRARY.md — vault root (Phase 5 mandatory update)
- vault root CLAUDE.md — Phase 6 mandatory update (state post-v53 block + project entry)
- GOALS.md — Phase 6 session 63 entry
