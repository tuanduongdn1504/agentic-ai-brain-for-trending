# Source provenance — capture, verification, and what broke

## Capture (2026-07-03)

- **Video:** yt-dlp metadata + English auto-subs for 14RP8liACqo → VTT deduped to ~221K chars / ~40.3K words (ffmpeg absent; VTT parsed directly). Saved with header: `raw/2026-07-03-jsm-six-file-context.md`. Read **in full** across 4 overlapping lens chunks (lines 1–1300 / 1250–3150 / 3100–4800 / 4750–6166).
- **Repo:** `gh api` — repo metadata, full recursive tree (672 blobs), 23 key files (AGENTS.md, CLAUDE.md, README, all six context files, 3 feature-specs, both trigger tasks, both superpowers plans, 3 SKILL.md samples, skills-lock.json, .mcp.json, package.json, trigger.config.ts), plus `.claude/` subtree **git modes** (symlinks = 120000 confirmed).
- **Link chasing:** jsm.dev/ghost-context → jsmastery.com/waitlist/six-file-context (email gate, not signed up); nextjs.org/blog/next-16-2-ai fetched in full (provenance for the AGENTS.md managed block + the AGENTS.md-vs-skills eval claim).

## Verification workflow

`wf_2c3bd01a-8f0` — **41 agents planned**: 9 lenses (4 transcript segments, 3 repo deep-dives, ecosystem prior-art, corpus mapping) → 102 claims extracted, 101 deduped → top 20 verified (5 high-stakes × 3-verifier panels + 15 single REFUTE-first skeptics) → synthesis + completeness critic. ~2.02M subagent tokens, 670 tool calls, ~5.5 min wall clock.

### What broke: session-limit mid-verify

The account usage window expired mid-Verify ("resets 1:30pm"): **13 of 15 panel verifiers + synthesis + critic died**. All 9 lenses and 12 verifier verdicts had already landed. **Main-loop takeover:** the operator session performed synthesis directly and closed the dead panels' claims with primary-source ground-checks:

- Next.js AGENTS.md-injection claim → closed via nextjs.org/blog/next-16-2-ai full fetch (markers official; wording variant).
- "proxy.ts not middleware.ts on Next.js 16" → corroborated by repo root `proxy.ts` + Clerk's own skill template shipping `proxy.ts` + tracker Architecture Decision ("middleware → proxy rename").
- License / commit count / PR count / spec-29 existence / current stars → direct `gh api`.
- "Six-file = proprietary methodology" + "markdown files solve memory" → resolved as framing claims via the ecosystem lens (prior-art) + kept as video-claims, not facts.

81 lower-stakes deduped claims carry **lens-reported only** status; anything load-bearing among them was folded into [[caveats-and-corrections]] "reported-but-unverified."

## Verifier misfires & conflicts resolved (Rule 7 / Rule 12 ledger)

1. **Fabricated quote caught** (our side, by a verifier — good catch): a lens invented a line-4843 transcript quote about tracker auto-updates. Stripped; corrected framing in caveats #6.
2. **Lens vs ground truth:** ".agents/skills is gitignored" → overridden by the recursive tree (committed). Caveats #8.
3. **Lens confabulated glosses:** "GSD = GitHub's Git Sync Dashboard", "spec-kit (Shopify)" → stripped, corrected to the corpus lineage. Caveats #14.
4. **Lens tool-identity error:** "Codex → probably Cursor" → corrected (OpenAI Codex; deliberate portability demo). Caveats #12.
5. **Two-lens conflict on skills auto-use** (build-1 lens said automatic; verifier proved hedged/reactive) → verifier wins, both quotes preserved. Caveats #1.
6. **"Apache-2.0-implied" license guess** → refuted by API (null) + tree (no LICENSE). Caveats #7.

## Known gaps (disclosed, not closed)

- 26 of 29 feature-specs and 16 of 19 SKILL.md files were not individually read (sampled 3 + 3; inventory from tree + lockfile).
- The synthesis + completeness-critic agents never ran; the operator session substituted. A residual risk of single-perspective synthesis bias stands — mitigated by the 20 recorded verdicts and this ledger.
- Reception stats and course economics not independently re-verified (flagged in caveats).
- The email-gated guide PDF was not obtained; wiki reconstructs the system from repo + transcript (superset of the gate, by all evidence).
