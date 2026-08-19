# (C) Strix — v248 Verdict

**`usestrix/strix` @ `0478a69a` (v1.5.3, 2026-08-18) — corpus-recursive REVISIT of v190 (`e6ca4d2`, 2026-07-03).**

## Classification

- **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
- **(a) FAIL (§41):** author `usestrix` / Cactus-of-security-startups is **not Anthropic**; Claude is one-of-8 LiteLLM backends and **not the default** (`openai/gpt-5.4` is the docs example); no declared affiliation, no (a)-7 vendor axis. Dominant committer **Ahmed Allam / 0xallam**. #19 19a.
- **(b) STRONG:** Strix IS an autonomous multi-agent system (Goal #1) and is the first corpus subject natively, authorizedly pilotable against the Goal-#2 target (hireui) as a security tool. ⚠️ MODERATE-on-the-security-*vertical* reading recorded reviewable (as at v190).
- **(c) STRONG:** 168 Python files / a real async multi-agent coordinator / per-scan Kali Docker sandbox + Caido MITM sidecar + ~60 tools / 60 internal skills / a **code-enforced report-validation gate** / SARIF 2.1.0 / a Go/Bubble Tea TUI / 8 providers / v1.5.3 / 27 tags. Caveats: PyPI classifier still **Alpha**, benchmark **stale (v0.4.0 vs v1.5.3)**, no programmatic authorization, telemetry default-ON.
- **(d) STRONG:** shannon v45 (the offensive-pentester N=1 anchor) · SkillSpector v169 (defensive counterpart) · magika v44 · Anthropic-Cybersecurity-Skills v98 · OpenHands v30 / AutoGPT (T5 + Docker) · browser-use v41 / Skyvern v24 / crawl4ai v29 (via `agent_browser`) · the multi-agent-orchestration + claude-api-cost-optimization + loop-engineering v189 threads · #66 dual-use.

## Mint decision — **NO NEW MINT; counts 46/11 UNCHANGED**

- **§C row 92** *"Autonomous Multi-Agent Offensive AI Penetration-Testing System"* already lists **Strix v190 as its N=2 anchor** (with shannon v45's credited priority). A revisit of an existing anchor **adds no N** and there is no independent 3rd instance here → **no promotion; the row stays N=2** (promotion-eligible at a genuine, independent N=3). §C live standalones **51 unchanged**; surface ≈58 unchanged.
- **Two new capability shapes → WATCH, not mint:** Shape A (vendor consumer-skill routing to a paid tier) = rare-not-novel, form-factor-within-a-genre, N=1 → DEFERRED watch axis; Shape B (in-app ChatGPT/Codex subscription-OAuth consumption) = not novel + distinct-from-the-gateway-row-100 → watch/cross-ref, not mint.
- **NON-claims:** NOT corpus-first (shannon v45 precedes) · NOT #52 (page-stated ~19k★ §37.4; the XBEN 96% is a *capability* benchmark, vendor-run, and **stale at v0.4.0**) · NOT #57 (uses Claude/OpenAI/Gemini as backends + integrates nmap/nuclei/sqlmap/Caido/LiteLLM/Playwright; mentions/deps ≠ recursion) · NOT #18 B1-MCP (consumes tools; the managed platform's MCP is out-of-repo) · NOT a new top-level pattern (max #85).

## What the revisit changed in the vault's own record

1. **CORRECTED v190's telemetry claim** — the recorded README-vs-code *"discrepancy"* was a **misreading** (severity counts ≠ vuln details; token counts ≠ requests). An **under-disclosure of what is tracked**, not a violation of the never-collect promise; and at HEAD the disclosure was widened to match the code. The v190 registry row carries a correction note.
2. **UPGRADED the "no-exploit-no-report" finding** — v190 recorded it as prose *doctrine*; it is a **code-enforced validation gate** (`tools/reporting/tool.py:150-207`, `poc_script_code`/`evidence`/`assumptions` required). The **exact inverse of v247**.
3. **RECORDED the product-shape shift** — CLI (v190) → agent-installable skill (`npx skills add usestrix/strix`, added 2026-08-06), Claude Code named first in the README.
4. **RECORDED the pilot was never run** — and that the tool is genuinely apt for hireui's #1 (BOLA) gap, so the non-execution reflects a **trust-model / ratified-policy misalignment**, not low value.

## Security posture (fair)

- **No broken-auth triad on the OSS CLI** in the v231/v232 sense: the sandbox binds exposed ports to `127.0.0.1` (`runtime/docker_client.py:219`); the credential file is `0600`. But note the **premise**: this is an offensive tool driving real exploits, and **authorization is honor-system prose only** (`README.md:352-353`) — standard for the pentest genre (Metasploit/Burp do the same), stated as characterisation not accusation.
- **Sandbox is broadly privileged by design:** `NOPASSWD:ALL` sudo for the `pentester` user (`containers/Dockerfile:36`), unconditional `NET_ADMIN`/`NET_RAW`, and **resource limits opt-in / unset by default** (a runaway can pressure the host unless `STRIX_SANDBOX_MEM_LIMIT`/`CPUS`/`PIDS_LIMIT` are set).
- **Supply chain — mixed:** strongest = GitHub Actions all **SHA-pinned** with least-privilege permissions + Go modules exact-pinned; weakest = the sandbox image is a **tag not a digest** (`ghcr.io/usestrix/strix-sandbox:1.3.0`), `litellm`/`docker`/`requests` unpinned upper bounds, `curl|bash` install with no signature, and a **self-updater that skips checksum verification when no digest is published**. `pip install strix-agent` is the inspectable alternative.
- **The headline caveat:** the OSS CLI hardcodes `authorization_source="strix_platform_verified_targets"` and tells the model *"never question your authority"* — a real refusal-suppression mechanism that a naive operator should understand before pointing it anywhere.

## Streak / governance

- **Streak: v247 `GA:105` → `GA:106 · OG:13 [7 ov]`** (**29 consecutive GA**, v220→v248). A revisit counts as a ship (v228/v242/v245 precedent).
- **§35 CLEAR** — window {v246 GA, v247 GA, v248 GA} = 0 OG. No override consumed (§40 not even invoked; cleanly goal-aligned).
- **⚠️ The ~v221 audit is now 36 ships overdue** (last v212). This ship hands it: the §C-row-92 promotion-eligibility (still N=2, still no independent 3rd), the two new watch axes (Shape A / Shape B), and the corrected v190 telemetry row.

## Bottom line (blunt)

A pentester the vault already knew, seen 47 days and 59,000 lines later, has quietly changed what it *is*: from a CLI you run into a capability your coding agent installs, with a consumer skill whose ambiguity default routes to the paid cloud and a sign-in flow that spends your ChatGPT subscription. The most instructive things in it are two opposite design choices sitting in the same repository. One is exemplary: a report cannot be written without a working proof-of-concept, enforced in code, not asked for in prose — the exact discipline your candidate-LLM policy demands, and the exact inverse of last ship's browser-seizing action guarded by a paragraph. The other is the quiet one: the free local tool hardcodes a string that tells the model a platform verified the target, then tells it never to question its authority — a real and probably necessary way to stop a safety-tuned model refusing your own authorized pentest, and worth naming out loud before you install it. And the finding that should sting a little: this is the tool that fits hireui's single worst risk — no object-level authorization, in a multi-tenant app full of candidate PII — its own skills spell out how to attack exactly that, a thorough pilot menu was written for it seven weeks ago, and not one command was ever run, because running it means letting an LLM drive exploits against your product on an honor-system authorization and default-on telemetry, which your own ratified policy forbids. The revisit's real payoff is not a scan. It is the two-to-four-hour zero-install act of reading `idor.md` and turning it into a BOLA checklist you apply to hireui by hand.
