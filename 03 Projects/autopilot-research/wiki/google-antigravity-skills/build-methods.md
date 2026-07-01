# Building a skill — the two methods + the Excel worked example

## Source

The [[google-antigravity-skills/video-summary|video]]'s two-method walkthrough and live Excel demo, reconciled with the official creation flow in [[google-antigravity-skills/skills-system]].

---

## Method 1 — Manual (author the files yourself)

Go into the project and create the skill by hand:

1. `mkdir .agents/skills/excel-sales-report/`
2. Write `SKILL.md` — a `description` that names *what it does and when to use it*, then Markdown instructions capturing the domain steps (e.g. *"given a monthly sales `.xlsx`: segment paid/unpaid customers, aggregate revenue + accounts-receivable, chart by province, classify agent vs individual, output a director-ready report"*).
3. (Optional) add `scripts/` (Python/Bash/Node), `resources/` (your company's report template), `assets/`.

The creator's tip is worth stealing: **give it your company's real template file** and instruct it to *"always output in exactly this layout"* — headings as H1/H2, a fixed font, etc. Providing a sample artifact beats describing the format in prose.

## Method 2 — Harvest from a working session (the "just talk to it" method)

The video's recommended, no-code path:

1. Work with the agent **normally** on a real task — feed it the May sales file, ask it to segment customers, compute AR, chart by province, produce the report. Iterate until the output is right.
2. Then tell it: **"create a skill from everything we just did."** The agent **writes the `SKILL.md`** (and can scaffold `scripts/`) capturing that workflow.
3. From then on, new inputs ("analyze June revenue **using the skill**") follow the captured procedure automatically.

> **Nuance (don't over-claim):** there is **no official `/create-skill` command or documented auto-extraction feature**. Method 2 works because **the agent can author files when asked** — it writes the `SKILL.md` for you. It's an emergent use of the agent, not a product button. Verify the generated file before relying on it (the demo itself notes the first pass can contain data errors you must check). See [[google-antigravity-skills/source-provenance]].

**Why Method 2 is the point:** it turns *a session you already ran* into *reusable, portable knowledge* — the "clone yourself" move. This is the same discipline as capturing a repeated Claude Code workflow into a `.claude/skills/…/SKILL.md` (see [[../claude-skills/_index]], [[../claude-code-skills-stack/_index]]).

## The worked example (Excel sales report)

The demo's end-to-end flow, as a template you can mirror for any recurring deliverable:

1. **Input:** two files in a `doanh-so/` (sales) folder — May and June revenue `.xlsx`. Columns: name, product, amount, collected/outstanding, payment status, province.
2. **Do it once, verbally:** *"Analyze May revenue — list paid vs unpaid customers, total revenue + AR, % of buyers by province, top products by sales, classify agent vs individual, then report to the director as a formatted file."*
3. **Capture:** *"…and create a skill for this whole process."* → agent generates the `excel-sales-report` skill (a `SKILL.md` with the analysis + formatting steps).
4. **Add the guard rule:** *"When doing these analyses, **never delete, edit, or overwrite the raw data** — only create a new report."* → this becomes a **Rule** (`AGENTS.md`), not another skill, so **every** report skill obeys it. (Later relaxable: *"if you ever need to overwrite, ask me first and wait for my OK."*) See [[google-antigravity-skills/rules-and-customization]].
5. **Verify:** open the generated report; the creator sanity-checks the province/AR figures — *"if the numbers are wrong, the skill is wrong; teach it until the data is right, then the skill is locked in."*
6. **Reuse (one-shot):** *"Analyze June revenue using the skill."* → same layout, same charts, same guarantees, one line of prompt.

The payoff the creator sells: instead of a long, slightly-different prompt every month (which yields a different-looking report each time), you get a **deterministic, repeatable** deliverable — and you can build **hundreds** of such skills to "clone" your whole role.

## Key Takeaways

- **Two build paths: (1) author `SKILL.md` by hand; (2) run the task once, then ask the agent to "make a skill from what we did."** Method 2 is the low-friction favorite.
- Method 2 has **no official one-click feature** — it works because the agent writes the file; **always verify the generated skill**.
- **Feed a real template file** rather than describing formatting in prose — the strongest tip in the demo.
- Put the **capability** in a Skill and the **constraint** ("never overwrite raw data") in a **Rule** so every skill inherits it.
- The pattern generalizes far beyond Excel: emails, decks, scripts, video, research — anything recurring becomes a captured, reusable skill.
