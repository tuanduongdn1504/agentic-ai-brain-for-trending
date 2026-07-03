# (C) Strix — Pilot Methods Menu (24 methods)

> **The ask:** *"pilot to apply knowledge into my working flow, show me many methods."*
> **The frame:** Strix is unique among recent corpus subjects — it's the **first one that's directly, natively pilotable against a real app you own (hireui)** as an authorized security tool. So this menu has a genuine Goal-#2 payoff, not just pattern-borrowing. But it's an **offensive** tool with no built-in authorization guard, so the **FENCE (bottom) is mandatory, not optional.**
> **Ladder:** A (read, zero-risk) → B (borrow patterns into your OWN vault/loop work, no Strix runtime) → C (low-risk scratch trials) → **D (authorized hireui security testing — the real payoff)** → E (meta/vault). Pick a rung; don't skip the fence.
> **AI-generated (Claude) — prefixed `(C)`.**

---

## ⚖️ Read first: the non-negotiable fence

1. **Only ever point Strix at something you own or are explicitly authorized to test.** hireui = yes (you own it). A scratch app you deployed = yes. **Anything else = no** (CFAA / cybercrime / GDPR exposure; the OSS CLI has *zero* authorization enforcement — the honor system is the only guard).
2. **`STRIX_TELEMETRY=0`** on every run (opt-out, default-ON; PostHog + Scarf otherwise get your scan metadata + severity counts + token spend).
3. **Set `--max-budget-usd` on every run** (it's OFF by default; ~$3.37/challenge on the benchmark → a deep scan of a real app can run into real money). Start at `--max-budget-usd 5`.
4. **Prefer `pip install strix-agent`** (inspectable) over `curl -sSL https://strix.ai/install | bash`. If you must use the installer, run the **`install-snapshot`** skill first. Docker required.
5. **Never run against production.** Deep scans can DoS the target (independently observed: DB connection-pool exhaustion). Use a **scratch clone / staging / local instance** of hireui.
6. **hireui work obeys hireui's CONSTITUTION:** operator installs tools (I-8), all agent work on an `agent-*` branch (I-2), repo-rooted, GitNexus-first. Never `--dangerously-skip-permissions`-style shortcuts.
7. **Pin `strix-agent==1.0.4`** (and note the sandbox image is tag-pinned only, `:1.0.0`, no digest — accept or pin a digest yourself).

---

## A — Read & learn (zero-risk, zero-install) — start here

**A1. Read the system prompt as a multi-agent-orchestration masterclass.** `strix/agents/prompts/system_prompt.jinja` is one of the best-written agent orchestration specs in the corpus: root-as-orchestrator, reactive nested spawning, one-job-per-agent, mandatory validation. ~30 min. Pairs with your `multi-agent-orchestration` pilot thread.

**A2. Read the Graph-of-Agents tools** (`tools/agents_graph/tools.py`): `create_agent`/`send_message_to_agent`/`wait_for_message`/`agent_finish`/`stop_agent(cascade)`. This is a clean, copyable reference implementation of a parent/child agent coordinator (inbox messaging, graceful cascade-cancel, permanent-stall guards).

**A3. Read 3 skill files + one scan-mode** (`skills/vulnerabilities/sql_injection.md`, `xss.md`, `idor.md` + `skills/scan_modes/standard.md`) to see the *structure* of a domain-vertical skill (attack-surface → detection → methodology → **validation** → false-positives → pro-tips). This is the format to steal into your own `05 Skills/`.

**A4. Gap-map: which parts of hireui's stack Strix already has skills for.** It ships `frameworks/{fastapi,nestjs,nextjs}` + `technologies/{supabase,firebase_firestore}` + `protocols/graphql`. Compare to hireui's actual backend/API stack → know in advance which vuln classes Strix will be strong on.

---

## B — Borrow the patterns into your OWN work (no Strix runtime) — highest ROI, zero risk

**B5. The maker/checker validation agent → strengthen your `loop-verifier`.** Strix's *"validation is mandatory — never trust scanner output, always validate with a PoC; independent verification through a subagent"* is exactly your v189 REJECT-first `loop-verifier`. Steal the framing: **a finding isn't real until a *separate* agent independently reproduces it.** Add "reproduce, don't trust" language to your `loop-verifier` agent.

**B6. The tool-call / lifecycle termination contract → your loop STATE discipline.** Strix: *"a text-only turn immediately ends the run with no report written; the lifecycle tool is the only valid termination."* This is the durable-state lesson your loop conventions encode. Cross-reference it in `loop-constraints.md` as an external corroboration.

**B7. The progressive-disclosure skill format → your `05 Skills/`.** Adopt the frontmatter (`name`/`description`) + body-of-methodology + explicit "validation / false-positives" section for your own skills. It keeps skills scannable + on-demand-loadable (the `load_skill` idea).

**B8. The `create_vulnerability_report` schema → a "finding" record for any review loop.** CVSS-3.1 + PoC-required + `fix_before`/`fix_after` verbatim diffs + LLM-dedup. This is a great template for *any* agent that produces reviewable findings (not just security) — e.g. your code-review meta-skill or the ai-berkshire v187 "AI Hiring Committee" verdicts.

**B9. A "security-sweeper" loop for the loop-engineering pilot.** Strix's CI diff-scope gate (`strix -n -t ./ --scan-mode quick`, exit 2 on findings) is a ready-made **8th loop pattern** to add to your loop menu — a scheduled/PR-triggered security sweep that reports (L1) before it ever blocks (L2). Composes with the D16 PR-babysitter: the babysitter watches PR *hygiene*, a Strix sweep watches PR *security*. Start at **report-only (L1)** per your own graduation bar.

**B10. The `--max-budget-usd` estimate→stop guard → your `loop-budget` + cost-opt spec.** Strix checks cost after every LLM response and stops cleanly at a dollar cap. Wire the same idea into hireui's `claude-api-cost-optimization-spec` (you already have the 80%/100% pattern) — a concrete external example of a per-run USD ceiling.

---

## C — Low-risk local trials (install, scratch target — NOT hireui yet)

**C11. Install into a scratch env + `install-snapshot`.** `pip install strix-agent==1.0.4` in a throwaway venv (or the `curl|bash` after running the `install-snapshot` skill). Confirm Docker + pull the sandbox image. Read the report format it generates.

**C12. Run against OWASP Juice Shop (a deliberately-vulnerable app you deploy locally).** `STRIX_TELEMETRY=0 strix -n --target http://localhost:3000 --scan-mode quick --max-budget-usd 3`. This is the safe way to see Strix actually find + PoC a real (intentional) vuln without touching hireui. Watch the live agent-graph in the TUI (drop `-n`).

**C13. Point it at a scratch copy of your OWN simplest service** with `--scan-mode quick` + a tight budget. Confirm the workflow end-to-end (recon → discovery → validation → report) on something you own but don't care about, before hireui.

**C14. Read a full generated report** (`./strix_runs/<name>/penetration_test_report.md` + the per-vuln `.md` files). Judge PoC quality + false-positive rate yourself — this is how you decide whether to trust it on hireui.

---

## D — Authorized hireui security testing (the real Goal-#2 payoff) — fenced

> hireui is a TalentAxis recruitment SaaS you own → **authorized.** This is where Strix does something no prior corpus subject could: give your Goal-#2 app a real, automated, PoC-validated security pass. Do it on a **scratch clone / staging**, on an `agent-*` branch, per hireui's CONSTITUTION.

**D15. White-box quick scan of the hireui repo (scratch clone).** `STRIX_TELEMETRY=0 strix -n --target ./hireui-clone --scan-mode quick --max-budget-usd 5 --instruction-file ./rules-of-engagement.md`. Start with the **backend/API** (where real vulns live — IDOR, auth, injection), not the RN frontend. Triage findings into tickets; ignore noise.

**D16. Focused scan on hireui's highest-risk surface.** `--instruction "Focus on IDOR, broken access control, and auth/JWT on the candidate + recruiter APIs"`. Recruitment SaaS = multi-tenant PII → **IDOR / broken-function-level-authorization** is the #1 real risk. Strix's `idor` + `broken_function_level_authorization` + `authentication_jwt` skills target exactly this.

**D17. A `security-sweeper` PR gate on hireui (L1 report-only first).** Add the GitHub Actions step (`strix -n -t ./ --scan-mode quick`, secrets `STRIX_LLM`/`LLM_API_KEY`) on `agent-*` PRs. **Run it report-only for ≥2 weeks** (comment findings, don't fail the build) — your own loop graduation bar — before letting exit-code-2 block a merge. Composes with D16-of-v189 (the PR-babysitter).

**D18. Use the auto-fix + PoC output to *seed* tickets, not to auto-merge.** White-box mode proposes `fix_before`/`fix_after` diffs. Treat them as **draft PRs a human reviews** (per hireui I-2/I-8) — never auto-apply a security "fix" from an Alpha tool.

**D19. Grey-box authenticated testing of a hireui staging instance.** `strix --target https://hireui-staging.internal --instruction "Authenticated testing as recruiter role: <creds>. Test tenant isolation + privilege escalation between recruiter and candidate roles."` This catches the business-logic + multi-tenant-isolation bugs static analysis misses. **Staging only, never prod** (DoS risk).

**D20. Route the backend at Claude.** `STRIX_LLM=anthropic/claude-sonnet-4-6` (or Opus) — you're on Goal #1 (mastering Claude for autonomous agents) *and* you get Anthropic's stronger reasoning on the hardest vuln-chains. Compare cost/quality vs the GPT-5.4 default on a fixed scratch target (feeds your cost-opt thread).

---

## E — Meta / vault

**E21. Compare Strix's Graph-of-Agents to your own workflow fan-outs.** You just ran a 12-agent read-only workflow to build *this* wiki. Strix's reactive-nested-spawning + inbox-messaging + cascade-cancel is a more dynamic model than your barrier/pipeline fan-outs — a reference design if you ever build a long-running vault agent-tree.

**E22. Harvest the security-vertical skill-authoring approach for a vault "self-audit" skill.** Strix's `coordination/source_aware_whitebox.md` (static-triage → prioritize → dynamic-validate → evidence-driven) is a transferable *methodology* skill, not just security-specific.

**E23. Feed the "AI Hiring Committee" (ai-berkshire v187 idea) with Strix's specialist-spawn model.** ai-berkshire's `/investment-team` = 4 parallel persona agents; Strix's `create_agent(skills=[...])` = reactive specialist spawning. Combine: a hireui recruitment feature where specialist agents (screener / culture-fit / technical) spawn per candidate and a validator agent must confirm each verdict — the maker/checker discipline applied to hiring.

**E24. Log the honest limits so you don't over-trust it.** Alpha-labeled; benchmarks vendor-run; 25% miss on hard vuln-chains; "complement not replace human review"; the primitives are third-party tools. Strix is a **first-pass amplifier + PoC-validator**, not a certifier. Put this line in the hireui `.pilot-log` if you run D15+.

---

## Recommended path (if you do one thing)

**B5 + B7 (borrow the maker/checker + skill format, ~1 hr, zero risk) → C12 (Juice Shop smoke test, prove the loop) → D15/D16 (a quick white-box scan of hireui's API on a scratch clone, `agent-*` branch, budget $5, telemetry off) = your first completed Goal-#2 security artifact.** Then D17 as a report-only PR sweep alongside the v189 PR-babysitter. Everything else is optional depth.

*Fence recap: authorized targets only · telemetry off · budget set · pip-install + install-snapshot · scratch/staging not prod · hireui per its CONSTITUTION · pin 1.0.4.*
