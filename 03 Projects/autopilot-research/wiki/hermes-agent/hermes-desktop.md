# Hermes Desktop — the surface the 2026-07-18 build missed entirely

> **Added:** 2026-09-03 revisit. The prior 10-article build had **no dedicated Desktop coverage** — one clause in passing at `channels-providers-deployment.md:17` ("native desktop apps for macOS 12+/Windows 10-11/Linux") and nothing else. Three of the six sources in this drain are Desktop-focused, which is what surfaced the gap.
>
> ⚠️ **That one clause caused a circular-verification incident during this revisit.** A critic agent "confirmed" the minimum OS versions by reading the prior wiki, and reported them as established fact. They are **not** in any primary source — `apps/desktop/README.md` names macOS, Windows and Linux with no version floors. The 2026-07-18 figures presumably came from a video. **A wiki cannot be evidence for itself**; see [[revisit-2026-09-03]] for the other verification-process failures this drain recorded.
> **Primary source:** `apps/desktop/README.md` in the main repo, fetched verbatim 2026-09-03 via `raw.githubusercontent.com`. Quotes below are from that file.

## Why it was missed, and why that matters

The 2026-07-18 bundle was eight videos about the **CLI**. Its `_index` describes Hermes as a "single-user, always-on personal agent … reachable across 20+ chat channels" — accurate, and silent on the fact that there is a **native GUI application** shipping from the same repo under the same MIT license.

The gap was not random. It is a **selection artifact**: the prior bundle's query surfaced CLI/comparison content, so the wiki inherited a CLI-shaped view of the product. The 2026-09-03 query (`Hermes Agent Nous Research setup tutorial`) surfaced install content, and install content is where Desktop lives — `t2-weeb3dev` (2026-06-08), `t4-wanderloots` (2026-07-01), and partly `t6-codehead`.

**Corpus lesson:** a topic's article set inherits the *shape* of its source query, not just its content. A second drain on a deliberately different query is the cheapest way to find out what the first one structurally could not see.

## What it is — verified

**First-party, in-tree, same license.** Source lives at `apps/desktop/` in `NousResearch/hermes-agent` (confirmed: `apps/desktop/package.json` and `apps/desktop/README.md` both return HTTP 200 from `raw.githubusercontent.com`, 2026-09-03). The main README's hero nav reads `Hermes Agent | Hermes Desktop`, both linking `hermes-agent.nousresearch.com`.

> "**The native desktop app for Hermes Agent** — the self-improving AI agent from Nous Research. **Same agent, same skills, same memory as the CLI and gateway**, in a polished native window — chat with streaming tool output, side-by-side previews, a file browser, voice, and settings, **no terminal required**. Available for **macOS, Windows, and Linux**."

Six documented capabilities (verbatim from the feature table):

| Feature | What the README says |
|---|---|
| Chat with the full agent | "Streaming responses, live tool activity, structured tool summaries, and the same conversation history as every other Hermes surface." |
| Side-by-side previews | "Render web pages, files, and tool outputs in a right-hand pane while you keep chatting." |
| File browser | "Explore and preview the working directory without leaving the app." |
| Voice | "Talk to Hermes and hear it back." |
| Settings & onboarding | "Manage providers, models, tools, and credentials from a real UI." |
| Stays current | "Built-in updates pull the latest agent and rebuild the app in place." |

**Requirements** — the one line that matters for the no-code question:

> "The installer handles everything for you (Python 3.11+, a portable Git, ripgrep)."

**Install — two paths, and the recommended one is not the GUI one:**

- **Recommended:** `hermes desktop` — *"Already have the Hermes CLI? Just run…"*. It "builds and launches the GUI against your existing install — same config, keys, sessions, and skills."
- **Alternative:** prebuilt installers, "built and distributed via the Hermes Desktop website."
- First launch, if no runtime or saved remote connection is found, offers to connect to an existing Hermes gateway **or** install Hermes locally.

**Updating:** background check with one-click update, or `hermes update` from the CLI.

## ⭐ The Desktop README undercuts the "no-code" framing from the inside

This bears directly on [[caveats-and-corrections]] H6 (*"no-code / easier than OpenClaw"* — MISLEADING) and on the 2026-08-26 anchor, whose title is *"Không Cần Biết Code"* ("no coding needed"):

- The README's own words are **"no terminal required"** — a claim about the *running* experience, not about installation.
- The **recommended install path starts with the CLI** (`hermes desktop`). The vendor's preferred route to the GUI runs through a terminal.
- The prebuilt-installer path does avoid the terminal, and the installer genuinely bundles Python 3.11+, Git and ripgrep — so a true no-code install **does exist**. It is simply not the one the vendor recommends, and it is not the one the anchor demonstrates: the anchor's body is a terminal session on a purchased VPS (`full setup`, space/enter selection, an explicit warning that Ctrl+C cancels rather than copies).

**Net:** "no-code" is defensible for the prebuilt-installer path and indefensible as a description of what the anchor actually teaches. H6 stands as MISLEADING, and the revisit sharpens *why* — the framing is now attached to a real product surface that the source does not use.

## Bot Mode — real, but its integration is under-documented

⚠️ **Handle with care. The claims below are unevenly grounded and are separated accordingly.**

**Verified:**
- **"Bot Mode" and "plugin" appear ZERO times in `apps/desktop/README.md`** (grep-confirmed, 2026-09-03). Whatever Bot Mode is, the Desktop app's own documentation does not mention it.
- v0.21.0 "The Pantheon Release" (tag `v2026.8.31`, 2026-08-31) release notes describe **Bot Mode shipped built-in to the desktop app**, with multi-agent society, cron jobs with memory, live subagent steering, and an MCP command center.

**Asserted by a secondary first-party source, not independently confirmed:**
- A standalone repo `NousResearch/Hermes-Bot-Mode` was created **2026-08-13** and is **now archived**, its README stating Bot Mode "now ships built into Hermes Desktop" (referencing PR #87886).
- That archived README is also the only source for the multi-bot roster, group chats, bot-to-bot messaging, and a Settings → Plugins toggle.

**Refuted as stated:**
- The specific path `apps/desktop/src/plugins/hermes-bots/` **does not resolve** — `README.md` and `index.ts` under it both return **404** (2026-09-03). This path came from the archived repo describing where its code was going, and should not be cited as the code's location.

**Unresolved:** whether Bot Mode is default-on. Claimed by the archived repo; absent from the Desktop README; not stated in the v0.21.0 notes.

## HermesOS does not exist

A high-reach video the rubric surfaced but did not select — Tina Huang's `1CLc-VeEivk` "My FULL Hermes Agent Setup (**HermesOS**)", 141,888 views — names a product called HermesOS.

**It is a creator coinage.** A GitHub search for `HermesOS org:NousResearch` returns **0 results**, and the string appears nowhere in the main README. Recorded here so a future ingest does not adopt it as a product name on the strength of a video title.

## Open questions a deployer would ask, unanswered by any source or doc

- **Does Desktop resume a *live* CLI session, or only share saved state?** Graded **UNVERIFIED (2 of 3 lenses)**. The docs support state *sharing* — "same config, keys, sessions, and skills"; "the same conversation history as every other Hermes surface" — but no primary source says the app can pick up a session already running in a terminal, which is what `t2-weeb3dev` demonstrates.
- **Minimum OS versions.** The README says macOS, Windows and Linux with no version floors. Any specific floor (e.g. "macOS 12+") is **unverified** — a critic asserted one and no primary source supports it.
- **Does Desktop change the subagent-isolation or data-residency picture?** Still the topic's hard deployment blocker ([[caveats-and-corrections]]), and Desktop's docs add nothing to it.

## Key Takeaways

- **Hermes Desktop is first-party, in-tree, MIT, and cross-platform**, and the prior build's silence on it was a source-selection artifact rather than a judgement.
- **A true no-code install exists** (prebuilt installer bundling Python/Git/ripgrep) — but it is the *un*-recommended path, and not the one the "no coding needed" anchor demonstrates.
- **Bot Mode is real and its documentation is not.** The feature is in the v0.21.0 notes and an archived repo; it is absent from the Desktop README, and the file path everyone cites for it 404s.
- **HermesOS is not a product.** Verified absent from the org.

## Cross-links
[[revisit-2026-09-03]] · [[the-vendor-seeded-false-claim]] · [[channels-providers-deployment]] · [[overview]] · [[caveats-and-corrections]] · [[claims-scorecard]] · [[source-provenance]]
