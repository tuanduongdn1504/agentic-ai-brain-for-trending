# (C) marketingskills — Deep Dive

**Wiki v202** · shipped 2026-07-15 · subject `github.com/coreyhaines31/marketingskills`
**One line:** the largest / most-used **marketing-vertical agent-skill collection** — 47 Claude-Code-first skills covering the whole marketing/GTM funnel, plus a `tools/` execution layer wiring ~100 real marketing platforms — by Corey Haines (Swipe Files).

> **Verification note (read first).** The read-only deep-dive workflow (9 agents) **failed** — every agent hit "Prompt is too long" / autocompact-thrashing because the repo's JS-heavy `tools/` tree blows a cloning agent's context. So **100% of this wiki is hand-verified** (targeted WebFetch of the rendered repo + raw files + README + VERSIONS.md + tools/REGISTRY.md + WebSearch), which is the strongest posture under the vault's `feedback_wiki_verify_independently_check_collisions` rule. Metrics are page-stated (§37.4 — GitHub API is mocked) → **no Pattern #52 velocity claim**. Two page-read errors were caught + corrected by hand (see *Caveats*).

---

## 1. What it is

Repo tagline (verbatim): *"Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering."*

README opening (verbatim): *"A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the Agent Skills spec."*

It is a **domain-vertical agent-skill collection** — markdown `SKILL.md` files (agentskills.io standard) that give a coding agent marketing expertise it doesn't have out of the box — **plus** a `tools/` layer of executable integrations so those skills can actually *act* against real marketing platforms. The README's second paragraph points to the author's other properties (Conversion Factory, Swipe Files, AI Marketing Training) and to **Magister** — *"an autonomous AI agent that uses these skills to be your CMO"* (a hosted product sitting on top of this open collection).

- **License:** MIT (*"Use these however you want."*)
- **Language stats (page-stated):** JavaScript 93.9% / HTML 4.6% / Shell 1.5% — **the JS is the `tools/` integration layer + the `ad-creative` CLI tools, not the skills** (the skills are markdown; see §4).
- **Metrics (page-stated §37.4, NOT velocity):** ~39.3k★ / ~6.3k forks / ~374 commits.
- **Current version:** **v2.8.10** (VERSIONS.md, 2026-07-14). Version tracking began 2026-01-27 → a ~6-month-old, very actively developed repo (~30 → 47 skills).

## 2. The 47 skills (directory-verified)

Corey Haines' own README groups them by funnel stage. Hand-verified against the `skills/` directory listing (47 folders):

| Group | Skills |
|---|---|
| **Foundation** | `product-marketing` (the shared-context anchor — see §3) |
| **Conversion (CRO)** | `cro`, `signup`, `onboarding`, `popups`, `paywalls` |
| **Copy & content** | `copywriting`, `copy-editing`, `cold-email`, `emails`, `sms`, `social`, `image`, `content-strategy` |
| **SEO & discovery** | `seo-audit`, `ai-seo`, `programmatic-seo`, `site-architecture`, `schema`, `competitors`, `aso` |
| **Paid & distribution** | `ads`, `ad-creative`, `directory-submissions`, `co-marketing` |
| **Measurement** | `analytics`, `ab-testing` |
| **Retention & growth** | `churn-prevention`, `referrals`, `lead-magnets`, `free-tools`, `marketing-loops` |
| **Strategy & monetization** | `marketing-ideas`, `marketing-psychology`, `launch`, `pricing`, `offers`, `marketing-plan` |
| **Sales & RevOps** | `revops`, `sales-enablement`, `prospecting`, `customer-research`, `competitor-profiling` |
| **PR & community** | `public-relations`, `community-marketing` |
| **Orchestration** | `marketing-council` (the persona board — see §3) |

These are **sub-functions within one professional domain (marketing/GTM)** — the same way cybersecurity v98 spans recon/exploit/defense or ai-berkshire v187 spans sizing/screening/moats. That is what makes this a *single-vertical* collection, not a cross-functional one (see the Verdict's pattern outcome).

## 3. Architecture — three ideas worth stealing

**(a) The shared-context foundation doc.** `product-marketing` is the anchor: it interviews you (section-by-section, never all questions at once, with a strict validate-before-advancing sequence) and writes `.agents/product-marketing.md` — a 12-area context document (positioning, ICP, personas, pains, competitive landscape, differentiation, objections/anti-personas, JTBD *four forces*, verbatim customer language, brand voice, proof points, goals). README: *"every other skill checks it first."* So the collection isn't 47 independent skills — it's a **hub-and-spoke** where one skill establishes durable product context the rest consume. Frontmatter is agentskills.io-core (`name` + a trigger-phrase-rich `description` + `metadata.version`); no Claude-Code-only extensions observed.

**(b) The persona council.** `marketing-council` (added v2.8.0) convenes a **simulated board of 12 legendary marketers**: seats 3–5 (or all 12 for big calls), *always includes a documented dissenter*, applies each advisor's real published frameworks (dossiers in `references/advisors/`), maps 2–4 genuine disagreements → synthesizes a fitted recommendation with skill hand-offs. Guardrails: no fabricated quotes, label output as simulation, prioritize living advisors. *"A council that agrees is a mirror, not a board."* This is the **domain-expert adversarial persona-panel** pattern — the same shape as ai-berkshire v187's `/investment-team` (4 investing masters) and adjacent to agency-agents v185's persona library. The pattern is now recurring across the corpus (see the Verdict's SECONDARY notes).

**(c) Verification gates + anti-fabrication.** `seo-audit` (a 5-domain diagnostic: technical / i18n / on-page / content-quality / site-type) carries an explicit *verification boundary*: `web_fetch`/`curl` can't see JS-injected JSON-LD, so it forces DevTools / Google Rich Results / Screaming Frog — preventing false-negative findings. `marketing-loops` (v2.6.0) is 43 repeatable workflows with a nine-part anatomy and **idempotency guardrails**. These are exactly the disciplines the vault's own skills enforce.

## 4. The `tools/` execution layer (the JS 93.9%)

The skills are markdown; the JavaScript is the **integration/execution layer** in `tools/` (hand-verified from `tools/REGISTRY.md`, which calls itself *"Quick reference for AI agents to discover tool capabilities and integration methods"*):

- **`tools/clis/`** — zero-dependency Node.js CLIs (native `fetch`, env-var auth, JSON output) for platforms without official CLIs: `ga4.js`, `hunter.js`, `stripe.js`, etc. Plus the `ad-creative` skill shipped **51 zero-dependency CLI tools** (v2.x, Feb 2026). This is the bulk of the JS.
- **`tools/composio/`** — a wrapper giving managed OAuth + pre-built connectors to **500+ tools via a single Composio MCP server** (HubSpot, Salesforce, Meta Ads, LinkedIn Ads, Google Sheets…). Note: the collection **consumes** Composio's MCP server — it does **not** ship its own MCP server.
- **`tools/integrations/`** — markdown setup guides per platform.

Net: wired up, the skills can read/write data, send emails, manage ad campaigns, even process payments across **~100 marketing/sales/analytics/payment platforms**. Crucially, **there is no auto-execution** — every integration requires explicit user setup (API keys / OAuth as env vars); nothing touches a live account unless you connect it. This is the "autonomous CMO" (Magister) substrate, delivered as open tooling.

Root also carries `.claude-plugin/` (the Claude Code plugin-marketplace manifest), `AGENTS.md` + `CLAUDE.md` (LLM routing artifacts, both present), `VERSIONS.md` (the changelog), and two `validate-skills*.sh` (the Shell 1.5% — a skill-format validator / CI).

## 5. Distribution — 5 install paths, cross-harness (README-verbatim)

```
npx skills add coreyhaines31/marketingskills          # agentskills.io CLI (recommended)
npx skills add coreyhaines31/marketingskills --skill cro copywriting
npx skills add coreyhaines31/marketingskills --list

/plugin marketplace add coreyhaines31/marketingskills # Claude Code plugin
/plugin install marketing-skills

git clone …/marketingskills.git && cp -r marketingskills/skills/* .agents/skills/
git submodule add …/marketingskills.git .agents/marketingskills
npx skillkit install coreyhaines31/marketingskills    # multi-agent
```

Supported harnesses: **Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports the Agent Skills spec.** One canonical skill source is consumed by many hosts via the standard `skills`/`skillkit` CLI + the `.agents/skills/` convention (this is provider-agnostic-by-design distribution — Pattern #84 84c; *not* the ponytail-v168 14-platform-generator mechanism). **There is no root `package.json`** — `npx skills add` runs the *external* agentskills.io `skills` CLI, not this repo's own package.

## 6. Author

**Corey Haines** (`coreyhaines31`) — a well-known SaaS/startup marketer and educator: founder of **Swipe Files** (a SaaS-marketing newsletter + paid community), **Conversion Factory** (a marketing agency/studio), **AI Marketing Training**, and **Magister** (the hosted autonomous marketing agent). He is **not affiliated with Anthropic**, and is **not** the well-known software-crafting "Corey Haines" (handle `coreyhaines`) — this is the *marketing* Corey Haines (handle `coreyhaines31`). Distinguishing the two was a deliberate hand-check.

## 7. Landscape (world, not corpus)

Marketing agent-skill packs are a **populated space**, not a novelty: peers include `realjaymes/marketingagentskills` (28 skills), `agentkits-marketing`, and multi-domain packs like `alirezarezvani/claude-skills` (345 skills across many domains). Third-party roundups (Composio's "best marketing skills," a Medium "10 best Claude marketing skill repos 2026," aibuilderclub) consistently name **coreyhaines31/marketingskills as the most-used / canonical** marketing pack — but it is **not world-first** for the category. This matters for the pattern outcome: it's the strongest *instance* of an already-populated class, not a new capability.

## 8. Caveats (blunt)

- **The hard marketing knowledge is Corey Haines' expertise packaged** — the engineering value is the *collection architecture* (foundation doc, persona council, integration layer, agentskills.io distribution), not novel software. Weight the quality of any single skill against your own marketing judgment; depth varies across the 47-skill long tail.
- **Doc-vs-page discrepancies caught by hand:** the rendered repo page reported "50 skills" and "latest v2.6.0" — both wrong. Authoritative: **47 skills** (directory + README list + VERSIONS.md "47 total as of v2.8.0") and **v2.8.10** (VERSIONS.md changelog, Jul 14 2026). The "22 releases" is a page-stated Releases-tab count that appears to lag the changelog.
- **Metrics are page-stated (§37.4)** — the ~39.3k★ is not API-verified and carries **no velocity claim**.
- **The execution layer is dual-use** — wired with real keys, skills can act against live marketing/sales/**payment** accounts. No auto-execution, but treat any real integration with the standard fence (see the Pilot Methods Menu §66).
- **Off the software-engineering core.** Marketing is not Goal #1's domain; this earns its INCLUDE on the *substrate* (a Claude-Code-first agentskills.io collection — the exact thing the vault studies) and a real TalentAxis-GTM pilot angle, exactly like ai-berkshire v187 (value investing) and OpenMontage v188 (video). See the Verdict.

---
*Companion docs in this folder: `(C) marketingskills — Verdict.md` · `(C) marketingskills — Pilot Methods Menu.md` · `wiki.html`. Prefix `(C)` = Claude-authored.*
