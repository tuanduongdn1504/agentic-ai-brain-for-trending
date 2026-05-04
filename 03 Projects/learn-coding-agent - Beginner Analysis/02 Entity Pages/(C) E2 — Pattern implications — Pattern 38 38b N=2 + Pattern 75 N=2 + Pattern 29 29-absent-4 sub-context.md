# E2 — Pattern implications: Pattern #38 38b N=2 + Pattern #75 N=2 + Pattern #29 29-absent-4 sub-context

> **Type:** Entity page (pattern-library impact summary)
> **Wiki #53**

---

## Summary of Pattern Library delta at v53

| # | Action | Status |
|---|--------|--------|
| Streak | Extends zero-new-active-candidates to **17 CONSECUTIVE WIKIS (v37-v53) — NEW LONGEST in corpus history** | ✅ |
| New active candidates | **0** | ✅ |
| New top-level OBSERVATION-TRACKs | **0** | ✅ |
| New sub-variants / sub-contexts within existing patterns | **3** (#38 38b, #29 29-absent-4, #75 strengthening with mechanism caveat) | — |
| Patterns strengthened (no status change) | **8+** (#19 / #22 / #12 / #27 / #18 / #57-negative / cross-tier CN / archive-genre i18n) | — |
| Promotion candidates accumulated post-v53 | **17+** cumulative across v45-v53 | — |

---

## NEW sub-variant 1: Pattern #38 38b single-tool-internals-deep-dive

### Current state of #38 (pre-v53)

🟡 #38 Prompt-Leak-Archive Genre — CANDIDATE since v21 (system-prompts-leaks N=1).

**Formal statement (v21):** *"Prompt-leak-archive genre: repositories aggregating system prompts extracted from closed-source commercial AI tools. Characterized by: (a) content = extracts not originals; (b) sources = closed-source commercial; (c) legal position = gray zone; (d) author often pseudonymous; (e) monetization = patronage + commercial derivative common; (f) extraction methods typically not documented."*

### v53 addition

learn-coding-agent v53 reverse-engineers ONE specific tool's INTERNALS (Claude Code v2.1.88 telemetry / codenames / undercover / killswitches / roadmap) — distinct from v21's collection of SYSTEM PROMPTS from 31 AI tools.

### Sub-variant taxonomy proposal

| Sub-variant | Wiki | Subject scope | Content |
|-------------|------|---------------|---------|
| **38a multi-tool-prompt-archive** | system-prompts-leaks v21 | 31 AI tools (broad) | System prompts as primary content |
| **38b single-tool-internals-deep-dive NEW v53** | learn-coding-agent v53 | 1 AI tool (Claude Code v2.1.88) | Architecture + telemetry + codenames + killswitches + roadmap |

### Promotion analysis

**Structural-N=2 promotion criterion check** (v2.1):
- ✅ N=2 distinct sub-variants identified
- ✅ Both fit broader formal statement (extracts of closed-source commercial AI tools, gray legal position, etc.)
- ⚠️ Sub-variant authorship divergence: v21 pseudonymous (x1xhlol multi-handle) vs v53 named-but-low-identity (Sanbu / Mars / blog-active)
- ⚠️ Monetization divergence: v21 has 6-channel patronage + ZeroLeaks commercial derivative; v53 has zero monetization signals
- ⚠️ Extraction-method divergence: v21 method opaque (likely tool-author leaks / community shares); v53 explicit "publicly available online references and discussions"

**Recommendation**: Register as **promotion-candidate at next mini-audit** under structural-N=2-sub-variant criterion. Mini-audit can:
- (a) PROMOTE #38 to CONFIRMED with both 38a + 38b sub-variants formalized
- (b) GENERALIZE #38 formal statement to "AI-tool-disclosure-archive genre" wrapping both
- (c) STAY CANDIDATE if sub-variant divergences (authorship + monetization + extraction-method) deemed too large

Operator overlap-resolution required at mini-audit.

---

## NEW sub-context 2: Pattern #29 29-absent-4 research-only-non-commercial-restriction

### Current state of #29 (post-v52)

✅ #29 License-Category-Diversity — CONFIRMED at v21. 4 sub-categories formalized at v50 mini-audit + extended at v52.

| Sub-context | Wiki | Description |
|-------------|------|-------------|
| 29-absent-1 | bizos v37 | Commercial-cold-start + README-proprietary-claim |
| 29-absent-2 | dive-into-llms v39 | Academic-public-welfare + no-claim |
| 29-absent-3 | awesome-claude-skills v50 + vercel-labs v51 | README-OSI-license-claim-without-LICENSE-file |
| **29-absent-4 NEW v53** | **learn-coding-agent v53** | **Research-only-non-commercial-restriction-without-LICENSE-file + Copyright-disclaimer** |

### v53 evidence

README §"Copyright & Disclaimer" verbatim:
```
This repository is provided strictly for technical research and educational purposes.
Commercial use is strictly prohibited.

If you are the copyright owner and believe this repository content infringes your rights,
please contact the repository owner for immediate removal.
```

- **No LICENSE file** in repo
- **Informal commercial-restriction** in README only (no legal-license weight; goodwill signal)
- **DMCA-style takedown clause** (acknowledges potential third-party rights infringement)
- **Default copyright applies** (international Berne Convention default = all rights reserved)

### Recommendation

Sub-context formalization-candidate at next mini-audit. Mini-audit decides whether to formally enumerate 29-absent-4 in Pattern #29 statement.

### Cross-corpus comparison

learn-coding-agent v53's license stance is structurally similar to v52 oh-my-openagent's SUL-1.0 (Sustainable Use License = non-commercial-restriction custom-non-OSI):
- Both restrict commercial use
- Both allow research/personal use
- v52 omo has formal SUL-1.0 license-text ↔ v53 has informal README-only declaration
- Different enforceability (formal license > README-only)

→ Both are part of broader "non-commercial-restriction" license-philosophy cluster (also includes PolyForm Noncommercial 1.0.0 from GitNexus v33 Pattern #72).

---

## NEW strengthening 3: Pattern #75 N=2 with mechanism-divergence caveat

### Current state of #75 (post-v37)

🟡 #75 Template-Use Fork-Star Anomaly at Cold-Start — OBSERVATION-TRACK NEW v37 (bizos N=1; 138% inversion at 2-day-old commercial-app).

### v53 addition

learn-coding-agent v53: **168.2% fork-to-star inversion** (19,741 forks vs 11,735 stars) — **NEW CORPUS-RECORD** exceeding bizos v37's 138% by 30 percentage points.

### Mechanism comparison (CRITICAL — must flag for mini-audit)

| Wiki | Inversion ratio | Repo age | Subject type | Hypothesized mechanism |
|------|-----------------|----------|--------------|------------------------|
| bizos v37 | 138% | 2 days | Commercial app (Next.js business OS template) | **Template-use** (forks for own deployment of business OS template) |
| **learn-coding-agent v53** | **168.2% (NEW RECORD)** | **25 days (abandoned day-2)** | **Research archive (markdown-only, no code)** | **MECHANISM UNCLEAR** — possibilities: (a) CN-class-assignment-fork (CN academic culture: students fork for course assignments); (b) mass-fork-bot (CN GitHub ecosystem has known fork-farm activity); (c) fork-as-bookmark (CN-GitHub-culture fork-instead-of-star convention); (d) attempt-to-self-host-mirror; (e) fork-to-translate-adapt |

### Why mechanism caveat matters

bizos = template-use mechanism is structurally clean (Next.js project explicitly designed for cloning + deploying). 168% inversion is rational for a deployable template at 2-day-old.

learn-coding-agent = mechanism is structurally unclean (markdown-only archive; nothing to deploy; no code to fork-and-modify). 168% inversion at 25-day-old abandoned-archive is anomalous.

**If mechanisms differ, Pattern #75 may need to split into:**
- **75a template-use-fork-amplification** (bizos)
- **75b CN-cultural-fork-pattern OR fork-bot-amplification** (learn-coding-agent — uncertain)

OR Pattern #75 may need to STAY OBSERVATION-TRACK at N=2 with explicit mechanism-divergence flag rather than auto-promote.

### Recommendation

**DO NOT auto-promote at v53.** Register Pattern #75 as N=2 OBSERVATION-TRACK strengthening with explicit mechanism-divergence caveat for mini-audit overlap-pre-check. Mini-audit can:
- (a) PROMOTE if mechanisms can be unified under broader "fork-amplified-cold-start" framing
- (b) SPLIT into 75a + 75b sub-variants
- (c) STAY OBSERVATION-TRACK if N=2 insufficient to disambiguate

---

## Patterns strengthened without status change (8+)

### Pattern #19 archetype 4 no-explicit-individual-lineage

learn-coding-agent README explicit: *"All materials are compiled entirely from publicly available online references and discussions"* → community-amalgam citation pattern; no individual influence node. Strengthens archetype 4 (community-viral-no-lineage) at outside-scope tier.

### Pattern #22 AGENTS.md absence at archive-genre minimum-governance

ZERO governance files (no AGENTS.md / no CLAUDE.md / no CONTRIBUTING / no SECURITY / no CODE_OF_CONDUCT). Reinforces archive-genre minimum-governance baseline (similar to system-prompts-leaks v21 + bizos v37).

### Pattern #12 Governance-Depth refined-formulation 8th baseline-fits wiki

v42 refined formulation predicts: solo + low-maturity-ambition + small-scale-tier → minimum governance. v53 fits perfectly:
- Solo CN researcher
- Research-archive-philosophy (NOT product)
- Functionally cold-start (25 days, abandoned-day-2)
- Minimum governance (4 READMEs, 0 governance files)

→ Strengthens refined formulation; NOT counter-evidence.

### Pattern #27 Community-Viral 22nd observation with cold-start sub-path counter-evidence-narrowing

11.7K stars / 25 days = ~470 stars/day = fast-cold-start star velocity. **BUT** the dominant amplification mechanism appears to be FORK not STAR (168% inversion). This is counter-evidence to the implicit Pattern #27 assumption that community-viral = star-amplified. Sub-path: community-viral via fork-amplification distinct from star-amplification.

→ Pattern #27 strengthens with new observational sub-path (no formal action yet; flag for mini-audit if N=2 fork-amplified emerges).

### Pattern #18 Agent Runtime Standardization observational

Subject of v53 IS Claude Code (Layer 2/3 runtime per #18 v36 + v52 refinements). v53 archive STUDIES Claude Code internals → orthogonal to runtime-standardization pattern. Strengthen-only with no formal action.

### Pattern #57 Recursive Corpus Reference — NEGATIVE confirmation

learn-coding-agent docs do NOT cite specific Storm Bear wikis. NOT 57a (no direct citation), NOT 57b (no compound 2-wiki cross-corpus), NOT 57c (no forward citation in README/docs to specific corpus subjects). Subject (Claude Code) is implicitly substrate of MANY corpus T1 wikis but learn-coding-agent does not name them. **No Pattern #57 hit at v53.**

### Cross-tier CN observational

CN-author wikis in corpus across tiers:
- TrendRadar v19 (outside-scope CN news aggregator)
- dive-into-llms v39 (T3 academic CN lab)
- MiroFish v49 (commercial-startup CN)
- **learn-coding-agent v53** (outside-scope CN research-archive)

→ N=4 CN-authors across 3 distinct tiers. Cross-tier CN observation strengthens but insufficient mechanism distinction for new candidate. Strengthen-only.

### Archive-genre i18n strengthening

Quadrilingual EN+CN+JA+KO at outside-scope is strong-mid-tier. Reinforces observation that archive-genre at outside-scope often has substantial i18n breadth (system-prompts-leaks v21 not multi-lang; this v53 is). Insufficient for pattern; strengthen-only.

### Adversarial-Anthropic-positioning observational N=2 (with mechanism-divergence)

| Wiki | Anti-Anthropic mechanism |
|------|--------------------------|
| oh-my-openagent v52 | Competitive anti-lock-in framing — "Anthropic blocked OpenCode because of us" + "Claude Code's a nice prison" |
| **learn-coding-agent v53** | Reverse-engineering disclosure — telemetry-no-opt-out / undercover-mode / remote-killswitches / GrowthBook-flag-without-consent disclosure |

**Mechanisms differ**: omo = competitive-positioning; v53 = reverse-engineering-disclosure. Insufficient for new pattern candidate (consolidation-forward discipline). Document N=2 observational for mini-audit attention; do NOT register standalone candidate.

---

## Pattern Library state at v53

**Pre-v53 (post-v52):** 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 18:38 = **0.474:1** (largest buffer 0.476 below 0.95:1 mini-audit trigger; preserved 2 cycles).

**Post-v53:** **38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 18:38 = 0.474:1 PRESERVED 3RD POST-v50-MINI-AUDIT CYCLE** (largest buffer in corpus history maintained 3 consecutive wikis: v51 + v52 + v53).

**17 promotion-candidates accumulated post-v53** (cumulative v45-v53):
- v53 NEW (3): #38 38b structural-N=2 + #29 29-absent-4 sub-context + #75 N=2 mechanism-divergence-flagged
- v52 carry (5): #57 57c structural-N=2 + #18 OpenCode-primary structural-N=2 + #29 SUL-1.0 sub-context + #58 58c sub-variant + #50 50d sub-variant
- v51 carry (9): #22 22d identical-mirror + #57 57c + #29 29-absent-3 + #29 AGPL-at-project-scope + #50 50b + #66 OT sub-categorization + #18 4-layer + #22 22c scope-narrowing + #47 retirement carry-forward

**Mini-audit warranted at next operator-trigger** (~30-60 min for 17 candidates).

---

## Cross-references

- E1 — Core archive (5-doc + roadmap)
- E3 — Sanbu / sanbuphy.cn ecosystem (author profile + abandoned status)
- E4 — 42nd consecutive Storm Bear meta-entity (Claude Code operational caveats)
- C2 — Full 5-doc content
- 04 Phase 4b Deliverable — Comprehensive pattern analysis with promotion-candidate breakdown
- PATTERN_LIBRARY.md — vault root (mandatory Phase 5 update)
