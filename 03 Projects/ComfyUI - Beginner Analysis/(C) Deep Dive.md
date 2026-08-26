# (C) ComfyUI — Deep Dive (v281)

**Subject:** `Comfy-Org/ComfyUI` — *"The most powerful and modular AI engine for content creation."*
**Ship:** v281 · 2026-08-26 · GOAL-ALIGNED INCLUDE 3/4 · **NO MINT**
**Source verified:** two independent full clones, working trees `diff -rq` clean (only `.git` index/reflog differ). **HEAD `7a054eb472d4f911ad3ed1d943f6e7de4d67730f`**, ComfyUI **v0.33.0**, GPL-3.0.

---

## 0. What it is

A node-graph engine for generative media. You wire boxes together — load a checkpoint, encode a prompt, sample, decode, save — and it executes the graph, caching what it can and paging models in and out of VRAM. It runs Stable Diffusion, Flux, Qwen Image, Wan, LTX-Video, Hunyuan3D, ACE-Step and dozens more, locally, offline, on consumer hardware.

It is not an AI coding-agent tool. It is on this corpus's shelf for a different reason, given in §2.

**Measured scale** (all figures from `git rev-list`, never `git log` — see §7):

| Fact | Value | Basis |
|---|---|---|
| Commits on HEAD | **5,819** | `git rev-list --count HEAD` |
| Commits all refs | **8,189** | `git rev-list --count --all` |
| Roots | **1** — `220afe33`, comfyanonymous, **2023-01-03**, *"Initial commit."* | `git rev-list --max-parents=0 HEAD` |
| Authors | **358** | `git rev-list --format='%aN' HEAD \| sort -u` |
| Top author | **comfyanonymous — 3,305 (56.8%)** | same, `uniq -c \| sort -rn` |
| Merges / tags / remote branches | 236 / 181 / 381 | `rev-list --count --merges`, `git tag`, `git branch -r` |
| Tracked files | **1,063** (792 `.py`) | `git ls-files` |
| Python LOC | **285,744** | `git ls-files '*.py' \| xargs wc -l` |
| Test functions | **1,301** | §5 |
| Node classes | **887** | §4 |
| Repo size | 134 MB | `du -sh` |

Commits per year on HEAD: **2023: 1,868 · 2024: 1,131 · 2025: 1,455 · 2026: 1,365.**

**Identity.** The root commit is comfyanonymous's own. The repository was *transferred* from `comfyanonymous/ComfyUI` to the `Comfy-Org` organisation (announced for completion ~2026-01-06; GitHub redirects the old URL). **This is the canonical ComfyUI, not a fork** — the v262 **D49** question answered from the tree: the root commit and the 5,819-commit history are continuous. Comfy Org is a funded company (**$30M at a ~$500M valuation**, Craft Ventures, April 2026; ~$47.5M total — web-sourced, not tree-verified).

**(a) FAILS.** Comfy Org is not Anthropic and not a registered (a)-7 vendor-direct source. Per §41 no inference from notability, funding, or profile.

---

## 1. ⭐⭐⭐⭐⭐ The spine: AI writes it, AI reviews it, and CI erases the fact that AI was there

This repository runs AI coding agents through **every stage of its pipeline except the one that would leave a permanent record.** Four surfaces, each verified from the tree.

### (1) It instructs agents — `AGENTS.md`, 361 lines

Added **2026-06-30** (`50e5270b`), revised **10 times** on HEAD, last edit **2026-08-03** (23 days before HEAD — current, not stale). **All 10 revisions authored by comfyanonymous**, and `CODEOWNERS` gives him sole ownership of the file:

```
* @comfyanonymous @kosinkadink @guill @alexisrolland @rattus128 @kijai
/CODEOWNERS  @comfyanonymous
/AGENTS.md   @comfyanonymous
/.ci/        @comfyanonymous
/.github/    @comfyanonymous
```

Ten sections: Engineering Style · Architecture Boundaries · No Internet Requests · State Ownership · Interface Contracts · Autograd and Model Freezing · Python Style · Model, Device, and Memory Behavior · Nodes and User-Facing Behavior · Commit and Review Habits.

The load-bearing sentence, `AGENTS.md:24-28`:

> *"Code must look hand-written for this repository. Changes that read like generic AI-generated code will be rejected automatically: unnecessary helper layers, vague names, boilerplate comments, defensive branches without a real failure mode, broad rewrites, or code that ignores the local style."*

### (2) An LLM enforces that document as policy — `.coderabbit.yaml`

CodeRabbit is configured with `profile: "assertive"`, `request_changes_workflow: true`, `auto_review.enabled: true`, and a repo-wide path instruction:

> *"Treat AGENTS.md as **mandatory repository policy**, not optional style guidance. Flag PR changes that violate AGENTS.md even when the code is otherwise functional. In particular, enforce architecture boundaries, dtype/device/memory rules, interface contracts, import style, no unnecessary try/except blocks, no inline imports, no outbound internet paths in core ComfyUI, and narrow scoped fixes."*

and a knowledge-base binding that makes it literal:

```yaml
knowledge_base:
  code_guidelines:
    enabled: true
    filePatterns:
      - files: "AGENTS.md"
        applyTo: "**"
```

Plus `enable_prompt_for_ai_agents: true` — CodeRabbit emits fix-prompts **addressed to coding agents**. And `ci-cursor-review.yml` adds a label-triggered Cursor review panel with judge consolidation, delegated to `Comfy-Org/github-workflows` and **SHA-pinned**.

⭐ So the answer to *"is the prose gated?"* is unusual: **it is gated by another AI.** Not by a test — by a reviewer that can read intent. That is the only mechanism that could plausibly enforce *"code must look hand-written"*, and they reached for it deliberately.

### (3) And CI deletes the evidence — `check-ai-co-authors.yml`

`on: pull_request, branches: ['*']`. It runs `.github/scripts/check-ai-co-authors.sh`, which builds one alternation regex from **12 named vendors** (Anthropic, Cursor, Copilot, OpenAI Codex, Aider, Gemini/Jules, Windsurf/Codeium, Devin, Amazon Q, Cline, Continue, Sourcegraph) plus **12 generic catch-alls**, walks `git rev-list base..head`, and on any match:

```
::error::AI agent Co-authored-by trailers detected in PR commits.
These trailers should be removed before merging.
To fix, rewrite the commit messages with:
  git rebase -i <base>
and remove the Co-authored-by lines, then force-push your branch.
```

**The remedy is not "don't use an agent." It is "rewrite history so it doesn't show."**

### (4) ⭐⭐⭐ Nineteen minutes

The gate did not come from a policy meeting. I measured its origin:

| Commit | Time (author, -0700) | What |
|---|---|---|
| `2bd4d82b` Luke Mino-Altherr | **2026-03-16 12:34:04** | *"feat(assets): align local API with cloud spec (#12863)"* — carries **13** `Co-Authored-By: Claude Opus 4.6` lines |
| `7d5f5252` Christian Byrne | **2026-03-16 12:53:13** | adds the workflow **and** the script |

**Nineteen minutes**, and `git merge-base --is-ancestor 2bd4d82b 7d5f5252` is TRUE. The gate is a direct, dated, same-afternoon response to the commit that provoked it — the v273 pattern (*every gate was born from a measured failure*), at the sharpest resolution the corpus has recorded.

**And it holds.** The full history carries **62 AI-trailer lines across exactly 5 commits**, and every one of those 5 predates the gate:

| Commit | Date | Trailer lines |
|---|---|---|
| `4993411f` Benjamin Lu | 2026-02-11 | 2 (Copilot) |
| `7591d781` Alexander Brown | 2026-02-21 | 1 (Claude) |
| `e544c65d` Dante | 2026-03-06 | 15 (Claude Opus 4.6) |
| `af7b4a92` Deep Mehta | 2026-03-12 | **31** (Claude) |
| `2bd4d82b` Luke Mino-Altherr | 2026-03-16 | 13 (Claude Opus 4.6) |

2+1+15+31+13 = **62** ✓. Since the gate: **899 commits, zero AI trailers.**

⚠️ **Counting correction on myself.** My first pass reported "62" from a flattened `grep -c` and my second reported "5" from a per-commit walk, and I treated them as contradictory. **Both were right** — 62 *lines* in 5 *commits*, because squash-merges concatenate every constituent commit's trailers (that is why one PR carries 31). The v278 rule replicating: enumerate, then reconcile, before publishing either number.

### What the gate cannot see

Three limits, all measured:

- **`on: pull_request` only.** Of the 899 post-gate commits, **875 are PR merges and 24 are not — and all 24 are comfyanonymous's** (verified twice, by two different methods). The person holding 56.8% of the history is the one person the gate structurally cannot observe.
- **It matches trailers, not code.** A commit written entirely by an agent passes cleanly if the trailer is stripped — which is exactly what the error message instructs.
- **"Looks hand-written" has no deterministic check.** It is adjudicated by CodeRabbit and Cursor: a paid third-party SaaS whose verdicts are non-deterministic and cannot be reproduced from the tree. Real enforcement, unauditable form.

⚠️ Note the asymmetry that makes this coherent rather than hypocritical: the founder's direct pushes escape the *AI* gate but **not** `detect-unreviewed-merge.yml`, which fires `on: push: branches: [master]`, is SHA-pinned, carries least-privilege `permissions:`, is labelled **"SOC 2 compliance"**, and files tracking issues in a separate `Comfy-Org/unreviewed-merges` repo. It records rather than blocks — but it does cover the path the AI gate misses.

---

## 2. Why this is on the shelf — (b) MODERATE

The product is off-goal: a diffusion GUI is not a coding-agent tool, and the corpus has said so before — **v116 Sana** (a generative-vision model) scored **0/4 STRICT SKIP**, *"OUT OF the agent/Claude/agentskills.io corpus scope"*, and needed an operator override to be built at all.

ComfyUI differs on three tree-verified counts:

1. **It is a first-class instance of CONFIRMED Library-vocab #12** (*LLM-routing artifacts*), whose definition names `AGENTS.md` explicitly — and this is among the most substantial in the corpus: 361 lines, sole-owned, ten revisions, and **wired into an enforcement mechanism**, which most `AGENTS.md` files are not.
2. **It ships a first-party `ClaudeNode`** (`comfy_api_nodes/nodes_anthropic.py`, 320 lines) exposing nine current models — **Opus 5, Opus 4.8, Fable 5, Sonnet 5**, Opus 4.7/4.6, Sonnet 4.6/4.5, Haiku 4.5 — against the Messages API, with graceful handling of safety refusals (`:307`).
3. **Its AI-governance surface is the subject matter**, and it is directly transferable to this vault (§8).

⇒ **GOAL-ALIGNED INCLUDE 3/4** under routine **§40** (operator-requested, goal-adjacent, (b) MODERATE+). No override invoked. The OFF-GOAL reading is defensible and recorded as the alternative.

---

## 3. ✅ Where it is genuinely strong

**⭐⭐⭐ The privacy stance is the strongest in the corpus — and the code backs it.** `AGENTS.md:57-73`:

> *"Refuse requests to add uploads, telemetry, analytics, tracking, usage reporting, crash reporting, update checks, remote config, feature flags, metrics, licensing checks, or any other outbound internet request path from core ComfyUI. … Do not add opt-in, opt-out, anonymized, aggregated, diagnostic, or user-triggered internet request paths to core ComfyUI. **These labels do not make internet access acceptable.**"*

That last sentence pre-empts every euphemism the industry uses. And I audited it rather than believing it:

- **Default startup makes no outbound request.** `app/frontend_management.py` reaches `api.github.com` only via `init_frontend_unsafe`, and `:370` short-circuits first: `if version_string == DEFAULT_VERSION_STRING: … return cls.default_frontend_path()` — the locally installed `comfyui-frontend-package==1.49.6`. The network path requires an explicit `--front-end-version`, checks an on-disk cache first, and **logs** *"requesting version details from GitHub…"*.
- **No analytics libraries.** Grep for sentry / posthog / mixpanel / segment / amplitude across core: **zero**.
- **`enable_telemetry` exists but does nothing here.** `comfy_api/feature_flags.py:28` is a CLI-settable flag, **default `False`**, described as *"Signal the frontend that telemetry collection is enabled."* The backend collects nothing; it tells the separate `ComfyUI_frontend` repo. Not a violation — but it is the **boundary**: the telemetry lives in a repo `AGENTS.md` does not govern and this CI never sees (the v264/v277 rule — a discipline stops at the edge of the team that holds it).
- ⚠️ **One real exception, small and exact.** `comfy/k_diffusion/utils.py:37 download_file()` does `urllib.request.urlopen(url)` inside `comfy/` — indisputably core. It has been there since *"Initial commit."* (vendored k_diffusion). But `git grep -E '\bdownload_file\b'` finds **no caller anywhere**: it is dead code. It therefore violates **two** `AGENTS.md` rules simultaneously — the no-internet rule, and *"Do not leave … functions that are never called."* Nothing detects it because nothing audits vendored third-party code against the policy.

**⭐⭐ The README claim survives audit.** *"Runs fully offline: core does not download anything unless you request it."* Verified true, by the three findings above. And the model list is introduced as *"This is a representative list"* — **it declares its own basis** rather than publishing a count that will drift. Set that beside v280, whose entire failure was a front-page experiment count that went stale in two places at once.

**⭐⭐⭐ `torch.load` is safe at every call site.** Exactly three uses in the tree, and **all three pass `weights_only=True`**: `comfy/sd1_clip.py:455`, `comfy/utils.py:191`, `comfy_extras/nodes_dataset.py:2097`. Note that `SECURITY.md` declares deserialization *out of scope* as an upstream PyTorch problem — **the code is stronger than the claim it makes for itself**, an inversion of the usual corpus finding.

**⭐⭐⭐ `SECURITY.md` is the best-reasoned threat model in the corpus.** It states four assumptions, then declares six categories of non-vulnerability *with reasons*. It is honest about the thing most projects hide:

> *"Anyone with access to the ComfyUI URL is trusted (a direct consequence of the localhost-only default)."*

**There is no authentication at all, and they say so and explain why.** Its central claim is verifiable: *"By default, the server binds to `127.0.0.1`"* → `comfy/cli_args.py:63 default="127.0.0.1"` ✓. (Bare `--listen` with no argument flips to `const="0.0.0.0,::"`, documented in the help text.) Contrast v278, which shipped a debugger control plane on `0.0.0.0` with zero auth and no disclosure at all.

**⭐⭐ Three independent instances of one discipline: make it fail loudly.**
- `.coderabbit.yaml`: `fail_commit_status: true`, with the reason written down — *"Without this, a review that never happened (rate limit, internal error) still posts a green 'CodeRabbit' commit status, so a throttled review is indistinguishable from a clean one."*
- `comfy_api/feature_flags.py:_coerce_bool` raises on anything but `true`/`false` — *"rather than silently treating typos like 'ture' or 'yes' as False."*
- `ruff` selects `S307` (eval) and `S102` (exec) explicitly.

That is v262's rule (*a gate that cannot fail is worse than one nobody invokes*) applied correctly, three times, by them.

**⭐ Security guidance written for agents.** `AGENTS.md:307-313` tells agents to treat `io.Combo`/`io.DynamicCombo` values as **untrusted** wherever they touch the filesystem, re-validated at the load/save boundary — *"Do not rely only on the advertised combo options or prompt validation."* Defense-in-depth against client-side trust, addressed to a machine.

---

## 4. Architecture, measured

**Two node registration systems coexist**, and any single node count is meaningless without saying which:

| Location | `define_schema` (new API) | `INPUT_TYPES` (legacy) |
|---|---|---|
| `nodes.py` | 0 | **65** |
| `comfy_extras/` (135 modules) | **493** | 74 |
| `comfy_api_nodes/` (39 vendors) | **255** | 0 |
| **Total** | **748** | **139** |

**887 node classes** by the basis *"defines `define_schema` or `INPUT_TYPES`"*. Cross-check: `nodes.py` yields **65** by both `INPUT_TYPES` count and `NODE_CLASS_MAPPINGS` entry count — two independent methods agreeing.

**The commercial layer is in the tree.** `comfy_api_nodes/` holds 39 vendor modules — anthropic, openai, gemini, grok, qwen, bfl, bytedance, kling, luma, runway, sora, veo2, elevenlabs, minimax, recraft, ideogram, topaz, tripo, meshy, hunyuan3d and more — and **255 node classes, 29% of all nodes**. They do not call vendors directly: `comfy_api_nodes/util/_helpers.py:74` routes through `https://api.comfy.org` with `Authorization: Bearer {auth_token_comfy_org}`, and responses carry `X-Comfy-Credits-Used`. **Comfy Org is the broker and the meter.** A GPL-3.0, local-first, categorically-no-telemetry engine, with a first-party paid brokerage bolted to the side — cleanly separated by the word *"core"* in every `AGENTS.md` rule, and switchable off with `--disable-api-nodes`.

**Custom nodes are arbitrary code, by design and by disclosure.** `nodes.py:2263 module_spec.loader.exec_module(module)`. `SECURITY.md` states it plainly.

**Dependency pinning is inverted.** The five first-party packages are exact-pinned — `comfyui-frontend-package==1.49.6`, `comfyui-workflow-templates==0.11.46`, `comfyui-embedded-docs==0.5.10`, `comfy-kitchen==0.2.31`, `comfy-aimdo==0.4.15`. Every third-party dependency is unpinned or floor-pinned; **`torch` carries no version constraint at all.** Defensible for a project that must span many torch/CUDA builds, but it means the packages they control cannot move and the ones they do not can.

---

## 5. Tests: 98.4% covered, and the 1.6% has a legible cause

**1,301 test functions**, reconciled by two methods:

| Location | Module-level | Async module-level | Class methods | Total |
|---|---|---|---|---|
| `tests-unit/` | 430 | 41 | 670 | **1,141** |
| `tests/` | 0 | — | 160 | **160** |
| | | | | **1,301** ✓ |

**Exactly two `pytest` invocations exist across all 28 workflows:**
- `test-unit.yml` → `python -m pytest tests-unit` (1,141)
- `test-execution.yml` → `python -m pytest tests/execution -v --skip-timing-checks` (160)

Both run `on: push` **and** `pull_request`, across Ubuntu/Windows/macOS. **1,280 of 1,301 tests run in ordinary CI — 98.4%.** That is far better than most subjects this corpus reads (v276 ran 1 of 349).

⭐ **But `tests/` has four test locations and CI names one.** Never executed by any job:

| Path | Tests |
|---|---|
| `tests/inference/` | 1 |
| `tests/compare/` | 4 |
| `tests/test_asset_seeder.py` | 16 |
| **Total invisible** | **21** |

**And the cause is a mechanism mismatch, not neglect.** `pytest.ini` declares a marker system with documented deselect syntax:

```
markers =
  inference: mark as inference test (deselect with '-m "not inference"')
  execution: mark as execution test (deselect with '-m "not execution"')
testpaths =
  tests
  tests-unit
```

Six files carry those markers. **No CI job ever selects or deselects by marker** — CI selects by *path*. So `@pytest.mark.inference` exists to let you exclude inference tests from a run that never happens, and the three siblings of `tests/execution/` fall through the gap between the two selection systems. ⭐ Note the inversion: `testpaths = tests, tests-unit` means a developer running bare `pytest` locally collects **all 1,301** — **the local default is broader than the CI default.**

⚠️ GPU tests are opaque: `test-ci.yml` and `pullrequest-ci-run.yml` delegate to `comfy-org/comfy-action@main`, whose source is not in this repository. What it runs is **UNVERIFIED**.

---

## 6. CI hardening: real, and applied where it was thought about

**57 `uses:` lines across 28 workflows. 5 are SHA-pinned (8.8%).** The pinned five are exactly the third-party and reusable-workflow calls — `contributor-assistant/github-action`, `Comfy-Org/github-workflows` ×2, `actions/create-github-app-token`, plus one `actions/checkout` inside `backport_release.yaml`. The other 52 are first-party `actions/*` at floating tags.

⭐ The repo cites the rule by name, once: `ci-cursor-review.yml:23` — *"SHA-pinned per zizmor `unpinned-uses: hash-pin`. Bump this SHA to pick up upstream changes; keep `workflows_ref` matching so prompts/scripts load from the same commit as the workflow definition."* That is careful reasoning about a real failure mode (workflow and prompts drifting apart). It is also the only file that mentions it. Pinning third-party and trusting `actions/*` is a defensible policy — but the citation reads as a standard while it is a one-file practice, and nothing lints it.

Minor drift the absence of that lint permits: `ruff.yml` uses `actions/setup-python@v2` at line 15 and `@v4` at line 34 — **two major versions of the same action in one file**; `github-script` is `@v6` in one workflow and `@v7` in another.

**`pull_request_target` appears in three workflows** and two are safe by construction — `cla.yml` and `api-node-template.yml` never check out PR code (`api-node-template.yml` carries explicit `permissions: contents: read, pull-requests: write` and only appends to a PR body).

⚠️ The third is real: **`pullrequest-ci-run.yml` combines `pull_request_target` + self-hosted macOS/Linux/Windows runners + `secrets.GCS_SERVICE_ACCOUNT_JSON` + `uses: comfy-org/comfy-action@main`** — a mutable branch ref. Its mitigation is a human one: it fires only on the `Run-CI-Test` label. Compare v273 and v275, where the `pull_request_target` workflow **names the hazard in its header and states the invariant that makes it safe**; this one's header explains what it does, not why it is safe.

**Lint scope:** `ruff.yml` runs `ruff check .` on `[push, pull_request]` with no path filter — genuinely repo-wide. Its companion `pylint` job runs on **`comfy_api_nodes` only**.

**No link checking of any kind exists** (`lychee`/`markdown-link-check`/equivalents: zero) — which is why §7 survives.

---

## 7. The namespace the project has outgrown

`git grep` across all tracked files: **19 references to `comfyanonymous/ComfyUI`** in five files — `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `comfy/cli_args.py`, `pyproject.toml` — against 6 to `Comfy-Org/ComfyUI`. Including:

- `pyproject.toml:9` → `repository = "https://github.com/comfyanonymous/ComfyUI"` — **published package metadata**
- `SECURITY.md` → routes vulnerability reports to the old namespace
- `README.md` → all release/download badges, and the "Release Process" section, which names *"ComfyUI Core"* at the old URL while naming its two sibling repos at `Comfy-Org/`

GitHub redirects, so nothing is broken and no user is harmed. But it is the corpus's standing drift class at an eighth site: **the repository moved and its self-description did not**, and no gate exists that could notice — because a link checker is the one kind of CI this project does not run. ⚠️ This is the vault's own disease (`_state/03c-projects-v61-v183.md` still carries a filename saying `-v183` while holding entries through v281), which is why §8 Rung 1 is what it is.

⚠️ **METHOD — the v267 pathology, replicated and caught in the first five minutes.** `git` here is **2.19.0**, and `git log` silently truncated at 50 commits: it reported **13 authors** and a **first commit of 2026-08-14** for a repository with 358 authors and a root in **January 2023**. Every count in this document comes from `git rev-list`. Anyone re-deriving these figures with `git log` on an old git will get different, wrong answers.

---

## 8. Verdict and what to take

**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG. **NO MINT.**

**Mint analysis, done by hand:**
- **Node-based generative-media engine** = the corpus's **first** subject in this domain (58 §C rows checked; nothing adjacent — C37 is *agent-first* video production, which this is not). **Domain-not-capability ⇒ NOT minted**, on the settled v212 tabularis precedent (*"the corpus's FIRST database-GUI/SQL-client DOMAIN subject — corpus-first-DOMAIN data-point, NOT a §C mint"*), reinforced by v196 meetily and v210 AIRI. Also decisively **not world-first**: node-graph media tools long predate it, and AUTOMATIC1111 preceded it in diffusion GUIs.
- **`AGENTS.md`** = a clean instance of **CONFIRMED Library-vocab #12** (*LLM-routing artifacts*), whose written definition names the artifact type. Instance-strengthening; N-tally is audit bookkeeping, not self-incremented.
- **CI-enforced erasure of AI-authorship trailers** = a **practice**, not a capability layer. **RECORDED as the audit-reviewable §C-2 candidate, NOT minted** — the v211 technique discipline and the v279/v280 handling.

**Counts 46/12 UNCHANGED; §C-1 13, §C-2 39 UNCHANGED.**

**PILOT: ⭐⭐ read-and-borrow, plus one genuinely safe local run.** The engine itself is not a hireui component and never touches candidate data. What transfers:

- **⭐ Rung 1 (30 min, the vault item).** Take `check-ai-co-authors.sh` as the *shape* of a provenance decision and answer the opposite question for this vault: this corpus has repeatedly found left-on default Claude trailers (v243's 905, v273's 599, v280's 1-of-2,055) and has no stated policy of its own. ComfyUI's answer is *strip them*; v239's was *require them*. **Write the vault's answer down**, and note that ComfyUI's gate covers 875 of 899 commits precisely because it runs on PRs — the same reason the vault's own single-operator, direct-commit workflow would need a different mechanism entirely.
- **⭐⭐ Rung 2 (45 min, the strongest borrow).** `.coderabbit.yaml`'s `path_instructions` are the cleanest working example the corpus has of **binding a prose policy document to an enforcing reviewer** — `code_guidelines.filePatterns → AGENTS.md`, plus per-directory focus lists. This vault has `CLAUDE.md`, `_state/`, `_patterns/` and nothing that enforces any of it. Copy the *binding*, not the vendor.
- **⭐ Rung 3 (60 min).** Read `SECURITY.md` and `AGENTS.md:57-73` together as a model for writing a threat model and a privacy rule that a machine can act on — then set them beside `hireui/evals/METHOD.md`. The sentence to steal verbatim in spirit: *"These labels do not make internet access acceptable."*
- **Rung 4 (~$0, optional).** Clone, `pip install -r requirements.txt`, `python main.py --cpu --disable-api-nodes` with no models present. Verified from the code: no network at startup, binds `127.0.0.1`, and `--disable-api-nodes` severs the api.comfy.org path.

🔴 **NEVERs.** Never install a custom node you have not read — `nodes.py:2263` executes it as arbitrary Python, and the project says so. Never run with bare `--listen` — it binds `0.0.0.0,::` and **there is no authentication whatsoever**. Never point it at candidate or production data. Never cite a node count without naming the registration system (**887 = 748 `define_schema` + 139 `INPUT_TYPES`**). Never re-derive this repo's history with `git log` on git 2.19 — use `rev-list`. Never assume the AI-trailer gate means the code was not written by an agent; it means the trailer was removed.

---

## 9. Method and its limits

**Source:** two full clones, working trees byte-identical, HEAD `7a054eb4`. Every number here is my own command output, stated with its basis.

⚠️ **The 20-agent fleet largely failed.** The machine slept mid-run; 9 of 15 agents errored (stalls, schema-retry exhaustion), 6 completed, over 8.6 wall-clock hours and **5.73M subagent tokens — past the 3M per-ship soft cap**. Per the binding loop-budget rule the ship was completed in **report-only mode with zero further fan-outs**, on hand verification. Five dimensions returned (governance, agents-md, api-surface, tests, ecosystem-identity); the five that did not — ai-review-layer, security, ci-surface, claims-audit, architecture — **I had already covered by hand before launching**, which is why coverage held.

⭐ **Corrections I made to the fleet's output:**
- **A fabricated quote.** An agent claimed `AGENTS.md` references a *"Node Input Compatibility workflow"* and quoted a sentence from it. `awk` over all 361 lines: **no such text**. Every occurrence of "workflow" in `AGENTS.md` means a ComfyUI node-graph, not a CI job. Discarded.
- **A wrong author breakdown.** An agent reported the recent non-PR commits split across seven people (8 by Alexander Piskun, 3 by Terry Jia…), derived via `git log -900` — the truncating command. Re-derived twice with `rev-list`: **all 24 are comfyanonymous's.**
- **Scope mismatches** on author and year totals (`--all` vs HEAD): agents' 3,327 / 14 revisions vs my HEAD-scoped **3,305 / 10**. Mine used throughout, scope stated.

⚠️ **Not overcome:** `comfy-org/comfy-action@main` is outside the repo, so GPU-CI behaviour is **UNVERIFIED**. Nothing was executed — 1,301 tests read, none run (no GPU, no models, and `python3` is unavailable in this sandbox). Star/fork figures are page-stated only (**§37.4** — the GitHub API is mocked here); funding and the repo-transfer date are web-sourced, not tree-verified.
