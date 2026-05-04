# (C) README + DESIGN.md Concept + Google Stitch Cluster Summary

> **Cluster:** DESIGN.md methodology + 9-section spec + Google Stitch lineage
> **Parent:** [[(C) index]]
> **Sources:** README + Google Stitch documentation
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **DESIGN.md concept** (methodology-lineage from Google Stitch)
2. **9-section spec** (color/typography/components/layout/depth/patterns/responsive/agent-prompts)
3. **69 templates × 3 files** (DESIGN.md + preview.html + preview-dark.html per site)

## 2. DESIGN.md concept

### Origin — Google Stitch

> *"DESIGN.md is a new concept...by Google Stitch"*

**Google Stitch** is Google's design-to-code AI tool. The DESIGN.md spec was pioneered there as a plain-text format for AI agents to consume design system information.

### Purpose

- **Human-readable** (markdown)
- **LLM-optimized** (plain text, structured sections)
- **Drop-in** — copy to project root
- **Agent-prompt-ready** — includes explicit agent instructions section

### Workflow

> *"Copy a DESIGN.md into your project, tell your AI agent 'build me a page that looks like this' and get pixel-perfect UI that actually matches."*

3 steps:
1. Copy site's DESIGN.md to project root
2. Tell AI agent to use it
3. Reference preview.html catalogs

## 3. 9-section DESIGN.md specification

### Section structure

| Section | Content |
|---------|---------|
| **Color** | Color palette + tokens |
| **Typography** | Font families + scale + weights |
| **Components** | Button / input / card / modal patterns |
| **Layout** | Grid / spacing / breakpoints |
| **Depth** | Shadow / elevation / layering |
| **Patterns** | Repeated UI patterns |
| **Responsive** | Breakpoint behavior |
| **Agent prompts** | Explicit instructions for AI |

### Why this structure

- Captures brand identity (color + typography)
- Captures structural rules (layout + responsive)
- Captures aesthetic character (depth + patterns)
- **Provides agent-specific guidance** — sets expectations for AI interpretation

## 4. 69 templates × 10 categories

### Category breakdown

| Category | Examples |
|----------|----------|
| AI/LLM platforms | Claude, Cohere, ElevenLabs, Mistral |
| Developer tools | Cursor, Vercel, Raycast, Warp |
| Database/DevOps | MongoDB, Supabase, PostHog |
| Fintech/Crypto | Stripe, Coinbase, Wise |
| E-commerce | Airbnb, Nike, Shopify |
| Automotive | Tesla, Ferrari, BMW |

### Per-site artifacts (3 files)

Each design system includes:
1. **DESIGN.md** — the spec (markdown)
2. **preview.html** — light-mode preview
3. **preview-dark.html** — dark-mode preview

**69 × 3 = 207 artifacts total.**

## 5. Compatible AI tools

| Tool | Compatibility |
|------|---------------|
| **Claude Code** | Explicit |
| **Cursor** | Explicit |
| **Google Stitch** | Native (methodology origin) |
| **Lovable** | Explicit |

Markdown-native format → broad LLM compatibility (any coding agent that reads markdown).

## 6. Pattern #19 archetype 2 — methodology-lineage data point

### Methodology-lineage archetypes post-v25

| Methodology | Source | Frameworks |
|-------------|--------|------------|
| SDD (Spec-Driven Development) | John Lam / shared community | GSD v5 + spec-kit v17 |
| BMM (Build More Architect Dreams) | BMad Code LLC | BMAD v11 |
| TDD (Test-Driven Development) | External | Superpowers v2 |
| Feature framework | External | ECC v1 |
| **DESIGN.md spec** | **Google Stitch** | **awesome-design-md v25** |

Methodology-lineage archetype grows. New category: **design-system methodology**.

### Significance

Before v25, methodology-lineage in corpus = coding/agent methodologies. awesome-design-md extends to **design-system methodology**. Broadens archetype 2.

## 7. Contrast with build-your-own-x education-aggregator

### Target audience difference

| Aggregator | Target | Format | License |
|------------|--------|--------|---------|
| build-your-own-x v8 | **Humans** learning | Tutorial links | CC0 |
| **awesome-design-md v25** | **AI agents** consuming | Drop-in DESIGN.md files | MIT |

### Structural difference

**build-your-own-x:** Points to external tutorials; humans read + learn + build.
**awesome-design-md:** Provides self-contained specs; AI agents read + generate UI.

**Both are awesome-list-style content aggregators, different audiences.**

### Sub-type claim

- Education-aggregator (v8) = human-directed
- **Design-template-aggregator (v25) = AI-agent-directed**

Distinct outside-scope sub-types. Or: generalize to "awesome-list-genre" with audience sub-classification.

## 8. Corpus position — methodology-vs-generation

### Generation-enablement aggregator

awesome-design-md's purpose = **enable AI agents to generate UI**. Not training. Not orchestration. Not browser automation. **Agent-input content library.**

Novel corpus role:
- T1-T5 = agent runtime + application
- Outside-scope training-infra = training models
- Outside-scope foundation-model = models themselves
- Outside-scope prompt-leak = extract-and-archive
- **Outside-scope design-template = provide inputs for agent consumption**

### Ecosystem position

- Skyvern v24 = agent does browser task
- awesome-design-md v25 = agent consumes design template → generates UI
- **Complementary:** awesome-design-md could feed Claude Code/Cursor/Lovable → any agent generating UI

## 9. Key observations

### Cluster-level

- **Google Stitch DESIGN.md spec** = methodology source (not VoltAgent invention)
- **9-section standard** = structured for LLM consumption
- **69 templates × 3 files** = comprehensive catalog
- **MIT license** = maximum adoption, minimum friction

### Cross-corpus

- **Pattern #19 archetype 2** grows with design-system methodology
- **Content-aggregator sub-type diversification** (human vs AI-agent consumption)
- **Pattern #32 research-paper-chain doesn't apply** — this is methodology-adoption, not research-network
- **Novel role: "input content library for AI agents"** — new outside-scope function

## 10. References

- Parent: [[(C) index]]
- Source: README + getdesign.md companion platform
- Google Stitch (external — Google's design-to-code tool)
- Sibling clusters: [[(C) VoltAgent ecosystem + getdesign.md commercial-funnel cluster summary]] + [[(C) Viral-velocity + vibe-design philosophy cluster summary]]
- Aggregator peer: build-your-own-x v8
- Methodology-lineage peer: spec-kit v17

---

**Cluster summary: Google Stitch DESIGN.md spec (methodology-lineage source) + 9-section standard + 69 templates × 3-file bundle (DESIGN.md + preview.html + preview-dark.html) across 10 categories. Compatible with Claude Code + Cursor + Stitch + Lovable. Pattern #19 archetype 2 data point (design-system methodology). Distinct sub-type from build-your-own-x (AI-agent-directed vs human-directed).**
