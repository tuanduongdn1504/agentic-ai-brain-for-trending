# The originals — every artifact behind the video, deep-dived

> Per the operator's "double deep-dive into the original resource" standing ask. Each entry: what it is, how we verified, what state it was in on 2026-07-03.

## 1. `adrianhajdin/ghost-ai` (the companion repo — primary artifact)

Created 2026-04-27, pushed 2026-05-01 (video release day), 240★/93 forks/33 commits/8 PRs, **no license**. Contains the entire methodology materialized: `context/` six files + 29 feature-specs, `AGENTS.md`/`CLAUDE.md`, `.agents/skills/` (19 vendor skills, committed) + `.claude/skills/` symlinks, `skills-lock.json`, `docs/superpowers/plans/` (2 files), in-product AI tasks. Committed dev debris (`.trigger/tmp/` build artifacts, watchdog.pid) shows an unpolished push. Fetched: tree (recursive), 23 key files, symlink modes.

## 2. The "Six-File Context System Guide" (jsm.dev/ghost-context)

**Email-gated lead magnet** → redirects to `jsmastery.com/waitlist/six-file-context` (name+email form; no file list on page; author credited: Adrian Hajdin, founder/CEO of JS Mastery). We did NOT sign up; the gate's content is fully reconstructable from repo + transcript ([[six-file-context-system]]) — nothing in our wiki relies on the gated PDF.

## 3. `vercel-labs/skills` — the `npx skills` CLI (skills.sh)

24,832★, created 2026-01-14, v1.5.14 (2026-06-29), TS, no license field. Produces the `skills-lock.json` format + `.agents/skills/` canonical dir + per-agent symlinks observed in ghost-ai. Same tool the official Next.js blog uses to distribute `next-browser` as a skill. Already adjacent to our corpus (vercel-labs is a prior project entry in the Storm Bear state chapters).

## 4. Vendor skills repos (all verified official, org-owned)

`clerk/skills` (2026-01-06, 54★) · `prisma/skills` (2026-01-23, 43★) · `liveblocks/skills` (2026-03-13, 7★) · `triggerdotdev/skills` (2026-01-26, 28★). Anthropic-standard SKILL.md frontmatter, MIT-licensed skill content, some with `evals/evals.json` + helper scripts. See [[skills-supply-chain]].

## 5. Next.js 16.2 "AI Improvements" (nextjs.org/blog/next-16-2-ai, 2026-03-18)

The provenance source for ghost-ai's AGENTS.md managed block: `create-next-app` ships AGENTS.md by default; `npx @next/codemod@latest agents-md` for existing projects; docs bundled at `node_modules/next/dist/docs/`; `CLAUDE.md` = `@AGENTS.md`; plus browser-log forwarding, dev-server lock file, `next-browser` agent devtools. Cites Vercel's eval research **"AGENTS.md outperforms skills"** (100% vs 79%). See [[agents-md-claude-md-portability]].

## 6. obra/superpowers traces (`docs/superpowers/plans/`)

Two plan files dated 2026-04-27 (design-system; feature-02 editor chrome): markdown checkbox task lists headed *"For agentic workers: REQUIRED SUB-SKILL — use superpowers:subagent-driven-development or superpowers:executing-plans."* They are **pre-flight planning templates referencing superpowers skills by name** — evidence the superpowers vocabulary was in the toolchain at project start, NOT proof of execution (no run IDs/hashes), and the pattern was **abandoned after Feature 02** in favor of `context/feature-specs/`. superpowers (Jesse Vincent) is already deep-dived in [[../pocock-agentic-workflow/the-originals]].

## 7. CodeRabbit (sponsor + review layer)

AI code-review SaaS; verified against docs.coderabbit.ai: PR-bot + VS Code extension, walkthrough summaries, 40+ linter integrations, accessibility checks. Both integration modes demoed ([[verification-and-review]]). Sponsor of the video (jsm.dev/ghost-coderabbit).

## 8. Trigger.dev, Clerk, Liveblocks (sponsors + infrastructure)

All three are sponsors AND load-bearing stack pieces. Trigger.dev: durable background tasks, v4 SDK (`task()`/`schemaTask()`), realtime hooks, MCP server (the only MCP committed in `.mcp.json`); its init injected the 35KB vendored docs into CLAUDE.md. Clerk: auth + `proxy.ts` (Next.js 16 renames middleware — the repo and Clerk's own skill templates both use `proxy.ts`). Liveblocks: multiplayer storage/presence + the skill that rescued drag-and-drop.

## 9. The "agentic course" (jsm.dev/ghost-agentic)

Waitlist only ("spec-driven agentic development course," in development). JSM Pro pricing reported around $294/quarter / $880/year (lens-reported, unverified detail). No release date; treat all course specifics as unverified.

## 10. Wispr Flow

Voice-dictation tool Adrian uses for long prompts (captions garble as "Whisper/Wizard Flow"). Same tool already noted in the Pocock threads.

## 11. Prior art the video does NOT cite

GitHub **spec-kit** (Sept 2025), **OpenSpec**, **GSD/gsd-2**, **cc-sdd** (our pilot #1), Cline/Cursor **memory-bank** patterns (e.g. vanzan01's cursor-memory-bank), Kiro steering files, and the mid-2025 **context-engineering** discourse (Karpathy; Tobi Lütke). The six-file system is an independent/convergent repackaging — assessment in [[originality-and-reception]].

## Key Takeaways

- The repo is the real deliverable; the email gate is marketing. Everything teachable is public.
- Three of four "original tools" are sponsor-funded appearances — the methodology is real, but tool *emphasis* follows sponsorship ([[caveats-and-corrections]] #11).
- The deepest original here is the **skills/AGENTS.md standards stack** (items 3–5) — first-party Vercel/Next.js infrastructure our vault already tracks from the Antigravity and Pocock angles.
