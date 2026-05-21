# (C) Entity 1 — Core product: 31-skill bundle + 72 design systems + 5 visual directions + 93 media prompts + Anti-AI-slop machinery + Junior-Designer workflow

**Entity scope**: What `open-design` IS, what it does, its layered methodology (Six load-bearing ideas + Five-dim critique + Anti-AI-slop machinery + Junior-Designer workflow from v82), and structural distinction from sibling design-skills v75 + v81 + v82.

## Identity statement

- **Repo**: [`nexu-io/open-design`](https://github.com/nexu-io/open-design)
- **Org**: nexu (GitHub `nexu-io`)
- **Tagline (primary)**: *"An open, agent-native alternative to Claude Design / Figma"*
- **Tagline (secondary)**: *"The open-source alternative to Claude Design. Local-first, web-deployable, BYOK at every layer"*
- **Tagline (positioning)**: *"Same loop, same artifact-first mental model, none of the lock-in"*
- **Repo description**: *"🎨 Local-first, open-source alternative to Anthropic's Claude Design"*
- **License**: Apache-2.0 root + bundled-MIT components retained in-tree
- **Custom domains**: `nexu.io` (org) + `open-design.ai` (product)
- **Stars / Forks / Watchers / Open issues / Age (Phase 0 snapshot 2026-05-21)**: 48,142 / 5,467 / 169 / 444 / 23 days
- **Velocity**: 2,093.1 stars/day NEW CORPUS-RECORD per-day-rate at pulse-class

## Product composition

### 31 skills (README claim) / ~280+ skills/ tree (actual)

- **27 prototype mode skills** + **4 deck mode skills** = 31 featured skills
- ~280+ skill subdirectories in `skills/` tree = sub-skills + variants + bundled-third-party-skills
- skills/AGENTS.md (2,717 bytes) = skill-router artifact analogous to v76 agent-skills-standard pattern

### 72 design systems

- 2 hand-authored starters
- 70 product design systems (Anthropic · Apple · Cursor · Supabase · Figma · etc.)

### 5 visual directions

1. **Editorial Monocle** — editorial-grade typography + restrained layout
2. **Modern Minimal** — clean/centered/whitespace-heavy
3. **Tech Utility** — functional + dense + utilitarian
4. **Brutalist** — asymmetric/modern (parallel to v81 brutalist-skill)
5. **Soft Warm** — friendly/approachable (parallel to v81 soft-skill)

### 93 media prompts

- 43 image prompts
- 39 video Seedance prompts
- 11 HyperFrames prompts

## Six load-bearing ideas (methodology stack — names mentioned, contents not Phase 0 enumerated)

README section title only; specific 6 ideas not extracted. Open question for Phase 4.

## Five-dim critique (verbatim 5-dimension enumeration)

1. **Philosophy** — design intent + brand-fit
2. **Hierarchy** — visual hierarchy + emphasis
3. **Detail** — micro-details (kerning + spacing + accuracy)
4. **Function** — does it work for the use case?
5. **Innovation** — beyond-the-template novelty

## Anti-AI-slop machinery (NAMED SECTION)

Enforcement primitives:
- **P0/P1/P2 gates** — agent must pass P0 before emitting
- **Explicitly forbidden in the prompt** — invented metrics + generic emoji icons (named); full forbidden-list unknown
- **Honest-placeholders > fake-stats discipline**
- **Anti-AI-slop checklist** at agent-runtime enforcement

## Junior-Designer workflow (borrowed from v82 huashu-design)

Explicit citation:
> *"Junior-Designer workflow borrowed from huashu-design"*

= Pattern #57 corpus-recursive at methodology layer.

## Senior-Designer + working-filesystem + deterministic-palette framing

> *"Senior designer with a working filesystem, deterministic palette library, and checklist culture."*

= Senior + Junior dual-mode positioning (Junior = show-early-iteration / Senior = deterministic-palette-with-checklist).

## "The prompt stack is the product" framing

> *"The prompt stack is the product"*

= emphasis on composable layers; product = the methodology stack (prompts + skills + design-systems + visual-directions + media-prompts).

## Architectural placement in T1 design-skill cluster

| Axis | v75 impeccable | v81 taste-skill | v82 huashu-design | v83 open-design |
|---|---|---|---|---|
| **Skill count (README claim)** | 1 monolithic | 12 sub-variants | 1 monolithic | **31 (27 prototype + 4 deck)** |
| **Skill count (tree actual)** | 1 | 12 | 1 | **~280+** |
| **Harnesses** | 14 (prior CORPUS-RECORD) | ~4 | 6 | **16 (NEW CORPUS-RECORD)** |
| **Output model** | Prompts-only | Prompts-only | Prompts + file-output pipelines | Prompts + file-output + Desktop app + Vercel-deploy + Docker |
| **Author identity** | Paul Bakaus (Google Creative Technologist) | Leon Lin (Munich solo founder) | 花叔 (China solo AI Native Coder) | **nexu org (3-mo-old indie org)** |
| **Skill spec size** | 9-file extensive governance | Per-skill SKILL.md × 12 | Single 60KB SKILL.md | **31 mode-specs + ~280+ sub-skill SKILL.md + AGENTS.md router + Six-load-bearing-ideas methodology** |
| **i18n** | EN-only | EN-only | EN + zh bilingual | **13 locales CORPUS-RECORD-TIE** |
| **License** | Apache 2.0 + NOTICE.md (2-source) | MIT | MIT (relicensed 2026-05-14) | **Apache-2.0 + bundled-MIT-components in-tree** |
| **Stars / age** | 28.8K / 185d | 18.2K / 90d | 14.5K / 32d | **48K / 23d** |
| **Velocity** | 155.8/d HIGH-NOT-EXTREME | 202.9/d HIGH-NOT-EXTREME | 452.4/d EXTREME-VIRAL pulse | **2,093.1/d NEW CORPUS-RECORD pulse** |
| **Anti-slop framing** | NO | YES (PRIMARY) | YES (named "Anti AI-slop Rules" + CSS) | **YES (named "Anti-AI-slop machinery" + P0/P1/P2 gates + forbidden-list + machinery-with-enforcement)** |
| **Lineage** | Anthropic frontend-design + ehmo typecraft (NOTICE.md 2-source) | Self-originated | Anthropic Claude Design reverse-engineering | **Anthropic Claude Design alternative-to + v82 workflow-cited + v81 sub-skill-bundled = 3-vector** |
| **Distribution methods** | 1 (`npx skills add`) | 1 (`npx skills add ... --skill`) | 1 (`npx skills add` shorthand) | **4 (source + Docker + Desktop + Vercel)** |
| **Economic model** | OSS no monetization | OSS + Sponsors | OSS + cross-platform-portfolio (book + App Store + sponsorships) | **OSS + BYOK-at-every-layer + zero direct monetization** |

**v83 = scale-up across all axes vs prior 3 design-skills**. The most ambitious project in T1 design-skill cluster.

## Anti-Slop-Design-Curation observation track sub-typology

**v83 implementation-granularity escalation evidence**:

| Sub-typology | Anchor | Evidence depth |
|---|---|---|
| **a — Framing-anchor** | v81 taste-skill | Anti-Slop tagline + product positioning |
| **b — Named-rules-with-enumeration** | v82 huashu-design | "Anti AI-slop Rules" named section + CSS-technique + cliché enumeration |
| **c — Machinery-with-enforcement** | v83 open-design | "Anti-AI-slop machinery" named section + P0/P1/P2 gates + forbidden-list + Honest-placeholders discipline + Five-dim critique enforcement |

**3-instance 3-consecutive-wiki arc** with escalating implementation-granularity = strong N=3 PROMOTION-LOCKED-IN evidence package.

## Pattern Library implications (Entity 1 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **Anti-Slop-Design-Curation observation track N=3 PROMOTION-LOCKED-IN with sub-typology a/b/c** | v81 framing + v82 named-rules + v83 machinery | **PROMOTION-LOCKED-IN at v85 audit** (matches Pattern #83 83f 3-instance 3-consecutive-wiki promotion-arc-speed CORPUS-RECORD) |
| **CORPUS-FIRST Multi-Tier Corpus-Recursive Citation Density at single subject** | 3-vector citation (bundled + cited + alternative-to) | Pattern #57 NEW sub-variant 57i PROVISIONAL N=1 |
| **NEW T1 sub-archetype candidate "OSS-Alternative-to-Vendor-Product with Multi-Distribution Stack"** | OSS + alternative-to-Anthropic-Claude-Design + 4-distribution + 31-skill + 72-system + 5-direction + 93-media | PROVISIONAL N=1 |
| **Pattern #82 STRONGEST quantitative-marketing density** | 31 skills + 72 systems + 5 directions + 16 CLIs + 93 media + 48K stars + 23-day age + BYOK + 13 locales + open-source-alternative-to-Claude-Design = 10+ claims | Within-pattern STRONG |
| **Pattern #78 STRONGEST single-subject LDS density** | 31-skill + 72-system + 5-direction + 93-media + AGENTS.md + Six-load-bearing-ideas + Five-dim critique + P0/P1/P2 gates | STRONG (challenges v76 259-skill at multi-axis layer) |
| **Library-vocabulary candidate "Visual Directions Taxonomy"** | 5-direction taxonomy (Editorial Monocle + Modern Minimal + Tech Utility + Brutalist + Soft Warm) | N=2 strengthening with v81 Axis A aesthetic-variants at design-direction-taxonomy layer |

## Open questions specific to Entity 1

- Six load-bearing ideas full content
- P0/P1/P2 gate criteria specifics
- Anti-AI-slop forbidden-list completeness
- Per-skill SKILL.md content for the 31 featured skills
- AGENTS.md skill-router logic
- 5 visual direction per-direction mechanics
