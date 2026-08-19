# (C) Needle 2 — Phase 0.9 Verdict + Mint Decision

**Ship:** v246 · **Date:** 2026-08-19 · **Subject:** `cactus-compute/needle` (Needle 2)
**Routine:** LLM Wiki Routine v2.7

---

## 1. Phase 0.9 four-criterion call

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** Anthropic affiliation / registered vendor-direct source | **FAIL** | Cactus Compute, Inc. — a corporate author, **not** Anthropic. Per **§41**, (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source; no name/heritage/notability inference is permitted. The disclosed-individual axis is answered NO. Anton Osika's single README typo commit is **not** an (a) signal. |
| **(b)** Goal relevance | **MODERATE** — keys the tier | Argued below. |
| **(c)** Source quality / studiability | **STRONG** | Apache-2.0, source-cloned twice, 44 files / 10,824 lines fully readable, 45 tests, a real CI workflow, three substantive docs, a companion arXiv paper with a matching author list. ⚠️ Tempered by the fact that the **inference engine is a binary** — the most interesting mechanisms (tool retrieval, byte-level grammar, confidence) are **not** in the tree. |
| **(d)** Actionability | **STRONG** | Multiple zero-install takeaways (the `silent` doctrine, the escalation-ladder shape, the `llms.txt` form, the "facts not instructions" boundary) plus a genuinely low-risk `pip` pilot path. |

### ⇒ **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG

Under **§40** (operator-direction GA-default for goal-adjacent subjects), an operator-requested
goal-adjacent subject defaults to GOAL-ALIGNED at (b) MODERATE+, with the OFF-GOAL reading recorded as
the reviewable alternative. This ship was operator-requested. **No override consumed; no §35 pressure.**

### The (b) argument, both ways

**FOR MODERATE (the call):** Needle 2 is agent substrate. It is a *tool-calling* model — the exact
primitive Goal #1 is about — and it ships an agent loop (`run()`), a tool-schema compiler, a refusal
contract, and a confidence gate. Its **in-model tool-retrieval head** speaks directly to the vault's own
live, unresolved ~54K tool-catalog problem (v167 → v238 → v245). Its `llms.txt` is a first-class
agent-facing artifact.

**FOR FAIL (the recorded alternative):** it is not a coding agent, it cannot write code, it will never
run a harness, and the operator will not deploy a 45M model in hireui. Its native domain is phones,
wearables and smart-home devices — three surfaces the operator does not build for. Under the strict
reading this is an **OFF-GOAL CAPTURE** rescued by §40.

**⚠️ Recorded as operator-reviewable.** The MODERATE call is consistent with the five prior
model-tier ships (GLM-5 v176, DeepSpec v186, TimesFM v193, PixelRAG v211 — all MODERATE per operator
direction, all with the OFF-GOAL reading defensible).

---

## 2. Mint decision: **NO MINT**

The §C standalone candidate would be something like *"Sub-100M On-Device Tool-Calling Foundation Model
Shipped as an Agent-Callable Library with Constrained Decoding."*

**It is DECLINED on five independent grounds**, three of which are the vault's own explicit, repeated,
written discipline. ⚠️ Each was verified by hand-grep, not taken from an agent.

### Ground 1 — the model-tier discipline binds, and this is its **fifth** data point

`_patterns/06-library-vocab-registry.md:171` (v176 GLM-5), verbatim:

> *"**NO §C standalone minted** — a single goal-adjacent frontier model is not a recurring capability
> class; §C vocab is **tool/capability-shaped** and competitor models have only a [single instance]"*

`_patterns/06-library-vocab-registry.md:199` (v193 TimesFM): a *"corpus-first time-series-forecasting FM"*
§C mint was **DECLINED** on exactly this reasoning, despite being the corpus's first forecasting FM.

The descriptive **Model/Inference-Substrate tier** — GLM-5 v176 · DeepSpec v186 · TimesFM v193 ·
PixelRAG v211 — **becomes N=5 with Needle v246** (bookkeeping only; counts unchanged). Four consecutive
prior rulings declined a mint for a model. **A model is not a capability class.** That binds here.

### Ground 2 — NOT world-first, and the band is crowded

Tiny/on-device function-calling models with constrained decoding are an established and contested class:
**FunctionGemma 270M** (Google), **LFM2 / LFM2.5** (Liquid AI), **Apple Foundation Models** on-device,
**Octopus v2** (NexaAI), plus the Gorilla / ToolLLM / xLAM / Hammer research line. Needle's own README
names three of these as peers. Grammar-constrained decoding is standard practice (llama.cpp GBNF,
Outlines, XGrammar, Guidance, JSON mode).

**What IS distinctive is scale, and scale is a number, not a class.** At 45M (Needle 2) / 26M (Needle 1)
it sits roughly **6–10× below** the smallest widely-cited peer, and one secondary source calls 270M *"the
smallest credible function-calling model of 2026."* Being the smallest instance of an existing class is a
**corpus-knowledge data-point**, not a mint — the **PixelRAG v211** discipline exactly
(*corpus-first-for-a-technique ≠ a mintable §C class*).

### Ground 3 — domain-not-capability

The native domain is **phones, wearables, smart home and robots** (the repo's own tagline). That is a
DOMAIN. The **meetily v196** and **AIRI v210** discipline applies: a corpus-first DOMAIN is a data-point,
not a §C mint.

### Ground 4 — §28 anti-inflation

The §C surface is ≈58 with 51 live standalones. §28 caps new standalones at ≤2 per wiki and requires
clustering-first. There is no cluster this joins and no N=2 partner in the corpus.

### Ground 5 — the distinctive machinery is **not in the subject**

The three things that would justify a capability mint — the learned **tool-retrieval head**, the
**byte-level grammar**, the **calibrated confidence head at inference** — are all inside a binary that
is not in this repository (`needle/__init__.py:38-48` binds exactly four C symbols). The vault would be
minting a class on the strength of prose describing code it has not read. **v242's D25 is the governing
rule: an un-cloned subject's caveats are hearsay** — and here the load-bearing component is, in effect,
un-cloned.

### ⇒ NO MINT. Counts **46 / 11 UNCHANGED**. §C live standalones **51 unchanged**. Surface **≈58 unchanged**.

The §C mint is **RECORDED as the operator/audit-reviewable alternative**, as the routine requires.

---

## 3. What Needle 2 *does* strengthen (recorded, not self-executed)

Per the **v232 rule — a promotion is an audit act** — these are recorded for the overdue audit and are
**not** self-incremented here.

| Item | Effect | Verified |
|---|---|---|
| **Library-vocab #12 "LLM-routing artifacts"** (CONFIRMED, N=5+) | `llms.txt` is a **clean instance-strengthening**, and an unusually strong one — see §4 | `_patterns/06:14` — hand-grepped |
| **Model/Inference-Substrate tier** | descriptive **N=4 → N=5** (bookkeeping only) | `_patterns/06:171,187,199` |
| **Pattern #83 Honest-Deficiency-Disclosure** | **two** instances, one of them exceptionally strong (§5) | `__init__.py:57`, `finetune.py:401`, `doc/finetuning.md:64` |
| **Pattern #66 supply-chain** | a **mixed** data-point: version-pinned engine, unpinned Python deps, OIDC trusted publishing, no hash verification | `fetch.py:8,88`, `pyproject.toml:7-15`, `release.yaml` |
| **The tool-catalog thread** (v167 ~54K floor → v238 → v245) | Needle is the **first instance in the corpus of the problem being solved at the MODEL layer** rather than the harness layer | §4 below |

> 🔴 **A stale-premise correction, recorded.** The workflow brief for this ship told its agents that
> Library-vocab **#12** was a v77 candidate named *"AI-Optimized Tutorial Index via llms.txt"* — that is
> the wording in the **CLAUDE.md shim's v77 narrative**. The **registry** (`_patterns/06:14`) shows #12
> was long since generalised to **"LLM-routing artifacts," CONFIRMED at N=5+ (v75→v168)**. The shim's
> narrative is stale relative to the registry.
> This is **v241's D21 live** — *a verifier checks the claim you hand it, not the question* — and it was
> caught only because the orchestrator re-grepped the registry instead of accepting the agent's answer
> to a mis-framed question. **It is also one more instance of the vault's own documentation drift**, in
> the same shim that the v239→v245 chain has been diagnosing.

---

## 4. The one genuinely new thing for the corpus

Every prior corpus treatment of tool-schema bloat has been at the **harness** layer:

- **v167 audit** — the vault's own **~54K tool-catalog floor**, named as a standing constraint.
- **v238 dsh-anchored-standard** — a preset that **blanks auto-injections** to constrain request #1;
  the vault noted Anthropic ships the mechanism first-party as `defer_loading` (77K → 8.7K).
- **v245 Unsloth** — **measured** it (*"~28k tokens of which ~18k is System tools"* via `claude -p /context`)
  and identified `--tools` as the flag that restricts schemas.

**Needle 2 is the first subject in the corpus that moves the problem into the model.** Its retrieval head
is trained to select the top-5 tools from a large declared catalogue per turn, and the decode grammar is
then constrained to that subset — so the catalogue never has to fit in the prompt at all.

**⇒ The thread reaches N=4 and, for the first time, spans two layers**: three harness-layer instances
(prompt engineering, a first-party API flag, a measurement) and one model-layer instance (a learned
retriever inside the weights).

⚠️ **The honest limit:** the retrieval head is in the binary. The vault has **verified the claim exists in
the documentation, not that it works.** No benchmark, eval harness, or reproduction script ships in this
repo — see the Verified Facts Ledger §9.

---

## 5. The strongest single finding

Not the model. **The engineering doctrine, which is greppable in one command:**

```bash
grep -rn -i "silent" .
```

Four hits. Three convert a would-be silent wrong answer into a loud failure with a stated remedy
(`__init__.py:75`, `export.py:30`, `export.py:551`). The fourth (`doc/finetuning.md:19`) admits a silent
truncation and only documents it — which is what keeps the finding honest rather than hagiographic.

**And the tension that makes it a wiki finding rather than a compliment:** this is the most
silent-failure-conscious codebase the corpus has read, and **its own daily automated PyPI release is
gated on a test suite in which every engine-touching test is skipped or deselected — and `pytest`
reports skips as success.** The doctrine is applied rigorously to the user's failure modes and not at
all to the project's own release gate.

---

## 6. Streak and ceiling

- **Streak:** v245 `GA:103` → **`GA:104 · OG:13 [7 ov]`** — **27 consecutive GA ships**, v220→v246.
- **§35:** window {v244 GA, v245 GA, v246 GA} = **0 OG → CLEAR.**
- **Overrides:** none consumed. Lifetime **10**; v153→v246 = **zero**.
- ⚠️ The **~v221 audit remains egregiously overdue** (last audit v212; v213–v246 all shipped).
