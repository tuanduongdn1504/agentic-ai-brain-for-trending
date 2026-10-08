<!-- Interview prep — Duong Van Tuan → HT Plus, React Native Mobile Developer. 2026-07-13. GITIGNORED (interview-prep/, PII once filled). SCAFFOLDS — fill with your REAL specifics; the [bracketed] parts are yours. Examples show the SHAPE only — do NOT use them as facts. -->

# STAR+R Interview Stories — HT Plus (React Native Mobile Developer)

## How to use this

- **STAR+R** = Situation · Task · Action · Result · **Reflection**. career-ops's rule: juniors describe *what happened*; seniors *extract the lesson*. You're a Leader — **lean into the Reflection**; it's your edge even for a mid role.
- **Aim ~250–400 words / ~2 minutes spoken** per story. Tell it, don't recite.
- **You WILL get follow-ups** ("which RN version? what latency exactly? what broke in the pods?"). Only claim what you can defend from real memory. **A fabricated detail collapses on the first probe** — that's why the specifics below are `[yours to fill]`, not mine to invent.
- **Surface the Native angle in both** — HT Plus wants Native + RN. Both stories have a natural native hook (below). Use it: it's the whole reason you're a fit + what you want to grow.

---

## Story 1 — The Livestream problem (their #1 "plus")

**Why this one wins:** Livestream is the *only* domain-specific plus in the JD, and few candidates have it. It proves deep React Native **and** the real-time/native edge (camera, encoder, RTMP, device quirks). Lead your technical answers with this.

**Native hook to surface:** livestream almost always touches native — the camera/encoder, an RTMP/HLS native module, hardware/codec behavior, background/foreground handling. Name where you worked below the JS layer.

**Fill this in (your real Song Anh livestream work — RN + Stallion + NodeMedia):**

- **S — Situation:** What was actually hard/broken? *[Pick your real one: e.g. streams froze/dropped on weak 3G-4G · high latency between broadcaster and viewers · reconnection after network switch · a native camera/encoder integration · crashes on specific Android devices · battery/CPU under long streams.]*
- **T — Task:** What were *you* specifically on the hook for? *[your ownership — as engineer/lead of the streaming layer]*
- **A — Action:** What did you *do*, technically? *[the real decisions — e.g. Stallion buffering config · NodeMedia RTMP settings · auto-reconnect with backoff · a native module bridge for the encoder · adaptive bitrate · testing on real devices. THIS is the meat — be concrete + name the native part.]*
- **R — Result:** What changed, ideally with a number? *[e.g. cut freeze rate from X→Y · reconnection recovered Z% of dropped sessions · supported N concurrent viewers · stable over M-minute streams. If you don't have the exact number, give the honest direction: "noticeably fewer drop-offs / support calls."]*
- **R — Reflection:** The lesson (senior signal). *[e.g. "real-time mobile lives on the network + native edge, not the JS layer, so I now design the reconnection/degradation path first" — your real takeaway.]*

**Shape example (REPLACE every specific — this is NOT your story, just the rhythm):**
> _"Our livestream app kept freezing for viewers on unstable mobile networks; they'd have to kill the app and rejoin. I owned the React Native streaming layer. I traced it to [X], reworked the [Stallion/NodeMedia] reconnection to [auto-retry with backoff], and bridged [a native module] so the encoder [did Y]. After that, [Z% of dropped sessions recovered without a restart]. The lesson: I now design the degradation path before the happy path for anything real-time."_

**Likely follow-ups — be ready:** Which library did the heavy lifting, Stallion or NodeMedia, and why? · RTMP or HLS, and the trade-off? · What did you have to drop to native and why couldn't it stay in JS? · How did you test it on real networks/devices? · What's still not solved?

---

## Story 2 — A version / dependency migration (their required skill)

**Why this one wins:** The JD *requires* "fix version/outdate — libraries, dependencies, build environment" and lists RN/dependency migration as a plus. This is bread-and-butter for the role — they need someone who keeps the app shippable. It also proves **native competence** (RN upgrades break iOS pods + Android gradle + native modules).

**Native hook to surface:** an RN version bump is where you *live* in native — CocoaPods, Xcode/build settings, Android gradle/SDK, native module compatibility. That's your Native evidence in disguise.

**Fill this in (your real RN/dependency upgrade — you do Codepush/Stallion OTA + version work):**

- **S — Situation:** Which migration, and what forced it? *[your real one: e.g. stuck on an old RN version · a security/CVE patch · a deprecated library · a new iOS/Android OS or Xcode/SDK requirement · a broken CI build.]*
- **T — Task:** Your ownership + the risk (a production app, a team depending on it).
- **A — Action:** *[the real path — mapped breaking changes · upgraded incrementally vs big-bang · fixed the native side (pods/gradle/native modules) · resolved conflicts · tested across devices · used Codepush/Stallion for a safe rollout with rollback ready · CI with Jenkins/SonarQube.]*
- **R — Result:** *[app back to shippable · zero/known regressions · build restored · crash-free maintained · delivered on time · unblocked the team.]*
- **R — Reflection:** *[e.g. "I keep dependencies current on a cadence now instead of a scary big-bang upgrade, because the cost compounds" — your real lesson.]*

**Shape example (REPLACE every specific):**
> _"We were pinned to [old RN version]; [a needed library / a store requirement] forced an upgrade, and the native iOS pods and Android gradle broke. I owned it for a live app. I mapped the breaking changes, upgraded [incrementally], fixed [the native module bridges + pod/gradle conflicts], tested on real devices, and rolled out via [Codepush/Stallion] with rollback ready. We shipped with [no regressions] and kept crash-free at [X%]. Since then I upgrade on a cadence, not in a panic."_

**Likely follow-ups — be ready:** Which versions, from→to? · What broke first — JS API, iOS pods, or Android gradle? · How did you de-risk a live app (staged rollout, rollback, feature flags)? · How long did it take, and what did you underestimate? · How do you decide *when* to upgrade?

---

## Bonus — the level question (behavioral, NOT a STAR — but the make-or-break)

They **will** ask some version of: *"You've led a team and shipped your own products (TalentAxis, Space 360). Why do you want a mid-level IC role here?"* Rehearse this out loud, calm and confident — it's the same as your cover-letter reason:

> _"I've run the full cycle and led a team, so I know what I'm choosing. Right now I want to go deep on native iOS and Android as a hands-on builder, not manage. This role values Native together with React Native, which is exactly the depth I want to build — and I bring the delivery discipline of someone who's owned the whole thing. I'm not looking to run the team; I'm looking to do great mobile work here."_

**Delivery:** own it, don't apologize. If you sound like you're settling, they hear "flight risk." If you sound like you're *choosing* craft over title, they hear "senior who'll raise the bar." Same words, opposite outcome.

---

## Before the interview
1. Fill both stories with your real specifics (kill every `[bracket]`).
2. Find one real number per story if you can (even rough).
3. Say each out loud twice — 2 minutes, conversational.
4. Prep the follow-up answers (that's the actual test, not the story itself).
