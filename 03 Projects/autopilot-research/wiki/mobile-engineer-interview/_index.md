# Mobile Engineer Interview — a verified study guide (React Native · React · Flutter)

**Five real Vietnamese mock/screening interviews for mobile & front-end engineer roles, turned into a fact-checked question bank. ~170 questions across 2 Flutter + 2 React/front-end + 1 React Native candidate — the study payload is the canonical answers + the recurring questions that break candidates, not any one candidate's (often wrong) answers. The corpus' SECOND interview topic and FIRST mobile/front-end interview topic.**

- **Source:** 5 private videos on the operator's own channel **Tuấn Dương** (interviewer), ~3h55m total, Vietnamese with embedded English tech terms. Candidates range from a 1-semester career-changer to a Play-Store-shipping RN dev. Hiring company appears to be **Innovo**. Full trail in [[source-provenance]].
- **Ingested:** 2026-08-06 (Path 5 — yt-dlp `--cookies-from-browser chrome`, both videos Private; no NotebookLM, no yt-search) · raw: `raw/2026-08-06-mobile-engineer-interview.md`
- **⚠️ Adversarially verified:** two Workflows — `wf_89de7c46-db7` (3/5) + `wf_2408264b-657` (2/5 recovery after a schema-truncation failure) — **13 agents** (5 per-video extractors → 5 refute-first per-video verifiers that re-read both transcripts; 2 failed-and-recovered) + Opus main-loop authorship (maker/checker). **~166 of 170 items verified faithful.** See [[claims-scorecard]].
- **⚠️ Doubly-garbled captions:** every technical term is a *reconstruction* from Vietnamese-original + auto-translated-English ASR (`Flashbox`→Flexbox, `Isaac`→Axios, `.abb`→`.aab`, `Fet 1`→`flex: 1`, `TD tag`→`<td>`). Raw captions are **not quotable**. Garble→term map in [[caveats-and-corrections]].
- **Corrections that matter:** Dart **const vs final** (one candidate had it backwards) · Flutter **StatefulWidget vs State-class lifecycle methods** · JS **call stack holds local variables, not the heap**. See [[caveats-and-corrections]].
- **Corpus second interview topic** (after [[nodejs-backend-interview/_index]]); same interviewer (Tuấn Dương). Grep-verified: first mobile/front-end interview topic.

## The one framing

**These interviews grade *foundations under pressure*, not vocabulary.** Tuấn's pattern across all five: broad concept → "why?" follow-up → live coding to expose the gap between *recognising* a thing and *using* it. Candidates who reason out loud and self-correct score higher than ones with confident-but-wrong recall. The junior candidates fail on the same handful of items every time — that list is the fastest thing to drill.

## Start here

- [[study-guide-and-gaps]] — **the questions asked in 3+ of 5 interviews + the ones that broke candidates**, ranked, each with a tight model answer + a drill. The fastest path to interview-ready.
- [[overview]] — the interviewer, the five candidates, the escalation arc, and how to use this topic.

## Topic articles (by domain)

- [[01-javascript-core]] — data types & primitives, `null` vs `undefined`, `==` vs `===`, higher-order functions, spread/rest, shallow vs deep copy, IIFE, ES6, string/array methods, TS vs JS.
- [[02-async-and-event-loop]] — Promises, async/await (built *on* Promises), the event loop + call stack + web APIs + micro/macrotask, Dart `Future`.
- [[03-react-and-hooks]] — Virtual DOM, JSX, hooks (useState/useEffect/useMemo/useCallback), the 3 dependency-array cases, lifecycle, SPA, CSR vs SSR, folder structure, UI libs, Vue vs React.
- [[04-flutter-and-dart]] — widgets, StatelessWidget vs StatefulWidget + the **real** lifecycle, Scaffold, Container vs SizedBox, **ListView-in-Column**, BuildContext, axis alignment, navigation, state management (BLoC/GetX/Provider), Dart types, **const vs final**, collections.
- [[05-react-native-and-mobile-deployment]] — RN + the **Android → Play Store** pipeline (keystore, SHA-256, `.aab`, review, Fastlane), HTTP clients (Axios vs fetch), REST vs GraphQL for mobile.
- [[06-css-html-and-web-fundamentals]] — Flexbox vs Grid (1D vs 2D), `flex: 1` shorthand, CSS `position` values, `<td>`, domain vs hosting.
- [[07-git-testing-and-engineering-practice]] — Git (commands, `checkout -b`/`-B`, **rebase vs merge**, `.gitignore`, merge conflicts done right, PRs, amend), testing stages/unit tests, clean code / SOLID / DRY, DevTools.
- [[08-behavioral-and-interview-craft]] — self-intro, strengths/weaknesses, career plans, teamwork & conflict, English self-rating, questions to ask — and how to answer Tuấn's scenarios (deadline clash, no-mentor job, group hiring).

## Appraisal

- [[claims-scorecard]] — per-video verification verdicts + the items that were flagged/corrected.
- [[caveats-and-corrections]] — the ASR-garble map, the technical corrections applied, the extraction-failure-and-recovery story, and the maker/checker overrides.
- [[hireui-relevance]] — interview prep (interviewee) + a ready-made mobile/front-end **screening rubric** (recruiter) + the ADR-safe product tie-in.
- [[source-provenance]] — sources, ingestion, and verification trail.

## Deliverable — portable interview cheatsheet

`output/(C) 2026-08-06-mobile-engineer-cheatsheet-handoff.md` — a self-contained cheatsheet another agent/session can consume: ranked question bank by stack (React/RN/Flutter/JS-core), crisp model answers, the gotcha list, and the verified corrections. Question-centric + anonymised (candidate names stay in the vault, not the portable artifact).

## Cross-links (corpus)

- [[nodejs-backend-interview/_index]] — the sibling interview topic (same interviewer, backend/Node); the CS-fundamentals + REST/GraphQL overlap.
- [[api-types/_index]] — the REST vs GraphQL taxonomy behind the RN/backend question.
- [[data-structures-16-in-32-min/_index]] — the DS/Big-O companion the junior candidates were missing.
- [[codesistency-mobile-app-course/_index]] · [[jasonlee-claude-mobile-app/_index]] — mobile-build siblings.
- [[hoidanit-fullstack-vibe-coding/_index]] — VN-language front-end/full-stack educator sibling.
- [[miai-cv-matching-agent/_index]] — the recruitment domain (the operator's product space).
