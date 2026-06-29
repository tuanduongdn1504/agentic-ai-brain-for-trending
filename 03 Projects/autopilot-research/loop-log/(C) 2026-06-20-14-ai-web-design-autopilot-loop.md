# (C) Autopilot Loop — 2026-06-20-14 (ai-web-design-workflow)

> **Trigger:** manual (operator-submitted single video + "double deep-dive into the original resource + pilot methods")
> **Topic:** ai-web-design-workflow (GPT-5.5/Codex + Taste Skill + Images 2.0 + Seedance 2.0)
> **Source:** YouTube PFO01z7Qe38 — Lukas Margerie, "Redesigning Websites with GPT-5.5 & Images 2.0" (2026-04-24, 7:18, ~31K views; third-party creator)
> **Mode:** path 5 yt-dlp full transcript + direct primary-source fetch + adversarial Workflow verification (NOT NotebookLM)

## [2026-06-20] ingest+compile | ai-web-design-workflow

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + 4 originals (Taste Skill ×2 angles) | 1 (new topic) | 0 | 1.0 (cold-start; topic fully built) |

## Sources ingested

- `raw/2026-06-20-ai-web-design-gpt55-taste-skill.md` — deduped 216-cue transcript + verbatim description (resource links)
- Originals fetched live (not via NotebookLM):
  - **Taste Skill** — github.com/leonxlnx/taste-skill (GitHub API + raw SKILL.md for taste-skill/redesign-skill/gpt-tasteskill/minimalist/brutalist/imagegen-frontend-web + plugin.json + CHANGELOG) — researched **twice independently** for verbatim-rubric fidelity
  - **GPT-5.5 / Codex** — developer.openai.com API docs + WebSearch (announcement page 403'd)
  - **ChatGPT Images 2.0** — WebFetch + WebSearch (MacRumors/TechCrunch/BuildFastWithAI)
  - **Seedance 2.0** — higgsfield.ai/seedance/2.0 + fal.ai + wavespeed.ai + multi-source
  - **Context** — Pietro Schirano/Magic Path, Jake @soft_servo, Lukas Margerie/Builderz Gym, Claude Design (anthropic.com/news)

## Workflow

- `wf_8b23bf2d-231` — 14 agents, 653,768 subagent tokens, 213 tool uses, ~17 min.
- Structure: pipeline(5 originals → research→skeptic-verify, Taste Skill ×2 angles) → synthesis brief → completeness critic.

## Wiki articles created

- `wiki/ai-web-design-workflow/_index.md` (NEW)
- `wiki/ai-web-design-workflow/overview.md` (NEW)
- `wiki/ai-web-design-workflow/taste-skill-deep-dive.md` (NEW — centerpiece)
- `wiki/ai-web-design-workflow/original-gpt-5-5-codex.md` (NEW)
- `wiki/ai-web-design-workflow/original-chatgpt-images-2-0.md` (NEW)
- `wiki/ai-web-design-workflow/original-seedance-2-0.md` (NEW)
- `wiki/ai-web-design-workflow/the-redesign-workflow.md` (NEW)
- `wiki/ai-web-design-workflow/video-to-original-crosswalk.md` (NEW)
- `wiki/ai-web-design-workflow/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added ai-web-design-workflow topic)
- `raw/_inventory.md` (UPDATED — row flipped raw→compiled)
- `output/(C) 2026-06-20-ai-web-design-pilot-methods.md` (NEW — 24 ranked methods)

## Final metric

- `gaps_closed_ratio` = 1.0 (cold-start new topic; index + overview + 4 original deep-dives + workflow recipe + crosswalk + provenance all written)
- Stop reason: topic complete; single-source single-cycle by design (operator-submitted video).

## Verification highlights (Rule 12 fail-loud)

- **62-not-73** pre-flight checkboxes; **14-not-15** design systems (Taste Skill counts corrected).
- **GPT-5.5 modes** = `low/medium/high/xhigh/none` (no "extra high intelligence"); **400K context** verified (1M unverified).
- **"Codex beats Claude at front-end" REVERSED** — multi-prompt UI test (blog.kilo.ai) favors Opus 4.7; Altman acknowledged GPT-5.5 trailed on front-end at launch; no design benchmark exists. (Good news for a Claude-centric operator.)
- **Images 2.0 QR-code capability** = likely fabrication, **dropped**.
- **🔴 Meta-correction:** the workflow's own synthesis brief declared **Seedance "not a real product — skip it."** Its high-confidence `seedance-2.0` research agent **refuted** that (T1, ByteDance model on Higgsfield/fal.ai/WaveSpeed). Per Rule 7 + Rule 4 the wiki records **Seedance as real** and flags the brief's over-correction. (A synthesis layer can over-correct — always check the underlying agent.)
- **Unverifiable:** "Anton Guilds" (the landing-page prompt's author — likely a conflation with Anton Sten/Repponen).

## Top unclosed gaps (carry-forward)

1. Taste Skill's other ~10 variants (image-to-code, brandkit, soft, stitch) read only at directory-listing level, not full SKILL.md.
2. Images 2.0 programmatic API model id + GPT-5.5 token-efficiency claim — both want a real-workload pilot (= pilot method B5) to ground.
3. The 62-point gate has no automated linter — operator method A4 (grep + hook) would close this.

## Suggested next action

Operator pilot (per `output/(C) 2026-06-20-ai-web-design-pilot-methods.md`): **A1** today — `npx skills add https://github.com/leonxlnx/taste-skill` in Claude Code on a throwaway page, run `/redesign`. Then **B1 + B2** on a hireui `agent-*` branch (operator installs the skill — I-8): run TalentAxis frontend through the redesign gate + bank the 62-point pre-flight as hireui's design-QA gate. **Storm Bear Pattern-Library note:** this is a **portable-skill-as-design-discipline** + a **cross-vendor-skill** (OpenAI-demoed, Claude-Code-native) data point — candidate evidence for the skills-as-portable-capability / cross-vendor-bridge patterns at the next mini-audit; the "AI-tells = mechanical checks" thesis composes with the Humanizer/signs-of-AI-writing thread in claude-skills.
