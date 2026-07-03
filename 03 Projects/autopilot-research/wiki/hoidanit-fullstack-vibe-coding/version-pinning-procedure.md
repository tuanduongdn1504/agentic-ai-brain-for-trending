# Version-pinning procedure — git baseline, ncu, strip the ranges, review the diff

> Ep-4 (and the course doc) established the pinning *discipline*; ep-3 contains the mechanical *procedure* that produces the pins. It is a complete, reviewable, 7-step workflow — with git diff as the review surface.

## Source
- Video #3 osISSsyTJJ8, ~1:06:30–1:19:20 — raw: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`
- Tool facts verified via `wf_f3c7237f-4c4` (npm docs, npm-check-updates repo/registry, typescript-eslint registry timeline)

## The procedure (as demonstrated, in order)
1. **`git init`** — "dùng git để bảo vệ mã nguồn... siêu quan trọng"; students without git get pointers (his ~4-yr-old YouTube git series + the free **"Git Zero"** course on hoidanit.vn — course page verified via search snippet).
2. **`git add` + `git commit -m "init project"`** — baseline BEFORE touching anything.
3. **semver literacy**: `^` = newest minor+patch (major fixed), `~` = patch-only, bare = exact ✅ (npm docs). To pin: remove the range char — *"chúng ta đóng đinh luôn cái version"* (nail the version down).
4. **`npm i -g npm-check-updates`** (`-g` explained: machine-wide vs per-project) → **`ncu`** lists available updates without changing anything (on camera: react 19.2.6→19.2.7; an eslint-family row 8.59→8.61 — matches **typescript-eslint**'s registry timeline exactly: 8.61.0 published 2026-06-08, and 8.62.0 landed only hours *after* the live).
5. **Strip the ranges**: Ctrl+H, replace-all `^` (17 hits) + remove `~` (on the TypeScript line — current template pins `typescript ~6.0.x`) → exact pins.
6. **`ncu -u`** — rewrites package.json ONLY (verified behavior; install still required) → **review the git diff**: left = before, right = after; every version bump visible line-by-line. *"Các bạn so sánh bên trái và bên phải... tác dụng của git."*
7. **`npm i`** → package-lock.json regenerates; commit.

Result: **newest-at-record-date, exactly-pinned, diff-reviewed dependency set** — the artifact the course doc then distributes as the frozen starter ([[vite-react-init-workflow]]).

## The AI hook (stated, and the reason this matters beyond beginners)
- *"Sau này khi mà các bạn dùng AI để vi coding ấy thì nó cũng hỗ trợ các bạn cái phần git này thôi. Nhưng mà mình sẽ làm thủ công để cho các bạn luyện tập"* — AI tools automate exactly this git loop; learn it manually so you can read what the agent does.
- Discard-changes demoed as the time machine: change → diff → revert. The workflow teaches beginners the *review posture* that agent-supervision requires: baseline commit → tool acts → human reads the diff → keep or discard.

## Verified tool facts
- `ncu` behavior: lists vs `-u` rewrite-only vs separate install — all ✅ (raineorshine/npm-check-updates). Caption "version 21" for the package is one major stale (latest 22.2.9) — cosmetic.
- package-lock.json: "guarantees that teammates, deployments, and CI install exactly the same dependencies" ✅ npm docs — his explanation matches the docs' purpose statement.
- ⚠️ Template drift note: the CURRENT create-vite react-ts template (post-9.1.x) ships **oxlint** and no typescript-eslint — a fresh scaffold today will not reproduce the video's dependency list. The 8.59→8.61 row is consistent with the template as of the live date; see [[caveats-and-corrections]].

## Corpus placement
- This is the **mechanical complement** to [[version-pinning-discipline]] (the why) — together they form pin-policy + pin-procedure.
- The git-diff-as-review-surface step is the beginner-scale seed of the review layer documented in [[jsm-practical-vibe-coding/_index]] (CodeRabbit) and [[how-we-claude-code/_index]] (agent-native verify): the substrate skill is *reading diffs*, taught here on a package.json.
- Pin-then-upgrade-deliberately mirrors the **skills-lockfile** thread ([[jsm-six-file-context/_index]] `skills-lock.json`) — same reproducibility instinct, dependency-graph edition.

## Key Takeaways
- The pinning workflow is 7 concrete steps with two invariants: **baseline commit before tool runs** and **human reads the diff after**.
- `ncu` splits "know what's newer" from "change the file" from "install" — three separate, individually reviewable moves; that separation is the teachable design.
- Strip `^`/`~` at scaffold time: a fresh project is the cheapest moment to convert ranges into exact pins.
- The same loop is agent-supervision training in miniature — Eric says so explicitly.
