# Video-to-Original Crosswalk: "Redesigning Websites with GPT-5.5 & Images 2.0"

## Source

**Video:** Lukas Margerie, "Redesigning Websites with GPT-5.5 & Images 2.0" (YouTube [PFO01z7Qe38](https://www.youtube.com/watch?v=PFO01z7Qe38), 2026-04-24, 7:18, ~31K views). Third-party creator.

**Transcript:** `raw/2026-06-20-ai-web-design-gpt55-taste-skill.md`

**Primary sources relied on:** github.com/leonxlnx/taste-skill (+ raw SKILL.md files), developer.openai.com API docs, higgsfield.ai/seedance/2.0, fal.ai/seedance-2.0, wavespeed.ai, anthropic.com/news/claude-design-anthropic-labs, plus WebSearch corroboration.

---

## Video claim → original → verdict

| Timestamp | Video claim | Canonical original | Verdict | Notes |
|---|---|---|---|---|
| 0:00–0:33 | Pietro Schirano (founder of Magic Path) built a "time machine" (prompt a moment → panoramic view), 100% in Codex w/ GPT-5.5 + new image model | [Magic Path](https://magicpath.ai) / Pietro Schirano (X @skirano) | PERSON VERIFIED / DEMO UNVERIFIED | Schirano real (CEO Magic Path, ex-Anthropic). The specific "time machine" demo not located — plausible, unconfirmed. |
| 0:33–0:55 | Jake Soft Servo built a 7-DOF robot arm "100% generated in Codex" with GPT-5.5; "would have taken weeks stitching tools" | X [@soft_servo](https://x.com/soft_servo) post 2026-04-23 | T2-CONFIRMED | Exact post + verbatim quote located. |
| 1:03–1:19 | The workflow: GPT-5.5 builds a landing page, ChatGPT Images 2.0 makes images, "C dance" animates them | [Images 2.0](../ai-web-design-workflow/original-chatgpt-images-2-0.md) + [Seedance 2.0](../ai-web-design-workflow/original-seedance-2-0.md) | CONFIRMED (+correction) | "C dance" = **Seedance** (phonetic). |
| 1:30–1:58 | Prompt by "Anton Guilds," a designer in the creator's community | — | UNVERIFIABLE | No person "Anton Guilds" found; likely conflation (Anton Sten / Anton Repponen) or pseudonym. Prompt not public. |
| 1:58–2:26 | Claude **Opus 4.7** "extra high effort" vs Codex **GPT-5.5** "extra high intelligence," same prompt | [GPT-5.5/Codex](../ai-web-design-workflow/original-gpt-5-5-codex.md) | CORRECTED | No "extra high intelligence" mode — real modes `low/medium/high/xhigh/none`. |
| 2:26–2:50 | "I actually like the Codex design much more" — Codex builds the better landing page | blog.kilo.ai UI test; Altman launch note; SWE-bench | OPINION (contradicted) | Single-prompt opinion. Evidence: **Opus 4.7 rates more polished**; Altman acknowledged GPT-5.5 trailed on front-end at launch. No design benchmark exists. |
| 2:50–3:19 | "There's this skill called the taste skill" — copy a CLI command to install it in Codex | [Taste Skill](../ai-web-design-workflow/taste-skill-deep-dive.md) | T1-CONFIRMED | `npx skills add https://github.com/leonxlnx/taste-skill`; ships `gpt-taste`, `redesign`, etc. |
| 3:19–4:14 | Type "taste" / run redesign → site restyled (better Bento, real image, sticky scroll, fades, hover) "less AI generated" | Taste Skill `redesign-skill` | T1-CONFIRMED | Scan→Diagnose(8 dims)→Fix(7-step). The "less AI generated" goal = the skill's whole anti-slop thesis. |
| 4:34–5:08 | Use the "new image two model from GPT" to redesign a section image from page context + a reference, feed into Codex | ChatGPT Images 2.0 | T2-CONFIRMED | Image-to-image restyle-from-reference. Rolled out ~2026-04-21. |
| 5:08–5:25 | Click **annotate** → "delete this" → element removed in <1 min | Codex annotate | ANECDOTE | Real Codex capability per demo; reproducible in Claude Code via a screenshot/preview loop. |
| 5:25–5:54 | Pinterest for reference images → ChatGPT "replace the background image of the truck… with this" | ChatGPT Images 2.0 | ANECDOTE/PROCESS | Pinterest-as-moodboard is the creator's workflow, not a tool feature. |
| 5:54–6:32 | "Use model C dance 2.0," 8s, 16:9, "slowly animate the sound waves"; "it has sound, I'll ask it to take the sound away" | Seedance 2.0 | T1-CONFIRMED | Seedance generates **native audio by default** — matches the "take the sound away" step exactly. |
| 6:32–7:01 | "Replace the attached video with a background image of the hero section" → animated hero background | Coding agent asset-swap | PROCESS | Final asset-swap; vendor-neutral. |

---

## What the video gets right & teaches well

- **The Taste Skill is the real lever.** The creator correctly identifies that the raw agent output is "a bit AI-generated" and that a *design-discipline skill* — not a better prompt — is what fixes it. The biggest visible quality jump in the video is the `redesign` step.
- **The asset sub-loops are genuinely reproducible:** restyle-a-section-image-from-a-reference, and animate-a-hero-image-then-mute. Both transfer to any image/video model.
- **"Annotate → delete this"** is a real, ergonomic visual control surface for agent-built UIs.
- **It's an honest, scoped demo** — 7 minutes, one site, no overclaiming about production-readiness.

## What the video omits / overstates

- **Overstates Codex's design superiority** — presents a single-prompt preference as if it settles "which builds better landing pages." The evidence favors Claude on front-end. (See [[ai-web-design-workflow/original-gpt-5-5-codex]].)
- **Omits that the Taste Skill is vendor-neutral and runs in Claude Code** — the video frames it as a Codex add-on; it's an MIT SKILL.md that installs anywhere.
- **Omits Anthropic's own design surface** — **Claude Design** (launched 2026-04-17) + the **`frontend-design`** skill are the first-party Claude analogs to the whole stack.
- **No accessibility/perf/eval discipline** beyond what the skill enforces — no mention of testing the redesign, measuring it, or production gaps (PII, CWV in prod, responsive QA).
- **No cost discussion** — image/video generation + a 400K-context coding model running "xhigh" is not free; the 87KB skill is ~26K tokens if mishandled.
- **Mishears "Seedance" as "C dance"** and never names the maker (ByteDance) or that it's on multiple hosts.

## Now-outdated / shifting since 2026-04-24

- **Model landscape moves fast.** GPT-5.5 / Opus generations and their benchmark gaps shift; treat the comparison as a snapshot. (The operator runs **Opus 4.8** today.)
- **Seedance leaderboard Elo** dropped from a March ~1,351 to ~1,195 — leaderboards churn; verify before citing.
- **Taste Skill is actively developed** (round-5 hardening; counts have moved) — pin a commit if you adopt it.

## Verdict summary

| Dimension | Grade | Notes |
|---|---|---|
| Technical accuracy (the workflow) | A− | The 5-step loop is real and reproducible; tools all verified |
| Completeness | B− | Omits vendor-neutrality, Claude-native path, cost, eval/accessibility |
| Currency | B | Model claims are a fast-moving snapshot; Seedance Elo stale |
| Verifiability | A− | Taste Skill fully T1; products confirmed; one QR fabrication caught & dropped |
| The headline opinion ("Codex > Claude for design") | C | Single-prompt opinion; contradicted by multi-prompt evidence |
| Pedagogical value | A | Excellent, honest intro to the vibe-design loop |

**Recommendation:** watch it for the **loop** and the **Taste-Skill pointer**, then ignore the OpenAI-specific framing — run the identical workflow on **Claude Code + the Taste Skill** (+ Claude Design / `frontend-design` skill), which is both cheaper for a Claude shop and the stronger-evidenced front-end path. Pilot file: `output/(C) 2026-06-20-ai-web-design-pilot-methods.md`.

## Cross-links

[[ai-web-design-workflow/_index]] · [[ai-web-design-workflow/taste-skill-deep-dive]] · [[ai-web-design-workflow/source-provenance]] · [[codex/_index]] · [[claude-skills/_index]]
