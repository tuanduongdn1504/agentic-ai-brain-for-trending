# (C) reverse-skill — Pilot Methods Menu (v279)

**Overall verdict: ⚠️ READ-AND-BORROW. A fenced clone-and-read is genuinely safe here** (unlike v278, which couldn't even build on darwin): the router / case / skill layer is pure markdown + shell/pwsh, macOS-supported, and the bootstrap is version-pinned + SHA256-checksummed with no `curl | bash`. **Do NOT run the offensive-toolchain installs, and do NOT wire the Burp/IDA MCP servers at candidate or production data.**

Ladder from lowest to highest footprint. Times are rough.

---

### Rung 0 — read the auth gate + the skill-supply-chain gate as forms (20 min, zero install)
Clone read-only and open four files:
- `skills/scripts/case-guard.sh` — the four-condition, section-scoped, `--force`-proof consent gate.
- `.github/workflows/ci.yml` — the offline-sample case-contract step that *proves the gate in CI* (a missing sample is rejected; `--force` still exits nonzero).
- `skills/ops/skill-supply-chain.md` — the AST10 checklist for vetting external skills/MCP.
- `skills/llm-security/references/agent-obedience-engineering.md` — read it as a **hazard specimen**, not a template: see how ~73% of its excuse-rebuttals suppress agent hesitation with no user re-involvement, and note it carries no "do NOT use for" disclaimer.

### Rung 1 — ⭐ THE VAULT ITEM: extend clause (g), and borrow the auth-gate shape (30 min)
Two moves, both feeding live vault threads:

1. **Clause (g), field-validated.** This ship is the cleanest real-world proof of v278's clause (g): the one number `reverse-skill` derives from source with an anchored command (`verify-doc-facts.ps1` → Burp **78**) is bulletproof, and my own fleet still produced **74 / 83 / 96** against it with naive re-counts; the ungated 43 / 173 / 44 are correct only by maintenance. Add to `(C) proposed-verify-vault-inventory.sh` clause (g) — *every stated count must be emitted by the anchored command that derives it, with the command shown; FAIL when a stated count and its derived count disagree* — and cite reverse-skill's `verify-doc-facts.ps1` as the exemplar and its ungated 43/173 as the counter-example. **And run the script: it is now 24 ships old and has never been run.**

2. **The auth-gate shape → the hireui candidate-LLM legibility ADR.** `case-guard.sh` is the strongest pre-action consent-gate code in the corpus since v244: a gate that reads a required-fields contract, **rejects fields forged outside their section**, and whose bypass flag prints a refusal and fails closed anyway. Write its shape into the RATIFIED candidate-LLM legibility ADR: *any hireui LLM path touching a candidate must pass an explicit, section-scoped authorization state whose "force" path cannot bypass it* — composing with v244's fail-closed consent gate and v278's hostile-artifact rule.

### Rung 2 — vet `05 Skills/` with the skill-supply-chain gate (30 min, zero egress)
`ops/skill-supply-chain.md` is an AST10-based checklist (read all `SKILL.md` + scripts, no mystery outbound, no `~/.ssh`/browser-store reads, no `curl|bash`, only trust curated sources). It is the same role `edgeone-skill-scanner` (v276) plays. Walk the vault's own `05 Skills/` through it by hand — it is pure documentation, no code to run — and record the result. Pairs with the v276 scanner as a two-tool skill-vetting bench.

### Rung 3 — the router-as-answer-to-tool-catalog-overload (45 min, design only)
The repo's whole thesis — *deep skills + a router that loads only the PRIMARY > a flat stack of skills* — is the independent, security-domain confirmation of the vault's own v238 finding (tool-catalog size changes how the model reasons) and its live ~54K tool-catalog problem. Read `routing.json` + `verify-routing-coherence.ps1` as a concrete pattern: a single-source-of-truth route table, validated by a benchmark, that dispatches to exactly one methodology. Consider whether the vault's own skill/tool exposure wants a `routing.json`-style SoT + a coherence gate rather than an ever-growing catalog. **Design only — do not port the offensive content.**

---

## 🔴 NEVERs

- **Never run the bootstrap offensive-toolchain installs** on a machine you care about (Frida / Nmap / SQLMap / Hashcat / Metasploit / etc.). They are pinned + SHA256-checksummed — but it is still a full offensive toolchain.
- **Never wire `burp-mcp-full` or the IDA/Ghidra MCP servers against candidate or production systems.** `burp-mcp` is localhost+bearer-auth (careful), but it exposes 78 offensive tools; the auth gate governs the CLI/case flow, not necessarily a raw MCP server you start yourself.
- **Never treat `agent-obedience-engineering.md` as a template for the vault's own skills.** It is a manual for suppressing agent hesitation. Borrow the *structure* of the "surface options to the user" rebuttals (rows 1/3/11/12); never the "your judgment does not apply" ones.
- **Never cite the Burp count from a naive grep** — it is **78** (getToolList body, the CI method); naive commands give 74 / 83 / 96.
- **Never cite `CTF-Sandbox-Orchestrator/` as a git submodule** (the README mislabels it; `git ls-tree` shows a checked-in directory); **never assume the AGPL Pentest Swarm AI is present** (referenced, zero code hits); **never reuse `burp-mcp-full` as licensed** (it carries none, and no NOTICE covers the GPLv3/AGPL parts).
- **Never use it against systems you do not own or are not authorized to assess.** The disclaimer + the auth gate are real mitigations — but the router dispatches to genuinely offensive methodologies.
