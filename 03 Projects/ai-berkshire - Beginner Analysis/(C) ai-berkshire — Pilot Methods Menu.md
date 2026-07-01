# (C) ai-berkshire — Pilot Methods Menu (v187)

> **You asked: "I want to pilot to apply knowledge into my working flow — show me many methods."** Here are **24 methods**, laddered by effort/risk, across three surfaces. ai-berkshire gives you **two transferable things**: (1) a **reusable agent-engineering blueprint** (persona-differentiated parallel multi-agent orchestration + deterministic-tool-offload + a verification/exit gate + forced-verdict discipline + cross-harness distribution) — on-goal for Goal #1 and portable to software/hireui; and (2) the **value-investing knowledge itself** — personally useful and a template for building a skill collection in *your own* domain (recruitment).
>
> **Read the Deep Dive + Verdict docs first.** **Fence (applies throughout):** run `install-snapshot` before any install · **never `claude --dangerously-skip-permissions`** (the README suggests it — don't; approve tool calls) · pilot in a **scratch repo** before the vault/hireui · the tools are zero-dep Python (safe) but read `xueqiu_scraper.py`/install scripts before running · hireui work follows ITS CONSTITUTION (operator-installs per I-8, `agent-*` branch per I-2, GitNexus-first) · pin commit `0222260`.

---

## Surface A — First loop: understand the mechanics (zero/low risk)

**A1. Install to a scratch dir + read the 3 flagship skills.** `install-snapshot` → `git clone` (pinned) → read `skills/investment-team.md`, `skills/investment-checklist.md`, `skills/quality-screen.md`. Goal: internalize how a *domain-vertical skill collection* is structured (scenario-named entry points, embedded agent orchestration, mandatory tool calls, forced output shape). *~20 min, zero risk.* **← recommended start.**

**A2. Run `/dyp-ask` on a NON-investing question.** Install the commands, then ask `/dyp-ask Should hireui adopt a monorepo or split repos?` — watch how a **single-persona thinking-tool skill** frames a decision (circle-of-competence, inversion, "本分/do the right thing," honest "I don't know"). Cheap, safe, and shows persona-skill mechanics without touching finance. *~10 min.*

**A3. Hand-read the two reference tools.** Read `tools/financial_rigor.py` (deterministic-offload: `decimal.Decimal`, market-cap/valuation verification, Benford) and `tools/report_audit.py` (15%-sample publish gate with a 1% tolerance + CI exit code). These are the two most portable ideas in the repo — you'll re-implement them in B5/B6. *~20 min, read-only.*

---

## Surface B — Steal the agent-engineering patterns into software work (Goal #1, directly on-goal)

**B4. Build a 4-persona "code-review team" skill (mirrors `/investment-team`).** ⭐ Your strongest on-goal play. Clone the `investment-team.md` structure into a vault skill that fans out **4 parallel `general-purpose` subagents** on a hireui PR — **Correctness** / **Security** / **Performance** / **Maintainability** (the software analogue of the 4 masters) — each with a persona prompt + the same input diff, then a **lead synthesizer** that resolves disagreements into a **forced go / gray / no-go verdict**. This is a concrete artifact on your **multi-agent-orchestration pilot thread** (composes with the ExamPro deep-dive) AND real Goal-#2 evidence. *Scratch repo first, then a real hireui PR on an `agent-*` branch.*

**B5. Port the deterministic-tool-offload gate to software.** The `financial_rigor.py` insight = "make the model call code for what it guesses wrong." Identify *your* agents' unreliable spots — **token/cost arithmetic** (your `claude-api-cost-optimization` thread), **dependency-version claims**, **schema/type drift** (the Candidate-Detail token-drift bug!) — and write a tiny zero-dep Python gate the skill *must* call via Bash instead of asserting. *Half a day; high leverage.*

**B6. Port `report_audit.py` as a "PR/spec audit gate."** ⭐ Extract N% of the factual claims an agent makes in a PR description / spec / research doc, re-verify each against the **actual diff + tests + docs**, emit **PASS/FAIL with offending lines + a non-zero exit code**. This is your own `feedback_wiki_verify_independently_check_collisions` rule, *productized as a runnable CI gate* — the doubt-driven-development idea (agent-skills v184) with teeth. *Composes with how-we-claude-code's phase-3-verify.*

**B7. Adopt the "mirror test" as a spec-articulation gate.** Before building any hireui ticket, require the 5-sentence articulation: (1) what changes, (2) why it's the right change, (3) how it's verified, (4) blast radius, (5) rollback. **Can't fill all 5 → don't build yet.** A dead-simple FOMO/scope-creep killer that composes with cc-sdd (#1 pilot) and your Scrum practice. *Zero setup.*

**B8. Steal the A/B/C information-richness pre-rating for research agents.** Before an agent researches anything (a library, a competitor, a bug), have it first rate available-information A/B/C and *change strategy* — A: attack the non-consensus; C: first-principles, don't fake a complete answer. Kills the "confident but hollow" agent output. *Add to your research-skill preamble.*

**B9. Adopt the one-canonical-source → generated-formats distribution for `05 Skills/`.** If you ever want your vault skills to run under Codex or another harness, copy the `sync-codex-skills.py` pattern (canonical `.md` source → generated per-harness formats + a `--check` drift gate). *Only worth it if you go multi-harness.*

---

## Surface C — Domain-transfer: build a skill collection for hireui's OWN domain (Goal #2)

> The masterstroke: **ai-berkshire's architecture maps almost 1:1 onto recruitment.** hireui is a recruitment SaaS — a "candidate/company evaluation team" is both a genuine product feature *and* the exact 4-persona + forced-verdict + tracker pattern.

**C10. Build an "AI Hiring Committee" (the `/investment-team` analogue).** ⭐ 4 parallel persona-agents evaluating a candidate: **Technical Depth** / **Culture & Values Fit** / **Growth Trajectory** / **Risk & Red-Flags** → a lead synthesizer → a **forced Pass / Gray / No-Hire verdict** with tiered recommendations (strong-hire / hire-with-conditions / no) and a **"hiring mirror test"** (can you state the hire rationale in 5 sentences?). Structurally identical to the four-masters team; a real hireui feature. *The single most valuable domain-transfer here.*

**C11. Build the candidate "quality-screen" (7 knockout criteria + exemptions).** The `quality-screen.md` analogue: 5–7 hard disqualifiers (must-have skills, min experience, location/comp fit, integrity flags) that eliminate obvious no's in seconds, **plus exemption rules** for high-potential edge cases (the Meituan/Costco exemption logic). Inversion applied: *don't lose a great candidate, but exclude the definitely-not-qualified.*

**C12. Build a post-hire "thesis tracker" (Scrum-coach gold).** The `thesis-tracker.md` analogue for onboarding: at hire, write a ≤200-word "hire thesis" + 3–7 verifiable 30/60/90-day assumptions + severity-tiered red lines → score a **hire-health number** each check-in → add-responsibility / hold / coach / part-ways. Direct fit for your coaching practice + a retention feature.

**C13. Reuse `/private-company-research` for market/competitor intel.** Its "detective mode" (piece financials from scraps + confidence-tag every datapoint 🟢🟡🔴 + multi-method cross-check) is exactly how you'd research a competitor recruiter, a candidate's current employer, or a target market for hireui. *Skill logic transfers verbatim; swap the domain.*

---

## Surface D — Use the value-investing knowledge directly (personal; off-goal but you asked)

**D14. Run `/investment-checklist` on a stock you're actually weighing.** The 6-gate 10-minute go/deep-dive. *Personal use; remember DYOR — the repo is explicitly not investment advice.*

**D15. Run `/investment-team` on one company for a real 4-lens report.** See the full parallel-agent research pipeline produce an actual decision memo (business/financials/industry/risk + synthesis + Bull/Bear + price tiers).

**D16. Adopt the Kelly / half-Kelly sizing discipline.** Not just for stocks — the "no edge → allocate 0; some edge → half-Kelly; loss asymmetry means survival > max growth" logic applies to **any allocation decision**, including how you spread effort across projects. Read `公众号-凯利公式` in the repo.

**D17. Adopt the mirror test + thesis tracker for your own holdings.** The durable, domain-agnostic decision-discipline layer (the picks in the repo are time-bound; the frameworks aren't).

**D18. Read the "AI five-layer cake" report as a field map.** `AI五层蛋糕-产业全景研究` — energy → chips → infra → models → apps, ranked by certainty. A genuinely useful orientation to the AI-industry investing landscape (and to who's buying the compute your agents run on).

---

## Surface E — Apply to the knowledge base itself (meta / vault)

**E19. Turn your wiki-verify rule into a runnable gate.** Port `report_audit.py`'s extract→verify→verdict into a vault script that samples corpus-fact/collision claims from a draft ship and forces a PASS/FAIL — codifying `feedback_wiki_verify_independently_check_collisions` (which you already run by hand) as a tool.

**E20. Note the `ai_CLAUDE.md` ↔ your MEMORY.md parallel.** ai-berkshire keeps a hand-maintained session-memory file (user persona + history + corrections + known-issues). You already do this (`MEMORY.md`) — worth comparing structures; feeds your **CC-memory-systems** pilot thread.

**E21. Adopt its anti-bias principle block into the vault's research rules.** The `CLAUDE.md` "highest-priority" block (fact-vs-opinion separation, banned phrases "I think/obviously", present-both-sides, honest "I don't know") is a tight, reusable objectivity contract for any research skill.

**E22. Use `/wechat-article`'s author→editor→reader pipeline** as a template for producing polished vault outputs (or posts about your agent-engineering work) — a 3-role multi-agent content pipeline.

---

## Surface F — Scrum-coach specific

**F23. Build a "sprint-review team" skill.** 4 parallel persona-agents (Delivery / Quality / Team-Health / Stakeholder-Value) evaluating a sprint → forced verdict + action signals. Same `/investment-team` skeleton, coaching domain.

**F24. Use inversion + forced-verdict in facilitation.** Munger's "invert, always invert" = a pre-mortem tool ("how could this sprint fail?"); the anti-fence-sitting discipline = "no both-sides retros — name the call and the owner." *Zero setup, pure facilitation technique.*

---

## The ladder (where to actually start)

1. **A1** — install to scratch + read the 3 flagship skills (~20 min, zero risk). Internalize the blueprint.
2. **B4 + B6** — build the 4-persona code-review team + the PR/spec audit gate, on a scratch repo then a real hireui PR (`agent-*` branch). **← strongest on-goal play; concrete multi-agent-orchestration + Goal-#2 artifact.**
3. **C10** — the "AI Hiring Committee" for hireui: the domain-transfer masterstroke (real recruitment feature × the exact ai-berkshire architecture).
4. Then pick from B5/B7/C11/C12 (high-leverage engineering + product patterns) and, separately, D14–D18 if you want the investing knowledge for personal use.

**Honest note:** methods that touch hireui advance your standing **Goal-#2 PILOT lever** (still zero completed pilots since v153) — a completed B4/B6/C10 pilot on an `agent-*` branch would be the first real pilot artifact. The investing-knowledge methods (Surface D) are personally valuable but off the software-development goal.
