# NCC Plus — Mezon AI English Interview · Upgraded RN-Forward Script (v2)

> **Supersedes v1** ("Locked Answers"). v1 was ~85% Scrum Master; this v2 **leads with React Native engineering** (the role) and keeps your Scrum depth as a **team-lead differentiator**. Built from **your real stories** — the D-U-N-S company-account setup, the Space360 Apple rejection + account-deletion fix, the `visionos`/CocoaPods build fight, and your two agentic-AI repos. Everything is **qualitative** (no invented numbers).

> **It's an English test** (a "[1] Developer Interview" that scores spoken English about your experience). So these are **experience stories told clearly**, not algorithm puzzles. Speak them slowly.

---

## Legend & voice-test rules

- **/** = short pause (comma) · **//** = full stop — **breathe** · **bold** = stress this word.
- **Start within ~2 seconds** — silence >4–5s auto-advances the bot. If you need to think, say: *"That's a good question — let me explain."*
- **Slow + clear beats fast + fancy.** The pauses are also **accent aids** — they give you time to land the final consonants (see Part 5).
- Keep each answer **30–60 seconds**. One-line answer → 2–3 support sentences → stop.
- **Run-the-test steps** are in the v1 file (mezon.ai → OTP → invite bot → `*start` → `[1]` → "ready"). Keep that open too.

---

# PART 1 — CORE (rehearse these first: RN engineering + AI)

### 1. "Tell me about yourself." *(your anchor — memorize)*
> "Thanks for having me today! // My name is **Tuan**. // I'm a **mobile engineer** with **five years** of hands-on experience, / based in **Da Nang**. //
> My core depth is **production React Native** — / with both **Expo** and **bare** workflows / — and I also have **Flutter** experience. // Right now I'm the **Mobile Leader** at CVTOT, / where I own the React Native side **end-to-end** / — from the UI, / to the API integration, / to the **release** on the App Store. //
> Earlier in my career, / I made a **deliberate move** to deepen my process skills / — I took a dual role in **Learning and Development** and as a **Scrum Master**, / and earned my **PSM Two** certification. // Mastering **Scrum** and **Kanban** gave me a real understanding of **team dynamics** and **delivery** / — which made me a **stronger engineer** when I came back to building. //
> And recently I've gone deep on **agentic AI** — / I use **Claude Code** every day to ship clean code faster, / while I keep the **review**, **testing**, and **security** in my own hands. //
> So what I bring is a **rare combination**: / hands-on **React Native** engineering, / the **process awareness** of a Scrum Master, / and an **AI-augmented** workflow. // I'm excited about this **senior React Native** role / where I can both **build** / and **help lead**. //"

*(Fix applied: your "interests shifted" line is gone — the Scrum period now reads as an intentional upgrade that made you a better engineer, not boredom.)*

### 2. "Walk me through an app you built." *(TalentAxis + Space360 — real)*
> "Sure. // At CVTOT I own the mobile side of two products that are **live on the stores**. //
> The first is **TalentAxis**, / a **recruitment app**. // I built the client with **React Native** and **Expo**, / and integrated it with a **microservices** backend / built in **Django** and **FastAPI**. // I owned the screens, / the **API integration** across several services, / and the **release** to the App Store. //
> The second is **Space360**, / a **property-management app**. // Same role / — the React Native client, / in a **monorepo** with a **Supabase** backend, / shipped to **both** the App Store **and** Google Play. // I also added **live streaming** with NodeMedia / and **over-the-air updates** with Stallion. //
> So I don't just build screens / — I take a product **all the way to real users**, / and keep it running. //"

### 3. "Tell me about a difficult technical problem you solved." *(the CocoaPods / visionOS native-build fix — #8)*
> "Yes. // One time, after a dependency upgrade, / my **iOS build** suddenly failed. // `pod install` threw an error about **`visionos`** / in a native library — **react-native-safe-area-context**. //
> Instead of guessing, / I traced the **root cause**. // It wasn't my app code / — it was a **toolchain version mismatch**: / my **CocoaPods** was too old to understand Apple's new **visionOS** platform, / and my **Homebrew** was also broken on a new macOS version. //
> So I fixed it **methodically** / — I updated CocoaPods, / cleaned up and re-linked Homebrew, / and reinstalled the problem native modules, / switching one library to the **Expo** version. // The build passed. //
> The lesson I always share with juniors: / on React Native, / **native build errors are usually a version or toolchain problem**, / not your app code. // And I used **AI** to diagnose it in minutes / instead of hours on StackOverflow. //"

### 4. "Tell me about a time something didn't go as planned." *(the Space360 App Store rejection + fix — #7)*
> "When I first submitted **Space360** to the App Store, / Apple **rejected** it. // Two reasons: / they needed clarity on our **business model**, / and they required an in-app **Account Deletion** feature / — under their guideline, / any app with sign-up **must** let users delete their account. //
> So I handled both. // I answered Apple's **business-model questions** clearly / — what's paid, / who the users are. // Then I **implemented account deletion**: / a **Delete Account** flow in the app / that removes the user's data in **Supabase** / and revokes the **Sign-in-with-Apple** token, / with a confirmation step / and a **screen recording** as proof for Apple. //
> It got **approved**. // And the best part / — I took those lessons into **TalentAxis**, / and it passed on the **first** submit. // I used **AI** to understand Apple's guidelines and implement the fix fast. //"

*(If asked "what does end-to-end ownership mean?" → the D-U-N-S story:)*
> "I even owned the **account setup**. // To get a **company** developer account, / Apple and Google both require a **D-U-N-S number** to verify the business / — a multi-day process through **Dun and Bradstreet**. // I researched the company's registration, / submitted the request, / and set up the **TestFlight** and **Google Play** testing pipelines, / including Google's rule of **twenty testers for fourteen days**. // So 'end-to-end' for me means / from the **build**, / to the **store account**, / to the **release**. //"

### 5. "How do you use AI in your work?" *(your differentiator — the two repos + the debugging pattern)*
> "I've gone **deep** on agentic AI. // I use **Claude Code** and custom **Claude Skills** every day / for pair programming. //
> I've also **built two open-source projects**. // One is an **agentic AI second brain** / — a knowledge system, / based on Karpathy's **LLM Wiki** pattern, / where an AI agent builds and maintains a structured wiki of **trending technology**. // It has over **fifty** documented entries and a pattern library. //
> The second is **Claude Agentic OS** / — a **local command center** for Claude Code, / built with **React**, **Vite**, and **FastAPI**, / with an **observability dashboard**, / cost tracking, / and a task queue. //
> And in daily work, / like that build error and the Apple rejection, / I use AI to **diagnose and fix hard problems fast**. // But the rule I follow is: / **AI helps me move faster** / — I stay **responsible** for the review, / the tests, / and the security. //"

### 6. "Tell me about a bug you're proud of fixing." *(the crash story — qualitative, from your CV)*
> "Early in my career / I joined an app that was **crashing often**. // I **reproduced** the crashes, / read the **stack traces** to find the **root cause** / — instead of just patching the symptom / — fixed the underlying problem, / and added tests so it wouldn't come back. // After that, / the **crash rate dropped significantly** / and the app became **stable**. // Finding the real root cause, / not a quick band-aid, / is how I like to work. //"

---

# PART 2 — RN technical talking points *(backup — short, only if the bot goes technical)*

Keep these **20–30 seconds**. Answer the one-liner, give one example, stop.

- **State management:** "I choose by complexity. // For **React Native** I use **Redux** for large shared state, / and **Zustand** and **React Query** for lighter and server data. // In **Flutter** I've used **GetX**. // The rule: / use the **simplest** tool that fits. //"
- **Performance:** "I watch for **unnecessary re-renders** / — I use memoization and stable keys, / and **lazy lists** like FlatList for long data. // On a TV or low-end device, / list rendering and images matter most. //"
- **API integration:** "A **central API client**, / auth token in the header — usually **JWT** — / and I always handle **loading, error, and empty** states. // I've integrated against **microservices** in production. //"
- **Async:** "In React Native it's **Promises** and **async-await**; / in Flutter, **Futures** and **Streams**. // The key rule: / **never block the UI thread**. //"
- **Testing:** "I use **React Native Testing Library** and **Jest**, / and Flutter Test on the Flutter side. // I test the important logic, / not everything for the sake of coverage. //"
- **Push notifications / offline** *(concept — be honest):* "The app gets a **device token**, / sends it to the backend, / which pushes through **Firebase** or **APNs** on iOS. // I handle **foreground, background, and closed** states. // I've used Firebase; / a large campaign system I'd ramp into. //"

---

# PART 3 — LEADERSHIP *(your differentiator — NCC wants a team-lead; keep it tight)*

### 7. "Tell me about your Scrum Master experience." *(upgraded — leads with the transformation + PSM II + real scale)*
> "As a **Scrum Master** at Enouvo, / I earned my **PSM Two** certification / and led **two cross-functional teams** / of **six to eight engineers** / through the shift **from waterfall to agile**. // With the **Innovation team**, / I helped them go from **resisting** the process / to **owning** it / — facilitating the ceremonies, / **removing impediments**, / and building trust through one-on-ones. // The real skill / isn't running the process / — it's **coaching people to own it**, / so the team becomes **self-organizing**. //"

> *Follow-up if asked to go deeper on leadership (the "lethal" line):* "The proof isn't the ceremonies / — I coached deeply enough to **elevate others**. // I mentored **another Scrum Master**, / and coached a **colleague to their own PSM Two**. // When your team produces **new leaders**, / the mindset has truly taken hold. //"

> ⚠️ Be ready to speak to **both teams** + one before/after if probed ("what was the resistance, what changed?"). The numbers only help if the story behind them is ready.

### 8. "Why are you a good Scrum Master? / Your greatest strength?" *(upgraded)*
> "I lead through **trust and coaching**, / not process enforcement. // I build enough **psychological safety** / that people bring me the **real** problems, / and I focus on making the team **self-organizing** / — so it runs well **even when I'm not in the room**. // For me, / a Scrum Master **succeeds** / when the team **doesn't need** them day-to-day. //"

### 9. "A team member skips the Daily Scrum — what do you do?" *(your locked coaching story)*
> "First / I'd talk to the person **privately** to understand why. // Say they tell me they have **no impediments**, / so they want to save the time. // I'd explain the Daily Stand-up is **not only about them** / — it's about the **team**. // Even with no problem of their own, / a teammate might have one, / and they could be the person who **helps**. // It gives everyone **transparency** / — what we did, / what we're doing, / where we're blocked. // In Scrum, / we **rise together and fail together**. // So I **coach** them to see the value, / not force the rule. // My approach is **coaching, not forcing**. //"

### 10. "Why should we hire you?" *(rebalanced — engineering first)*
> "Because I bring a **combination** you don't see often. // I'm a **hands-on React Native engineer** / who ships real apps to the store, / **end-to-end**. // I have the **process discipline** of a Scrum Master, / so I can also **lead and mentor** a small team. // And I work in an **AI-augmented** way / that makes delivery **fast and reliable**, / without losing quality. // For a **mid-to-senior** mobile role that includes leading, / that mix makes me a strong fit. //"

---

# PART 4 — CLOSERS

### 11. "Why NCC / why remote?"
> "NCC works with **international clients** on many kinds of projects, / so I'd use **both React Native and Flutter** and keep growing. // I want a **senior role** where I can **build and also lead** / — which matches my background. // And I'm **experienced with remote work** / — as a Scrum Master I communicate **clearly** and **asynchronously**, / and I deliver **on time** without close supervision. //"

### 12. "Do you have questions for us?" *(always have 2 ready)*
> - "Do teams use **React Native, Flutter, or native** / — and does it change by client project?"
> - "How big is the team I'd help lead, / and how much **client communication** is involved?"
> - "How is **fully-remote** structured with international clients?"

---

# PART 5 — Accent & pronunciation guide *(Vietnamese-English focus)*

> I can't hear your video, so this targets the **specific hard words in your script** + the **top Vietnamese-speaker English fixes**. Practicing these 10 minutes out loud will do more than any wording change.
>
> **⭐ Your personal, evidence-grounded trouble map** (from your own recording — in the separate "SM Intro" doc) is sharper than this generic list: your caption engine lost **"Scrum Master" → "drum matter"**, **"helped" → "hit"**, and systematically dropped final **`-s`** (plurals) and **`-ed`** (past tense). Those exact weak spots trip you in *this* script too — **drill them first**.

**The #1 fix — land your FINAL consonants.** Vietnamese drops word-endings; English scores you on them. Over-pronounce the ends of:
- **-t / -ct / -pt:** Reac**t**, produc**t**, tes**t**, buil**t**, projec**t**, shipp**ed** (say "shipp-**T**"), develop**ed** ("develop-**T**"), worked ("work-**T**").
- **-d:** deploye**d** ("deploy-**D**"), owne**d**, sol**d**, buil**d**.
- **-s (plurals / verbs):** app**s**, skill**s**, team**s**, year**s**, screen**s**, service**s**, crash**es**. Don't drop the -s.

**-ed endings have 3 sounds** — get these right:
- **/t/** after voiceless: ship**ped**, develop**ed**, work**ed**, fix**ed**, pass**ed**.
- **/d/** after voiced: deploy**ed**, own**ed**, learn**ed**.
- **/ɪd/** after t/d: integra**ted** ("integra-tid"), estima**ted**, documen**ted**.

**"th" (tongue between teeth)** — not "t"/"d"/"f":
- **the, three, both, with, thanks, month** → soft /θ/ or /ð/.
- **strength** is the hardest word in your script → **"strengkth"** (streng-th). Practice it slowly 5×.

**Word stress (English is stress-timed — don't say every syllable equally):**
- de-**VEL**-op-er · ex-**PER**-ience · re-spon-si-**BIL**-i-ty · **AR**-chi-tec-ture · tech-**NI**-cal · cer-ti-fi-**CA**-tion · col-**LAB**-o-rate · **IM**-ple-ment · a-**GEN**-tic · ob-serv-**A**-bil-i-ty · **MO**-bile.

**Tricky names in your script (say them cleanly):**
- **React Native** → "ree-**ACT** NAY-tiv" (land the "-ct"). · **Redux** → "REE-duhks". · **Zustand** → "TSOO-shtahnt" (or "ZOO-stand" is fine). · **GraphQL** → "graph-Q-L". · **Expo** → "EKS-po". · **CocoaPods** → "KO-ko-pods". · **Supabase** → "SOO-pa-base". · **Django** → "JANG-go" (silent D). · **Scrum** → "skruhm". · **Kanban** → "KAHN-bahn". · **impediment** → "im-**PED**-i-ment". · **Dun and Bradstreet** → "dun and BRAD-street".

**/r/ vs /l/** — keep them distinct: **R**eact / **r**elease / **r**eview vs **l**eader / **L**earning / **l**evel.

**The pacing rule that fixes most of it:** the **//** breaks in the script are your friend — **pause, breathe, and land the last sound of the previous phrase**. Rushing is what makes an accent hard to follow; slowing down makes even a strong accent clear. **Record yourself** reading answers 1–6 once, listen for **dropped final consonants**, and redo.

---

# PART 6 — APPENDIX: Deep Scrum Q&A *(kept for a possible human/technical-lead round — NOT for the English bot)*

*These are your original strong Scrum answers. The AI English test likely won't ask them, but keep them for a follow-up human interview. Trim each to ~45s if you use them live.*

- **Pushy PO adds a story mid-sprint** → "Taking new stories mid-sprint should be an **exception**, not a habit. // If it's genuinely high-priority, being agile means we can adapt / — but we loop in the **developers** to estimate, / and either **swap out** equal story points, / or, if it's too late in the sprint, / the PO gets **extra resources**. //"
- **New PO unfamiliar with Scrum** → coach them on the role (business value, owning the Product Backlog), Definition of Done / Ready, and INVEST for good user stories.
- **Retrospective techniques** → Sailboat · Mad-Sad-Glad · Start-Stop-Continue · Liked-Learned-Lacked-Longed-for · anonymous written notes. "I rotate them so the team stays engaged."
- **Spike vs Technical Debt** → a Spike is a time-boxed research story to reach an estimate; technical debt is a shortcut taken under deadline that needs refactoring later.
- **Good user story (INVEST)** → Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Improve a low-performing team** → use retrospectives to find the **root cause** first (estimation? capacity? defects? unplanned leave?), then fix that.
- **Biggest failure/success** → challenge = changing a waterfall-to-agile **mindset**; success = coaching teams to self-organize and a colleague to **PSM II**, plus a global remote team reaching the performing stage.

---

*✅ Ready to rehearse. Priority order: **1 (intro) → 2 (walk-through) → 3 (build fix) → 4 (Apple rejection) → 5 (AI) → 6 (crash)**, then 9 (Daily Scrum) and 10 (why hire). Do the accent warm-up (Part 5) on those. Everything is true to your real work and kept qualitative.*
