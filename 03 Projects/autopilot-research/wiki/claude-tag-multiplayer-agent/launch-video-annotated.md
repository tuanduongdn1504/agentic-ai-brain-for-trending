# The Launch Video, Annotated — "The future of work with @Claude"

## Source

- [`MhfnicQVkgY`](https://www.youtube.com/watch?v=MhfnicQVkgY), official Claude channel, 2026-07-02, 11:26. Boris Cherny (Head of Claude Code) + Cat Wu (Head of Product, Claude Code). Full EN transcript in [`raw/2026-07-06-claude-tag-future-of-work.md`](../../raw/2026-07-06-claude-tag-future-of-work.md).
- Format: launch-marketing conversation, not a technical talk — every claim below is annotated against first-party docs and independent checks. Confidence labels follow the verify pass in [[caveats-and-corrections]].

## The narrative arc (as told)

1. **Three-generation evolution story:** typeahead ("the agent was… just writing the line") → Claude Code ("whole functions, whole files, whole features") → Claude Tag ("it just does the whole thing… an entire experiment end-to-end").
2. **Human-role shift:** "a person always in the loop, typing a line at a time" → "one person with like 10 Claudes" → "Claude is actually driving… an entire team interacting with it." This is the same *human-steers-agents-execute* progression as [[external|Storm Bear: harness-engineering]] — but told by the vendor as product marketing rather than as an operator discipline.
3. **Product definition (Boris):** "In the past, you had to open Claude and ask… With Claude Tag, Claude jumps in, it's proactive, it knows when to jump in. It'll do the work, even if it takes days or weeks, and it'll follow up… it'll remember what I told it for next time."
4. **The three pillars** the interview keeps returning to: **proactivity** (jump-in judgment, "EQ"), **multiplayer** (whole team steers one session; "everyone gets to see it"), **memory** (per-channel standing instructions from all users).

## Claim-by-claim annotation

| # | Video claim (speaker) | What checks out | Annotation |
|---|---|---|---|
| 1 | "Latest METR evals: our latest models can work for 16 hours at a time… we can't even accurately detect how long" (Boris) | METR's 50%-time-horizon for Claude Mythos Preview = "at least 16 hours" (95% CI 8.5–55h) | **PARTIAL / marketing compression.** 16h is a *task-length-at-50%-success-rate* estimate, not continuous runtime; the "can't detect" phrasing has a real basis (task-suite saturation: only 5/228 tasks ≥16h) but overstates precision. Full grading: [[metr-16-hour-claim]] |
| 2 | "Claude can schedule a follow-up after days, or weeks, or months" (Boris) | Docs: scheduled operations / standing instructions; Boris's own month-long session anecdote is self-reported | Feature real per docs; the month-long-experiment anecdote is unverifiable dogfood testimony |
| 3 | "Memory in the model… remember all the instructions that all the users have given it over time" (Boris) | Docs: per-channel memory, admin-viewable/editable/deletable | Real, with important scoping the video omits: **channel-isolated**, private-channel memory doesn't propagate; DM memory runs on the sender's personal account. See [[memory-model]] |
| 4 | "Claude is trained to have a good sense for when it's needed, and it can take the back seat" (Cat) | First-party marketing claim; no eval published | Unverifiable as stated; the tunability ("jump in less/more" remembered) matches the docs' standing-instructions mechanic |
| 5 | "The number of PRs written by Tag… like 65% now" (Cat) — description restates as "65% of the product team's code" | Anthropic's announcement uses the "code" wording; Cat's X post uses "merges 65% of product PRs" | **Self-reported, three non-equivalent wordings** (PRs written / PRs merged / code created), no denominator or window published. Full forensics: [[the-65-percent-claim]] |
| 6 | "Running in the same remote sandbox that we use for mobile and for the desktop app, and it's using the same agent SDK. So it's just as intelligent" (Boris) | Docs confirm Anthropic-hosted ephemeral sandboxes; press confirms Opus 4.8 | Sandbox + Agent SDK reuse consistent with docs; "just as intelligent" = same-model claim (Opus 4.8), fair |
| 7 | "We launched Claude Tag in Slack, and we're excited to bring it to more platforms… like Microsoft Teams" (Cat) | Announcement says expansion "more widely"; Teams named only in the video | **Teams is a video-only roadmap mention** — not found in the written announcement or docs at ingest date |
| 8 | Chat/Cowork/Claude Code framed as "reactive… you have to remember to open it" vs Tag's proactive higher-level objectives | Matches [[external|Storm Bear: claude-cowork]] app-must-be-open constraint (first-party confirmed there) | Internally consistent positioning: Tag is the first Anthropic surface where *the agent owns the trigger*. See [[corpus-positioning]] |
| 9 | "Make sure your collaboration platform has public channels" (Cat) — observation-driven best-practice diffusion | Sociological claim, dogfood-only | Notable as an org-design prescription: public-by-default channels become an AI-adoption mechanism, not just a transparency norm |
| 10 | Onboarding self-serve: "instead of asking Legal… or HR… they can just tag Claude Tag" connected to "source-of-truth files" (Cat) | Docs: connectors + org files | The compliance-sensitive example (Legal/HR) is notable given the docs' own ambient-monitoring caveats — see [[security-and-governance]] |

## What the video does NOT say (found only in docs/press)

- **Tier gating** (Enterprise + Team ≥10 seats), **launch credits** ($25K/$2.5K, expire 2026-09-01), **org-funded billing** for channel work vs personal billing for DMs.
- **Mandatory migration**: legacy Claude-in-Slack app auto-switches 2026-08-03, **no true rollback** (Legacy-pinned channels simply stop responding).
- **Opus 4.8 exclusivity** (press), ephemeral per-thread sandboxes discarded on idle, agent-centric service-account identity, default-deny egress.
- Any security discussion at all — prompt-injection surface of ambient mode, permission elevation, audit fragmentation (see [[security-and-governance]]).

## Key Takeaways

- The video is a **positioning artifact**: proactive + multiplayer + memory is the pitch; every operational constraint (tiers, credits, migration, model, sandbox lifecycle, admin controls) lives outside it.
- Its strongest verifiable spine — long-horizon models + self-scheduling + per-channel memory — is real per first-party docs, but the two headline numbers (16h, 65%) are both **compressed retellings** of messier underlying facts.
- The "team interacting with one agent" frame is the genuinely new part vs everything else in this corpus: single-operator harnesses ([[external|Storm Bear: harness-engineering]]), single-user desktop agents ([[external|Storm Bear: claude-cowork]]), and self-built chat bridges ([[external|Storm Bear: telegram-remote-control-stack]]) all assume one human steering.
