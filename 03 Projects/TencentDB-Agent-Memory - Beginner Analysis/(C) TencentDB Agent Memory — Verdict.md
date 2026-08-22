# (C) TencentDB Agent Memory — Verdict

**v265** · `TencentCloud/TencentDB-Agent-Memory` · MIT · 2026-08-22
**GOAL-ALIGNED INCLUDE 3/4** · **NO MINT** · counts **46/12 UNCHANGED** · **READ-AND-BORROW, do not deploy as-is**

---

## The one-paragraph verdict

Tencent Cloud has open-sourced a genuinely capable team-scoped memory platform for AI coding agents — 183,339 lines of TypeScript, a first-class Claude Code path, and an asset-governance model that is the best-implemented thing in it. It is also the clearest specimen this run has found of a single mechanism: **a discipline travels freely wherever it is free and stops wherever the safe choice would cost something.** The asset ACL refuses team admins, was *changed* to a safe default in July, and closes the agent-binding side door as well. The gateway that stores those assets ships with authentication **off**, because the proxy cannot send the header — and they wrote that down, in the file the README tells you to edit, including the words *"for production this must be fixed on the proxy side first."* Same organisation, same release, both reasoned, both documented, opposite outcomes.

---

## What to believe

| Claim | Status |
|---|---|
| `private` assets are unreadable by team admins | ✅ **TRUE** — enforced by ordering; `canBindAsset` closes the agent door too |
| "No plugin, hook, or MCP server required" | ✅ **TRUE** — and §7 of the Deep Dive explains the trick |
| L2/L3 injected, L0/L1 fetched on demand | ✅ TRUE, in code |
| Claude prompt-caching survives the proxy | ✅ TRUE — `cache_control` preserved deliberately |
| Telemetry off by default, no phone-home | ✅ TRUE — `clickhouse.enabled: false`, placeholder endpoint |
| SDK defaults to Tencent's cloud | ❌ **FALSE** — docstring examples only; `endpoint` is required |
| README's clone URL is broken | ❌ **FALSE** — it redirects and works |
| **PersonaMem 48% → 76% (+59%)** | 🔴 **Do not cite** — 2 files, both READMEs; no harness, no model, no config |
| "Current release is v2.0.0" | ⚠️ Four surfaces, four answers; the npm manifest is the *oldest* |
| 7 agents supported equally | ⚠️ 5 have adapters; the other 2 use the generic path *by design* |

---

## The four findings that matter

1. 🔴 **A merged security fix is reverted on the shipped branch, and its test is gone.** Contributor PR #175 turned on `looksLikePromptInjection`; the default branch has it commented out, `sanitize.test.ts` deleted, the detector exported with **zero callers**, and the live call-site comment still promising the filter. The threat is this product's central loop: captured text → LLM extraction → persisted → **re-injected into the system prompt** of every future session and agent.
2. 🔴 **Auth is off in the documented install** — `MEMORY_CORE_GATEWAY_API_KEY=` is empty, `""` coerces to `undefined`, the gate returns `"ok"`, and the port is published on all interfaces. Their own escalating warning describes it exactly, naming `/capture`, `/search/conversations`, `/recall`, `/seed` — into a docker log.
3. ⚠️ **A CI guard that prints `PASS` on the file it exists to protect** — proven by running it. Plus: CI fires only on `main`, which is not the default branch and has no `MemoryCore/`; and there is no test job at all behind four vitest configs and five test scripts with zero tests.
4. ⚠️ **97 citations to 26 design documents in a directory that has never existed** — including the credential plan, the multinode audit's `P0-2`, and the ADR named in the CI guard's own failure message.

---

## The three things worth stealing

1. ⭐⭐⭐ **Extend an agent you cannot modify by appending a curl recipe to its system prompt.** No MCP, no plugin, no client change — the proxy injects the credentials on the way out, so the recipe holds no secrets. Their prompt even has to *forbid* the model from replying *"I'd need an MCP server for that."*
2. ⭐⭐⭐ **Choose defaults by asymmetric harm, and write the reasoning in the code.** `credit-reporter.ts:37-44` picks the fallback that under-charges rather than over-charges, and says why. In the billing path.
3. ⭐⭐ **Enforce a privacy rule by ordering, then enumerate its blast radius in-comment, then close the second door.** `permission-checker.ts` + `canBindAsset` is a small masterclass — and directly applicable to hireui's candidate-data ACL.

---

## Pilot posture

**READ-AND-BORROW. Do not run it against anything real, and never against candidate data.**

If you do stand it up to look at it: **bind loopback only** (`-p 127.0.0.1:PORT:8420`), set `MEMORY_CORE_GATEWAY_API_KEY` and accept that the proxy path breaks, treat every captured conversation as permanently readable by anyone on the network otherwise, and assume the prompt-injection filter is off because **it is**.

🔴 **NEVER:** point it at a repo or conversation containing candidate PII · expose the memory-core port beyond loopback · cite the PersonaMem number · assume a memory that came back is a memory that was filtered · trust that memory is working (its failure mode is silence).

---

## Blunt

**This is the most instructive repository of the run, and it is instructive for a reason its authors would not choose.** Almost everything here is competent — a 2,129-line Anthropic handler that preserves your prompt-cache breakpoints, a classifier that tells a Claude Code fork from a main turn by marker position, telemetry that is architecturally forbidden from throwing, an ACL that refuses admins by construction and explains its own blast radius, a billing default chosen by reasoning about which way the error hurts less. These are not the artifacts of a careless team.

And then: a contributor's merged prompt-injection fix is off again on the published branch with its regression test deleted; the only CI guard passes on the exact file it guards, which I proved by changing that file and running it; four test harnesses sit over zero tests; 97 pointers lead to a directory that was never published; and the gateway holding every conversation your agents have had ships unauthenticated because the other half of the same product cannot authenticate to it.

Every one of those is the same defect, and it is not negligence. **It is what happens when a practice has to cross a boundary and nothing carries it.** v258 found that code moves forward in time and never backward. v262 found it does not transfer by proximity. v264 found it does not transfer between two directories of one repository. v265 finds it does not transfer across a branch re-root, across an internal-to-public export, or across the gap between a code default and the installer that overrides it — and, in the one case where we can read the reason aloud, it did not transfer because **the safe version cost something and the unsafe version did not.**

So take the curl-recipe trick, take the asymmetric-default habit, take the ACL. Then go and ask the question this repository answers by accident: **which of my safe defaults were free — and what did I quietly not do when one wasn't?**
