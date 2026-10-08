# Pre-registered claim set — v82 anchor hm8NzEd5io0
# Source: HUMAN-AUTHORED caption track (verbatim-safe). Timestamps from that track.

## A. Deployment / architecture
A1 [01:26] Mihir: Watchtower "spun that up in Managed Agents in 2 weeks"; now "one of our most used features"
A2 [19:34] INTERVIEWER+Mihir: per-account agents are NOT on CMA — "They have a memory architecture that you own that's completely independent." Only Watchtower is on CMA.  <-- PRE-REGISTERED: any source saying otherwise is wrong
A3 [22:19] Todd: "under 2 weeks" to a working solution on CMA
A4 [15:03] Sahaj: first version "in a day"; "100 to 1,000X scale-up in the user base over the course of a few weeks"

## B. Outcomes
B1 [03:41] INTERVIEWER frames it: "supplying a rubric to the agent and allowing the agent to iterate until the rubric is satisfied"
B2 [05:56] Sahaj: "we actually use an independent context window, independent verifier agent, and that's baked into outcomes"
B3 [05:04] Sahaj: briefs run "24 hours before the conversation"
B4 [06:22] Sahaj: they use it to SUPPRESS output when uncertain, not to iterate to perfection

## C. Memory
C1 [07:40] Mihir: concepts stored in "org-wide memory"; improves results "for everyone else"
C2 [09:27] INTERVIEWER introduces the word "dreaming"; Mihir does NOT repeat or confirm it, answers about memory layers  <-- framing attributed to host, not founder
C3 [09:54] Mihir: two-by-two — memory per-account AND cross-account; per-user AND per-org
C4 [18:16] Mihir: per-account memory "can get corrupted over time"; they index it themselves "to make it efficiently queryable"
C5 [18:43] Mihir: the less-core memory is where "managed memory just unblocks a lot of that"

## D. Sandboxing
D1 [10:45] Todd: snapshots customer SOURCE CODE; "you can potentially get secrets"
D2 [11:37] Todd: overnight batch systems + cron + interactive sessions, all on CMA
D3 [22:44] Todd: PR-triggered CMA session; "lightweight UX review"; opens its OWN PRs for instrumentation
D4 [11:11] Todd: "we'd spend some time rolling our own, but you're just covering every single edge case... it's not core to our value prop"

## E. Cost (the criticism layer — the reason this is not a launch video)
E1 [29:23] Mihir: "the markup of Managed Agents is pretty low in terms of the amount of CPU overhead"
E2 [29:23] Mihir: "you can't run batch mode that easily today with it" -> "we could probably save 50%-75% on cost"
E3 [32:10] Mihir: "it's all or nothing in some sense"; "There aren't that many levers for cost"
E4 [32:10] INTERVIEWER: "We have things like effort, we have multi-agent, we have obviously many models"
E5 [32:40] Mihir: wants to "pre-warm sandboxes... to reduce cold start latency" — implies unavailable
E6 [17:19] INTERVIEWER: "things like prompt caching are just solved"
E7 [31:41] Mihir: fan-out across 500 accounts cannot use frontier intelligence; "we'll use much cheaper models"
E8 [33:06] Mihir: CMA fits when "you need frontier intelligence, you're relatively price insensitive, and the task is hard, so it runs for minutes"

## F. Models / evals
F1 [28:03] Sahaj: "The whole five series of models tends to produce writing in a way that has actually a lot more AI telltale signs than previous series of models. More em dashes."
F2 [26:45] Mihir: no good way found to eval a live stateful memory system
F3 [27:11] Sahaj: same for MCP tool calls to third-party services with mutating state
F4 [16:54] INTERVIEWER: "in the very early days, Claude Code didn't have evals"
F5 [24:31] Sahaj: "Phase zero is vibes-based" then hill-climb; warns about overfitting to internal dogfood
