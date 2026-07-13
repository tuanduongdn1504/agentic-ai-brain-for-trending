# GitHub import → AI Studio Build

## The headline feature (real, ~July 8 2026)

You point AI Studio Build at a GitHub repository instead of a blank prompt; it pulls the repo in, transforms it to a runtime-compatible form, builds it, and lets you keep iterating + deploy — no local clone, no terminal, no manual dependency install.

- **Google's own words** (via MarkTechPost quoting the launch): the importer *"will automagically take the repo and transform it into a format that is compatible with our runtime and then let you keep iterating on it in AI Studio, deploy it, and more."*
- **Launched ~July 8, 2026** as part of a Build-mode update batch (alongside [[design-variations|Design Variations]]). Confirmed by [MarkTechPost (Jul 9)](https://www.marktechpost.com/2026/07/09/google-ai-studio-adds-import-from-github/), [digg](https://digg.com/tech/zbx1iyi1), a [how-to guide](https://shaam.blog/articles/google-ai-studio-github-import-guide-2026), a sibling English video, **and the on-screen demo in the source video**.
- **Access model:** connect your GitHub account; import a repo your account can access (public or private). You can **"Commit and Push"** changes back to a new/existing branch.

## ⚠️ The docs-lag correction (why the verification agents got this wrong)

The refute-first agents (all Haiku 4.5) read the [official Build-mode docs](https://ai.google.dev/gemini-api/docs/aistudio-build-mode), which still say *"We do not currently support pulling remote changes"* and *"This functionality is not yet available,"* and concluded **the whole feature is vaporware (FALSE)**. That is wrong — the docs page simply **lagged a 6-day-old launch**, and the agents conflated two different things:

- **One-time IMPORT** of a repo → **real, shipped.** (What the video shows.)
- **Ongoing SYNC / re-pulling remote changes** after import → **genuinely not supported.**

Main-loop anchors (fresh journalism + the live demo) **override** the agent verdicts. See [[source-provenance]] for the full override record. *Lesson: on features <2 weeks old, first-party docs pages lag journalism and the product UI — verify against multiple current sources, not one doc snapshot.*

## The real limitation the video *does* gloss (keep this one)

- **No round-trip sync.** Import is a **one-time snapshot**. Once it's in AI Studio you iterate there and push *out* to GitHub; you **cannot re-pull upstream GitHub changes** back into the AI Studio project. So AI Studio and your Git history diverge the moment anyone edits either side.
- **Fork-first for third-party repos.** The video's "you must fork someone else's repo first" is *practically* true: to import + push back you need the repo under your account / with write access — hence forking. (Not a hard rule for repos you already own.) → grade ◐ in [[claims-scorecard]].
- **"Restructure to runtime format" is real but undisclosed.** Google confirms the transform; the *exact* mechanics (and private-repo behavior) were "unconfirmed at launch." Output is standard frameworks (React/Angular/**Next.js**, Node.js/npm), **not** a proprietary locked format — so the video's implied lock-in is overstated, but the one-way-sync divergence is the real portability cost.

## Why it matters for hireui (Next.js)

- **Tempting but incompatible with the constitution.** hireui is Next.js, so the importer *would* build it. But: (a) importing the real repo puts proprietary source through Google (trained-on unless a billing account is attached — [[pricing-privacy-data]]); (b) no round-trip sync fights **GitNexus-first + `agent-*` branches + CI/CD**; (c) AI-Studio-is-source-of-truth breaks the moment CI redeploys. → **prototyping only, on a sanitized/synthetic fork.** See pilot **A1/A2** and the fence **D1**.

## See also
[[_index]] · [[design-variations]] · [[cloud-run-deploy]] · [[pricing-privacy-data]] · [[source-provenance]]
