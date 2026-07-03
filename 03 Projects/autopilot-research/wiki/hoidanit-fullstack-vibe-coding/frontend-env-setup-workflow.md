# Environment-setup workflow — Node as platform, LTS literacy, one-version rule

> Ep-3's middle hour is a complete beginner environment-setup curriculum. Every version number in it survived verification — the captions garble words, but this episode's numbers were all real.

## Source
- Video #3 osISSsyTJJ8, ~36:50–57:00 — raw: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`
- Ground truth via `wf_f3c7237f-4c4` (Node release index, nodejs/Release policy, GitHub API, npm registry)

## The mental model taught
- **Node = platform/environment, not a library or framework** — Microsoft-Word-runs-on-Windows analogy: *"chúng ta không học về hệ điều hành"* (you don't study the OS; you install it to run the things you DO study — React, NestJS).
- npm = package manager bundled with Node (verified: "npm bundled" per nodejs.org); registry = *Google Drive for JS packages*; per-language registries (Java → Maven Central Repository ✅ formal name). *"Người đứng sau là Microsoft"* — verified 2-hop: Microsoft→GitHub (2018, $7.5B)→npm Inc (Mar 2020).

## LTS/EOL literacy (all verified)
- LTS = long-term support (Ubuntu analogy); EOL = End of Life ("có bug xảy ra thì anh đi mà fix lấy").
- **Even-major = LTS is real policy**, exact quote from nodejs/Release: *"Odd-numbered release lines are not promoted to LTS."*
- **Never install the newest; install the newest LTS.** On the live day nodejs.org showed **26.3.0 Current** (released 2026-06-01; Node 26 is even → scheduled to *become* LTS ~Oct 2026, not LTS yet — his on-screen uncertainty was the correct read) vs footnote "latest LTS = Node 24" (**Active LTS, codename Krypton** in June 2026).
- Anti-latest-chasing: *"Những cái mà các bạn nghĩ ngày hôm nay nó mới thì qua ngày mai nó là cũ rồi"* — learn on a pinned version, upgrade after it runs clean.

## The install procedure
1. Doc pin: **"Cài chính xác Node.js version 24"** → nodejs.org/download/release/**v24.14.0**/ (real, 2026-02-24). On camera he also swaps the URL to **v24.16.0** (real, 2026-05-21 — the newest 24.x patch at the live date). Teaching: the **release-directory URL pattern** (swap the version segment; per-OS artifacts, MSI for Windows) beats hunting the download page.
2. Verify: `node -v` → v24.x; `npm -v` → **npm 11** (verified: "Node.js 24 comes with npm 11").
3. **One-version rule for beginners**: install exactly ONE Node. He runs 20/22/24 across series — via **nvm** (nvm-sh, **94,012★** verified vs caption ~93K) on macOS/Linux and the separate **nvm-windows** (coreybutler, 46,973★, active, Releases-page installer) on Windows; `nvm use 24.14.0` demoed. Multiple versions = a maintainer's need, not a learner's.
4. Terminal literacy sidebar: Windows 11 right-click → Terminal (install "Windows Terminal" from Microsoft Store if absent); macOS `cd` + `ls -a`; *"đây là cách các bạn dùng máy tính... không phải là lập trình"* — computer literacy is the hidden prerequisite he refuses to skip.

## Why exact pins (the game analogy)
- A game built for one Windows version isn't guaranteed on the next — same for toolchains: pin the environment the video used → *"code của các bạn giống code trong video... ít bug nhất có thể."* Reproducibility is the point, not conservatism: *"khi mà mình quay video... là mình đã cài version mới nhất rồi"* (it WAS the newest — at record time; then he freezes it).

## Key Takeaways
- The platform/tool distinction ("don't study the OS") is load-bearing pedagogy: it tells beginners where NOT to spend attention.
- LTS/EOL/even-major literacy turns "which version?" from folklore into a checkable policy — and his live uncertainty about 26.3.0 modeled *the correct epistemic move* (check the LTS label, don't assume).
- Doc pins a slightly-older LTS patch (24.14.0) than the day's newest (24.16.0): both real; the doc wins for the cohort — freezing beats freshness (Rule-7 surfaced, no conflict).
- The URL-pattern teaching (release-directory + version-swap) is a small **docs-navigation skill** in the same family as the version-dropdown skill in [[version-pinning-discipline]].
- Cross-links: [[docs-first-ai-second]] (docs as canonical source), [[version-pinning-procedure]] (the dependency-level sequel), [[tech-stack-rationale]].
