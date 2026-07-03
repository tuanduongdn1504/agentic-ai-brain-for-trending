# Raw source — Hỏi Dân IT "Fullstack Vibe Coding với AI" series, video #3 (MVP + environment + frontend init) — FULL first-party treatment

> **Ingested:** 2026-07-04 (path 5 yt-dlp, operator-submitted URL; deepening of existing topic `hoidanit-fullstack-vibe-coding`)
> **Video:** https://www.youtube.com/watch?v=osISSsyTJJ8
> **Title:** #3. MVP & Setup Môi Trường & Dự Án Frontend | Series Fullstack Vibe Coding với AI Dành Cho Beginner
> **Channel:** Hỏi Dân IT (@hoidanit) — 74,600 subs per yt-dlp at fetch
> **Uploaded:** 2026-06-24 (Wednesday) · 1:27:32 · 1,337 views at fetch · **livestreamed Monday 2026-06-22** (transcript: "Hôm nay là thứ hai... thứ tư tuần này thì mình sẽ ra video"; closes "hẹn gặp lại tối thứ hai tuần sau")
> **Captions:** Vietnamese auto-subs 1.13MB VTT → deduped 2,631-line / ~131K-char timestamped transcript, **read in full in main loop**
> **Prior coverage:** 6-bullet secondary digest in `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md` (ep-4 anchor ship). This file supersedes that digest for ep-3.
> **Verify workflow:** `wf_f3c7237f-4c4` (10 dives + 16 refute-first skeptics + critic) — verdicts folded into Corrections below.

## Episode structure (as delivered)

1. **MVP analysis** (~06:15–20:30) — concept, e-commerce MVP checklist via AI, defer-list, work order
2. **Environment setup** (~36:50–57:00) — Node-as-platform, LTS/EOL, exact-version install, nvm, npm
3. **Frontend init** (~25:00–36:00 rationale + 57:00–1:19:00 hands-on) — Vite selection, create-vite demo, package.json anatomy
4. **git + version pinning procedure** (~1:06:30–1:19:00) — git init baseline, ncu, strip range chars, diff review
5. **Run + HMR** (~1:24:00–1:26:30) — npm run dev, port 5173, hot reload demo

## Digest (EN structured extraction; timestamps from VN transcript)

### MVP method (the checklist he built on camera and pasted into the course doc)

- MVP = minimum viable product = "bản demo nhưng cần thể hiện được workflow... những tính năng cốt lõi nhất" [00:07:30].
- **Stated core reason: money.** [00:08:34] "cái lý do chủ chốt... câu chuyện liên quan về tiền... đây chính là cái yếu tố sống còn" (his personal view, flagged as such on camera). Cost→revenue feasibility; over-building before market validation = "vứt tiền qua cửa sổ" [00:09:12].
- Version 1→N mental model: Shopee is a version-N product, not built in a day [00:08:09]; phase-based delivery ("face 1, face 2"); **rebuilding v1 entirely at v2 is normal** [00:09:40].
- Anti-blind-vibe warning reprised: vibe-coding 10K–100K lines you don't understand = **technical debt, "quả bom nổ chậm"** (time bomb) [00:05:00–00:05:16].
- **The scope decision itself is AI-assisted but human-curated**: he prompts an AI chat ("tôi coding web thương mại điện tử, MVP là gì?"), reads the checklist, **catches what the AI missed on camera** — user management: "Ở đây thì nó đang thiếu... trang quản lý user. Một cái huyền thoại. Nếu mà không có user thì hệ thống này thì làm kiểu gì" [00:23:02] — and edits before pasting into the doc. "Bắt buộc các bạn sẽ cần phải đọc và chúng ta đánh giá... không thể rằng là tôi copy paste và tôi không phản biện với nó được" [00:15:32].
- **MVP scope (buyer):** 4 pages — product listing (image/name/price/buy+add-to-cart buttons), product detail, cart, checkout [00:11:06–00:12:26].
- **MVP scope (admin/backend):** inventory (kho) + orders + **user management (his addition)** [00:12:26, 00:23:02].
- **Defer list:** auth/login (explicitly optional for MVP!), online payment (**COD first** — cash on delivery; VN-market default), reviews, discount codes + campaigns (Shopee 6/6-7/7-style), advanced inventory, search/filter, **deployment** (skipped: he has an existing deploy series; deployment costs money) [00:12:47–00:18:23].
- Use-case-diagram / actor framing: the MVP checklist ≈ a use-case analysis; actors (normal user vs admin; logged-in vs not deferred) [00:11:27].
- Anti-panic war story: real e-commerce platform (Magento, his past job) has **~100–200+ DB tables**; organized per-module like microservices; "hiểu được một cái bộ phận này, chúng ta có thể áp dụng cái tư duy đấy sang những bộ phận còn lại" [00:16:38–00:17:18].
- **Work order:** admin-first (client UI needs data) OR backend + fake data; he picks easy→hard: **user module first**, then vibe-code acceleration on later modules once the pattern is set [00:22:26–00:23:26].

### Environment setup pedagogy (Node)

- **Node = platform/environment, not a library or framework** — Microsoft-Word-runs-on-Windows analogy; "chúng ta không học về hệ điều hành" (we don't study the OS; we need it to run the tools we DO study) [00:37:08–00:38:27]. Node = JS runtime server-side; "browser" = the frontend environment.
- **LTS/EOL literacy:** LTS = long-term support (Ubuntu analogy); EOL ("End of Life", caption-garbled "and apply") = no more patches; **even-major = LTS convention**; "đừng bao giờ chọn cái version mới nhất" — never grab the newest, grab the newest LTS [00:39:05–00:40:51].
- On the live day nodejs.org showed a newer non-LTS (caption: "26.3.0") vs "latest LTS = Node 24" footnote [00:40:43–00:41:09].
- **Exact-version pin:** "Cài chính xác Note JS version 24" into the doc [00:43:22]; rationale = same-environment-as-video → fewest bugs; game-on-Windows-version analogy; "không phải lúc nào mới cũng là tốt" + "cứ chạy theo mới nhất thì không bao giờ đuổi kịp" [00:44:31–00:45:43]. Learn on a pinned version, upgrade after it runs clean.
- **nodejs.org/download/release/vX.Y.Z/ URL pattern taught:** swap the version segment in the URL; per-OS artifacts (MSI for Windows) [00:47:13–00:48:09]. Doc pins v24.14.0; on-camera he also shows swapping to 24.16.0 (the newer LTS patch that day — caption-derived).
- **Verify install:** `node -v`; npm arrives bundled — `npm -v` shows **npm 11 with Node 24** [00:48:29–00:54:37].
- **Multiple Node versions:** he runs 20/22/24 across series; **beginners: install exactly ONE version**; experienced: nvm (`nvm use 24.14.0` demoed) — nvm-sh repo (caption ~93K stars) is macOS/Linux; **Windows uses the separate nvm-windows project** (installer via GitHub Releases, next-next-next) [00:49:01–00:51:47].
- Terminal literacy sidebar: Windows 11 right-click Terminal; install "Windows Terminal" from Microsoft Store if missing; macOS `cd` into folder [00:41:56–00:42:59]. "Đây là cách các bạn dùng máy tính... không phải là lập trình đâu" [01:12:15].

### Docs-first-AI-second (ep-3's full statement — the most complete in the series)

- [00:33:04–00:35:15] Two framing reasons to init from official docs, not AI: (1) **canonical + newest** — "AI phụ thuộc data training... model được training với dữ liệu cũ"; docs guarantee latest; (2) **AI init costs tokens** — "nó tốn phần token của các bạn bởi vì nó cần phải init rất nhiều file... dùng qua API thì tốn kém không cần thiết"; **plus AI scaffolds are untested/multi-platform-unverified** — "không có điều gì đảm bảo... nó được test... chạy trên đa môi trường" (his Windows vs a student's macOS); official scaffolds are human-tested. Reprised at [01:02:41]: "Lý do đầu tiên... tốn token. Vấn đề thứ hai... source code này người ta test rồi."
- He notes he teaches the same principle in his Java Spring course [00:35:15].
- **Nuance new to ep-3:** students do NOT run create-vite themselves — after the video he uploads HIS init as a starter: "Download dự án init FE tại đây, KHÔNG tự coding phần này — để đảm bảo môi trường + source code giống hệt video, hạn chế bug" [01:05:50–01:06:28]. The on-camera init exists to teach the **thinking** for the students' own later projects [00:55:54–00:56:15]. So: docs-first for learning-to-fish; starter-download for course reproducibility.

### Frontend stack decisions (with reasons)

- **Vite** chosen: author lineage (Evan You, Vue creator; "cha đẻ của VueJS"), actively maintained (recent commits), **~81K GitHub stars (caption)**, multi-framework (vue/react/preact/svelte/solid); **selection heuristic taught: stars + recent-commit activity** [00:26:53–00:27:49]. Name = French "quick", pronounced /vit/ [00:35:29].
- **"Vite đầu quân cho Cloudflare"** — he recalls Vite/creator "joined Cloudflare", then sees a banner on vite.dev mid-live and takes it as confirmation [00:27:23, 00:36:33] (⚠️ see Corrections — verify workflow verdict).
- **CRA history:** create-react-app was Facebook's, he used it in his 2022 full-stack series ("4 năm rồi"), now unmaintained → don't use [00:28:05–00:28:29].
- **Vite version-compat teaching:** latest Vite 8 (8.0.16 caption) requires **Node ≥22**; his docs-version-dropdown demo shows an older Vite requiring 18/20 — the read-old-docs skill from ep-4 reprised on a second product [00:54:41–00:55:48].
- **No Tailwind for this course:** Tailwind = "mì ăn liền" (instant noodles) good for vibe coding, but a "cơn ác mộng" (nightmare) for beginners without CSS foundations [00:28:46–00:29:26]. **Tailwind economics story:** a post some months back — since ChatGPT, Tailwind downloads multiplied but maintainer revenue barely moved; "tốt cho AI nhưng với human... gây khó khăn cho beginner"; debate about Tailwind's future [00:29:34–00:30:11] (⚠️ verify). Vanilla CSS first; AntD (praised: "các bố Trung Quốc làm hơi bị ghê", great for admin) / shadcn / Chakra later — some of those pull Tailwind in anyway, which he doesn't want [00:30:25–00:30:47].
- **State:** React Context API only ("đơn giản, out of the box, đủ sức cho tác vụ đơn giản"); Redux/Zustand later — "cho dù dùng cái nào... quan trọng nhất chính là việc các bạn tư duy" [00:31:26–00:31:59].
- **Data fetching:** basic fetch; **no React Query** — its main value is caching, which confuses beginners; "mới bắt đầu thì cứ code cho nó chạy được cái đã" [00:32:03–00:32:40]. All skipped tools = future phases.
- Theme dark/light noted as a Tailwind out-of-the-box win he forgoes [00:31:12].

### create-vite demo (hands-on)

- `npm create vite` → **project-naming rules taught:** (1) no Vietnamese diacritics — foreign-authored tools prioritize English, diacritics break things; (2) no special chars (@, spaces...); hyphens over spaces; English names more meaningful [00:58:00–00:59:31]. Names it `frontend-react-hoi-it`-style (caption garbled).
- Framework: React → variant menu includes TypeScript options, **"React Compiler" variant (he picks the 2nd option — caption "script và reciler")**, React Router v7, TanStack, RedwoodSDK ("nói thật... mình cũng méo biết nó là gì" — honest ignorance modeled on camera) [00:59:33–01:00:56]. React Compiler explained: React-19-era, "React bây giờ nó chạy nhanh hơn" [00:59:48–01:00:19]; on-camera npm check: **React 19.2.7 latest** [01:00:02].
- Declines auto "install with npm and start now" to show manual steps [01:01:05].
- `cd` (tab-completion tip for beginners), `code .` opens VS Code [01:02:02–01:02:29].
- **package.json anatomy:** "xương sống dự án" (project spine); dependencies vs devDependencies (dev tooling vs production runtime; production build ships lean); scripts (`npm run dev`); metadata (name/private/author/homepage — adds his account + https://hoidanit.vn) [01:03:04–01:05:40].
- `npm i` (shorthand for install) [01:19:24]; **node_modules explained:** transitive deps "con cháu chút chít" — vite's own package.json pulls **lightningcss, rolldown** (caption "Ligh CSS... rollown") etc. [01:20:00–01:21:32]; never edit node_modules.
- **package-lock.json:** born at first install; pins exact versions + tree "ghi chính xác version... đảm bảo khi các bạn gõ lại npm i... version phần mềm sử dụng là giống nhau"; don't edit it, code against package.json [01:21:37–01:23:24].

### git + the version-pinning procedure (the ep-3 headline workflow)

Order as demonstrated:
1. `git init` — "dùng git để bảo vệ mã nguồn... cực kỳ quan trọng" [01:06:35–01:07:00]; git self-study pointers: his ~4-year-old YouTube git series + newer free series on hoidanit.vn [01:09:10–01:10:25].
2. `git add` + `git commit -m "init project"` — **baseline commit before any changes** [01:12:53].
3. VS Code Source Control as before/after review surface: "bên trái... before và bên phải... after"; **discard-changes as time machine** [01:13:11–01:13:50]. "Sau này khi mà các bạn dùng AI để vi coding ấy thì nó cũng hỗ trợ các bạn cái phần git này thôi. Nhưng mà mình sẽ làm thủ công để cho các bạn luyện tập" [01:10:53] — AI tools automate git, but learn it manually first.
4. **semver range literacy:** `^` = newest minor/patch, major fixed; `~` = patch-level; to pin EXACTLY, remove the range char — "chúng ta đóng đinh luôn cái version" [01:07:26–01:08:53]. (Caption garbles "semantic" as "Symmetric".)
5. **npm-check-updates:** `npm i -g npm-check-updates` (`-g` explained: machine-wide vs per-project) [01:14:01–01:16:18]; `ncu` lists newer versions (on camera: React 19.2.6→19.2.7; a "@types/node"-ish row showing 25; an eslint-ish package 8.59→8.61 — caption-derived) [01:16:21–01:16:50]; **strip `^` via Ctrl+H replace-all (17 occurrences) + strip `~`** [01:16:55–01:17:35]; `ncu -u` writes package.json ONLY (install still required) [01:17:56–01:18:28]; review the git diff of package.json [01:18:34–01:19:11]; then `npm i`.
6. Result: **exact-pinned, newest-at-record-date dependency set, reviewed through a git diff** — the mechanical procedure behind ep-4's pinning discipline.

### Run + HMR

- `npm run dev` → **Vite dev port 5173** ("ngày xưa 3000... 4173... đổi lên 5173" — caption-garbled sequence; see Corrections) [01:24:05–01:24:31].
- Ctrl+click on the localhost link unexpectedly opened inside VS Code (new VS Code version behavior — "version mới của phần IDE của mình thì nó như thế này"); he copies to Chrome manually [01:24:37–01:25:10].
- Edits `src/App.tsx` "Getting Started with hoi-it account", Ctrl+S → **hot reload without browser refresh** — "chúng ta coding tới đâu thì giao diện cập nhật tới đấy" [01:25:21–01:26:28].
- Episode ends: backend + database setup moved to next video; source pushed for download; "kể từ các video tiếp theo đấy chúng ta sẽ dựa vào cái source code này" [01:26:30–01:27:06].
- Student comment confirms stack: "react thì em nghĩ xài với TypeScript" — "Khóa này thì mình dùng với TypeScript mà" [01:27:13].

### Notable quotes (VN + EN)

- [00:08:40] "Câu chuyện liên quan về tiền... đây chính là cái yếu tố sống còn" — "It comes down to money... this is the survival factor" (why MVPs exist).
- [00:05:12] "Technical debt... nó giống như kiểu rằng là một quả bom nổ chậm" — "Technical debt is like a time bomb" (on vibe-coding 100K lines you don't understand).
- [00:15:32] "Bắt buộc các bạn sẽ cần phải đọc và chúng ta đánh giá... không thể... copy paste và tôi không phản biện" — "You must read and evaluate [AI output]... you can't just copy-paste without pushing back."
- [00:23:02] "Nó đang thiếu... trang quản lý user... Nếu mà không có user thì hệ thống này thì làm kiểu gì" — the on-camera catch of the AI's missing MVP item.
- [00:33:29] "Đọc tài liệu ở trên này... đảm bảo... các bạn đọc được cái tài liệu mới nhất" — docs guarantee freshness; AI training data may be stale.
- [00:34:01] "Nó sẽ tốn cái phần token của các bạn bởi vì nó cần phải init rất nhiều file" — AI project-init burns tokens on many files (the cost reason).
- [00:44:44] "Những cái mà các bạn nghĩ ngày hôm nay nó mới thì qua ngày mai nó là cũ rồi" — "What you think is new today is old tomorrow" (anti-latest-chasing).
- [01:08:49] "Chúng ta đóng đinh luôn cái version" — "We nail the version down" (the pinning verb).

### Caption garbles noted (main-loop read)

"Fend/FN/fan/forend"→frontend · "vít/vịt/VI/ví"→Vite · "gilus"→(likely Copilot; unreliable) · "T script/Tcript/Trip"→TypeScript · "script và reciler"→TypeScript + React Compiler (95%) · "Cloud Flir"→Cloudflare · "USKAS/usecate"→use case · "Juston"→Zustand · "SECO/SEO"→fetch (low confidence) · "backit/filbackit"→package.json · "backitlock/logon"→package-lock.json · "Ligh CSS"→lightningcss · "rollown"→rolldown · "Symmetric"→semantic (versioning) · "and apply"→End of Life · "NVMSH"→nvm-sh · "not/note/nots"→Node · "myql/máy SQL"→MySQL · "skyf"→scaffold(ed) · "Bantino"→Bun/Deno(?) · numeric strings (24.16.0 / 26.3.0 / 8.0.16 / 93K / 81K / 8.59→8.61 / port sequence) = caption-derived, verified separately.

### Copilot/AI-budget aside (⚠️ caption-unreliable segment [00:05:30–00:05:55])

He says he had NOT yet bought one AI tool ("gilus" garble — likely Copilot per course doc), "hôm trước thì thấy nó rẻ rẻ khoảng 15 đô" (~$15 — repeats the doc's contested figure verbally), that he currently uses **Claude Code the most (paying)**, pays for ChatGPT + Codex, and is now buying this one too. Consistent with ep-2's "Claude Code is best, Copilot+Gemini chosen for students" stance. The $15 figure remains REFUTED as Copilot Pro price ($10/mo, prior ship's verify); most plausibly conflates a credits allowance or Pro+ tier confusion.

## Verification outcome (wf_f3c7237f-4c4: 27 agents = 10 dives + 16 refute-first skeptics + critic; ~1.09M tokens, 471 calls)

**Confirmed (highlights):** Vite→Cloudflare = REAL ACQUISITION (Cloudflare acquired VoidZero 2026-06-04; vite.dev banner real; $1M ecosystem fund) · vite 8.0.16 latest at live date (8.1.0 next day) · Vite 81,727★ (caption "81K" exact) · create-vite `react-compiler-ts` = 2nd React variant; router options = customCommand menu entries · vite@8 deps rolldown + lightningcss (registry) · typescript-eslint 8.59/8.61 timeline exact · Node v24.14.0 + v24.16.0 + v26.3.0 all real; npm 11 w/ Node 24; even=LTS policy verbatim; Node 24 = Active LTS "Krypton" June 2026 · nvm 94,012★; nvm-windows coreybutler active · ncu behavior exact (latest 22.2.9, caption "21" stale) · semver ^/~ teaching exact per npm docs · package-lock purpose exact · npm→GitHub(2020)→Microsoft(2018) · Maven Central ✓ · shadcn REQUIRES Tailwind, AntD/Chakra do NOT · Tailwind story real but WORSE than told (Adam Wathan Jan-2026: revenue −80%, 75% eng layoffs, docs traffic −40%) · MVP = Robinson 2001/Ries 2011; validated-learning nuance absent · Magento 2.4.3 = 411 tables (his ~200 fits older era) · COD-VN 60–85% · live-Mon/VOD-Wed deterministic · exactly 4 vibe-coding courses on hoidanit.vn · "Git Zero" free course found.

**Overturned prior-ship discards:** "Vite acquired by Cloudflare" had been DISCARDED as garble in the ep-4 ship's digest pass — TRUE; "Vite 81K stars do-not-quote" — TRUE. Logged as the "discard-as-garble" misfire class.

**Main-loop overrides:** lightningcss-absent dive verdict (summarizer miss vs registry) · Node-26-"odd" parity error · Node-24-"Maintenance-LTS" phase error · critic's spurious "npm-security-check plugin" reference + redundant Copilot re-check.

<!-- compiled: 2026-07-04 -->

