# Subject — Anthropic-Cybersecurity-Skills

**Repo**: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
**Owner**: mukul975 (individual)
**Owner profile**: Mahipal (full name "Mahipal Jangra" inferred from Twitter @Mukul_jangra) + Berlin-located + Indian-name + SRH Berlin academic affiliation (via GARS-2026 study) + bio "🔐 Cybersecurity \| 💻 Dev \| 📷 Street Photographer 🎓 MSc \| 📚 Research & AI Security" + blog mahipal.engineer + 30 public repos + 375 followers + GitHub since 2018-08-31 (8-year account; hireable=true)
**Tier**: T1 Domain-Vertical-Skill-Collection (cybersecurity-vertical; same archetype-family as v64 claude-seo + v90 academic-research-skills; T1 sub-archetype N=3 PROMOTION-ELIGIBLE administrative at v100 audit with cross-vertical spread PASS)
**License**: Apache 2.0 (clean; with separate **CC-BY 4.0** declared for academic survey results published open access)
**Primary language**: Python
**Created**: 2026-02-25 (89 days old at v98 ship)
**Last push**: 2026-05-13 (12 days before fetch; actively maintained)
**Description**: "754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0"
**Homepage**: https://mahipal.engineer/Anthropic-Cybersecurity-Skills/
**Topics** (20): ai-agents + claude-code + cloud-security + cybersecurity + devsecops + ethical-hacking + incident-response + infosec + llm + malware-analysis + mcp + mitre-attack + nist-csf + osint + penetration-testing + red-team + security + security-automation + threat-hunting + threat-intelligence
**Discussions**: ENABLED

## Core metrics (v98 fetch, 2026-05-25)

| Metric | Value |
|---|---|
| Stars | 8,735 |
| Forks | 1,085 |
| Subscribers | 80 |
| Open issues | 16 |
| Velocity | 8,735 / 89 days = **~98.1 stars/day = Pattern #52 SUSTAINED-MODERATE-HIGH N=2 STRENGTHENING** (within 25-150/d sub-band; v77 anchor 91.7/d + v98 = 2-instance arc) |
| Fork ratio | 12.4% HIGH (well above median; reflects clone-and-adapt usage pattern at domain-vertical-skill-library scope) |
| Repo size | 11,360 KB (11.4 MB; substantial content) |

## What it is

**The largest open-source cybersecurity skills library for AI agents** (per README). 754 structured cybersecurity skills following the agentskills.io open standard, each mapped to 5 industry frameworks, covering 26 security domains, compatible with 26+ AI platforms.

Headline framing from README:

> Give any AI agent the security skills of a senior analyst
>
> A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. Your AI agent doesn't — unless you give it these skills.

## CORPUS-FIRST: Vendor-Branded Third-Party Repository Naming with Affiliation Disclaimer

Repo title is `Anthropic-Cybersecurity-Skills`. Owner is `mukul975` (NOT `anthropics` org). README contains explicit disclaimer:

> ⚠️ **Community Project** — This is an independent, community-created project. Not affiliated with Anthropic PBC.

This is **structurally distinct from the (a)-7 Foundational-Vendor-Direct-Source cluster** (v92 claude-for-legal + v93 anthropics/skills + v95 claude-plugins-official) where Anthropic PBC IS the owner. v98 USES the Anthropic brand in repo name for SEO/discoverability but is at third-party scale.

**Library-vocab PROVISIONAL N=1** registration at v98. Phase 4b PRIMARY proposal-document. v113 = 15-wiki forced-retire deadline if N=2 not reached.

## CORPUS-RECORD-HIGH 5-framework cross-mapping at domain-vertical-skill-library scale

| Framework | Version | Scope |
|---|---|---|
| MITRE ATT&CK | v18 | 14 tactics · 200+ techniques (adversary behaviors and TTPs) |
| NIST CSF 2.0 | 2.0 | 6 functions · 22 categories (organizational security posture) |
| MITRE ATLAS | v5.4 | 16 tactics · 84 techniques (AI/ML adversarial threats) |
| MITRE D3FEND | v1.3 | 7 categories · 267 techniques (defensive countermeasures) |
| NIST AI RMF | 1.0 | 4 functions · 72 subcategories (AI risk management) |

Each skill is mapped across all 5 frameworks. Example from README:

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |
|---|---|---|---|---|---|
| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 |

Exceeds prior corpus density records:
- v66 Pattern #78 78a PROMOTED at 3-standard (OWASP + NIST + MCP-spec)
- v71 agents-best-practices at 3-standard (OWASP + NIST + MCP-spec)
- v76 agent-skills-standard at 3-standard
- **v98 = 5-framework = NEW CORPUS-RECORD-HIGH** multi-standard-tracking density

Pattern #78 **NEW sub-mechanism candidate "5-Framework-Cross-Mapping at Domain-Vertical-Skill-Library Scale"** PROVISIONAL N=1.

## CORPUS-FIRST Progressive-Disclosure Architecture per Skill with Token-Cost Annotation

README explicitly documents the architecture:

> Each skill costs **~30 tokens to scan** (frontmatter only) and **500–2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 754 skills in a single pass without blowing context windows.

Token-cost annotation as design contract at data-structure layer = CORPUS-FIRST in v60+ window. Distinct from:
- v87 claude-comstyle: per-style %-token-impact at composition-axis
- v97 distill: product-level %-token-saving at runtime-axis
- **v98 progressive-disclosure-per-skill** at data-structure-axis

Together these form the **3-instance arc for Library-vocab "Token-Economy-Quantification" N=3 PROMOTION-ELIGIBLE** administrative at v100 audit (cross-axis spread PASS: composition + runtime + data-structure).

## Architecture

```
Anthropic-Cybersecurity-Skills/
├── skills/                          # 754 structured cybersecurity skills
├── mappings/                        # Cross-framework mapping artifacts
├── tools/                           # Supporting tooling
├── index.json                       # Master skill index (frontmatter-only scan)
├── ATTACK_COVERAGE.md               # MITRE ATT&CK coverage manifest at top-level (CORPUS-NOVEL)
├── CITATION.cff                     # Academic-citability discipline (mirrors v74 Manning pattern)
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                          # Apache 2.0
├── README.md                        # Substantial; badge-cluster + 26-domain table + 5-framework table + quick-start + GARS-2026 + Casky.ai
├── .claude-plugin/                  # Claude Code plugin manifest
├── .github/                         # CI/CD workflows
└── assets/banner.png                # README hero
```

## 26 security domains (from README)

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |
| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |
| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |
| Security Operations | 36 | SIEM correlation · log analysis · alert triage |
| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity |
| SOC Operations | 33 | Playbooks · escalation workflows · metrics |
| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |
| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |
| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |
| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |
| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |
| Deception Technology | 2 | Honeytokens · breach detection canaries |

Total: 26 domains × variable skill-counts = 754 skills.

## Installation

```bash
# Option 1: npx (recommended; same shorthand as v81/v82/v85/v90)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Compatibility: Claude Code + GitHub Copilot + OpenAI Codex CLI + Cursor + Gemini CLI + 20+ other agentskills.io-compatible platforms.

## GARS-2026 academic survey integration

Subject integrates academic research with OSS skill-library distribution. From README:

> 🌍 **GARS-2026 — Global Agentic AI Readiness Survey**
>
> I'm running a global academic study measuring how ready security professionals, developers, and enterprise teams actually are for agentic AI — MCP servers, tool calling, governance, and human-in-the-loop workflows.
>
> **If you use this repo, your response would be a genuinely valuable data point.**
>
> - 60 questions · Anonymous · Supervised by **SRH Berlin**
> - You get **50 Casky Tokens** for early access to casky.ai
> - Results published open access under **CC-BY 4.0**

CORPUS-FIRST observation: **Academic-Survey-Tied-to-OSS-Skill-Library** (SRH Berlin university supervision + CC-BY 4.0 dual-license at research-output layer + token-incentive). Library-vocab PROVISIONAL N=1.

## Casky.ai external-SaaS-playground integration

Subject links to external SaaS playground for live skill execution:

> 🚀 **Try it on the Playground**
>
> Experience Casky.ai hands-on — no setup required.
>
> The playground lets you:
> - Run live cybersecurity skill exercises against real targets
> - See AI agents execute structured skills in real time
> - Explore MITRE ATT&CK mapped workflows interactively
> - Test threat hunting, DFIR, and penetration testing scenarios

CORPUS-FIRST observation: **Casky.ai External-SaaS-Playground Integration with Token Incentive** (waitlist + 50-Casky-Token incentive tied to GARS-2026 survey). Distinct from v78 ECC OSS-with-hosted-Pro-SaaS-tier (RETIRED at v96 §18); v98 is incentive-tied-to-survey not paid-tier. Library-vocab PROVISIONAL N=1.

## Pattern Library cross-references

### Phase 4b PRIMARY: NEW Library-vocab "Vendor-Branded Third-Party Repository Naming with Affiliation Disclaimer" PROVISIONAL N=1

See `01 Analysis/(C) Vendor-Branded-Third-Party-Repository-Naming-with-Affiliation-Disclaimer-N1-registration.md` for full registration document.

### Library-vocab "Token-Economy-Quantification" N=3 PROMOTION-ELIGIBLE administrative at v100 audit

3-instance arc with cross-axis spread PASS:
- v87 claude-comstyle: per-style %-token-impact (composition-axis)
- v97 distill: product-level %-token-saving (runtime-axis)
- v98 Anthropic-Cybersecurity-Skills: progressive-disclosure-per-skill (data-structure-axis)

### T1 Domain-Vertical-Skill-Collection sub-archetype N=3 PROMOTION-ELIGIBLE administrative at v100 audit

3-instance arc with cross-vertical spread PASS:
- v64 claude-seo: SEO-vertical (anchor)
- v90 academic-research-skills: academic-vertical (N=2)
- v98 Anthropic-Cybersecurity-Skills: cybersecurity-vertical (N=3)

### Pattern #52 SUSTAINED-MODERATE-HIGH sub-class N=2 STRENGTHENING

- v77 easy-vibe: 91.7/d × 144d (anchor)
- v98: 98.1/d × 89d

Both within 25-150/d sub-band. Sub-class N=3 PROMOTION-ELIGIBLE pending one more anchor at v100+.

### Pattern #84 84c.1 sub-sub-mechanism N+1 post-CONFIRMED strengthening

8-instance arc: v85 + v90 + v92 + v93 + v94 + v95 + v97 + **v98**.
84c.1 remains CONFIRMED at N=6+ at 4-layer Pattern hierarchy (promoted at v96 audit).

### Pattern #78 NEW sub-mechanism candidate "5-Framework-Cross-Mapping at Domain-Vertical-Skill-Library Scale" PROVISIONAL N=1

5-framework cross-mapping (MITRE ATT&CK + NIST CSF + MITRE ATLAS + D3FEND + NIST AI RMF) exceeds prior 3-framework records.

### Pattern #57 NEW sub-variant candidate "Standards-Conformance-Layer Corpus-Recursive Chain (3-Implementer)" PROVISIONAL N=1

agentskills.io standard 3-implementer chain:
- v76 HoangNguyen0403/agent-skills-standard (anchor; first third-party implementer)
- v93 anthropics/skills (authoritative reference + spec at `./spec/` + template at `./template/`)
- **v98 mukul975/Anthropic-Cybersecurity-Skills (third-implementer at cybersecurity-vertical)**

### Pattern #45 NEW sub-typology candidate "Inter-License Boundary at Code-vs-Research-Output Layer" PROVISIONAL N=1

Apache 2.0 (code) + CC-BY 4.0 (GARS-2026 academic survey results) within same repo/project = corpus-novel inter-license boundary. Distinct from v74 sub-typology 45d (intra-Apache modification at book-content-exclusion).

### Pattern #82 quantitative-marketing strengthening

5 explicit quantitative claims at README header:
1. 754 structured skills
2. 26 security domains
3. 5 framework mappings
4. 26+ AI platforms
5. 4.8 million unfilled cybersecurity workforce roles (ISC2 2024 stat)

### Pattern #57 sub-variant 57c-product MID-STRONG citation density

6+ corpus-subject citations in product surface:
- Claude Code (v65 + v94 + v97)
- OpenAI Codex CLI (v62 + v85)
- Cursor (v75/v76)
- Gemini CLI (v77 + v82)
- GitHub Copilot
- Hermes Agent (corpus-recursive to v78 ECC + NousResearch/hermes-agent)

### Pattern #83 honest-deficiency-disclosure variant at repo-naming-affiliation layer

"⚠️ Community Project — Not affiliated with Anthropic PBC" disclaimer at README top = honest-deficiency-disclosure NEW sub-variant at **repo-naming-affiliation** axis (distinct from prior 83b harness-boundary disclosure + 83d product-feature deficiency + 83f.4 README-declared-LICENSE-vs-actual-mismatch).

### Pattern #66 supply-chain awareness within-pattern strengthening

5-framework cross-mapping at single subject = supply-chain coverage built into product surface as design contract. Distinct from Pattern #66 anchor v66 supply-chain-awareness at runtime/install-layer.

### Pattern #19 NEW sub-mechanism candidate "Indian-Diaspora-Berlin Solo-Academic Profile" PROVISIONAL N=1

Mahipal-Berlin-MSc-SRH-affiliated profile distinct from existing Pattern #19 sub-mechanisms (VN-Community Multi-Profile-Type CONFIRMED N=5 + Chinese-Mainland clusters + Munich-solo-founder + Brazilian-Solo-Dev v97 + ...). Adds to growing graveyard concern (~9-10 PROVISIONAL N=1 sub-mechanisms post-v97; v100 audit CONSOLIDATION review may be triggered if graveyard exceeds 10 candidates).

## Library-vocab PROVISIONAL N=1 registrations at v98

| # | Library-vocab | Distinguishing axis |
|---|---|---|
| 1 (PRIMARY) | Vendor-Branded Third-Party Repository Naming with Affiliation Disclaimer | repo-name-as-SEO + explicit-affiliation-disclaimer at third-party scale |
| 2 | Progressive-Disclosure Architecture per Skill with Token-Cost Annotation | data-structure-axis token-economy |
| 3 | Academic-Survey-Tied-to-OSS-Skill-Library (GARS-2026 / SRH Berlin) | OSS-skill-library + university-supervised-research + CC-BY 4.0 dual-license at output layer |
| 4 | Casky.ai External-SaaS-Playground Integration with Token Incentive | external-SaaS-playground + incentive-tied-to-survey (distinct from paid-tier) |
| 5 | Indian-Diaspora-Berlin Solo-Academic Profile (Pattern #19 sub-mechanism candidate) | profile-type axis |

## Honest deficiency-disclosure (what subject does NOT have)

- **Repo-name uses "Anthropic" brand without authorization** — README disclaimer addresses but does not eliminate trademark-ambiguity concern; legal exposure unaddressed.
- **No documented threat-model for the skills themselves** — skills could be used offensively; CONTRIBUTING.md + SECURITY.md exist but operator-side use-policy not stated.
- **No N=2 evidence yet for vendor-branded-third-party-naming Library-vocab** — pilot grades single-subject scope.
- **Mahipal "Mahipal Jangra" full-name + SRH Berlin affiliation inferred not confirmed** — Twitter handle @Mukul_jangra + GitHub bio "MSc" + survey supervised by "SRH Berlin"; no explicit binding statement in repo.
- **GARS-2026 survey + Casky.ai SaaS introduce monetization-adjacent attention-economy** — operator pilot should be aware of survey-incentive structure.

## Operator-applicability summary

**MEDIUM-RELEVANCE Tier-1 actionable pilot candidate position #4** (between distill v97 #3 and claude-comstyle v87 #5; DISPLACES claude-comstyle from #4 to #5). Pilot value is at **methodology-extraction layer** not full-install (cybersecurity ≠ Storm Bear vertical).

**Recommended pilot sequence**: ~10-min read-only inspection of 2-3 sample skill files + 5-framework mapping artifact + ATTACK_COVERAGE.md manifest. Extract:
- Progressive-disclosure-per-skill architecture pattern (for vault state-block refactor candidates at v2.4 codification)
- 5-framework cross-mapping discipline (for vault Pattern Library cross-axis variance scoping at v2.4 codification)
- Framework-coverage-manifest-at-top-level artifact convention

**Not a methodology-influence Tier-1-special** (no foundational-vendor status + not source-authoritative + does not redefine corpus methodology-direction).
