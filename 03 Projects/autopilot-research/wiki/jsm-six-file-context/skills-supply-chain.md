# The skills supply chain — vendor skills, lockfile, symlinks (headline finding)

> This is the topic's most corpus-valuable artifact: a **package-manager-shaped supply chain for agent skills**, observed end-to-end in a real repo. All claims below gh-api-verified 2026-07-03.

## The pieces

1. **Installer:** [vercel-labs/skills](https://github.com/vercel-labs/skills) — "The open agent skills tool - npx skills", **24,832★**, created 2026-01-14, TypeScript, latest v1.5.14 (2026-06-29); the skills.sh ecosystem. Commands: `npx skills add <owner>/<repo>` (project scope default, `-g` global; **symlink mode default**, `--copy` optional).
2. **Vendor-published skill repos** (all org-owned, official — verified):

| Vendor | Repo | Created | ★ | Layout |
|---|---|---|---|---|
| Clerk | `clerk/skills` | 2026-01-06 | 54 | `skills/core/*` + `skills/frameworks/*` |
| Prisma | `prisma/skills` | 2026-01-23 | 43 | `<skill>/SKILL.md` at root |
| Liveblocks | `liveblocks/skills` | 2026-03-13 | 7 | `skills/<skill>/SKILL.md` |
| Trigger.dev | `triggerdotdev/skills` | 2026-01-26 | 28 | `<skill>/SKILL.md` at root |

3. **Lockfile:** `skills-lock.json` — `{version: 1, skills: {<name>: {source: "<owner/repo>", sourceType: "github", skillPath, computedHash (sha256)}}}`. Ghost AI pins **19 skills**: 5 Clerk + 7 Prisma + 1 Liveblocks + 6 Trigger.dev.
4. **Layout:** `.agents/skills/` = canonical install location (**committed to git** in ghost-ai — a lens claimed gitignored; tree ground truth says committed). `.claude/skills/*` = **symlinks** (git mode 120000) into `.agents/skills/` — one source of truth, per-agent adapters.
5. **Format:** every SKILL.md uses Anthropic-standard YAML frontmatter (`name`, `description`, `license: MIT`, `metadata: {version, author}`) + Markdown body; larger skills ship `references/*.md` + `scripts/` + `evals/evals.json` (Clerk ships eval files with its skills).

## Why this matters for the corpus

- **`.agents/skills/` in the wild** — this is the exact portable-skills location from the google-antigravity-skills finding ([[../google-antigravity-skills/anthropic-agent-skills-portability]]): Anthropic's open SKILL.md format + agent-neutral directory + per-agent symlinks. Ghost AI is our first observed **production tutorial repo** shipping it.
- **Vendors now publish skills like they publish SDKs.** Clerk/Prisma/Liveblocks/Trigger.dev each maintain an official skills repo (all created Jan–Mar 2026). The dependency-manager framing (lockfile + content hashes + named sources) is a third distribution mechanism distinct from the corpus's prior two (runtime API-translation proxies; install-time format translators) — Storm Bear Pattern #18 Layer-2 candidate material.
- **Supply-chain surface:** content hashes pin what was installed, but there's no signature chain; `npx skills add` from an arbitrary repo is exactly as trustworthy as the repo. (Compose with the vault's `npm-security-check`/`install-snapshot` discipline if piloting.)

## How skills were actually used in the video (verified, important)

- Installed **before** related features: `npx skills add clerk/skills` (picked `clerk-nextjs-patterns` etc.), `prisma/skills` (all 7), `triggerdotdev/skills` (agents/config/setup), `liveblocks/skills`.
- **NOT auto-consulted.** Adrian's own words are hedged: *"it might even consult the Prisma skill."* No mechanism in the repo auto-loads skills; the transcript shows explicit direction each time. Verifier verdict: automatic-consultation claim REFUTED.
- The one decisive use is **reactive**: after the drag-and-drop failure resisted two fix rounds, *"let's simply tell the agent to check the Liveblocks best practices and fix the drag and drop flow"* → the skill immediately surfaced 3 Liveblocks schema mismatches (nested `flow` key; wrong initial storage; wrong mutation path) and fixed the feature.
- Distilled rule (verbatim): *"whenever you're working with specific tools, always verify that they also have their agent skills, install them, and ask your agent to use them."* Skills as **knowledge-of-last-resort + domain rescue**, not ambient magic.

## The tension: Vercel's own eval says AGENTS.md beats skills

The official Next.js 16.2 AI blog cites Vercel research ("AGENTS.md outperforms skills in our agent evals"): bundled always-available docs hit **100%** on Next.js evals vs **79%** max for skill-based approaches, *"because agents often fail to recognize when they should search for documentation."*
So the same ecosystem ships **both** mechanisms: AGENTS.md-injected always-on context (Next.js docs in `node_modules/next/dist/docs/`) AND on-demand vendor skills — and Ghost AI uses both. The video's reactive-rescue anecdote is consistent with Vercel's finding: the agent didn't reach for the Liveblocks skill until told. See [[agents-md-claude-md-portability]].

## MCP alongside skills

`.mcp.json` commits **only** the Trigger.dev MCP (`npx trigger.dev@4.4.4 mcp`) — installed during `trigger.dev init` with "install MCP for Claude Code: yes". The video's setup flow shows MCP prompts for other tools, but the committed config is Trigger-only. Division of labor observed: **MCP for live platform operations** (Trigger.dev task scaffolding), **skills for knowledge/patterns** (Clerk/Prisma/Liveblocks).

## Key Takeaways

- Skills now have a **dependency manager**: named vendor sources + lockfile + hashes + symlinked per-agent adapters. Treat `skills-lock.json` like `package-lock.json` for your harness.
- The `.agents/skills/` + symlink layout is the portability play: one install serves Claude Code, Codex, Cursor, Antigravity.
- Install vendor skills for your stack, but **prompt for them explicitly** — auto-invocation is not real (here), and Vercel's evals suggest ambient context beats on-demand retrieval for core-framework knowledge.
- Vendor-official skills (with evals!) are a stronger trust story than community skill packs — but still unsigned; keep install hygiene.
