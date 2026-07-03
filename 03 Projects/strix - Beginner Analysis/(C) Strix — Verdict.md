# (C) Strix — Verdict (v190, routine v2.6)

> **Produced INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. A 12-agent read-only workflow (`wf_162247b2-a80`, ~1.79M subagent-tokens) did **source-reading + upstream research ONLY**. **All corpus / collision / identity / positioning claims were verified BY HAND** (grep over `_state/` + `_patterns/` + `03 Projects/`; read of shannon v45's entry + the SkillSpector v169 §C row + the full §C standalone list + the T5 sub-archetype registration in `02b`).
> **AI-generated (Claude) — prefixed `(C)`.**

---

## Verdict: GOAL-ALIGNED INCLUDE 3/4 — [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]

### (a) FAILS cleanly
`usestrix` is a commercial security startup (`Strix <hi@usestrix.com>`; agent's in-prompt self-identity "OmniSecure Labs"), **not Anthropic**. Claude is one of **8** LLM backends (GPT-5.4 is the docs' example default; Claude Sonnet 4.6 + Gemini 3 Pro also recommended). **First `usestrix` author → #19 19a** institutional data-point. This is the declared-non-Anthropic-institution situation (the Keygraph-v45 / NVIDIA-v169 / Kilo-AI-v177 class); no heritage/locale rescue. The "$117M funding / Matt-Shannahan-Mahesh-Ramichetty founders / YC" claims are **unverified** (web-only) and are **not** relied upon for any axis.

### (b) STRONG — keys the tier (⚠️ MODERATE-on-the-security-domain reading recorded operator-reviewable)
Strix **IS an autonomous multi-agent system** (a genuine parent/child agent graph on the OpenAI Agents SDK + LiteLLM) — dead-center on Goal #1's *"autonomous agents"* half — applied to **application security testing, a real part of the SDLC**, and it lands on the operator's live **multi-agent-orchestration** pilot thread + the **claude-api-cost-optimization** thread. **The load-bearing delta from shannon v45:** shannon was rated LOW-direct-pilot *only* because the vault was markdown-only ("markdown-vault vs web-app fundamental mismatch"). That constraint is **gone** — the operator now owns **hireui** (a real, testable, TalentAxis recruitment web app), so Strix is the **first corpus subject that is directly, natively, *authorizedly* pilotable as a security tool against the Goal-#2 target.**

**STRONG-not-STRONGEST** because: third-party (not Anthropic substrate); Claude is one of 8 backends and *not* the docs' default; and the domain is a security *vertical*, not general software development. ⚠️ The domain-weighted **(b) MODERATE** reading is recorded operator-reviewable (the ai-berkshire v187 / OpenMontage v188 handling) — but GOAL-ALIGNED holds either way under §31, exactly as the prior Domain-Vertical instances (SEO v64 / academic v90 / cybersecurity v98) were goal-aligned *regardless of vertical*.

### (c) STRONG
Mature, substantial engineering: 87 Python files; a real async multi-agent coordinator (`create_agent`/`send_message_to_agent`/`wait_for_message`/`agent_finish`/`stop_agent`-cascade; parent/child tree; budget-stop; `max_turns=500`); a per-scan Kali Docker sandbox + in-container Caido MITM proxy sidecar + ~60 tools; **45 progressive-disclosure skill files**; ~20 host tools incl. a full Caido proxy suite + a `create_vulnerability_report` writer (CVSS 3.1 + CVE/CWE + **PoC-required** + `fix_before`/`fix_after` diffs + LLM dedup); black/white/combined + auto-fix modes; a CI diff-scope gate (exit 2); resume; TUI with a live agent-graph; 8 providers via LiteLLM. 32.3k★, v1.0.4, 16 releases. Independent XBEN 96%. **Caveats:** the hard exploit primitives are bundled third-party tools (Strix = the orchestration layer); PyPI classifier still says **Alpha**; benchmark is vendor-run; **no programmatic authorization enforcement**; telemetry opt-out default-on with a README-vs-code discrepancy.

### (d) STRONG
Dense cross-references: **shannon v45** (the direct AI-pentester predecessor — N=2), **SkillSpector v169** (defensive counterpart — offensive/defensive book-ends), **magika v44** (Google security-adjacent), **Anthropic-Cybersecurity-Skills v98** (cybersecurity skill-collection — Strix's `skills/` is the executable analogue), **OpenHands v30 / AutoGPT** (T5 agent-as-application + Docker sandbox family), **browser-use v41 / Skyvern v24 / crawl4ai v29** (browser-automation neighbors), and live threads **multi-agent-orchestration**, **claude-api-cost-optimization**, **loop-engineering v189** (tool-call/lifecycle termination + maker/checker + CI-gate-as-loop), plus **#66 supply-chain/dual-use**.

---

## Pattern outcome: 1 NEW §C standalone at N=2 (NOT corpus-first)

**"Autonomous Multi-Agent Offensive AI Penetration-Testing System"** — an autonomous system that orchestrates a *tree of specialized AI agents* through **recon → discovery → validation-with-a-real-PoC → reporting (→ fixing)** across a **sandboxed full pentest toolkit**, where a finding is only reported once independently reproduced by a validation agent ("no exploit, no report").

- **Anchors:** **shannon v45** (`KeygraphHQ/shannon`) = **N=1, the un-registered corpus-first** — minted at v45 as the T5 "AI-pentester" *tier* sub-archetype, **before the v2.4-era §C registry existed**, so it never got a §C standalone. Credited here. + **Strix v190** = **N=2**.
- **Why mint at N=2 (not corpus-first, not re-register):** exact **camofox v179 / codebase-memory-mcp v172 precedent** — a capability species whose first instance predates the §C registry, and a genuine cross-author 2nd instance appears → mint a §C standalone at N=2 to credit the prior instance's priority. (camofox credited CloakBrowser v69's un-registered stealth-browser priority; codebase-memory-mcp credited codegraph v70's code-graph priority. Same move here for shannon v45.)
- **Strix's distinguishing facets recorded as within-class variation, NOT separately minted** (anti-"draw-the-circle", camofox v179 discipline): Python + OpenAI Agents SDK (vs shannon's TS + Claude Agent SDK); black-box + white-box + combined + **auto-fix** (vs white-box focus); Caido MITM sidecar + Kali sandbox + 45-skill progressive disclosure; CI diff-scope gate; hosted app.strix.ai twin.

### ⚠️ NO-MINT alternative — recorded operator/audit-reviewable
"Strix = a **clean N=2 instance of the already-registered T5 AI-pentester sub-archetype** (shannon v45 + Strix v190) → **no §C mint**, just tier N-tally bookkeeping" — the **ai-berkshire v187 precedent** (a clean instance of a CONFIRMED sub-archetype gets no new mint). The mint stands on the reading that the §C registry (the current home for capability-class vocabulary) has **no** offensive-pentester standalone, so registering one at N=2 fills a real gap the way camofox/codebase-memory-mcp did. **This is the single reviewable judgment of the ship. Either way, confirmed counts are UNCHANGED 46/11.** The **T5 AI-pentester tier sub-archetype strengthens to N=2** regardless (recorded, not self-incremented into any confirmed count).

---

## SECONDARY (observations, NOT minted)
- **#19 19a** — first `usestrix` author; declared-non-Anthropic-institution data-point.
- **#28 Multi-Provider AI Support** — 8 providers via LiteLLM (shannon v45 had 5); strengthening data-point.
- **Agent-skills progressive-disclosure cross-ref** — Strix internally uses the Anthropic-style SKILL.md pattern (`create_agent(skills=[...])` + `load_skill`) applied to a security vertical; cross-ref to agent-skills-standard v76 / Anthropic-Cybersecurity-Skills v98. NOT a mint (internal design choice; skill-collections are well-covered).
- **loop-engineering v189 cross-ref** — the tool-call/lifecycle termination contract + the mandatory maker/checker validation agent + the CI diff-scope gate (a "security-sweeper" loop). Data-point on the loop thread.
- **#66 supply-chain / DUAL-USE (the load-bearing secondary)** — offensive tool with **no programmatic authorization** (honor-system warning only); `curl|bash` install (benign, but no digest-pin / no signature — contrast codebase-memory-mcp v172's SLSA-L3); sandbox image by tag not digest; opt-out-default-on telemetry to PostHog + Scarf with a README-says-"never-collect-vuln-details"-vs-code-sends-severity-counts discrepancy; cost-runaway risk (`--max-budget-usd` off by default); aggressive-testing collateral (independent report of target DB-pool exhaustion). This is the CloakBrowser v69 / camofox v179 dual-use class **plus active exploitation** — the pilot fence foregrounds it.

## NON-claims
- **NOT corpus-first** autonomous AI pentester — shannon v45 precedes (N=2 scoped honestly).
- **NOT a new top-level pattern** (max #85).
- **NOT #52** — 32.3k★ / 3.4k forks / v1.0.4 / 16 releases page-stated, NOT API-verified (§37.4) → velocity unestablishable. The XBEN 96% is a *capability* benchmark, not a viral-velocity claim.
- **NOT #57** — uses Claude/OpenAI/Gemini as backends + integrates nmap/nuclei/sqlmap/Caido/LiteLLM/Playwright/Textual as tools; acknowledgements name only non-corpus projects; mentions/deps ≠ influence-citation recursion.
- **NOT #18 B1-MCP** — consumes tools; the Caido sidecar is not an MCP-server-to-many-clients shape.
- The company facts ($117M / founders / YC) = **UNVERIFIED**, reported with hedging, load-bearing on nothing.

---

## Tier & counts
- **Tier: T5 Agent-as-application (AI-pentester flavor, N=2 with shannon v45).** The OSS repo *is* the autonomous agent; app.strix.ai is the hosted commercial twin. NOT T2 service.
- Confirmed top-level patterns **46** (unchanged). CONFIRMED Library-vocab **11** (unchanged).
- **§C live standalones 33 → 34** (+1, the new N=2 pentester standalone). Tracked PROVISIONAL surface ≈40 → **≈41**.
- **Streak: `GA:51 · OG:11 [7 ov]`** (forward-only from v126; ⚠️ v176/v186 OFF-GOAL reading → GA:49·OG:13). **§35 CLEAR** — window {v188 GA, v189 GA, **v190 GA**} = 0 OG. **36 consecutive goal-aligned ships v153→v190.**

## Verification trail (hand-done)
- **Collision grep** (`strix`/`usestrix`) over `_state/` + `_patterns/` + `03 Projects/` → **clean** (no prior Strix subject).
- **shannon v45 read** (`_state/03b` + `_state/02` + `_patterns/02b`) → confirmed the corpus-first autonomous AI pentester, minted as a **T5 sub-archetype, NOT a §C standalone** → Strix = N=2, mint-at-N=2-crediting-priority per camofox/codebase-memory-mcp.
- **§C list read** (`_patterns/06`, §C) → the only security §C standalone is **SkillSpector v169 (defensive)**, whose own row explicitly frames shannon as "the offensive pentester" and distinct → confirms **no offensive-pentester §C standalone exists** → the N=2 mint fills a real gap.
- **Workflow confabulation watch:** the workflow did source + upstream only; no corpus facts were taken from it. (The "$117M funding" and founder names surfaced by the web agent are flagged UNVERIFIED and not used.)
- `inflation_check` = discipline **HELD** — 1 mint ≤2 cap; filed at honest N=2 (not an N=1 corpus-first over-claim); max #85; counts 46/11 unchanged; NO-MINT alternative recorded reviewable; no N-bumps on #28/#66; no double-count (T5 tier N-tally vs §C capability = different axes).
