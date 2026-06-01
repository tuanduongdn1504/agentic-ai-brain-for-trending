# (C) Command Center build-pilot — handoff + dispatch convention

> **Date:** 2026-06-01
> **Type:** Pilot handoff / next-session state doc (sibling to `04 Reviews/(C) 2026-05-08 adversarial-review comparison pilot setup plan.md`).
> **Pilot target (the thing being built/piloted):** `/Users/Cvtot/KJ OS Template/03 Projects/product/build-your-own-dashboard-prompt` — "Command Center", the operator's own agent-ops product. NOT a corpus wiki subject; this is a wiki←product build pilot.
> **Purpose:** Drop this into a fresh session for full continuity. Also codifies the build-session dispatch convention (worktree vs main) for any future knowledge/product build.

---

## 1. What Command Center is

Standalone localhost agent-ops dashboard. **Repo:** `/Users/Cvtot/KJ OS Template/03 Projects/product/build-your-own-dashboard-prompt` (git, branch `main`). **Install (separate copy):** `/Users/duongtuan/.command-centre`. Stack: Python FastAPI + SQLite-WAL backend · Vite/React/TS web UI · 3 launchd agents (`mission-control` dispatcher, `telegram-bridge`, `weekly-backup`) · stdlib Telegram bridge. Server `127.0.0.1:8765`. DB `~/.command-centre/data/command-centre.db`. `cc` CLI at `~/.command-centre/bin/cc`; venv python `~/.command-centre/venv/bin/python3`.

## 2. Environment gotchas (these bit hard — read first)

- **`rtk` shell wrapper** mangles `git`/`grep`/large-output commands ("command not found: rtk"). Bypass: run via `command bash --noprofile --norc -c '…' > /tmp/out.txt 2>&1` then Read the file; use `command git --no-pager`, `command grep`.
- **arm64 machine.** Working claude = `~/.nvm/versions/node/v24.13.1/bin/claude`. `/usr/local/bin/claude` is BROKEN (native binary missing) — overridden via `CLAUDE_CLI_OVERRIDE` in the mission-control plist (install.sh resolves the operator's claude via login shell).
- **Install ≠ repo.** Code on `main` is NOT live until deployed:
  `bash command-centre/install.sh --yes --no-otel --no-build-ui --project-root="<repo>" --port=8765 --model=claude-sonnet-4-6` then `cc restart` (DB migrations run on server startup).
- **UI build:** `ui/dist` is gitignored (a worktree build's dist does NOT come over on merge — rebuild from merged main). `package-lock.json` was regenerated for arm64 (prior lock pinned rollup native dep to x64 → `npm run build` failed). If a UI build fails on `@rollup/rollup-darwin-x64`: `rm -rf node_modules package-lock.json && npm install` in `command-centre/ui`.

## 3. Shipped (all on `main`, deployed, validated)

v0.6.0 → v0.6.8, v0.7.0 (adversarial review gate), v0.7.1 (accept-as-is), **v0.7.2** `d02b5de` (dispatcher actually executes), **v0.7.3** `ebbbc80` (tasks run in `CC_PROJECT_ROOT`). Latest line: `ebbbc80 ← d02b5de ← 0f18c9d(v0.7.1) ← 233acf8(v0.7.0) ← 5ce116e(v0.6.8)`. **Committed LOCAL-ONLY — not pushed.**

Wiki contribution this arc: **Cost-Discipline Enforcement Observation-Track** filed to this vault (commit `60b6d2d`, branch `autopilot-research`; entry in `_patterns/03-active-candidates.md`; proposal in `04 Reviews/(C) 2026-05-29 …Cost-Discipline Enforcement….md`).

## 4. The key lesson (do not repeat)

The dispatcher's core loop **had never executed a real task** across 13 features — smoke tests stubbed `claude`, masking 3 bugs (wrong binary under launchd / missing `--verbose` / headless permission wall) + a 4th (no `cwd`). Found only when the operator finally tested from the phone. Fixed v0.7.2 + v0.7.3. **A smoke test that stubs the core dependency can pass while the product is fundamentally broken — validate the real path on real hardware before trusting "done".**

Full loop now **human-validated**: phone `/run` → launchd dispatcher → claude (working binary, project cwd, `--dangerously-skip-permissions`) → file written in the project → task `done` → ✅ Telegram ping (msg 22, confirmed on device 2026-06-01).

## 5. Dispatch convention — worktree vs main (the operator's question, answered)

**Default fresh BUILD sessions to a git worktree; keep small inline hotfixes on `main`.**

| Work type | Where | Why |
|---|---|---|
| **Dispatched build session** (a feature spec handed to a separate Claude Code session) | **worktree** on a `claude/<name>` branch | Isolation — `main` stays stable until merge. Enables a verify-before-merge gate (this arc that gate caught a stale UI dist + an unmerged-state confusion). Safe for autonomous `--dangerously-skip-permissions` agents. Allows parallel builds. Matches what already happened (v0.7.0/v0.7.1 built in worktrees). |
| **Small inline hotfix** (1–2 files, diagnosed in the driving session) | **`main`** directly | Worktree is ceremony overhead. v0.7.2/v0.7.3 were done on `main` — faster, fine. |
| **DRAFT spec commit** (the amendment + CHANGELOG DRAFT) | **`main`** | Small docs; the worktree branches from `main` with the DRAFT already present. |

**So: YES, prefer worktrees for fresh dispatched build sessions** — but it is not free. Enforce this discipline or worktrees become cruft:

1. **Verify in the worktree before merging** (this is the whole value): confirm the build matches spec + run its smoke suite IN the worktree, then fast-forward merge to `main` (`git merge --ff-only claude/<name>`).
2. **Clean up after merge.** This arc left ~4 stale worktrees (`reverent-napier`, `upbeat-goldberg`, `vigorous-elgamal`, `v0.6.1-status`) + their branches. After merge: `git worktree remove <path>` + `git branch -d claude/<name>`.
3. **Gitignored-artifact trap.** `ui/dist` + `node_modules` are gitignored → a worktree's built dist does NOT merge to `main`. After merging a UI change, rebuild dist from `main` (and fix arm64 node_modules once — see §2) before deploying, or the deploy ships stale UI on fresh backend (split-brain).
4. **Deploy from `main`** after merge (install.sh reads the repo it runs in). Don't deploy a worktree.

Mechanisms: the `Agent` tool supports `isolation: "worktree"`; a fresh Claude Code session does `git worktree add` + `git checkout -b claude/<name>`.

## 6. Open backlog (all non-critical)

- doctor's stale `telegram-bot` check (real agent is `telegram-bridge` → false alarm) — ~30 min
- `is_error` success-detection (v0.7.4, in CHANGELOG) — dispatcher trusts returncode only; should parse the stream `result` line's `is_error`
- multi-account UUID config — `~/.command-centre/data/accounts.json` has `uuids:[]` empty since v0.6.3; operator UUID `6374a372-fd9a-4d06-9183-3fe7af57e289`
- bridge restart-quietness — `Connection refused` spam during deploys (server down while bridge polls); add retry/backoff
- review-gate (v0.7.0) + accept (v0.7.1) flows not yet phone-exercised (smoke-only: 69/69, 43/43)
- push v0.7.x hotfixes to remote (currently local-only)

## 7. Working rules (Storm Bear vault CLAUDE.md)

Blunt/direct · prefix AI files with `(C)` · ask before editing existing notes · never fabricate · end every reply with a next action · commit only when asked · never push unless asked.

## 8. Continue / re-deploy (commands)

```bash
# deploy main → live install (runs migrations on restart)
bash command-centre/install.sh --yes --no-otel --no-build-ui \
  --project-root="/Users/Cvtot/KJ OS Template/03 Projects/product/build-your-own-dashboard-prompt" \
  --port=8765 --model=claude-sonnet-4-6
~/.command-centre/bin/cc restart && ~/.command-centre/bin/cc doctor
# verify a real run: /run a task from Telegram → file lands in <repo>/tmp + ✅ ping
```

---

End of handoff. Clean restart point: the Command Center pilot's product loop works end-to-end and is human-validated; remaining work is the §6 backlog. For future build sessions, default to a worktree per §5.
