# (C) Cluster — Combined source summary

> **AutoGPT v59 source ingestion** (compressed-scope at EXTREME tier per v56 lesson)
> Single combined cluster covering: GitHub repo metadata + README positioning + LICENSE structure + multi-component repo architecture + Agent Protocol citation

---

## 1. Repo metadata (verbatim from WebFetch + api.github.com)

**Repo:** `Significant-Gravitas/AutoGPT`
**Created:** 2023-03-16 (~3.13 years operational at v59 probe)
**Last push:** 2026-05-07 (today; actively maintained)
**Default branch:** `master` (rare in corpus — 3rd master after build-your-own-x v8 + n8n v56)
**Repo size:** ~564 MB
**License declared:** NOASSERTION (GitHub API), actual = **dual MIT (most files) + PolyForm Shield License (autogpt_platform/ folder)**

**Community metrics:**
- Stars: **184,043** (XX-Large; **2nd-largest pure-product in corpus** behind n8n v56 185,728; Microsoft build-your-own-x 491K is tutorial-aggregator outside-scope)
- Forks: 46,246 (25.1%)
- Watchers: 1,500
- Open issues: 254
- Pull requests: 149
- Commits: 8,477
- Contributors: not extracted at probe scope

**Languages:** Python 69.0% + TypeScript 29.4% (Python-primary + TS-secondary hybrid; 1st corpus Python-primary+TS-secondary at T1)

**Topics:** agentic-ai / agents / ai / artificial-intelligence / autonomous-agents / claude / gpt / llama-api / llm / openai / python (LLM-agnostic broad positioning)

**Latest release:** `autogpt-platform-beta-v0.6.58` (April 29, 2026) — actively-released; "beta" marker in version string

**Homepage:** agpt.co (commercial cloud-tier hosted platform)

---

## 2. Author + organization attribution

**Organization:** **Significant-Gravitas** (GitHub org)

**Founder:** **Toran Bruce Richards** — created AutoGPT March 2023; original solo-developer of viral-2023 release. Public-attribution preserved through org-stewardship transition (founder name remains publicly known despite org-scale-commercial growth).

**Sister projects (Significant-Gravitas org):**
- **GravitasML** — MIT licensed
- **Code Ability** — MIT licensed

**Org-portfolio pattern:** flagship dual-licensed (AutoGPT MIT+PolyForm-Shield) + sister projects MIT-baseline. Pattern #2 + Pattern #17 variant 1 strengthening.

---

## 3. Repository structure (top-level)

```
.agents/          ← agent configuration
.claude/          ← Claude-specific config
.github/          ← workflows
.vscode/          ← editor config
autogpt_platform/ ← NEW Platform codebase (PolyForm-Shield licensed)
classic/          ← original AutoGPT + Forge + benchmark + frontend (MIT licensed)
docs/             ← documentation
[config files]    ← .branchlet.json / .deepsource.toml / .dockerignore / .gitignore / .nvmrc / .pre-commit-config.yaml / .secrets.baseline
[governance]      ← README.md / AGENTS.md / CLAUDE.md / CONTRIBUTING.md / CODE_OF_CONDUCT.md / SECURITY.md / CITATION.cff / LICENSE / codecov.yml
```

**Multi-component sub-tier structure visible:**
- **AutoGPT Platform** (`autogpt_platform/`) = NEW in-development primary product; PolyForm-Shield licensed; T1-tier classification (agent-building platform)
- **AutoGPT Classic** (`classic/` root) = original 2023 standalone agent; MIT licensed; T5-tier (application-layer)
- **AutoGPT Forge** (`classic/forge/`) = toolkit for building custom agents; MIT licensed; T1/T5-bridge
- **Benchmark** (`classic/benchmark/`) = agent-evaluation harness
- **Frontend** = TypeScript-based UI

**Multi-tier monorepo at T1+T5 within single repo** = corpus-first explicit T1+T5 convergence (vs n8n v56 single-T2 with multiple integrations; vs gh-aw v48 multi-tier at workflow-automation; AutoGPT explicitly differentiates platform-tier vs application-tier in README).

**EXTREME-primitive-count classification confirmed** (7th in corpus; joins ruflo v42 + aidevops v47 + gh-aw v48 + awesome-claude-skills v50 + oh-my-openagent v52 + n8n v56). Primitive types ≥7: Platform / Classic / Forge / benchmark / frontend / docs / agents-config / .claude-config.

---

## 4. README primary positioning + key claims

**Verbatim tagline:** "AutoGPT is the vision of accessible AI for everyone, to use and to build on."

**Verbatim mission:** "Our mission is to provide the tools, so that you can focus on what matters."

**Core capabilities highlighted (4):**
1. **Agent Builder** — "intuitive, low-code interface" for customization
2. **Workflow Management** — "Build, modify, and optimize your automation workflows"
3. **Ready-to-Use Agents** — pre-configured options
4. **Monitoring** — "Keep track of your agents' performance and gain insights"

**Example use cases (in README):**
- Viral video generation from trending Reddit topics → automated short-form production
- YouTube video analysis → extract impactful quotes for social media distribution

**Notable absence in README:**
- NO Karpathy citation
- NO John Lam citation
- NO Boris Cherny / Anthropic-engineer citation
- NO SDD / TDD / DDD methodology citation
- NO book-citations like mattpocock v57 (Pragmatic / DDD / XP / Philosophy)
- NO corpus-subject citations (no spec-kit / no BMAD / no GSD / no OpenSpec / no n8n)
- NO anti-pattern foil framing (mattpocock v57 + OpenSpec v58 both used "real engineering vs vibe coding")

**Authority-construction observation:** AutoGPT's authority comes from **first-mover status** (March 2023 = THE catalyst for autonomous-agent boom). Distinct from:
- Citation-supported authority (mattpocock v57 books)
- Personal-claim authority (automate-faceless-content v55 "OG AI Wizard")
- Corporate-organizational authority (spec-kit v17 GitHub Microsoft)
- Pseudonymous-org authority (OpenSpec v58 Fission-AI)

**NEW Pattern #19 sub-variant candidate first-mover-authority-without-lineage** N=1 stale-flagged v64/v69. AutoGPT pioneered the autonomous-agent paradigm that virtually every later corpus subject inherits — but it does NOT cite predecessors and is not cited by successors in their READMEs.

---

## 5. License structure (verbatim from README LICENSE section)

**Dual-licensing structure:**
- **PolyForm Shield License** → `autogpt_platform/` folder (in-development Platform codebase)
- **MIT License** → everything else (Classic AutoGPT, Forge, sister projects GravitasML + Code Ability)

**PolyForm Shield license characteristics:**
- Source-available, NOT OSI-approved
- Permits use for any purpose EXCEPT building a competing product/service
- Distinct from PolyForm-Noncommercial (GitNexus v33) which restricts commercial use entirely
- Distinct from SUL (Sustainable Use License — n8n v56 / oh-my-openagent v52) which restricts hosting-as-service-to-third-parties

**Pattern #29 non-commercial-restriction-custom-license sub-context post-v59:**
| Wiki | Tier | License | Sub-flavor | Restriction-axis |
|---|---|---|---|---|
| GitNexus v33 | T5 | PolyForm-Noncommercial | non-commercial-entirely | commercial-use-restricted |
| oh-my-openagent v52 | T1 | SUL-1.0 | bespoke-non-OSI | hosting-as-service-restricted |
| n8n v56 | T2 | n8n-SUL | bespoke-non-OSI | hosting-as-service-restricted |
| **AutoGPT v59** | **T1+T5** | **PolyForm-Shield** | **standardized-non-OSI** | **competing-product-restricted** |

**4 distinct flavors across 4 tiers + 4 license-name-instances** = Pattern #29 sub-context most-richly-categorized in corpus.

**Pattern #45 Dual-Licensing structural observation post-v59:**
| Wiki | Tier | License pair |
|---|---|---|
| Unsloth v23 | T5 | Apache-2.0 + commercial |
| **AutoGPT v59** | **T1+T5** | **MIT + PolyForm-Shield** |

**N=2 STRUCTURAL across 2 tiers + 2 distinct license-pair-instances** = un-stale event at v59 + promotion-candidate criterion 2 structural-N=2 at v60 mini-audit.

**Pattern #72 PolyForm-family observation post-v59:**
| Wiki | PolyForm flavor | Restriction axis |
|---|---|---|
| GitNexus v33 | PolyForm-Noncommercial | commercial-use-entirely |
| **AutoGPT v59** | **PolyForm-Shield** | **competing-service-restricted** |

**N=2 STRUCTURAL across 2 distinct PolyForm-family flavors** = un-stale event at v59 + rename Pattern #72 to "Pattern #72 PolyForm-Family-License" with sub-variants 72a Noncommercial + 72b Shield + promotion at v60 under criterion 4 variant-within-pattern-at-N=2.

---

## 6. Agent Protocol citation + intellectual-influence

**README quote:** "Employs agent protocol standard by the AI Engineer Foundation"

**Agent Protocol** = standardization initiative by AI Engineer Foundation; older + narrower scope than MCP (Model Context Protocol introduced 2024 by Anthropic).

**Pattern #18 Layer 1 protocol-axis observation post-v59:**
| Wiki | Protocol consumed |
|---|---|
| n8n v56 | MCP (bidirectional Client + Server Trigger) |
| OpenSpec v58 | (no MCP citation; per-tool skill-format translation instead) |
| **AutoGPT v59** | **Agent Protocol** (AI Engineer Foundation) |

**NEW protocol-axis: Agent Protocol** (distinct from MCP) — corpus-first explicit Agent Protocol citation. Observational sub-axis at N=1; not promotion-tier at present.

**Intellectual-influence absences:**
- No Karpathy / Lam / Cherny / SDD / TDD / DDD methodology lineage
- Generic "accessible AI for everyone" vision-language
- Authority via FIRST-MOVER status (AutoGPT was THE pioneer)

---

## 7. Pattern Library implications synthesized

**STRENGTHENING (8 patterns):**
1. Pattern #45 Dual-Licensing UN-STALES → N=2 STRUCTURAL → promotion-candidate v60
2. Pattern #72 PolyForm-Family-License rename + UN-STALES → variant-within-pattern N=2 → promotion-candidate v60
3. Pattern #29 non-commercial-restriction-custom-license → N=4 sub-context taxonomy
4. Pattern #19 founder-personal → org-stewardship → N=2 sub-variant (with n8n v56)
5. Pattern #19 first-mover-authority-without-lineage → NEW sub-variant N=1 stale-flagged v64/v69
6. Pattern #27 community-viral → corpus-historical-foundational data point
7. Pattern #69 EXTREME primitive-count → 7th data point formal-statement-extension candidate
8. Pattern #22 AGENTS.md + CLAUDE.md coexistence → 2-file-coexistence sub-observation

**NEGATIVE / ABSENCE EVIDENCE (1):**
- Pattern #57 BIDIRECTIONAL-ABSENCE at corpus-historical-foundational subject (informative absence; OT or sub-observation candidate)

**0 NEW STANDALONE CANDIDATES** registered — all routed to within-pattern strengthening per consolidation-forward discipline. **23-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES streak NEW LONGEST extends v58 22-streak.**

---

## 8. Storm Bear pilot relevance

**MEDIUM-LOW pending license-decision at v60+.**

Constraints:
- PolyForm-Shield commercial-competition restriction (not absolute blocker but needs decision)
- Multi-component complexity high (vs OpenSpec v58 single-CLI-installer simplicity)
- Self-host requires infrastructure Storm Bear vault doesn't currently have
- agpt.co cloud-tier evaluation needed (paid commercial tier)

Potential value-adds (require concrete-use-case workshop):
- Agent Builder for autonomous sprint-metrics aggregation (vs n8n v56 workflow-builder)
- Forge toolkit for custom Scrum-agent development (vs OpenSpec v58 SDD framework)

**Pilot ranking estimate: BELOW Top-5** (claude-hud + claude-howto + OpenSpec + mattpocock + n8n likely ahead). Re-evaluate post-v60 mini-audit.

---

## 9. Velocity + scope notes for future reference

- 1 combined cluster (vs typical 3) — compressed-scope per v56 lesson at EXTREME tier
- Probe → cluster-summary ~15 min (compressed)
- All 12 Phase 0.5 observations routed to within-pattern strengthening with 0 new standalone candidates
- 2 strong un-stale events documented (Pattern #45 + #72) = corpus-rare double un-stale at single wiki
