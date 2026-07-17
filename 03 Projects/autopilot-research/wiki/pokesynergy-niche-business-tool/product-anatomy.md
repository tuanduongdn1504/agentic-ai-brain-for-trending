# Product Anatomy — the live PokéSynergy

*Verified by direct WebFetch of the live site (main loop) + Workflow `dive:product`. Where the video and the site differ, see [[pokesynergy-niche-business-tool/what-it-actually-is-vs-the-pitch]].*

## What it is

A free, no-login, browser-based **team builder for Pokémon Champions (VGC 2026 Doubles)**. Self-description on site:

> "PokeSynergy is a free Pokemon Champions team builder for players who want fast, explainable team checks instead of a blank roster grid."

Positioning is **explainability-first**: every weakness / threat / suggestion / damage label should have *"a short reason you can act on"* — not opaque scores. Designed for an *"edit-check-edit loop."*

## Feature suite

| Tool | What it does |
|---|---|
| **Team Builder** | Draft up to 6 Pokémon; import/export Showdown-style (+ text paste, screenshot import) |
| **Damage Calculator** | Damage ranges per attack (e.g. "88.5%–104.2%"; >100% = guaranteed KO) |
| **Speed Tiers** | Live speed comparison vs meta, with Tailwind / Trick Room / paralysis toggles; breakpoints vs real usage spreads |
| **Weakness Checker / Type Coverage / Type Chart** | Defensive/offensive type analysis |
| **Tier List** | By play-rate / results / role |
| **MetaDex** | Tournament data aggregator (play rates, win rates, top-8s per season) |
| **SynerDex** | Pokédex (forms, type filtering, evolutions, moves/abilities/items) |
| **PokeBox** | Preset manager for saving/organizing builds (local + optional cloud) |
| **Guides (×5)** | Beginner team building, stat points, tier-list reading, doubles-vs-singles, mega evolutions |
| **/vs comparison pages** | vs Pikalytics, ChampTeams, ChampionsLab, PokeBase, OP.GG |

## Tech stack (inferred from page source + policies)

| Layer | Tech | Evidence |
|---|---|---|
| Framework | **Next.js** | `/_next/image` URL patterns |
| Hosting | **Vercel** (inferred) | Vercel Web Analytics integrated |
| Auth | **Clerk** | privacy policy: "authentication identifiers through Clerk" |
| Analytics | **Vercel Web Analytics** | privacy policy |
| Storage (primary) | **Browser LocalStorage** | "stores team data … in your browser without requiring an account" |
| Storage (optional) | Cloud backup | "optional cloud backup (separate from required local storage)" |

**Architecture = local-first + optional cloud.** Core team editing is client-side (no account needed); tournament/meta data and analytics are server-backed. This is a deliberate **privacy-first / no-lock-in** design — notable given the operator's own [[external|hireui candidate-LLM legibility ADR]] leanings.

## Data sources (attribution)

- **Tournament results:** [LimitlessVGC](https://limitlessvgc.com/) (explicitly attributed).
- **Sprites / icons:** Pokémon Showdown + Serebii (site: "data, usage data, sprites, icons … may come from public or third-party sources").
- **Base stats / damage formula:** not explicitly cited; implements standard VGC mechanics (type effectiveness, STAB, weather, terrain, abilities, Doubles 0.75× spread penalty) — consistent with the ubiquitous `@smogon/calc` engine used across the ecosystem.

## Pricing & maturity

- **100% free.** No premium tier, ads, Patreon, Ko-fi, or donations. No login required.
- Terms **defer** commercialization: *"Before a broad public launch or paid plans, these Terms should be reviewed by qualified legal counsel."* → intent to maybe monetize later, no model announced.
- "Last content update" reported **~June 29–30, 2026**; cadence otherwise unknown (no public repo, commit history, issue tracker, or roadmap page found). No GitHub/Twitter/email surfaced on the site itself.
- Community: **Discord** (`discord.gg/88zqNjVnuU`).

## Key Takeaways

- It's a **mature-enough, genuinely useful, integrated workspace** — not a toy: 9+ tools, real tournament data, guides, competitor-comparison pages.
- **Modern indie web stack** (Next.js + Vercel + Clerk + local-first) — the kind a solo dev can stand up and run cheaply. Directly relevant to "build a tool like this."
- **Free + local-first + explainable** is a coherent trust posture; the monetization is entirely deferred (see [[pokesynergy-niche-business-tool/business-model-and-risks]]).
