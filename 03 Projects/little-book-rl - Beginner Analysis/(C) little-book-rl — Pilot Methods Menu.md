# (C) little-book-rl — Pilot Methods Menu

> LLM-Wiki **v220** · 2026-07-18 · `alxndrTL/little-book-rl` — *The Little Book of Reinforcement Learning*.
>
> ⚠️ **Blunt honest framing:** this is a **learning resource, not a tool.** There is **nothing to install-and-use as software**, **no hireui pilot** (recruitment is not an RL problem; there is no Goal-#2 artifact here), and **no product**. The value is **on-goal *reading* for Goal #1** — the classical RL ladder (MC→PPO) is the foundation of the RLHF / GRPO / agentic-RL that trains Claude and coding agents. So this menu is honestly short (~12 methods, mostly **read → borrow-by-hand → optional scratch-run → fence**), *not* padded to 24. **⭐ One-thing path: A1 → A2 → B5.**

## A — Read & learn (the core of the value; zero risk, zero install)

- **⭐ A1 — Read the book as a fast, code-anchored RL refresher.** The free CC PDF (`book.pdf`, ~157 pages, MC→PPO, code-first). It is deliberately short — the "fastest way back into RL for an engineer who did it once and forgot most of it." ~an afternoon. Zero risk (free reading).
- **⭐ A2 — Map the ladder onto the modern RL-for-LLMs stack (the on-goal payoff).** As you read, keep a running margin note: **PPO → the RL step in RLHF**; **actor-critic + advantage estimation (GAE) → GRPO / RLVR / agentic-RL** (the paradigms that train reasoning models + coding agents). After A1 you can read a GRPO / agentic-RL paper or thread with the foundation in hand — which is the whole reason a classical-RL book is on-goal.
- **A3 — Work the `supplementary/` DP proofs.** The one place the book goes rigorous (policy/value-iteration convergence). Read if you want the *why* behind the algorithms, skip if you only want the *what*.
- **A4 — Use it as an RL glossary / index, not a course.** Because it's opinionated and short, its best long-run use is a quick lookup ("what exactly is the PPO clip doing?") — Sutton & Barto remains the reference textbook; this is the fast on-ramp.

## B — Borrow by hand into the vault / your notes (zero install, highest durable ROI)

- **⭐ B5 — Distil a one-page "RL foundations for agent-training" cheat-sheet into the vault's `05 Skills/` or notes.** The MC→TD→policy-gradient→actor-critic→PPO ladder + the one-line bridge to RLHF/GRPO/agentic-RL. This is the **borrow-by-hand shape used for LLMs-from-scratch v74 / AI-For-Beginners v191 / mlsysbook v197** — the reading compounds when it becomes a durable reference. Zero install.
- **B6 — Add "PPO ≠ novel; PPO = RLHF's RL step; GRPO = its LLM-era variant" to your mental model** so the corpus's RL-component subjects (fish-speech v20 GRPO, LlamaFactory v22 / Unsloth v23 RL methods #43, DeepSpec v186, hello-agents v111 agentic-RL) all connect to one foundation rather than being isolated jargon.

## C — Optional scratch-run of the code (learning aid; small install fence)

- **C7 — Run one `algos/` implementation on a toy environment** to build intuition (e.g. Q-learning or PPO on a gridworld / a `gymnasium` classic-control env). It's a *learning aid*, not a pilot — you're building RL muscle memory, not shipping anything.
- **C8 — Compare the book's PPO impl against a reference** (Spinning Up's / CleanRL's) to see the same algorithm two ways. Best done only if you're actively studying policy optimization.
- **Fence for C7/C8:** ⚠️ **NOT source-cloned** by this wiki → `install-snapshot` before a `pip install` + a **scratch venv** (the code needs PyTorch + likely `gymnasium`/an env; check `algos/` requirements first) + throwaway dir. No supply-chain surface beyond the standard PyTorch stack, but treat unread third-party code as untrusted.

## D — hireui / Goal #2

- **None applicable.** Classical RL has no direct hireui feature (recruitment is a matching/ranking/LLM problem, not a sequential-decision RL problem). No pilot, no artifact. If a future hireui feature ever needed bandits/RL (e.g. exploration in ranking), the foundation from A1 would help — but that's speculative, not a pilot.

## F — Vault-meta / audit follow-ups

- **F9 — File the T3 "book + companion code" sub-archetype data-point** for the ~v221 audit: little-book-rl ≈ the **LLMs-from-scratch v74 sub-shape** (individual ML educator's short book + PyTorch companion + paid print) → the retired-but-re-registerable T3 sub-archetype candidate now has v74 + v220 as instances (recorded, not self-registered).
- **F10 — File the Pattern #83 83f.3 license-inconsistency cross-ref** (this ship + hello-agents v111 = 2 instances of "stated non-commercial vs cited license that isn't"; recorded not self-incremented).
- **F11 — Note the "corpus's first RL DOMAIN" data-point + the declined §C mint** (domain-not-capability + not-world-first) so the ~v221 audit sees the reasoning; **no watch axis carried** (saturated genre, the v217/v219 restraint).
- **F12 — Candidate future subject: `mamba.py`** (Alexandre's notable pure-PyTorch/MLX Mamba impl in 🤗 Transformers) — a *tool/architecture* subject, unlike this *book* subject; queue if an architecture-internals ship is ever wanted (non-corpus today).

## Fence summary

- **A/B are free + zero-risk** (reading + borrow-by-hand). This is where ~all the value is.
- **C** = optional scratch-run only: `install-snapshot` + scratch venv + read `algos/` deps before installing (NOT source-cloned → treat as untrusted).
- **Reuse:** the content is CC and the author states **non-commercial** intent — treat it as non-commercial despite the cited "BY-SA" (the 83f.3 ambiguity); don't republish/resell.
- **No hireui code, no product, no metered LLM spend.**
