# Original Deep-Dive: Design Skills — UI UX Pro Max + Awesome Design MD + design.md

## Source

- **UI UX Pro Max:** [github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) + npm `uipro-cli`.
- **Awesome Design MD:** [github.com/voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md).
- **design.md format:** [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md) (Google Labs).
- Verified (`gh api`, 2026-06-29) — see table.

| Repo | Stars | License | Lang | Created |
|---|---|---|---|---|
| `nextlevelbuilder/ui-ux-pro-max-skill` | **97,573★** | MIT | Python | 2025-11-30 |
| `voltagent/awesome-design-md` | **94,132★** | MIT | (markdown) | 2026-03-31 |
| `google-labs-code/design.md` | 22,960★ | Apache-2.0 | TypeScript | 2026-04-10 |

---

## UI UX Pro Max (skill #3)

- **What:** a design-intelligence skill for Claude Code/Cursor/Windsurf/18+ agents; on a UI request it matches product-type → palettes/styles/typography/spacing and emits a full design system incl. "patterns to avoid".
- **⚠️ Big correction:** the video says it's "trained on hundreds of industry-specific data". **REFUTED** — there is **no ML training**. It bundles **curated CSV lookup tables** (67 UI styles / 161 color palettes / 57 font pairings / 99 UX guidelines / 25 chart types) + **161 hand-written reasoning rules** driving a **deterministic reasoning engine**. All data is local CSV; no API keys, no model calls of its own.
- **Install:** `npm i -g uipro-cli && uipro init --ai claude --global` (writes to `~/.claude/skills/`; requires **Python 3.x**), or `/plugin add nextlevelbuilder/ui-ux-pro-max-skill`.
- **Install safety (verified LOW risk):** **no postinstall script**; deps are 4 standard CLI libs (commander/chalk/ora/prompts); on `init` it downloads release assets from the GitHub API (with bundled fallback) — no telemetry observed. Caveat: **`nextlevelbuilder` org ownership is opaque** (no named maintainer found).

## Awesome Design MD (skill #4)

- **What:** **73 curated `DESIGN.md` files** scraped/derived from major brands (Claude, Stripe, Figma, Apple, Spotify, Tesla, Notion, Vercel, Cursor, Lovable, ClickHouse, …). Copy one into your repo, reference it in `CLAUDE.md`/cursor rules, and the agent restyles your UI to that brand system.
- **Install:** copy-based (clone the repo / copy a file) — there is **no single npm install** for the collection (the video's "run this command" is the optional Google `npx @google/design.md lint` validator, or a per-skill install).

## The `design.md` format (the concept Eric attributes to Google Stitch)

- **Origin (CONFIRMED, with nuance):** `design.md` (a markdown + YAML-tokens design-spec readable by AI agents) was **created by Google *inside* Stitch** (Google's AI UI tool; Stitch launched at Google I/O, May 2025), then **open-sourced by Google Labs ~April 2026** (Apache-2.0). It was **not** a pre-existing community convention that Google later adopted (web searches for a 2023–24 `design.md` convention returned nothing).
- **Nuance:** the *broader* "markdown-as-agent-format" trend **is** a community pattern (`AGENTS.md`, `SKILL.md`, `CLAUDE.md`); `design.md` is the design-specific, Google-originated member of that family.
- (Auto-captions garbled "Stitch" → "Stage"; the video means Stitch.)

## How this compares to what the operator already has

The vault already surfaced a **stronger, Claude-native design lever**: the **Taste Skill** (`leonxlnx/taste-skill`, ~47K★, MIT, 62-point anti-slop gate — [[ai-web-design-workflow/_index]]), plus Anthropic's **first-party `frontend-design` skill**. Relationship:

- **Taste Skill** = opinionated *quality gate* (anti-slop, em-dash ban, WCAG, motion isolation) — best for *fixing taste*.
- **UI UX Pro Max** = *generative* design-system from lookup tables — best for *cold-start* design by niche.
- **Awesome Design MD** = *imitate a specific brand* (copy its `design.md`).
- **Anthropic `frontend-design`** = first-party baseline.

They're composable: generate with UI UX Pro Max or a brand `design.md`, then gate with the Taste Skill.

## Operator relevance (hireui Goal #2)

- Extract a **TalentAxis `DESIGN.md`** (codify the real hireui brand tokens) and version it — directly supports the **Candidate-Detail refactor** (the token-drift root cause documented in the operator's spike).
- Run a 3-way bake-off on the hireui frontend: Taste-Skill-gate vs UI-UX-Pro-Max-generate vs brand-`DESIGN.md` — measure against the Figma source-of-truth.
- Install per hireui **I-8** (operator-installs skills) + **I-2** (agent-* branch) governance.

## Key Takeaways

- UI UX Pro Max is a **deterministic CSV reasoning engine**, not a trained model — and it's install-safe.
- `design.md` is genuinely a **Google Stitch** invention (open-sourced ~April 2026); the broader markdown-as-format trend is community.
- For the operator, the design layer is **already covered better by the Taste Skill** — treat these as alternatives/complements, with `DESIGN.md`-as-brand-codification the most novel addition.

## Related

[[ai-web-design-workflow/_index]] · [[claude-code-skills-stack/the-eight-skills]] · [[claude-skills/_index]] · [[claude-api-cost-optimization/_index]]
