# (C) reverse-skill — Verdict (v279)

## Classification: GOAL-ALIGNED INCLUDE — 3/4

| Criterion | Call | Basis |
|---|---|---|
| **(a) Source authority** | **FAIL** | Owner `zhaoxuya520` pseudonymous (`ww7517437@gmail.com`, `linux.do`); top committer `jhuang-tw` also pseudonymous; **zero Anthropic commits**; no registered (a)-7 vendor-direct source. §41: no name/heritage/notability inference. |
| **(b) Goal-relevance** | **STRONG** ⚠️MODERATE-reviewable | The *capability* — a cross-harness agent skill **router**, an **obedience-engineering** layer, an **authorization/scope hard-gate**, a **skill-supply-chain vetting gate** — is squarely on Goal #1 (mastering Claude/agents) and directly transferable to the vault's own architecture and to the hireui candidate-LLM legibility ADR. The *domain* (offensive security) is off both the operator's day-job and the vault's substrate core → the OFF-GOAL reading is defensible; recorded as the reviewable alternative. |
| **(c) Rigor** | **STRONG** | 122 commits, 17 authors, 22 merges, issue-driven; the corpus's most extensive skill-collection CI (routing regression + coherence + supply-chain pin gate + doc-facts + leak-scan + version + BOM/parser gates, SHA-pinned actions); an un-bypassable, CI-proven auth gate; version-pinned + SHA256-checksummed bootstrap with no `curl\|bash`. |
| **(d) Wiki value** | **STRONG** | Corpus-first at full extent (0 across 23,292 md, controls firing); the near-perfect inverse of v278; a live validation of v278's clause (g); rich pattern surface (router / auth-gate / obedience-tension / skill-supply-chain / gate-scope). |

**No §40 override needed** (operator-requested subject, (b) MODERATE+). **Streak: GA continues.**

Notation reconciliation with the CURRENT HEAD: v278 closed at `GA:135 · OG:13 [7 ov]`; v279 → **`GA:136 · OG:13 [7 ov]`** — **59 consecutive goal-aligned ships v220→v279**. §35 CLEAR (window {v277, v278, v279} = 0 OG). Override review: **19th consecutive discharge**.

## Mint decision: **NO MINT**

Counts **46 / 12 UNCHANGED**; §C-1 **13** UNCHANGED; §C-2 **39** UNCHANGED.

I concur with the adversarial mint-refuter after my own analysis. Two candidate surfaces were tested and both declined:

**Candidate 1 — the router (declined: form-factor-within-a-genre + not-world-first).**
The subject leads with "Cybersecurity Skills Router" and its own `IDENTITY.md` names "three-axis routing + PRIMARY fast-path" as feature #1. But "route a task to the right skill" is the **universal convention** of every agent skill system (Claude Code / Cursor / Windsurf description-matching; Anthropic ships routing/lazy-loading first-party as `defer_loading`). A **config-SoT + benchmark-regression** implementation is more *engineered*, not a novel *capability*. This is decisively a **cybersecurity Domain-Vertical-Skill-Collection** (CONFIRMED; cybersecurity already an established vertical via **v98**), with a router form-factor. **v238** declined a routing-adjacent preset on exactly this ground (form-factor-within-genre, `defer_loading` precedent). §44.5: §28 alone cannot decline, but **form-factor-within-a-genre** and **not-world-first** are load-bearing and both apply.

**Candidate 2 — the hard authorization/scope state machine (declined *here*, RECORDED as the audit-reviewable alternative).**
The genuinely corpus-first thing in this repo is **not** the router — it is the **hard, un-bypassable, section-scoped pre-target-action authorization/scope state machine** (`auth.status=granted` + valid `network_profile` before ACT; `--force` cannot bypass; forged out-of-section fields ignored; CI-proven; shell and PowerShell parity). No corpus subject implements a pre-action authorization gate of this shape (shannon v45 / Strix v190 = §C **C39**, the *autonomous offensive-pentester system* class, is a different object; OpenSandbox v244 minted a *sandbox runtime*, not a *consent gate*). It **ships**, it is **CI-tested**, and it is a **capability**, not a technique or a domain — so on the §C-2 "corpus-first for the surface, NOT world-first" standard it is genuinely mintable.

It is **not** minted at this ship because (i) it is **bundled** inside a package whose headline capability is the form-factor router, and the adversarial refuter's bundling-dilution point is fair — a genuinely-novel-but-bundled capability is better adjudicated by the audit than asserted by a ship; and (ii) the corpus mints **conservatively** on skill-collection subjects (geti v213, ui-skills v218, hallmark v204, marketingskills v202, ai-berkshire v187 all NO MINT). **RECORDED for the ~v268 audit** (now 19 ships overdue): a candidate §C-2 N=1 — *"Hard, Un-bypassable, Section-Scoped Pre-Action Authorization/Scope State-Machine gating an AI agent's target actions (auth-granted + legal network-profile before ACT; `--force` cannot bypass; out-of-section fields ignored)."* Not self-executed — a mint is an audit act.

**Not a §C C39 instance.** reverse-skill's `IDENTITY.md` **explicitly refuses** to be an autonomous multi-agent system (the "Z3r0" it defines itself against). Its CTF-Sandbox-Orchestrator is itself a *router* ("control context bloat … route by problem type to sub-skills"; the 41 competitions carry `allow_implicit_invocation: false`, only the orchestrator `true`), not an autonomous agent-tree. Distinct from C39.

## Recorded for the audit (not self-executed)

- **#18 B1-MCP ≈N=16 → ≈N=17** — `burp-mcp-full` is a first-party 78-tool Burp Suite MCP server (a capability delivered via MCP). Audit bookkeeping.
- **Cybersecurity Domain-Vertical-Skill-Collection** instance-strengthening (v98 precedent) — the top-level pattern is CONFIRMED; no count change.
- **The candidate auth-gate §C-2 mint** (above) — deferred to the audit.
- **Clause (g) field-evidence** — this ship is the cleanest real-world validation of v278's clause (g): the one number under an anchored gate (Burp 78) is bulletproof and my own fleet still produced 74/83/96 against it; the ungated 43/173/44 are correct-by-maintenance. Feeds the vault's own `(C) proposed-verify-vault-inventory.sh` clause-(g) proposal.

## The blunt line

reverse-skill is the near-perfect inverse of the ship before it. v278 gated nothing and put a debugger's memory-write on the open internet with no password; v279 gates almost everything a machine can check — 173 routing cases, a coherence gate, a supply-chain pin gate that fails on one unpinned dependency, a doc-count derived from source, and a consent gate whose `--force` flag prints a refusal and exits nonzero anyway — and gates nothing a machine cannot: forty-four skill modules, forty-one CTF competitions, a Burp extension that hands a caller seventy-eight offensive tools, all verified by nothing but code review. The discipline stops exactly where the artifact stops being machine-checkable, which is the seam between the router and the skills. And the same repository that builds the most careful pre-action authorization gate this corpus has reviewed also builds its most explicit manual for defeating an agent's hesitation — the one folder engineered to make the agent stop until it is authorized, the next folder engineered to make it never stop once it is. They are coherent only if a single authorization check at the front door is enough to trust everything the agent does after it, on an offensive-security toolchain, forever. That is the assumption the whole design rests on, and it is the one thing in the repo that no test can check.
