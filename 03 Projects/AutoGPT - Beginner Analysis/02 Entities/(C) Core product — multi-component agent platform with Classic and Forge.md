# (C) Core product — Multi-component agent platform with Classic and Forge

> **Entity 1 of 4** — AutoGPT v59
> **Type:** Core product entity (13-section canonical)

---

## 1. What it is (one-line)

`Significant-Gravitas/AutoGPT` is a multi-component autonomous-agent monorepo — currently in mid-transition between the original 2023 community-viral standalone agent (Classic + Forge, MIT-licensed) and the in-development cloud-tier Platform (PolyForm-Shield-licensed) — 184K stars, 2nd-largest pure-product in corpus.

## 2. Verbatim positioning

> "AutoGPT is the vision of accessible AI for everyone, to use and to build on."

> "Our mission is to provide the tools, so that you can focus on what matters."

## 3. Architecture overview

**Multi-component monorepo** with 3 distinct tiers within single repo:

| Component | Folder | Tier | License | Status |
|---|---|---|---|---|
| **AutoGPT Platform** | `autogpt_platform/` | T1 (agent-building platform) | PolyForm Shield | NEW in-development primary |
| **AutoGPT Classic** | `classic/` (root) | T5 (standalone agent application) | MIT | Original 2023; legacy maintenance |
| **AutoGPT Forge** | `classic/forge/` | T1↔T5 bridge (toolkit) | MIT | Agent-developer toolkit |
| **Benchmark** | `classic/benchmark/` | Eval harness | MIT | Agent performance evaluation |
| **Frontend** | (within classic/) | UI layer | MIT (TypeScript) | UI for Classic + bridges Platform |

**Multi-tier monorepo at T1+T5 within single repo** = corpus-first explicit T1+T5 convergence. Distinct from n8n v56 single-T2 with multiple integrations + distinct from gh-aw v48 multi-tier workflow-automation.

**Primitive count ≥7** = 7th EXTREME-tier subject in corpus (joins ruflo v42 + aidevops v47 + gh-aw v48 + awesome-claude-skills v50 + oh-my-openagent v52 + n8n v56). Pattern #69 EXTREME primitive-count formal-statement extension candidate at v60.

## 4. Key architectural choices

**Choice 1 — Multi-component monorepo with explicit tier-divergence:**
Platform (new, cloud-tier, restricted-license) lives alongside Classic (original, standalone, permissive-license) in single repo. README explicitly differentiates: "in-development platform" vs "original stand-alone AutoGPT Agent."

**Choice 2 — Dual-licensing strategy:**
PolyForm-Shield restricts use as competing service for autogpt_platform/ (the commercializable surface). MIT for Forge + Classic + sister projects (the community + ecosystem surface). Pattern #45 + #72 + #29 strengthening.

**Choice 3 — Agent Protocol standardization:**
Employs Agent Protocol from AI Engineer Foundation (older + narrower than MCP introduced by Anthropic 2024). Pattern #18 NEW protocol-axis distinct from MCP-axis.

**Choice 4 — Both AGENTS.md AND CLAUDE.md present at root:**
Most corpus subjects have one or the other. AutoGPT 2-file coexistence = Pattern #22 strengthening sub-observation.

## 5. Distribution surfaces (Pattern #2)

**6+ distribution surfaces:**
1. GitHub repo (open clone)
2. Docker (autogpt_platform deployment)
3. agpt.co (cloud-tier hosted commercial platform)
4. Classic AutoGPT standalone install (CLI clone-and-run from classic/)
5. Forge toolkit (developer-extension entrypoint)
6. Frontend UI distribution (likely npm-based for TS-portion)
7. AutoGPT Platform-beta released versions (latest `autogpt-platform-beta-v0.6.58` April 29, 2026)

**Pattern #2 distribution-evolution strengthening at N=10+** data point.

## 6. Authority construction

**First-mover authority WITHOUT lineage citation.**

AutoGPT pioneered the autonomous-agent paradigm in March-April 2023 viral inflection. Authority comes from being THE catalyst that triggered the entire 2023 autonomous-agent wave (every later corpus subject inherits this paradigm — explicit agent-loop + tool-use + memory paradigm).

**Distinct from 4 other corpus authority-construction modes:**
- **Citation-supported authority:** mattpocock v57 cites Pragmatic+DDD+XP+Philosophy books
- **Personal-claim authority:** automate-faceless-content v55 "OG AI Wizard" self-claim
- **Corporate-organizational authority:** spec-kit v17 GitHub Microsoft official entrant
- **Pseudonymous-org authority:** OpenSpec v58 Fission-AI hidden members

**NEW Pattern #19 sub-variant candidate first-mover-authority-without-lineage** N=1 stale-flagged v64/v69. Promotion path: 2nd first-mover-authority subject (e.g., LangChain hypothetical / Anthropic's MCP origin / OpenAI's GPT origin if corpus includes) → variant-within-pattern-at-N=2.

## 7. Methodology (NONE explicit)

NO named-methodology citation in README at probe scope.

**Methodology absences:**
- NO SDD (vs spec-kit v17 + OpenSpec v58)
- NO TDD (vs mattpocock v57 `/tdd` skill)
- NO DDD (vs mattpocock v57 cites Eric Evans)
- NO XP (vs mattpocock v57 cites Kent Beck)
- NO BMM / BMAD (vs BMAD v11)
- NO GSD methodology (vs gsd-2 v54)

**Architectural pattern (implicit, not framed as methodology):** agent-loop + tool-use + memory-store paradigm. AutoGPT introduced this paradigm to mass adoption but does not name it as methodology.

## 8. Governance (HEAVY 7+)

11 governance files at root:
- README.md
- AGENTS.md
- CLAUDE.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- CITATION.cff
- LICENSE
- .pre-commit-config.yaml
- codecov.yml
- .deepsource.toml

Pattern #12 Governance-Depth refined v42 3-factor: HEAVY governance + commercial-org-stewardship + dual-licensing → fits HEAVY-governance baseline.

## 9. Cross-references to corpus siblings (≥3 mandatory)

- **n8n v56** — 2nd-largest pure-product (185K stars vs AutoGPT 184K); 7-year-mature commercial-org GmbH stewardship; founder-to-org transition; SUL custom-non-OSI license
- **Unsloth v23** — Pattern #45 Dual-Licensing N=1 precedent (Apache-2.0 + commercial); 35-wiki stale until v59 un-stale
- **GitNexus v33** — Pattern #72 PolyForm-Noncommercial N=1 precedent; 26-wiki stale until v59 un-stale-with-rename
- **gh-aw v48** — EXTREME primitive-count predecessor + multi-tier workflow-automation peer
- **OpenSpec v58** — corpus-broadest multi-platform (30+ tools); contrast: OpenSpec uses MCP-style + per-tool format-translation; AutoGPT uses Agent Protocol
- **mattpocock v57** — contrast: mattpocock cites 4 books for authority construction; AutoGPT cites NONE (first-mover-authority-without-lineage)

## 10. Tier placement

**T1 Assistant primary** (autogpt_platform/ = agent-building platform; multi-tenant agent runtime; agent-builder + workflow-management + monitoring)

**T5 Application secondary** (classic/ = standalone agent application; original 2023 release)

**Multi-tier subject** with primary classification T1 by recent center-of-gravity (autogpt_platform/ active development; classic/ legacy maintenance).

## 11. Pattern Library impact

| Pattern | Direction | Note |
|---|---|---|
| #2 distribution-evolution | STRENGTHEN | 6+ surfaces |
| #18 Layer 1 protocol consumer | STRENGTHEN | Agent Protocol NEW protocol-axis |
| #19 archetype 4 founder-personal → org-stewardship | NEW SUB-VARIANT N=2 | with n8n v56 |
| #19 first-mover-authority-without-lineage | NEW SUB-VARIANT N=1 stale-flagged v64/v69 | distinct from 4 prior authority-construction modes |
| #22 AGENTS.md + CLAUDE.md coexistence | STRENGTHEN | 2-file-coexistence rare |
| #27 community-viral | CORPUS-HISTORICAL-FOUNDATIONAL | peak-viral-2023 |
| #29 non-commercial-restriction-custom-license | STRENGTHEN | sub-context grows N=4 |
| #45 Dual-Licensing | UN-STALES | N=2 STRUCTURAL → promotion v60 |
| #57 forward-citation | BIDIRECTIONAL ABSENCE | informative absence at corpus-historical-foundational subject |
| #69 EXTREME primitive-count | STRENGTHEN | 7th data point |
| #72 PolyForm-Family-License | UN-STALES + RENAME | variant-within-pattern N=2 → promotion v60 |

## 12. Open questions

See `00 OPEN-QUESTIONS.md` Q1-3 (license-axis), Q4-7 (pattern-test), Q8-10 (architectural).

## 13. Storm Bear pilot relevance

**MEDIUM-LOW pending license-acceptability decision** at v60+. Multi-component complexity high; PolyForm-Shield restriction needs explicit Storm Bear business-model alignment check; self-host infra not currently available. Pilot ranking estimate BELOW Top-5.
