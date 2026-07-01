# Video summary — Dũng's "Antigravity 2.0: Create Skills & Rules A-Z"

## Source

[UFmV7YsVqlM](https://www.youtube.com/watch?v=UFmV7YsVqlM) — "Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z", **Dũng - Chia Sẻ Công Nghệ** (1,320 subs), 2026-06-27, 22:39, 1,093 views. Vietnamese, beginner audience. Full auto-caption transcript in `raw/2026-07-01-google-antigravity-skills-rules-dung-chiasecongnghe.md`.

> **What this creator is:** a small Vietnamese tech-tutorial channel aimed at **non-programmers / office workers** (n8n, Lark, Obsidian, Stitch, OpenCode/OpenClaw tutorials in the sidebar). The value here is **pedagogical**, not authoritative — for the authoritative mechanism see [[google-antigravity-skills/skills-system]] and [[google-antigravity-skills/rules-and-customization]]. The demo bundles a **sample skill/rule folder** on Google Drive (linked in the description).

---

## The pitch (00:00–03:30)

*"Ever have to stand over a new employee explaining every little step — take this file, paste into that one, fix the font, make the chart — every single day? Using AI today is the same: you write a long prompt every time to re-explain what you need. Exhausting. So why not teach it **once**?"*

The mental model: **clone yourself.** Create a copy that knows your skills and knowledge and works in your place. "That's what making a **skill** is." No programming required.

## Part 1 — What a Skill is (03:30–08:00)

- A skill is *"just a folder in the project"* under a skills path (the audio names a path the auto-caption garbled — the real path is **`.agents/skills/`**, see [[google-antigravity-skills/skills-system]]). Inside: the **skill file** (`SKILL.md`) and a **`scripts/`** folder for executable code (he says Python / PowerShell).
- **Auto-discovery:** *"the magic of Antigravity is that when you give a command, it scans all your skill folders to see which one matches the description, and auto-activates it"* — instead of calling it manually. (Confirmed: this is progressive disclosure.)
- **Workspace vs Global** via the **two-houses analogy**: workspace skill = a vacuum cleaner you bought (only your house's agent uses it); global skill = a shared street lamp (both houses' agents use it).
- **Skill vs Rule:** *"the thing people confuse most."* Skill = capabilities (analyze the Excel, make charts). Rule = a constraint, e.g. *"never delete raw data, only add a new report sheet."* Don't repeat the constraint in every skill — put it in **one Rule** all skills read (3–5 skills, 1 rule). Manage both in **Settings → Customization**.

## Part 2 — Two ways to build (08:00–12:00)

- **Manual:** open the skill folder in your project and write the skill's domain steps (for an Excel-analysis project: analyze the month's data, draw charts…).
- **Fast / no-code (recommended):** work with the agent normally, then tell it *"create a skill including everything I just did with you"* — it generates the skill (and rules) and saves them to the folders. *"The fastest method; anyone can do it."*
- Examples he lists: office reports are just one small kind; you can make skills for **making videos, writing scripts, writing emails** (e.g. different fonts/formatting for foreign vs domestic customers — one command picks the right skill).

## Part 3 — Live Excel demo (12:00–end)

Walkthrough (details in [[google-antigravity-skills/build-methods]]):

1. Two files in a `doanh-so/` (sales) folder — **May** and **June** revenue. He prompts *"analyze May revenue"*; it reads the file (columns: name, product, amount, collected/outstanding, status, province).
2. He notes this first pass looks like any ChatGPT/Gemini analysis — **the difference is he'll save it as a skill** so he never re-asks.
3. A prepared prompt lists the tasks (paid/unpaid list, revenue+AR totals, % buyers by province, top products, agent-vs-individual), then *"report to the director as a formatted file, **and create a skill for this whole process**."*
4. It produces a **plan → skill**, generates the report (overview, revenue/AR, province breakdown — Hà Nội/Thanh Hóa, comparison charts). He **verifies the numbers** ("if the data's wrong, the skill's wrong — teach it until it's right").
5. He opens the generated **`SKILL.md`** — notes Antigravity reads **`.md`** but **not `.doc`** — containing the analysis process, system requirements, read/write Excel, chart, format, install libraries. Tip: **feed your company's real template file** and require that exact output layout.
6. **Adds the Rule:** *"never delete/edit/overwrite raw data"* → shows this rule runs across **all** skills in the sales workspace (not other workspaces); the rule file appears as **`agents.md`**; later relaxable ("ask me before overwriting").
7. **Reuse:** *"analyze June revenue **using the skill**"* → same layout/charts/guarantees, one line.
8. Shows **Settings** listing the Rule (`user global` + `agent`) and the Skill. Closes: *"deployment is fast; you can make hundreds of skills; cloning yourself takes your efficiency toward 100%."*

## Auto-caption garbles (interpreted, not transcribed literally)

| Caption garble | Actual meaning |
|---|---|
| "Asian triệt skill" / "giặt ngang skill" | the skills path — **`.agents/skills/`** (not `.antigravity/skills`) |
| "titon" | Python · "power sell / Power Boy" | PowerShell |
| "ru / RU / CRW / rồi" | **Rule** |
| "agent ch mas down" / "agent.mdown" | **`agents.md`** / `AGENTS.md` |
| "prom / brom / Rom" | prompt · "chác/chát" | chat |
| "Facebook / facew" | the **report file** (garble) · "super skill" | "use the skill" |

## Key Takeaways

- A **clear, well-paced beginner tutorial** whose real value is the **Skill (capability) vs Rule (constraint)** mental model and the **"teach once / clone yourself"** framing.
- The **live Excel demo** is a reusable template for *any* recurring deliverable: do it once → capture as a skill → guard with a rule → one-shot forever.
- **Verify the mechanism claims against official docs** — the creator's spoken **skills path is garbled/wrong** and there's **no official "make a skill" button** (the agent authors the file). See [[google-antigravity-skills/source-provenance]].
- Sample skill/rule files are on the creator's **Google Drive** (description link) for reference.
