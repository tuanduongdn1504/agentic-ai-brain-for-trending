# (C) DESIGN.md Spec + Google Stitch Methodology-Lineage

> **Type:** Entity — core methodology + intellectual lineage
> **Parent:** [[(C) index]]
> **Sources:** README + Google Stitch documentation + 9-section spec
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

DESIGN.md is a **plain-text spec for AI agents to generate UI matching a brand/design system**. Concept pioneered by **Google Stitch** (Google's design-to-code AI tool) — awesome-design-md aggregates 69 DESIGN.md files following the spec. 9-section standard: color / typography / components / layout / depth / patterns / responsive / agent prompts. Pattern #19 archetype 2 (methodology-lineage) data point — broadens archetype from coding methodologies to design-system methodology.

## 2. What DESIGN.md is

### Core concept

A **markdown file** capturing a design system sufficiently for AI agents to generate matching UI:
- Plain-text (LLM-native format)
- 9 structured sections
- Drop-in (`cp DESIGN.md ./`)
- Agent-prompt-ready

### Why markdown

- LLMs read markdown natively
- No parsing infrastructure needed
- Human-editable
- Version-control-friendly
- Shareable via Git / direct copy

### Position in toolchain

```
Design System → DESIGN.md → AI Agent (Claude Code/Cursor/Stitch) → Generated UI
```

Bridge layer between design documentation + AI code generation.

## 3. Google Stitch origin

### Citation (verbatim)

> *"DESIGN.md is a new concept...by Google Stitch"*

### What Google Stitch is

**Google Stitch** = Google's design-to-code AI tool (2024-2025). Enables designers to sketch UI + get code output. DESIGN.md format pioneered there as the input/output spec for design system information.

### VoltAgent's contribution

VoltAgent did NOT invent DESIGN.md. VoltAgent's contribution:
- **Aggregated 69 examples** across 10 categories
- **Packaged per-site 3-file bundle** (DESIGN.md + preview.html + preview-dark.html)
- **Made MIT-licensed + community-contributable**
- **Built getdesign.md companion platform**

Role: **curator / amplifier of Google Stitch methodology**, not methodology inventor.

## 4. 9-section DESIGN.md spec

### Section structure

| Section | Purpose |
|---------|---------|
| **Color** | Palette + tokens (e.g., `--primary: #FF6B35`) |
| **Typography** | Font families + scale + weights |
| **Components** | Button / input / card / modal patterns |
| **Layout** | Grid / spacing / breakpoints |
| **Depth** | Shadow / elevation / layering |
| **Patterns** | Repeated UI patterns (e.g., hero / testimonial / pricing) |
| **Responsive** | Breakpoint behavior |
| **Agent prompts** | Explicit instructions for AI |

### Why this 9-section design

1. **Color + Typography = brand identity** — captures core visual DNA
2. **Components + Patterns = repeated structures** — captures reusable UI parts
3. **Layout + Responsive = structural rules** — captures spatial organization
4. **Depth = visual language** — captures elevation / shadow / layering feel
5. **Agent prompts = interpretation guide** — captures aesthetic intent beyond specs

### Balance: spec + vibe

First 7 sections = **specs** (deterministic).
Last section (Agent prompts) = **vibe** (interpretive).

This hybrid enables AI agents to:
- Hit deterministic aspects (colors, sizes)
- Interpret aesthetic aspects (cinematic feel, warm terracotta character)

## 5. Pattern #19 archetype 2 — methodology-lineage data point

### Methodology-lineage corpus post-v25

| Methodology | Source | Frameworks |
|-------------|--------|------------|
| SDD (Spec-Driven Development) | John Lam / community | GSD v5 + spec-kit v17 |
| BMM (Build More Architect Dreams) | BMad Code LLC | BMAD v11 |
| TDD (Test-Driven Development) | External | Superpowers v2 |
| Feature framework | External | ECC v1 |
| **DESIGN.md spec** | **Google Stitch** | **awesome-design-md v25** |

### Archetype broadening

Before v25: methodology-lineage archetype = **coding/agent methodologies**.
v25 extends: **design-system methodology** also methodology-lineage archetype.

**Archetype 2 broader than initially observed.**

## 6. Compatible AI tools

### Explicit compatibility

| Tool | Source |
|------|--------|
| **Claude Code** | README |
| **Cursor** | README |
| **Google Stitch** | Methodology origin — native |
| **Lovable** | README |

### Implicit compatibility

Any LLM that reads markdown:
- Codex / GitHub Copilot
- Windsurf
- Kiro
- Trae / Trae CN
- Any OpenAI/Anthropic-compatible agent

**Markdown-native = broadest possible compatibility.**

## 7. Per-site 3-file bundle structure

### Files per design system

```
awesome-design-md/
├── stripe/
│   ├── DESIGN.md           # The spec
│   ├── preview.html        # Light mode
│   └── preview-dark.html   # Dark mode
├── airbnb/
│   ├── DESIGN.md
│   ├── preview.html
│   └── preview-dark.html
├── ... (69 total)
```

### Why 3 files

1. **DESIGN.md** — agent-consumable spec
2. **preview.html** — verify what spec produces (light)
3. **preview-dark.html** — verify dark-mode variant

Preview HTML = reference implementation. Demonstrates what correct DESIGN.md interpretation looks like.

## 8. 10 categories breakdown

| # | Category | Examples |
|---|----------|----------|
| 1 | AI/LLM platforms | Claude, Cohere, ElevenLabs, Mistral |
| 2 | Developer tools | Cursor, Vercel, Raycast, Warp |
| 3 | Database/DevOps | MongoDB, Supabase, PostHog |
| 4 | Fintech/Crypto | Stripe, Coinbase, Wise |
| 5 | E-commerce | Airbnb, Nike, Shopify |
| 6 | Automotive | Tesla, Ferrari, BMW |
| 7 | (Others — full catalog at getdesign.md) | — |

**Broad coverage** — spans tech + commerce + luxury.

## 9. Contribution model

### How people add new DESIGN.md

1. **Open issue first** — discuss idea with maintainers
2. **PR after approval** — add DESIGN.md + preview.html + preview-dark.html
3. **Improvements welcome** — fix colors, tokens, descriptions

### Curation vs submission

VoltAgent maintains **curation bar** — not all submissions accepted. Issue-first-then-PR model suggests quality gating.

## 10. Usage workflow

### Step-by-step

```bash
# 1. Copy DESIGN.md to project root
cp awesome-design-md/stripe/DESIGN.md ./

# 2. Tell AI agent to use it
# In Claude Code / Cursor:
"Use the DESIGN.md in this project. Build me a landing page for a SaaS product."

# 3. Reference preview.html for visual verification
open awesome-design-md/stripe/preview.html
```

### Integration with workflow

- **Prototyping:** fast landing-page iteration
- **Greenfield projects:** consistent design DNA from day 1
- **Learning:** reverse-engineer how brand design translates to markdown

## 11. Novel role in corpus — "input content library"

### T1-T5 tiers consume inputs from outside-scope

| Outside-scope sub-type | Corpus role |
|-------------------------|-------------|
| Education-aggregator (v8) | Human learning content |
| Foundation-model (v20) | Models consumed by agents |
| Prompt-leak-archive (v21) | Extracted prompts for study/reuse |
| Training-infra (v22, v23) | Tools to fine-tune models |
| **Design-template-aggregator (v25)** | **Spec inputs for agent UI generation** |

awesome-design-md = **new category of content** that agents consume. Distinct from models they use, prompts they're built with, or tools that train them.

## 12. Edges + limitations

### Design-system coverage

- **Western-biased** — major Silicon Valley + US brands dominate (Stripe, Airbnb, Shopify)
- **No enterprise B2B dark-launch brands** (IBM, Salesforce patterns may not fit)
- **Vibe > precision** — 100% pixel-exact impossible; agent interpretation varies

### 9-section spec limitations

- **No motion/animation section** — missing animation patterns
- **No accessibility section** — a11y not explicit
- **No internationalization** — RTL / non-Latin scripts not addressed

### Tool-compatibility bias

Optimized for **Chrome-based UI** + modern web (CSS Grid / Flexbox). Legacy browser support not addressed.

## 13. Related concepts

- [[(C) VoltAgent Ecosystem-Layer + Pattern 17 Promotion Consideration]] — organizational
- [[(C) Extreme Viral Velocity + Pattern 27 Data Point]] — scale
- [[(C) 5th Outside-Scope Sub-Type + Vibe-Design + Storm Bear]] — meta
- Pattern #19 archetype 2 (methodology-lineage) — new data point
- spec-kit v17 (John Lam SDD methodology-lineage) — peer
- Parent: [[(C) index]]

## References

- README DESIGN.md section
- Google Stitch (external — Google design-to-code tool)
- getdesign.md companion platform
- Compatible tools: Claude Code, Cursor, Stitch, Lovable

---

**DESIGN.md = plain-text markdown spec for AI agents to generate UI matching a design system. Pioneered by Google Stitch, aggregated by VoltAgent. 9-section standard (color/typography/components/layout/depth/patterns/responsive/agent-prompts). 69 templates × 3-file bundle. Pattern #19 archetype 2 methodology-lineage data point — extends archetype to design-system methodologies. Novel corpus role: input content library for AI agents.**
