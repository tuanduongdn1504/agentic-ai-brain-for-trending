# DESIGN.md as a portable source of truth

> **This is the single most stealable idea in the whole topic** — usable *without installing Open Design at all*. If you read one article for the hireui angle, read this + [[open-design/huashu-design-deep-dive]].

## Source

`nexu-io/open-design` README (design-systems section) + [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md) README (the schema's origin, gh-api: **94,742★**, MIT, created 2026-03-31) + [`bergside/awesome-design-skills`](https://github.com/bergside/awesome-design-skills) (1,482★, MIT). Workflow `wf_4a91a8b2-2bb` agent `designmd`.

## The idea

A **`DESIGN.md`** is a **single plain-markdown file that *is* your design system** — colors, type, spacing, components, motion, voice, brand, anti-patterns — written so both a human *and* a coding agent can read it directly. No Figma export step, no theme-JSON transpile, no proprietary format. Open Design's slogan: *"design systems are portable markdown + team JSON."*

Because it's markdown in your repo, it is **version-controlled, diff-able, reviewable in a PR, and portable across any of the 15+ agents** — the same brand contract drives Claude Code today and Codex tomorrow without a rewrite. Open Design layers a small **`open-design.json`** manifest beside it for marketplace/discovery metadata, keeping *brand logic (markdown)* decoupled from *discovery/execution (JSON)*.

## The 9-section schema (⚠️ two versions — know the difference)

The README credits `VoltAgent/awesome-design-md` as the source of a **"9-section DESIGN.md schema and 70 product systems."** But the two projects publish **different** 9-section lists — flag this rather than blending them (a real discrepancy the workflow surfaced):

| | **VoltAgent/awesome-design-md** (the origin) | **Open Design's own `DESIGN.md`** |
|---|---|---|
| 1 | Visual Theme & Atmosphere | Color |
| 2 | Color Palette & Roles | Typography |
| 3 | Typography Rules | Spacing |
| 4 | Component Stylings | Layout |
| 5 | Layout Principles | Components |
| 6 | Depth & Elevation | Motion |
| 7 | Do's and Don'ts | Voice |
| 8 | Responsive Behavior | Brand |
| 9 | Agent Prompt Guide | Anti-patterns |

Both are "9 sections" and cover overlapping ground (color, type, layout, components, anti-patterns/Do's-and-Don'ts); Open Design **adapted** VoltAgent's schema rather than copying it verbatim. The **"Agent Prompt Guide"** (VoltAgent §9) is the agent-native twist: a section written *to* the coding agent about how to apply the system. Open Design ships **~150 pre-built systems** (Linear, Stripe, Vercel, Airbnb, Apple, Tesla, Notion, Anthropic, Cursor, Supabase, Figma, …).

## Why this is the fix for hireui's token drift

The hireui **Candidate Detail** refactor is drowning in exactly the failure `DESIGN.md` is designed to prevent: **drifted, half-migrated tokens with no authoritative record** — navy `#1E2960`→`#002D79`, accent `#E8743C`→`#DC6803`, Inter→Roboto, orphaned spacing/type tokens, a stalled r1→r2 migration. Today the "source of truth" is split across Figma, `tokens.ts`, and tacit knowledge — so it drifts.

The `DESIGN.md` move: **make one markdown file the canonical brand contract**, check it into the repo, and treat Figma + `tokens.ts` as *render targets* of it, not competing authorities. Then any agent regenerating a component reads the same contract and can't invent a fourth navy.

You do **not** need Open Design installed to do this. You can:
- **Steal the pattern:** author `apps/mobile/.../DESIGN.md` (or a `design-systems/hireui-talentaxis/DESIGN.md`) with the reconciled Figma r2 values, and reference it from every agent prompt + your `CONSTITUTION`.
- **Or adopt the tool:** create it as an Open Design design system (`od design-system create`) and let the app enforce it across generations.

Either way it's a **portable, agent-agnostic single source of truth** — the thing hireui is currently missing. Concrete methods: `output/(C) 2026-07-01-open-design-pilot-methods.md` (H2, S1, S3).

## Relationship to your existing anti-slop stack

`DESIGN.md` answers *"what is on-brand?"* (the positive contract). Your **Taste Skill** ([[../ai-web-design-workflow/_index]]) and huashu-design's **anti-AI-slop checklist** ([[open-design/huashu-design-deep-dive]]) answer *"what is generic slop to reject?"* (the negative gate). They compose: `DESIGN.md` sets the target; the anti-slop gates catch drift away from it. `bergside/awesome-design-skills` bundles design skills that pair a `SKILL.md` (workflow) with a `DESIGN.md` (system) — the same two-file idea.

## Key Takeaways

- **`DESIGN.md` = your whole design system as one portable, version-controlled, agent-readable markdown file.** Brand logic in markdown; discovery/execution metadata in a sidecar JSON.
- The **9-section schema originates from `VoltAgent/awesome-design-md`** (94.7K★) but **Open Design ships its own 9-section variant** — they differ; don't conflate the two lists.
- It is the **direct structural fix for hireui's drifted tokens**: one canonical contract, Figma/`tokens.ts` become render targets — and you can adopt the *pattern* with zero install.
- It **composes with your anti-slop stack**: `DESIGN.md` defines on-brand (positive), Taste Skill + huashu anti-slop checklist reject off-brand (negative).
