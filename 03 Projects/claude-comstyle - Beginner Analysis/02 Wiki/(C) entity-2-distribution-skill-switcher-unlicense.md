# (C) Entity 2 — Distribution + style-switcher SKILL.md + 2-harness footprint + Unlicense governance

**Type**: Distribution + packaging + governance entity.

## Distribution model — 3-tier persistence

The README describes three install/persistence modes:

| Mode | Mechanism | Persistence | Cost-of-trial |
|---|---|---|---|
| Per-chat | Copy prompt → paste at start of Claude chat | Single conversation | ~10 seconds; zero install |
| Permanent globally | Add prompt to `~/.claude/CLAUDE.md` | Every Claude session on the machine | ~30 seconds; reversible via file edit |
| Per-workspace via skill | Copy `skills/style-switcher/SKILL.md` into `.claude/skills/style-switcher/` + restart Claude | Per-workspace | ~1 minute; reversible via `rm -rf` |

**CORPUS-FIRST tri-layer prompt-persistence at communication-style sub-product** in v60+ window. Prior corpus subjects offered installer scripts, npm packages, multi-platform manifests, or skill bundles — but did not articulate the 3-tier persistence-scope continuum (single-conversation → global-user → per-workspace) for prompts specifically.

**Lowest cost-of-trial in corpus**: even the heaviest install mode (per-workspace skill) is a 1-minute single-file copy. No `npx`, no `npm install`, no Docker, no CLI tool, no Vercel deploy, no Electron app. This positions v87 as **MINIMUM-FRICTION pilot candidate**.

## The style-switcher SKILL.md

Located at `skills/style-switcher/SKILL.md` in the repo. Per README, install to `.claude/skills/style-switcher/SKILL.md` in any workspace, restart Claude → the `/style` command becomes available.

### Command surface

```
/style          → shows full menu (all 13 styles + descriptions)
/style 1        → apply Military directly (numeric addressing)
/style feynman  → apply by name (case-insensitive name addressing)
/style 3 + terminal CLI  → apply Reality Check with plain-text modifier
```

**3-mode addressing scheme**:

1. **No-arg menu**: `/style` → shows the catalog
2. **Numeric**: `/style 1` through `/style 13` → direct index addressing
3. **Name**: `/style feynman` (case-insensitive) → name-based addressing
4. **Compositional**: `/style 3 + terminal CLI` → base + modifier composition

CORPUS-FIRST **multi-mode skill-command-addressing with compositional modifier** in v60+ window. Prior corpus skill commands were typically name-only or single-argument.

### Cross-harness claim

README states: *"Works with Claude Code and Cowork."*

- **Claude Code**: corpus subject v65 (Anthropic CLI; matches `.claude/skills/` directory convention)
- **Cowork**: not in corpus; Anthropic-internal product (skills protocol shared with Claude Code)

The Cowork mention is **2-harness coverage**, NOT multi-platform manifest distribution (no `skill.json` listing per-harness paths). The 2-harness coverage is sufficient for Anthropic-ecosystem users but excludes Cursor / Codex / Gemini / Kiro / Trae / Windsurf etc. covered by v85's 18-platform manifest.

## Pattern #84 84c.1 LIGHT-end placement

v87 contributes the **lowest-harness-count data-point in v60+ window** observed under Pattern #84 84c.1:

```
v85 ui-ux-pro-max-skill: 18 harnesses (skill.json formal manifest)  ← CORPUS-RECORD high
v83 open-design:        16 harnesses
v75 impeccable:         14 harnesses
v76 agent-skills-std:   10+ via CLI-generated (84c.2 variant)
v82 huashu-design:       6 harnesses
v81 taste-skill:         ~4 harnesses
v84 image-blaster:        1 harness (Claude Code only)
v87 claude-comstyle:      2 harnesses (Claude Code + Cowork)   ← LIGHT-end
```

**Full-distribution-observability**: Pattern #84 84c.1 sub-mechanism now spans **1 → 18 harnesses** within 14-wiki window v71→v87. The LIGHT-end is **positive-evidence** — author chose to support 2 harnesses (more than 1) by explicit README statement, but did not author per-harness install instructions. This represents a **deliberate-narrow-distribution profile** at the LIGHT-end (Library-vocab strengthening from v79 + v80 N=2).

## Governance — Unlicense

The repository ships [Unlicense](https://unlicense.org) (public-domain dedication). This is **CORPUS-FIRST Unlicense in v60+ window**:

| License | Prior corpus subjects (v60+) |
|---|---|
| MIT | v65, v66, v67, v68, v69, v70, v71, v72, v73, v75, v81, v82, v85 (multiple) |
| Apache 2.0 | v63, v74 (Apache-2.0 with book-content-exclusion sub-typology 45d), v76, v83 (Apache-2.0 + bundled-MIT) |
| BSD | (none in v60+ window per available records) |
| CC BY-NC-SA 4.0 | v77 easy-vibe (declared README; "None specified" GitHub API per Pattern #83 83f) |
| NOASSERTION (absent LICENSE file) | v79, v80 (v79 README-declared MIT + no LICENSE = Pattern #83 83f.4) |
| **Unlicense** | **v87 claude-comstyle (NEW)** |

### Pattern #29 vs Pattern #45 framing decision (DEFERRED to v90)

Unlicense is a **public-domain-dedication mechanism** — distinct from both:

- **Pattern #29 absent-LICENSE** (v80 / v79 / etc. — no license file at all OR README claims license but GitHub API returns NOASSERTION)
- **Pattern #45 sub-typology** (existing 45a/b/c/d cover tier-based / wrapper-based / artifact-scope-split / Apache-with-book-exclusion)

Unlicense ≠ absent — there IS a LICENSE file. Unlicense ≠ existing 45a-d — it's not tier/wrapper/scope-split/exclusion. **Two framing options for v90 audit**:

1. **Pattern #45 NEW sub-typology 45e "Public-Domain-Dedication via Unlicense"** PROVISIONAL N=1
2. **Pattern #29 sister observation** "explicit-public-domain-dedication-as-alternative-to-MIT-Apache" — distinct mechanism from absent-LICENSE but adjacent

**Disposition recommendation**: framing-decision deferred to v90 audit; record as Pattern #45 sub-typology candidate AND Pattern #29 sister candidate, let v90 decide which framing is load-bearing.

### Governance pack at micro-scale

`claude-comstyle` ships a fuller-than-expected governance pack for a 28-star repo:

- `LICENSE` (Unlicense)
- `README.md` + `README_VN.md`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`

5-document governance at 28-star micro-scale is **higher governance-document-density per star** than most prior corpus subjects. v76 agent-skills-standard (496 stars) had similar 3-document; v85 (81K stars) had extensive governance. v87's per-star governance-density signals **professional-discipline-at-micro-scale** = Library-vocab candidate at OC layer.

## What this entity does NOT include

- **No `skill.json` formal manifest** — only single `SKILL.md` for style-switcher; v87 contrasts with v85's 18-platform `skill.json` CORPUS-RECORD
- **No package metadata** — no `package.json`, `pyproject.toml`, `Cargo.toml`; pure markdown collection
- **No release tags** — no semver versions, no changelog
- **No CI/CD** — no `.github/workflows/`
- **No automated testing** — no eval scripts for the styles
- **No `.shared/` or symlink architecture** — single source-of-truth structure absent (vs v85 multi-symlink CORPUS-FIRST)
- **No telemetry / metrics collection** — % token-impact claims unverifiable client-side
- **No localization for prompts themselves** — only example tables show VN; the 13 prompts are English-only

These absences are **honestly aligned** with the project's positioning as a personal-curated-collection rather than productized infrastructure. The Pattern #83 within-pattern honest-disclosure operates at per-style granularity (Pros/Cons sections); project-level gap-disclosure of measurement-methodology is implicit rather than explicit.

## Pattern #19 sub-mechanism candidate detail

**"VN-Solo-Dev-with-Chrome-Extension-Sister-Product"** PROVISIONAL N=1:

bsquang has a 2-product mini-portfolio:

- **claude-comstyle** — 28★ prompt collection (this subject)
- **naotab** — 40★ JavaScript Chrome extension: *"A Chrome extension that turns your browser tabs into a personal knowledge base — save tabs with context, auto-tag with AI, and visualize connections as a network graph."*

Both products are:
- AI-adjacent personal-tooling
- Small-but-shipped (40★ and 28★)
- Maintained by solo author
- Cross-product theme: augmenting individual-developer knowledge work via AI

**Distinct from existing Pattern #19 sub-mechanisms** 19a-19m (solo with depth-focus, multi-book portfolio, etc.) and 19n (VN-located AI-skills indie organization). v87 contributes a **VN-solo-with-2-product-Chrome-extension-portfolio** archetype.

**RISK**: this candidate joins Pattern #19's **9-PROVISIONAL-N=1 graveyard** already flagged at v86 audit for v90 CONSOLIDATION. Most prudent framing: register as PROVISIONAL N=1 WITH explicit graveyard-risk acknowledgment; v90 audit consolidation may absorb v87's candidate into broader "VN-solo-dev with multi-product portfolio" sub-mechanism alongside v76 (Hoang) + v80 (Duy).

## CORPUS-FIRST observations consolidated for this entity

1. **CORPUS-FIRST Unlicense in v60+ window** (Pattern #29 / Pattern #45 framing-decision deferred to v90)
2. **CORPUS-FIRST tri-layer prompt-persistence** (per-chat / global-user / per-workspace skill)
3. **CORPUS-FIRST multi-mode skill-command-addressing with compositional modifier** (`/style` numeric + name + `+ terminal CLI` composition)
4. **CORPUS-FIRST pure-markdown T1 in v60+ window** (no Shell / HTML / TypeScript / Python / Rust primary; 100% markdown)
5. **LIGHT-end Pattern #84 84c.1 anchor** at 2-harness (full-distribution-observability 1→18 across v60+ window)
6. **Library-vocab strengthening**: "Deliberately-Narrow Distribution Profile" v79 + v80 + v87 = N=3 evidence (PROMOTION-ELIGIBLE at v90)
