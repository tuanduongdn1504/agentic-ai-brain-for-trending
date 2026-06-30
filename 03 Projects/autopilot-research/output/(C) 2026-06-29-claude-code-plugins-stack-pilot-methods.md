# Chase AI's 17 Claude Plugins: Ranked Pilot Methods for Storm Bear

> **Source:** Chase AI — "Use These 17 Claude Plugins, It Will Make You 10x Better." ([V2RIVnGCy74](https://www.youtube.com/watch?v=V2RIVnGCy74), 2026-06-26, 17:30, 16.5K views).
> **Originals (all `gh api`-verified 2026-06-29):** Taste Skill `leonxlnx/taste-skill` 52.9K★ · Impeccable `pbakaus/impeccable` 42.2K★ · Awesome Design MD `voltagent/awesome-design-md` 94.2K★ · Ponytail `DietrichGebert/ponytail` 65.9K★ · notebooklm-py `teng-lin/notebooklm-py` 17.0K★ · Playwright CLI `microsoft/playwright-cli` 11.7K★ · Codex Plugin `openai/codex-plugin-cc` 21.8K★ · GWS `googleworkspace/cli` 29.1K★ · GitHub CLI `cli/cli` 45.0K★ · Skill Creator `anthropics/skills` 156.5K★ · Last 30 Days `mvanhorn/last30days-skill` 47.5K★ · Firecrawl `firecrawl/firecrawl` 141.1K★ · autoresearch `karpathy/autoresearch` 89.1K★ · Supabase CLI `supabase/cli` 2.3K★ · Obsidian `kepano/obsidian-skills` 38.8K★ · LightRAG `HKUDS/LightRAG` 37.1K★ · Stripe CLI `stripe/stripe-cli` 2.1K★.
> **Date:** 2026-06-29. **Operator:** Storm Bear (Karpathy LLM-Wiki maintainer ×2 vaults + `~/.claude` memory + Scrum coach + hireui/TalentAxis Goal #2).
> **Verification:** deep-dive + adversarial Workflow `wf_81b898cf-93e` (35 agents) + independent `gh api` ground-check. Full ledger: [source-provenance](../wiki/claude-code-plugins-stack/source-provenance.md). Companion wiki: [claude-code-plugins-stack](../wiki/claude-code-plugins-stack/_index.md) (12 articles).

---

## Headline Insight

**You already own more than half of this list — so the pilot story is "refine + add the 3 that matter," not "install 17 things."** Nine of the 17 are in your wiki, and **two are this vault's own foundation** (`karpathy/autoresearch` = the routine you ported; `teng-lin/notebooklm-py` = the engine your `yt-pipeline` runs on). That reframes the whole video: the real deliverables are a **verified map**, the **8 new tools**, and a **maintenance to-do** for the two you already depend on.

Among the genuinely new tools, three actually move your needles:

1. **Ponytail** — the highest-leverage *cheap* NEW pilot: a code-minimalism skill that cuts LOC/tokens/cost on agent output (−54%/−22%/−20% on Haiku, verified). It's the **code-gen discipline layer that composes orthogonally with your cc-sdd #1 pilot**, and it's a 1-hour install. This is your fastest "measured Goal-#2 cost evidence."
2. **Supabase CLI** — the single best **hireui Goal-#2 fit**: hireui is React/Next + TypeScript with zero LLM today, and Supabase is the clean data/auth on-ramp (candidate forms, recruiter auth, **schema → TypeScript types**). The sharp move: make the **generated DB types the source-of-truth for the Candidate-Detail data shape**, which attacks the documented token-drift root cause of your locked refactor spike.
3. **notebooklm-py upgrade audit** — pure self-maintenance: you're pinned to **v0.3.4** while current is **v0.7.2** (breaking changes between). Plus a 2-line correction to your own `notebooklm.md` ("bus factor = 1" → 27 contributors).

Everything else is reinforcement (you already run it), conditional (needs a hireui feature that isn't scoped), or a teaching artifact (the GWS firing).

---

## ▶ Start Here (3-Step Sequence)

1. **Week 1 — Ponytail on a sandbox + notebooklm-py upgrade audit (zero-to-low risk).** `/plugin install ponytail@ponytail` on a throwaway repo; run one task with it on vs off; eyeball the diff. In parallel, on a branch, `pip install notebooklm-py==0.7.2` in a *copy* of the autopilot venv and run the yt-pipeline smoke test (`yt-search` → `notebooklm source add` → `ask`) to see what breaks. **Measure:** Ponytail's LOC/token delta; whether v0.7.2 breaks the pipeline.

2. **Week 2 — hireui (Supabase, the systematize move).** Stand up `supabase start` locally; model the candidate/recruiter schema; run `supabase gen types typescript --local > types/database.ts`; refactor the Candidate-Detail data layer to consume those generated types as the SoT (per the locked phase-2 plan). Stay hireui-rooted (GitNexus + I-2 agent-branch + I-8 operator-installs). **Measure:** does data-from-schema eliminate the orphaned-token drift? mobile/web parity on the data layer?

3. **Week 3 — Ponytail on a real hireui feature + a design gate decision.** Run one TalentAxis ticket with Ponytail enabled on an `agent-*` branch, measuring token cost vs baseline (compose with `ccusage`). Separately, run the Candidate-Detail screen through **Impeccable's live editor vs your Taste-Skill gate** and pick one. **Measure:** the cost delta (Goal-#2 evidence) + which design tool earns a permanent slot.

---

## Ranked Methods Table

| Rank | Method | Flow | Effort | Value | First Step | Success Signal |
|------|--------|------|--------|-------|-----------|-----------------|
| 1 | **Ponytail cost-discipline on agent code** | A/C | Low | High | `/plugin install ponytail@ponytail`; one feature on/off | −20%+ tokens on the git diff; composes with cc-sdd |
| 2 | **Supabase CLI: schema → TS types as Candidate-Detail SoT** | C | Med | High | `supabase start` + `gen types` in hireui | token-drift root cause replaced by schema-driven types |
| 3 | **notebooklm-py v0.3.4 → v0.7.2 upgrade audit** | B | Med | High | branch-test v0.7.2 against yt-pipeline smoke test | upgrade path known; pin decision made with evidence |
| 4 | **Fix `notebooklm.md` "bus factor = 1" → 27 contributors** | B | Low | Med | edit the caveat (sole-owner risk, not solo) | caveat accurate; no stale fact in the skill |
| 5 | **Impeccable vs Taste Skill bake-off on Candidate-Detail** | C | Med | High | run `/impeccable audit`+`live` vs Taste gate on one screen | one design tool wins on Figma-parity; the other dropped |
| 6 | **Last 30 Days as an autopilot ingestion source** | B | Low | Med-High | `/plugin marketplace add mvanhorn/last30days-skill`; one brief | engagement-ranked signal adds value vs YouTube drains |
| 7 | **autoresearch lineage honesty + license note** | B | Low | Med | annotate the routine: metric is softer than `val_bpb`; MIT README-only | lineage citation is honest; license caveat recorded |
| 8 | **Codex Plugin as a 2nd-opinion review gate on hireui** | A/C | Low | Med-High | `/plugin install codex@openai-codex`; `/codex:adversarial-review` | dual-model review catches what Claude-only misses |
| 9 | **Playwright CLI QA on the Candidate-Detail flow** | C | Med | Med-High | add the CLI; capture screenshot+console per step | QA report w/ per-step evidence; ~4× cheaper than MCP |
| 10 | **GWS firing as a Scrum/harness org-resistance lesson** | D | Low | High | build a 1-slide case study from the Poehnelt story | team can name agent-adoption org risk concretely |
| 11 | **Skill Creator: formalize a fuzzy autopilot skill + evals** | B | Med | High | run Create→Eval→Improve on `yt-search`/`notebooklm` | eval-backed SKILL.md + pass-rate baseline (routine v2.2) |
| 12 | **Ponytail YAGNI ladder as a code-review teaching frame** | D | Low | Med | teach the 7-rung ladder as a review heuristic | team adopts "does this need to exist?" first |
| 13 | **Firecrawl-MCP as a cleaner bypass-403 ingestion path** | B | Low | Med | `npx -y firecrawl-mcp` for one bot-protected source | cleaner than ad-hoc scraping; sibling to bypass-403 skill |
| 14 | **Stripe CLI readiness check (conditional)** | C | Low | Low | grep hireui for Stripe; only invest if payments scoped | a yes/no on whether to learn it now |
| 15 | **Firecrawl candidate/job-scraping spike (conditional)** | C | Med | Med | only if a recruitment-data agent enters scope | bot-resistant scrape feeding a screening agent |
| 16 | **LightRAG candidate-profile RAG spike (conditional)** | C | High | Med | only if hireui adds resume/profile retrieval | graph-RAG over resumes; weigh vs NaiveRAG (2025 eval) |
| 17 | **"Works WITH vs INTO Claude Code" literacy lesson** | D | Low | Med | teach the shell-out-vs-native-skill distinction | team stops over-trusting "connect X to Claude Code" |
| 18 | **`gh` + `gh api` fluency check (you likely have it)** | A | Low | Low | confirm `gh auth status`; adopt `gh api` for ground-checks | agent-driven PR/issue ops + metadata verification |
| 19 | **Obsidian-skills install for agent format-fluency** | B | Low | Low | copy `kepano/obsidian-skills` into vault `.claude/skills/` | fewer malformed `.base`/`.canvas`/wikilink emits |
| 20 | **Pattern-Library evidence: log the new T4/T5 entrants** | B | Low | Med | file Ponytail/Impeccable/GWS/Supabase as audit evidence | new instances recorded at next mini-audit |

---

## Detailed Methods by Flow

### **Flow A — Personal Claude Code Harness**

**A1. Ponytail (rank 1).** The single best *new* pilot. `/plugin marketplace add DietrichGebert/ponytail` → `/plugin install ponytail@ponytail`. Run one task with `/ponytail full` vs `off`; inspect the diff and token report. **Why you:** it's the code-gen discipline layer that composes orthogonally with cc-sdd (methodology) — and gives you a *measured* cost number, which is what your Goal-#2 thread keeps lacking. **Measure with `ccusage`** ([[claude-code-observability]]) so "discipline overhead" is a number. **Caveat:** the "Opus is even more drastic" claim is unverified — run your own Sonnet/Opus test before promoting it.

**A2. Codex Plugin as a review gate (rank 8).** You've already got this catalogued ([[codex]] + Storm Bear v62). The refresh: it's **8 commands** (not 7 — `/codex:setup` was missed) and **ChatGPT Free works**. Add `/codex:adversarial-review --base main` as a 2nd-opinion gate on hireui `agent-*` branches; this is Pattern-#76 (adversarial review) evidence and composes with cc-sdd.

**A3. Skill Creator → eval a fuzzy autopilot skill (rank 11).** Run Create→Eval→Improve→Benchmark on `yt-search` or `notebooklm`; write 10–20 assertions from real failures (your [[prompt-evaluation]] discipline). Output: an eval-backed SKILL.md + a pass-rate baseline — a ready template for the long-pending routine v2.2 codification.

**A4. `gh`/`gh api` fluency (rank 18).** You almost certainly have `gh` (2.92.0 on the machine). The only "new" is adopting `gh api` for metadata ground-checks — which this very wiki build did to verify all 17 repos. Low value because it's already in your muscle memory; listed for completeness.

---

### **Flow B — autopilot-research + Storm Bear Vaults**

**B1. notebooklm-py upgrade audit (rank 3).** You're pinned to **v0.3.4**; PyPI is **v0.7.2** with breaking changes (retry behavior, exception hierarchy, return signatures, cookie auth). On a branch, install v0.7.2 in a *copy* of the venv and run the pipeline smoke test. **Decision:** upgrade (and refactor yt-pipeline) or keep the pin with eyes open. Don't upgrade blind.

**B2. Fix the `notebooklm.md` caveat (rank 4).** Your skill says "bus factor = 1 — solo maintainer." Verified: **27 contributors** (teng-lin is sole *owner*, so single-point-of-failure is at the release/gatekeeper level, not "solo"). Two-line edit; keeps your own docs honest.

**B3. autoresearch lineage honesty + license note (rank 7).** You ported autoresearch's design into your routine — accurately. Two refinements: (a) note that `val_bpb` is a *hard ground-truth* number while your `gaps_closed_ratio` is *judgment-based gap-counting* (be honest about the lineage's limit); (b) record that autoresearch's **MIT is README-only (no LICENSE file)** if you ever quote/vendor its code. See [[claude-code-plugins-stack/originals-this-project-runs-on]].

**B4. Last 30 Days as an ingestion source (rank 6).** `/plugin marketplace add mvanhorn/last30days-skill`. It's engagement-ranked, recency-bounded community research across 13+ platforms — a *different signal* than your YouTube-bundle drains. Free core (Reddit/HN/Polymarket/GitHub). **Pilot:** one weekly AI/LLM briefing; does upvote/odds-ranked sentiment add signal vs your fact-check/synthesis flow? **Note:** the "#1 GitHub Trending" claim is real (Mar 2026); the "cheaper-than-/deep-research" framing is the video's, not the docs'.

**B5. Firecrawl-MCP as a bypass-403 sibling (rank 13).** When a source is bot-protected, `npx -y firecrawl-mcp` (cloud) is a cleaner ingestion path than ad-hoc scraping — a sibling to your `bypass-403-escalation` skill. **AGPL caution** is moot here (you're calling the cloud API, not vendoring the core).

**B6. Obsidian-skills for agent format-fluency (rank 19).** Same as the [[claude-code-skills-stack]] B1 recommendation — copy `kepano/obsidian-skills` into each vault's `.claude/skills/` so the agent emits valid `.base`/`.canvas`/wikilinks. Low risk, low-but-real value. (Reminder: it's a *format* tool, not memory — the memory is your Karpathy pattern.)

**B7. Pattern-Library evidence (rank 20).** At the next mini-audit, log the new entrants: Ponytail + Impeccable (design/discipline skills), GWS (org-resistance-to-agents case), Supabase/Stripe (T5 infra). Ponytail's "prompt-as-engineering-artifact" framing is a sibling to Zen van Riel's `/smell` already in [[harness-engineering]].

---

### **Flow C — hireui Goal #2 (TalentAxis SaaS — the real-software target)**

> Execute hireui-rooted (GitNexus + Figma MCP + I-8 operator-installs + I-2 agent-* branch + BMAD). Adopt *architectures*, audit any third-party skill before install.

**C1. Supabase CLI → schema-as-SoT for Candidate-Detail (rank 2).** The standout. `supabase start` (Docker) → model the candidate/recruiter schema → `supabase gen types typescript --local`. Then refactor the Candidate-Detail data layer (per the locked `phase-2-candidate-screen-rework.md`) to consume the **generated types as the source-of-truth**, instead of drifting Figma tokens. This is the operator-fit critic's sharpest move: it attacks the *documented root cause* of your token-drift spike (data from the schema, not orphaned tokens), uses infra hireui needs anyway, and produces a real Goal-#2 artifact. **Caveats:** free tier auto-pauses after 1 week + no auto-backups (fine for the spike, plan around it for prod); the "natural language" is Claude Code + Supabase MCP, not the CLI.

**C2. Impeccable vs Taste Skill bake-off (rank 5).** Run the Candidate-Detail screen through **Impeccable** (`/impeccable audit` + the alpha `live` visual editor) and your existing **Taste Skill** gate ([[ai-web-design-workflow]]), against the Figma SoT. Pick one as the permanent design gate. The variable Impeccable adds is the **on-DOM live visual editor** — test whether that's worth a second tool. Don't keep both reflexively.

**C3. Playwright CLI QA on Candidate-Detail (rank 9).** Add the CLI (not MCP) for repeatable screenshot+console QA across the refactor's edge cases → a QA report with per-step evidence for Figma-vs-rendered parity. Reserve MCP for the one high-fidelity pixel-diff pass. (Already resolved in [[claude-code-skills-stack]]; this video just re-surfaces it.)

**C4. Codex adversarial review on hireui PRs (rank 8, see A2).** Dual-model review gate on `agent-*` branches.

**C5. Stripe CLI readiness check (rank 14, conditional).** Grep hireui for existing Stripe references. Only invest if payments (premium recruiter features / listing fees) are actually scoped — *currently unplanned*. If yes, local webhook testing in CI is the win.

**C6. Firecrawl candidate/job-scraping spike (rank 15, conditional).** Only if a recruitment-data/competitive-intel agent enters scope. Bot-resistant scraping (cloud Fire-engine, ~$0.006/page) feeding a screening agent ([[multi-agent-orchestration]]). **AGPL-3.0 flag:** don't vendor the open-source core into the proprietary SaaS (network-copyleft); use the cloud API or the MIT SDKs.

**C7. LightRAG candidate-profile RAG spike (rank 16, conditional, lowest priority).** Only if hireui adds resume/profile retrieval. Graph-RAG over resumes (multimodal via RAG-Anything). **Weigh honestly:** the 2025 meta-eval (arXiv:2506.06331) found NaiveRAG outperforms LightRAG under unbiased evaluation — so benchmark against a plain vector RAG first; don't assume the graph wins.

---

### **Flow D — Scrum Coaching / Teaching Teams**

**D1. The GWS firing as an org-resistance case study (rank 10).** Justin Poehnelt built a viral, genuinely useful tool and **was fired** — ~2 days after Google announced its own competing CLI, amid leadership fears that agents would disrupt the Workspace product. This is a sharp, *real* artifact for teaching **organizational resistance to agents inside legacy product divisions** — directly relevant to hireui's own agent-adoption risk profile and the [[harness-engineering]] "agent-manager role emergence" thread. One slide, big discussion.

**D2. Ponytail's YAGNI ladder as a review heuristic (rank 12).** Teach the 7 rungs (does-this-exist? → reuse → stdlib → native → dependency → one-liner → minimum) as a code-review *and* backlog-refinement frame ("the best code is the code you never wrote"). Maps to Definition-of-Done discipline.

**D3. "Works WITH vs integrated INTO Claude Code" literacy (rank 17).** Teach the distinction: most "Claude Code plugins" in roundup videos are CLIs you *shell out to*, not native skills. It changes setup expectations and stops teams from over-trusting "connect X to Claude Code" marketing. A small but durable literacy win.

---

## What to Consciously SKIP (and Why)

- **Don't install all 17.** Nine are already yours; the action is *refine the 2 you depend on + add the 3 that matter* (Ponytail, Supabase, Last 30 Days), not breadth.
- **Don't treat the design tools as additive.** You have the Taste Skill. Run the C2 bake-off and keep **one**. Impeccable, Awesome Design MD, and UI-UX-Pro-Max (from [[claude-code-skills-stack]]) are alternatives, not stack-ons.
- **Don't believe "Impeccable is built into GitHub Copilot."** It isn't — Impeccable added a Copilot *hook*; you still install + enable it. (And the live editor is *alpha*.)
- **Don't cite "autoresearch ran 83 experiments → 15 improvements."** It's not in the repo. And don't call it "ML for any app" — it's nanochat-pretraining-specific.
- **Don't expect Stripe CLI to have "natural language in Claude Code."** It has zero LLM features; you just shell out to it.
- **Don't self-host Firecrawl expecting bot-evasion** (Fire-engine is cloud-only) **or vendor its AGPL core into hireui.**
- **Don't assume LightRAG beats plain vector RAG** — a 2025 unbiased eval reversed its original benchmarks. Test before committing.
- **Don't lean on raw star counts** — Skill Creator's 156K and Firecrawl's 141K are gold-rush attention, not quality verdicts; Supabase's 2.3K is mature tooling, not obscurity.

---

## Critic's Reframe

Chase AI's video is a competent, mostly-honest beginner roundup with a paid-community funnel — and for *you specifically* it's an unusually low-novelty ingest: more than half the list is already in your wiki, and two items are the literal foundation of the project you used to build this analysis. That's not a knock; it's a signal that **your toolkit map is mature**, and the value of a video like this is now (a) catching the *new* tools early (Ponytail at 17 days old, Impeccable's live editor) and (b) catching the *errors* before they propagate (the Copilot claim, the "founder" claim, the "any app" framing, the "natural language" claims).

The durable contribution isn't "17 plugins." It's three moves that convert your perennial "N pilots ranked / 0 deployed" into deployed evidence: **Ponytail** (a measured cost number on agent code), **Supabase** (a real hireui data layer that fixes the token-drift you already diagnosed), and a **notebooklm-py upgrade audit** (maintaining the dependency your whole research loop rides on). Do those three; treat the rest as a verified reference shelf you pull from when a concrete need (payments, scraping, retrieval) actually arrives.

---

## Cross-Links to Sibling Wiki Topics

- **[claude-code-plugins-stack](../wiki/claude-code-plugins-stack/)** — the companion wiki (12 articles, full deep-dives + corrections)
- **[claude-code-skills-stack](../wiki/claude-code-skills-stack/)** — the sibling roundup (Eric Tech, 8 dev skills); overlaps on Awesome Design / Playwright CLI / Obsidian / Skill Creator
- **[ai-web-design-workflow](../wiki/ai-web-design-workflow/)** — the Taste Skill (Impeccable's rival); the C2 bake-off
- **[codex](../wiki/codex/)** — Codex-as-adversarial-reviewer (the plugin is the install path)
- **[claude-code-memory-systems](../wiki/claude-code-memory-systems/)** — Obsidian + LightRAG sit on this taxonomy
- **[claude-api-cost-optimization](../wiki/claude-api-cost-optimization/)** + **[claude-code-observability](../wiki/claude-code-observability/)** — measure Ponytail's token delta
- **[harness-engineering](../wiki/harness-engineering/)** — autoresearch ur-pattern + the GWS org-resistance lesson
- **[multi-agent-orchestration](../wiki/multi-agent-orchestration/)** — Firecrawl/LightRAG as a screening-agent's data layer
- **[prompt-evaluation](../wiki/prompt-evaluation/)** — Skill Creator's grader/comparator = LLM-as-judge

---

## Suggested Next Action

**This week:** A1 (Ponytail on a sandbox — 1h) + B1 (notebooklm-py v0.7.2 branch audit). **Report:** Ponytail's LOC/token delta on the diff; whether v0.7.2 breaks yt-pipeline.

**Week 2:** C1 (Supabase `gen types` → Candidate-Detail data-SoT spike, hireui-rooted under I-2/I-8). **Report:** does schema-driven typing eliminate the token-drift root cause?

**Week 3:** A1 on a real hireui ticket (Ponytail cost delta via `ccusage`) + C2 (Impeccable vs Taste Skill bake-off; pick one). **Report:** the cost number (Goal-#2 evidence) + the design-gate decision.

**Decision to tee up:** after Week 3 you'll have (a) a measured agent-code cost number, (b) a schema-driven Candidate-Detail data layer, and (c) one chosen design gate — three concrete deployments that finally move "N ranked pilots / 0 deployed" forward.

---

**File prepared for Storm Bear's vault. Most of this list you already run — the win is the 3 new tools that matter (Ponytail, Supabase, Last 30 Days), the maintenance on the 2 you depend on, and not getting fooled by the 6 corrected claims.**
