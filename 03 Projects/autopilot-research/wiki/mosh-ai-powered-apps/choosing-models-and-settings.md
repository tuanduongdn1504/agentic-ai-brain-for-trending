# Choosing Models & Model Settings

## Source

Video PtETUYa3i2Q, chapters "Choosing the Right Model" (25:43) + "Understanding Model Settings" (30:45). Transcript read directly (lines ~605–960).

## The 6-criteria decision framework ("there is no best model")

1. **Intelligence/reasoning** — complex problem-solving needs a reasoning model; summarization/extraction/classification does not.
2. **Speed** — bigger models are slower, especially on long outputs; real-time UX wants fast models.
3. **Modalities** — text in/out is the default; check image/audio/video needs. Example taught: `gpt-image-1` takes text+image in but outputs **images only**.
4. **Cost** — per-token in/out; see [[tokens-and-cost]].
5. **Context window** — long docs, codebases, extended conversations need more; most features don't.
6. **Privacy** — sensitive data (medical records) → self-hosted open-source models (the paid course's Ollama section).

At video time the OpenAI featured models were GPT-4.1, o4-mini, o3 (o3 = strongest reasoning, slowest). Knowledge cutoff is also flagged: older models can be fine "if up-to-date world knowledge doesn't matter."

## Settings (taught in the OpenAI playground)

- **Text format:** `text` | `json_object` | `json_schema`. JSON schema is the "define the exact shape" option — Mosh has the AI generate the schema itself from an example. (= OpenAI Structured Outputs; Claude equivalent is `output_config.format` / `messages.parse()`.)
- **Temperature (OpenAI range 0–2):** low **0.2–0.4** for logical/factual work (summarization, Q&A); high **0.7–1.0** for creative work; **never the extremes** — demo at temperature=2 degenerates into gibberish mid-story. Rule of thumb: 0.7 balanced default.
  - ⚠️ Vendor-specific: Claude's temperature is **0–1**, and the newest Claude models (Fable 5 / Opus 4.8/4.7 / Sonnet 5) **removed sampling params entirely** — steering is done by prompt + adaptive thinking + `effort`. See [[openai-to-claude-mapping]].
- **Max tokens:** caps response length; too low ⇒ mid-sentence truncation. Mitigation taught is prompt-side: "write a complete answer in ≤50 tokens without cutting off mid-sentence" — a first taste of prompt engineering.
- **Top-p (nucleus sampling):** alternative randomness control via probability-mass cutoff (1.0 = full range, 0.3 = only most-likely tokens). **Use temperature OR top_p, not both**; default top_p=1.
- **Store/logs:** ON by default — all prompts logged server-side at OpenAI, browsable in the dashboard (input, output, model, datetime, response ID, params). The response ID shown here is the hook for conversation state later.

## Key Takeaways

- The framework generalizes verbatim to Claude: Haiku 4.5 (fast/cheap) ↔ Sonnet ↔ Opus 4.8 tiers map onto the same 6 criteria; the Models API (`client.models.retrieve`) provides the live capability data the video reads off openai.com/models.
- "Playground before code" is the pedagogy: every parameter is demonstrated visually before appearing in the SDK call — a good pattern for teaching teammates (Scrum-coaching reusable).
- The temperature guideline (0.2–0.4 factual / 0.7–1.0 creative) is corpus-verified against multiple sources, but is **legacy advice on 2026 frontier models** where sampling knobs are gone.
- store:true default = your prompts persist on vendor servers unless disabled — a privacy fact most beginner tutorials skip; feeds criterion #6.
- Cross-links: [[calling-models-responses-api]], [[tokens-and-cost]], [[caveats-and-corrections]] (model lineup drift).
