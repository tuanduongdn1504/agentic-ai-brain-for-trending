# Tech-stack rationale (NestJS · MySQL · React-not-Next)

## Source
- Video #4 tD0Uve-0Ltk (13:43 why NestJS, 59:55 database, 1:14:15 TS-vs-JS packages, 1:17:52 React docs) + course Google Doc

## The choices and stated reasons
- **One language across the stack:** TypeScript everywhere — "minimize time investment" for beginners covering both ends. (Doc-stated rationale.)
- **NestJS over raw Express:** Express is what NestJS uses underneath (Express 5 in Nest 11 — verified); Nest is chosen to *reduce boilerplate decisions* for learners while keeping the Express escape hatch (Fastify swap mentioned at 16:34).
- **MySQL over NoSQL:** the **90/10 claim** [1:06:27] — "~90% of the problems you'll meet are solved with SQL; the remaining 10% is where NoSQL earns its place." MongoDB named but deferred. Relational-first is framed as employability + problem-coverage, not fashion. (The 90/10 number is the instructor's empirical estimate — teaching heuristic, not a measured statistic.)
- **MySQL Workbench** as the GUI (official Oracle client, v8.0.47 current — verified; note: 2026 tool roundups increasingly point beginners at DBeaver/Beekeeper instead — competitor-adjacent sources, flagged in [[caveats-and-corrections]]).
- **React (pure) over Next.js:** framework-vs-library taught at the docs tour; react.dev's own recommendation (frameworks Next.js/React Router/Expo, or Vite/Parcel/RSbuild from scratch — verified) is *shown*, then deliberately overridden for pedagogy: foundations first ([[beginner-pedagogy-model]] "bicycle before big bike"). Series uses **Vite**.
- **Docker deferred** — named as the deployment-grade path, pushed to a future deploy series; beginners install MySQL natively.

## The AI-tool selection (ep 2 — the decision behind the doc's Copilot+Gemini line)
- Tools compared on stream: GitHub Copilot, Google Gemini, Codex/ChatGPT, Claude Code. **On camera: "Claude Code is currently the best" ("xịn sò con bò nhất") — with the fluidity disclaimer "next week it may change."** The series still picks **Copilot + Gemini**: *"chọn cái phổ biến, an toàn"* — popular + safe + findable documentation/mentorship beats best-in-class for beginners.
- **Antigravity 2.0 reviewed as disappointing** ("thất vọng") — dismissed as a Cursor clone despite Google's resources; Cursor recommended over it (a sharper first-party-practitioner verdict than most coverage in [[google-antigravity-skills/_index]]).
- Anti-tool-mystification rule: *"Đừng có quan trọng hóa việc tôi phải dùng công cụ này công cụ kia"* — any hinting+debugging IDE suffices for learning.
- **Next.js explicitly rejected** for this project as "spaghetti" (front/back logic mixing) — the ep-4 "React before Next.js" ladder is the pedagogy face of this ep-2 architecture verdict.
- Ep-3 frontend specifics: Vite (Evan You; CRA unmaintained), **vanilla CSS — no Tailwind for beginners** (AntD/shadcn/Chakra later), React Context over Redux/Zustand, Fetch over Axios/React-Query — every choice minimizes new-concept count per layer.

## Corpus placement
- The stack is deliberately **boring-by-design** — the opposite selection pressure from creator-economy content that optimizes for novelty; the same "boring tech for the parts that must not surprise you" instinct as [[self-hosted-devops-oss/_index]]'s displacement thesis and [[ai-engineering/_index]]'s production-first framing.
- The stated trade (fewer choices → more retention) is a **decision-budget** argument: beginners get exactly one new concept per layer.

## Key Takeaways
- Every stack choice is argued from *learner economics* (one language, one DB paradigm, one build tool), not from technical superiority claims.
- The 90/10 SQL/NoSQL split is a teaching heuristic offered as experience, and flagged as such here.
- The series shows the official recommendation (react.dev frameworks) and then explains *why it deviates* — modeling how to disagree with docs without ignoring them.
- Deferred complexity (Docker, NoSQL, Next.js) is named and scheduled, not hidden — a syllabus-level honesty pattern.
