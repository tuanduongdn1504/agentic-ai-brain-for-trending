# Grading the "16 hours" METR Claim

## The claim

> "If you look at the latest METR evals, our latest models can work for 16 hours at a time, and are now in the zone where we can't even accurately detect how long it's able to work for." — Boris Cherny, launch video [`MhfnicQVkgY`](https://www.youtube.com/watch?v=MhfnicQVkgY) (~02:39)

## What METR actually measures

- METR's **time-horizon** metric ([metr.org methodology](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)): fit a logistic curve of model success probability vs **human-expert completion time** of the task, then read off the task length where the model succeeds **50% of the time**.
- It is a **task-difficulty horizon, not a runtime**: "can work for 16 hours" (continuous autonomous operation) is not what the number says. A model with a 16h horizon completes tasks *that would take a human expert 16 hours* about half the time — and fails the other half.

## The actual numbers (all first-party METR)

| Model | Date | 50%-time-horizon | 95% CI |
|---|---|---|---|
| Claude Opus 4.5 | Dec 2025 | ~4h49m | 1h49m – 20h25m |
| Claude Opus 4.6 | Feb 2026 | ~14.5h | 6h – 98h |
| **Claude Mythos Preview (early)** | **Mar 2026** | **"at least 16 hours"** | **8.5h – 55h** |

- Sources: [METR time-horizons page](https://metr.org/time-horizons/), METR_Evals X posts (2052896621760004602, 2024923422867030027, 2002203627377574113), [METR Claude-Code/Codex measurement note](https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/).
- **Task-suite saturation:** only **5 of 228 tasks** are estimated ≥16h. METR itself: measurements at this range are "unstable and less meaningful," and it does not publish exact estimates above 16h.

## Grading

- **The number is real, the frame is shifted.** "16 hours" matches the Mythos Preview point estimate; "our latest models" is doing marketing work (the 16h figure is the *preview* eval of the model family Fable/Mythos 5, not a floor for anything shipping).
- **"Can't even accurately detect how long"** — a genuinely fair paraphrase of the saturation problem (CI 8.5–55h; the suite runs out of long tasks), but rhetorically inverted: METR frames it as *measurement unreliability*, Boris frames it as *unbounded capability*.
- **The relevant nuance for Tag:** Boris's own follow-up is the honest mechanic — the 16h-class task doesn't run 16h wall-clock; **self-scheduling extends effective horizon** ("Claude can schedule a follow-up after days, or weeks, or months"). The product's long-horizon story is *checkpointed recurrence* (schedule + memory + follow-up), not a 16-hour continuous run.
- Anthropic's own [Fable 5 / Mythos 5 announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5) does **not** cite METR or a 16h figure — the claim exists only in the video's framing.

## Key Takeaways

- Read every "works for N hours" vendor claim as **50%-success task-horizon** unless proven otherwise; the failure half of the distribution is the operationally-relevant half.
- The wide CIs (6–98h for Opus 4.6!) mean **the frontier of this metric is currently noise-dominated** — treat cross-model horizon comparisons above ~8h as directional at best.
- For the operator: this is the same *self-scheduling-extends-horizon* architecture the vault already runs (CronCreate / ScheduledWakeup loops + memory files) — validation of the pattern, not a capability the operator lacks. See [[corpus-positioning]].

Cross-links: [[launch-video-annotated]] · [[architecture-and-execution-model]] · [[external|Storm Bear: harness-engineering]] (long-horizon economics)
