# Sources & stances — the vercel-eve bundle

## Source
- `raw/2026-07-18-vercel-eve/_sources.md` (full manifest) + the 7 transcripts. Verification workflow `wf_e215817b-a5d`.

Seven YouTube sources (operator anchor + yt-search bundle), scored across stances so the fact-check isn't captured by any single POV.

| # | Source | Stance | What it uniquely contributes | Bias / disclosure |
|---|---|---|---|---|
| 1 ⚓ | **Cole Medin** (~217K) | Promotional-collaborative | Best live walkthrough: folder structure, local run, Slack HITL demo, Claude Code plugin scaffolding | **⚠️ Disclosed "I worked with Vercel on this video."** Treat as **Vercel-adjacent reporting** — cross-check all claims. |
| 2 | **Syntax** — Wes Bos + Scott Tolinski (~478K) | Independent, skeptical | Balanced dev view; names Flue + Standard Agent spec; flags **vendor lock-in** + sandbox safety-vs-utility trade | Sponsored by Sentry (disclosed); no Vercel tie. Most credible independent voice. |
| 3 | **Sonny Sangha** (~435K) | Hands-on tutorial | Deep end-to-end build; source of the (unverified) **`eve build`→Nitro self-host** claim | Tutorial creator; no disclosed tie. |
| 4 | **Elie Steinbock** (~103K) | Comparison | **Eve vs Flue** trade-offs; pragmatic "just compose it yourself" take; source of the (unverified) **$3/10K Connect pricing** claim | Independent. |
| 5 | **Rob Shocks** (~44.7K) | Practitioner overview | Accessible framing; source of the **MISLEADING "completely open / manual security"** framing (corrected) | Independent. |
| 6 | **Infisical** (~757) | Feature overview | Security/credential-brokering angle ("everything it is") | Secrets-management company; angle-consistent, not deceptive. |
| 7 | **openclaw / "Dennis"** | Analytical explainer | Strongest on competitive landscape + lock-in critique ("analyzed 25 sources"); source of the **FALSE "6 months" stat** (corrected to ≈1 year) | Small channel; analytical but made the one hard factual error. |

## Primary sources (ground truth)

- [vercel.com/blog/introducing-eve](https://vercel.com/blog/introducing-eve) · [github.com/vercel/eve](https://github.com/vercel/eve) (Apache-2.0) · [changelog](https://vercel.com/changelog/introducing-eve-an-open-source-agent-framework) · [vercel.com/eve](https://vercel.com/eve)
- The Register (headline only; article blocked): *"Vercel debuts eve… tries to fix shadow AI with Passport"* → **Passport** is an adjacent governance feature (see gap in [[vercel-eve/caveats-and-corrections]]).

## Meta-finding

- **The independent sources corroborated the primary facts; the errors came from the promotional/small-channel end.** The one FALSE (openclaw's "6 months"), one MISLEADING (Rob Shocks' "completely open"), and the two unverified specifics ($3/10K pricing; `eve build` self-host) did **not** originate from Syntax (the most skeptical source) — a healthy signal that the bundle's cross-source spread worked.

## Key Takeaways

- 7 sources spanning promotional → skeptical → analytical; **anchor (Cole Medin) is Vercel-collaborated** and was cross-checked, not trusted.
- **Syntax** is the most reliable independent voice here; the factual slips came from the promotional/small-channel sources.
- Primary Vercel docs + the Apache-2.0 repo are the ground truth for every load-bearing claim.

## See also
- [[vercel-eve/claims-scorecard]] · [[vercel-eve/caveats-and-corrections]] · [[vercel-eve/_index]]
