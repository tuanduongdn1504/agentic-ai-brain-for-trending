# (C) OpenSandbox — Verdict

**Wiki v244** · 2026-08-19 · [`opensandbox-group/OpenSandbox`](https://github.com/opensandbox-group/OpenSandbox) · Apache-2.0 · ✅ source-cloned twice

---

## Phase 0.9 — INCLUDE decision

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** Author is Anthropic / a registered vendor-direct source | **FAIL** | **Alibaba Group Holding Ltd.** — declared in 1,674 CI-enforced copyright headers, the root commit's `@alibaba-inc.com` address, and every Maven/npm/NuGet/Go coordinate. Corporate-but-not-Anthropic ⇒ FAIL per **§41** (the NVIDIA v169 precedent). No inference-rescue attempted. |
| **(b)** Goal relevance | **STRONG** | **This is the execution substrate for AI agents** — squarely Goal #1. It ships a first-party **MCP server**, **six installable agent skills** across six harnesses, and **nine coding-agent examples** with Claude Code named first. Not goal-*adjacent*; goal-*core*. **No §40 needed.** |
| **(c)** Quality / rigour | **STRONG** | 19-OSEP Kubernetes-KEP-style process (10 `implemented`), 447 test files across six languages, OpenSSF Best Practices **passing at 100%**, cosign keyless release signing + provenance attestations, a documented crypto key-length policy with named enforcement points, 19 lockfiles and **zero npm lifecycle scripts**. |
| **(d)** Analysability | **STRONG** | Fully public, Apache-2.0, source-cloned twice; 2,400-commit history intact with one root commit and no rewriting. |

### ⇒ **GOAL-ALIGNED INCLUDE — 3/4** *(cleanly; (b) STRONG keys the tier, no operator override, no §35 pressure)*

**Streak: v243 `GA:101` → `GA:102 · OG:13 [7 ov]`** — **25 consecutive goal-aligned ships (v220 → v244)**.
**§35 CLEAR:** rolling window {v242 GA, v243 GA, **v244 GA**} = 0 OFF-GOAL.
**Tier:** T1 agent-capability substrate (infrastructure/platform facet).

---

## The mint decision

### ⭐ **MINT — 1 NEW §C standalone at N=1**

> **"Self-Hostable Sandbox / Code-Execution Runtime for AI Agents"** — an open-source, self-hosted control plane that provisions, runs, inspects, snapshots and destroys **isolated execution environments** for agent workloads, exposing them through multi-language SDKs, a CLI, an MCP server and a public API contract, with per-sandbox network egress policy and credential injection, over pluggable container/Kubernetes backends.
>
> **N=1** · anchor **v244 OpenSandbox** (`opensandbox-group/OpenSandbox`, Alibaba) · **CORPUS-FIRST for the surface, explicitly NOT world-first.**

**Counts: 46 confirmed patterns / 11 CONFIRMED Library-vocab — UNCHANGED.** §C live standalones **49 → 50**; §C surface ≈56 → ≈57.

### Why it mints

1. ⭐ **Verified corpus-first, by my own grep — not delegated.** Across `_state/03c` and `_patterns/06`, **E2B appears 14 + 10 times and every single occurrence is as a dependency or substrate *inside another subject*** (open-lovable v224's live preview, Strix v190's Kali sandbox, grok-build v215's worktrees, DSH v235's sandbox plugin seam, ClawWork v233's harness). One `micro-VM` mention corpus-wide. **No §C row describes the execution layer itself.** The corpus has been reading things that *stand on* sandboxes for 243 wikis without ever reading a sandbox.
2. ⭐⭐ **It is the last missing member of a family the corpus mints repeatedly.** The agent-capability-layer cluster is well established and each member minted at N=1: **browser** (`browser-use` v41), **iOS simulator** (`serve-sim` v183), **web/social reach** (`Agent-Reach` v174), **Office documents** (`OfficeCLI` v206), **stealth browser** (`camofox` v179), **database** (`tabularis` v212), **file search** (`fff` v194), **video** (`video-use` v198 / `OpenMontage` v188). Every one answers *"what can the agent reach?"* — and **the one an agent needs most, somewhere safe to run code, was absent.** This is a capability an agent *gains*, not a domain it operates in, so the **v196 meetily / v210 AIRI / v211 PixelRAG domain-not-capability** bar is cleared.
3. **Mint-at-N=1-for-a-corpus-first-capability is settled precedent, when scoped not-world-first:** grok-build v215, openinterpreter v223, fff v194, serve-sim v183, llm-space v221, career-ops v200, open-lovable v224, ClawWork v233, OfficeCLI v206, CLIProxyAPI v207.
4. **It is a working tool, not a collection** — clearing the v201 `awesome-llm-apps` collection-not-minted line decisively.

### ⚠️ The NO-MINT alternative — recorded, and genuinely strong

**The case against, at its strongest: `kubernetes-sigs/agent-sandbox` (Nov 2025, KubeCon Atlanta) had already standardised this shape three months before OpenSandbox's public launch — and OpenSandbox *supports* that standard (OSEP-0002, `status: implemented`) rather than setting it.** When a Kubernetes SIG owns the category, it is an established industry class, not a corpus-shaping capability — the **v240** (awesome-selfhosted's data repo + HACS decisive) and **v242** (Eclipse RCP/OSGi decisive) discipline. Add: E2B (2023) and Daytona precede as products; Anthropic ships first-party Claude Code sandboxing; **§5 of the Deep Dive shows OpenSandbox delegates isolation rather than implementing it**, so the class is "an API over other people's isolators"; **fame ≠ mint** (v222 lobehub, v201) and 14.3k stars earn nothing; and **§28** anti-inflation cuts against a 50th standalone.

**I lean MINT** — the corpus-first-capability grounds are strong and the class is genuinely load-bearing for Goal #1 — **but this is the closest mint call since v233, and it is flagged for the operator or the audit to flip.** If flipped, the fallback is: a corpus-knowledge data-point + a DEFERRED watch axis *"self-hostable agent code-execution substrate,"* counts unchanged.

### Explicitly NOT minted

- ❌ **Not** a §C row for the AGENTS.md/CLAUDE.md bridge — see below, that is instance-strengthening of an existing row.
- ❌ **Not** a mint for the 19-OSEP process (a governance practice, not an agent capability).
- ❌ **Not** a mint for the `osb skills` renderer — that is **Pattern #84 84c**, already CONFIRMED.
- ❌ **Not** world-first at anything (Deep Dive §9).

---

## ⭐⭐ RECORDED, NOT EXECUTED — flagged to the audit

### 1. The committed cross-harness agent-context bridge reaches **N=3** — and crosses the eligibility threshold

- **v213 geti** — committed cross-harness symlinks for a first-party skill suite (N=1)
- **v243 ToolJet** — `CLAUDE.md` as a 9-byte symlink to canonical `AGENTS.md`, at 3 of 13 dirs (N=2, *recorded and flagged by v243, not promoted*)
- **v244 OpenSandbox** — `server/CLAUDE.md` as a 9-byte symlink to `AGENTS.md`, **plus** an 85-byte prose stub at root (**N=3**)

⭐ **This is now three independent, cross-author, cross-domain, non-port instances** (Intel / ToolJet / Alibaba). The corpus's **eligible-at-N=3** discipline (v203) is therefore **satisfied**, and a promotion is now live on the table.

⚠️ **I am recording it and not executing it — a promotion is an audit act (the v232 rule, upheld at v235 and v243).** Three things the audit should weigh:

- The three instances are **not the same mechanism**: geti symlinked a *skill suite*; ToolJet symlinked the *root context file* (the load-bearing half); OpenSandbox symlinked a *subdirectory* context file and used a **prose stub** at root. So the class may need to be stated as *"a committed, drift-proof bridge from the harness-specific filename to a canonical `AGENTS.md`"* — mechanism-agnostic — or it will fracture at N=3.
- **Both multi-instance cases are partial**: ToolJet 3 of 13 directories, OpenSandbox 2 of 6, and OpenSandbox uses **two incompatible mechanisms inside one repo**. The pattern's real-world form is *incomplete adoption*, and the row should say so.
- The prose-stub variant is drift-proof too (it carries no content), but it is **weaker for the harness** — it costs a second read. If the row is promoted, it should rank the mechanisms, not just enumerate them.

### 2. A **positive counter-example** to the broken-authentication triad — a new axis worth registering

The vault recorded a broken-auth triad at **v231** (`require_auth:false` + wildcard CORS while holding live sessions) and **v232** (auth fails open, `0.0.0.0`, wildcard CORS). ⭐ **OpenSandbox ships the same convenience mode and gates it behind an explicit, timed, logged, bilingually-documented consent check that fails CLOSED on timeout** (`startup_guard.py` — env-var path, ANSI-red TTY prompt requiring exact `YES`, 30-second abort, tracking-issue link). **This is the corpus's first instance of the *right* answer to that failure mode.** Recorded as a candidate axis — *"insecure-by-convenience mode behind a fail-closed informed-consent startup gate"* — **not minted**; it is a *mechanism within* a security posture, and one instance.

### 3. Instance-strengthening, bookkeeping only (no N self-increment)

- **Pattern #18 sub-archetype B1-MCP** → +1 (`sdks/mcp/sandbox/python`, `pip install opensandbox-mcp`, stdio + http configs, documented for Claude Code and Cursor). Recorded for the audit's tally.
- **Pattern #84 84c** *"CLI-generates-native-formats-from-canonical-source"* → +1, and a **notable new form**: the first instance from an *infrastructure vendor* rather than a skills project, and the first to distinguish **copy** targets (harnesses with a skills directory: Claude Code, Cursor, Codex) from **append** targets (harnesses with one instruction file: Copilot, Windsurf, Cline).
- **Pattern #83 honest-deficiency-disclosure** ×2 — the `OPENSANDBOX_INSECURE_SERVER` warning documented in four places plus two Chinese-language example configs; **and** the gVisor-is-incompatible-with-our-egress-policy trade-off encoded in validators and tests rather than hidden.
- **Pattern #66 supply-chain positive exemplar** — joins **pi v228** and **ToolJet v243**: zero npm lifecycle scripts across all five `package.json` files, 19 lockfiles, no lockfile mirror substitution, cosign keyless signing with provenance attestations.
- **Pattern #19** — (a) FAIL on corporate-not-Anthropic; no ecosystem-portfolio claim made.

---

## ⭐ New method rules

- **D28 — an absent config file is not an absent check.** 24 workflows, zero scanner references, no `dependabot.yml` — yet 18 `Copilot Autofix` commits and 5 `dependabot/` branches prove both run via GitHub *settings*, invisible in the tree. A tree-only audit systematically **under**-reports automated security posture; the detector is the bot's commit trailers. Completes the trio with **D26** (what a body-grep counts) and **D27** (which refs it counts over).
- **D29 — `mtime` is not drift; test the claims, not the date.** A critic called `cli/AGENTS.md` "67 days stale"; I tested all 11 paths it names and **every one exists.** Staleness is content disagreeing with reality. ⭐ **This is the discipline that decides whether `verify-vault-docs` is a linter or just a recency alarm.**
- **D30 — when the API is mocked, read the repo's own committed badges.** A hardcoded `Stars-11.6k` badge, replaced in a dated commit, yielded a verifiable dated metric that §37.4 otherwise forbids.
- **D26 extended — the commits↔trailer-lines gap measures merge strategy.** v243: 165 commits / 905 lines (mean **5.48**, squash-dominant). v244: 197 / 340 (mean **1.73**, merge-commit-dominant). Same metric, different meaning — report the ratio *and* the strategy.

---

## ⚠️ PILOT RULING — **READ-AND-BORROW. Do not point it at candidate data.**

This is the first subject in eleven ships that is *architecturally* pilotable for hireui rather than only readable — Apache-2.0, no copyleft trap, and it solves a problem hireui will eventually have (running untrusted code / third-party tooling in isolation). **But it is not a hireui component today, and three fences are non-negotiable:**

- 🔴 **Never point it at candidate data.** Sandboxes execute untrusted code by design; a CV-processing path inside one is a data-residency and PII question the **RATIFIED candidate-LLM legibility ADR** governs, and it is out of scope for a pilot.
- 🔴 **Set `server.api_key` before anything else, and never set `OPENSANDBOX_INSECURE_SERVER=YES` on a reachable host.** The default binds `0.0.0.0` (Deep Dive §6.1).
- 🔴 **Test the proxy-path bypass first** (§6.2). In single-tenant mode, `/v1/sandboxes/{id}/proxy/{port}/...` skips the API-key check *even when a key is set*. Whether `secure_access` covers it is **unverified** — verify it yourself before exposing anything, and if it is a real hole, **report it upstream** via their private security advisory (they commit to a 48-hour acknowledgment).
- ⚠️ **Do not build their K8s images without knowing the mirrors.** Two Dockerfiles rewrite Alpine to `mirrors.aliyun.com` and set `GOPROXY=goproxy.cn` (§6.3). Use the published cosign-signed images and **pin by digest**.
- ⚠️ **Do not expect gVisor/Kata/Firecracker isolation for free** — you install the runtime; and **choosing gVisor disables their egress policy** (§5).
- ⚠️ `pip install opensandbox-cli` writes skills into `~/.claude/skills` when you ask it to — run `install-snapshot` first, and prefer project scope over user scope.

**Grade:** ⭐⭐ **the strongest architecture-borrow of the run, and a genuine future infrastructure candidate** — but a fenced pilot, not an adoption.

---

## ⭐ THE PAYOFF — a tenth consecutive ship hands the vault a piece of `verify-vault-docs`, and this one hands over the *proof* the doctrine needs

The chain: **v239** the linter · **v240** prose-vs-code + the inventory rule as working code · **v241** provenance-at-divergence + **D22** · **v242** **D23** · **v243** ⭐ the **symlink** + the living-docs rule as deployable policy + the proof that policy without a linter fails · **v244** ⭐⭐ **the third symlink instance (N=3, promotion now eligible), the source-of-truth ownership table, and — the real gift — `D29`: the discipline that separates a linter from a recency alarm.**

⭐ And the single best artifact of the run is one commit. **PR #1100 (`fb5a2c91`, 2026-06-18)** deleted stale agent-facing prose *by name* — *"outdated content … 'Planned' K8s roadmap, stale internal implementation details"* — and, **in the same PR**, added the `CLAUDE.md` symlink that makes that class of staleness structurally impossible. `Co-Authored-By: Claude Opus 4.6` on both bullets. **The vault's own D22 diagnosed and structurally fixed in one commit, by Claude, in a stranger's repository.** That is the template: *delete what rotted, then remove the mechanism that let it rot.*

---

## Blunt assessment

**Alibaba built the thing a coding agent most needs and then spent six months making it look like nobody built it.** The GitHub org has zero public members. `GOVERNANCE.md` — nine and a half kilobytes on maintainers, consensus and conflict-of-interest recusal — never says the word Alibaba. There is a CNCF Landscape entry, an OpenSSF badge at 100%, a nineteen-proposal enhancement process borrowing Kubernetes' exact status vocabulary, and a commit that says in plain words *"Update repository links after GitHub org migration."*

And it cannot finish, because **a required status check on every pull request fails the build unless the file says `Copyright Alibaba Group Holding Ltd.`** — which is why 1,674 files say it, and why every new file any of the 119 contributors writes must say it too. They de-branded everything a human reads and left a robot re-branding everything a compiler reads. Ten `go.mod` files still declare `github.com/alibaba/...`, zero declare the org the code actually lives in, the README's own `go get` line depends on GitHub redirecting from the org they left, and the OpenSSF badge still lists the old URL. **This is the most precise illustration the corpus has of what open-source vendor-neutrality can and cannot reach: documents are cheap to neutralise, and build gates, module paths, package coordinates and copyright headers are not — because those are the ones with downstream consumers.** Nothing here is dishonest. Every fact is in the tree. But the *interface* says community and the *build* says Alibaba, and the build is the part that is enforced.

The engineering is good, and better than its own marketing. The README's one 🏰 bullet claims gVisor, Kata and Firecracker isolation; the code passes a `runtimeClassName` through and makes you install the runtime — while quietly encoding, in validators and tests, the genuinely useful fact that **choosing gVisor turns off their egress control.** The marketing hides the honest part. Meanwhile the security posture is the best in the run: cosign keyless signing, a crypto key-length policy with named enforcement points, zero npm lifecycle scripts, no lockfile mirrors — and `startup_guard.py`, which takes the exact insecure-by-convenience default that made v231 and v232 pilot-AVOID and puts it behind a red-text prompt that demands you type `YES` and **aborts if you say nothing for thirty seconds.** **That is the first time this corpus has seen the right answer to that failure mode, and it is nine lines of it worth copying.** One finding survives in the other direction: in single-tenant mode a proxy route skips the API key *even when you set one* — the consent gate protects the operator who configured nothing, and a different code path un-protects the one who configured something.

For us, the lesson is smaller than the repo and sharper than anything in it. **They solved the hard drift problem with code and the easy one by hand.** One canonical skill rendered into six harnesses across two different file layouts, from a single source, by a function — that is engineered. One file with two names — `AGENTS.md` and `CLAUDE.md` — they solved twice, differently, and put the drift-proof mechanism in the subdirectory while the root, the file Claude Code opens first, got a prose stub. v243 made the mirror-image error: it symlinked so two files could not diverge, then hand-copied one paragraph into three skill files where it came out different three times. **Two unrelated companies, opposite mistakes, one cause: whatever a machine does not generate, humans will let diverge.** Our `_state/03c-projects-v61-v183.md` has held entries through v244 for sixty-one versions. Four ships have now diagnosed that exact defect and none of us has run `ln -s`.

And I was wrong twice in ways worth recording. I opened this analysis thinking the affiliation was concealed; it is in 1,674 copyright headers and every install coordinate, and the org page is the *only* place it is missing — which exonerates them. I wrote "auth fails open" before finding `startup_guard.py`, which is the opposite of what I claimed. Both corrections made the findings better, and both came from checking rather than concluding — as did the one I never wrote, when 406 references to a second domain turned out to be Kubernetes API groups. **The verifier fleet, meanwhile, told me this project used Claude in three commits out of 2,400 and was "not Claude-Code-native." It is 197 commits and 340 trailer lines — a sixty-five-fold error, produced by sampling fifty commits and then inventing a tooling limitation to explain the result.** Nine ships have handed us parts for a linter. This one also handed us the reason a linter needs a rule that a file which has not changed in sixty-seven days, because it is still true, is not stale.

*Verdict by Claude (Opus 5) for Storm Bear · v244 · 2026-08-19*
