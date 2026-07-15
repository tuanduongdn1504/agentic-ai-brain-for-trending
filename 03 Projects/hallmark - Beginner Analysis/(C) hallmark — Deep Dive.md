# (C) hallmark — Deep Dive (LLM Wiki v204)

> Claude-authored. Operator-requested: *"build LLM wiki for https://github.com/Nutlope/hallmark"* (2026-07-16). Source-verified by hand (README + `skills/hallmark/SKILL.md` + `references/slop-test.md` + `package.json` fetched directly; identity + landscape via WebSearch). The read-only 10-agent deep-dive workflow (`wf_eedf8a60-fbb`) **failed prompt-too-long on all 10 agents** (~204.7K > 200K limit — the oversized CLAUDE.md shim + tool catalog snapshotted into each subagent), so this ship was produced **INLINE + fully hand-verified**, per the v191/v200/v201/v202 self-throttle precedent.

---

## 1. One-liner

`Nutlope/hallmark` — **"A design skill for Claude Code, Cursor, and Codex that refuses to look AI-generated."** An anti-AI-slop **design skill** (a markdown `SKILL.md` + reference rule-files) that a coding agent installs so the pages it generates, audits, redesigns, or reverse-engineers avoid the generic "AI slop" aesthetic. Made by **Together AI**; author **Hassan El Mghari** (`@nutlope`). MIT. v1.1.0.

## 2. Identity & provenance (source-verified)

| Field | Value |
|---|---|
| Repo | `github.com/Nutlope/hallmark` |
| Tagline | *"A design skill for Claude Code, Cursor, and Codex that refuses to look AI-generated."* |
| Frontmatter | `name: hallmark` · `version: 1.1.0` · `description: "Anti-AI-slop design skill for greenfield pages, audits, redesigns, and design extraction from URLs or screenshots."` |
| License | MIT |
| Languages | CSS 58.3% / HTML 35.2% / JavaScript 6.5% (design assets + a static demo site + a markdown skill) |
| Stars / forks | ~8.2k★ / ~429 forks (**page-stated §37.4 — GitHub API mocked → NOT a Pattern #52 velocity claim**) |
| Releases | **0 published** (pin the commit, not a tag) |
| Author | **Hassan El Mghari** (`@nutlope`, nutlope.com) — **DevRel Lead at Together AI**; a prolific viral-indie-AI-app builder: RoomGPT, RestorePhotos, LlamaCoder ("open-source Claude Artifacts", Llama 3.1 405B), BlinkShot, Self.so, AI Commits, pdftochat, TurboSeek. **NOT Anthropic.** |
| Org | "Powered by Together AI" (an AI-inference / open-model company — a competitor infra vendor, **not Anthropic**) |
| Demo | usehallmark.com |
| Install | `npx skills add nutlope/hallmark` (the **agentskills.io / vercel-labs `skills` CLI verb**) — or copy `SKILL.md`+references to `.claude/skills` / a Codex skill dir, or paste the body into `.cursor/rules/hallmark.mdc` |

**Repo structure (source-verified):**
```
skills/hallmark/
  SKILL.md
  references/  (slop-test.md · macrostructures.md · typography.md · color.md ·
                layout-and-space.md · motion.md · copy.md · anti-patterns.md ·
                responsive.md · microinteractions.md · interaction-and-states.md ·
                hero-enrichment.md · custom-theme.md)
docs/  (recipes.md · study-examples.md)
site/  (the usehallmark.com static demo)
README.md · ROADMAP.md · LICENSE (MIT) · package.json · vercel.json
```

## 3. What it does — the four verbs (source-verified from `SKILL.md`)

Hallmark is a **markdown skill embedded in an AI code editor**, not a CLI binary. You trigger it with natural language; the four "verbs" are invocation modes, not shell flags.

1. **Default / generate** — a user brief → the skill picks **one** macrostructure (of 21, never bulk-loaded), applies the rule-sets, runs the pre-emit self-critique, then a 57-gate slop sweep, and emits. **Catalog** (the 20 named themes) by default; **custom** mode only if the brief signals a brand colour / multi-attribute vibe / explicit request. **Diversification is mandatory**: successive builds must differ on macrostructure *and* ≥1 theme axis (paper band / display style / accent hue).
2. **`hallmark audit <target>`** — score existing code against the anti-patterns, return a **ranked punch-list. READ-ONLY (no edits).**
3. **`hallmark redesign <target> [--mood <name>]`** — replace the visual / interaction layer, **preserve routes / IA / brand / copy.**
4. **`hallmark study <screenshot | URL>`** — extract design **DNA** (macrostructure / archetypes / type-pairing / colour), diagnose, and optionally **export a portable `design.md`**; explicitly rejects template-marketplace URLs as sources.

## 4. The machinery (source-verified)

- **57 enumerated slop-test gates (#1–#57)** across six axes. Sampled verbatim from `references/slop-test.md`:
  - Gate 2: *"Is there a purple-to-blue (or cyan-to-magenta) gradient anywhere — including a `background-clip: text` gradient headline?"*
  - Gate 6: 100vh centred hero with eyebrow/title/lede/CTA all on one centred axis.
  - Gate 10: `transition: all` used anywhere.
  - Gate 22: a neutral/surface colour with `oklch(... 0 ...)` (zero chroma).
  - Gate 34: horizontal scroll on any viewport 320–1920px.
  - Gate 40: any text/icon/`:focus-visible` ring failing its contrast threshold against its *computed* background.
  - Gate 42: the AI-default nav (wordmark-left + 4–5 inline links + button-right).
  - Gate 46: any quantitative claim the user didn't supply and the model fabricated.
  - Gate 49: any button/nav/footer link wrapping to two+ lines at any viewport.
  - Gate 57: a `study` diagnosis emitted but the build defaults to a catalog theme instead of studied DNA.
- **Pre-emit self-critique (verbatim):** *"Run this **before** the gate list, not after. Score the planned output 1–5 on each axis. Anything **< 3 on any axis triggers a revision pass** before the gate sweep."* Six axes = **Philosophy · Hierarchy · Execution · Specificity · Restraint · Variety.** The six scores are stamped at the top of the artifact: `/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */`.
- **21 macrostructures** (`references/macrostructures.md`): Specimen, Bento Grid, Long Document, Marquee Hero, Stat-Led, Workbench, Manifesto, Quote-Led, Catalogue, … — picked one at a time.
- **20 named themes** (catalog): Specimen, Atelier, Brutal, Newsprint, Studio, Manifesto, Terminal, Midnight, Almanac, Garden, Riso, Sport, Bloom, Coral, Cobalt, Aurora, Editorial, Carnival, Lumen, Hum.
- **Component archetypes:** 9 heroes, 5 section-heads, 6 features, 4 CTAs, 4 testimonials, 8 footers, 14 navs.
- **Core rule files:** typography · color (OKLCH-based) · layout-and-space (4pt scale) · motion · copy · anti-patterns · responsive · microinteractions · interaction-and-states · hero-enrichment.
- **Six universal disciplines** (all verbs): (1) pre-emit self-critique; (2) honest copy (no fabricated metrics/testimonials/logos); (3) locked tokens (named CSS custom properties only — no inline OKLCH/hex); (4) no re-drawn chrome (no fake browser/phone/IDE frames); (5) mobile at 320/375/414/768px (non-negotiable floor); (6) typography purity (italic headers always banned; emphasis via weight/colour/underline).
- **Token-efficiency rule (verbatim):** *"Never load the whole index plus more than one per-macro file in a single build."*

### ⚠️ Doc inconsistency caught by hand
The README markets **"fifty-seven slop-test gates."** `references/slop-test.md` **enumerates exactly 57** (highest # = 57). But the SKILL.md summary and the self-critique prose call it a **"fifty-eight-gate review"** — i.e. the pre-emit self-critique is counted as an implicit 58th pass. **Authoritative enumerated count = 57 (#1–#57) + a 6-axis pre-emit critique;** the "58" is a framing/rounding artifact, not a discrepancy in capability. (This is the class of doc-vs-doc nuance the vault's hand-verification exists to catch — cf. marketingskills v202 "50→47", career-ops v200 "21→~53".)

## 5. Attribution & lineage (the #57 check, done by hand)

Hallmark cites, as consensus **sources** for its anti-slop rules:
- **"Anthropic's frontend-design skill"** — a real Anthropic artifact (a ~50-line `SKILL.md`, ~300K installs by late-April 2026; the purpose/tone/constraints/differentiation four-question framework).
- **"The Claude cookbook on frontend aesthetics"** — Anthropic cookbook material.
- **"Powered by Together AI"** and the **"2026 tactile rebellion"** design movement as framing/inspiration.

**No non-Anthropic third-party derivation** (no v0, shadcn, Framer, Webflow; no other author's repo). **This is NOT a Pattern #57 corpus-recursion:** "Anthropic's frontend-design skill" and "a Claude cookbook" are *Anthropic-upstream references* (mentions of Anthropic material), not a corpus **subject** citing another corpus **subject** as an influence. It IS a notable **(d) cross-reference**: hallmark and corpus subject **impeccable v75** (Paul Bakaus) *both* build on Anthropic's frontend-design skill — the corpus's design-skill cluster converges on the same Anthropic upstream.

## 6. Landscape — where hallmark sits (source: WebSearch, by hand)

The anti-slop-design-skill space is **crowded and Anthropic-anchored**:
- **Anthropic's own `frontend-design` skill** is the upstream (~300K installs) + **Claude Design** (claude.ai/design, launched 2026-04-17) ships Anthropic's own anti-slop guardrails.
- A marketplace of competing anti-slop skills exists (skills.rest "anti-slop-design", mcpmarket "Design Anti-Slop", LobeHub "anthropic-frontend-design", etc.).
- hallmark is a **notable, well-built, more-productized** instance (57 gates + pre-emit critique + 20 themes + 21 macrostructures + audit/redesign/study verbs + a hosted showcase), with third-party coverage (e.g. a Mervin Praison writeup, 2026-05).
- **NOT world-first**, and **NOT corpus-first**: in-corpus, **impeccable v75 / taste-skill v81 / huashu-design v82 / open-design v83 / ui-ux-pro-max v85** all precede it in the design-skill / anti-slop family.

## 7. Supply-chain (#66) — BENIGN

`package.json` v1.1.0: **zero dependencies, NO postinstall/preinstall/prepare** — the only script is `serve` (`python3 -m http.server --directory site 4173`). The repo is **CSS/HTML/markdown design assets + a static demo site + a `SKILL.md`** — no install-time code execution. `npx skills add nutlope/hallmark` runs the **external agentskills.io `skills` CLI** (which copies the markdown skill into your agent's skill dir) — that external CLI is the only thing to `npm-security-check`; hallmark itself installs no code. Read-only `audit`/`study` add zero write risk; `redesign`/generate write code you review.

## 8. Source-verification note

Verdict + all corpus/collision/identity/mint claims produced **BY HAND** (per `feedback_wiki_verify_independently_check_collisions`). Hand-fetched: README, `skills/hallmark/SKILL.md`, `references/slop-test.md`, `package.json`, `docs/recipes.md`, the repo tree; WebSearch for identity (Hassan El Mghari / Together AI, NOT Anthropic) + landscape (Anthropic frontend-design skill + Claude Design + the crowded anti-slop marketplace). Corpus collisions hand-grepped over `_state/` + `_patterns/`: **zero prior hallmark / Nutlope / Together-AI subject** (collision-clean); the design-skill cluster (impeccable v75 / taste-skill v81 / huashu-design v82 / open-design v83 / ui-ux-pro-max v85) + **Pattern #88 "Anti-Slop-Curation"** (CONFIRMED) + the §C registry all read by hand. The 10-agent read-only workflow failed prompt-too-long (shim-too-big; a recurrence of the v167 structural issue) → not re-run; no workflow output was relied on.
