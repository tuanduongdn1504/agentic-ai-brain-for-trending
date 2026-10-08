<!-- English interview-prep drill — Duong Van Tuan → Digital Unicorn (Mobile Developer RN, Middle/Senior, Da Nang, AI-first, FR/EN clients). 2026-07-13. GITIGNORED (interview-prep/, PII). Answers anchored in VERIFIED facts (see (C) Product Facts — proof points.md). [FILL] = your real specific; never invent. -->

# English Interview Drill — Digital Unicorn (React Native, Senior)

## How to practice (do this, in order)
1. **Memorize the self-intro + the "why" answer** (below) — they open ~every interview and are 100% predictable. Say each out loud 5×, then from memory.
2. **Rehearse the 3 stories** out loud in English (livestream / migration / AI-tools). Fill your real specifics first.
3. **Record yourself** on the self-intro + one story. Listen back once. Don't chase perfect — chase *clear + calm*.
4. **One mock** — ask me (I'll play the interviewer in English and drill follow-ups), or a friend.
5. **Say the "buy-time" phrases** (below) until they're automatic. They're your safety net.

> **Mindset:** English is your second language and that's fine. Don't apologize repeatedly. If useful, say it **once** at the start — *"English isn't my first language, so please tell me if you'd like me to clarify anything"* — then speak with confidence. Clear and slow beats fast and flustered.

---

## 1. Self-introduction (memorize — your opener) ~75 sec

> "Hi, I'm Tuan. I'm a React Native engineer based in Da Nang, with around seven years in mobile development and React Native since 2018.
>
> Right now I'm the React Native Leader at CVTOT, where I build and ship our products end to end. The two most recent are **TalentAxis**, a recruitment app, and **Space 360**, a property-management app. Both are **React Native and Expo**, shipped to the **App Store and Google Play**, with **in-app purchases** and **social login**. I own the full release cycle — build, store submission, over-the-air updates, and dependency migrations.
>
> I also work **AI-first**: I use **Claude Code** every day to build, review, and refactor. And I'm a **certified Scrum Master**, so I care about how the team ships, not only the code.
>
> What I'm looking for next is a **senior, hands-on role** where I can go deeper into **native** and work with a team that engineers AI-first — which is exactly why Digital Unicorn stood out to me."

*(Every fact here is verified. Practice until it's natural, not recited.)*

---

## 2. "Why leave CVTOT? / Why Digital Unicorn?" (memorize)

> "I've led the mobile team and shipped our own products, so I know how to own things end to end. What I want next is to go **deeper into native iOS and Android as a hands-on engineer**, and to work somewhere that's genuinely **AI-first** — where using tools like Claude Code is the normal way of building, not an experiment. Digital Unicorn does both: you build for international clients with React Native and native together, and AI tooling is part of how the team works. That's the environment I want to grow in."

---

## 3. Common technical questions — English answer-frames (anchored in your real stack)

> For each: 1–3 sentences. Where you see **[FILL]**, drop in a real detail. Signpost with "So…", "In my case…", "For example…".

- **"Expo vs bare React Native — when do you use each?"**
  > "I use **Expo** for most apps — it speeds up delivery, gives me OTA updates and managed native config. TalentAxis and Space 360 are both Expo. I go **bare** when I need custom native that Expo doesn't cover — for example the **live-streaming app at Song Anh**, where I used Stallion and NodeMedia for the native streaming layer."

- **"How do you handle a React Native or dependency upgrade?"**
  > "Incrementally, never big-bang. I map the breaking changes, upgrade in steps, fix the native side — iOS pods and Android gradle — test on real devices, and roll out safely with **Codepush/Stallion OTA** so I can roll back. [FILL: one real upgrade you drove.]"

- **"How do you debug a slow screen / RN performance?"**
  > "I profile first, don't guess. Common wins: optimize list rendering (`FlatList`, memoization), cut unnecessary re-renders, move animations to the native driver, and keep heavy work off the JS thread. [FILL: one real fix + roughly the impact.]"

- **"Over-the-air updates — how, and the risk?"**
  > "Codepush and Stallion. The main risk is shipping JS that's incompatible with the installed native binary, so I gate native-affecting changes to a store release and keep OTA for JS-only fixes, with rollback ready."

- **"State management — what and why?"**
  > "Redux or Zustand for app state, React Query for server state and caching. I pick the lightest thing that fits — Zustand for smaller apps, Redux when the team needs strict structure."

- **"How have you used Supabase?"**
  > "In Space 360 — Postgres database, auth including **social/SSO login**, and generated types. [FILL: one thing you built on it — realtime, RLS, edge function.]"

- **"Payments / in-app purchases?"**
  > "App Store in-app purchases in TalentAxis, and **VietQR** payment integration in Space 360. [FILL: one gotcha you handled — receipt validation, sandbox testing.]"

- **"Testing strategy?"**
  > "React Native Testing Library and unit tests for logic, plus real-device testing for the flows that matter. I'm comfortable picking up Vitest and Maestro — I've used Testing Library heavily; the tools transfer."

- **"Web + mobile parity in a monorepo?"**
  > "Space 360 is a **Turbo monorepo** — web and `apps/mobile` together. I keep route contracts and shared logic aligned across both, and I've done exactly this parity work — matching mobile routes to the web navigation contract."

- **"How do you use AI in your workflow?"** ← *their favorite — go concrete*
  > "I build **AI-first with Claude Code, every day** — writing features, reviewing diffs, and driving refactors and migrations. I also built a **code-analysis harness** that runs lint, typecheck, and web/mobile parity checks across the monorepo, and I use a code-intelligence tool (GitNexus) to check the blast radius before I change shared code. [FILL: one concrete thing AI let you ship faster or safer.]"

- **"Tell me about the microservices side."** *(if backend comes up)*
  > "TalentAxis runs on a microservices platform — Django and FastAPI services, Celery, MySQL, DynamoDB, Elasticsearch, all Dockerized. **I own the React Native client and its API integration** across those services; I'm not the backend author, but I work across the whole system daily." *(Honest boundary — don't claim you built the services.)*

---

## 4. Behavioral questions — English frames

- **"A hard bug you solved?"** → tell your **livestream** or **migration** STAR (§6). Signpost: *"So the situation was… what I did was… the result was…"*
- **"Disagreement with a teammate or PM?"** → *"As a Scrum Master I focus on the goal, not winning. I make the trade-off explicit — cost, risk, timeline — and let the team or PO decide with that in front of them. [FILL: one example.]"*
- **"How do you mentor juniors?"** → *"I've mentored junior mobile developers at Enouvo and now lead the mobile team at CVTOT — code reviews, pairing, and small clear tasks so people build confidence. [FILL: one example.]"*
- **"Describe leading the mobile team."** → *"At CVTOT I set the mobile architecture, review the work, and keep web/mobile parity — while still coding the hard parts myself."*

---

## 5. Phrases that save you (say these until automatic)

- **Buy time:** "That's a good question — let me think for a second." · "Let me give you some context first."
- **Structure a story:** "So, the situation was…" · "What I did was…" · "And the result was…"
- **Clarify:** "Do you mean X, or Y?" · "Just to make sure I understand the question…"
- **If you blank / mis-speak:** "Sorry, let me rephrase that." · "Let me start again." *(Totally normal — interviewers don't mind.)*
- **Check in:** "Does that answer your question?" · "I can go deeper if that's helpful."

---

## 6. Your 3 stories in English (fill your real specifics — see the HT Plus STAR file for the full scaffolds)

1. **Livestream** (RN + Stallion + NodeMedia) — the real problem you solved + the result. *Their-plus-adjacent + shows native depth.*
2. **RN / dependency migration** — a real upgrade, what broke in native, how you rolled out safely.
3. **AI-tools** (⭐ your edge here) — a concrete thing you built/shipped/reviewed with Claude Code (e.g. the code-analysis harness; a feature you shipped faster; a refactor). Not "I use AI a lot" — one specific, real example.

*(Full STAR+R structure + prompts: `interview-prep/(C) STAR Stories — HT Plus.md` — reuse stories 1 & 2, add the AI-tools one.)*

---

## 7. Questions to ask THEM (asking good questions in English signals seniority)

- "How is AI tooling like Claude Code actually used day-to-day on the team?"
- "Is the mobile stack Expo managed or bare, and what's the backend — Supabase, NestJS, something else?"
- "For French and English-speaking clients, what's the working language day-to-day, and how much client contact does the role have?"
- "What does growth look like for a senior React Native engineer here — toward native depth, architecture, or lead?"
- "How do the mobile and backend teams collaborate on a typical project?"

---

## 8. Tricky words — say them slowly (optional)
`dependency` (di-PEN-den-see) · `asynchronous` (ay-SINK-ro-nus) · `authentication` (aw-then-ti-KAY-shun) · `architecture` (AR-ki-tek-cher) · `migration` (my-GRAY-shun) · `Supabase` (SOO-pa-base) · `Expo` (EX-po) · `queue` (kyoo). When unsure, slow down — clarity wins.
