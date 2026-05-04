# (C) README + VN summary — BMAD-METHOD

> **Sources:** `README.md` (6 KB), `README_VN.md` (7.5 KB) — WebFetch 2026-04-19
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Positioning + dual acronym

README presents **BMAD-METHOD** with two expansions:

- **"Breakthrough Method for Agile AI-Driven Development"** — GitHub description / official tagline
- **"Build More Architect Dreams"** — README playful alternate (subtitle)

The dual acronym is **intentional marketing ambiguity** — "Breakthrough" for serious positioning, "Build More Architect Dreams" for community-facing personality. Unusual in T1 corpus (ECC/Superpowers/gstack/GSD all use single crisp positioning).

**Tagline concept:** "Traditional AI tools do the thinking for you, producing average results. BMad agents and facilitated workflows act as expert collaborators who guide you through a structured process to bring out your best thinking in partnership with the AI."

⚠️ **Verification note:** Phase 0 log quoted "Human Amplification, Not Replacement" as explicit tagline. On re-fetch, this exact phrase is **not confirmed** in current README — the philosophy is present (expert collaboration, human-centered), but the slogan may be from older version or community material. Logged to open questions.

## 2. 12+ specialized agents (numbers, not names)

README mentions **"12+ domain experts (PM, Architect, Developer, UX, and others)"** but does **not publish the full roster in README itself**. Named agents come from CHANGELOG:

- **Amelia** — Developer agent (consolidated v6.3, absorbed Barry/Quinn/Bob)
- **PM** — Product Manager
- **Architect** — Architecture design
- **UX** — UX expert
- **(Others not named in README — likely in `bmad/bmm/agents/` module directory)**

**v6.3 consolidation signal:** Trend is **fewer agents with broader scope** (Barry/Quinn/Bob → Amelia), not more. N=12+ may be stable or shrinking slightly.

## 3. 34+ workflows — largest library in T1

Workflows live in **BMM (BMad Method)** core module. README claims **34+ workflows** — the largest workflow count observed in T1 corpus (ECC has skills not "workflows"; Superpowers ~10 patterns; gstack ~15 specialist roles; GSD 33 agents but not workflow-framed).

**Workflow ≠ agent ≠ skill** in BMAD taxonomy:
- **Agent** = personality/role (Amelia, PM, Architect)
- **Workflow** = multi-step procedure an agent executes
- **Skill** = v6 unit of distribution (everything installs as a skill)

## 4. 5 module ecosystem

| Module | Name | Purpose |
|--------|------|---------|
| **BMM** | BMad Method | Core framework, 34+ workflows |
| **BMB** | BMad Builder | Create custom BMad agents and workflows |
| **TEA** | Test Architect | Risk-based test strategy and automation |
| **BMGD** | Game Dev Studio | Game development workflows (Unity, Unreal, Godot) |
| **CIS** | Creative Intelligence Suite | Innovation, brainstorming, design thinking |

⚠️ **Correction to Phase 0 log:** Abbreviation is **BMGD** (not "GMAD"). Phase 0 notes carried wrong letters — corrected here.

**Architecture insight:** BMM is core. BMB = meta (build more BMAD). TEA/BMGD/CIS = domain-specific. This is **a framework that can build frameworks** — unique in T1.

## 5. Novel primitives

### Party Mode
> "Bring multiple agent personas into one session to collaborate and discuss"

Multi-agent dialogue in single session. Analogous concept: GSD's 33 agents are invoked serially; BMAD's Party Mode puts them in conversation with each other. Novel for T1.

### Scale-Domain-Adaptive Planning
> "Automatically adjusts planning depth based on project complexity"

README does not expose algorithm — treats as black box. Likely heuristic on project size / scope signals. Logged to open questions.

## 6. Platform support

- **Primary:** Claude Code (`.claude-plugin/` in repo root)
- **Secondary:** Cursor (confirmed in README), Augment (claimed in Phase 0 log — repo has `.augment/` directory, README re-fetch did not mention by name)
- **Added v6.3:** Junie (JetBrains AI) — from CHANGELOG

**Install command:** `npx bmad-method install` (matches GSD's `npx get-shit-done-cc` pattern — npm-first distribution).

## 7. Licensing + trademark

- **License:** MIT (README claims; GitHub metadata shows NOASSERTION — resolved: MIT is authoritative per LICENSE file)
- **Trademark:** "**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC"
- **Entity:** BMad Code, LLC — commercial LLC. Distinguishes from solo-maintainer T1 peers (Jesse Vincent/Superpowers, TÂCHES/GSD)

## 8. Vietnamese README (README_VN.md) — honest assessment

### Quality verdict: Professional machine-translation, minimal human polish

**Evidence:**
- Phrasing awkward in places: `"một mô-đun khung phát triển hướng AI"` is clunky; a native speaker would smooth this
- "Build More Architect Dreams" rendered literally without idiomatic VN adaptation
- Tone: formal/corporate — faithful but stiff. Lacks VN personality touches

**Technical term handling (mixed):**
- **Preserved in English:** Agent, AI, CI/CD, agile, Node.js, Python, Discord, Skills
- **Localized to VN:** `kỹ sư` (engineer), `động não ý tưởng` (brainstorm), `kiến trúc` (architecture), `quy trình` (process)
- **Inconsistency:** "Skills" untranslated while "process" localized

**Structure parity:** ✅ Identical to EN — Quick Start, Modules, Documentation, Community, License all present.

**VN-specific content:** ❌ None detected
- URLs point to `docs.bmad-method.org/vi-vn/` (language suffix only)
- No VN-regional examples, case studies, cultural references
- "Buy me a coffee" + Discord links identical to EN
- `bmad-help` usage shows conversational VN (`"Tôi vừa hoàn thành..."`) — suggests interactive VN use was considered

### ⚠️ Correction to Phase 0 log
Phase 0 claimed VN was **"professional-quality, full fidelity, VN-specific URL paths, contextual examples in VN"**. Deeper read shows:
- Quality = **machine-translated with light polish** (not professional-quality human)
- No contextual examples in VN (only language-suffixed URLs)

This is **honest downgrade**. For a Storm Bear VN operator, README_VN is **useful but not native-feeling** — better than nothing, but EN remains the reference.

### Storm Bear relevance (still significant)

Even at machine-translation quality:
- ✅ BMAD is **first T1 entrant with any VN translation at all** (ECC/SP/gstack/GSD = zero VN)
- ✅ Signals project's intent to serve VN users
- ✅ Lowers barrier to VN team members reading official docs
- ⚠️ Does NOT signal active VN community presence — may be translation dump, not community request

## 9. Source strategy note

README + README_VN are **the canonical positioning source** for BMAD. CHANGELOG fills in version history + agent names. CONTRIBUTING fills in dev workflow. Entity pages (Phase 3) should cite README for claims, CHANGELOG for evolution.

## 10. Cross-references to T1 siblings

| Claim | BMAD | ECC | Superpowers | gstack | GSD |
|-------|------|-----|-------------|--------|-----|
| Dual acronym | ✅ | ❌ | ❌ | ❌ | ❌ |
| Explicit workflow count | 34+ | — | ~10 | ~15 roles | 33 agents |
| Module ecosystem | 5 | Skills | Patterns | Roles | Commands |
| VN translation | ✅ (v6.3) | ❌ | ❌ | ❌ | ❌ |
| LLC commercial entity | ✅ | ❌ (solo) | ❌ (solo Jesse) | ✅ (YC) | ❌ (solo) |
| Install pattern | `npx` | git setup | plugin | `npm` | `npx` |

→ BMAD = **largest + most formalized + most VN-accessible** T1 entrant. Also **most ambiguous on tagline** (dual acronym).

## Open questions surfaced

- Where does "Human Amplification, Not Replacement" slogan come from? Retired? → Q16
- Full 12+ agent roster not in README — where is it? (likely `bmad/bmm/agents/` in installed module) → Q17
- Who translated VN + Czech? Machine + review? Contractor? Community? → Q3 (existing)
- Scale-Domain-Adaptive algorithm = heuristic or model-based? → Q9 (existing)
