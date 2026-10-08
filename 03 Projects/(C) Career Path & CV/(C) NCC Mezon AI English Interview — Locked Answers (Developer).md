# NCC Plus — Mezon AI English Interview · Locked Answers (Developer)

**Format:** AI voice bot on **mezon.ai**. It's an **English proficiency test** framed as a developer interview → it scores **clear spoken English** as much as your technical content. Keep answers **simple, structured, and spoken slowly**.

> **Anti-fabrication:** every answer below is true to your real profile (5 yrs RN + Flutter, App Store apps, TalentAxis/Space360, PSM II, AI-first). **Two spots need YOUR real detail** — marked `[YOUR …]`. Don't invent numbers or events; a qualitative true answer beats a fake number.

---

## A. How to run the test (do this first so you're not fumbling)

1. Go to **mezon.ai**, create a meeting.
2. Username = your **application email**; authenticate with the **OTP** sent to that email.
3. **Invite the bot agent** to the room.
4. Type **`*start`** → select **`[1] Developer Interview`**.
5. Turn on your **microphone**, say **"ready"**.
6. Answer each question out loud. If something breaks, type **`*cancel`** to restart.
7. At the end the bot says "Congratulation…" → **click the robot icon** to remove the bot and finish.

**Voice-test survival rules:**
- **Start speaking within ~2 seconds** — silence >4–5s makes it auto-advance. If you need a beat, say a bridge out loud: *"That's a good question — let me explain."*
- **Speak slowly and clearly**, quiet room, mic close. Loud and clear beats fast and fancy.
- **Keep each answer 30–60 seconds.** Structure: one-sentence answer → 2–3 supporting sentences → done. Don't ramble.
- **Simple sentences win.** Short clear English scores higher than long clauses you trip on.
- It repeats a question max twice — if unsure, **answer what you understood**; don't freeze.

---

## B. Locked answers *(rehearse these out loud 2–3 times)*

### 1. "Tell me about yourself." *(your anchor — memorize this one)*
> "Hi, my name is Tuan. I'm a mobile engineer with **five years of experience**, based in Da Nang. I mainly build cross-platform apps with **React Native**, and I also work with **Flutter**. I've shipped several apps to the **App Store and Google Play** — for example **TalentAxis**, a recruitment app, and **Space360**, a property-management app. I own the mobile side end to end — from the UI, to the API integration, to the release. I'm also a certified **Scrum Master**, so I care about teamwork and delivering on time. And I use AI tools like **Claude** every day to work faster, while I keep the code review and testing in my own hands. I'm interested in this role because it's a **mid-to-senior mobile position** where I can also help lead a small team."

### 2. "Walk me through a project you built."
> "One project is **TalentAxis**, a recruitment app. I built the mobile client with **React Native** and Expo, and I integrated it with a **microservices backend** built in Django and FastAPI. I handled the API integration, the app's screens, and the release to the App Store. I also added **live streaming** using NodeMedia and **over-the-air updates**. The biggest challenge was keeping the app stable while integrating many services, so I focused on good error handling and testing. In the end we shipped it to real users on the App Store."

### 3. "React Native vs Flutter — what's the difference?"
> "Both are cross-platform frameworks. **React Native** uses **JavaScript and React**, and renders to native components through a bridge. **Flutter** uses **Dart** and draws its own UI with its own rendering engine, so it looks the same on every device. I've used **both in production**, so I can work with whichever a project needs. I choose based on the team and the project requirements."

### 4. "How do you manage state?"
> "It depends on how complex the state is. For **React Native**, I use **Redux** for large shared state, and lighter tools like **Zustand** and **React Query** for server data. In **Flutter**, I've used **GetX** and **Bloc**. For simple local UI state, I keep it in the component. The rule I follow is: use the simplest tool that fits — don't add Redux if local state is enough."

### 5. "How do you work with APIs / REST?"
> "I use a **central API client** and send the auth token in the header, usually a **JWT**. I always handle the **loading, error, and empty states**, and I use **React Query** for caching and automatic retries. At TalentAxis I integrated against a **microservices backend**, so I dealt with multiple services and authentication across them."

### 6. "How do you handle asynchronous programming?"
> "In **React Native** it's **Promises and async-await**. In **Flutter** it's **Futures and Streams**. The most important rule is to **never block the UI thread** — I do the heavy work or the network call in the background, and update the UI only when the result is ready. For streams of data, like live updates, I use Streams in Flutter or observables in React Native."

### 7. "How do push notifications work?" *(study this most — it's your newest area)*
> "First the app registers and gets a **device token**. It sends that token to the **backend**, which stores it. When the backend wants to notify the user, it sends a message through **Firebase Cloud Messaging**, and on iOS that goes through **APNs**. On the device, I handle **three cases** — when the app is in the **foreground**, in the **background**, and when it's **closed**. I also use the notification to **deep-link** the user into the correct screen."

### 8. "How do you store data locally?"
> "For small data like settings, I use **key-value storage**. For structured data, I use **SQLite**. And for secrets like auth tokens, I use the **Keychain on iOS and Keystore on Android** — never plain storage, for security. For offline support, I keep the local database as the source of truth and sync with the server when the connection comes back."

### 9. "Tell me about a hard bug or technical challenge." *(the crash story — locked, qualitative)*
> "In one project, I joined an app that was **crashing often**. I reproduced the crashes, then I read the **stack traces** to find the **root cause**, instead of just patching the symptom. I fixed the underlying problem and added tests so it wouldn't happen again. After that, the **crash rate dropped significantly and the app became stable**."

> *Intentionally no percentage — this is the honest version. It's a complete answer on its own; don't invent a number if the bot asks "how much."*

### 10. "Tell me about teamwork or leading a team." *(your strength — say it confidently)*
> "I'm a certified **Scrum Master, level PSM II**. At Enouvo, I was the **Scrum Master for an innovation team** — I ran the ceremonies, **removed blockers**, and coached the team together with the product owner. I also ran an **internship and mentoring program**, so I recruited and trained junior engineers. So I'm comfortable **leading a small team**, unblocking people, and making technical decisions — which fits the team-lead part of this role."

### 11. "Tell me about a disagreement or conflict in a team." *(the Daily Scrum coaching story — locked)*
> "As a Scrum Master, I once had a **team member who often skipped the Daily Stand-up**. First, I talked to him **privately** to understand the reason. He said he had **no impediments**, so he wanted to save the time for his own work. I explained that the Daily Stand-up is **not only about him — it's about the whole team**. Even when he has no problem, another teammate might, and he could be the person who **helps them**. The Stand-up gives the team **transparency** — what we did yesterday, what we do today, and where we are blocked. In Scrum, we **rise together and we fail together** — we own the work as a team. So I **coached him to see the value, not just the rule**, and after that he started joining again and contributing. When someone disengages, my approach is **coaching, not forcing**."

> *If the bot pushes — "what if he still refuses?" — say: "If coaching doesn't work, I make the impact visible to the team, and involve the manager if I really need to — but I always start with understanding and coaching first."*

### 12. "What are your strengths and weaknesses?"
> **Strength:** "My strength is that I **deliver end to end** — I don't just write screens, I take an app all the way to the App Store, and I lead delivery as a Scrum Master. And I work with **both React Native and Flutter**, so I'm flexible."
> **Weakness (honest + a plan):** "My deepest experience is **cross-platform**, so **native Kotlin and Swift** are areas I'm still growing. I've worked with Swift foundations and native modules, and I'm improving. And I'm actively practicing my **spoken English** so I can communicate better with international clients."

### 13. "Why do you want to join NCC / work remotely?"
> "NCC works with **international clients** on many kinds of projects, so I would grow a lot and use both React Native and Flutter. I'm looking for a **mid-to-senior role** where I can also **lead and mentor**, which matches my Scrum Master background. And I'm **experienced with remote work** — as a Scrum Master I communicate clearly and asynchronously, and I deliver on time without close supervision."

### 14. "How do you use AI tools in your work?"
> "I use **Claude Code and AI assistants every day** for faster coding — like a pair programmer. But I keep the **code review, the tests, and the security decisions in my own hands**. The AI helps me move faster, but I stay responsible for the quality. I think that's the right way to use AI as an engineer."

### 15. "Do you have any questions for us?" *(always have 2 ready)*
> - "For this role, do teams use **Flutter, React Native, or native** — and does it change by client project?"
> - "How big is the team I would help lead, and how much **direct client communication** is involved?"
> - "How is the **fully-remote** work structured with international clients?"

---

## C. English delivery tips *(this test scores your English)*

- **Speak slowly.** Pause between sentences, not in the middle of them.
- **Use simple connectors:** *first / then / after that / because / for example / in the end / so.*
- **Start every answer with a direct one-liner**, then explain. ("I manage state based on complexity. For React Native, I use…")
- **Avoid dead air** — if you need to think, say a bridge: *"That's a good question, let me explain…"* (keeps the 4–5s timer from cutting you off).
- **If you don't understand a word**, it's fine to say: *"Could you repeat the question, please?"* (it repeats up to twice) — that itself is good English.
- **Numbers and names you'll say a lot:** React Native, Flutter, JavaScript, Dart, Redux, Firebase Cloud Messaging, APNs, Scrum Master, TalentAxis, Space360 — practice saying them clearly.
- **End answers cleanly** — finish with a short closing so the bot knows you're done: *"…and that's how I handle it."*

---

## D. 15-minute warm-up before you press `*start`

- [ ] Read answers **1, 2, 9, 10, 13** out loud twice (intro, project, crash, leadership, why-NCC — the most likely).
- [ ] Read answers **9 (crash bug)** and **11 (Daily Scrum coaching)** out loud — both are locked now.
- [ ] Do a **mic check** in a quiet room.
- [ ] Practice your **self-intro (§1)** once more — a strong start sets the tone.
- [ ] Have answer **§15 questions** ready for the end.

---

*✅ Fully locked — all 15 answers are finished and true to your profile. §9 (crash) is honest and qualitative; §11 (Daily Scrum coaching) is your real Scrum-Master approach, tightened for speaking. Now just rehearse out loud and run `*start`.*
