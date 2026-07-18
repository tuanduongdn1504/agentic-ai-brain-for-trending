# Theo's independent hands-on evidence (N=3)

> A full day of *real* work — migrations, UI overhauls, a security audit, 3D game-gen — not a leaderboard reaction (N=1) or a single-bench vendor livestream (N=2). Most items are **single-practitioner anecdote or first-party demo** (verdict: OPINION), so they're catalogued as *lived evidence*, not independently-verified fact. Their value is **texture the benchmarks can't show**.

## What K3 built for Theo

- **ping.gg port — 3+ hours, 122 tasks off a ~1.5-paragraph prompt [12:30–13:25].** A real migration of his Zoom-for-creators app that stayed coherent for 122 tasks before hitting a context limit. Theo: *"I've never seen an open weight model come close to staying coherent for even half of this length."* Long-horizon agentic coherence is his headline positive.
- **T3 Chat UI work [26:11–29:20].** Five marketing-page redesigns (pills, Bento-box, a "cringe terminal" one that looked like the Claude design skill had been baked in), then a harder real task — a **dark sidebar redesign that he says came out "better than what we had."** His verdict: for marketing pages, *slightly better than OpenAI models, slightly behind Claude*; for the real UI task, good enough to ship from.
- **macOS-27 liquid-glass web-app recreation [29:20–29:48]** (community example) — "looks and works this well… for not too expensive is kind of crazy," with the honest caveat "a lot of little things are broken in it."
- **3D game-gen — "Fish Slap 3D" [16:12–18:02].** The demo that genuinely surprised him: K3 iterated code ↔ live screenshots, generated rider/horse/fish/submarine 3D models with sound effects. Theo: *"the best fish model I've seen any lab create… if this model can actually do 3D, that's going to change things."* Frontier labs (OpenAI/Anthropic) aren't chasing 3D/game-dev — a capability *axis* K3 explores that they don't.
- **Security audit on his "Lakebed" product [32:58–33:26].** K3 spun up discovery agents, ran a **verification pass with ~25 agents**, synthesized, hit a context limit, compacted, continued, and delivered usable hardening feedback — *a task Fable/Soul often refuse* (see [[theo-security-safety-and-open-weight-risk]]).

## The genuinely novel observation — sub-agent orchestration [36:39–37:07]

The one hands-on finding with no corpus precedent and no obvious analogue in other models, per Theo:

> When told to use a workflow, most models make **one** workflow to break down a big task. K3 made **a workflow per phase**, started running them, and — the surprising part — **let its sub-agents check off to-do items one level up** in the parent to-do list. Theo: *"Never seen that before. Even Fable doesn't do that inside of Claude Code."*

Catalogued as an **OPINION/observation** (single practitioner, one session, not reproduced) — but a concrete, falsifiable claim about K3's agentic *style*, worth a note for anyone studying multi-agent orchestration patterns. Cross-link: [[../multi-agent-orchestration/_index]].

## The honest rough edges Theo volunteers

A skeptic's credibility comes from the negatives, and Theo lists them:

- **UX gap (Moonshot's own words):** *"a noticeable gap in user experience compared with Fable 5 and 5.6 Soul."* Too proactive; **responds to the sub-agent/completion ping instead of to the user** [35:42–36:11] — Theo had to notice "oh, it's not going anymore" and follow up.
- **Under-RLHF'd on user expectations** [25:16] — because most Kimi usage is on *third-party providers*, Moonshot gets little telemetry to tune the niceties. (The completeness critic flagged this as a plausible *inference*, not an established fact.)
- **Visible-reasoning inefficiency** [34:47–35:42] — because the thinking is open, Theo watched it **waste reasoning on whether it should use `any`… inside a *markdown* file** (a plan, not code). Combined with ~20 TPS, "it feels slow."
- **Context-window surprise** — the subscription tiers don't grant the full 1M window, which is what cut off the ping.gg run mid-flight. See [[theo-cost-speed-and-how-to-use]].

## How to read this evidence

- **It's texture, not proof.** Nearly every item is Theo's own session or a Moonshot demo — OPINION-class. Do **not** cite "best fish model ever" or "122 tasks" as verified capability; cite them as *what an experienced skeptic observed in one day*.
- **The pattern is consistent with the benchmarks:** strongest where visual/frontend/3D and long-horizon coherence live; rough where day-to-day UX polish and speed live — exactly the **specialist, not generalist** shape ([[theo-benchmarks-and-the-hallucination-reconciliation]]).

## Key Takeaways

- **Long-horizon coherence (122-task migration) + 3D/game-dev + frontend** are Theo's standout positives — and they're the axes where K3 genuinely leads, not the general-purpose ones.
- **The novel finding:** K3's sub-agents check off parent to-do items — an orchestration pattern Theo says he's never seen. Falsifiable, single-session, worth watching.
- **A credible skeptic's negatives** (UX gap, ping-not-user responses, reasoning waste, ~20 TPS, subscription context caps) match the corpus's "operationally incomplete" read.
- Everything here is **lived evidence (OPINION), not independently verified** — its job is texture, not fact.
