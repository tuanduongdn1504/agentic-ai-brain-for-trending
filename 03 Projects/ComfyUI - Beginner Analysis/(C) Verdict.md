# (C) ComfyUI — Verdict (v281)

**`Comfy-Org/ComfyUI`** · v0.33.0 · GPL-3.0 · HEAD `7a054eb4` · 2026-08-26

## Phase 0.9

| Axis | Call | Basis |
|---|---|---|
| **(a) Anthropic / registered vendor-direct** | **FAIL** | Comfy Org is a funded independent company, not Anthropic, not a registered (a)-7 source. §41 — no inference from notability or funding. |
| **(b) Goal relevance** | **MODERATE** | The product (a diffusion node-graph engine) is off-goal. The **agent-governance layer** is on-goal and substantial: a 361-line `AGENTS.md` bound into an enforcing LLM reviewer, a CI gate on AI authorship, and a first-party `ClaudeNode` exposing nine current Claude models. ⚠️ The OFF-GOAL reading is defensible and recorded. |
| **(c) Quality / rigour** | **STRONG** | 5,819 commits, 358 authors, 1,301 tests with 98.4% running in ordinary CI, the best-reasoned `SECURITY.md` in the corpus, `weights_only=True` at 3/3 `torch.load` sites. |
| **(d) Transferable idea** | **STRONG** | The prose-policy→LLM-reviewer binding, the AI-provenance decision, and the "these labels do not make internet access acceptable" privacy rule. |

⇒ **GOAL-ALIGNED INCLUDE 3/4** under routine **§40** (operator-requested, goal-adjacent, (b) MODERATE+). **No override invoked.**

## Mint

**NO MINT.** Counts **46/12 UNCHANGED**; **§C-1 13**, **§C-2 39** UNCHANGED.

1. **Node-based generative-media engine** — the corpus's first subject in this domain (58 §C rows checked by hand; C37 is *agent-first* video production, which this is not). **Domain-not-capability**, on the settled **v212 tabularis** precedent, reinforced by v196 meetily and v210 AIRI. Also **not world-first** (node-graph media tools long predate it; AUTOMATIC1111 preceded it in diffusion GUIs).
2. **`AGENTS.md`** — a clean instance of **CONFIRMED Library-vocab #12** (*LLM-routing artifacts*), whose written definition names the artifact type. Instance-strengthening only; N-tally is audit bookkeeping.
3. **CI-enforced erasure of AI-authorship trailers** — a **practice**, not a capability layer ⇒ **RECORDED as the audit-reviewable §C-2 candidate, NOT minted** (the v211 technique discipline; the v279/v280 handling).

## Streak

**`GA:137` → `GA:138 · OG:13 [7 ov]`** — **61 consecutive goal-aligned ships v220→v281.**
**§35 CLEAR** — window {v279 GA, v280 GA, v281 GA} = 0 OG. **Override review: 21st consecutive discharge.**

## The sentence

**ComfyUI runs AI coding agents through every stage of its pipeline except the one that would leave a permanent record.** It instructs them in a 361-line `AGENTS.md` that only the founder may edit. It has CodeRabbit enforce that file as *"mandatory repository policy"* and emit fix-prompts addressed to agents. It runs a Cursor review panel. And then a CI job fails any pull request whose commits still carry an agent's name, and tells the contributor to rebase and force-push until they don't.

That gate was written **nineteen minutes** after the commit that provoked it, and in the **899 commits since, not one AI trailer has landed** — 62 of them across 5 commits, all before. It is one of the few gates this corpus has read that demonstrably works.

**And what it covers is exactly what it can see.** It fires on `pull_request`, so the **24 post-gate commits that bypass PRs — every one of them the founder's, who holds 56.8% of the history — are structurally invisible to it.** It matches trailers, not code, so a commit written wholly by an agent passes clean once the line is gone; the error message *instructs* that removal. And *"code must look hand-written"* is adjudicated not by a test but by a paid LLM whose verdicts cannot be reproduced from the tree.

v279 asked what a repository gates and what that reveals about what it fears. v280 answered that it gates what it can compare to another copy of itself. **v281 answers a third way: it gates what it can see — and a project can be scrupulous about the record while being entirely relaxed about the practice.** ComfyUI is not hiding that agents write its code; `AGENTS.md` is a public instruction manual for them. It has decided that agent involvement is a fact about the process and not a fact about the commit — and it built the only machinery that could enforce that distinction: another AI to judge whether the output reads as human.

The rest is unusually good and deserves saying plainly. Its `SECURITY.md` states a threat model, declares six categories of non-vulnerability with reasons, and admits there is no authentication at all — then its code matches the claim (`cli_args.py:63` binds `127.0.0.1`). Its privacy rule refuses telemetry categorically and pre-empts every euphemism — *"These labels do not make internet access acceptable"* — and I verified the default startup path makes no outbound request. All three `torch.load` sites pass `weights_only=True`, defending against a risk `SECURITY.md` explicitly declares out of scope: **the code is stronger than the promise.** And its README introduces its model list as *"a representative list"* rather than a count — which is precisely the discipline whose absence was v280's entire failure.

Where it slips, it slips at the seams it does not own: telemetry lives in the frontend repo the policy cannot reach; a dead vendored `download_file()` has sat in `comfy/` since the initial commit violating two `AGENTS.md` rules because nothing audits vendored code; 19 references still point at `comfyanonymous/ComfyUI` in a repository that moved to `Comfy-Org` — and the one class of CI this project does not run is a link checker.

## Take

⭐ **Rung 1 (30 min, the vault item)** — this corpus has found left-on default Claude trailers four times (v243's 905, v273's 599, v280's 1-of-2,055) and has never written down its own policy. ComfyUI says *strip them*; v239 said *require them*. **Write the vault's answer down**, noting that ComfyUI's gate works because it runs on PRs — a single-operator, direct-commit vault would need a different mechanism entirely.
⭐⭐ **Rung 2 (45 min, strongest borrow)** — `.coderabbit.yaml` is the cleanest working example the corpus has of **binding a prose policy to an enforcing reviewer** (`code_guidelines.filePatterns → AGENTS.md`). This vault has `CLAUDE.md` and nothing that enforces it. Copy the binding, not the vendor.
⭐ **Rung 3 (60 min)** — `SECURITY.md` + `AGENTS.md:57-73` as the template for a threat model and privacy rule a machine can act on → `hireui/evals/METHOD.md`.
**Rung 4 (~$0)** — `python main.py --cpu --disable-api-nodes`, no models. Verified safe from the code.

🔴 **NEVERs** — never install an unread custom node (`nodes.py:2263` execs it as arbitrary Python) · never run bare `--listen` (binds `0.0.0.0,::`, **zero authentication**) · never point it at candidate data · never cite a node count without its basis (**887 = 748 `define_schema` + 139 `INPUT_TYPES`**) · never re-derive this history with `git log` on git 2.19 — it truncated at 50 commits and reported 13 authors for a 358-author repo · never read the AI-trailer gate as evidence the code was not agent-written.

## Method

Two clones, byte-identical. ⚠️ **The 20-agent fleet largely failed** — the machine slept mid-run; 9 of 15 agents errored across 8.6 hours and **5.73M subagent tokens, past the 3M per-ship soft cap**. Ship completed in **report-only mode, zero further fan-outs**, on hand verification; the five dimensions that failed were ones I had already covered by hand. ⭐ Corrections made to the fleet: **a fabricated `AGENTS.md` quote** (a *"Node Input Compatibility workflow"* that does not exist in the file), **a wrong author breakdown** derived from truncating `git log`, and two `--all`-vs-HEAD scope mismatches. ⚠️ Not overcome: `comfy-org/comfy-action@main` is outside the repo so GPU-CI behaviour is UNVERIFIED; nothing was executed (1,301 tests read, none run); stars/funding are page- and web-sourced (**§37.4**).
