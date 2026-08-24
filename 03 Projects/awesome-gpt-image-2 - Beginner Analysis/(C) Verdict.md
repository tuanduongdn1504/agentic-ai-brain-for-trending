# (C) Verdict — v272 `freestylefly/awesome-gpt-image-2`

**Ship date:** 2026-08-24 · **Branch:** `wiki/v272-awesome-gpt-image-2` off the v271 tip (`a6dc2db`) · **NOT auto-merged**

---

## Phase 0.9 STRICT — **GOAL-ALIGNED INCLUDE 3/4**

| Criterion | Verdict | Reasoning |
|---|---|---|
| **(a)** Storm Bear cultural-peer / Anthropic affiliation | **FAIL** | 苍何 / Cang He is a disclosed individual Chinese developer with a WeChat official account. No declared Anthropic affiliation; not a registered (a)-7 vendor-direct source. **Routine v2.7 §41 forbids inference from name, heritage or locale** — the disclosed-individual axis is answered NO. Consistent with v269, v270, v271. |
| **(b)** goal-relevance | **STRONG** | Ships a **Claude Code / Codex Agent Skill** published to npm and GitHub Packages, plus a **`.claude-plugin/marketplace.json`**, generated from a curated schema by a fail-closed generator — which is *this vault's own architecture*, built independently. Goal #1 (agent-capability substrate) is squarely hit. Goal #2 is hit too: it is a complete worked example of "OSS catalogue → monetised niche SaaS," the shape hireui occupies. **No §40 needed.** |
| **(c)** corpus / pattern-library value | **STRONG** | A build-breaking anti-AI-slop assertion; two sibling generators with opposite failure semantics; a measured 108-day freeze of the validated artifact against 33% growth of the unvalidated one; a Claude-co-authored root commit; 27 named payment tests that never run; the second instance of a 222-ship-stale Pattern #50 sub-variant. |
| **(d)** tractability | **STRONG** | MIT, cloned twice and verified, 10,666 lines JS + 2,179 SQL + 12 md, fully readable, generators executable locally. |

**Cleanly GOAL-ALIGNED. No §40 invocation, no operator override.**

**⚠️ Precedent note worth recording:** the corpus's two prior image-generation subjects — **v84 image-blaster** and **v139 image-extender** — both scored **0/4 STRICT** and shipped only on operator override. This subject is not that class. The agent skill, the plugin manifest and the schema-driven generator carry (b) on their own; the image domain is incidental to why it is on-goal.

---

## Mint decision — **NO MINT**

**Counts: 46 top-level patterns / 12 CONFIRMED Library-vocab — UNCHANGED. §C-1 = 12. §C-2 = 39.**
`inflation_check` **HELD** — 0 mints, 0 promotions, 0 retires.

### Recorded instance-strengthening (recorded, NOT self-incremented — the v205 / v235 discipline)

- ⭐⭐ **Pattern #50 sub-variant 50c — *"Aggregator-with-commercial-product-entry-bundled-in-repo"* — N=1 → N=2.**
  50c was registered at the **v50 audit** on the single anchor **v50 awesome-claude-skills (Composio Inc.)**, with the funnel terminus defined literally as *"Commercial-product install (`composio-skills/.claude-plugin/marketplace.json` …)"*. This repository ships a `.claude-plugin/marketplace.json` pointing at its own skill, inside an awesome-list aggregator, alongside 6 `aff=` and 3 `utm_` links in each of three READMEs — including `utm_campaign=awesome-gpt-image-2`, the **v40 UTM-instrumented-funnel** mechanism with the campaign named after the repo.
  ⚠️ **It was registered N=1 stale-flagged with a retirement review due at v60. That review is 222 ships overdue.** A genuine second instance arriving now is exactly what the row needed.
  ⭐ **Variant note for the audit:** at the v50 anchor the bundled entry pointed at Composio's *external* SaaS. Here **the entire commercial platform is committed in the same MIT repository as the catalogue that funnels to it** — 33 serverless handlers, Stripe, Alipay, a credit ledger, an 8-endpoint admin console and refunds. That is materially beyond 50c's formal statement, which specifies a *"separate commercial platform (distinct website … different codebases)."* The row may need widening or splitting; **that is an audit call, not a ship call.**
- **Pattern #68 Awesome-List-Genre** — instance-strengthening, code-carrying hybrid sub-variant (the v201 / v240 / v253 / v254 line). 50c *"mechanically requires Pattern #68 hybrid form"*; satisfied.
- **Pattern #88 88c machinery-with-enforcement** — an instance at the **build** layer rather than the review layer: a regex assertion that fails the build if the generated agent-facing artifact contains 不是…而是. ⚠️ Scope caveat recorded: 0 matches in the guarded file, **14 in unguarded files.**
- **Pattern #19 19a** — author not Anthropic.

### Declined: a new §C-2 standalone at N=1

Candidate framing: *"Curated Prose Catalogue Compiled into Both a Product Data Layer and an Agent Skill."* **Declined on five grounds:**

1. **Not corpus-first for the mechanism, decisive.** **C12** (v137 book-to-skill: arbitrary document → agent skill), **v240** awesome-dsh-plugin (per-plugin YAML → bilingual READMEs + a live public registry API — *"it is a REGISTRY not a document"*), **v269** OpenViking (one source → 103 byte-checked plugin copies), **v271** HiThink (code → 84 hash-pinned skill files). The compile-a-catalogue-into-an-agent-artifact move is among the corpus's better-represented threads. This instance's generator is bespoke to its own data, so it is not even C12's N=2 — C12's anchor is a *general-purpose tool* taking arbitrary documents. **ADJACENCY, not instance.**
2. **Not world-first.** Markdown-as-source-of-truth compiled to JSON for a static site is the ordinary Jamstack shape, older than any corpus subject.
3. **Form-factor within a genre.** Awesome-list is a genre the vault has ruled on at v170, v201, v240, v253 and v254, declining a mint every time.
4. **The interesting thing here is a method observation, not a capability class** — the asymmetry between a schema-gated pipeline and its prose-ungated sibling. Routine v2.8 §42 clause 5: *a method is not a capability.*
5. **§28 as a supporting ground only**, measured against **§C-1 = 12** per v2.8 §44 clause 5, and not load-bearing alone — grounds 1–4 each suffice.

⭐ **Fifteenth-consecutive §44 application behaving as designed:** the anti-inflation argument was written against §C-1 (12), not the 39-row catalogue, and explicitly demoted.

### Also declined

- **C16 Agent-Native Vendor CLI** (N=2, v143 + v271) — this ships no CLI beyond a skill installer, and the vendor's product is a catalogue, not an API.
- **#24 / C40 Product-First Native Application Retrofitted with a First-Party MCP Server** — there is **no MCP server anywhere** in this repository (extent: all 656 tracked files, needle `mcp`: 0 hits outside dependency noise).
- **#18 B1-MCP** — no MCP implemented.
- **Pattern #57 corpus-recursive** — ⭐ **explicitly DECLINED.** `packycode` appears in the vault at `_patterns/03-active-candidates.md:1683`, among cc-switch **v73**'s ~20 sponsors. **A shared sponsor is a funding relationship, not a dependency** — the v268 `vercel-labs` org-coincidence precedent. Recorded as an observation.

### DEFERRED watch axes registered (not self-executed)

1. **"An anti-AI-slop rule enforced as a build-breaking assertion on a generated artifact"** (N=1) — distinct from the review-time gates of the #88 design-skill cluster (v75/v81/v82/v83/v85/v204/v218).
2. **"A prompt-parameterization notation used at scale, documented nowhere, consumed by nothing"** (N=1) — the `{argument name="X" default="Y"}` convention: **204 occurrences across 70 of 529 case prompts (13.2%), 133 distinct argument names**, split **198 in `gallery-part-1.md` / 6 in `gallery-part-2.md`** (the two counts cross-validate exactly against the 204 measured from the parsed JSON). **68 of the 164 cases in the part-1 range use it (41.5%); 2 of 365 in the part-2 range (0.5%).** Documented in **0 of 12** tracked `.md` files. Parsed by **0 lines of code** (extent: `src/ api/ scripts/ agents/ index.html` — the single `argument` hit is `window.dataLayer.push(arguments)`). ⭐ **The project's tagline is "Prompt as Code"; it invented a parameter syntax, used it 204 times, abandoned it after case 165, explained it nowhere, and wrote nothing that reads it** — while `src/main.jsx:805` copies the prompt verbatim to the clipboard. (Mitigating: `src/main.jsx:2803` gives the user an editable prompt before generation.)
3. **"Library-vocab #13 OSS-with-hosted-Pro-SaaS-tier-on-MIT-base"** — **RETIRED at v96**; this is a clean second instance and is **re-registration-eligible at N=2** under the **C07** precedent (*retired at v151, re-registered at N=2 at the v184 ship*). Recorded for the audit.

---

## Streak

**v271 `GA:128` → v272 `GA:129 · OG:13 [7 ov]`.**
**52 consecutive goal-aligned ships, v220 → v272.**
**§35 CLEAR** — rolling 3-ship window {v270, v271, v272} = **0 OFF-GOAL**.
**Override review: 12th consecutive discharge** — v153 → v272 = 0 overrides. Lifetime 10, of which 3 logged `[ceiling-override]` (v146 / v148 / v152).

---

## Blunt assessment

He did the hard parts right and skipped the cheap ones, and the pattern in which he did so is completely legible.

Twenty-six SQL functions, twenty-six pinned search paths — no exceptions, across four months. Eight admin endpoints, eight authorisation checks. Eleven user-facing endpoints, eleven scoped on a verified JWT and not one on a request parameter. Stripe's signature verified on the raw body with the parser explicitly disabled; Alipay's verified with the seller id, the app id, the trade state and the amount re-checked against the stored order in the RPC as well as in JavaScript. A unique `notify_id` so a replayed callback cannot pay twice. A payment kill-switch that defaults closed, and a test asserting that it defaults closed. Twenty-seven tests that name, one by one, every way a payment system gets defrauded. Three hundred and one lockfile entries, every one with an integrity hash, every one from npmjs.org. Zero secrets in the history. Nothing ever deleted. A thirty-two-line test that enumerates the API directory dynamically so it can never drift — the exact defect two of the last three subjects shipped.

And nothing runs the tests. There is no linter for ten thousand lines of JavaScript. The advisory lock he learned to need in July guards the ¥9.90 button and not the credit ledger from May that debits a user per image. The badge says 532 and the data says 529, and the three missing numbers are images that were committed on day one for cases nobody ever wrote. The tagline is "Prompt as Code" and the parameter syntax it invented is documented nowhere and read by nothing. The one thing his build actually validates — five invariants, a cross-document reference check, an assertion that fails the build if the AI's favourite Chinese tic appears — guards an artifact that has not changed a byte in a hundred and eight days, while the five hundred and twenty-nine cases it summarises grew by a hundred and thirty-one.

None of that is carelessness. Every check that exists is a check something else already demanded: Vercel wanted a build, so the validators run; Supabase's advisor sent a warning list, so a whole migration exists to clear it; npm's default registry produced a clean lockfile; publishing to npm required a licence file, so there is one. Every check that is missing is one he would have had to choose: install a linter, add a CI job, give the five hundred and twenty-nine cases a schema so that a validator would have something to hold on to.

That is the finding, and it is about us. The vault has `(C) proposed-verify-vault-inventory.sh` sitting in a project folder, seventeen ships old, still called *proposed*. It is our `npm test`. It will stay unrun for exactly as long as running it requires someone to remember. **Which of your checks runs because you chose it, and which runs because something you needed anyway happened to drag it along?**
