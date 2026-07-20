# Free Tokens vs Free Claude — the Three Paths

> **This is the load-bearing article of the topic.** Every video in the bundle collapses three very different mechanisms into one "free forever" pitch. Separating them is the whole value of this wiki.

## Source
Synthesis across all 7 transcripts + ground-truth (Anthropic ToS, Antigravity/Kiro status) + Workflow `wf_e3d4a558-e70` (the Path-A/B/C distinction recurs across 9 of 12 verdicts).

## Path A — route the client to free NON-Claude models  ✅ legal & useful
- **Mechanism:** point Claude Code / OpenCode / Cursor at OmniRoute; OmniRoute routes to **free tiers of non-Claude providers** (DeepSeek, Gemini, Mistral, Kimi, Groq, Nvidia Nemotron, Pollinations…).
- **This is what the "~1.6B free tokens" actually is** and what the anchor's demo actually did (served DeepSeek V4).
- **Status:** fair use of each provider's **published** free tier. Legal *as long as* you respect each provider's own anti-abuse rules (no multi-account farming, no key rotation to dodge caps — behaviour some videos casually encourage, e.g. t6's "delete the key in 30 days").
- **What you give up:** free tiers are slower, rate-limited, quality-variable; Opus still wins hard problems (t3's own verdict).
- **Verdict:** genuinely useful cost-reduction for non-critical, model-agnostic work. This is the pattern worth understanding.

## Path B — proxy *other vendors'* free tiers that bundle Claude  ⚠️ expired / ToS-violating
- **Mechanism:** get *real* Claude models "free" by OAuth-ing into a **third party's** free tier that resells Claude — chiefly Google **Antigravity** and AWS **Kiro** — then routing it through OmniRoute into Claude Desktop/Code. (video **t6** "Use ALL Claude Models".)
- **Status — largely dead and against those vendors' terms:**
  - **Antigravity:** Claude Sonnet/Opus 4.6 *were* in Antigravity's selector (~May 2026), then **removed** ("Anthropic models disappeared from the Antigravity provider"). By the video dates (July 16–20) free Claude via Antigravity was gone — Claude now needs *your own* Anthropic API key there. So t6's live "free Claude via Antigravity" is **FALSE/expired**.
  - **Kiro:** its ToS/FAQ **explicitly prohibits** "use with OpenClaw and similar tools that leverage third-party harnesses," and AWS/Bedrock abuse-detection applies. Routing Kiro through OmniRoute **violates Kiro's terms**.
- **Verdict:** the "free Claude via Antigravity/Kiro" pitch is expired and/or a ToS violation of Google/AWS. See [[antigravity-kiro-and-the-free-claude-window]].

## Path C — reuse a Claude *subscription's* OAuth token  🚫 banned by Anthropic
- **Mechanism:** extract the OAuth token from a Claude Pro/Max subscription (via Claude Code's login flow) and replay it in a third-party client to get Claude API access ~5–10× below pay-as-you-go. This is **CLIProxyAPI's** native trick — and OmniRoute is a **TS port of CLIProxyAPI** with one-click `~/.cli-proxy-api/` import.
- **Status — explicitly banned:** Anthropic's **Jan/Feb 2026** enforcement blocked exactly this and **cut off OpenClaw, OpenCode, Roo Code, and Goose**; the Feb 2026 Consumer Terms state OAuth tokens are **exclusively** for Claude Code + claude.ai.
- **Verdict:** technically feasible in OmniRoute's inherited codebase, **not shown** in most videos, and an **account-ban risk** if you try it. See [[anthropic-oauth-ban-and-tos-risk]].

## The one-glance table

| | Path A | Path B | Path C |
|---|---|---|---|
| **What you get** | free **non-Claude** models | *real* Claude (via 3rd-party free tier) | *real* Claude (via subscription token) |
| **Via** | provider free tiers | Antigravity / Kiro OAuth | Claude subscription OAuth reuse |
| **Legal?** | ✅ (respect provider AUP) | ⚠️ violates Google/AWS ToS | 🚫 violates Anthropic ToS |
| **Works now (Jul 2026)?** | yes | mostly **no** (Antigravity removed; Kiro forbids) | works but **bannable** |
| **The "1.6B tokens"** | ✅ this pool | ✗ | ✗ |

## Why the conflation matters
The videos market **all three as one thing** ("free Claude forever"). A viewer can't tell that the *legal, working* path (A) gives free **non-Claude** models, while the *"free Claude"* they came for is expired (B) or bannable (C). That gap — not any single false number — is the real story.

## Key Takeaways
- Three paths, one marketing blur. **A = free non-Claude (legal, useful). B = free Claude via Antigravity/Kiro (expired/ToS-violating). C = Claude OAuth reuse (banned).**
- The "~1.6B free tokens" is **Path A only**; there is **no working, legal "free Claude"** path as of July 2026.
- Use OmniRoute for Path A if at all; **never** run Path C against a real Anthropic account.
- Related: [[anthropic-oauth-ban-and-tos-risk]] · [[antigravity-kiro-and-the-free-claude-window]] · [[the-1.6-billion-free-tokens-claim]] · [[hireui-relevance]]
