# how-we-claude-code

> **Topic index.** How Anthropic engineers actually use Claude Code: a *discipline* (not a feature list) tuned to the reality that **agents now run longer and burn more tokens, so a vague spec is expensive**. Front-load verification into the spec, and make verification **native to the artifact** so the agent can drive it.
>
> **Entry point:** VN dub "Hướng Dẫn Build App Có Verification Agent-Native" ([ATsbgIRA0Fw](https://www.youtube.com/watch?v=ATsbgIRA0Fw), BizMate AI) — a faithful localization of the **authoritative original**: Anthropic's **"How we Claude Code"** workshop ([IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE), 2026-05-23, 31:43), presented by **Arno** (Applied AI team). Full transcript read.
>
> **Originals (deep-dived):** **Thariq Shihipar's** blog *"The Unreasonable Effectiveness of HTML"* (claude.com) + [ThariqS/html-effectiveness](https://github.com/ThariqS/html-effectiveness) (20 files / 9 categories) · the **[anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops)** `how-we-claude-code/` repo (3 phases; phase-3 = a real Vite+React verification engine) · Richard Sutton's *Bitter Lesson*.
>
> **Verification:** Workflow `wf_109aca29-27c` (16 agents: 6 deep-dive extractors + 9 adversarial verifiers + synthesis) + operator `gh api`/`yt-dlp` ground-checks. **4 verifiers misfired against the local filesystem and were overridden by primary-source extracts** — logged in [[how-we-claude-code/source-provenance]]. Constitutional rule #4 honored.

---

## Articles

- [[how-we-claude-code/overview]] — the workshop, the three pillars, the 3-phase repo map, and Arno's closing rig (Auto Mode + `/effort x-high` + `/fast` + Opus 4.7→**4.8**).
- [[how-we-claude-code/pillar-1-interview-and-bitter-lesson]] — **Pillar 1:** stop saying "make it better"; use **Ask User Question** so Claude interviews you. The *Bitter Lesson* framing (and where it over-reaches).
- [[how-we-claude-code/pillar-2-html-specs-over-markdown]] — **Pillar 2:** Markdown >100–200 lines goes unread → **HTML specs**. 4 parallel design directions, screenshot feedback, export buttons, `design_system.html`.
- [[how-we-claude-code/pillar-3-agent-native-verification]] — **Pillar 3 (architecture):** components publish state to the DOM via `data-verify-*`; VerifiableUnit (fixtures/invariants/schema) + 4 verifiers + PASS/FAIL/BLOCKED/SKIP verdicts.
- [[how-we-claude-code/verification-framework-deep-dive]] — **the centerpiece double-deep-dive:** file-by-file mechanism (`contract.ts`, `runner.ts`, `window.__verify`, the 3 surfaces, `matrix.test.ts`, `EXPECTED_FAIL` + probe fixtures, `record.ts`).
- [[how-we-claude-code/the-originals-thariq-and-repos]] — Thariq Shihipar, the two repos (`html-effectiveness` + `cwc-workshops`), and Sutton — who originated what.
- [[how-we-claude-code/claude-code-primitives]] — Auto/Fast/`/effort`/`/goal`/AskUserQuestion/Playwright MCP verified vs. docs; the Opus 4.7→4.8 version drift.
- [[how-we-claude-code/caveats-and-when-not-to-use-html]] — **the critic layer:** when Markdown wins (RAG / agent-to-agent / version control = *this vault*), the 2–4× token cost, ephemerality, accessibility, HTML-as-untrusted-input security, and the Bitter-Lesson over-reach.
- [[how-we-claude-code/source-provenance]] — the verified-vs-corrected ledger (name spelling, Todo-not-bill-splitting, no-S3, unverified virality, the verifier-misfire override).

## Pilot methods (how to apply this to your flow)

A ranked menu + a critic's reframe lives in **`output/(C) 2026-06-29-how-we-claude-code-pilot-methods.md`**. Four angles: **hireui Goal #2** (interview-first specs, HTML mockups, and an **agent-native verification harness** on real components — the strongest "actual pilot deployment" evidence yet), the **autopilot/Storm Bear vaults** (keep Markdown for memory; HTML only for ephemeral artifacts), **personal Claude Code** (Auto/Fast/effort discipline + screenshot loops), and **Scrum coaching** (eval/verify-first Definition of Done).

## Cross-topic links

- [[../ai-web-design-workflow/_index]] — HTML/design generation + the Taste anti-slop gate (pillar 2 pairs directly)
- [[../prompt-evaluation/_index]] — verification-first discipline; rubric grading for specs/LLM features
- [[../claude-code-skills-stack/_index]] — package the interview/HTML/verify patterns as composable skills
- [[../workflow-ai-coding/_index]] — "grill-me" planning, spec-first workflow, harness discipline
- [[../multi-agent-orchestration/_index]] — adversarial subagent review (sibling to phase-3's agent-driven verify)
- [[../claude-api-cost-optimization/_index]] — the token-cost trade-off behind "HTML isn't less efficient"
- [[../ai-engineering/_index]] — Chip Huyen's demo→production playbook; verification = the eval discipline at the UI surface
- [[../claude-code-hooks/_index]] — wire the verify/review steps as `settings.json` hooks

## Key Takeaways

- **Three pillars:** interview-driven specs (Ask User Question) → **HTML specs** for rich human verification → **agent-native verification** baked into the artifact.
- The unifying move is **"agent-first"**: rearrange familiar primitives (Storybook fixtures, Zod, DOM attrs, Playwright) so an **agent** is the primary driver, across **one engine / three surfaces** (human dashboard · browser agent · headless CI).
- **`data-verify-*` DOM contract** decouples verification from React internals → survives refactors; **probe fixtures + `EXPECTED_FAIL`** make it trustworthy (it must be able to fail).
- **HTML is conditional, not absolute** — keep Markdown for RAG/memory/agent-to-agent (i.e. this vault); HTML for ephemeral, visual, single-session specs and reviews.
- Use **Opus 4.8** (not the talk's 4.7) + **Fast Mode** for a present-day pilot.
