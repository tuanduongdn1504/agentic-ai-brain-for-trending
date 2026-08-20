# Cordis and the paper the source-read missed

> **This page carries the bundle's single most valuable corpus contribution.** The YouTube layer surfaced a formal paper that the vault's own eight source-level DSH analyses (v235–v242, `/Users/Cvtot/KJ OS Template/03 Projects/`) do not record — despite it being linked from the README they read.

## The paper is real

Verified independently on 2026-08-20:

| Field | Verified value |
|---|---|
| Title | **"A Programming Paradigm for Spatiotemporal Composability"** |
| Repo | `github.com/cordiverse/paper` — **2.4k stars** |
| Status | **"Draft of August 13, 2026"**, *"a preprint under active revision"* |
| Authors (per secondary reporting) | Yifan Shi (Peking University + DeepSeek), Wei Zhang (Peking University), Tianyi Cui (DeepSeek) |
| Length | ~80+ pages (secondary sources; **not** primary-verified) |
| Math basis | **effects and coeffects** from type theory |

The DSH README *"is powered by Cordis"* and links this paper by title. **So the paper was reachable from the exact file the source-level read opened.** That is a method finding, not a subject finding — see [[deepseek-harness/hype-vs-source-scorecard]].

## The abstract, verified verbatim

The Cef Experience reads the abstract aloud on camera. Fetching `cordiverse/paper` returns the same text:

> *"Modern software—from plugin systems to self-evolving agent harnesses—increasingly requires dynamic composition, yet its formal foundations remain underdeveloped. We identify two orthogonal dimensions of the problem: temporal composability, the ability to completely revert a component's side effects upon removal, and spatial composability, the ability to declare and reactively manage inter-component dependencies."*

Cef's read-aloud is accurate to the source. Graded CONFIRMED.

## The two dimensions, in plain terms

**Temporal composability — every change ships with its inverse.** Turing Post: *"If a component registers a listener, Cordis records how to unregister it. If it starts a timer, Cordis reports how to stop it. When the component leaves, those effects unwind in reverse order."*

**Spatial composability — dependency-ordered shutdown.** *"If one plugin provides a service that another needs, the dependent plugin shuts down first while it can still access the service. Only then does the provider disappear."*

The problem being solved is stated crisply by Turing Post: *"Creating the plugin is the easy part. Removing it is where the paper begins."* Remove a plugin naively and the command disappears while its timer keeps running and its dependents lose what they needed to shut down cleanly. Software's traditional fix is *"restart the whole application and hope everything comes back."*

## Confluence — and its boundaries

The paper's headline result, as Turing Post renders it: load A, add B, experiment with C, remove C, restore A — versus simply loading final A and B from scratch. **Under the paper's conditions, once both systems settle, their observable state should be equivalent.** The final system depends on the components that remain, *"rather than every detour it took to get there."*

**Turing Post then states the limits, and this is why it is the strongest source in the bundle:**

- *"Plugin authors must provide correct inverses."*
- *"The strongest result assumes successful execution, sufficiently independent effects, and dependencies without cycles."*
- *"The formal model also simplifies some features in the implementation."*
- And the line that should be quoted at anyone selling reversibility: *"Cordis can remove the plugin that sent an email. It cannot remove the email from somebody's inbox."*

**Load-bearing caveat for the vault: this is a preprint under active revision, dated four days before the earliest video in the bundle. It is not peer-reviewed.** Turing Post treats confluence as a result; it is a drafted claim. Do not cite it as established PL theory.

## Lineage — Cordis did not come from DeepSeek

This is the fact that reframes the whole "DeepSeek shipped a breakthrough" narrative.

Turing Post: *"Cordis was not a DeepSeek invention. It came out of the [Koishi] ecosystem, and [Koishi] is an open source chatbot framework created by [Shigma], who also created Cordis and named after [Komeiji Koishi], a character from Touhou Project."* Verified: Cordis is an independent meta-framework by **shigma**, and has been Koishi's foundation for **four years**.

**Turing Post's independently-verified production claim:** *"Over 4 years, more than 4,000 community contributed plugins pushed the run time through real dependencies, hot reloads, failures, and cleanup problems."* Confirmed by external reporting — 4,000+ community plugins in production over four years.

So DeepSeek's contribution was **recognition plus formalization**, not invention. Turing Post says this outright: *"DeepSeek recognized what was sitting there."* And: *"The harness layer was never proprietary. It was sitting in open source inside a chatbot plugin ecosystem waiting for somebody to recognize what it could become."*

This **independently corroborates the v242 source-level finding** that DSH's README credits Cordis to `cordiverse` / Shigma and that **dsh is the *consumer* of the plugin framework, not its author** — a conclusion v242 reached by cloning 201MB and reading `README.md:7`. Two entirely different methods, same answer. That is the strongest cross-vault agreement in this ship.

**One unresolved date divergence:** Better Stack says Cordis has *"been sat on GitHub since 2022"*; v242's source read recorded the copyright header as *"Copyright (c) 2021-present Shigma"*; external reporting says "four years" as of Aug 2026 (→ ~2022). Recorded, not resolved. See [[deepseek-harness/caveats-and-corrections]].

## Why the paper matters beyond DSH

Turing Post's framing — the most interesting idea in the bundle — is that the novelty is *"the package. And the attempt to prove the local discipline can produce a stable global result."* The ingredients *"have precedents in effect systems, dependency injection, hot reloading, and dynamic service frameworks."*

Cef reaches the same generalization from the implementation side: *"this doesn't have to be limited to coding agents or harnesses. Any type of application, so if an app is built on top of such a framework such as Cordis, and it can have plugins and be modified without breaking, then if you have an LLM behind the scenes, then it can add new components, remove components, and truly customize the user experience."*

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/overview]] · [[deepseek-harness/everything-is-a-plugin]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[deepseek-harness/claims-scorecard]] · [[elicit-verifiable-agent-dsl/_index]] · [[system-thinking-ai-coding/_index]]
