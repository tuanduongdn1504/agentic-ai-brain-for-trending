# The redesign workflow (vendor-neutral recipe)

> The video's end-to-end loop, abstracted away from the OpenAI stack into a reproducible recipe — plus the **Claude-Code / Anthropic translation** of each step. The only non-swappable asset is the [[ai-web-design-workflow/taste-skill-deep-dive|Taste Skill]].

## The loop, abstracted

```
brief ─▶ Design Read ─▶ scaffold ─▶ TASTE GATE (redesign) ─▶ restyle section images ─▶ animate hero ─▶ asset-swap ─▶ annotate-to-edit ─▶ re-gate
         (1 line)       (agent)     (62-pt skill)            (image model)            (video model)   (agent)        (point + speak)
```

## Step by step

| # | Step | What happens | Tool in video | Vendor-neutral / Claude-native |
|---|---|---|---|---|
| 1 | **Brief → Design Read** | Agent states one line: *"Reading this as: \<page kind\> for \<audience\>, \<vibe\>, leaning \<system/aesthetic\>"* before any code | Taste Skill Section 0 | Same — works in any agent |
| 2 | **Scaffold** | Agent builds first-draft page from the prompt | Codex + GPT-5.5 | **Claude Code + Opus 4.8** (evidence favors Claude for front-end) |
| 3 | **Taste gate (redesign)** | Run the `redesign` command: Scan → Diagnose (8 dims) → Fix (font→color→hover→layout→component→states→motion); must pass the **62-point pre-flight** | Taste Skill in Codex | **Same Taste Skill in Claude Code** + Anthropic `frontend-design` skill |
| 4 | **Restyle section images** | "Redesign this section as an image" from page context + a reference (Pinterest mood) → feed image back to agent | ChatGPT Images 2.0 | Any image model (Images 2.0 / Imagen / Flux / Ideogram) |
| 5 | **Animate hero** | "8s, 16:9, slowly animate…" → short clip; **mute it** (audio is on by default) | Seedance 2.0 (Higgsfield) | Any image→video model (Seedance / Veo / Runway / Pika) |
| 6 | **Asset-swap** | Agent replaces `<img>`/adds `<video>` background in code | Codex | Claude Code |
| 7 | **Annotate-to-edit** | Point at an element, say "delete this" → agent removes it | Codex annotate | Claude Code + screenshot loop, or Claude-in-Chrome / a preview tool |
| 8 | **Re-gate** | Re-run the 62-point check; ship only if every box ticks | Taste Skill | Same |

## Why each layer is swappable (and one isn't)

- **Coding agent (step 2/6):** Claude Code and Codex are near-peers. Front-end evidence favors **Claude** ([[ai-web-design-workflow/original-gpt-5-5-codex]]). → swap freely.
- **Image model (step 4):** "restyle from reference + prompt" is a generic capability. → swap freely.
- **Video model (step 5):** "image→short loop" is generic; the gotcha is **muting default audio**. → swap freely.
- **Taste Skill (step 1/3/8):** the *only* piece carrying durable, transferable knowledge — a named catalogue of LLM design tells turned into binary checks. → **adopt this**, stay agnostic on the rest.

## Making the manual gate a real gate (operator upgrade)

The 62-point pre-flight is a **manual** checklist (no shipped linter). To make it enforceable in a real project:
- Wrap a subset as a **deterministic check** — e.g. grep the build output for `—` (em-dash), `font-family:.*Inter` as default, three-equal-column patterns, `window.addEventListener('scroll'` — and fail CI. (Code-grader discipline, cf. [[prompt-evaluation/_index]].)
- Or run the gate as a **[[claude-code-hooks/_index|PostToolUse/Stop hook]]** that re-reads the skill and reports violations.
- Or treat the redesign output as an artifact to **eval** (LLM-as-judge against the 62 items) before merge.

## Key takeaways

- The workflow is a **5-stage asset pipeline** around one **design-discipline gate**; only the gate is worth "adopting," everything else is a tool choice.
- For a Claude shop, **every step runs on Claude Code + the same Taste Skill** — no OpenAI dependency.
- Turn the manual 62-point checklist into a **code-checkable subset + a hook/eval** to get a true quality gate rather than a vibe.

## Cross-links

[[ai-web-design-workflow/taste-skill-deep-dive]] · [[ai-web-design-workflow/overview]] · [[ai-web-design-workflow/original-gpt-5-5-codex]] · [[ai-web-design-workflow/original-chatgpt-images-2-0]] · [[ai-web-design-workflow/original-seedance-2-0]] · [[prompt-evaluation/_index]] · [[claude-code-hooks/_index]] · [[harness-engineering/_index]]
