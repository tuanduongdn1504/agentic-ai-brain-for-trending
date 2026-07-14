# Progressive disclosure — a real parallel to Agent Skills, not the same spec

## The claim

Cole, on-screen, in his own words (verified against the full transcript, not inferred by a verifier): *"just like with skills in Claude code, Codex, GitHub Copilot, you have the ability to give a brief description of the capability... it's only going to load the full instructions for the capability when it decides it actually needs it."* He demos this live: an Orbit support agent loads its "knowledge base" capability for a product question but only pulls in the "escalation" capability when a refund complaint appears — the unused capability's full instructions never enter context.

**Verdict: CORRECT_BUT_INCOMPLETE.** The mechanism and the vendor comparison are both real, but they're two independently-designed systems that rhyme, not one shared standard.

## What's confirmed

- Pydantic AI capabilities support exactly this two-stage load: a brief description sits in the agent's catalog at all times; full instructions load only via `defer_loading=True` when the model decides it needs that capability (`pydantic.dev/docs/ai/core-concepts/capabilities/`).
- The Pydantic AI docs **themselves draw the same comparison Cole makes** — an unprompted, first-party confirmation: *"If you've used Anthropic's Agent Skills, this is the same idea generalised: a skill is a markdown file the model can pull in on demand."*
- Anthropic's own Agent Skills spec documents the identical three-stage loading model (discovery → activation → execution) at [agentskills.io](https://agentskills.io) — already established in this wiki as the **same open spec** GitHub's Agent Skills and Claude's Agent Skills both implement (see [[../github-copilot-cli-agents/agent-skills-shared-standard]]).

## What's missing from the comparison

Despite Pydantic's own docs invoking Agent Skills, Pydantic AI's capability does **not** implement the `agentskills.io` spec:

- Agent Skills is a **portable, filesystem-based format** — a `SKILL.md` file discoverable by any compliant agent runtime (Claude Code, Codex, GitHub Copilot).
- A Pydantic AI capability is a **framework-native Python construct** (an internal `load_capability()` tool + `defer_loading=True` parameter) — it isn't a markdown file another agent runtime could pick up.
- The gap is concrete enough that a third party built a bridge: [`pydantic-ai-skills`](https://github.com/DougTrajano/pydantic-ai-skills) by Douglas Trajano, whose own README states it "implements Agent Skills (agentskills.io) support with progressive disclosure for Pydantic AI" — i.e., native Pydantic AI capabilities needed an adapter to interoperate with the spec at all.

So this is a genuine case of **convergent design, not standard adoption**: three different vendors' agent runtimes (Claude, Codex, GitHub Copilot) share one literal spec; Pydantic AI independently arrived at the same progressive-disclosure UX with its own incompatible mechanism. Cole's "just like" is directionally true and even echoed by Pydantic's own docs — but it reads as spec-parity to a viewer, when it's really UX-parity.

## Cross-link

[[../github-copilot-cli-agents/agent-skills-shared-standard]] — the prior corpus finding this builds on (GitHub + Claude Agent Skills = same spec). Combined, the picture is: **two vendors share one spec, a third (Pydantic) designed an equivalent pattern independently** — a useful three-way comparison point for anyone evaluating skill/capability portability.
