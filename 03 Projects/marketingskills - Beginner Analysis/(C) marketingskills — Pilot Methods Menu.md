# (C) marketingskills — Pilot Methods Menu

**Subject:** `coreyhaines31/marketingskills` — a Claude-Code-first marketing-vertical agent-skill collection (47 skills + a `tools/` integrations layer) by Corey Haines (Swipe Files / Conversion Factory / Magister).
**Wiki:** v202 (2026-07-15). **Verdict:** GOAL-ALIGNED INCLUDE 3/4. **Pattern outcome:** NO MINT (Domain-Vertical-Skill-Collection instance-strengthening — marketing = a new vertical; the v187 ai-berkshire precedent).

> **How to read this.** 24 methods in six escalating groups: **A** read & learn (zero risk) → **B** borrow patterns zero-install → **C** hands-on scratch trial → **D** TalentAxis/hireui GTM (Goal #2, business) → **E** personal / Scrum-coach → **F** vault-meta. The sharpest **on-Goal-#1** value is the *architecture* (how a 47-skill single-vertical collection is built), not the marketing content itself — treat this the way v187 ai-berkshire was treated: **steal the engineering patterns.**
>
> ⭐ **One-thing path: A1 → B5 → F22** — read how the collection is architected (foundation-context-doc + cross-skill references + persona-council + agentskills.io distribution), steal those two patterns into the vault's own `05 Skills/`, then use the whole thing as the structural template to build the operator's OWN domain-vertical skill collection (recruitment / hireui). That is the Goal-#1 substrate transfer *and* a Goal-#2 artifact in one line.
>
> **Fence (applies to every hands-on method):** install-snapshot before any `npx`/plugin install · `npm-security-check` the **external** `skills` / `skillkit` CLI (that CLI is what runs — the repo itself has no root `package.json`/postinstall) · **inspect `tools/` (composio / clis / integrations) before wiring any real marketing-platform API key** · MIT-licensed so patterns are safe to borrow · keep TalentAxis GTM work **separate from hireui's engineering CONSTITUTION** (this is business/marketing, not product code — don't run it against the hireui repo) · pin to `v2.6.0`.

---

## A — Read & learn (the architecture; zero risk)

- **A1 ⭐ — Read it as a domain-vertical-collection case study.** Read `skills/product-marketing/SKILL.md` (the foundation) + `skills/marketing-council/SKILL.md` (the persona board) + one execution skill (`cro` or `seo-audit`). Goal: internalize *how* a 47-skill single-vertical collection is structured — this is the on-Goal-#1 payoff.
- **A2 — Study the distribution.** Read the README's 5 install paths (`npx skills add`, Claude Code `/plugin`, git-clone-cp to `.agents/skills/`, submodule, `skillkit`). This is a live map of the agentskills.io ecosystem's install surface (the v51/v76/v93/v184/v201 thread).
- **A3 — The shared-context-foundation pattern.** Note how `product-marketing` writes `.agents/product-marketing.md` and *every other skill checks it first*. This is a reusable architecture idea (one skill establishes durable context that the rest consume), distinct from independent one-off skills.
- **A4 — The verification-gate + anti-fabrication discipline.** `seo-audit` warns "web_fetch/curl can't see JS-injected JSON-LD → use DevTools/Rich Results/Screaming Frog"; `marketing-council` forbids fabricated quotes and labels output as simulation. These are exactly the disciplines the vault's own verify rule enforces.

## B — Borrow patterns zero-install (into the vault / the operator's own skills)

- **B5 ⭐ — Steal the foundation-context-doc pattern.** Add a vault-wide (or hireui-wide) `context.md` that a "project-context" skill establishes and every other skill references first — the `product-marketing` → `.agents/product-marketing.md` move, generalized. High ROI, zero install.
- **B6 — Steal the persona-council.** Port `marketing-council` (seat 3–5 conflicting advisors, always a dissenter, disagreement-map → synthesis, no fabricated quotes) into a **code-review / design-review / architecture-decision council** skill. This composes with ai-berkshire v187's `/investment-team` and agency-agents v185 — the persona-panel pattern is now recurring; build your own.
- **B7 — Steal the verification-boundary idiom.** Adopt seo-audit's "this tool can't observe X → use Y instead" pattern in the vault's own skills (e.g. "a static read can't verify runtime behavior → drive the app"). Prevents false-negative agent findings.
- **B8 — Steal the anti-fabrication rule.** "Grounded in documented positions; no invented quotes; label simulations" → paste into `CLAUDE.md` and any hireui LLM-feature spec (composes with the career-ops v200 anti-fabrication rule and the candidate-LLM-legibility ADR).

## C — Hands-on scratch trial (low-risk)

- **C9 — Snapshot + list.** `install-snapshot`, then `npx skills add coreyhaines31/marketingskills --list` in a throwaway dir to see the 47 skills without installing anything into a real project.
- **C10 ⭐ — Run `product-marketing` for TalentAxis.** In a scratch dir, install just `product-marketing` (`npx skills add coreyhaines31/marketingskills --skill product-marketing`) and let Claude Code build a TalentAxis `.agents/product-marketing.md` (positioning/ICP/personas/differentiation). A real, low-risk artifact + a firsthand look at the foundation skill.
- **C11 — Run `seo-audit` on a scratch clone of the TalentAxis marketing site.** See the 5-domain diagnostic + the verification-gate in action.
- **C12 — Inspect `tools/` before wiring anything real.** Read `tools/composio/`, `tools/clis/`, `tools/integrations/`, `tools/REGISTRY.md` to understand what the execution layer connects to **before** giving any skill a real marketing-platform API key. Never let an autonomous skill act against a live marketing account on the first run.

## D — TalentAxis / hireui GTM (Goal #2, business — NOT hireui engineering)

- **D13 ⭐ — TalentAxis positioning/ICP doc.** Use `product-marketing` to produce TalentAxis's positioning, ICP, personas, differentiation, JTBD, and customer-language doc. This is a genuine business deliverable and the input for everything below.
- **D14 — Marketing-site copy + CRO.** Use `copywriting` + `copy-editing` + `cro` + `signup` + `onboarding` on a scratch clone of the TalentAxis marketing site (never the product repo).
- **D15 — Pricing & offers.** `pricing` + `offers` to pressure-test TalentAxis's packaging.
- **D16 — Feature-launch playbook.** `launch` for the next hireui feature release (announcement, positioning, channels).
- **D17 — Council a GTM decision.** Run `marketing-council` on a real TalentAxis GTM question (e.g. "PLG vs sales-led for recruiters?") to surface the trade-offs before committing.
- **D18 — Discovery/SEO.** `seo-audit` + `ai-seo` + `programmatic-seo` + `schema` for TalentAxis's organic discovery (recruiters searching for ATS/sourcing tools).

## E — Personal / Scrum-coach (off the software goal)

- **E19 — Personal brand.** `marketing-psychology` + `copywriting` + `content-strategy` for the operator's own consulting/coaching brand.
- **E20 — Community.** `community-marketing` + `co-marketing` for a Scrum/agile community or newsletter.
- **E21 — Thought-leadership funnel.** `lead-magnets` + `emails` + `free-tools` (strategy) to package coaching IP.

## F — Vault-meta (Pattern Library / corpus)

- **F22 ⭐ — Build a recruitment domain-vertical skill collection.** Use marketingskills as the *structural template* (foundation-context-doc + cross-skill references + persona-council + agentskills.io distribution) to build the operator's OWN single-vertical collection for recruitment/hireui. This is the on-Goal-#1 architecture transfer — the highest-leverage output of this wiki.
- **F23 — File the persona-council thread for the audit.** ai-berkshire v187 `/investment-team` + agency-agents v185 personas + marketingskills `marketing-council` = a recurring "domain-expert adversarial persona-panel" pattern (N≥3 now). Recorded as a DEFERRED watch axis for the overdue ~v192 audit (do not self-mint).
- **F24 — Record the OSS-under-hosted-product + the mint-alternative note.** Magister (the hosted "autonomous CMO" agent) sits on top of the open marketingskills — an OSS-skills-under-a-hosted-product relationship (cf. meetily v196 PRO / PilotDeck). Also record the reviewable NO-MINT alternative: the "§C #4 Multi-Domain (Cross-Functional)" reading (if broad-GTM counts as cross-functional) — defensible but loses to single-vertical (marketing = one professional domain).

---

*Prefix `(C)` = Claude-authored. Facts hand-verified per the wiki-verify discipline; page-stated metrics (§37.4) are not velocity claims. See the (C) Verdict + (C) Deep Dive in this folder.*
