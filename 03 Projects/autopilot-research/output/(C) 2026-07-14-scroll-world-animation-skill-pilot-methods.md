# (C) Pilot methods — scroll-world-animation-skill

> Source topic: [[scroll-world-animation-skill/_index]]. Ranked methods for applying this topic's findings to the operator's actual flows (hireui Goal-#2, the autopilot vault itself, personal harness, Scrum-coaching). A-tier = cheap/near-term, B-tier = moderate effort/needs eval, C-tier = watch-not-build, D-tier = governance/ADR.

---

## A-tier — cheap, near-term

**A1 — Steal the budget-tier + spend-approval-gate UX pattern.** Scroll World's fork shows a clean pattern for any future metered/paid-generation feature: name explicit cost tiers (Lean/Standard/Showcase), show a generation-count + time estimate, and require explicit approval before spending. If hireui ever ships a metered AI feature (e.g. bulk CV re-parsing, generated outreach content), copy this shape rather than a bare "Generate" button with hidden cost. Zero cost to note now; apply whenever the first metered feature is scoped.

**A2 — Steal the crawlable-static-copy-block SEO pattern.** The fork's `data-sw-seo` block (real headings/text present in the DOM, hidden after mount, so crawlers see content a human sees as animation) is a reusable technique for any client-heavy-rendered marketing page. Relevant if hireui's own public-facing marketing pages (not the app itself) ever go more visually dynamic.

**A3 — A single sandboxed Scroll World spike, marketing-site only.** If curious, run the skill once against a throwaway/sanitized brief for a hireui *marketing* landing page (never the real recruitment app, never real candidate data) to get firsthand cost/quality data. Tag with an explicit budget cap before starting (per [[scroll-world-animation-skill/original-higgsfield-platform]], the "~800 credits" figure for six scenes is unverified — assume real cost until proven otherwise).

## B-tier — moderate effort, needs eval

**B1 — Only evaluate a full animated marketing site if/when a marketing site is actually prioritized.** This is explicitly **not** a Goal-#2 item — hireui's Goal-#2 is shipping the recruitment SaaS itself, not its marketing site. Don't let this topic's visual appeal pull effort off the Candidate-Detail refactor or the first LLM feature (Match-Explain).

**B2 — Reuse the Higgsfield-MCP-onboarding writeup as a reference pattern.** If the operator ever documents an MCP integration for the vault or hireui, [[scroll-world-animation-skill/original-higgsfield-platform]]'s corrected Settings→Connectors flow (vs. the invented slash-command a workflow agent fabricated) is a small, concrete example of "verify the docs before writing the how-to."

## C-tier — watch, not build

**C1 — Watch GPT-5.6 Sol vs Claude Fable 5, but don't switch anything yet.** Both models are real and both were less than two weeks past a major availability event (GA / restored-after-outage) at the time of this video — see [[scroll-world-animation-skill/original-gpt-5-6-and-fable-5]]. Neither is a reason to change hireui's planned model stack for Match-Explain (currently Haiku-4.5-class structured outputs per [[miai-cv-matching-agent/_index]] pilot notes) on the strength of one creator's subjective, single-run "the transitions look sleeker" opinion.

**C2 — Watch Higgsfield as a vendor, low priority.** A recruitment SaaS has little organic need for AI-generated scrollytelling video; if a future marketing refresh wants generated visual assets, Higgsfield is now a known, verified option (MCP + CLI + credits) rather than an unknown.

## D-tier — governance / ADR

**D1 — ADR: scrollytelling marketing sites are out of scope for the current sprint.** A one-line addition to whatever tracks hireui scope decisions: "AI-generated animated marketing pages (Scroll World-style) are explicitly deferred; core recruitment product ships first." Cheap insurance against scope creep from an objectively fun demo.

**D2 — Carry forward a general model-risk principle: don't hard-pin production dependencies to models <2 weeks past a GA or outage event.** This topic is now the second corpus case (after the Fable-5-pricing-window garble-guard in [[jasonlee-claude-mobile-app/_index]]) where a bleeding-edge Anthropic/OpenAI model release had real, undisclosed turbulence in the two weeks before a creator's demo. Worth a durable note in the vault's own model-selection practice, not just this topic's caveats.

## Skip list

- **Skip:** maintaining a fork of Scroll World — no product need for hireui.
- **Skip:** any paid Higgsfield credits beyond a single bounded spike (A3).
- **Skip:** treating "Fable 5 beat GPT-5.6 Sol on scene transitions" as evidence for anything about structured-output/reasoning quality — it's a visual-motion opinion from one uncontrolled run, orthogonal to what hireui's actual LLM feature needs.

## Critic's reframe

The most operationally useful thing in this topic isn't the animation technique — it's the verification trail itself. Two workflow agents died outright, three separate confabulations were caught and excluded (a wrong creator-name attribution, an invented CLI command, a conflated "government-restricted preview" story), and one claim that *sounded* just as confabulated (Fable 5's real 19-day export-control outage) was checked rather than discarded and turned out to be true. That combination — catching fabrications in both directions in the same topic — is the actual export for the vault's own practice, more than the web-design trick the video sells.
