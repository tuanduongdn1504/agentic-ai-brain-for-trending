# 07 — Git, testing & engineering practice

Stack-independent hygiene Tuấn checks in every interview. The Git section is where several candidates showed **dangerous habits** — this is high-yield to get right.

## Git

### Everyday workflow

`git status` → `git add <files>` → `git commit -m "msg"` → `git pull` (before push, to avoid conflicts) → `git push`. First push of a new branch: `git push -u origin <branch>` (sets upstream).

### `git checkout` variants (asked in video 2)

- `git checkout <branch>` — switch branches.
- `git checkout -b <branch>` — **create + switch** (lowercase `-b`).
- ⚠️ `git checkout -B <branch>` — **create-or-reset (force)**; not the everyday create. Candidate used `-B` where `-b` was meant — the case matters.
- `git checkout -- <file>` — discard local changes to a file. `git checkout <commit>` — detached HEAD. (Modern Git splits these into `git switch` / `git restore`.)

### `git fetch` vs `git merge` vs `git pull`

- **`fetch`** = download remote commits **without** touching your working tree (safe, read-only "let me see what's on the remote").
- **`merge`** = integrate fetched commits into your current branch (changes your files).
- **`pull`** = `fetch` + `merge` in one step.

### `git rebase` vs `git merge` (asked in videos 1 & 2; neither candidate knew rebase)

- **merge** keeps both histories and adds a **merge commit** (branching history tree).
- **rebase** **replays** your commits on top of the target branch → **linear history**, no merge commit. `git rebase -i HEAD~N` also lets you **squash/reword/reorder**.
- ⚠️ **Golden rule:** don't rebase commits already **pushed to a shared branch** — it rewrites history for everyone.

### Merge conflicts — the right way (candidates got this WRONG)

- A conflict = two people changed the **same lines**. Git inserts markers: `<<<<<<< HEAD` … `=======` … `>>>>>>> incoming`.
- **Resolve:** read both sides, edit the file to the correct combined result, **delete the markers**, `git add <file>`, `git commit`. Use an IDE 3-way merge / `git mergetool`.
- ⚠️ **Anti-pattern seen twice:** "avoid the conflict by **renaming the file**" — this discards the other person's changes and is a real red flag. Never do this.

### `.gitignore` (candidate hadn't used it)

- Lists patterns Git should **not track**: `node_modules/`, `.env`, `build/`, `/ios/Pods`, `*.log`. Keeps generated + **secret** files out of the repo. Essential hygiene.

### Pull requests

- Push a feature branch → open a **PR** (branch → main) → request review → reviewers approve / request changes → merge (merge-commit / **squash** / rebase strategy). The PR is the **code-review gate** before main. (Candidate knew the flow but not the review/approval details or merge strategies.)

### Amending a commit

- **Local, not pushed:** `git commit --amend` (last commit) or `git rebase -i HEAD~N` → `reword`.
- **Already pushed:** `git commit --amend` then `git push --force-with-lease` — risky (rewrites history); avoid on shared branches. ⚠️ (Candidate confused this with `git reset`.)

## Testing

- **Stages dev → release:** unit (dev) → integration (QA) → system → UAT (user acceptance) → regression → release. Candidates typically named only "developer self-test + tester test" and had **never written a test** — knowing the ladder + that automation runs throughout is the stronger answer.
- **Unit test:** tests a single function/component **in isolation** (mock its dependencies), asserting output for given input. Tools: **Jest / Vitest** (JS/React), **flutter_test** (Flutter). Runs before integration; a green suite gates merge/deploy.

## Code quality

- **Clean code:** descriptive names, small single-purpose functions, shallow nesting (<3), comments explain **why** not **what**, testable (no hidden side effects).
- **SOLID:** **S**ingle Responsibility · **O**pen/Closed · **L**iskov Substitution · **I**nterface Segregation · **D**ependency Inversion. Candidates typically knew only **S** (one function = one job) — at least name all five; SRP is the one to explain well.
- **DRY (Don't Repeat Yourself):** duplicate logic → extract a reusable function/component so a fix happens in one place.

## Debugging / DevTools

- **Browser DevTools:** Elements (DOM), Console (logs/errors), **Network** (API requests — often forgotten but key), Sources (breakpoints).
- **React DevTools:** component tree, props, hook state. **Flutter DevTools:** widget inspector, performance, layout.

## Key Takeaways

- **Resolve merge conflicts by editing the markers — never by renaming the file.**
- Know **rebase vs merge** (linear vs merge-commit) + the "don't rebase shared history" rule.
- `.gitignore` keeps `node_modules`/`.env`/secrets out of the repo.
- A **unit test** isolates one unit (mock deps); name the full **dev→release** test ladder.
- **SOLID** = name all five, explain **S**; **DRY** = one source of truth.

**Sources:** all five videos (Git = 1,2; testing/quality = 5; DevTools = 5). Related: [[08-behavioral-and-interview-craft]] · [[nodejs-backend-interview/06-testing-git-docker]] · [[fullstack-docker-cicd/_index]].
