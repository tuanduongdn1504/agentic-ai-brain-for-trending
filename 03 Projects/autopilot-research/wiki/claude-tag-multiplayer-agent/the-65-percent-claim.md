# The 65% Claim — Forensics

## Three non-equivalent official wordings

| Source | Exact wording | Metric implied |
|---|---|---|
| Cat Wu in the launch video (~09:15) | "the number of **PRs that are written by Tag**, I think it's like 65% now, and it's just climbing" | share of PRs *authored* |
| Cat Wu on X ([2069473118742331608](https://x.com/_catwu/status/2069473118742331608)) | "Our internal version **merges 65% of product PRs**" | share of PRs *merged* |
| Anthropic announcement + video description ([introducing-claude-tag](https://www.anthropic.com/news/introducing-claude-tag)) | "65% of our product team's **code** is created by our internal version of Claude Tag" | share of *code volume* |

PRs-written, PRs-merged, and code-created are three different denominators; Anthropic has published **no methodology, no time window, no definition of "authored"** ([Latent Space](https://www.latent.space/p/ainews-claude-tag-multiplayer-proactive) makes the same complaint). All three get press-flattened into "Claude writes 65% of its own code" (TechTimes headline) — a fourth, stronger claim nobody official made.

## Scope: "product org" ≠ Anthropic

- The claim is scoped to **the product org** ("the part of the company that we sit in" — Cat). Not research, not infra, not company-wide.
- It is **lower** than two prior public Anthropic figures — which measure different things:
  - Boris, May 2025: "most of Claude Code is written using Claude Code… like 80 or 90%" ([developing.dev profile](https://www.developing.dev/p/boris-cherny-creator-of-claude-code)); March 2026: "Claude Code is 100% written by Claude Code" ([officechai](https://officechai.com/ai/claude-code-is-now-100-written-by-claude-code-creator-boris-cherny/)).
  - Anthropic, June 2026: ">80% of code merged into Anthropic's codebase as of May 2026 was authored by Claude" (company-wide, all Claude surfaces — not Tag-specific).
- So the honest reading: **65% is the Tag-attributed share within one org**, sitting *inside* an ~80%+ all-Claude-surfaces company figure. Press narrating 65%→80% as acceleration (or 90%→65% as regression) is comparing orthogonal metrics.

## Independent verifiability: none

- No third party can audit Anthropic's internal PR attribution. Verdict class: **PLAUSIBLE-UNVERIFIED, self-reported** — same treatment this corpus gave StrongDM's 32.2K-line factory and TNT's overnight percentages, with one upgrade: unlike those, this one has *three inconsistent first-party wordings*, which is itself evidence the metric is informal.
- [Forbes (Jon Markman, 2026-06-26)](https://www.forbes.com/sites/jonmarkman/2026/06/26/how-one-ai-tool-is-writing-65-of-anthropics-own-code/) explicitly warns the figure "is being read the wrong way" — the differentiator is *where the agent sits* (inside the conversation layer where work is already described), not the percentage.

## Why this matters to this corpus

- This is the **third first-party "AI writes most of our code" datapoint** in the corpus (after Cherny's Claude-Code-writes-itself line and Stripe/StrongDM third-party factories in [[external|Storm Bear: harness-engineering]]) — but the **first tied to a *multiplayer chat surface* rather than a developer harness**. The implied claim: PR-shaped work migrates to wherever the *task description* already lives (bug reports in channels).
- The operator's hireui repo has an **auditable version of this metric for free**: constitution rule I-2 mandates `agent-*` branch prefixes, so agent-authored-PR share is a `git log` query — see pilot method C3 in the pilot menu.

## Key Takeaways

- Quote the claim only in its weakest first-party form: *"Anthropic self-reports that ~65% of product-org PRs are authored/merged by its internal Claude Tag; wording varies across its own channels; no methodology published."*
- Never launder the press form ("writes 65% of its own code") back into the wiki.
- The number's real informational content is **directional dogfooding intensity** — Anthropic runs its own product org on Tag hard enough to publish a majority-share figure 2 weeks into beta.

Cross-links: [[launch-video-annotated]] · [[corpus-positioning]] · [[external|Storm Bear: harness-engineering]] (dark-factory empirics ladder)
