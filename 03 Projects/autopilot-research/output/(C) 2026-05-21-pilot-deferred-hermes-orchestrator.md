# Pilot deferred — Hermes + Codex + Claude orchestrator pattern

> **Status:** DEFERRED (not rejected) — decision-ready, parked for future
> **Date deferred:** 2026-05-21
> **Source artifact:** Nemanja Mirkovic, [Codex Builds. Claude Reviews. Hermes Agent Runs It.](https://www.youtube.com/watch?v=O-PEeD7fymo) (2026-05-20)
> **Companion repo:** [github.com/nemanjadotcom/goal-video-resources](https://github.com/nemanjadotcom/goal-video-resources)
> **Wiki cluster:** [[harness-engineering/personal-repo-hermes-orchestrator]] + [[harness-engineering/hermes-goal-mechanics]]
> **Audit:** `output/(C) 2026-05-21-subscription-billing-verification.md`

---

## Why deferred (not rejected)

The pattern is decision-ready and the pilot is cheap (~2h). The deferral is **scheduling**, not skepticism. The pattern remains a viable pilot candidate and the diligence done in this research arc means a future pickup costs only the pilot run itself — no re-research needed.

## Conditions that would trigger pickup

Pick up the pilot when ANY one of these happens:

1. **Storm Bear v66 mini-audit cadence** raises Pattern #76 (Adversarial Subagent Review) or Pattern #18 Layer 2 (Cross-Vendor Bridge) and an operational data-point would strengthen the audit.
2. **Independent N=2 evidence lands** on the orchestrator-mediated cross-vendor pattern-class (e.g., Droid-CLI-as-reviewer per @aichess.online comment, or any new sibling source). The cross-vendor pattern moves from N=1 to N≥2 and a pilot would calibrate operational claims.
3. **A real project task fits the pattern's sweet spot** (well-scoped greenfield build with clear acceptance criteria, where having a separate reviewer model meaningfully de-risks the output).
4. **Anthropic clarifies `claude -p` billing** in current versions (changelog / new help article / GitHub-issue resolution). If `-p` becomes OAuth-fallback by default, condition 2 of the env-hygiene rule disappears and the pattern becomes safer to adopt.
5. **>30 days elapsed** and the topic hasn't naturally resurfaced — a forcing function to either pilot or formally retire.

If none of the above fires by **2026-08-21** (3 months), revisit and decide: pilot, retire, or extend deferral with new conditions.

## Pilot runbook (ready to execute when picked up)

### Setup (~2 hours total)

| Step | Time | Action |
|---|---|---|
| 1 | 30 min | Install Hermes + Codex CLI + Claude Code CLI (host says Hermes can do this autonomously: *"Hey, I need you to install Cloud Code CLI and CodeX CLI so that I can log in with my subscription credentials."*) |
| 2 | 10 min | Authenticate both CLIs with native subscription auth (`codex login`, `claude` interactive first run for OAuth) |
| 3 | 5 min | Clone companion repo: `git clone https://github.com/nemanjadotcom/goal-video-resources` |
| 4 | 5 min | Copy `03-hermes-codex-claude/PROMPT.md` + `AGENTS.md` into a sandbox project workspace |
| 5 | 15 min | **Apply safeguards:** (a) Anthropic billing console → set "Extra usage" cap to **$0**; (b) in launching shell: `unset ANTHROPIC_API_KEY` then `env \| grep -i anthropic` (must be empty) |
| 6 | 15 min | Decide architecture variant: **demo path** (PROMPT.md's "Do NOT use Hermes profiles") OR **SOUL-profile path** (copy SOUL-*.md, accept the `claude -p` API-billing dependency) |

**Recommendation: start with the demo path.** Lower risk; mirrors what the video actually shows.

### Run (~1 hour)

1. Open VS Code with Hermes running.
2. `/goal` + paste PROMPT.md contents (with workspace path adjusted).
3. Step away — Hermes orchestrates Kanban + invokes Codex + Claude CLIs.
4. Return when status is "done" or "blocked."

### Verify (~15 min, the load-bearing step)

1. **Anthropic Console → API Usage dashboard:** any calls in the past 24h? If yes → env-hygiene leaked.
2. **Anthropic Console → Extra usage:** $0 consumed? Confirms the cap held.
3. **Anthropic Console → Subscription usage:** did the run register against subscription quota? Confirms OAuth path worked.
4. **ChatGPT subscription:** similar verification for Codex side (out of scope for this audit but worth doing).
5. **Output quality:** functional? matches PRD? compactions during run (count from Hermes Kanban)?

### Decide

| Verify result | Decision |
|---|---|
| Subscription used + cap held + output usable | ✅ Pattern works. Document as Tier-A pilot-confirmed. Storm Bear Pattern #76 N=2 evidence. |
| API billing leaked (any non-zero API call) | ⚠️ Architecture is conditional, not free. Either commit to env-hygiene discipline or only use no-profile demo path. |
| Cap hit / reviewer fails | ❌ Confirmed `claude -p` API-billing dependency in current Claude Code version. Pattern requires API budget OR alternative reviewer invocation. Decide: pay, find workaround, or retire. |
| Output quality poor | ❌ Pattern works mechanically but doesn't outperform single-model loop. Retire. |

## What already exists (no re-research needed when picked up)

- **Transcript artifacts:** [raw/2026-05-21-nemanja-codex-claude-hermes-orchestrator-transcript.md](../raw/2026-05-21-nemanja-codex-claude-hermes-orchestrator-transcript.md) + [raw/2026-05-21-nemanja-goal-vs-ralph-transcript.md](../raw/2026-05-21-nemanja-goal-vs-ralph-transcript.md)
- **Verbatim companion-repo artifacts:** [raw/2026-05-21-nemanja-goal-video-resources-repo.md](../raw/2026-05-21-nemanja-goal-video-resources-repo.md) (PROMPT.md + AGENTS.md + both SOUL files + 5 comment threads)
- **Architecture article:** [wiki/harness-engineering/personal-repo-hermes-orchestrator.md](../wiki/harness-engineering/personal-repo-hermes-orchestrator.md)
- **`/goal` mechanics + pilot cost analysis:** [wiki/harness-engineering/hermes-goal-mechanics.md](../wiki/harness-engineering/hermes-goal-mechanics.md)
- **Subscription-billing audit (6 sources, 3 conditions, corroborated by comments):** [output/(C) 2026-05-21-subscription-billing-verification.md](<(C) 2026-05-21-subscription-billing-verification.md>)

## Open empirical question (only resolvable by running)

**With both safeguards active (`$0` extra-usage cap AND `ANTHROPIC_API_KEY` unset), does the reviewer leg of the loop:**

- **(a)** succeed via OAuth fallback → architecture is genuinely cost-zero on current Claude Code versions
- **(b)** fail outright → confirms `claude -p` strictly requires API key, architecture is API-only by construction
- **(c)** hit the billing cap → would-have-billed-API; safeguard is the actual reason it's free

This is a 1-hour empirical test that the audit cannot answer from documentation alone. It is the single remaining unknown.

---

## Cross-references

- [[../wiki/harness-engineering/personal-repo-hermes-orchestrator]] — pattern architecture
- [[../wiki/harness-engineering/hermes-goal-mechanics]] — prerequisite mechanics + companion-repo audit
- `output/(C) 2026-05-21-subscription-billing-verification.md` — billing audit
- `raw/2026-05-21-nemanja-goal-video-resources-repo.md` — verbatim companion-repo artifacts
