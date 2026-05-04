# (C) C1 — README + manifesto + adversarial positioning + 5-language i18n + reviews

> **Cluster scope:** User-facing positioning surface — primary README + 4 translations + manifesto + landing testimonials + Discord building-in-public framing.
> **Source files:** `README.md` (24.5 KB en) + `README.ko.md` + `README.ja.md` + `README.zh-cn.md` + `README.ru.md` + `docs/manifesto.md` + `.github/assets/` (hero + sisyphus + hephaestus + omo banner + sisyphuslabs banner)
> **Wiki phase:** Phase 2 cluster summary
> **Cross-wiki siblings cited:** OMC v27 / obra/superpowers v2 / paperclip v14 / GitNexus v33 / vercel-labs v51

---

## 1. Positioning + tagline

**GitHub description (verbatim):** "omo; the best agent harness - previously oh-my-opencode"

**README hero (verbatim):**
- "Oh My OpenCode" (legacy brand displayed in hero image; repo renamed to oh-my-openagent)
- "The Best AI Agent Harness - Batteries-Included OpenCode Plugin with Multi-Model Orchestration, Parallel Background Agents, and Crafted LSP/AST Tools" (package.json description)

**Anti-thesis (corpus-first explicit subject README claim):**
> "Anthropic [**blocked OpenCode because of us.**](https://x.com/thdxr/status/2010149530486911014) **Yes this is true.**
> They want you locked in. Claude Code's a nice prison, but it's still a prison.
>
> We don't do lock-in here. We ride every model. Claude / Kimi / GLM for orchestration. GPT for reasoning. Minimax for speed. Gemini for creativity.
> The future isn't picking one winner—it's orchestrating them all. Models get cheaper every month. Smarter every month. No single provider will dominate. We're building for that open market, not their walled gardens."

⚠️ **Subject-claim caveat:** The "Anthropic blocked OpenCode because of us" claim is asserted in README and references an X.com post by @thdxr. Storm Bear vault has not independently verified the underlying incident. Document as subject-claim; flag in beginner guide ethical framing.

This is the **strongest adversarial-runtime-vendor positioning observed in 52 corpus wikis**. Prior corpus poles:
- **paperclip v14** "zero-human companies" (autonomy-max framing, Pattern #13 retired but framing precedent)
- **claude-code-best-practice v34** Boris Cherny + Anthropic-team-aggregator citation (lineage style; pro-Anthropic)
- **OMC v27** "Multi-runtime first; Claude, Codex, Gemini, Cursor-agent" (multi-runtime equivalence; not adversarial)

omo v52 is unique in **explicitly framing Anthropic as antagonist** rather than neutral provider. Continues: *"We run best on Opus, but Kimi K2.5 + GPT-5.4 already beats vanilla Claude Code. Zero config needed."*

## 2. Manifesto philosophical position (corpus-first explicit autonomy-max declaration)

`docs/manifesto.md` — verbatim title section: **"Human Intervention is a Failure Signal"**

> "**HUMAN IN THE LOOP = BOTTLENECK**
>
> Think about autonomous driving. When a human has to take over the wheel, that's not a feature. It's a failure of the system. The car couldn't handle the situation on its own.
>
> **Why is coding any different?**
>
> When you find yourself:
> - Fixing the AI's half-finished code
> - Manually correcting obvious mistakes
> - Guiding the agent step-by-step through a task
> - Repeatedly clarifying the same requirements
>
> That's not 'human-AI collaboration.' That's the AI failing to do its job.
>
> **Oh My OpenAgent is built on this premise**: Human intervention during agentic work is fundamentally a wrong signal. If the system is designed correctly, the agent should complete the work without requiring you to babysit it."

Additional manifesto sections:
- **"Indistinguishable Code"** — *"Goal: Code written by the agent should be indistinguishable from code written by a senior engineer. Not 'AI-generated code that needs cleanup.' Not 'a good starting point.' The actual, final, production-ready code."*
- **"Token Cost vs Productivity"** — *"Higher token usage is acceptable if it significantly increases productivity."*
- **"Minimize Human Cognitive Load"** — *"The human should only need to say what they want. Everything else is the agent's job."*

**Comparison to paperclip v14** (corpus prior autonomy-max pole):
- paperclip: "zero-human companies" (organizational endpoint framing)
- omo: "Human In The Loop = BOTTLENECK" (operational signal framing) + autonomous-driving analogy
- Both reach Pattern #51 Vibe-Coding Spectrum anti-vibe-pole / pro-full-autonomy via different framings

## 3. ultrawork command — primary user-facing primitive

**Verbatim:** *"You're actually reading this? Wild. Install. Type `ultrawork` (or `ulw`). Done. Everything below, every feature, every optimization, you don't need to know it. It just works."*

**Subscription-stack recommendation (verbatim, with caveat):**
> "Even only with following subscriptions, ultrawork will work well (this project is not affiliated, this is just personal recommendation):
> - ChatGPT Subscription ($20)
> - Kimi Code Subscription ($0.99) (*only this month)
> - GLM Coding Plan ($10)
> - If you are eligible for pay-per-token, using kimi and gemini models won't cost you that much."

This = **subscription-rotation strategy** (similar to aidevops v47's 4-provider OAuth pool: Anthropic + OpenAI + Cursor + Google). Pattern #28 strengthens — subscription-rotation as multi-provider sub-axis.

## 4. 14-feature highlights table (verbatim header texts)

| Emoji | Feature | What it does (verbatim) |
|---|---|---|
| 🤖 | Discipline Agents | Sisyphus orchestrates Hephaestus, Oracle, Librarian, Explore. A full AI dev team in parallel. |
| ⚡ | `ultrawork` / `ulw` | One word. Every agent activates. Doesn't stop until done. |
| 🚪 | IntentGate | Analyzes true user intent before classifying or acting. No more literal misinterpretations. |
| 🔗 | Hash-Anchored Edit Tool | `LINE#ID` content hash validates every change. Zero stale-line errors. Inspired by oh-my-pi. |
| 🛠️ | LSP + AST-Grep | Workspace rename, pre-build diagnostics, AST-aware rewrites. IDE precision for agents. |
| 🧠 | Background Agents | Fire 5+ specialists in parallel. Context stays lean. Results when ready. |
| 📚 | Built-in MCPs | Exa (web search), Context7 (official docs), Grep.app (GitHub search). Always on. |
| 🔁 | Ralph Loop / `/ulw-loop` | Self-referential loop. Doesn't stop until 100% done. |
| ✅ | Todo Enforcer | Agent goes idle? System yanks it back. Your task gets done, period. |
| 💬 | Comment Checker | No AI slop in comments. Code reads like a senior wrote it. |
| 🖥️ | Tmux Integration | Full interactive terminal. REPLs, debuggers, TUIs. All live. |
| 🔌 | Claude Code Compatible | Your hooks, commands, skills, MCPs, and plugins? All work here. |
| 🎯 | Skill-Embedded MCPs | Skills carry their own MCP servers. No context bloat. |
| 📋 | Prometheus Planner | Interview-mode strategic planning before any execution. |
| 🔍 | `/init-deep` | Auto-generates hierarchical AGENTS.md files throughout your project. |

## 5. Greek-mythology specialist agent personas (corpus-first cluster at T1)

**11 named agents in src/agents/** (verified via /bin/ls):
1. **Sisyphus** (`claude-opus-4-7` / `kimi-k2.5` / `glm-5`) — main orchestrator; "plans, delegates to specialists, drives tasks to completion with aggressive parallel execution. Does not stop halfway."
2. **Sisyphus-Junior** — variant for smaller scope
3. **Hephaestus** (`gpt-5.4`) — autonomous deep worker; "*The Legitimate Craftsman.*"
4. **Prometheus** (`claude-opus-4-7` / `kimi-k2.5` / `glm-5`) — strategic planner; "Interview mode: it questions, identifies scope, and builds a detailed plan before a single line of code is touched."
5. **Oracle** — architecture/debugging
6. **Librarian** — docs/code search
7. **Explore** — fast codebase grep
8. **Atlas** — (per AGENTS.md inventory)
9. **Metis** — (per AGENTS.md inventory)
10. **Momus** — (per AGENTS.md inventory)
11. **Multimodal-Looker** — vision-augmented inspection

**Mythology source distribution:** Greek (8: Sisyphus / Hephaestus / Prometheus / Oracle / Atlas / Metis / Momus + Sisyphus-Junior) + functional (3: Explore / Librarian / Multimodal-Looker).

**Pattern #25 Personality-Driven Agent Design retired v27 audit** — do NOT re-register. Greek-mythology cluster = aesthetic/cultural choice, not architectural pattern. Documentation only.

**Sister projects + Korean ecosystem connection:** Sisyphus mythology also appears in OMC v27 (`oh-my-claude-sisyphus` was original npm package name) and Sisyphus Labs (sisyphuslabs.ai) commercial incubation. Both Korean Seoul authors (Yeachan Heo + YeonGyu-Kim) reference Sisyphus mythology. Within Pattern #73 73a Korean-T1-archetype sub-observation cluster (NOT new candidate).

## 6. 5-language README i18n

Files verified via /bin/ls in repo root:
- `README.md` (English primary)
- `README.ko.md` (Korean — 한국어; native author language)
- `README.ja.md` (Japanese — 日本語)
- `README.zh-cn.md` (Simplified Chinese — 简体中文)
- `README.ru.md` (Russian — Русский) — **corpus-first inclusion of Russian at T1**

**Comparison to corpus i18n at T1:**
- claude-howto v32: 4-language (en + vn + zh-CN + uk) — Ukrainian first
- OMC v27: 7-language (en + ko + zh + ja + es + vi + pt) — broadest T1
- omo v52: 5-language (en + ko + ja + zh-cn + ru) — first Russian at T1; matches OMC pattern of Korean-author-driven multi-language
- claude-code-best-practice v34 / agency-agents v18: EN-only or limited

**Korean-author multi-lang convention** observed (within Pattern #73 73a strengthening): Korean Seoul authors prioritize multi-language docs at T1 distinct from English-monoglot Anglo-T1 default.

## 7. Reviews / testimonials (verbatim — building-in-public + viral-validation surface)

README opens with 8+ testimonials including:

> "It made me cancel my Cursor subscription. Unbelievable things are happening in the open source community." — Arthur Guiot

> "If Claude Code does in 7 days what a human does in 3 months, Sisyphus does it in 1 hour. It just works until the task is done. It is a discipline agent." — B, Quant Researcher

> "Knocked out 8000 eslint warnings with Oh My Opencode, just in a day" — Jacob Ferrari

> "I converted a 45k line tauri app into a SaaS web app overnight using Ohmyopencode and ralph loop. Started with interview me prompt, asked it for ratings and recommendations on the questions. It was amazing to watch it work and to wake up this morning to a mostly working website!" — James Hargis

> "use oh-my-opencode, you will never go back" — d0t3ch

> "You guys should pull this into core and recruit him. Seriously. It's really, really, really good." — Henning Kilset

> "Hire @yeon_gyu_kim if you can convince him, this dude has revolutionized opencode." — mysticaltech

> "Oh My OpenCode Is Actually Insane" — YouTube Darren Builds AI

**Pattern #50 50b recruiting-as-funnel-terminus** observation reinforced (Henning + mysticaltech recruit-suggestions); same dynamic as MiroFish v49 originator-of-50b-sub-variant.

**Building-in-public framing (verbatim):**
> "The maintainer builds and maintains oh-my-opencode in real-time with Jobdori, an AI assistant built on a heavily customized fork of OpenClaw.
> Every feature, every fix, every issue triage — live in our Discord.
> [→ Watch it happen in #building-in-public]"

→ **Jobdori = name of YeonGyu's customized OpenClaw fork** (Korean: 잡도리 / "doing thoroughly"). Corpus-first explicit named OpenClaw-fork at T1. Within Pattern #18 OpenCode-primary observation strengthening.

## 8. Sisyphus Labs commercial-incubation banner (corpus-first observation)

Embedded near top of README:

> "[Sisyphus Labs - Sisyphus is the agent that codes like your team.]
> **We're building a fully productized version of Sisyphus to define the future of frontier agents. Join the waitlist [here](https://sisyphuslabs.ai).**"

→ **Pattern #50 50d incubation-waitlist-as-funnel-terminus** sub-variant observation. Distinct from:
- 50a standard commercial-tier funnel (most prior #50 data points)
- 50b recruiting-as-funnel-terminus (MiroFish v49 originator + omo v52 testimonials echo)
- 50c aggregator-with-bundled-commercial-product (awesome-claude-skills v50)

50d mechanism: **separate commercial entity (Sisyphus Labs) with waitlist landing page entrypoint embedded in OSS README** — the OSS project IS the lead-magnet for the commercial entity, but commercial product not yet released (waitlist-only). Different from 50a where commercial tier exists alongside OSS, and 50c where commercial product ships inside OSS repo.

N=1 stale-flagged at registration v52 → v57 stale-check / v62 retire-check.

## 9. Discord + community surface

- Discord: `discord.gg/PUwSMR9XNk` (1.4K members per badge)
- X account: @justsisyphus (proxy; @q_yeon_gyu_kim suspended per README)
- GitHub follower: @code-yeongyu (2,956 followers)

**#building-in-public channel** = corpus-first explicit named channel for live-development streaming at T1.

## 10. Skip-the-README ethos

> "**Skip This README** — We're past the era of reading docs. Just paste this into your agent: 'Read this and tell me why it's not just another boilerplate: https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/README.md'"

→ Agent-mediated documentation consumption pattern (corpus first explicit at T1; precedent: aidevops v47 README cite-don't-read style).

## 11. Installation paths (3 surfaces)

**For Humans (verbatim):**
> "Copy and paste this prompt to your LLM agent (Claude Code, AmpCode, Cursor, etc.):
> 'Install and configure oh-my-opencode by following the instructions here: https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md'"

**For LLM Agents (verbatim):**
> "Fetch the installation guide and follow it: `curl -s https://raw.githubusercontent.com/code-yeongyu/oh-my-openagent/refs/heads/dev/docs/guide/installation.md`"

**Manual** (less promoted): read `docs/guide/installation.md` directly.

**Note (verbatim):** *"Use the published package and binary name `oh-my-opencode`. Inside `opencode.json`, the compatibility layer now prefers the plugin entry `oh-my-openagent`, while legacy `oh-my-opencode` entries still load with a warning. Plugin config files still commonly use `oh-my-opencode.json` or `oh-my-opencode.jsonc`, and both legacy and renamed basenames are recognized during the transition."*

→ Pattern #58 58c rebrand-repo-keep-npm-package + dual-bin-alias confirmed via:
1. Repo renamed (`oh-my-opencode` → `oh-my-openagent`)
2. npm package preserved (`name: "oh-my-opencode"`)
3. Dual-bin alias (`bin: { "oh-my-opencode": "...", "oh-my-openagent": "same-file" }`)
4. Compatibility layer in opencode.json accepts both legacy + new entries
5. Config files accept both `oh-my-opencode.json[c]` and `oh-my-openagent.json[c]` basenames

## 12. Telemetry disclosure (corpus-first explicit)

**README verbatim (paragraph after install):** *"Anonymous telemetry is enabled by default to help improve install and runtime reliability. It uses PostHog with a hashed installation identifier, never the raw hostname, and can be disabled with `OMO_SEND_ANONYMOUS_TELEMETRY=0` or `OMO_DISABLE_POSTHOG=1`. See Privacy Policy and Terms of Service."*

→ Privacy Policy + ToS in `docs/legal/`. Pattern #12 governance-depth strengthening (corpus-first telemetry-on-by-default with opt-out + Privacy/ToS at solo-T1 — ties bizos v37 in-app /guide tutorial discipline; exceeds typical solo-T1 minimum).

## 13. Uninstallation discipline (corpus-first explicit at T1)

README dedicates 30+ lines to uninstall procedure (3 steps with `jq` example to surgically remove plugin entries from `~/.config/opencode/opencode.json`). Recognizes both legacy + new basenames.

→ Operational governance discipline at solo-T1 = 7th counter-evidence wiki for Pattern #12 v42 refined formulation (governance correlates with maturity-ambition + maintainer-philosophy + scale-tier, NOT solo-vs-corporate alone). YeonGyu's maintainer-philosophy = thorough operations.

## 14. Cross-cluster Pattern #57 57a observation (preview)

`docs/superpowers/` subdirectory exists in repo (verified via /bin/ls; contains `plans/` + `specs/`). This is direct citation of **obra/superpowers (Storm Bear v2 wiki subject)** as integrated skill-system component within omo. Pattern #57 57a 5th data point.

omo v52 also is itself **subject of forward-citation-then-wiki sub-variant 57c** (OMC v27 wiki entry cited "oh-my-opencode" as inspirational source 25 wikis BEFORE v52 wiki built). 57c reaches structural N=2 at v52 (joins v51 vercel-labs).

## 15. Cluster takeaways

- **Adversarial-Anthropic positioning** = corpus-first explicit subject README claim (subject-claim caveat applied)
- **Manifesto autonomy-max** = strongest "human in loop = bottleneck" framing observed in 52 wikis (parallel to paperclip v14 organizational framing)
- **Greek-mythology persona cluster** = aesthetic/cultural Korean-author signature (within #73 73a sub-observation; not new pattern; #25 already retired)
- **5-language i18n with Russian first at T1** = corpus-first observation; Korean-author multi-lang convention strengthening
- **Sisyphus Labs commercial incubation** = Pattern #50 50d sub-variant NEW (incubation-waitlist-as-funnel-terminus; N=1 stale-flagged)
- **Pattern #58 58c sub-variant** = repo rename without npm rename + dual-bin alias (NEW; N=1 stale-flagged)
- **OpenCode-primary observation N=2** = omo extends OpenCode runtime as plugin (joins aidevops v47); Pattern #18 OpenCode-primary un-stale + promotion-candidate
- **Pattern #57 57c structural N=2** at v52 (OMC v27 cited oh-my-opencode 25 wikis pre-v52); promotion-candidate at next mini-audit
- **Pattern #57 57a 5th data point** (omo cites obra/superpowers v2)
- **Subscription-rotation as Pattern #28 sub-axis** = ChatGPT $20 + Kimi $0.99 + GLM $10 stack
- **Telemetry-on-by-default with opt-out + Privacy/ToS at solo-T1** = Pattern #12 v42 refined 7th counter-evidence wiki (HOLDS)
