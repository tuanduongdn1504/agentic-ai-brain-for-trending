# (C) NeMo Agent Toolkit — Pilot Methods Menu (v264)

**Verdict: ⭐ READ-AND-BORROW, with ONE genuinely tempting install.**

Apache-2.0 with **no restrictive licence in its own code** (verified across all tracked files), so unlike v188/v214/v243/v245/v247 the licence is not the reason to hold back. The reasons to be selective are **footprint** (34 packages, 321,288 lines, an NVIDIA-first default path) and **prerequisites** (a Rust toolchain for NeMo Relay, `git-lfs` for any example data).

---

## Rung 0 — 30 minutes, read only, highest value per minute

Read these five things in this order. Clone nothing, install nothing.

1. **`packages/nvidia_nat_core/src/nat/utils/telemetry/consent.py`** — the whole file. Read the module docstring first (`:17-31`), then `read_persisted_consent` (`:102-165`), then `render_prompt` (`:216-244`). **This is the best-argued 310 lines in the corpus.**
2. **`examples/experimental/claude_code_agent_adapter/configs/config-relay.yml`** — eleven lines, four safety decisions. Then `register.py:61,67,73` for how the defaults differ from the example.
3. **`register.py:130-132`** — `_usage_for`. Look at what the field is called and what it contains.
4. **`ci/scripts/documentation_checks.sh:19-21`** — the exclusion and its stated reason.
5. **`packages/nvidia_nat_core/src/nat/runtime/loader.py:138`** and the ten lines under it. Then ask what the comment refers to.

Then run one command against your own repositories:

```bash
grep -rn "backwards compatib\|for compatibility\|kept for\|legacy" --include="*.py" --include="*.ts" . | head -40
```

**Every hit is a claim about code that may no longer exist.** That is the `loader.py:138` class of defect, and no linter checks it.

---

## ⭐⭐⭐ Rung 1 — 30 minutes — the asymmetric consent rule, into the ratified ADR

**This is the highest-value item on the whole list and it touches a standing policy.**

The ratified candidate-LLM legibility ADR says every hireui LLM path touching a candidate must be fixed, legible, audited, human-in-the-loop and eval-gated. **It has a version. It has nothing that invalidates a stale consent.** `consent.py` shows the exact shape:

- Stamp every consent/disclosure record with a **`disclosure_version`**.
- On a version mismatch: a stored **refusal stands** (never silently re-enable); a stored **agreement expires** and must be re-obtained.
- Write the reason in the code, beside the branch, the way `:121-125` does.
- Keep the disclosure text **inline in the code** so a change to what a candidate is told appears in a PR diff and can be asserted by a test.

Under **Art. 50(4)** — deployer duties, which are yours, not the vendor's — that is not a nicety. It is the difference between "we told them" and "we can show what we told them and when."

**Deliverable:** a paragraph in the ADR and one test that fails when the disclosure string changes without the version bumping.

---

## ⭐⭐ Rung 2 — 45 minutes — the split rule for `hireui/evals/METHOD.md`

`METHOD.md` already carries the v249/v252 ground-truth contamination gate. **v264 adds the case those miss:** the optimizer. `nat optimize` runs a genetic algorithm over prompts, scored by `nat eval` on **one dataset**, with guidance that says *"never shrink the dataset"* and no mention of generalization anywhere in 1,377 lines — in a repository whose fine-tuning docs ship `--validation_dataset` and warn about overfitting five times.

**Write down one rule:**

> **A held-out split is a precondition of the optimizer, not a property of the harness.** Any process that *selects* a prompt, threshold, or config by score must be scored on data it did not select against. If there is no split, there is no optimizer — there is a fitting procedure.

Then add the counter-example, because the corpus already holds it: **v178 SkillOpt** is a text-space optimizer for agent-skill documents whose defining feature is **held-out validation gates that reject non-improving edits**. Same problem, opposite discipline, and it is the model to copy.

---

## ⭐⭐ Rung 3 — 45 minutes — the vault's own exemption audit

`(C) proposed-verify-vault-inventory.sh` has nine clauses and reports 0 FAIL. **v263's Rung 1 was "wire it to a git hook"; v264's is a different and prior question.**

`documentation_checks.sh` proves the point: they wrote down where they were *not* aiming the linter, gave a defensible reason, and the drift appeared in the gap. So:

1. **List every exemption in your own checks** — every `grep -v`, every path excluded, every clause that warns instead of failing.
2. For each, write the justification next to it. If you cannot write one, it is not an exemption, it is an omission.
3. **Then look for drift inside each exemption**, because that is where it is.

The vault's known exemptions to start with: **`05 Skills/`** (nine copied, re-versioned routine files that no clause compares to each other) and the **`_state/03c-projects-v61-v183.md` filename**, declared stale at v245 and still stale. ⭐ **The `05 Skills/` one is the same shape as this subject's finding, one level up** — and v259 left it as an open operator decision.

---

## The tempting install — and how to fence it

⭐ **The Claude Code adapter is the first thing in ~40 ships I would actually consider running**, because it does something nothing else offers: **traces and scores Claude Code's own runs.** If you take it:

**Prerequisites, all real:**
- Python 3.11–3.13, `pip install nvidia-nat`, plus `uv pip install -e examples/experimental/claude_code_agent_adapter`
- **A Rust toolchain.** NeMo Relay is a separate public repo (`NVIDIA/NeMo-Relay`, Apache-2.0, Rust) installed by `cargo install --path crates/cli`. ⚠️ The README's clone command uses **SSH** (`git@github.com:`) — **use HTTPS instead** unless you have a GitHub SSH key.
- **`git-lfs`**, or every example's `data/` directory is a 130-byte pointer. 117 files in this repo are LFS objects.
- Docker, for `arizephoenix/phoenix` if you want the trace UI.

**The fence:**
- ✅ **Keep the shipped config's four safety settings.** `permission_mode: plan`, all five mutating tools denied, `setting_sources: [project]`, and **set `max_budget_usd` yourself — the code default is `None`, i.e. uncapped.**
- ✅ Run it in a **scratch repository first**, never in `hireui` or the vault, until you have seen one full trace.
- ✅ Run `nat configure telemetry --status` **before** anything else, and `--disable` if you want it off. Then verify with `NAT_TELEMETRY_ENDPOINT=stdout` that nothing you object to is in the payload — the code documents this specifically so you can look.
- 🔴 **Do not trust `ChatResponse.usage`.** Its token counts are word counts (`register.py:130-132`). Read tokens from the **Phoenix trace** or from `nat eval`'s `avg_tokens_per_llm_end`, which come from the Relay bridge and are real.
- 🔴 **Do not expose the MCP server** in this pilot. It has **no approval gate and no read-only mode** — the only control is the startup `tool_names` allow-list.

**What you would learn:** whether a real trace of Claude Code's tool calls and token usage, in Phoenix, changes how you spend on it. That is a question your own infrastructure has been asking for several ships.

---

## 🔴 NEVER

- **Do not put the MCP server in front of candidate data.** No approval gate, no read-only mode, extent verified across both MCP packages. `nat/middleware/hitl/` exists in core and the MCP path does not use it; until you wire that yourself, this surface is unfenced.
- **Do not use `nat optimize` to tune anything a candidate could be told about or could contest** — no held-out split, no warning, and a GA that will happily fit your eval set.
- **Do not run the LangChain ReAct path with Claude and expect reasoning to survive.** `plugins/langchain/agent/base.py:48-57` *"ignores non-text blocks such as tool-use or reasoning."*
- **Do not cite its star/fork counts.** Page-stated only; the GitHub API is mocked here.
- **Do not treat 6,294 tests as evidence that the parts you care about work.** The five coding-agent adapters have **zero** tests; the 131 integration tests do not run in GitHub CI.
- **Do not assume the framework adapters are peers.** LangChain is 10,464 non-test lines; CrewAI is 476.
- **Do not read the GitHub releases page for dates.** It returns 2024 for 2026.

---

## One-line summary

**Read `consent.py` and steal its versioned asymmetry today; borrow the split rule and the exemption audit this week; and if you install one thing from 264 subjects, install the Claude Code adapter in a scratch repo with the budget cap set by hand — then ignore the number it hands you and read the trace.**
