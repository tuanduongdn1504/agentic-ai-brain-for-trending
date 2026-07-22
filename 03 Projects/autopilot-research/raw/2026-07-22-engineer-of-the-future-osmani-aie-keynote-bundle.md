<!-- raw: 2026-07-22 -->
# RAW — "The Engineer of the Future" (Addy Osmani AIE keynote) + 5-video bundle on the shifting engineering role under AI agents

> **Ingested:** 2026-07-22 · Path 1 `/loop autopilot research <video>` (operator anchor + yt-search bundle ×6)
> **Fetch method:** `yt-dlp --write-auto-subs --write-subs --sub-langs "en.*" --cookies-from-browser chrome` → `bin/vtt-to-md.py` → full transcripts read in main loop. NO NotebookLM (`notebook_id: none`).
> **Transcripts (scratchpad, session-local):** `scratchpad/md/{n97BCfyFIvw,g8um2AEf5ZA,LCEmiRjPEtQ,8h9j2rskP14,ubrfeaLEVVA,R9K2574YEAg}.md`
> **Total:** ~27.4K words across 6 talks.
> **Verification:** adversarial refute-first Workflow `wf_dabc1f67-f9f` (15 claim-cluster verifiers + corpus-collision). Scorecard folded into `wiki/engineer-of-the-future/claims-scorecard.md`.

---

## Source bundle

| # | Video ID | Title | Speaker / Channel | Date | Len | Role in bundle |
|---|---|---|---|---|---|---|
| ⭐ anchor | `n97BCfyFIvw` | "The engineer of the future is the person who is able to choose what is worth doing." | Addy Osmani / AI Engineer | 2026-07-14 | 18:26 | Answerability thesis (synthesis) |
| 2 | `g8um2AEf5ZA` | The Future of Software Engineering | Andrew Ng / DeepLearningAI | 2026-05-20 | 19:21 | Building blocks, PM bottleneck, no job-apocalypse |
| 3 | `LCEmiRjPEtQ` | Software Is Changing (Again) | Andrej Karpathy / Y Combinator | 2025-06-19 | 39:31 | Software 1.0/2.0/3.0, LLM-as-OS, autonomy slider |
| 4 | `8h9j2rskP14` | The next era of AI coding | Cursor | 2026-05-12 | 9:38 | tab→agent→teams eras; agent managers |
| 5 | `ubrfeaLEVVA` | Software Engineering + AI = ? | Gergely Orosz / Sonar Summit 2026 | 2026-03-04 | 36:51 | Field report; Dec-2025 "breakthrough" |
| 6 | `R9K2574YEAg` | The Future of AI Agents: Interrupt 2027 | Harrison Chase / LangChain | 2026-05-21 | 22:10 | Agent futures; continual learning; Fleets |

Cross-link to existing corpus: `pocock-software-fundamentals` (same AI Engineer channel; the "fundamentals matter more" companion to Osmani's "engineering moves up a level").

---

## ⭐ Anchor — Addy Osmani, "The engineer of the future… choose what is worth doing" (`n97BCfyFIvw`)

**Central thesis:** As agents automate more of the *doing*, the engineer's value shifts to **choosing what is worth doing** and **owning the verdict** — the evidence, the understanding, and the production decision. "Answerability" becomes an engineering requirement, not a philosophy.

- **Verdict / answerability:** Not judging for its own sake — being *accountable for production decisions* (ship / block / redirect / accept risk). "Quality produces evidence; a verdict assigns responsibility; answerability is what lets us stand behind a verdict."
- **Boris Cherny's role taxonomy** (attributed): roles "rebundling around the work" — modes **prototype / build / sweep / grow / maintain**. The scarce thing isn't doing the task; it's knowing which mode the product needs, what quality bar applies, and who owns the result.
- **The stack that got us here:** harness engineering (model + harness: context, tools, filesystem, git) → **loop engineering** (systems that keep prompting / checking / remembering / deciding) → **software factory** (agents run the inner loop, evidence comes out — credits "Dex's talk"). Humans still make the production decisions; the wind moves human judgment to the highest-leverage checkpoint.
- **Sonar 2026 survey** (cited): AI-assisted code is "no longer marginal"; clean vs messy repos have ~same pass rates but **clean code uses fewer tokens + causes fewer revisits**; **~96% skeptical of AI code but only ~half always verify** before committing → "distrust without bandwidth." Making generation cheaper does not make review cheaper. Safety = making verification cheaper/clearer/harder-to-skip.
- **Alpha & decay:** *Alpha* = the gap between what you can do and what current models can do. *Decay* = the clock on that gap; any capability edge eventually gets eaten by the frontier. Speed decayed; recall decayed (harness memory); verification is moving into harnesses/evals/static-checks/model-critique; **taste decays slowly but still resets** as models learn from examples.
- **Taste:** Paul Graham — "when anyone can make anything, choosing what to make becomes important." Mitchell Hashimoto — taste = "the ability to make high-quality qualitative judgments where no objective metric exists yet." Taste is *alpha*, not an eternal moat; the best version isn't mystique, it's leaving behind examples/critique the team + system can learn from.
- **Better strategic question:** not "what can the agent do" (that list keeps shrinking) but **"what can only a human be answerable for."** The word *engineer* gets stricter: reason about systems, defend trade-offs, manage risk, be the person reached when things break.
- **Three things to avoid:**
  1. **Cognitive debt** — erosion of your understanding of how to solve problems; *delegation debt* = build passes, PR merges, but the team can no longer explain the system it ships. Long-horizon agent runs (hour/day-scale) let the human "lose the thread"; review must become a control system, not a glance.
  2. **Cognitive surrender** — blindly accepting AI output before forming your own opinion. Wharton study cited: when AI was wrong, ~73% still picked the wrong answer *and felt more sure* = "borrowed confidence."
  3. **Orchestration tax** — cognitive bandwidth doesn't parallelize; more agents ≠ more of you. Fix = designing your attention like a system (where you enter, what you require, what you reuse).
- **Career math:** half-life of an *edge* (speed/recall/verification/taste) ≈ one model release; half-life of a *signature* (your credibility, the name on the work) is much longer. Skills earn leverage; **accountability turns leverage into trust.**
- **Execution vs responsibility:** agents can choose/route/merge/escalate/operate-inside-policy — but "the agent can follow your runbook, it can't inherit the consequences." When something fails: who understood the policy, who accepted the risk, who owns the blast radius?
- **Agency ladder:** flag → execute → diagnose → propose → recommend → resolve → **discernment** (deciding whether a problem is even worth investing in). High agency = "ownership with judgment attached," not "I do everything," not hustle theater.
- **Operating model:** inner loop = **capability** (agents investigate/implement/test/report); outer loop = **agency** (decide/verify/approve/own). "The boundary is not *human looks at AI output* — the boundary is evidence and responsibility."
- **Operational rule:** **"Explain it or don't ship it."** Not because humans type every line, but because someone must understand the work well enough to defend it. (CODEOWNERS analogy — who's accountable for that part of the architecture.)
- **Close:** Automation moves the floor; engineering moves up a level. New work = loop design, evidence design, brownfield stewardship. Jevons-style: every time we made software cheaper to write (high-level languages, frameworks, cloud, low-code) demand went *up*, not down. Agents move the bottleneck from "can we build this?" to **"should this exist, and can we answer for it?"** — "Build the factories, keep the lights on, own the verdict."

---

## 2 — Andrew Ng, "The Future of Software Engineering" (`g8um2AEf5ZA`)

- **Software = assembling building blocks** (LEGO metaphor: more distinct bricks → combinatorial explosion of what you can build). AI coding agents make assembling building blocks — AI (LLMs, RAG, agentic workflows) and non-AI (UI, DBs, auth) — far faster; blocks proliferate daily.
- **~100% AI coding:** Ng says his own coding is "pretty much 100% AI"; frontier teams trend toward ~100%. The last gap (80%→100%) matters: at 80%, human review of the remaining code becomes the bottleneck. Not a religion (hand-write the 50-line NASA spaceship code if you must).
- **Product-management bottleneck:** building got 10–100× faster → *deciding what to build* is the new bottleneck. PM:engineer ratios moved 1:8 → 1:2 → 1:1 → collapse into a **single generalist** (engineers who shape products / PMs who code move fastest). Also design, legal/compliance, marketing, sales bottlenecks — small AI-native generalist teams use AI to cover functions.
- **Scaling teams:** many AI-native teams with limited communication + clear API boundaries.
- **No job apocalypse:** business media (paid to get it right) increasingly says the apocalypse is overhyped; cited a **Federal Reserve Bank of Philadelphia** reference re: CEOs/workforce. Future AI-engineer has a bright future; unmet demand.
- **Hiring criteria:** (1) use coding agents effectively (Claude Code / Gemini / Codex / opencode), (2) robust knowledge of building blocks, (3) generalist skills (basic PM etc.).
- **Parallel skill development:** agents get more capable + humans need complementary skills to drive them.
- **Context Hub** (built with Vivek Prasad, Sanyam Hota + Ng): feeds coding agents up-to-date docs — fixes stale/deprecated-API hallucination (e.g. agents defaulting to OpenAI *chat completions* instead of the newer *responses* API); generates a ~600-line markdown doc *for the agent*.
- **Code Dream / "Code Realm"** (name ambiguous in captions; Codoji build environment): a "conversation, not a course" learning product with a voice agent (build a joke-generator app); announced in preview.

---

## 3 — Andrej Karpathy, "Software Is Changing (Again)" (`LCEmiRjPEtQ`, YC AI Startup School, June 2025)

> Note: ~13 months older than the others; the canonical thesis the newer talks build on. Some specifics (model names, tools) are mid-2025-vintage.

- **Software 1.0 / 2.0 / 3.0:** 1.0 = code you write; 2.0 = neural-net *weights* (HuggingFace ≈ GitHub of 2.0); 3.0 = **LLMs programmed in English** (prompts are programs). Be fluent in all three; fluidly transition.
- **LLMs as utility / fab / OS:** utility (capex to train ≈ building a grid; opex metered per-token; OpenRouter ≈ transfer switch; "intelligence brownout" when models go down). Fab (huge capex, deep R&D tech-trees centralizing). **Operating system = best analogy** (LLM ≈ CPU, context window ≈ memory; closed Windows/macOS vs open Llama≈Linux; apps like Cursor run on GPT/Claude/Gemini via a dropdown). We're in the **1960s time-sharing era** — compute expensive, centralized in cloud, thin clients; personal-computing revolution not yet (Mac minis fit batch-1 inference). Talking to an LLM in text ≈ a terminal.
- **Diffusion flip:** normally new tech goes government/corp → consumer; LLMs went **consumer first** (boil-an-egg, not ballistics).
- **LLM psychology — "people spirits":** stochastic simulations of people; encyclopedic memory (Rain Man) but cognitive deficits — hallucinate, **jagged intelligence** (9.11 > 9.9; two Rs in "strawberry"), **anterograde amnesia** (context window ≈ working memory; Memento / 50 First Dates), gullible / prompt-injection-prone.
- **Partial-autonomy apps:** Cursor = traditional interface + LLM integration. Shared properties: (1) LLMs do context management, (2) orchestrate multiple model calls (embeddings/chat/diff-apply), (3) **app-specific GUI** to audit fallible output fast (diff red/green; cmd-Y/cmd-N), (4) **autonomy slider** (tab → cmd-K → cmd-L → cmd-I). Perplexity similar (search/research/deep-research slider).
- **Generation-verification loop:** AI generates, humans verify — keep the loop fast two ways: (1) **GUIs speed verification** (vision = highway to the brain), (2) **keep the AI on a leash** (small concrete diffs; a 10,000-line diff makes the human the bottleneck; concrete prompts raise verification success). Education example: split teacher-app / student-app around an *auditable* course artifact.
- **"Decade of agents, not year of agents":** rode a flawless self-driving demo in 2013, yet ~12 years later autonomy still needs humans in the loop. Software is tricky; be serious; keep humans in the loop.
- **Iron Man suit:** augmentation + agent; build **suits (partial autonomy)** not **robots (full autonomy)**; slide autonomy left→right over the decade.
- **Everyone's a programmer** (English). **Vibe coding** (his tweet became a meme / Wikipedia page). Built an iOS Swift app in a day without knowing Swift; **MenuGen** (menu.app) — the coding was easy; making it "real" (auth/payments/domain/deploy) took a week of browser clicking (DevOps, not code).
- **Build for agents:** agents = a new consumer/manipulator of digital info ("people spirits on the internet"). `llm(s).txt` (≈ robots.txt); docs in **markdown** (Vercel, Stripe early movers); Vercel replaced "click here" with equivalent **curl** commands; **MCP** (Anthropic); **GitIngest** (github→gitingest URL → one pasteable text); **DeepWiki** (Devin/Cognition auto-docs a repo). "Meet the LLM halfway."

---

## 4 — Cursor, "The next era of AI coding" (`8h9j2rskP14`)

- **Framing:** Star Wars (1977) premiered at the venue that is now Cursor's office; used the "Dykstraflex" computer-controlled camera → technology redefining a category. Software's complexity is hidden (unlike a Gothic cathedral), which is why non-technical stakeholders underestimate change cost.
- **Three eras: tab → agent → teams.** Over 2025 the ratio flipped: **agent requests up ~15×** YoY; started 2025 with ~10× more tab-accepts than agent-requests, ended with far more agent-requests (and an agent request = a giant body of work vs a few chars for tab).
- **Teams era (forward-thinking cos):** internally **~30% of Cursor's PRs are developed end-to-end by an agent with no human intervention** (agent has its own cloud computer, runs hours/days). Enterprise segment: AI-generated code rose from ~15–20% (a year ago) to **~75%**; humans don't touch the syntax, they delegate.
- **Role shift → "agent managers":** from ~thousands of human engineers to "tens of thousands of ghost colleagues" alongside them; engineers spend much more time on **review** (looking at syntax, build versions, testing) and on **multitasking / parallelism / context-switching** (1–3 local agents → dozens of cloud agents).
- **Bad path exists:** you *can* generate unsustainable code / bad architecture / bugs — hence more review time.
- **Far-future experiment:** an agent team built a **prototype web browser over ~1 week, no humans in the loop, ~3M lines of code, many PRs** — day 1 can't render apple.com; by end, a mostly-functional web-rendering prototype. Nascent, not production-ready; informs product decisions for the teams era.

---

## 5 — Gergely Orosz (The Pragmatic Engineer), "Software Engineering + AI = ?" (`ubrfeaLEVVA`, Sonar Summit 2026)

- **FUD both directions:** headlines (Zuckerberg "AI replaces mid-level engineers"; Wired "vibe coding coming for jobs"; a VC crossing a "threshold") vs on-the-ground failures (agent adding too much observability cost a small co a few $K; a security tool wrongly flagging last-4-of-credit-card as PII; founders reverting because output got harder to review).
- **Company-by-company field report** (from visiting offices Oct 2025):
  - **Cursor** — ~40–50% of Cursor's code written by Cursor (Oct); auto-oneshot Linear tickets; agents >> tabs internally.
  - **OpenAI** — unlimited ChatGPT/Codex; parallel Codex agents the norm; "fix-it" button oneshots a PR; **>90% of the Codex app generated by Codex**; typical Codex engineer runs **4–8 parallel agents** (head of eng "Tibo"); "walk around with laptops open, agents running."
  - **Anthropic** — a *research* company that happens to make the most-used dev tools; wants people to "feel the raw model." **Boris Cherny (creator of Claude Code):** by December he stopped opening his IDE; **Opus 4.5 wrote all his PRs**. **Claude Cowork built in ~10 days, 100% by Claude** ("all of it").
  - **Google** — everything custom (Cider / Cider-V IDE fork; critique code-review; code search); "Jetski" (Google's Antigravity variant on the monorepo); prepping for **10× the lines of code** into production; NotebookLM, internal LLM playground, Moma.
  - **Amazon** — Amazon Q Developer Pro; "Kiro" (spec-based); **MCP servers everywhere** (API-first → MCP trivial); Claude hosted internally; PR-FAQ writing.
  - **Meta** — VS-fork; **"Trajectories"** (shows vibe-coded-diff prompt history in code review — mild privacy controversy; one engineer prompts in Polish so fewer colleagues understand).
  - **Traditional companies + independents** — surprisingly *higher* daily AI-tool usage than big tech (a central bank ahead of a tech-first company because "our mission is to understand them"). Independents: **Armin Ronacher** (creator of Flask, founding engineer at Sentry) prefers being an "engineering lead to a virtual programmer intern"; **Simon Willison** (Django co-creator) — "coding agents actually work now… run an LLM in a loop with compilers/tests/linters."
- **The December-2025 "breakthrough":** Karpathy Oct-2025 "models are just not there… it's slop" → Feb-2026 "programming is becoming unrecognizable… you're spinning up agents, giving tasks in English, reviewing in parallel." Adam Wathan (Tailwind), DHH (Rails), Jana(?) Dogan (Google distinguished eng), Mitchell Hashimoto (Ghostty; co-founder HashiCorp) all had breakthrough moments. **Simon Willison's cause:** Opus 4.5 + GPT-5.2 (Nov/Dec 2025) tipped an invisible capability line.
- **Open questions:** are token-burning devs actually more productive (a head of eng: "no real difference")? Willison — "it takes a surprisingly long time to get good at these tools"; "if you start with a theory of how LLMs work, it'll hold you back." Will code review / pull requests survive? **Peter Steinberger (OpenClaw; joining OpenAI):** "I don't like pull requests anymore… I prefer **prompt requests** — share the prompt, I'll run it myself and merge." Kent Beck (52 yrs programming): comparable to microprocessors→mainframe, internet, iPhone — but faster; what's cheap/expensive has flipped. Martin Fowler (Thoughtworks, *Refactoring*): won't wipe out software dev, but a change like assembly→high-level languages.
- **Conclusion:** LLMs will write most code everywhere, but **experienced engineers do the prompting/guiding/controlling**. Cursor research (Eric Z.): **senior engineers more effective with agents — agents AMPLIFY existing output, don't replace it.** Need much more **verification** (can't keep up by hand → tools like Sonar/SonarQube) + rebuilt infrastructure. **Less valuable skills:** language/framework-specific depth, implementing well-defined tickets, rigid adherence to old best practices. **More valuable:** curiosity/experimentation, business interest, strong fundamentals (to guide agents + know when *not* to hand over the wheel).

---

## 6 — Harrison Chase (LangChain), "The Future of AI Agents: Interrupt 2027" (`R9K2574YEAg`)

- **Two divergent agent types:** (a) **long-horizon** agents (run minutes→hours→days; code execution, planning, sub-agents, skills; driven by outcomes/goals) doing valuable knowledge work; (b) **low-latency customer-experience** agents (support/sales; brand + voice matter). Shared stack underneath — open question how much is shared vs particular.
- **Voice:** today's pipeline = STT → agent (text) → TTS sandwich; native **speech-to-speech** models emerging (OpenAI released a "v2"); not steerable enough yet for high-control apps, expected to change.
- **Sandboxes:** all agents (esp. long-horizon) need one — code isn't just software, it's data analysis, web browsing, image-gen, deep research ("give the marketing team a software engineer — what would it build?"). LangChain launched sandboxes.
- **Open models** rising: base open models approaching frontier on some tasks; cheaper (coding agents burn tokens fast); **trainable for your domain** (post-training on your traces).
- **Agent identity / auth:** two patterns — (a) act on behalf of an individual user (user credentials; different users see different things), (b) fixed credentials / service account (everyone sees the same). OpenClaw popularized the agent-as-its-own-thing with its own creds; some SaaS now let agents create their own accounts. Both futures coexist; being precise about which matters.
- **Continual learning (LangChain's biggest excitement):** improve the agentic system across **three layers** — **model** (e.g. fine-tune; Ramp + Prime Intellect fine-tuned a model for "Ramp sheets" — low latency, high accuracy), **harness** (code around the model; Deep Agents, Claude Code SDK; **"Meta-Harness" paper, MIT + Stanford** — an agent optimizes a coding harness on **Terminal-Bench 2**, outperforming human-written harnesses), **context** (agent.md, skills). **Evals + traces are the "training gradient"** for the harness/context layers (not literal gradient descent). LangChain moved **top-30 → top-5 on Terminal-Bench 2 by changing only the harness**. Announced **LangChain Labs** (research group) + LangSmith as the trace/feedback foundation.
- **Everyone builds agents:** the best agent-builders are the people who do the job (domain experts). **LangSmith Fleets** — no-code natural-language agent builder; **~200 built-in tools + Arcade partnership (~7,500 more) + MCP**; native in Slack/Gmail/Outlook; shareable like a Google Doc; credential/auth management; cost tracking + spend limits; **human-in-the-loop first-class**; model-agnostic; built on the **Deep Agents** open harness; downloadable to code. Demo: a go-to-market agent (Salesforce/BigQuery/Slack/Gmail; sub-agents + skills; HITL email approval) — 84% of the GTM team uses it weekly, lead→qualified up 240%, ~40 hrs/month saved per rep; originally engineer-built, rebuilt in Fleet so the GTM team owns it end-to-end without code.

---

## Cross-cutting thesis (what the bundle converges on)

Every talk, from different vantage points, says the same thing: **as agents absorb code *production*, the engineer's scarce work moves to the outer loop — deciding what's worth building, verifying fallible output fast, orchestrating parallel agents, and owning the result.**

- **Osmani** names it: answerability / verdict / "explain it or don't ship it"; inner-loop=capability, outer-loop=agency.
- **Karpathy** gives the mechanism: partial-autonomy apps + the generation-verification loop + keep-AI-on-a-leash + build-for-agents; "decade of agents."
- **Ng** gives the org shape: building blocks + PM-bottleneck + generalist collapse + no job apocalypse (demand goes up).
- **Cursor** gives the trajectory: tab→agent→teams; engineers become "agent managers"; review is the bottleneck.
- **Gergely** gives the field evidence: Dec-2025 breakthrough; senior engineers *amplified* not replaced; verification tooling required; "prompt requests."
- **LangChain** gives the systems view: continual learning across model/harness/context; **evals-as-forcing-function**; domain experts build their own agents.

**Convergent corollary: verification / judgment / accountability is the new bottleneck, and it does not parallelize** — which is exactly Osmani's "orchestration tax" and Karpathy's "I'm still the bottleneck."

---

## Claim inventory (→ verified in claims-scorecard.md via `wf_dabc1f67-f9f`)

**High-value / load-bearing (checkable):** Boris Cherny = Claude Code creator + role taxonomy; Sonar 2026 survey numbers (96% skeptical / half verify / clean-code-fewer-tokens); Paul Graham + Mitchell Hashimoto taste quotes; Wharton "73% + more sure" study; "Dex" software-factory talk; Ng 100%-AI + PM ratio + Fed-Philadelphia study + Context Hub authors + Code Dream/Realm name; OpenAI chat-completions "deprecated" (likely MISLEADING — older/not-recommended ≠ deprecated); Karpathy software-3.0 + vibe-coding-tweet + MenuGen + Waymo-2013; llms.txt / Vercel-Stripe markdown / MCP / GitIngest / DeepWiki; Cursor 15× / 30%-PRs / 75%-enterprise / 3M-LOC-browser / Star-Wars-Dykstraflex; Gergely bio + Zuckerberg + Wired; Opus-4.5 + GPT-5.2 Dec-2025; Cherny stopped-opening-IDE; Claude Cowork 10-days-100%-Claude; Codex >90%-self-generated + Tibo; Steinberger OpenClaw + OpenAI move + prompt-requests; Kent Beck 52yrs + Martin Fowler; Cursor senior-eng amplification (Eric Z.); Simon Willison (Django co-creator), Armin Ronacher (Flask/Sentry), Adam Wathan (Tailwind), DHH (Rails), Mitchell Hashimoto (Ghostty/HashiCorp); LangChain two-agent-types; Meta-Harness paper (MIT+Stanford, Terminal-Bench-2); Ramp+Prime-Intellect fine-tune; LangChain top-30→top-5; LangSmith Fleets + Arcade 7500 + Deep Agents; OpenAI speech-to-speech v2.

**Known caption garbles (corrected in wiki):** "re-bumbling" → *rebundling*; "Boris Cherney/Churnney" → *Boris Cherny*; "Michelle Hashimoto / Ghosty" → *Mitchell Hashimoto / Ghostty*; "Simon Willis" → *Simon Willison*; "Adam Wan" → *Adam Wathan*; "Armen Ronacher" → *Armin Ronacher*; "Andre Carpathy" → *Andrej Karpathy*; "Code Dream/Code Realm/Codoji" — product-name to be pinned; Steinberger "2019" year garble.
