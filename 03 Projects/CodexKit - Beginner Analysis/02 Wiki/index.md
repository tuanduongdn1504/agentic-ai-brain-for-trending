# CodexKit — Wiki (v121)

> `hoavdc/CodexKit` · **"A Codex-first starter repo with installable skills, templates, and workspace kits for engineering, project management, finance, legal, HR, operations, strategy, analytics, marketing, sales, support, founders, and CX."** · An open-source **OpenAI Codex / ChatGPT "operating kit"** — 90 installable skills across 15 work domains, in Codex's own `SKILL.md` + `agents/openai.yaml` skill format, installable to `~/.agents/skills`. **No Claude support.**

**(C) Claude-generated wiki page.** Fetched 2026-05-30 (GitHub API + README + author profile). Routine v2.4, wiki #121 — first build of the post-v120-audit window (v120 audit cleared the cadence). Phase 0.9 **STRONG INCLUDE 3/4** — (a) PASS (inferred-Vietnamese), (b) **WEAK** (Codex-not-Claude + business-ops-not-software-dev), (c)(d) STRONG. 4th consecutive clean PASS after the v116 Sana OVERRIDE.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`hoavdc/CodexKit`](https://github.com/hoavdc/CodexKit) |
| What | **OpenAI Codex / ChatGPT operating kit** — 90 installable skills × 15 work domains + playbooks + 14 automation recipes + 18 templates + 9 workspace kits + MCP guidance + Next.js docs site |
| Tier / archetype | **T1 Assistant Skill / Multi-Domain (Cross-Functional) Skill Collection** — contrasts the single-vertical **T1 Domain-Vertical-Skill-Collection** (CONFIRMED N=4: v64 SEO / v90 academic / v98 cybersecurity / v119 nature); CodexKit spans 15 domains in one bundle |
| Stars / forks | **19★ / 10 forks** (fork_ratio **0.526** — very high active-deployment intent at micro-scale; cf. v76 0.296 / v79 0.484 / v80 0.765 VN cluster) |
| Subscribers / open issues | 0 / 7 |
| Created / pushed | 2026-03-20 / 2026-05-15 (**~71 days** old at fetch) |
| Velocity | **~0.27 stars/day → NOT a Pattern #52 instance** (well below every velocity sub-class floor; micro-scale, like v76 4.0/d / v80 17★) |
| License | **MIT** (GitHub API `mit`) |
| Language | TypeScript 69.1% + JS 21.2% + Shell/PowerShell/Batchfile — but these are the **docs site (Next.js) + install scripts**; the 90 skills themselves are Markdown content |
| Releases | **v0.10.0** (2026-05-15) / **8 releases** — sustained dev cadence despite micro-scale stars |
| Distribution | Download release + platform starter scripts (Win/macOS/Linux), or `install-skills.ps1` / `install-skills.sh`; installs to `$HOME/.agents/skills` (user-scope) or repo-local `.agents/skills` |
| Default branch / homepage | `main` / [codexkit.pages.dev](https://codexkit.pages.dev/) |
| Topics | ai, codex, ai-agents, ai-assistant, codex-cli, codex-external, codex-github, codex-skill, codex-skills |
| Author | **Hoa Dang** (`hoavdc`, `owner.type: User`) — **inferred Vietnamese** (Vietnamese name + a shipped `HUONG-DAN-NHANH.md` "Hướng dẫn nhanh" / Quick-Guide). Profile location/bio **undeclared**; account 2020-08, **236 public repos** (prolific), 7 followers. |
| Affiliation | Third-party / independent — implements OpenAI's Codex skill format; not affiliated with OpenAI. |

## What it is

A library of **90 installable skills** authored in **OpenAI Codex's own skill spec** (`SKILL.md` body + `agents/openai.yaml` metadata, discoverable via the `.agents/skills` convention), wrapped with playbooks, automation recipes, templates, workspace kits, and a docs site. It is, structurally, *what agentskills.io is for Claude/multi-harness, but for Codex/ChatGPT* — and it covers business operations, not just engineering.

**5-Layer Skill Framework** (every skill): **Intent → Knowledge → Execution → Verification (4C gates: Correctness / Completeness / Context-fit / Consequence) → Evolution.**

**3-tier progressive structure:**
- **Tier 1** — `SKILL.md` + `agents/openai.yaml` (all **90** skills)
- **Tier 2** — + `verification/` + `examples/` (**26** skills)
- **Tier 3** — + `templates/` + `scripts/` (**5** technical skills)

**8 categories:** knowledge 17 · data 16 · scaffolding 16 · runbook 10 · verification 9 · automation 9 · review 9 · infra 4.

**15 work domains:** project management, finance, legal, HR, operations, supply chain, strategy, analytics, marketing, data, customer success, sales, IT & admin, training & development, founder workflows + cross-functional — i.e. an *office/operations* skill OS, not a software-dev one.

Also bundled: 14 automation recipes, 18 templates, 9 workspace starter kits, `mcp/` guidance for choosing/rolling out MCP servers, a Next.js documentation site (`web/`), and a Vietnamese quick-start (`HUONG-DAN-NHANH.md`).

**References:** OpenAI Codex, ChatGPT, ChatGPT Deep Research, Gemini, Perplexity Pro. **No Claude anywhere.**

## Why it's in the corpus

**STRONG INCLUDE 3/4** (one criterion WEAK; INCLUDE rests on (a)(c)(d)):
- **(a) PASS (inferred)** — author **Hoa Dang** is inferred-Vietnamese (Vietnamese name + a shipped Vietnamese-language quick-guide `HUONG-DAN-NHANH.md`) = a direct Storm Bear cultural-peer. Stronger evidence than v117's inferred-China (an actual VN-language doc is shipped), but **location is undeclared on the profile**, so this is an *inferred* PASS, not a declared one. Extends the VN sub-cluster (v76 Hanoi + v80 + v85 org + v91 + **v121**) and Pattern #19's CONFIRMED VN-Community Multi-Profile-Type (N=5).
- **(b) WEAK** — **Codex/ChatGPT-first with zero Claude support**, routing entirely away from the vault's substrate (more Codex-pure than v117, which at least managed a coding agent). And the 90 skills are **business-operations** (finance/legal/HR/marketing/sales/ops), not software development or agent-mastery. Goal #1 is "master Claude and autonomous agents for software development" — CodexKit serves neither Claude nor software-dev as its primary use. Value is **study/reference only**, not operational. Honestly WEAK — not laundered to MODERATE.
- **(c) STRONG** — the **5-Layer Skill Framework** (with explicit 4C verification gates + an Evolution layer) + **3-tier progressive structure** + 8-category taxonomy + 90-skill breadth is a genuinely instructive, well-architected **skill-authoring reference**, and the methodology is cross-applicable to agentskills.io / Claude skill authoring even though the runtime is Codex.
- **(d) STRONG** — high corpus connectivity: the **Codex-tool cluster** (v62 codex-plugin-cc + v117 CodexPlusPlus); the **VN cultural-peer cluster** (v76/v80/v85/v91); a **multi-domain variant** of the T1 Domain-Vertical-Skill-Collection (N=4); the **Codex-native skill standard as a parallel to agentskills.io** (corpus-novel — *not* the Pattern #57 57k chain, the competing standard); MCP guidance; high-fork-ratio micro-scale signal.

## Pattern Library contribution (summary)

- **PRIMARY (NEW Library-vocab standalone, PROVISIONAL N=1, CORPUS-FIRST):** **"Codex-Native Skill Collection implementing OpenAI's Codex skill spec (`SKILL.md` + `agents/openai.yaml` + `.agents/skills`) — a *parallel* skill-authoring standard to agentskills.io."** Distinct from the prior Codex subjects, which are *tools around* Codex, not skill collections *in* its skill format: v62 codex-plugin-cc (bridge) / v117 CodexPlusPlus (management harness) / v112 freellmapi (proxy). First observed corpus instance of the Codex skill-authoring standard being implemented as a third-party skill library — evidence the agent-skill ecosystem is **bifurcating** (agentskills.io for Claude/multi-harness vs Codex-native for Codex/ChatGPT). Filed to the registry (section C). Promotion-eligible at N=2.
- **SECONDARY (NEW Library-vocab standalone, PROVISIONAL N=1):** **"Multi-Domain (Cross-Functional) Skill Collection"** — a single bundle spanning **15 work domains × 90 skills** (engineering + business ops), structurally contrasting the single-vertical T1 Domain-Vertical-Skill-Collection (N=4, each one vertical). Tier-sub-archetype-layer; filed to the registry (section C). *(These two are exactly the §28 ≤2-new-standalones-per-wiki cap; everything else below is cluster-filed or administrative — no further minting.)*
- **Cluster filings (no new mint, §28 clustering-first):** **LV-C4** (cadence/velocity micro-signals) ← high fork_ratio 0.526 at 19★ with *sustained* dev (8 releases / v0.10.0) = high-deployment-intent micro-signal — note: NOT clean #17 Try-Once (there IS sustained development). **LV-C1** (Vendor-Direct Skill-Authoring & Distribution) ← the 5-Layer + 4C-verification-gate + 3-tier authoring methodology, noted as an adjacent member (third-party, not vendor-direct).
- **Administrative strengthening (no mint):** Pattern #19 VN-Community Multi-Profile-Type (CONFIRMED N=5) — CodexKit = a VN-solo prolific-builder data point; Codex-tool cluster (v62/v117); MIT clean. **NOT a Pattern #52 instance** (~0.27/d — negative evidence).
- **Honest non-claims:** **NOT in the agentskills.io 57k chain** (this is Codex's *competing* standard, deliberately not counted as a 57k implementer); **(b) is WEAK, not inflated** (Codex-not-Claude, business-ops-not-dev); **(a) is inferred, not declared**; **NO new top-level Pattern** (PRIMARY is a Library-vocab N=1); exactly **2 new standalones registered** (the §28 cap), the rest cluster-filed; **NO Pattern Library state change at ship** (46 confirmed / ~25 active / 8 Library-vocab CONFIRMED unchanged).

---

*See `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md` and `01 Analysis/(C) Pattern-Library-Phase-4b-Codex-Native-Skill-Standard-N1.md`.*
