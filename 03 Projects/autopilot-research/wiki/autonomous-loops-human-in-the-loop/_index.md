# Autonomous Loops with Human-in-the-Loop

> **Topic:** Goal-driven agentic loops (observe-think-act) with human checkpoints for high-stakes actions
> **First compiled:** 2026-05-14 (autopilot overnight drain 2026-05-13)
> **Source bundle:** `../../raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md` (6 YouTube videos via NotebookLM)
> **NotebookLM ID:** `abe1647e-c9c3-4ad1-8e63-5e93fac50865`
> **Maintained by:** Claude Code librarian per `../../CLAUDE.md`

> ⚠️ **Signal quality:** The auto-selection had to relax the recency filter; sources skewed toward generic "What is Agentic AI" / IBM / CNN explainer videos rather than dialed-in Karpathy-autoresearch / Ralph-loop / human-checkpoint content. **A re-run with a tighter query (`Karpathy autoresearch Ralph loop human checkpoint goal driven Claude Code`) is recommended before treating this topic as authoritative.** See [[gaps-and-followups]].

---

## What this is

Six videos that collectively describe the **observe → think → act** loop (sometimes called perceive → decide → execute → learn) that distinguishes "agentic" from "generative" AI, plus a thin slice of human-in-the-loop guidance (drafts-not-sends, scoped permissions, alignment concerns). The bundle is **strong on agentic-loop architecture and context-engineering tactics**, **weak on the specific HITL checkpoint patterns** the topic was supposed to surface — see [[gaps-and-followups]] for the recommended re-run.

---

## Articles in this topic

| Article | What it covers |
|---|---|
| [[overview]] | What a goal-driven autonomous loop is, the observe-think-act / perceive-decide-execute-learn variants, where humans plug in |
| [[core-patterns]] | Five recurring techniques: agentic-loop architecture, context-engineering via markdown, MCP tooling, skills-as-SOPs, task decomposition + verification |
| [[expert-disagreements]] | Generative-vs-agentic framing, autonomy-vs-control trade-off, "agent vs workflow" boundary fight, cloud-vs-file memory |
| [[practical-takeaways]] | 7 actionable rules (kept honest — bundle is thin on HITL specifics) |
| [[gaps-and-followups]] | ⚠️ Re-run query recommended — explains why and lists what was missed (Karpathy autoresearch, Ralph loop, paperclip governance, plan-mode + grill cycles) |

---

## Source citations (within this topic)

| Source # | Channel | Title | URL |
|---|---|---|---|
| 1 | Collaboration Simplified | NEW Copilot Workflows Agent Will Automate Your Job (Full Tutorial) | https://www.youtube.com/watch?v=_w-jVw8Uhc0 |
| 2 | The Coding Sloth | I Have Spent 500+ Hours Programming With AI. This Is what I learned | https://www.youtube.com/watch?v=91B_v-wOaws |
| 3 | Greg Isenberg | Building AI Agents that actually work (Full Course) — guest Remy Gasil | https://www.youtube.com/watch?v=eA9Zf2-qYYM |
| 4 | IBM Technology | Generative vs Agentic AI: Shaping the Future of AI Collaboration | https://www.youtube.com/watch?v=EDb37y_MhRw |
| 5 | codebasics | What is Agentic AI and How Does it Work? | https://www.youtube.com/watch?v=15_pppse4fY |
| 6 | CNN | AI CEO explains the terrifying new behavior AIs are showing — Jared Rosenblatt, Lori Siegel, David Sacks | https://www.youtube.com/watch?v=GJeFoEw9x0M |

> Source numbers above match the inline `[Source N]` citations within each article. They correspond to the order listed in the raw bundle.

---

## Related topics

- [[../workflow-ai-coding/_index]] — Ralph Wiggum loop article + planning-first patterns (the dialed-in content this bundle largely missed)
- [[../harness-engineering/_index]] — Lopopolo's bounded-autonomy framing, where human checkpoints fit in the harness
- [[../claude-md-12-rules/_index]] — Rule 4 goal-driven execution, Rule 10 checkpoint-after-significant-step
- [[../claudekit/_index]] — workflow primitives that operationalise loops
- [[../claude-code-hooks/_index]] — deterministic checkpoints (pre-tool-use blocks) as a HITL substitute
- [[../10x-claude-code/_index]] — productivity patterns referenced when loops actually work

---

## Provenance note

The Greg Isenberg interview (Source 3) and The Coding Sloth video (Source 2) are the two sources that actually engage with loop architecture and HITL mechanics in any depth. Sources 1, 4, 5 are vendor/explainer content; Source 6 is journalism focused on the safety/alignment angle. Weight citations accordingly.
