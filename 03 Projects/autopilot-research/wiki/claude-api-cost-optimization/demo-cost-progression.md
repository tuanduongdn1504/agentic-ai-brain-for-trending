# Demo: HeroCorp cost progression

> The talk's running example: **HeroCorp**, a fictional "superhero outsourcing" company with an OKR dashboard that pulls from web, Slack, Gong, and Jira. CEO (speaker) + CTO "Ben" live-code the optimizations on stage.
> Use this as the **ordered playbook**: apply the four levers in this sequence and watch cost fall while output stays identical.

## The cost arc (as narrated in the demo)

| Stage | What was applied | Cost (per dashboard load) | Signal |
|---|---|---|---|
| Baseline | Opus 4.7, no caching | **~£31** | 0% cache hit |
| + Prompt caching | one-line auto-caching | **cost ~halved** | ~58% cache hit; output byte-identical (caching doesn't touch intelligence) |
| + Context engineering | tool search + programmatic tool calling + compaction (400K threshold) | **~£11** (~⅓ of baseline) | context window grows slower per turn |
| + Advisor strategy | Sonnet 4.6 executor + Opus 4.7 advisor | **further reduced** | intelligence preserved; advisor catches the "watermelon" |

**Takeaway:** the levers compound. Caching alone ~halved it; context engineering took it to ~a third; the advisor strategy pushed cost down further while *restoring* Opus-grade judgment on the calls that mattered.

## The load-bearing discipline: read the transcript

Repeated 3–4× in the talk: **always open the agent/developer transcript and look at what the model actually sees.** Every optimization started from that inspection —
- caching: "what's your cache hit rate right now?" (often 0%);
- tool search: noticing tool defs eating context after a few turns;
- programmatic tool calling: seeing a 30–60 min Gong transcript dumped in when only the sentiment was needed.

You can't optimize context you haven't looked at.

## The framing that matters most

> *"This session isn't about an impressive demo. There are lots of great AI demos. The point is getting it into real production — where you must match context to need so the product succeeds."*

The cost work is in service of shipping a **production** agent (for you and your customers), not a flashy one-off.

## Key Takeaways

- Apply in order: **cache → context-engineer → model-tier (advisor)**. Each multiplies the previous.
- Caching is cost-only (output identical); context engineering and advisor are cost *and* quality.
- The whole method is downstream of one habit: inspect the transcript.

Related: [[prompt-caching]], [[context-engineering]], [[advisor-strategy]], [[_index]].
