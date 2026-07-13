# (C) Pilot menu — applying `google-ai-studio-github-import` to your working flow

> **From:** wiki topic [[google-ai-studio-github-import]] (video: BizMate AI, *"Google AI Studio: Import GitHub, auto-redesign, deploy to Cloud Run"*, 2026-07-11).
> **For:** Storm Bear — the **hireui** recruitment SaaS (Goal #2: ship software with these tools) + vault harness work.
> **Date:** 2026-07-13.
> **How to read:** 11 methods in 4 tiers, each with *what / why / effort / risk / success signal*. Threads tagged: 💰 cost · 🔒 data-residency/privacy · 🎨 design · 🚢 deploy · 🧩 harness. Ranked recommendation at the bottom.

**The one big idea to carry across every method:** AI Studio Build is a genuinely fast **prototyping / exploration sketchpad** — and a **trap** if you follow the demo literally into production. Everything it shows is real; everything that matters for a regulated recruitment SaaS (data-training, residency, cost-beyond-free, one-way sync, source-of-truth lock-in) is the part it *omits*. So the play is: **harvest ideas, designs, and patterns from the sketchpad; build the real thing under hireui's own harness.** Two hard rules make that safe — **synthetic data only** and **billing-account attached** (so Google isn't training on you). See [[google-ai-studio-github-import/pricing-privacy-data]].

---

## Tier A — Try-it-this-week (your own account, zero hireui-repo risk)

### A1 · Stand up AI Studio Build + import a throwaway repo, baseline the loop 🚢
- **What:** Attach a **billing account** to a fresh Google Cloud project first (this flips you to the no-training "paid" classification — [[google-ai-studio-github-import/pricing-privacy-data|why]]). Then: New App → Build → Import from GitHub → import a **public, non-sensitive** Next.js repo → watch it auto-build → note what the importer restructured and what broke.
- **Why:** You can't reason about AI Studio for hireui until you've felt the real import→build→deploy loop and seen where it diverges from a normal Next.js dev flow (especially the **one-way sync** — [[google-ai-studio-github-import/github-import]]).
- **Effort:** ~1 hour. **Risk:** none (throwaway repo, synthetic).
- **Success signal:** a working imported app + a half-page of notes: what auto-installed, what the "runtime format" changed, whether push-back-to-GitHub worked, what you *couldn't* re-pull.

### A2 · Design-Variations exploration on a **sanitized** Candidate-Detail clone 🎨 ⭐
- **What:** Fork a **stripped, synthetic-data-only** copy of the Candidate-Detail screen (no PII, no secrets, mock candidates). Import it, then use **Design Variations + Annotation Mode** to generate 3-5 visual directions for the screen. **Extract the direction + tokens as inspiration** → implement properly in hireui under its rules (Figma SoT, locked plan paths, `agent-*` branch).
- **Why:** The active [Candidate-Detail refactor spike](../../..) is stuck on **drifted design tokens** + a half-done r1→r2 migration. This is exactly what a variant explorer is *good* at — cheap divergent options in minutes — without you committing to any of the generated code.
- **Effort:** ~2-3 hours. **Risk:** low, **if** you never ship AI Studio's code into the real component (fidelity risk on animated/stateful components is unverified — [[google-ai-studio-github-import/design-variations]]).
- **Success signal:** a screenshot board of 3-5 directions + a written "here's the direction + the 6 tokens I'm taking" note that feeds the real refactor. **This is the headline method.**

### A3 · Nano Banana asset spike (non-sensitive only) 🎨
- **What:** Generate placeholder illustrations / empty-state art / job-category icons for hireui with **non-sensitive** prompts (never candidate photos).
- **Why:** Real, immediate value; kills the "ugly placeholder" problem cheaply. Sibling of the [[ai-web-design-workflow/_index|Taste-Skill]] polish pass.
- **Effort:** ~1 hour. **Risk:** low. **Cost:** paid per-image (~$0.04-0.24). **Fence:** never send candidate photos/resume images to Nano Banana — that's PII egress.
- **Success signal:** a small set of reusable empty-state/illustration assets + a per-image cost note.

---

## Tier B — Deploy-layer & architecture (informs Goal #2)

### B1 · Cloud-Run one-click deploy as a **bake-off datapoint** 🚢💰 ⭐
- **What:** Deploy the A1 throwaway app via AI Studio's one-click **Publish → Cloud Run**. Time it, price it, probe the limits (2-app cap, region lock, no custom domain, redeploy behavior). Put the numbers **head-to-head** against the [[fullstack-docker-cicd/_index|fullstack-docker-cicd]] **A3 SSH-deploy Action** and the **E1 managed-vs-self-hosted** bake-off.
- **Why:** hireui's deploy layer is an open Goal-#2 decision. "Managed one-click (Cloud Run)" vs "self-hosted (Docker+SSH)" is a real fork; this gives you a concrete managed-side datapoint instead of hand-waving.
- **Effort:** ~half a day. **Risk:** low (throwaway app).
- **Success signal:** a comparison table — setup time / monthly cost at X req / lock-in / rollback story — added to the fullstack-docker-cicd deploy notes.

### B2 · Harvest the server-side-key pattern for hireui's first LLM feature 🔒
- **What:** AI Studio deploys with `GEMINI_API_KEY` as a **server-side secret**, never in the client bundle. Document this as the **reference architecture** for hireui's first LLM feature key handling (Secrets-Manager-injected env, server-only calls).
- **Why:** It's the concrete implementation of the [[jasonlee-claude-mobile-app/_index|"keys never client"]] ADR and the [[api-security-7-techniques/_index|api-security]] discipline — hireui currently ships `EXPO_PUBLIC_`-style plaintext risk patterns elsewhere, so codify the right one before the first key lands.
- **Effort:** ~1 hour (write-up). **Risk:** none (pattern extraction, not adoption).
- **Success signal:** a short ADR: "LLM provider keys are server-side-only, injected via secrets, never in any client bundle — enforced in CI."

---

## Tier C — Managed Agents / Match-Explain (WATCH & compare, don't build)

### C1 · Managed-Agents-vs-Claude-Haiku for Match-Explain — track for GA 🧩🔒
- **What:** Log Gemini **Managed Agents** (AGENTS.md/SKILL.md declarative, sandboxed) as a candidate *alternative provider* behind the planned [[mosh-ai-powered-apps/_index|Mosh A2 Match-Explain seam]] — but **do not adopt now**: it's preview, which **contractually forbids PII** and offers **no residency** ([[google-ai-studio-github-import/managed-agents]]). Write the eval criteria; revisit at GA.
- **Why:** Because the seam already abstracts the provider, this stays a **config swap, not a rewrite** later. Keeps your options open without betting the feature on a preview product.
- **Effort:** ~2 hours (eval-criteria doc + a diary note to re-check at GA). **Risk:** none.
- **Success signal:** a one-pager "Match-Explain provider options: Claude Haiku (build now) vs Gemini Managed Agents (watch, GA-gated) vs local Qwen (from local-ai pilot)" behind the same seam.

### C2 · Keep hireui's harness rules in the portable AGENTS.md / SKILL.md format 🧩
- **What:** Google Managed Agents, Anthropic Skills, and [[google-antigravity-skills/anthropic-agent-skills-portability|Antigravity Skills]] now **all** use the same `AGENTS.md` + `SKILL.md` declarative format. Author hireui's harness rules once in that format so they travel across Claude Code, Antigravity, and Gemini agents.
- **Why:** Cheap portability insurance; reinforces the "author once, stay portable" thesis the corpus keeps confirming.
- **Effort:** ~1-2 hours (normalize existing rules). **Risk:** low.
- **Success signal:** hireui's agent rules live in `AGENTS.md`/`.agents/*/SKILL.md`, loadable by any of the three harnesses.

---

## Tier D — Governance fences (protect the operator + the juniors)

### D1 · The AI-Studio fence ADR 🔒🚢 ⭐
- **What:** A CONSTITUTION addendum: **AI Studio Build is a prototyping-only tool.** Forbidden: (a) importing the **real hireui repo** (proprietary source through Google; trained-on unless billing-attached, and no residency guarantee even then); (b) any **candidate PII** through the free/unpaid tier (ToS-forbidden + trained + human-reviewed); (c) **deploying hireui production** via AI Studio→Cloud Run (source-of-truth conflict, region lock, no round-trip, no container export). Allowed: synthetic-data prototypes on a **billing-attached** account, design exploration (A2), asset generation (A3).
- **Why:** This video is *exactly* the kind a junior copies literally — and it would walk them straight into egressing candidate data and creating an un-syncable production deploy. The fence turns "don't do that" into an enforceable rule.
- **Effort:** ~1 hour. **Risk:** none — it's pure protection.
- **Success signal:** the ADR merged into hireui's CONSTITUTION; a junior reading it knows the exact green/red zones.

### D2 · Free-vs-paid tier gate (if Gemini API is ever used) 🔒💰
- **What:** If any Gemini API touches hireui, **code-enforce billing-attached** (paid classification → no training) and document the "**paid ≠ residency; residency needs Vertex AI + DPA**" fact. Add a startup assertion / CI check that fails if an unpaid-tier key is configured.
- **Why:** The free tier is one careless prompt from training Google on a candidate's data. Make it structurally impossible. Sibling of the [[api-security-7-techniques/_index|BOLA/authorization]] + keys-never-client gates.
- **Effort:** ~2 hours. **Risk:** low.
- **Success signal:** a failing test/boot-check when a non-billing Gemini key is present; the residency fact in the data-governance doc.

### D3 · Provenance-literacy teaching note for the team 📎
- **What:** Use this video as a 1-slide case study: *real tools, omitted caveats.* The lesson for juniors evaluating any AI demo — "the demo shows the magic; you find the compliance/cost/lock-in bill it skipped."
- **Why:** Cheap culture investment; mirrors the [[system-thinking-ai-coding/_index|design-before-prompt]] discipline and the [[google-ai-studio-github-import/source-provenance|docs-lag lesson]] (even our own verification agents fell for a lagging docs page).
- **Effort:** ~30 min. **Risk:** none.
- **Success signal:** a short "how we vet AI demos" note in the team wiki.

---

## Ranked recommendation

1. **A2 — Design-Variations on a sanitized Candidate-Detail clone** 🎨⭐ — immediate, real value, feeds the active refactor spike; do this first.
2. **D1 — The AI-Studio fence ADR** 🔒⭐ — do it *alongside* A2 so the boundaries are written before anyone gets ambitious.
3. **B1 — Cloud-Run bake-off datapoint** 🚢 — one afternoon, resolves a real Goal-#2 deploy-layer unknown.
4. **C1 + C2 — Managed-Agents watch + AGENTS.md portability** 🧩 — the forward-looking thread; no build cost now, big optionality later.
5. **A1 / A3 / B2 / D2 / D3** — fast supporting spikes; slot in as time allows.

**What NOT to do:** import the real hireui repo, put any candidate PII through AI Studio, or deploy hireui production via AI Studio→Cloud Run. Those are the D1 red lines — the exact things the video makes look easy and safe, and aren't.

## Next action
Run **A2** on a synthetic Candidate-Detail fork this week and write **D1** in the same sitting; bring the A2 direction-board to the next Candidate-Detail refactor session. Everything else can wait for a Goal-#2 deploy sprint.
