# The quality ceiling and the failure modes that don't announce themselves

> Hardware ([[the-hardware-ladder]]) decides whether local coding is *usable*. This article is about whether it is *trustworthy* — a separate question with a worse answer.

## The headline: the dangerous failures are silent

Every failure in this bundle that would actually hurt you in production is one that **passes its checks**. Slowness is loud and self-correcting. These are not.

## 1. The type-checker-invisible bug — the most important finding in the topic

ForrestKnight, testing on the real **Excalidraw** codebase, asked for a five-pointed star shape. Qwen3 Coder Next generalised diamond and star collision handling into one shared helper — reasonable-sounding — but the helper **always uses star points**. Diamond collision now runs through star geometry.

> *"That is a bug, a bug that **the type checker will not catch** because the code works, it passes all the checks, the star draws, it's on the toolbar, everything on the UI looks perfect. **If you're a vibe coder, job well done.**"*

This is the class of defect that compounds: *"these little bugs that appear that if you're not actually checking the code will compound and not be so pretty after a week or a month."*

The same pattern, milder, on the highlighter task: Opus modelled highlighter as a real property on the element's data model; the local model produced a **visually identical** result that stops being a highlighter once the stroke exists. Same output, worse model, no failing test.

**Implication:** the review burden goes *up*, not down, with a weaker model — and it lands precisely where automated gates can't help. Cross-reference [[../local-ai-coding-agents/_index|local-ai-coding-agents]] and the anti-vibe-coding thread in [[../jsm-practical-vibe-coding/_index|jsm-practical-vibe-coding]].

## 2. The hard ceiling — it gives up

Same source, harder Rust task (command bookmarks in **Warp**). Qwen3 Coder Next touched the right areas — persistence, terminal view, action wiring, left-panel UI, schema — then failed to compile with **47 errors**, tried repeatedly, and quit:

> *"Given the complexity, let me stop here. The bookmarked commands feature is mostly implemented, but has compilation errors that need to be fixed by someone familiar with the Warp code base's UI API."*

Worth recording honestly: **Opus 4.7 also only half-delivered** on that task — it inserted the bookmarked command without executing it, and created a panel type that never integrated. The gap is real but it is a gap between *imperfect* and *unusable*, not between *perfect* and *broken*.

## 3. The silent hang — no error at all

Zen van Riel, with LM Studio's small default context:

> *"It will hang indefinitely because the Claude Code system prompt is thousands of tokens long... and **there's no clear error message indicating this**."*

**Claude Code's system prompt is 4,200 tokens** (Anthropic-documented). A default window smaller than that produces an infinite hang, not a diagnostic. This is the single most likely thing to make a first local-agent attempt fail for reasons the user cannot see.

## 4. The model-identity trap

The local model reported that it was **Sonnet** — because Claude Code's system prompt says so.

> *"They don't always have self-awareness of the model that they actually are. The system prompt that they are fed really dictates their behavior very much."*

Consequences, both real:
- **You cannot verify which model answered by asking it.**
- Claude Code's own **token counter is wrong** — it displayed 45 K / 200 K based on assuming Sonnet 4.6, not the local model's actual configuration.

Compounding this, Anthropic documents that sessions on an unrecognized model ID *"compact at the context window Claude Code assumes for the ID"* — so **auto-compact fires against the wrong number**. `CLAUDE_CODE_MAX_CONTEXT_TOKENS` is the documented override. The anchor hit this warning directly ([[anchor-quanit-64gb]]).

## 5. Hallucinated specifics

Zen van Riel's local model hard-coded a fictional **"NVIDIA RTX 3080"** into a dashboard meant to show real loaded models. His framing is fair — *"this is the same for state-of-the-art models"* — but the fix is instructive: he gave the agent the ability to **call the backend API directly** so it could self-check its output against reality rather than invent it.

## 6. The filesystem-scope risk (local-specific)

The anchor's agent requested **iCloud Drive and Music** access. See [[anchor-quanit-64gb]]. Local inference protects your weights and prompts; it does not confine your agent's filesystem reach. **Local ≠ contained.**

## 7. Output that looks finished and isn't

Tech With Tim, on a 64 GB M5 Max, asked for a chess game **in React**. Got ~600 lines of **plain JavaScript**, and the game **didn't load**. He shipped the tutorial with *"clearly there's some bug."* Wrong framework, non-functional result, presented as a working demo.

## The operating instructions that actually follow

ForrestKnight's are the most concrete, and the rest of the bundle converges on them:

> *"Treat them as if they were models that you're coding with maybe a year or two ago. You have to be very specific. You have to give it more information... and you also really need to **break those tasks into much smaller tasks and give it one by one by one**."*

Plus:
- **Use subagents** ([[why-agentic-differs-from-chat]]) — caps prefill cost *and* context-quality decay.
- **Run it asynchronously.** ForrestKnight: local was **≥5× slower**, so *"you have two tasks running simultaneously. You're working on one, it's working on another."*
- **Give the agent a way to check itself** against real APIs/builds rather than trusting its output.
- **Read the diff.** The failures that survive your test suite are exactly the ones you must catch by eye.

## The honest scope of "good enough"

ForrestKnight's own definition, from the video titled *"Local AI Coding is Finally Good Enough"*:

> *"Good enough when you look at it from a standpoint of being able to help you in your work as a software developer, **not comparing it to a frontier model**."*

And his motivation is **regulatory, not economic** — ITAR-controlled defence code, HIPAA, IP-sensitive work, hedge funds where *"no code or data can leave the building."* He concedes upfront: *"If you can go that route [frontier cloud], do it. Why not?"*

Set against the anchor's bar — **Sonnet parity** — the two verdicts are not actually in conflict. They are answering different questions. See [[claims-scorecard]].

## Key Takeaways

- **The dangerous failures pass their checks.** A collision-geometry bug that compiles, type-checks, and renders correctly is the signature risk.
- **There is a hard ceiling:** 47 compile errors and an explicit give-up on a real architecture-touching Rust task.
- **A too-small context window fails silently and infinitely** — Claude Code's 4,200-token system prompt alone overruns a default window.
- **The model will tell you it's Sonnet, and the token counter will agree.** Neither is true. Auto-compact fires on the wrong number.
- **Local ≠ contained** — filesystem scope is a separate axis from weight privacy.
- **Review burden increases** with a weaker model, exactly where automated gates don't reach.
- **"Good enough" means "helps a developer", not "matches a frontier model"** — and its real driver is compliance, not cost.

## See also
[[the-hardware-ladder]] · [[why-agentic-differs-from-chat]] · [[anchor-quanit-64gb]] · [[the-tooling-layer]] · [[claims-scorecard]] · [[caveats-and-corrections]]
