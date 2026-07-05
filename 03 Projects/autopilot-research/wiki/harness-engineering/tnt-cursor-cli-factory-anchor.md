# TNT (Trung Tran) — Cursor-CLI factory: first-party VN talk + public end-to-end repo

> **10th individual-scale sibling** — and the first in the layer to pair a first-party talk with a **fully public, inspectable factory repo** (harness + specs + generated app + run ledgers + git history, all in one place).
> **Source pair:** talk `LaIZ4yRd7mA` "AI Harness Engineering | Góc nhìn cá nhân và quick demo | FPT HCM 28/06/2026" (46:17, 1,993 views at fetch, channel TNT) + repo `trannamtrung1st/ai-engineering-learning` → `projects/ai-harnessed_we-event-app` (created 2026-06-24 — **4 days before the talk**; TypeScript; 6★; no license; still active, pushed 2026-07-05).
> **Compiled:** 2026-07-05, workflow `wf_3740e2d5-2b4` (22 agents ~1.55M tokens; 6 dives + 3 external verifiers + 12 refute-first claim verifiers + critic). Raw: `raw/2026-07-05-tnt-harness-fpt-talk-and-we-event-repo.md`.

## Who

- **Trung Tran** (GitHub `trannamtrung1st`, HCMC, 70 public repos; YouTube channel TNT `@TNT-nz5be` is his personal channel — VERIFIED).
- Works at **Web Synergies** (Singapore IT/DX company, **Yokogawa** subsidiary — acquisition completed ~May 2025 per ARC Advisory; prior investment Oct 2021), IoT domain, full-stack engineer. ⚠️ Auto-caption garble said "Western Synergy" — CORRECTED by verify agent (discard-as-garble guard rule 1: searched before discarding).
- Explicit humility framing: ~1 year applying AI at work, "không phải chuyên gia", presents "góc nhìn cá nhân" and warns the audience his harness is "not a standard to copy — understand the idea, build your own".
- Venue: FPT University HCM library, 2026-06-28 workshop with lecturers (thầy Hoàng, thầy Phương gave the theory session before him; a later session demos a requirements-phase harness-generating tool — not identified, not ingested).

## The talk's conceptual contribution

1. **Four guiding questions** that motivate harness engineering (each maps to a mechanism in his repo):
   - Is the output *actually* correct, or does it just look correct? → checked against requirements, not vibes (test-case artifacts per requirement tag).
   - Will the same prompt produce correct results *across runs*? → probabilistic model ⇒ per-run gates, not per-prompt trust.
   - Can I enhance/refactor without regressions? → whole-app backlog + re-queue slices + browser regression gate.
   - Can I *detect* unintended changes? → computational checks + review gate + doc-fingerprint drift detection.
2. **Prompt → context → harness** progression, told through a live audience poll (one student had reached context engineering; Trung pushes the next step: even perfect docs don't guarantee compliance — you need the *checking environment*). Matches Archon's prompt→context→harness evolution thesis ([[archon-harness-builder-anchor]]) with zero citation lineage — independent convergence.
3. **Goal-first harness definition** (his strongest framing): a harness succeeds when (a) the *harness*, not the human, checks correctness; (b) failures produce **agent-readable feedback**; (c) the loop repeats until fully correct. Then the question flips: not "how do I make AI generate correctly the first time" but **"when AI generates wrong, does the system detect it, feed back, and converge?"** — accept wrong at attempts 1–3, converge by 4–6.
4. **Validation vs evaluation distinction** (formalized in the repo as separate gates): *validation* = computational checks + browser tests (binary, machine-decidable); *evaluation* = reviewer judgment (scope, completeness, minor-vs-critical, "80/100 checks passing may still be a pass if the 20 are minor — unless one is critical"). See [[tnt-we-event-harness-mechanics]].
5. **Human role redefinition**: during the build he **never edits code and never prompts "fix this bug"** — he only improves the harness (docs, context, tools, scripts). Confirmed empirically: zero human app-code commits in 687-commit history ([[tnt-factory-run-empirics]]).
6. **Honest non-answers**: token optimization — "even the big players can't guarantee it; monitor with-harness vs without-harness, and token usage must be paired with quality" (no numbers offered). This honesty profile matches the corpus' anti-hype cohort (Zen van Riel's scale-honesty).

## Economics (verified)

- Stack: **Cursor CLI** (`agent` binary) + **Auto model** + Playwright MCP. NOT Claude Code — first full factory in the individual-scale layer on a non-Claude agent CLI.
- His claim: runs the loop all day + overnight on a **~$200/year** Cursor plan with Auto included. VERIFIED: Cursor Pro annual = $16/mo = **$192/yr** (cursor.com/pricing), and official docs state **"Auto mode is unlimited on all paid plans"** and **"Auto does not cost credits"** (cursor.com/docs/models-and-pricing). This is the strongest *verified* cost-arbitrage datum in the topic — cf. the subscription-economics thread in [[harness-economics-and-tos-timeline]] (Anthropic side is contested; Cursor's Auto lane is officially sanctioned).
- His "Auto has thinking/reasoning" aside: UNVERIFIABLE from official docs (Auto routing is deliberately vague) — keep as speaker observation.

## Corrections & caption-garble ledger

| Heard in auto-captions | Actual | How resolved |
|---|---|---|
| "Western Synergy" | **Web Synergies** (Singapore, Yokogawa subsidiary) | Web search per discard-as-garble guard; ARC Advisory acquisition note |
| "cơ sơ" | **Cursor** | repo ground truth (`agent` CLI, `.cursor/mcp.json`) |
| "play MCB" | **Playwright MCP** | `.cursor/mcp.json` single server entry |
| "slide" / "lá c" | **slice** (backlog work unit) | `whole-app-backlog.json` |
| "hold app backlock" | **whole-app-backlog.json** | repo file |
| "AIH prefix" | `aih:` commit prefix | 566/687 commits |
| "$200/year" | $192/yr Cursor Pro annual | cursor.com/pricing |

## Verification ledger (highlights; full in workflow record)

- CONFIRMED: Cursor CLI binary `agent`, install cmd, OAuth login, `stream-json`, MCP enable, `-p`/`--force` flags (with community-documented `-p` hang issues — see mechanics article for why his watchdog exists); Auto-unlimited-no-credits; identity; FPT event; personal channel; 16.6-min median slice cadence; 40.5% overnight commits; zero human app-code commits; `web-event-cover-image` demo slice commit `161edee` (2026-06-27 18:02) — the exact feature he reverted and rebuilt live on stage.
- REFUTED (dive-agent misfires caught by refute-first pass): "drift check runs only at loop start" (it runs **every iteration**, `ralph-once.sh` lines 25–46); "Vitest runners" (actually **Node native `--test`**); "talk says docs were AI-generated" (talk doesn't say it — he says he "already had" the docs; the repo's `docs/brds/prompt.md` and the hesd docs family's 70–85% AI-likelihood assessment are separate, repo-side evidence).
- PARTIALLY-TRUE: reviewer read-only enforced via Cursor `--mode plan` + prompt boundaries (best-effort, not sandbox-hard); Ralph-loop lineage (zero citations in repo — community vocabulary adopted without provenance).

## Key takeaways

- The strongest single idea for practitioners: **design the harness goal first** (harness-checks / machine-readable-feedback / loop-until-correct) and only then choose techniques — any technique that meets the goal is acceptable.
- The verified pair (public repo + git ledger + talk) makes this the corpus' most *auditable* individual-scale factory claim: cadence, overnight runs, and no-human-code-edits are all checkable, and check out.
- Cost floor for an unattended factory is now a **verified $192/yr** (Cursor Auto lane), not an estimate.
- His meta-answer on harness authorship — *vibe-code the harness itself, then understand it incrementally through use* — is a distinct authoring posture vs Archon's install-a-builder and cc-sdd's adopt-a-framework ([[tnt-vs-corpus-positioning]]).
- MVP scope-guard self-check inside `docs/brds/prompt.md` (out-of-scope feature? non-canonical state? rule broken? audit missing?) is a portable 5-line artifact.

## Related

[[tnt-we-event-harness-mechanics]] · [[tnt-factory-run-empirics]] · [[tnt-vs-corpus-positioning]] · [[archon-harness-builder-anchor]] · [[personal-repo-tu-ba-khuym-getting-started]] (the other VN first-party voice) · [[harness-economics-and-tos-timeline]]
