# (C) README + CONTRIBUTING + zh-CN cluster summary — agency-agents

> **Sources:** README.md + CONTRIBUTING.md + CONTRIBUTING_zh-CN.md (main branch)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

3 user-facing / contributor-facing documents at repo root. README = positioning + features. CONTRIBUTING + zh-CN = community governance (with unique Chinese-primary contribution guide — first in corpus).

## 2. Core positioning (verbatim)

### Main tagline

> "A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers."

### Expanded positioning

> "Assembling your dream team, except they're AI specialists who never sleep, never complain, and always deliver."

### Origin story (verbatim)

> "born from a Reddit thread and months of iteration"

With the metric:
> "50+ requests in the first 12 hours"

### Anti-generic stance

> "Not generic prompt templates — Battle-tested workflows and success metrics."

## 3. "Agency" metaphor — novel framing

### Corpus comparison

| Framework | Metaphor |
|-----------|----------|
| ECC v1 | "everything" / feature collection |
| Superpowers v2 | "superpowers" (abilities) |
| gstack v3 | "virtual engineering team" |
| GSD v5 | "get shit done" |
| BMAD v11 | "Breakthrough Method for Agile AI-Driven Development" |
| codymaster v12 | "Vibe Coding Framework" |
| spec-kit v17 | "Spec-Driven Development toolkit" |
| **agency-agents v18** | **"AI agency"** |

**Agency metaphor first in corpus.** Implies:
- **Coordinated collective** (not random agents)
- **Specialized professionals** (not interchangeable prompts)
- **Distributed roles** (engineering / marketing / sales / design / etc.)
- **Autonomous practitioners** within virtual firm structure

**Pattern candidate #24 — Metaphor Inflation at T1:** Each T1 framework adopts distinctive metaphor. As T1 saturates at N=8, differentiation via metaphor is marketing strategy.

## 4. 12 divisions with agent counts (verbatim)

| Division | Agents | Examples |
|----------|--------|----------|
| **Engineering** | 27 | Frontend, Backend, Mobile, DevOps, Security, Architecture |
| **Design** | 8 | UI Designer, UX Researcher, Brand Guardian, **Whimsy Injector** |
| **Paid Media** | 7 | Ad strategy, performance marketing |
| **Sales** | 9 | Outbound Strategist, Discovery Coach, Deal Strategist |
| **Marketing** | 26 | Content Creator, Twitter Engager, **Reddit Community Builder** |
| **Product** | 5 | PM, PO, product strategy |
| **Project Management** | 6 | Scrum coach, project ops |
| **Testing** | 8 | QA, test automation, Reality Checker |
| **Support** | 6 | Customer support, community |
| **Spatial Computing** | 6 | AR/VR (corpus-first division) |
| **Specialized** | 41 | Edge cases, domain-specific |
| **Finance** | 5 | Revenue, accounting, finance analysis |
| **Game Development** | 20+ | Game design, level design, narrative (corpus-first) |
| **Academic** | 5 | Research, writing, citation |

**Total: 144+ agents**

### Novel agent types

- **Whimsy Injector** (Design) — inject playfulness purposefully
- **Reality Checker** (Testing) — defaults to finding 3-5 issues
- **Reddit Community Builder** (Marketing) — authentic community engagement
- **Brand Guardian** (Design) — brand consistency
- **Deal Strategist** (Sales) — deal-closing tactics

### Division novelty

- **Game Development** — first corpus with 20+ game-dev agents
- **Spatial Computing** — first corpus with AR/VR focus
- **Paid Media** — first corpus with dedicated paid-media division
- **Specialized** (41) — largest division (catch-all for specialty edge cases)

## 5. Agent structure (verbatim from README)

### Each agent includes

- **Personality traits** — distinct character
- **Domain-specific workflows** — how agent approaches task
- **Code examples** — concrete implementation
- **Success metrics** — measurable outcomes

### Example invocation patterns

**Claude Code:**
```
"Use the Frontend Developer agent to review this component."
```

**Antigravity (Gemini):**
```
@agency-frontend-developer review this React component
```

**OpenCode:**
```
@backend-architect design this API.
```

**Cursor:**
```
Use the @security-engineer rules to review this code.
```

### Personality-driven philosophy (verbatim)

> "Every playful element must serve a functional or emotional purpose"

## 6. Installation workflow

### Quick install

```bash
./scripts/install.sh
```

Interactive mode — auto-detects installed AI coding tools, asks which to install agents for.

### Targeted install

```bash
./scripts/install.sh --tool claude-code
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
```

### Non-interactive

```bash
./scripts/install.sh --no-interactive --tool all
./scripts/install.sh --no-interactive --parallel --jobs 4
```

### Parallel execution

- Auto-detects CPU count: `nproc` (Linux), `sysctl -n hw.ncpu` (macOS), fallback 4 threads
- `--parallel` flag for convert.sh + install.sh

### Corpus context — shell-based install

Parallels **gstack v3** (shell-based). Contrast:
- npm: ECC, Superpowers, BMAD, codymaster (4)
- pip: graphify v16
- uv: spec-kit v17
- **shell: gstack v3 + agency-agents v18 (2)**

Shell-first install = lower dependency footprint.

## 7. 11 supported platforms

### Full list (verbatim)

1. **Claude Code** (native `.md` agents)
2. **GitHub Copilot**
3. **Antigravity** (Gemini research tool)
4. **Gemini CLI**
5. **OpenCode**
6. **OpenClaw**
7. **Cursor**
8. **Aider**
9. **Windsurf**
10. **Qwen Code**
11. **Kimi Code**

### Overlap analysis vs spec-kit (30+) vs graphify (15)

| Platform | spec-kit v17 | graphify v16 | agency-agents v18 |
|----------|--------------|--------------|-------------------|
| Claude Code | ✅ | ✅ | ✅ |
| Codex | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ✅ |
| Copilot | ✅ | ✅ | ✅ |
| Gemini CLI | ✅ | ✅ | ✅ |
| Aider | ❌ | ✅ | ✅ |
| OpenCode | ✅ | ✅ | ✅ |
| OpenClaw | **❌** | ✅ | ✅ |
| Hermes | ❌ | ✅ | ❌ |
| Kiro | ✅ | ✅ | ❌ |
| Qwen | ✅ | ❌ | ✅ |
| Windsurf | ❌ | ❌ | ✅ |
| Kimi Code | ❌ | ❌ | ✅ |
| Antigravity | ✅ | ❌ | ✅ |

**Key observations:**
- agency-agents includes Windsurf + Kimi Code (niche, not in other wikis)
- agency-agents has OpenClaw (community-platform style); spec-kit doesn't (corporate)
- agency-agents doesn't have Hermes (partial Pattern #18 — has OpenClaw but not Hermes)

## 8. Pattern #18 (OpenClaw) at v18 — 5th wiki mention

### Updated OpenClaw timeline

| Wiki | Evidence level | Context |
|------|----------------|---------|
| codymaster v12 | 📄 Doc | Listed as install platform |
| paperclip v14 | 🏗️ Architecture | First-class adapter |
| multica v15 | 📄 Doc | 1 of 8 supported agent models |
| graphify v16 | 🛠️ Execution | Dedicated `graphify openclaw install` |
| **agency-agents v18** | **🛠️ Execution** | **Install script supports OpenClaw** |

**Pattern #18 strengthened further:**
- **5 wikis** now mentioning OpenClaw
- **2 wikis with execution-level evidence** (graphify + agency-agents)
- **Community-platform-specific** (v17 refinement) validated — all 5 are solo/community, NOT corporate (spec-kit corporate has NO OpenClaw)

**Hermes timeline at v18:**
- paperclip v14 + multica v15 + graphify v16 (3 wikis)
- agency-agents v18 does NOT include Hermes
- Pattern #18 split: OpenClaw more universal than Hermes within community-platform wikis

## 9. CONTRIBUTING + CONTRIBUTING_zh-CN (corpus-first)

### Chinese contribution guide

CONTRIBUTING_zh-CN.md is **first corpus Chinese contribution guide**.

Prior Chinese presence in corpus:
- deer-flow v9: zh-CN README
- multica v15: zh-CN README
- graphify v16: zh-CN README + ja-JP + ko-KR (CJK-trio)
- **agency-agents v18: zh-CN CONTRIBUTING guide** (not README)

### Implications

- **Contributor-first localization** — unusual pattern
- Chinese developer community engagement priority
- **Pattern candidate:** Contribution-guide localization vs README localization (different strategies)

### CONTRIBUTING workflow (inferred)

- Fork + PR
- Agent template format
- Category/division placement rules
- Quality review for agent quality

## 10. Anti-patterns + philosophy

### Explicit stance

> "Not generic prompt templates"

### Authenticity principle (Reddit Community Builder)

> "You're becoming a valued community member who happens to represent a brand"

### Quality default (Reality Checker)

> "Defaults to finding 3–5 issues and requires visual proof for everything"

### Whimsy discipline

> "Every playful element must serve a functional or emotional purpose"

**Corpus comparison:**
- paperclip v14: alignment-theory philosophical framing
- spec-kit v17: anti-vibe-coding stance
- **agency-agents v18: authenticity + quality + purposeful-whimsy**

Each framework stakes distinct philosophical ground.

## 11. Scale signals

### 82.9K stars + solo maintainer = corpus first

| Framework | Stars | Author |
|-----------|-------|--------|
| ECC v1 | ~5K | Solo |
| Superpowers v2 | ~8K | Solo |
| graphify v16 | 30K | Solo (+ 7 contrib) |
| **agency-agents v18** | **82.9K** | **Solo** |
| spec-kit v17 | 89.2K | Corporate |

**agency-agents is 2.7× graphify's solo scale.** Nearly matches corporate spec-kit scale.

### 13.2K forks = high derivative work

High forks suggests:
- Active community customization
- Template reuse pattern
- Potentially fragmentation risk

### 43 open issues at 82.9K stars = low issue ratio

Possibilities:
- Issues resolved quickly
- Community forks instead of opens issues
- Solo maintainer triage efficient
- Low actual usage (star inflation?)

## 12. Cross-references

- [[(C) SECURITY + Governance + Installation Scripts cluster summary]] — governance
- [[(C) 12 Divisions + 144 Agents Taxonomy cluster summary]] — agent details
- [[(C) 144 Agent Personalities + 12 Divisions Taxonomy]] (entity)

## 13. Corpus-first observations

- **First solo-at-enterprise-scale** (82.9K solo)
- **First agency metaphor** at T1
- **First 144-agent library** (largest)
- **First Reddit-viral-origin** framework
- **First CONTRIBUTING_zh-CN.md** (CN contribution guide)
- **First Game Development division** (20+)
- **First Spatial Computing division**
- **First Paid Media division**
- **First personality-driven design** emphasis (Whimsy / Reality Checker / Reddit Community Builder)
- **5th wiki mentioning OpenClaw** — Pattern #18 strengthened
- **2nd shell-primary T1** (after gstack v3)
