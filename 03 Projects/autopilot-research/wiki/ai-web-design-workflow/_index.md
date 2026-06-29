# Topic: ai-web-design-workflow

> **"Vibe-designing" with a coding agent** — scaffold a landing page with an LLM coding agent, fix its taste with a portable **design-discipline skill**, redesign section images with an AI image model, animate a hero with an AI video model, and let the agent swap the assets in. Built from one creator video + a double deep-dive of its four originals.
> **Compiled:** 2026-06-20 (path 5 yt-dlp full transcript + direct primary-source fetch + adversarial workflow verification `wf_8b23bf2d-231`, 14 agents).
> **Source video:** Lukas Margerie — "Redesigning Websites with GPT-5.5 & Images 2.0" ([PFO01z7Qe38](https://www.youtube.com/watch?v=PFO01z7Qe38), 2026-04-24, 7:18, ~31K views). **Third-party creator, NOT first-party OpenAI/Anthropic.**

---

## The premise

The video is a 7-minute live build: open **OpenAI Codex** running **GPT-5.5**, paste a landing-page prompt, install the **Taste Skill** to redesign the result, generate replacement section images with **ChatGPT Images 2.0**, animate a hero image with **Seedance 2.0**, and swap everything back in — finishing with a polished site in one sitting. It's a worked example of the 2026 **"vibe-designing"** movement (build it / design it / market it in natural language).

**The load-bearing takeaway is not the OpenAI stack — it's the Taste Skill.** It's the only piece that is open, fetchable, and *portable*: an MIT-licensed design-discipline skill that runs in **Claude Code** just as well as Codex. Everything else (which coding agent, which image model, which video model) is swappable. See [[ai-web-design-workflow/overview]].

## The four originals → what they are

1. **Taste Skill** ([leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill)) — the centerpiece. A 47K-star MIT skill that turns "generate something that looks OK" into "pass a 62-point mechanical anti-slop gate." **Portable to Claude Code.** → [[ai-web-design-workflow/taste-skill-deep-dive]]
2. **GPT-5.5 + Codex** — the coding agent doing the build. Real (released 2026-04-23). The video's "Codex beats Claude at front-end" is a single-prompt opinion — **contradicted** by the evidence (Opus 4.7 rates *more* polished on multi-prompt UI tests). → [[ai-web-design-workflow/original-gpt-5-5-codex]]
3. **ChatGPT Images 2.0** — image model used to restyle section images from page context + a reference. Real (rolled out 2026-04-21). → [[ai-web-design-workflow/original-chatgpt-images-2-0]]
4. **Seedance 2.0** — ByteDance's image→video model (on Higgsfield), animates a static hero image. Real (the transcript's "C dance" = phonetic mishearing of "Seedance"). → [[ai-web-design-workflow/original-seedance-2-0]]

## Articles

- [[ai-web-design-workflow/overview]] — what vibe-designing is, the 5-step loop, why the Taste Skill is the real prize, the Claude-native translation
- [[ai-web-design-workflow/taste-skill-deep-dive]] — **the centerpiece:** the 3 dials, the 62-point pre-flight gate, the em-dash ban + every mechanical rule (verbatim), the 13 skill variants, format + portability to Claude Code, maintenance risk
- [[ai-web-design-workflow/the-redesign-workflow]] — the vendor-neutral end-to-end recipe (brief→Design-Read→scaffold→taste-gate→image-restyle→hero-animate→asset-swap→annotate-to-edit) + the Claude-Code/Anthropic translation of each step
- [[ai-web-design-workflow/original-gpt-5-5-codex]] — GPT-5.5 facts (modes, pricing, context), the Codex relationship, and the Claude-vs-Codex front-end claim (evidence-checked)
- [[ai-web-design-workflow/original-chatgpt-images-2-0]] — Images 2.0 capabilities, the restyle-from-reference workflow, pricing, what's flagged
- [[ai-web-design-workflow/original-seedance-2-0]] — Seedance 2.0 facts (architecture, durations, audio-by-default, pricing, hosts) + the meta-correction (the synthesis brief wrongly called it fabricated)
- [[ai-web-design-workflow/video-to-original-crosswalk]] — every video claim → canonical original → verdict; what the video gets right / omits / overstates
- [[ai-web-design-workflow/source-provenance]] — verification ledger: confirmed / corrected / flagged, incl. the Seedance meta-correction

## Pilot

Ranked methods to apply this to the operator's flows: `output/(C) 2026-06-20-ai-web-design-pilot-methods.md` (**24 methods** across hireui-frontend-Goal-#2 / autopilot-deliverables / Claude-Code-skills / personal / Scrum-coaching, + a skip list + a critic's reframe). **Headline:** port the Taste Skill into Claude Code and run hireui's TalentAxis frontend through its 62-point redesign gate — the cheapest, most Claude-native, highest-leverage win.

## Cross-links

- [[codex/_index]] — the GPT-5.5/Codex-as-harness topic (Codex-as-adversarial-reviewer; Claude-vs-Codex framing)
- [[claude-skills/_index]] — the SKILL.md format the Taste Skill uses; **Anthropic ships its own `frontend-design` skill** (the first-party analog)
- [[claude-cowork/_index]] · [[claude-skills/_index]] — skills-as-portable-capability lineage
- [[harness-engineering/_index]] — "the skill *is* the harness" (a design rubric injected as a skill = harness engineering for design)
- [[prompt-evaluation/_index]] — eval the redesign quality before trusting "it looks better"
- [[claude-api-cost-optimization/_index]] — the 87KB skill = ~26K tokens; progressive-disclosure / cost discipline
- [[ai-operating-system/_index]] — skills-as-SOPs framing

## Source provenance (headline)

Primary-source-grounded + adversarially verified (14 agents). **All four originals are real.** Corrected from the raw drafts: Taste Skill pre-flight count **62 (not 73)** + **14 design systems (not 15)**; GPT-5.5 modes are `low/medium/high/xhigh/none` (**not** "extra high intelligence"); GPT-5.5 context **400K verified (1M unverified)**; the **"Codex beats Claude at front-end"** claim is reversed by evidence; an **Images 2.0 QR-code capability** flagged as a likely fabrication and dropped; and a **meta-correction** — the workflow's own synthesis brief wrongly declared **Seedance "fabricated/skip,"** but its high-confidence research agent confirmed Seedance 2.0 is a real ByteDance model. **Unverifiable:** "Anton Guilds" (the prompt's author — likely a conflation). Full log: [[ai-web-design-workflow/source-provenance]].
