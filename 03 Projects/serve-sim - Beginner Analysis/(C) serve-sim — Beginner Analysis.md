# (C) serve-sim — Beginner Analysis (LLM Wiki v183)

> **AI-generated** (prefix `(C)` per vault rule). Built 2026-06-22 by Claude as the v183 LLM-wiki ship.
> **Subject:** [`EvanBacon/serve-sim`](https://github.com/EvanBacon/serve-sim) — *"The `npx serve` of Apple Simulators."*
> **One-line:** A macOS tool that **streams a live iOS Simulator into a web browser and gives an AI coding agent a control channel to tap, swipe, type, rotate, inject a camera feed, and read app logs** — so the agent can finally *see and drive the app it is building*. "Browser Use, but for the iOS Simulator."
> **Source of the request:** a Facebook post (Vietnamese) — *"Làm sao để agent 'nhìn thấy' iPhone Simulator?"* ("How does an agent *see* the iPhone Simulator?").

---

## 0. TL;DR for a beginner

An AI coding agent (Claude Code, Codex, Cursor, …) is great at **writing** iOS/React-Native code. But after it writes the code, it is *blind*: it cannot look at the running app, cannot tap a button, cannot tell whether the screen it just built actually looks right or crashes. On the **web** that gap is mostly solved — tools like **Browser Use** give an agent a real browser it can see and click. On **mobile**, the equivalent was missing.

**serve-sim closes that gap for the iOS Simulator.** You run one command:

```sh
npx serve-sim
```

…and three things happen:
1. A small **Swift helper** captures the Simulator's screen (via Apple's `xcrun simctl io`) and streams it as **live 60 FPS video** to your browser (`http://localhost:3200`). A human can watch; **an agent can "look" at it** via a browser-vision tool.
2. A **control channel** opens (a WebSocket + a set of CLI commands) so the agent can **tap, swipe, type text, press hardware buttons, rotate the device, and even inject a fake camera feed**.
3. App **logs are forwarded** to the browser so the agent (or you) can read what the app is doing.

It ships as an **Agent Skill** (`skills/serve-sim/`) that teaches Claude Code / Codex / Cursor / Gemini CLI *how* to drive the Simulator. Install it into Claude Code with:

```sh
/plugin marketplace add EvanBacon/serve-sim
```

The author is **Evan Bacon**, the creator of **Expo** (the most popular React-Native framework). It's **Apache-2.0**, **macOS / Apple-Silicon-only**, currently early (**v0.1.34**, ~2k★).

**Why it matters to you (Storm Bear):** your real-software target, **hireui**, has an **Expo / React-Native mobile app** (the `CandidateDetailScreen` redesign spike). serve-sim is built *by the Expo author*, auto-integrates with `npx expo start`, and would let your vault's Claude Code **see and verify hireui's running iOS UI** — closing the loop on exactly the "demo template" visual-drift problem you've been fighting. That's the pilot story (see the companion [Pilot Methods Menu](<(C) serve-sim — Pilot Methods Menu.md>)).

---

## 1. The problem, in plain language

The Facebook post frames it perfectly (paraphrased):

> *An AI coding agent cannot fix an iOS interface if it cannot see that interface. With `npx serve-sim`, the iPhone Simulator screen is streamed to a browser, and a control channel is opened so Codex, Claude Code, or Cursor can tap, swipe, type, and read app logs. There were already tools for the iOS Simulator like `simctl` and `fb-idb`, but most were built for **human** automation. serve-sim is designed assuming the "person" using the simulator is an **AI agent**. If Browser Use gave AI eyes on the web, serve-sim does the same for iOS — a small but possibly important piece as AI coding shifts from "writing code" to "building and testing software."*

The core insight is the **perceive → decide → act loop** (a.k.a. the "agentic loop"):

- A **code-only** agent reads/writes text files. It *assumes* its code works.
- A **vision+control** agent **sees** the rendered UI (a screenshot / video), **reasons** about it, **acts** on it (tap, type), then **looks again** to check. It can *verify its own work* and recover from mistakes.

serve-sim supplies the **eyes (a live screen stream + accessibility tree + logs) and the hands (tap/type/gesture/camera)** for the iOS Simulator, so a coding agent can run that loop on a real running app instead of guessing.

---

## 2. What serve-sim actually is (verified facts)

**Identity & licensing** *(cloned + source-read at commit `a55ce8e`, default branch `main`, 2026-06-21; cross-checked against the rendered GitHub page)*:

| Field | Value |
|---|---|
| Repo | `EvanBacon/serve-sim` |
| Tagline (package description) | **"The `npx serve` of Apple Simulators."** |
| GitHub "About" | *"Host your simulator for use with Agent tools like Codex, Cursor, or Claude Desktop — locally, over your LAN, or host on a remote mac and tunnel anywhere."* |
| Author | **Evan Bacon** (`baconbrix@gmail.com`, evanbacon.dev) — **creator of Expo** |
| License | **Apache-2.0** (© 2026 Evan Bacon) |
| Primary language | **TypeScript ~73%** + native Swift / Objective-C(++) |
| npm package | `serve-sim` **v0.1.34** (+ `serve-sim-client` v0.1.15); **"No releases published"** on GitHub |
| Scale (page-stated) | **~2k★ / 102 forks** |
| Size / maturity | **~17,087 lines TS** + **23 native files** (.swift/.m/.mm/.h) + **47 test files**; monorepo (2 workspaces) |
| Platform | **macOS only**, **Apple Silicon (arm64) only** (the bundled `serve-sim-bin` is an arm64 binary — does **not** run on Intel); needs **Xcode command-line tools** (`xcrun simctl`); **Node ≥20**; macOS 14+ for camera injection |
| Supply chain | **No postinstall scripts. No telemetry.** Ships a compiled arm64 Swift helper + a camera-injection dylib inside the npm package. |

**It is NOT a single MCP server.** It is the composition of three things:
1. **A streaming server** (the Swift `serve-sim-bin` helper, one per device) that turns the Simulator framebuffer into video + a control socket.
2. **A CLI** (`serve-sim …` with subcommands) + **Connect-style middleware** you can mount in a dev server (Metro / Vite / Next / Express).
3. **An Agent Skill** (`skills/serve-sim/`) that teaches an agent to use the CLI/stream.

This composition detail matters for the pattern verdict (§6) — serve-sim *pairs with* browser-use MCP tools for the "vision" half rather than being one monolithic MCP server.

---

## 3. How it works (architecture)

```
┌──────────────┐   simctl io   ┌─────────────────┐  MJPEG / H.264 + WS  ┌─────────┐
│ iOS Simulator│ ────────────► │ serve-sim-bin   │ ───────────────────► │ Browser │  ← human watches
└──────────────┘   (Swift)     │ (per-device)    │                      │  + agent│  ← agent "sees" via
                               └─────────────────┘                      └─────────┘     browser-vision tool
                                       ▲
                                  state file in $TMPDIR/serve-sim/
                                       ▲
                               ┌──────────────────────────┐
                               │ serve-sim CLI / middleware│  ← agent "acts" (taps, types, …)
                               │ + Agent Skill             │
                               └──────────────────────────┘
```

**Perception (the "eyes"):**
- **Live video.** The Swift helper captures the Simulator framebuffer via `xcrun simctl io` and serves it as **MJPEG** (`/stream.mjpeg`, software JPEG) or **H.264/AVCC** (`/stream.avcc`, hardware-accelerated when the browser can decode it). Default preview UI on **port 3200**; per-device helper on **3100**.
- **Accessibility tree.** An endpoint `/.sim/ax` returns a JSON snapshot of the on-screen accessibility tree (so an agent can reason about elements, not just pixels).
- **WebKit DevTools / CDP bridge.** `/.sim/devtools/*` exposes a Chrome-DevTools-Protocol bridge into web views.
- **Forwarded logs.** Simulator logs are streamed to the browser **"for browser-use MCP tools to read from"** (the README's exact phrasing — note the explicit hand-off to browser-use).

**Action (the "hands")** — via CLI subcommands and a token-authenticated WebSocket exec channel:
- `serve-sim gesture '<json>'` — touch gestures (tap/swipe/drag); pinch-to-zoom (hold Option).
- `serve-sim button [name]` — hardware buttons (home, etc.); keyboard hotkeys forwarded (e.g. ⌘⇧H = home).
- `serve-sim type <text>` — type via the simulator keyboard (also `--stdin` / `--file`).
- `serve-sim rotate <orientation>` — portrait / upside-down / landscape-left/right.
- `serve-sim camera <bundle-id> …` — **inject a synthetic camera feed** (placeholder / image / video / live host webcam) by swizzling AVFoundation via a `DYLD_INSERT_LIBRARIES` dylib — so you can test camera-using apps without a real camera.
- `serve-sim ca-debug`, `serve-sim memory-warning` — toggle CoreAnimation debug flags, simulate a memory warning.
- Drag-and-drop images/videos onto the streamed device to add media.

**The control wire protocol** (`exec-ws.ts`): the client sends a token (SHA-256 constant-time match, 10-second auth window), then `{id, command}` shell requests get `{id, stdout, stderr, exitCode}` back; there's also an in-process simulator-settings path and same-origin SSE subscriptions. The `serve-sim-client` library exposes a typed **Gateway** protocol (`exec` / `file:read` / `file:write`).

**Deployment shapes:** localhost → LAN → **remote Mac + tunnel** (run the Simulator on a Mac in the cloud, tunnel the served URL, and a remote agent or human uses it "as if it were local"). Auto-integrates with `npx expo start` (Metro middleware); mountable in any Connect-style server via `simMiddleware({ basePath: "/.sim" })`.

**Agent integration:**
- **Agent Skill** `skills/serve-sim/` — "teaches AI coding agents (Claude Code, Cursor, Codex CLI, Gemini CLI, and any host implementing the open Agent Skills standard) how to drive a simulator through the CLI: taps, gestures, hardware buttons, rotation, camera injection, and handing the stream off to the host's preview pane." Install: `bunx add-skill EvanBacon/serve-sim` or, in Claude Code, `/plugin marketplace add EvanBacon/serve-sim`.
- **Claude Desktop** via a `.claude/launch.json` configuration that runs `npx serve-sim` on port 3200.

---

## 4. The "double deep-dive": the original knowledge behind the analogy

The request asked to *"double deep dive into the original resource for knowledge in the image."* The image's load-bearing reference is **Browser Use** plus the older simulator tooling (`simctl`, `fb-idb`). Here is the foundational knowledge, source-verified.

### 4.1 Browser Use — the web analogue (corpus subject **v41**)
- `browser-use/browser-use` — *"🌐 Make websites accessible for AI agents. Automate tasks online with ease."* (tagline elsewhere: "The way AI uses the web"). MIT; ~**89.9k★** in the corpus record; Python; 2-founder commercial entity (Magnus + Gregor Zunic, Zurich + SF). It gives an LLM agent a **real, controlled browser** it can perceive (DOM + accessibility + screenshots) and act on (click/type/scroll), with recovery loops. It is the **corpus's reference point for "agent eyes+hands on the web."** serve-sim is its **iOS-Simulator counterpart** — same paradigm, *different surface* (native app framebuffer vs. web DOM).
  - ⚠️ Corpus bookkeeping note: the current CLAUDE.md shim head miscaches browser-use as "v34" in a couple of places. The **authoritative project chapter** (`_state/03b`) records it as the **41st wiki = v41**. This wiki uses **v41**.
- Sibling corpus subjects: **Skyvern v24** (vision-primary browser automation) and **crawl4ai v29** (DOM-only crawler) — together the corpus's "browser-agent architectural spectrum."

### 4.2 The general paradigm: computer use / GUI agents
- **Anthropic computer use** — Claude takes a **screenshot**, reasons over the rendered pixels, and issues structured UI actions (`left_click(x,y)`, `type(...)`), then looks again. This is the canonical **perceive→reason→act→verify** loop and the conceptual parent of serve-sim's design. (Not a corpus subject; the paradigm, not a tool the vault ships.)
- The research framing: a *vision agent* "detects, understands, decides, and acts; then learns from the outcome" — distinct from classic computer vision (detect-and-stop) and from text-only agents (never see the UI).

### 4.3 The older iOS-Simulator tooling serve-sim supersedes
- **`xcrun simctl`** (Apple, official) — boot/shutdown sims, install/launch apps, take screenshots/recordings, `openurl`, push notifications. **Built for humans + CI**: it's a fire-a-command tool, text output, no persistent server, no live stream, no agent-friendly loop. serve-sim *uses* `simctl io` under the hood for capture, but wraps it in an agent-shaped server.
- **`facebook/idb`** (Meta's "iOS Development Bridge") — a daemon + Python/gRPC client that adds tap/swipe/text-input and accessibility queries over simctl, on device + simulator. ~5.1k★, MIT; **maintenance has slowed** (last release ~2022). Powerful but a **headless Python client** — no human-watchable stream, designed for scripted QA, not an LLM in the loop.

### 4.4 The fast-emerging peer crop (be honest: serve-sim is *not* alone externally)
This is a hot, crowded 2026 niche. Notable peers (NOT corpus subjects):
- **`joshuayoes/ios-simulator-mcp`** — wraps idb as an **MCP server** (~2.1k★, 15 tools incl. `ui_find_element` via the accessibility tree). MCP-native, structured element queries; **no live stream**.
- **`mobile-next/mobile-mcp`** — cross-platform (iOS **and** Android, sims + real devices), 20+ tools, accessibility-first + screenshot fallback. Broader surface; no real-time visualization.
- **`callstackincubator/agent-device`** (Callstack) — *"Give AI coding agents a real app feedback loop"*; token-efficient semantic snapshots; iOS/Android/Expo/Flutter/RN. Closest in *thesis*.
- **`jasonkneen/agent-simulator`** — browser-based iOS simulator for agents with **MJPEG stream + accessibility tree + MCP (15 tools)**. **The closest functional twin to serve-sim**, near-simultaneous.
- **Appium / appium-mcp** (~17k★, WebDriver) — industry-standard cross-platform, complex, flaky in practice. **AppAgent** (Tencent, ~6.5k★) — research multimodal GUI agent, Android-primary.

**Honest read of serve-sim's distinctiveness:** it is *not* the only "agent sees the simulator" tool, and **not a world-first**. Its distinctive *combination* is: **agent-first design + a human-watchable live 60 FPS browser stream + a bundled Agent Skill (not a separate MCP wrapper) + one-command `npx` UX + camera injection + Expo/Metro middleware + the Expo author's backing**. The "hard parts" (`simctl io` capture, AVFoundation swizzling) are platform-provided; serve-sim is the **agent-surface + streaming/orchestration layer** on top — analogous to how camofox-browser (v179) is the service layer over Camoufox's C++ fingerprint-spoofing.

---

## 5. Goal-alignment scorecard (routine v2.6, §31)

**Goal #1** = master Claude + autonomous agents for software development. **Goal #2** = ship real software (hireui). The tier is keyed on **(b)**, not (a) (§31).

| Axis | Verdict | Reasoning |
|---|---|---|
| **(a) Anthropic / cultural-peer source** | **FAIL (clean)** | Evan Bacon is a **disclosed, notable individual developer (the Expo creator)** — not Anthropic ((a)-7 is Anthropic-only), and "notable framework author" is not a registered (a) axis. No heritage/name rescue (v159→v181 discipline). First Evan-Bacon author → a **#19 19a** data-point. *(He is a stronger disclosed identity than the recent indie builders Waishnav v171 / Neo Reid v174 / Jack Le v181; the open disclosed-builder (a)-axis question is held operator-reviewable at N=3 per the v182 audit — not reopened here. His being the Expo author is a (b)/(d) signal, not an (a) one.)* |
| **(b) Goal-relevance — KEYS THE TIER** | **STRONG** | Gives a coding agent the **perceive→act loop over a running native iOS app** = core agent-autonomy substrate (Goal #1), and the **corpus's first such surface for mobile**. Claude is first-class (Claude Code Agent Skill + Claude Desktop `launch.json` + plugin marketplace). **Directly pilotable into hireui's Expo/React-Native mobile app** (Goal #2) — the vault's Claude Code could *see and verify* hireui's running iOS UI. **STRONG-not-STRONGEST:** third-party (not Anthropic substrate) · Claude one of several supported hosts (Codex/Cursor/Gemini) · capability-*augmentation* (extends what an agent can do, isn't the agent) · the vision half is consumed via browser-use MCP rather than a first-class native Claude integration · arm64-macOS-only · v0.1.x early. Calibrates to **Agent-Reach v174 (b) STRONG** and **camofox-browser v179 (b) STRONG**. |
| **(c) Substance / engineering** | **STRONG** | ~17K TS + 23 native Swift/ObjC files + 47 test files; framebuffer capture, MJPEG **and** H.264 streaming, a token-authed WebSocket exec channel, an accessibility endpoint, a WebKit/CDP bridge, AVFoundation camera-injection via dylib swizzling, Connect middleware for 4 dev servers, a typed client gateway library, an Agent Skill + plugin marketplace. By the Expo author; Apache-2.0; no postinstall; no telemetry. **Honest caveats:** v0.1.34 / "no releases published" / arm64-macOS-only / ~2k★ early / the hard primitives are platform-provided. |
| **(d) Cross-reference density** | **STRONG** | Browser-agent family (browser-use **v41** / Skyvern v24 / crawl4ai v29) · agent-capability-layer cluster (Agent-Reach v174 §C / camofox v179 §C) · computer-use paradigm · Agent-Skills ecosystem (agent-skills-standard v76 / ponytail v168 / SkillOpt v178) · Pattern #18 agent-tool-server · #84 84c provider-agnostic · #66 supply-chain · #12 routing-artifacts · **the Expo/React-Native tie to hireui (Goal #2)**. |

**Outcome: GOAL-ALIGNED INCLUDE 3/4** [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG].

---

## 6. Pattern Library verdict (verified by hand, inline)

> Per `feedback_wiki_verify_independently_check_collisions`, the verdict is produced **inline** (NOT the multi-agent verdict workflow, which has confabulated corpus facts). The source-read was delegated to **one read-only Explore agent** (clone at `a55ce8e`); **all corpus-fact / collision / identity claims were verified by hand** — grep over `_state/` + `_patterns/` + `03 Projects/`, the full §C standalone list (31 rows) read, and a targeted mobile/simulator term-grep. Confirmed: **no prior serve-sim / iOS-simulator / Evan-Bacon / Expo subject**, and **no existing §C standalone for a mobile/native-simulator perception+control surface**.

### 6.1 PRIMARY — 1 NEW §C Library-vocab standalone (CORPUS-FIRST, N=1)

**"Agent-First Mobile-Simulator Perception+Control Layer (live browser-streamed framebuffer + accessibility tree + forwarded logs for *perception*; taps/gestures/type/rotate/hardware-buttons/camera-injection for *action*; packaged as an Agent Skill so a coding agent can SEE and DRIVE a running native iOS app)."** — Anchor: **v183 serve-sim** (`EvanBacon`).

- **The mint is the CONJUNCTION:** (agent-*first* design for a native-app simulator) × (a human-watchable live framebuffer stream + accessibility + forwarded logs as the perception surface) × (a full action channel: tap/gesture/type/rotate/hardware-buttons/camera-injection) × (Agent-Skill packaging so Claude Code/Codex/Cursor/Gemini drive it). This is the **mobile/native-simulator analogue of the corpus's web-surface capability layers** — a genuinely new *surface*.
- **Scope of the "corpus-first" claim:** corpus-first **for the mobile/native-simulator surface**. NOT corpus-first for "agent vision+control" in general (browser-use v41 / Skyvern v24 preceded for the **web**). And NOT a *world*-first — externally it is one of a fast-emerging crop (agent-simulator, agent-device, ios-simulator-mcp, mobile-mcp); the §C mint is the corpus's first instance of the class, honestly scoped.
- **DISTINCT from:** browser-use v41 / Skyvern v24 / crawl4ai v29 (web browser/DOM surface) · Agent-Reach v174 §C (web/social **read+search of content**, not see+drive a live app UI) · camofox-browser v179 §C (anti-detect **web** browser server) · the GUI-client / management-GUI / observability families (those operate/watch the *agent*; serve-sim gives the agent eyes+hands on the *subject app it is building*).
- §28: 1 new standalone (≤2-per-wiki cap honored). **PROMOTION-ELIGIBLE at N=2** (a 2nd agent-first mobile-simulator perception+control layer — plausible soon given the external crop). Time-aware stale-watch (≥15 wikis AND ≥30 days, §39).

### 6.2 SECONDARY (NOT minted)
- **#19 19a** — first **Evan-Bacon** author (the Expo creator); (a) FAIL clean.
- **#84 84c** provider-agnostic (one Agent Skill consumed by Claude Code / Codex / Cursor / Gemini / any Agent-Skills host + Connect middleware for Metro/Vite/Next/Express). **NO N-bump** (per v86). Explicitly **NOT** the v168 ponytail "14-platform native-rule-file *distribution*" mechanism — serve-sim distributes **one** skill that many hosts consume.
- **#66 supply-chain / dual-use cross-ref** — ships a **compiled arm64 Swift binary** + a **camera-injection dylib injected via `DYLD_INSERT_LIBRARIES`** (swizzles AVFoundation) + a **WebSocket exec channel that runs arbitrary shell** (token-gated, SHA-256 constant-time, 10s auth) + a **tunnel-anywhere / remote-host posture**. Real attack-surface note (offset by: no postinstall, no telemetry, Apache-2.0, token auth). Pilot-fence material.
- **#12 LLM-routing-artifacts INCIDENTAL** — ships an Agent Skill + plugin-marketplace entry + `.claude/launch.json` (NO N-bump; side-effect of capability exposure).
- **Library-vocab #20 Token-Economy QUALIFIED-ADJACENT** — logs forwarded "for browser-use MCP tools to read from" is token-relevant, but **no quantified benchmark** → **N stays 4**, no bump.
- **Pattern #18 adjacency** — serve-sim *pairs with* browser-use MCP for the vision half but is **NOT itself an MCP server** → **NOT a #18 B1-MCP instance** (a streaming-server + CLI + Agent Skill, not one-MCP-server-many-clients).

### 6.3 NON-claims (anti-inflation)
- NOT a new top-level pattern (max stays **#85**).
- NOT **#52** (~2k★ / 102 forks / "no releases published" / v0.1.34 are **page-stated**, NOT API-verified §37.4 → velocity unestablishable, MCP-Night demo buzz notwithstanding).
- NOT corpus-first agent-vision+control **globally** (web preceded — claim scoped to the mobile/simulator surface).
- NOT **#18 B1-MCP**. NOT **#57** (it names Codex/Cursor/Claude/Gemini as *clients it provisions* and hands logs to *browser-use MCP tools* as a downstream consumer — integration/mentions ≠ influence-citation; the browser-use hand-off is an interesting corpus-subject-integration data-point, not recursion).

### 6.4 Tier & streak
- **Tier: T2 Service** (self-hosted local developer tool / streaming + control server). Same family as camofox-browser v179 / Agent-Reach v174 / claude-tap v173 / agentmemory v66.
- **Counts UNCHANGED at the top-level: 46 patterns / 11 CONFIRMED Library-vocab.** §C live standalones **+1** (the new mint).
- **Streak: GA:43 → GA:44** (forward-only from v126; historical "49+3*" frozen @v125; ⚠️ under the v176-GLM-5 OFF-GOAL reading → GA:43·OG:12).
- **§35 CLEAR** — rolling-3-ship window {**v180 GA**, **v181 GA**, **v183 GA**} = 0 OFF-GOAL (v182 = audit, excluded).
- **29 consecutive goal-aligned ships v153→v183** (GA reading; audit v182 excluded).

---

## 7. Risks, limitations, honest caveats

- **Platform lock-in:** macOS + Apple-Silicon only; needs Xcode CLT. Useless on Linux/Windows/Intel. (Your dev machine is `darwin` arm64-era — fine; CI on Linux would not be.)
- **Maturity:** v0.1.34, "no releases published," ~2k★. Expect churn and rough edges. Pin the commit/version.
- **Security surface (the big one):** the control channel runs **arbitrary shell** on the host (token-gated) and the design *invites* exposing the stream over LAN / a public tunnel. A leaked token + an open tunnel = remote shell on your Mac. The camera-injection dylib uses `DYLD_INSERT_LIBRARIES` (library injection) into simulator processes. **Treat any non-localhost use as a real risk.**
- **Vision is not free:** the agent still needs a browser-vision tool (browser-use / computer-use) to *interpret* the stream, OR it works from the accessibility tree / logs. serve-sim provides the surface, not the model's eyesight.
- **iOS Simulator ≠ real device:** simulators miss real-hardware behavior (true camera, sensors, performance, push). Good for UI iteration; not a substitute for device QA.

---

## 8. Sources

- Repo (cloned + source-read at `a55ce8e`, 2026-06-21): https://github.com/EvanBacon/serve-sim
- Browser Use: https://github.com/browser-use/browser-use · https://browser-use.com
- Anthropic computer use: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- Apple `simctl` (Xcode) · Meta idb: https://github.com/facebook/idb
- Peers: https://github.com/joshuayoes/ios-simulator-mcp · https://github.com/mobile-next/mobile-mcp · https://github.com/callstackincubator/agent-device · https://github.com/jasonkneen/agent-simulator
- Demo context: WorkOS "MCP Night" write-up of Evan Bacon's serve-sim demo.

> **Next:** see the companion **[Pilot Methods Menu](<(C) serve-sim — Pilot Methods Menu.md>)** for many concrete ways to apply this to your workflow (hireui mobile + the vault's own Claude Code).
