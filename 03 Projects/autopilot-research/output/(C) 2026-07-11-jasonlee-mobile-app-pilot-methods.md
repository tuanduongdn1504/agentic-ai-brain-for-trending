# (C) Pilot Methods — jasonlee-claude-mobile-app → Your Working Flow

> **Source topic:** [[jasonlee-claude-mobile-app/_index]] (compiled 2026-07-11; scorecard 1 CONFIRMED / 4 INCOMPLETE / 1 OVERSIMPLIFIED / 6 MISLEADING / 0 fabricated)
> **Operator context:** hireui (TalentAxis recruitment SaaS, frontend repo, zero LLM integration yet, Goal #2 target), Mosh A2 vendor-seam + Mì AI Match-Explain first-LLM-feature thread, api-security A1-BOLA-first pilot thread, Scrum-coach role.
> **Framing:** the video's *toolchain* verified real; its *business math* is theater. So the pilots extract the workflow and the security corrections — and quarantine the revenue method behind error bars.

---

## ⭐ Headline recommendation

**A1 — CV-parsing spike using the receipt-scanner pattern.** It is the exact convergence point of three existing corpus threads: this video's *photo→structured-row via vision* pattern, Mì AI's *CV↔job matching* domain, and Mosh's *A2 vendor seam*. One evening of work produces hireui's first real LLM artifact (parsed-CV JSON with an eval set) without touching production. Then ship the two zero-cost wins (A4 screenshot-fix-loop, A5 key-placement ADR) the same week.

---

## Track A — hireui direct (the recruitment-SaaS mapping)

**A1. CV-parsing spike = the receipt pattern, transposed.** ⭐
Receipt photo → `{vendor,total,tax,category}` becomes CV PDF/image → `{name,roles[],skills[],education[],languages[]}`.
- Haiku 4.5 (`claude-haiku-4-5`, $1/$5 per MTok) + vision/document blocks + **structured outputs via `client.messages.parse()`** (never prose-parse — the exact trap Mì AI's serving path fell into).
- Behind the **Mosh A2 vendor seam** on an `agent-*` branch per hireui CONSTITUTION I-2; server-side only (A5).
- Ship WITH an eval set from day one: 10–20 real anonymized CVs + recruiter-labeled ground truth; measure field-level accuracy. Cost at Haiku: ~$0.003–0.01/CV — the same "rounding error" economics verified twice now (receipts here, ~$0.00134/CV in Mì AI).
- Effort: ~1 evening for the spike + 1 session for the eval harness. → [[jasonlee-claude-mobile-app/receipt-scanning-with-claude-vision]]

**A2. Confidence-gated model ladder (cost-tier per document, not per agent).**
Add a `confidence` field to the extraction schema; low-confidence or messy CVs (scans, handwriting, unusual layouts) escalate Haiku → Sonnet 5. This is the *defensible* version of the video's cost-tiering intent — measured with `usage` fields, not asserted. Pairs with the video's real lesson: tiering is configuration + telemetry, never a chat request.

**A3. Claude Design with design-system import — for NON-locked screens only.**
Claude Design (post-2026-06-17) imports design systems from a GitHub repo and round-trips with Claude Code via `/design-sync`. Pilot: import hireui's design tokens, generate mockups for a screen *without* operator-locked decisions (Candidate-Detail's 3-tabs/72px-avatar/timeline-colors are locked per the refactor-spike memory — Figma stays source-of-truth there). Use it where Figma coverage is thin (empty states, error states, the future Match-Explain panel). Gate output through the ai-web-design-workflow Taste checks. → [[jasonlee-claude-mobile-app/claude-design-handoff]]

**A4. Screenshot-annotate-fix loop as the standard frontend bug-report format.** (zero cost, adopt today)
The video's cleanest demonstrated pattern: screenshot → annotate what's wrong → paste + one-line prompt. Make it the norm for hireui frontend fixes and for junior bug reports (D1). Vision-grounded reports beat prose for UI defects.

**A5. Key-placement ADR: "LLM keys never touch the client."** (zero cost, one page)
hireui is a *frontend* repo storing JWT in localStorage (api-security recon) — the temptation to call Anthropic from the browser will arise. Write the ADR now: all LLM calls go through a backend route/function holding the key; `EXPO_PUBLIC_`/`NEXT_PUBLIC_` never carry secrets; per-user auth + rate limit on the proxy. This is the same decision the video leaves dangerously ambiguous. → [[jasonlee-claude-mobile-app/api-key-handling-in-mobile-apps]]

**A6. RLS-shaped reinforcement of the BOLA audit.**
The video's missing-RLS hole is the database-policy twin of hireui's #1 risk (Recruiter A reading Company B's candidate — api-security pilot A1). No new pilot; add one line to that audit's checklist: *"if any Supabase/Postgres surface exists backend-side, verify RLS policies per exposed table with two-account tests."* → [[jasonlee-claude-mobile-app/supabase-mcp-and-rls]]

## Track B — Goal-#2 builder track (your own app/side product)

**B1. One-evening pipeline reproduction (evaluate the pipeline, not the product).**
Run the full verified loop once on a throwaway idea: plan-first prompt ("Give me the full plan. Do not build first.") + competitor-URL crawl → Claude Code writes the Claude Design prompt → reference image → export-zip → build → Expo Go on your phone. Deliverable: a `04 Reviews/`-style writeup scoring each step (what held, what broke, tokens/time spent). This is the cheapest way to own an informed opinion on the "vibe-code an app" genre before any bigger bet.

**B2. Niche-mining with error bars.**
The research method is usable if you make the uncertainty explicit: App Store category mining + an estimate tool (Appfigures publishes 5–25% MAPE; observed errors reach 55% *in both directions*) → treat any figure as a range, demand a second signal (ratings velocity, funding, hiring) before believing a niche. Never build on a YouTuber's screenshot. → [[jasonlee-claude-mobile-app/the-80k-title-and-revenue-claims]]

**B3. The "boring B2B, one painful problem" screening rubric.**
The video's three filters (boring niche / one problem done well / B2B data-stickiness) are a decent first-pass idea screen — B2B SaaS retention benchmarks (~88–90%) support the class. Add the missing fourth filter: *distribution story* (cloning gets a product, not customers).

**B4. Ship-gap pre-commitment gate.**
Before committing to ANY app idea, price the full table from [[jasonlee-claude-mobile-app/expo-go-to-app-store-gap]]: auth, RLS, payments/IAP, store review (incl. 4.3 clone risk), integration assessments (QuickBooks-class OAuth reviews = weeks-to-months), privacy labels, ops. If the idea's margin doesn't survive the table, it dies before line one — the exact discipline the genre's titles are engineered to bypass.

## Track C — process/tooling ports into the existing stack

**C1. Per-subagent model tiering, done as configuration.**
In the vault loops and hireui BMAD agents: put `model:` in agent frontmatter (reviewer=opus, builders=sonnet, mechanical/drain agents=haiku), then **verify routing with telemetry** (ccusage/OTEL thread) — the two verified bugs (#44385 closed, #47488 open: Cowork silently routing everything to Haiku) prove silent misrouting happens in both directions. Rule of thumb from this pass: *asking nicely in chat is not configuration; configuration is files + params, and belief requires telemetry.* → [[jasonlee-claude-mobile-app/multiagent-cost-tiering-reality]]

**C2. Prompt-for-a-prompt as a standard cross-tool handoff.**
"You have the context — write the prompt I should give tool X" (the video: Claude Code → Claude Design). Port to your stack: Claude Code writes NotebookLM queries, yt-search queries, Telegram-loop task briefs. The context-holder writes better briefs than the operator retyping from memory.

**C3. Supabase-MCP posture rules (file for when/if adopted).**
If any project adopts Supabase MCP: `read_only=true` default, `project_ref` scoping, **dev/test data only** (vendor's own "never connect to production"), returned rows = untrusted input. One paragraph in the project CLAUDE.md, written before first use.

**C4. Fable-5 economics rule for the stack.**
The video's model economics are right and now verified: Fable 5 = usage credits ($10/$50) post-2026-07-12 — reserve it for verify/judge-class work where correctness dominates cost; Opus 4.8 + Sonnet 5 + Haiku 4.5 cover build loops. Revisit when Anthropic returns Fable 5 to subscriptions "as capacity allows."

## Track D — Scrum-coaching angles

**D1. "Spot the six misleading claims" media-literacy dojo.**
Give juniors the video + 30 minutes, then reveal the scorecard from [[jasonlee-claude-mobile-app/caveats-and-corrections]]. Teaches: estimate-vs-fact, title-vs-content, demo-vs-product, and that *real tools can carry fake math*. Pairs with system-thinking's 3-golden-questions as onboarding material (D1/D2 of that thread).

**D2. Demo ≠ Done, with a concrete artifact.**
The ship-gap table is a ready-made Definition-of-Done workshop: "the video's demo 'works' — list what's missing before you'd charge money for it." Maps one-to-one onto sprint conversations where a feature "works on my machine."

**D3. Estimate discipline transfer.**
The revenue-estimate lesson (±25–55%, both directions, source never named) is the same epistemics as story-point/velocity abuse: an estimate quoted without its error bar and source is a rhetorical device, not a plan. Usable as a retro prompt.

## Skip-list (deliberate non-actions)

- **Don't build the receipt app.** Saturated niche, 4.3 clone risk, and your Goal-#2 domain (recruitment) already has a better-fitting first feature.
- **Don't buy Arcads now.** Real product, honest price advantage ($11/video vs ~$198 human UGC) — but hireui has nothing to advertise yet; file for the distribution phase.
- **Don't adopt chat-prompted "multi-agent workflows" as a cost measure.** C1 is the correct form.
- **Don't cite the video's revenue numbers anywhere.** Unattributed estimates; SimplyWise's $60K/mo is uncorroborated.
- **Don't treat Lottie's license as settled** until lottiefiles.com/page/license unblocks (403 at ship time); quotes match the known Simple License text but were single-source.

## Suggested first 7 days

1. **Day 1 (zero-cost):** A5 ADR + A4 adopted as team norm + A6 line added to the BOLA audit checklist.
2. **Day 2–3:** A1 CV-parsing spike behind the A2-seam on an `agent-*` branch; 10-CV eval set.
3. **Day 4:** A2 confidence-ladder + cost/accuracy readout (usage fields).
4. **Weekend:** B1 one-evening pipeline reproduction → short review writeup (also feeds D1/D2 material).
5. **Anytime:** D1 dojo scheduled for the next junior session.

## Watch-list
- Fable 5 returning to subscription plans ("as capacity allows") — re-run C4 economics when it does.
- anthropics/claude-code#47488 (Cowork Haiku-routing, open) and #44385 resolution — gates on trusting frontmatter tiering.
- Whether Track Rabbit ever ships (prediction: no) — would upgrade/downgrade the source-provenance read.
- Lottie license page unblocking; Arcads×Omni Flash confirmation.
