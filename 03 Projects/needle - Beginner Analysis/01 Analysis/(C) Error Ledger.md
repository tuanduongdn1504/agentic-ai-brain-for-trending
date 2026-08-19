# (C) Needle 2 — Error Ledger (v246)

Errors caught during this ship, who made them, and how they were caught. The vault's convention: record
**my own** errors as prominently as the agents'.

---

## MINE — 3

### E1 · Truncated month histogram read as a fact (counting-method)
**The error.** The first `git log --format="%cd" | sort | uniq -c` run printed a total of **50** commits
against a `rev-list` count of **268**, and I nearly wrote up the gap as a repository finding
(orphaned refs, a graft, a rewrite).
**The truth.** The pipeline's stdout was truncated by **the vault's own known zsh stdout-drop defect**.
Re-run routed to a file: 17 + 167 + 34 + 16 + 2 + 32 = **268**. No repository anomaly at all.
**Caught by:** noticing the sum did not reconcile with `rev-list` and re-running to a file.
**Rule it violated:** the vault's own standing workaround — *route long output to a file and `cat` it.*
This is the second consecutive ship where that defect nearly produced a phantom finding.

### E2 · A filtered grep reported as a total (counting-method)
**The error.** I ran `grep -rn -i "silent" --include="*.py" .`, got **three** hits, and wrote the
"silent-failure doctrine" finding as *"exactly three hits, and all three are the same idea."*
**The truth.** The correct scope returns **four**. The fourth (`doc/finetuning.md:19`, *"longer examples
are silently truncated"*) is a **counter-example** — a silent data-loss path that is documented rather
than made loud. It inverts the finding's shape from "a total doctrine" to "a doctrine with an admitted
exception," which is both more accurate and more interesting.
**Caught by:** re-running without the `--include` filter while verifying citations.
**Rule it violated:** **D26/D27 family** — *a filtered grep is a claim about the filter.* State the
population, then count. The vault has carried this rule since v243 and I made the error anyway.

### E3 · Fed a stale premise to the fleet
**The error.** The workflow brief told all fourteen agents that Library-vocab **#12** was a v77 candidate
named *"AI-Optimized Tutorial Index via llms.txt"*, and asked whether Needle's `llms.txt` would be a
genuine **N=2**.
**The truth.** That wording is from the **CLAUDE.md shim's v77 narrative**. The **registry**
(`_patterns/06-library-vocab-registry.md:14`) shows #12 was long since generalised to
**"LLM-routing artifacts," CONFIRMED at N=5+ (v75→v168)**. There was no N=2 question to answer; Needle's
`llms.txt` is straightforward instance-strengthening of a confirmed family.
**Caught by:** hand-grepping the registry rather than accepting the agent's answer.
**Rule it violated:** **v241 D21** — *a verifier checks the claim you hand it, not the question.* A
mis-framed premise propagates silently through an entire fleet.
⭐ **And it is itself a vault-drift data point:** the shim's narrative disagrees with the registry, in
exactly the shim the v239→v245 chain has been diagnosing.

### E4 · Computed the context window from dataclass defaults, not the shipped preset
**The error.** I computed the effective KV window as **1,472 tokens** using `TransformerConfig`'s
dataclass defaults (`d_model=512, num_layers=12`) and put that number in three documents.
**The truth.** `architecture.py:38-43` defines named **`PRESETS`**, and the defaults match **neither**:
both presets use **27 layers**, not 12. Correct figures — **`needle` preset: 480 tokens**;
`base` preset: 704.
**Caught by:** the workflow's architecture mapper, which read `PRESETS` and flagged that the parameter
count did not reconcile either. **The fleet corrected the orchestrator.**
**Why it mattered:** 1,472 vs 480 is the difference between "tight but workable for a CV section" and
"a CV section does not fit." It changed the pilot verdict, not just a number.
**Rule it violated:** the same family as E1 and E2 — **I took a default for the configuration.** Three
counting/scoping errors in one ship, all of the form *"the number I measured is not the number I claimed
to measure."*

---

## AGENTS' — 2 rejected, 1 accepted-with-correction, 1 correction ACCEPTED

### A1 · "WORLD-FIRST at 45M parameters" — **REJECTED**
The prior-art agent concluded: *"Needle 2 is **WORLD-FIRST at 45M parameters** for a tool-calling-
specialized model. No smaller competing model found in the literature."*

**Rejected on three grounds:**
1. **It is an absence-of-evidence argument.** "No smaller model found in my search" is not "no smaller
   model exists," and the vault's standing instruction is to err toward *not* world-first.
2. **It is falsified inside the same product line.** `cactus-compute/cactus` — the same organisation's
   own current repo — describes **Needle as a 26m parameter model**. A 45M model cannot be the smallest
   when its own vendor documents a 26M one.
3. **It confuses a number with a class.** Being the smallest known instance of an existing class is a
   corpus-knowledge data-point, not a novel capability — the **PixelRAG v211** discipline
   (*corpus-first-for-a-technique ≠ a mintable §C class*).

**What survives:** Needle sits roughly **5–6× below** the smallest widely-cited peer (FunctionGemma 270M,
LFM2.5 230M). *Distinctive for scale* is supportable. *World-first* is not, and the wiki says so.

### A2 · Verdict inflation on the adversarial stage — **partially discounted**
The Verify phase returned **7 CONFIRMED / 1 PARTIAL** against a brief that explicitly said *"your default
answer is REFUTED; try to kill this claim."* A stage that confirms ~88% of the claims handed to it is not
functioning adversarially — it is grading its own orchestrator's hypotheses.

**Handling:** the two claims that mattered most were **re-verified by hand** and both came back *narrower*
than the fleet's CONFIRMED:
- *"the engine is not open"* → **corrected**: the engine source **is** public
  (`cactus-compute/cactus`, 5.9k★) — but under a custom **$2M-capped** licence, and the fetched artifact
  is a prebuilt binary from a repo declaring apache-2.0, with **no document reconciling them**. The
  narrower claim is the true one and it is the better finding.
- *"no hash pinning / no signature verification"* → **confirmed but softened**: the engine **is**
  version-pinned (`ENGINE_VERSION = "2.0.2"`) and fetched over HTTPS via `huggingface_hub`. The correct
  characterisation is *"pinned-but-unverified over TLS,"* which is a materially weaker finding than the
  plaintext-`http://` MITM class of **v234**.

### A3 · Accepted-with-correction: the collision check
The vault-collision agent's core findings — **zero** prior corpus mentions of cactus-compute / Needle /
Henry Ndubuaku / Cactus Quants, and the model-tier discipline applying strictly — **matched independent
hand-grep exactly**. Accepted. Its answer to the `llms.txt` question was discarded because the *question*
was wrong (see **E3**), not because the agent erred.

---

## Method note

**Four of the six substantive findings came from the orchestrator's own hand-checks** — the licence split,
the release-gate skip, the training-provenance-in-a-topic-tag finding, and the `silent` doctrine. The
fleet's most valuable contributions were the **negative** and the **corrective** ones: a clean collision
check that matched independent hand-grep exactly, a map of the competitive band, and — decisively —
**the `PRESETS` discovery that overturned the orchestrator's context-window number and with it the pilot
verdict (E4)**.

**That last one is the case for the fan-out in one line.** The adversarial *verification* stage was
close to useless here — 7 CONFIRMED out of 8 against a brief that demanded refutation is a rubber stamp.
The *mapping* stage, which was asked to read files and report what was in them, is what caught the
orchestrator's mistake. **Agents asked to check a claim tend to confirm it; agents asked to read the
code find what the claim got wrong.**

**And the standing lesson repeats:** three of my four errors (E1, E2, E4) were the same shape —
*the number I measured was not the number I claimed to measure* — a truncated pipeline, a filtered grep,
and a default mistaken for a configuration. The vault has carried D26/D27 for exactly this family since
v243. **Carrying a rule is not the same as applying it**, which is itself the finding of the last three
ships.
