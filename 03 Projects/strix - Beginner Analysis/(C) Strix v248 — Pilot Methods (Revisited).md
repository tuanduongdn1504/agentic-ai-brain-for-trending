# (C) Strix — v248 Pilot Methods (Revisited)

**The v190 pilot menu was never run.** This revisit does not re-issue 24 methods — it answers *why nothing happened* and gives a **short ladder by value ÷ risk**, with the load-bearing insight up front:

> The v190 pilot went unexecuted because Strix's trust model — an LLM driving real exploits in a privileged sandbox, on honor-system authorization, with telemetry on by default — collides with the operator's **ratified candidate-LLM legibility ADR** (any LLM path touching candidate data must be fixed / legible / audited / human-in-loop / eval-gated). A scan against hireui satisfies none of those clauses out of the box. **So the value is not a scan. It is the tool's knowledge, applied by hand.**

---

## Rung 1 — ⭐ DO THIS FIRST. Extract a hireui BOLA checklist from the skills. Zero install, zero egress, 2–4 h.

hireui's #1 documented risk is **broken object-level authorization (BOLA) — no authorization layer**, multi-tenant, candidate PII. Strix's `idor.md` (217 lines) and `broken_function_level_authorization.md` (154 lines) are a ready-made methodology for exactly that:

```bash
# read from the clone — nothing installed:
sed -n '1,120p'  "strix/skills/vulnerabilities/idor.md"
sed -n '120,217p' "strix/skills/vulnerabilities/idor.md"
cat "strix/skills/vulnerabilities/broken_function_level_authorization.md"
```

**Artifact you write:** a `hireui-bola-audit.md` mapping the skill's 6-phase procedure (build subject×object×action matrix → owner + non-owner principals → collect IDs → cross-channel → transport variation → consistency check) onto hireui's real endpoints (`/api/candidates/:id`, `/api/jobs/:id`, tenant-scoped resources). Cross-tenant isolation and composite-key (`{orgId}:{userId}`) references are called out explicitly in the skill. **Highest confidence, highest learning, no policy conflict.** Composes with the standing API-security thread ("BOLA authz absent = hireui #1 risk").

## Rung 2 — Borrow the code-enforced report gate into the candidate-LLM ADR. Zero install.

Read `strix/tools/reporting/tool.py:150-207`. The pattern — **a finding cannot be emitted unless `poc_script_code` + `evidence` + `assumptions` are non-empty and a full CVSS breakdown validates** — is the concrete shape your ratified ADR wants for hireui's first LLM feature: *no claim without required, structured evidence, checked in code.* Write it into the ADR as the "legible + audited" mechanism. (This is the exact inverse of v247's prose-only guard — cite both.)

## Rung 3 — Borrow the evidence-ladder-not-verdict discipline. Zero install.

`strix/tools/reporting/tool.py:1159` + the `reachability` enum: *"The level is an evidence ladder, never an exploitability verdict."* Apply to hireui's Match-Explain / candidate-scoring: record what the evidence shows on a **named ladder**, and never let a de-prioritisation signal read as a conclusion. Pairs with the wardrobe v217 confidence-scored-JSON template.

## Rung 4 — (only if a scan is genuinely wanted) one white-box quick scan of a LOCAL hireui clone.

Flags verified against `strix/interface/cli_args.py` and the scan-mode skills:

```bash
cd /path/to/hireui-scratch-clone          # NOT prod, NOT staging
export STRIX_TELEMETRY=0                   # off — default is ON
export STRIX_LLM="anthropic/claude-sonnet-4-6"
export LLM_API_KEY="sk-ant-..."            # metered; Claude has NO subscription path here
export STRIX_SANDBOX_MEM_LIMIT="4g"        # opt-in; default is UNSET/unbounded
export STRIX_SANDBOX_CPUS="2"
strix -n -t ./ --scan-mode quick --max-budget 5   # -n headless; --max-budget default is None(!)
# read strix_runs/<run-name>/penetration_test_report.md ; check run.json status + llm_usage.cost before trusting exit 0
```

Cost anchor (⚠️ from the repo's **stale v0.4.0** benchmark, treat as order-of-magnitude): ~$3.37/challenge → a quick scope is a few dollars. Do NOT pick the ChatGPT-subscription path (unofficial; and it isn't offered for Claude anyway). **Do NOT install the consumer skill** (`npx skills add …`) — its ambiguity default routes your agent to the paid cloud.

## Rung 5 — LAST, and only after 1–4. Authorized grey-box staging test of tenant isolation.

Authenticated staging, disposable tenants, budget-capped, telemetry off, findings → draft tickets (never auto-merged fixes). Governed by the ratified ADR and hireui's CONSTITUTION (I-8 operator-installs / I-2 `agent-*` branch / GitNexus-first). Never `--dangerously-skip-permissions`.

---

## FENCE (mandatory, unchanged from v190 and reaffirmed)

Authorized targets **only** (hireui / scratch — CFAA/GDPR exposure otherwise) · `STRIX_TELEMETRY=0` every run · `--max-budget-usd` every run (**default is off**) · set `STRIX_SANDBOX_*` limits (**default unbounded**) · prefer `pip install strix-agent` over `curl|bash` · `install-snapshot` first · scratch/staging never prod (DoS + the aggressive-testing collateral Ostorlab observed) · pin `strix-agent==1.5.3` · never let it touch real candidate PII (the ADR forbids it) · never cite its benchmark numbers (stale v0.4.0) · never assert the unverified founder/funding claims.

## The one-line answer

**Do Rung 1.** Read `idor.md`, write the hireui BOLA checklist by hand. It is the single highest-value, zero-risk, policy-compatible thing this repository offers you — and it is why the fancy pilot never needed to run.
