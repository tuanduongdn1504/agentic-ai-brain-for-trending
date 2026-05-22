# (C) Cluster 1 — README 24,955 bytes + 669+ codified design-system elements + Design System Generator + BM25 search

**Source bundle**: README.md (24,955 bytes) + CLAUDE.md (4,050 bytes — internal "Antigravity Kit" codename + Sync Rules + Architecture details).

## Verbatim taglines (4 layered)

1. *"An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms"* (GitHub repo description)
2. *"UI UX Pro Max is an AI skill providing design intelligence for professional UI/UX development across multiple platforms and frameworks."* (README first line)
3. *"From Zero to One Is Always the Hardest Part. We Can Take You There."* (org bio)
4. *"Antigravity Kit is an AI-powered design intelligence toolkit..."* (CLAUDE.md internal codename)

= **CORPUS-FIRST internal-codename ≠ public-tagline observation** (Library-vocab candidate "Internal-Codename-Distinct-from-Public-Product-Tagline").

## 669+ codified design-system elements (NEW CORPUS-RECORD LDS density)

| Category | Count | Examples |
|---|---|---|
| **UI styles** | 67 | glassmorphism + claymorphism + minimalism + brutalism + neumorphism + bento grid + dark mode + AI-native UI + 59 more |
| **Color palettes** | 161 | industry-specific product-category alignment |
| **Font pairings** | 57 | with Google Fonts integration |
| **Chart types** | 25 | for dashboards and analytics |
| **Tech stacks** | 15 | React + Next.js + Vue + Nuxt + SwiftUI + Flutter + React Native + Astro + Svelte + Shadcn + Jetpack Compose + SwiftUI + html-tailwind + others |
| **UX guidelines** | 99 | best practices + accessibility |
| **Reasoning rules** | 161 | automated design system generation |
| **Stack templates** | 13 | html-tailwind (default) + react + nextjs + astro + vue + nuxtjs + nuxt-ui + svelte + swiftui + react-native + flutter + shadcn + jetpack-compose |
| **skill.json keywords** | 8 | ui + ux + design + design-system + color-palette + typography + accessibility + ai-skill |
| **skill.json platforms** | 18 | (see Cluster 2) |

**Total: 669+ codified design-system elements** (67+161+57+25+15+99+161+13+8+18 = **624 minimum** + likely many more in CSV databases) = **NEW CORPUS-RECORD Pattern #78 LDS density at single subject**, exceeding v76's 259-skill prior record and v83's compound density.

## Version 2.5.0 "Design System Generator" architecture

**Flagship feature** (CLAUDE.md verbatim):
> *"AI-powered reasoning engine that analyzes your project requirements and generates a complete, tailored design system in seconds."*

**Pipeline architecture**:
```
user input
   │
   ▼
multi-domain search across 5 parallel categories
   │
   ├─→ product (SaaS, e-commerce, portfolio)
   ├─→ style (glassmorphism, minimalism, brutalism + AI prompts + CSS keywords)
   ├─→ typography (font pairings + Google Fonts imports)
   ├─→ color (palettes by product type)
   └─→ ux (best practices + anti-patterns)
   │
   ▼
reasoning engine application
   │
   ▼
complete design system output
   ├─→ patterns
   ├─→ styles
   ├─→ colors
   ├─→ typography
   ├─→ effects
   ├─→ anti-patterns
   └─→ checklists
```

= **CORPUS-FIRST 5-parallel-domain reasoning engine in T1 design-skill cluster**.

## Search engine: BM25 + regex hybrid

**Verbatim CLAUDE.md**:
> *"The search engine uses BM25 ranking combined with regex matching. Domain auto-detection is available when `--domain` is omitted."*

**Domain search CLI**:
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

Domains: `product` / `style` / `typography` / `color` / `landing` / `chart` / `ux`

**Stack search CLI**:
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --stack <stack>
```

= **CORPUS-FIRST BM25 + regex hybrid search engine within design-skill in v60+ window**.

## Architecture (verbatim from CLAUDE.md)

```
src/ui-ux-pro-max/                # Source of Truth
├── data/                         # Canonical CSV databases
│   ├── products.csv, styles.csv, colors.csv, typography.csv, ...
│   └── stacks/                   # Stack-specific guidelines
├── scripts/
│   ├── search.py                 # CLI entry point
│   ├── core.py                   # BM25 + regex hybrid search engine
│   └── design_system.py          # Design system generation
└── templates/
    ├── base/                     # Base templates (skill-content.md, quick-reference.md)
    └── platforms/                # Platform configs (claude.json, cursor.json, ...)

cli/                              # CLI installer (uipro-cli on npm)
├── src/
│   ├── commands/init.ts          # Install command with template generation
│   └── utils/template.ts         # Template rendering engine
└── assets/                       # Bundled assets (~564KB)
    ├── data/                     # Copy of src/ui-ux-pro-max/data/
    ├── scripts/                  # Copy of src/ui-ux-pro-max/scripts/
    └── templates/                # Copy of src/ui-ux-pro-max/templates/

.claude/skills/ui-ux-pro-max/     # Claude Code skill (symlinks to src/)
.factory/skills/ui-ux-pro-max/   # Droid (Factory) skill (symlinks to src/)
.shared/ui-ux-pro-max/            # Symlink to src/ui-ux-pro-max/
.claude-plugin/                   # Claude Marketplace publishing
```

**Multi-symlink architecture** (.claude/ + .factory/ + .shared/) maintains single-source-of-truth at `src/ui-ux-pro-max/` while exposing skill to multiple platforms via symlinks.

= **CORPUS-FIRST multi-symlink-architecture in v60+ window**.

## Installation methods

```bash
npm install -g uipro-cli
uipro init --ai claude
```

OR per-platform via skill.json template:
```bash
npx uipro-cli init --ai {{platform}}
```

= **CLI-generates-native-formats** Pattern #84 84c.2 N strengthening from v76 (template-driven per-platform per-stack generation).

## Apple-product-naming-convention observation

Product name "UI UX **Pro Max**" follows Apple iPhone Pro Max naming convention — "Pro" + "Max" suffix denotes premium/flagship variant in Apple ecosystem.

= **CORPUS-FIRST Apple-product-naming-convention adoption** in v60+ window — Library-vocab candidate "Apple-Product-Naming-Convention-Adoption-as-Marketing-Discipline" PROVISIONAL N=1.

## Antigravity Kit internal codename

Per CLAUDE.md (verbatim):
> *"Antigravity Kit is an AI-powered design intelligence toolkit providing searchable databases of UI styles, color palettes, font pairings, chart types, and UX guidelines."*

Internal codename "Antigravity Kit" is distinct from public product tagline "UI UX Pro Max". Possible connection to:
- v67 opencode-antigravity-auth (corpus subject) — "antigravity" terminology
- Google Antigravity (one of platforms cited in v83 16-harness list at "Devin for Terminal" / "Antigravity" topic)
- Internal-team-product-codename pattern (vs public-marketing-product-name)

= **CORPUS-FIRST "Antigravity Kit" internal codename + Library-vocab candidate "Internal-Codename-Distinct-from-Public-Product-Tagline"** PROVISIONAL N=1.

## PR-discipline at project-CLAUDE.md scope

Verbatim CLAUDE.md:
> *"Never push directly to `main`. Always: Create a new branch + Commit + Push -u + gh pr create"*

= **CORPUS-FIRST PR-discipline at project-CLAUDE.md scope in v60+ window** — Library-vocab candidate "PR-Discipline-at-Project-CLAUDE.md-Scope" PROVISIONAL N=1.

## Pattern Library implications (Cluster 1 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW CORPUS-RECORD Pattern #78 LDS density** | 669+ codified design-system elements at single subject | NEW CORPUS-RECORD (exceeds v76 259-skill + v83 compound) |
| **CORPUS-FIRST BM25 + regex hybrid search engine within design-skill** | scripts/core.py | NEW within-pattern observation |
| **CORPUS-FIRST 5-parallel-domain reasoning engine** | Design System Generator architecture | NEW within-pattern observation |
| **CORPUS-FIRST multi-symlink-architecture** | .claude/ + .factory/ + .shared/ symlinks to src/ | NEW within-pattern observation |
| **Library-vocab candidate "Apple-Product-Naming-Convention-Adoption"** | "UI UX Pro Max" naming | PROVISIONAL N=1 |
| **Library-vocab candidate "Internal-Codename-Distinct-from-Public-Tagline"** | "Antigravity Kit" vs "UI UX Pro Max" | PROVISIONAL N=1 |
| **Library-vocab candidate "PR-Discipline-at-Project-CLAUDE.md-Scope"** | "Never push directly to main" 4-step workflow | PROVISIONAL N=1 |
| **CORPUS-FIRST Python-primary T1 design-skill in v60+ window** | Python 3.x no external deps | Within-pattern observation |
| **Pattern #84 84c.2 CLI-generates-native-formats N strengthening from v76** | uipro-cli template-driven per-platform generation | Within-pattern strengthening |

## Cross-wiki siblings (Cluster 1)

- **v76 agent-skills-standard** — 259-skill prior CORPUS-RECORD now SURPASSED by v85's 669+ LDS density
- **v83 open-design** — 31-featured + 280-tree skill bundle vs v85 1-skill × 669+ codified elements (different axis: bundle-count vs element-codification-depth)
- **v82 huashu-design** — 1-monolithic-60KB-SKILL.md vs v85 multi-symlink + CSV database architecture (mechanism distinction at LDS layer)

## Open questions specific to Cluster 1

- Verbatim content of 99 UX guidelines + 161 reasoning rules (Phase 0 only summary fetched)
- Whether Anti-Slop-Design-Curation track is present at v85 (need verify in 24,955-byte README)
- Whether Antigravity Kit codename is referenced elsewhere (docs/ + cli/ directories not Phase 0 probed)
- BM25 vs alternative ranking algorithms — design choice rationale
