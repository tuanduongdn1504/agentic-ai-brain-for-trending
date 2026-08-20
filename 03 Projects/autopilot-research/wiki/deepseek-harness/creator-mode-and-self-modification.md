# Creator mode, and how far the self-modification actually goes

## The four modes

| Mode | What the bundle says |
|---|---|
| **standard** | Full tool set, day-to-day work. Chase AI: *"like what you do if you're inside a Claude Code."* |
| **PTC** | Multi-step tasks. Chase AI: instead of tool calls one by one, *"it would create a script where it runs all the tools essentially in one go… this will reduce some of the context bloat."* Firecrawl: *"great for coding."* |
| **minimal** | Simple/low-complexity tasks. |
| **creator** | Inspect and author plugins from inside the harness. |

**Unresolved:** no source expands the acronym "PTC". The described behaviour — emit one script that batches tool calls instead of round-tripping each one — is the same mechanism as programmatic tool calling, but **no source in the bundle states the expansion, so the vault does not assert it.** Flagged for a follow-up read of DSH's docs.

## What creator mode does

The agent writes a plugin for its own harness, mid-session, and you approve it.

Four demos in the bundle, all cosmetic on purpose: a Matrix falling-character theme (Chase AI), a black-and-orange retheme and an archive-chats plugin (Firecrawl), a flashing rectangle plus a settings panel to configure its colour and size (Cef), a dinosaur jumping game (Better Stack). DeepSeek's own marketing examples are a floating whale and a snake game.

Cef's is the most instructive because he pushes a second step: after the rectangle, *"I'm going to ask it to add a setting to configure the color and size of the rectangle"* — and it works, writing CSS and wiring a settings entry. He then inspects the trajectory and finds the actual mechanism: *"there is a bunch of Cordis related tools. We have a Cordis define, which defines an immutable Cordis package for new plugin use."* **The model has tools whose job is to mint plugins into the running runtime.**

Turing Post gives the non-toy example that makes the feature legible: an agent reviewing a database migration cannot compare two schema versions, so *"the agent can write a temporary plugin for that comparison. You approve it and the new tool joins the running assistant."* Her framing: *"The working environment grew a new capability after the task had already begun."*

And the sentence worth keeping: *"This is the point where a coding agent stops searching only for a solution and begins searching over the composition of the worker that will find the solution."*

## The persistence limits — where the bundle disagrees

This is the bundle's clearest internal divergence, and getting it right matters because it is exactly where hype lives.

- **Turing Post:** *"These packages live only in process memory and disappear when Harness restarts. They cannot promote themselves into permanent plugins and a person still has to start them."*
- **Chase AI:** *"when you create custom plugins, it doesn't save it. It's not permanent. You have to tell it that you want it to be saved… or else you're going to lose it at the end of the session."*
- **Firecrawl:** *"if I do restart the harness, then that plugin disappears. The only way to keep it is to tell the model to add it to the configuration file."* He then shows one that *did* persist, because he asked.

**Resolution: these are compatible, and Turing Post's phrasing is the precise one.** A creator-mode package cannot promote *itself*; a human instruction can cause the model to write it into the config file, at which point it persists. Chase AI and Firecrawl describe the human-initiated path; Turing Post describes the absence of an autonomous one. No contradiction — but a reader taking only Firecrawl's account would over-read the autonomy, and a reader taking only Turing Post's would miss that persistence is available at all.

## The hot-reload claim — where one source is wrong

- **Cef:** *"when you modify a plugin, it gets updated without having to rebuild the application or relaunch it."* — **overstated.**
- **Firecrawl:** *"that is true for dynamic plugins, but for these type of plugins, the presets are frozen at session start, so you'll have to restart."*
- **Chase AI:** *"That is kind of sort of true. It depends on the plugin itself."*
- **VN:** initially states the strong version (*"mọi người cài plugin vào một phát là mọi người không cần phải khởi động lại"*), then contradicts it from his own screen — he is forced to restart repeatedly. Later, honestly: *"Hôm trước mình thử thì là mình không cần khởi động lại nó vẫn chạy. Hôm nãy không hiểu kiểu gì."* (last time it worked without restart; today, no idea.)

**Verdict: hot reload applies to dynamic plugins (creator-minted, toggleable) but not to installed preset plugins, which are frozen at session start.** Chase AI and Firecrawl are correct; Cef's unqualified version is the bundle's most-repeated overstatement. See [[deepseek-harness/claims-scorecard]].

## Where the self-improvement story actually stands

**Chase AI, the anchor, is the most deflationary and the most credible:**
> *"the dream of this, you know, self-improving harness that can create its own plugins and adjust itself to your task sounds awesome in theory, but in reality, I don't know if it's ever going to actually happen. And maybe it will, but not today."*

**Turing Post pre-empts her own hype in the same breath:**
> *"Let me slow down before this begins to sound like self-improving agent fan fiction… So, Harness is not waking up at night or designing itself and returning smarter before you got your coffee."*

Her calibrated version: *"What DeepSeek has built is the beginning of that loop. An agent can propose a change to its own toolbox, and the running system knows how to absorb it."*

**Cef is the most speculative** — *"if we get a smart enough LLM, it will be capable of self-modifying its code, its harness, and evolving it depending on the new requirements"* — and marks it as speculation.

**Nobody in the bundle demonstrates a functional self-improvement loop.** Every demo is a cosmetic UI plugin. The gap between "the runtime can absorb a generated plugin" (demonstrated) and "the agent improves itself" (not demonstrated) is the whole distance between the architecture and the marketing.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/cordis-and-the-paper]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/claims-scorecard]] · [[autonomous-loops-human-in-the-loop/_index]] · [[agent-development-lifecycle/_index]]
