# Vite + React init workflow — tool selection, create-vite, and the starter-download policy

> Ep-3's hands-on half: how a docs-first instructor selects a build tool, scaffolds with it, and then tells students NOT to repeat the scaffold. Includes the episode's biggest verified surprise: the Vite→Cloudflare acquisition, 18 days old at air time, which the prior digest pass had wrongly discarded as caption garble.

## Source
- Video #3 osISSsyTJJ8, ~25:00–36:00 + 57:00–1:06 + 1:19–1:27 — raw: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`
- Ground truth via `wf_f3c7237f-4c4` + main-loop registry/GitHub checks

## Tool selection, as taught (all claims verified)
- **Vite** (French "quick", he says /vít/): by **Evan You** (Vue creator ✅), multi-framework, actively maintained. **Selection heuristic taught: GitHub stars + recent-commit activity** — on camera "81.000 star" → verified **81,727★**.
- **"Vite đầu quân cho Cloudflare"** — CONFIRMED, and fresher than it sounds: **Cloudflare acquired VoidZero on 2026-06-04** (press release; Evan You leads the team inside Cloudflare's ETI org; $1M Vite ecosystem fund; Vite ~130M weekly downloads per the announcement). The **vite.dev banner he noticed mid-live is real** ("Cloudflare supports Vite's mission"). He recalled an 18-day-old ecosystem event correctly on live TV — and hedged appropriately ("hay sao ấy"). ⚠️ The prior secondary-digest pass had DISCARDED this as garble — see [[caveats-and-corrections]].
- **CRA history:** create-react-app was Facebook's, powered his 2022 series, now unmaintained (sunset 2025-02-14, verified in the ep-4 ship) → dead tools get named, dated, and dropped.
- **Version-compat teaching:** Vite 8 (8.0.16 = latest at the live date, published 2026-06-01; 8.1.0 landed the day *after*) — he reads the Node requirement from the docs. Actual engines: `^20.19.0 || >=22.12.0` (his "minimum 22" is a simplification — the 20.19 branch also works; course uses Node 24, satisfied regardless). His docs-dropdown demo of an older Vite requiring "18 and 20" matches Vite 5/6 engines exactly. The read-old-docs skill from [[version-pinning-discipline]], reprised on a second product.

## What he deliberately does NOT install (with stated reasons)
- **No Tailwind**: "mì ăn liền" (instant noodles) — good for AI vibe-coding, a "cơn ác mộng" (nightmare) for beginners without CSS foundations. His economics story checks out **and is worse than he tells it**: Adam Wathan, Jan 2026 — *"Tailwind is growing faster than it ever has... and our revenue is down close to 80%"* + **75% of engineering laid off** + docs traffic −40% since early 2023 (AI codegen bypasses the docs where the paid products live). Vanilla CSS first.
- **UI kits later**: AntD praised ("các bố Trung Quốc làm hơi bị ghê") — and does NOT require Tailwind ✅; **shadcn/ui requires Tailwind** ✅ (his "some of these pull Tailwind in" is right for shadcn, wrong for Chakra — Chakra uses Emotion ✅).
- **No Redux/Zustand**: React Context API is enough for the MVP ("out of the box"); *"quan trọng nhất chính là việc các bạn tư duy."*
- **No React Query**: its main value = caching, which confuses beginners; "code cho nó chạy được cái đã." All cuts = future phases.

## The create-vite demo (verified against create-vite source)
1. `npm create vite` → **naming rules**: no Vietnamese diacritics, no special chars/spaces, hyphens, English preferred (foreign-authored tools assume ASCII).
2. Framework **React** → variant menu: he picks the **2nd option = "TypeScript + React Compiler"** (`react-compiler-ts` — literally 2nd in the FRAMEWORKS array ✅). React Compiler explained as "React 19-era, React runs faster" — acceptable simplification; precisely: stable Oct 2025, automatic memoization, defaults to React 19 but supports 17/18 with config.
3. Menu also shows **React Router v7 / TanStack / RedwoodSDK** — real menu entries, but implemented as `customCommand` hand-offs to external CLIs, NOT built-in templates (both skeptic lenses were right at different layers). His honest "mình cũng méo biết nó là gì" (no idea what that one is) is modeled ignorance — a senior admitting unknowns on camera.
4. Declines auto-install to show `cd` (tab-completion tip) + `code .` + manual `npm i`.
5. **package.json anatomy**: "xương sống dự án" (the project's spine) — dependencies vs devDependencies (dev tooling vs production runtime), scripts (`npm run dev`), metadata (adds his name + hoidanit.vn).
6. **node_modules**: transitive deps "con cháu chút chít" (children and great-grandchildren) — vite's own package.json pulls **rolldown 1.0.3 + lightningcss ^1.32.0** (registry-verified; caption "rollown/Ligh CSS" was accurate) — explains why the folder is huge and untouchable.
7. **package-lock.json**: born at first install; pins exact versions + tree so `npm i` reproduces the same substrate on every machine ✅ (npm docs); never hand-edit.
8. `npm run dev` → **port 5173** (dev; 4173 = preview; the caption's "3000 → 4173 → 5173" sequence is garbled — 3000 was CRA's port). Ctrl+S on App.tsx → **HMR without refresh** as the payoff demo.

## The starter-download policy (ep-3's docs-first nuance)
- After the video he uploads HIS scaffold; the doc says **"Download dự án init FE tại đây — KHÔNG tự coding phần này"** (download, don't re-scaffold) — to guarantee environment + source identical to the video, minimizing bugs.
- So the on-camera scaffold exists to teach the *thinking* ("cách các bạn tư duy cũng như cách chúng ta đọc tài liệu để chúng ta tự làm") for students' own future projects; course reproducibility rides on the frozen artifact. **Docs-first for learning-to-fish; starter-download for the cohort.**

## Key Takeaways
- Tool selection is taught as a checkable procedure: stars + commit-recency + who-maintains-it + who-owns-it-now — and it survived adversarial verification 5-for-5 (stars, acquisition, banner, versions, ports).
- The dead-tool story (CRA) and the live-acquisition story (Vite→Cloudflare) bracket the same lesson: maintenance status is a first-class selection criterion, checked at decision time.
- The not-installed list is the curriculum: every omitted tool gets a reason + a phase where it may return — deferral with reasons, cf. [[mvp-scoping-method]].
- Tailwind's Jan-2026 crisis (usage ↑, revenue −80%, docs traffic −40%) is the sharpest corpus datum yet for the **AI-breaks-docs-funded-OSS** loop — connects to [[google-zero-open-web/_index]] (same mechanism, package-ecosystem edition).
- Cross-links: [[docs-first-ai-second]], [[frontend-env-setup-workflow]], [[version-pinning-procedure]], [[tech-stack-rationale]].
