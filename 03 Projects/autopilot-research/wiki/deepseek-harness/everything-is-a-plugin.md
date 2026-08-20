# "Everything is a plugin" — architecture and contribution policy

## What the slogan actually covers

The bundle's five independent enumerations of what-is-a-plugin agree almost perfectly:

| Component | Cef | Better Stack | Turing Post | VN | Chase AI |
|---|---|---|---|---|---|
| Model adapter | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tool registry / tool calls | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Agent loop** | ✓ | ✓ | ✓ | ✓ | ✓ |
| Web UI | ✓ | ✓ | ✓ | ✓ | ✓ |
| Session log / storage | — | ✓ | ✓ | ✓ | — |
| Sandbox policy | — | — | ✓ | — | — |
| TUI | — | ✓ | — | ✓ | — |
| Memory | — | — | — | ✓ | — |
| Skills | — | ✓ | ✓ | ✓ | ✓ |
| API gateway | — | ✓ | — | — | — |
| Scheduling | — | — | ✓ | — | — |

Cef's summary: *"the UI in itself is made out of plugins and the model is a plugin and the tool calls are plugins and the agent loop that orchestrates everything is a plugin."*

Better Stack draws the sharp consequence: *"you can just turn the most core pieces of functionality off and completely [lobotomize] the application."* That is the honest flip side of total configurability.

## The claim that separates DSH from Claude Code

**This is the one architectural claim the whole bundle makes, and it is the one worth taking seriously.**

Chase AI states it most precisely: *"the DeepSeek harness allows us to actually edit and change the harness itself in ways you just can't do with these other harnesses… Claude Code, you can sort of approximate a lot of these changes… with things like skills and hooks, but you aren't changing the actual plumbing under the hood. You can do that here."*

He gives a concrete instance: the plugin configuration exposes the **agent loop** itself — *"this is literally like a core part of the plumbing of the DeepSeek harness that you can begin to edit just in terms of parallel tool calls."*

The VN source reaches the same conclusion independently: Claude Code and peers have plugins, *"nhưng mà cái plugin của nó nó rất là hạn chế… Ví dụ cái giao diện cũng không phải là plugin mà nó fix cứng"* (their plugins are very limited — e.g. the UI isn't a plugin, it's hardcoded).

Cef enumerates what that unlocks: *"The agent loop is a plugin so we can do things before calling a tool or after calling a tool. We can add some role-based access control. We can add some monitoring, some tracing. We can modify the loop logic."*

**Corpus note:** Claude Code has since shipped configurable tool-loading (`defer_loading`) — recorded in the vault at v238 — but the vault's own v238 finding is about *tool schema* conditioning, not agent-loop replacement. These are different depths. The DSH claim stands as stated at the loop level.

## The dissent: is this solving a real problem?

**Firecrawl is the only source that attacks the premise, and it is the sharpest moment in the bundle:**

> *"the biggest problem of all is that… the whole plugin architecture is solving a problem I'd say never existed. I've used a many harnesses in the past and the issue has never been the way plugins are loaded and unloaded. I actually don't mind restarting my harness whenever I install a new plugin."*

Chase AI arrives at a softer version of the same doubt: *"is it worth it to do something like that? Is it really moving the needle so much to have this custom harness for your problem? And is it also worth the time and energy to get to that place?"*

**Both dissents are about the hot-reload half of the value proposition, not the everything-is-a-plugin half.** That distinction matters: reversible-removal-at-runtime is what the paper proves and what Firecrawl calls unnecessary; deep-configurability is what Chase AI calls the real sell. They are separable, and the bundle never separates them cleanly.

## The half nobody in the bundle mentions

**"Everything is a plugin" is also a contribution policy, and no video says so.**

The vault's v242 source-level read found the mechanism in `CONTRIBUTING.md` (23 lines): DSH *"cannot accept external pull requests at the moment"* → instead, create a plugin and **associate your GitHub project with the `dsh-plugin` topic**. 1,008 PR merges, all internal; `github.com/deepseek-harness` is a real org with **zero public repos**.

So the exploding plugin ecosystem every video celebrates is, mechanically, **the only channel through which outside contribution is permitted.** The architecture and the governance are the same decision.

The VN source gets closest to noticing — he documents the `dsh-plugin` topic as the discovery mechanism (*"ở trong GitHub này nó có một cái tag gọi là… DSH plugin"*) — but frames it as community enthusiasm rather than as policy. That is exactly the gap between reading a repo and watching a video about it.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/cordis-and-the-paper]] · [[deepseek-harness/ecosystem-and-the-catalogue-gap]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[claude-code-plugins-stack/_index]] · [[claude-code-skills-stack/_index]] · [[open-design/_index]]
