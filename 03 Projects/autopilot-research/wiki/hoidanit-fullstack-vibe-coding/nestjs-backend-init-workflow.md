# NestJS backend init workflow (as demonstrated, versions verified)

## Source
- Video #4 tD0Uve-0Ltk 10:47–59:55; course Google Doc (verbatim commands)

## The workflow
1. **Pin + install the CLI:** `npm i -g @nestjs/cli@11.0.23` → verify with `npm list --global --depth=0`
   - ✅ verified: 11.0.23 is not just real — it is the **current npm `latest` dist-tag** for `@nestjs/cli` (registry, 2026-07-04; 12.0.0-alpha.6 exists on `next`). The doc's "pin" today equals latest — the pin is for *cohort reproducibility over time*, not conservatism.
2. **Scaffold:** `nest new backend-nestjs-hoi-it` — package manager npm (yarn/pnpm mentioned as "after you get tired of npm"), ESLint + Prettier yes.
3. **Script convention:** align backend dev script with the frontend's `npm run dev` (watch mode / hot reload) vs `npm run start`.
4. **Install deps** → a ~22-package vulnerability warning appears → triaged as ignorable in learning context (see [[error-triage-and-warning-literacy]]).
5. **First run fails — TypeScript compile error** (chapter 43:00). Error pasted into AI (captions ≈ Claude Code); several iterations (baseUrl/dist red herrings); resolution lands on **version pinning** (project TS 5.9.3). Caption numbers cross-contaminate TypeScript/ESLint here — see [[caveats-and-corrections]].
6. **Hello World** at `http://localhost:3000/` (`src/app.service.ts` → `getHello()`); port-3000 conflicts debugged with TCPView on Windows.
7. **tsconfig warning explained:** VS Code-bundled TypeScript (6.0.x) ≠ project TypeScript (5.9.3) → UI-level mismatch, not a build error. *"Không phải máy của chúng ta lỗi đâu — do phần mềm nó bị vênh version thôi"* (57:08).
8. **Database:** MySQL + MySQL Workbench, root account, `localhost:3306` (PostgreSQL 5432 named as the alternative; MongoDB explicitly deferred; Docker deferred to a future deploy series).

## Verified version facts (refute-first workflow `wf_b1314fa6-590` + main-loop fetches)
| Claim (video/doc) | Ground truth | Verdict |
|---|---|---|
| NestJS 11 current | nestjs/nest latest v11.1.27 (2026-06-15); no stable v12 | ✅ |
| NestJS 11 needs Node ≥ 20 | `engines: >=20` in nest package.json + migration guide | ✅ |
| Express 5 default | platform-express deps express 5.2.1 | ✅ |
| Node 24 ("cài chính xác v24.14.0") | release dir HTTP 200; Node 24 = LTS line | ✅ |
| @nestjs/cli@11.0.23 | = npm `latest` | ✅ |
| TS 5.9.3 project / VS Code TS 6.0.x | both real (6.0.2 stable 2026-03-23, 6.0.3 2026-04-16); mismatch scenario documented VS Code behavior | ✅ plausible |
| React 19 (19.0→19.2) | 19.2.7 latest; 19.0 GA 2024-12-05 | ✅ |
| Playwright "63M/wk" | ~62M/wk (Snyk) | ✅ ±1.6% |

## Key Takeaways
- The whole init path is doc-verbatim + version-pinned — reproducible by a cohort months later even as `latest` moves ([[docs-first-ai-second]] in practice).
- The only AI involvement in the init is *error recovery*, and it's shown taking several iterations — the honest cost of AI debugging.
- Editor-vs-project TypeScript mismatch is taught as a *layers* lesson (which TS compiles your code vs which TS lints your editor) — unusually good beginner mental-model building.
- Every checkable number in this episode checked out; for a beginner-tier source that is the corpus exception, not the rule (cf. [[caveats-and-corrections]] for the one doc-level miss).
