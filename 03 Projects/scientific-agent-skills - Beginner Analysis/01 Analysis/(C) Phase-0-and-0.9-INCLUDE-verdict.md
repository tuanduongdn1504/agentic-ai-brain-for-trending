# (C) Phase 0 + Phase 0.9 INCLUDE verdict — scientific-agent-skills (v124)

**Routine:** v2.4. **Fetched:** 2026-05-30 (GitHub API + README + README detail + org page + root-contents listing). **Verdict:** **STRONG INCLUDE 3/4** ((a) FAIL US-commercial-org; (b) MODERATE; (c) STRONG; (d) STRONG). 2nd clean PASS after the v122 dograh OVERRIDE.

> ⚠️ **Cadence:** v124 is the **projected natural-audit window AND the mandated Phase-0.9 override-review window** (v122's first-ever 2-in-20 trip). The cadence sanctioned "v121+ = wikis OK" through ~v124–v125, so this clean in-scope wiki at v124 is within discipline — but **v125 = a HARD audit** (mandated override-review + "(a)-rescue N=2" + natural cadence), no further wiki deferral.

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `K-Dense-AI/scientific-agent-skills` |
| License present | ✅ **MIT** (per-skill licenses may vary in `SKILL.md`) |
| Active / recently pushed | ✅ pushed 2026-05-28; created 2025-10-19 (~223 days); **83 releases**, v2.45.0 |
| Scale floor (≥1★) | ✅ **26,567★** / 2,750 forks (fork_ratio 0.10) — mega-scale |
| Tier classification | **T1 Assistant Skill / Domain-Vertical-Skill-Collection** (scientific-research vertical) — CONFIRMED archetype, this = **N=5** |

**Phase 0 = PASS, and genuinely in-scope.** This is an **agentskills.io-standard skill collection** (141/142 `SKILL.md` skills in `skills/`) targeting Claude Code (+ Cursor / Codex / Antigravity / Gemini CLI / Claude Cowork). It is the corpus's bread-and-butter archetype — unlike the prior two builds (v122 dograh voice-AI override; v123 MoneyPrinterTurbo faceless-video (a)-rescue), this one is squarely on the agent-skills axis the corpus tracks.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **FAIL**

Owner = **K-Dense Inc.** (`owner.type: Organization`, branded "K-Dense AI"), bio "A world leader in empowering scientists with AI agentic tools," **location United States**. It is a commercial AI-science startup (Series-backed profile; hosted platform "K-Dense Web" + free OSS desktop app "K-Dense BYOK"; active X/LinkedIn/YouTube brand). None of the (a) sub-axes apply:
- Not a VN/Asian indie cultural-peer ((a)-1…(a)-6).
- Not **(a)-7 Foundational-Vendor-Direct-Source** — the vault depends on Anthropic/Claude, not on K-Dense. (K-Dense is a *third-party* skill author, like v114 GreenSock, not a substrate vendor.)

Mirrors v114 gsap-skills (US commercial org → (a) FAIL) and v98 (third-party, (a) FAIL). **(a) FAIL — clean.**

### (b) Goal-relevance / vault-utility — **MODERATE**

Two-sided, like v119 nature-skills:
- **Off-vertical:** the 141 skills are scientific (genomics, drug discovery, cheminformatics, clinical, proteomics, materials…) — not Storm Bear's software-dev / Scrum vertical. As *daily-use tools*, near-zero relevance.
- **But on-methodology:** it's a **Claude-Code agentskills.io skill library**, and goal #1 is "master Claude and autonomous agents for software development." As a **skill-authoring exemplar** — how to structure 141 `SKILL.md` skills, enforce spec-compliance (CONTRIBUTING), version them, security-scan them (Cisco AI Defense), and distribute multi-harness — it is directly studyable for the vault's own skill-authoring.

Per §10 (cost × relevance): LOW cost-of-trial (`npx skills add`, reversible) × INDIRECT-but-real (methodology, not domain) = **MODERATE**. Deliberately not inflated to STRONG (the *domain* is off-vertical) nor deflated to WEAK (the skill-authoring value is genuine and goal-adjacent). Matches v119 nature-skills' (b) MODERATE exactly.

### (c) Instructive / exemplary — **STRONG**

One of the largest and most mature domain-vertical skill libraries in the corpus:
- **141/142 skills × 17 domains** + **78–100+ scientific databases** (unified database-lookup skill + specialized integrations).
- **Published skill-supply-chain security:** weekly **LLM-based security scans via Cisco AI Defense Skill Scanner**, results committed to a **518 KB `SECURITY.md`**; contributor command `skill-scanner scan … --use-behavioral`. This is a notably mature skill-security discipline.
- **Spec-compliance enforcement:** every skill requires valid `SKILL.md` frontmatter + quoted `metadata.version`; CONTRIBUTING enforces the Agent Skills spec; `scan_skills.py` / `scan_pr_skills.py` tooling.
- Reusable foundation for the free **K-Dense BYOK** desktop co-scientist (BYO keys, 40+ models, optional Modal cloud).

This is an exemplary model for *authoring + validating + securing* a large Claude-skill library. **(c) STRONG.**

### (d) Corpus connectivity — **STRONG**

- **agentskills.io 57k chain — 12th implementer** (after v119 nature-skills = 11th per the v120 reconciliation): v76→v93→v98→v99→v100→…→v119→**v124**.
- **T1 Domain-Vertical-Skill-Collection → N=5** (v64 SEO + v90 academic + v98 cybersecurity + v119 nature + v124 scientific) — CONFIRMED archetype.
- **Direct v119 nature-skills sibling** — both 2026 scientific/academic agentskills.io domain libraries with bundled scientific data access (v119 bundled an MCP retrieval server; v124 unifies 100+ databases via a skill).
- **Pattern #84 multi-harness** (6: Claude Code / Cursor / Codex / Antigravity / Gemini CLI / **Claude Cowork**).
- **Pattern #66 supply-chain** — published automated skill-security-scanning (N=2 with v76).
- **Corpus-recursive Karpathy-echo** — K-Dense ships a repo literally named **`karpathy`** ("agentic machine learning engineer," 1,447★) + `agentic-data-scientist`; a methodology-lineage wink given the vault is built on Karpathy's LLM-wiki pattern.
- **"Claude Scientific Skills → Scientific Agent Skills"** rename = a Claude-exclusive→open-standard broadening (Pattern #57 standard-adoption arc).

**(d) STRONG.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer / (a)-7 | **FAIL** — K-Dense Inc., US commercial AI-science startup; not a peer, not a substrate vendor |
| (b) goal-relevance / vault-utility | **MODERATE** — off-vertical domain, but a Claude-Code agentskills.io skill-authoring exemplar (cf. v119) |
| (c) instructive | **STRONG** — 141-skill / 17-domain library + published security-scanning + spec-compliance enforcement |
| (d) corpus connectivity | **STRONG** — 57k 12th-implementer + T1 Domain-Vertical N=5 + v119 sibling + 6-harness + #66 + Karpathy-echo |

**STRONG INCLUDE 3/4** — INCLUDE rests on (b)(c)(d); (a) FAILs honestly. Same shape as v114 gsap-skills and v98 cybersecurity (3/4, (a) FAIL + (b) MODERATE + (c)(d) STRONG).

**Finding-2 calibration note:** (a) genuinely FAILED (US commercial org) and was not laundered; (b) held at MODERATE (not STRONG — the domain is off-vertical; not WEAK — the skill-authoring value is real). Honest discrimination, consistent with v119 nature-skills.

**Streak:** "48+3\*" → **"49+3\*"** (49 PASS + 3 OVERRIDE; v124 = 2nd clean PASS after the v122 dograh override — v123 was 1st). Clean PASS, does not add to override count.

## Pilot

**Conditional / reference pilot** — the most actionable skill-authoring exemplar of the recent builds. Worth *reading* a few `SKILL.md` files + the CONTRIBUTING spec-compliance + the Cisco-AI-Defense security-scan setup as a model for the vault's own Claude skills; `npx skills add` is reversible if a scientific skill is ever useful. Not a daily-use tool (off-vertical); does not join the operational Claude-Code stack.
