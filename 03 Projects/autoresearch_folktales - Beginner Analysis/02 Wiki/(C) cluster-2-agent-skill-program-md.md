# (C) Cluster 2 — Agent skill (`program.md` verbatim Karpathy instructions)

**Source:** `program.md` on branch `autoresearch/apr10`; fetched 2026-05-20 via WebFetch of github.com.

**Critical observation**: `program.md` appears **byte-identical or near-byte-identical to Karpathy's original `autoresearch/program.md`**. Thu Vu has FORKED the agent-skill verbatim and adapted only `train.py` + dependencies for MPS support. The skill itself is preserved as-is — this is Pattern #57 evidence at the maximum-faithful-preservation depth (methodology is treated as immutable inheritance).

## 15-section format

### 1. Cluster scope

The contributor-facing surface = `program.md` (the autonomous-agent skill / instruction document). This is **THE artifact** of autoresearch as a framework — it's what differentiates the project from a generic LLM training script. The skill defines: setup protocol + experimentation protocol + output format + logging protocol + experiment-loop protocol.

### 2. Positioning of program.md

**Internal positioning** (from program.md verbatim):
> *"This is an experiment to have the LLM do its own research."*

**Function**: defines a complete agentic-research-framework instruction set for autonomous AI agents (Claude Code, Mistral Vibe, etc.) to:
1. Set up a fresh experiment branch
2. Run iterative experiments on a fixed compute budget
3. Decide commit/discard/keep based on a single metric
4. Log results in TSV
5. Continue indefinitely until interrupted

**Corpus-first signal**: program.md is **CORPUS-FIRST `.md` agent-skill format that uses git-state-tracking + branch-naming-discipline as the agent's primary state-management mechanism** in v60+ window.

### 3. Verbatim structural sections of program.md

1. **Setup** (6-step initialization protocol)
2. **Experimentation** (CAN-do/CANNOT-do allowlist)
3. **Output format** (verbatim sample of summary block)
4. **Logging results** (TSV column schema + format)
5. **The experiment loop** (9-step looping protocol)
6. **Timeout** (5-min budget + 10-min auto-fail threshold)
7. **Crashes** (use-judgment fallback)
8. **NEVER STOP** (explicit autonomy escalation)

### 4. Setup protocol (6-step, verbatim ordering)

> 1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
> 2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
> 3. **Read the in-scope files**: The repo is small. Read these files for full context: README.md, prepare.py, train.py.
> 4. **Verify data exists**: Check that `~/.cache/autoresearch/` contains data shards and a tokenizer. If not, tell the human to run `uv run prepare.py`.
> 5. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
> 6. **Confirm and go**: Confirm setup looks good.

**Observation**: this is a **6-step deterministic-setup-checklist**. The agent is instructed to follow it AS-IS before any experimentation begins. The discipline is similar to v71 agents-best-practices' 7-invariant loop ("model proposes, harness disposes"), but applied at experiment-setup layer rather than tool-use layer.

### 5. CAN/CANNOT allowlist (verbatim binary)

**CAN**:
- Modify `train.py` — model architecture, optimizer, hyperparameters, training loop, batch size, model size

**CANNOT**:
- Modify `prepare.py` (read-only — fixed evaluation, data loading, tokenizer, constants)
- Install new packages or add dependencies (only what's in `pyproject.toml`)
- Modify the evaluation harness (`evaluate_bpb` function in prepare.py is ground truth)

**Pattern Library implication**: this is a **declared-constraint-architecture** — the agent's action-space is explicitly bounded by a permissioning policy. Distinct from typical agentic frameworks that constrain via tools + permissions (e.g., Claude Code's allowlist) — `program.md`'s constraint is embedded in the SKILL itself + read by the AGENT, not enforced by the harness.

→ **Pattern #18 NEW sub-archetype #9 candidate "agentic-research-framework-with-constraint-architecture"** evidence:
- Constraint is at the SKILL layer, not the HARNESS layer (distinct from v66 agentmemory PLATFORM-PRIMITIVE FOUNDATION + distinct from v68 zero PROGRAMMING-LANGUAGE-AS-AGENT-SUBSTRATE)
- Defines: single-file mutability + fixed-budget + never-stop-autonomy as a 3-constraint architecture

### 6. The simplicity criterion (verbatim)

> *"All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win."*

> *"A 0.001 val_bpb improvement that adds 20 lines of hacky code? Probably not worth it. A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep."*

**Observation**: program.md encodes an **explicit-trade-off-documentation** principle: complexity-cost vs improvement-magnitude. The agent is told to evaluate qualitatively + reject changes that are "ugly hacks for 0.001 gain". This is non-trivial — it instructs the agent to be a curator with editorial judgment, not just a metric-maximizer.

→ Cross-wiki signal: this aligns with v71 agents-best-practices' L0-L4 autonomy levels + draft-commit pattern; and with v75 impeccable's editorial-build-validator approach (denylist).

### 7. The experiment loop (9-step, verbatim)

> LOOP FOREVER:
> 1. Look at the git state: the current branch/commit we're on
> 2. Tune `train.py` with an experimental idea by directly hacking the code.
> 3. git commit
> 4. Run the experiment: `uv run train.py > run.log 2>&1` (redirect everything — do NOT use tee or let output flood your context)
> 5. Read out the results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
> 6. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the Python stack trace and attempt a fix. If you can't get things to work after more than a few attempts, give up.
> 7. Record the results in the tsv
> 8. If val_bpb improved (lower), you "advance" the branch, keeping the git commit
> 9. If val_bpb is equal or worse, you git reset back to where you started

**Loop design observations**:

- **Step 4** explicitly redirects to a log file + warns against context-flooding: *"do NOT use tee or let output flood your context"* — corpus-first **explicit context-window protection discipline embedded in agent-skill** (v60+ window). Typical agentic harnesses delegate context protection to the harness; program.md treats it as an explicit agent obligation.
- **Step 5** uses `grep` rather than parsing the full log — token-efficient extraction discipline
- **Step 6** caps debug-attempts at "more than a few" — defines the give-up threshold deliberately
- **Step 8-9** define the keep/discard polarity binary at val_bpb improvement-magnitude
- **LOOP FOREVER**: the agent is instructed to run indefinitely

### 8. The Never-Stop autonomy escalation (verbatim)

> *"NEVER STOP: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask 'should I keep going?' or 'is this a good stopping point?'. The human might be asleep, or gone from a computer and expects you to continue working indefinitely until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period."*

**Observations**:

- **"NEVER STOP"** = explicit non-interruption directive. Distinct from typical agentic-framework safety-defaults that build-in check-in pauses.
- **"think harder"** = explicit reasoning-loop self-prompting instruction.
- **"read papers referenced in the code"** = directs agent to seek external knowledge sources within the constrained read-allowlist (in-scope files).
- **"try combining previous near-misses, try more radical architectural changes"** = explicit exploration-escalation policy.

→ **Cross-wiki signal**: this is **CORPUS-FIRST explicit-never-stop-autonomy-escalation discipline in v60+ window**. Compare to v71 agents-best-practices' 7-loop-invariants (less directive) + v73 cc-switch session-handoff (opposite spirit — session-boundary respect). v79 program.md sits at the OPPOSITE END of the autonomy-spectrum from session-handoff disciplines.

### 9. Example use case (verbatim)

> *"As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!"*

**Pattern Library implication**: this is **CORPUS-FIRST explicit human-asleep-as-design-target use case** in v60+ window. The framework is designed assuming the human is unavailable for hours at a time — a workflow not yet documented in any prior corpus subject.

### 10. TSV logging schema (verbatim)

> *commit | val_bpb | memory_gb | status | description*

- commit: 7-char short hash
- val_bpb: 6-decimal-place float (`0.997900`) — `0.000000` for crashes
- memory_gb: 1-decimal-place float (rounded from `peak_vram_mb / 1024`) — `0.0` for crashes
- status: enum `keep` | `discard` | `crash`
- description: short free-text experiment summary

**Tab-separated mandated explicitly**: *"tab-separated, NOT comma-separated — commas break in descriptions"* — explicit rationale for the format choice. Pattern-Library implication: this is an example of **declared-format-choice-with-rationale** discipline at sub-paragraph scale.

### 11. Cross-wiki sibling intersections

| Sibling wiki | Intersection axis | Direction |
|--------------|-------------------|-----------|
| **v9 autoresearch (Karpathy parent)** | program.md verbatim inheritance | Thu Vu preserves Karpathy's skill VERBATIM; only modifications are at train.py + pyproject.toml |
| **v63 andrej-karpathy-skills (forrestchang distillation)** | Karpathy-derivative kinship | Both are Karpathy-derivatives; v63 = 1st-order public-observations distillation; v79 = 2nd-order codebase-derivative |
| **v66 agentmemory (PLATFORM-PRIMITIVE FOUNDATION)** | platform-substrate-layer comparison | agentmemory is the platform substrate; autoresearch is the experimental loop on top of (training-platform) substrate |
| **v68 zero (PROGRAMMING-LANGUAGE-AS-AGENT-SUBSTRATE)** | sub-archetype precedent | both are NEW sub-archetypes at v60+ scale; v68 = language-substrate; v79 = research-framework-substrate |
| **v71 agents-best-practices** | "model proposes, harness disposes" + 7-loop-invariants | v71 codifies execution-separation explicitly; v79 program.md embeds execution-separation IMPLICITLY (CAN/CANNOT lists) |
| **v73 cc-switch + v77 easy-vibe + v78 ECC** | autonomy / session-handoff spectrum | v79 sits at OPPOSITE END — never-stop-autonomy vs session-handoff-discipline |

### 12. Absences (counter-evidence)

**Notable ABSENCES from program.md**:
- **No prompt-injection defense baseline** (compare v78 ECC's 6-axis Prompt Defense Baseline at project-CLAUDE.md scope)
- **No security model** for the agent's bash-command output redirection (`uv run train.py > run.log 2>&1` could be hijacked by output-injection if dataset is malicious; not addressed)
- **No multi-vendor harness coverage** in skill (Claude Code + Mistral Vibe only; no MCP / no CLI-generates-native-formats compare v76 agent-skills-standard)
- **No L0-L4 autonomy-level taxonomy** (v71-style); autonomy is binary (off until setup-confirmed; full after experiment-loop-start)
- **No anti-vibe positioning** — program.md is neutral on the vibe-coding spectrum; explicit-rationality-via-metric-driven philosophy (val_bpb objectivity); no Pattern #51 sub-pole alignment
- **No supply-chain mention** — `pyproject.toml` is the only dependency mention; no sub-allowlist; no audit-trail enforcement

### 13. Pattern Library implications from Cluster 2

- **Pattern #57 57g** PRIMARY — program.md verbatim inheritance from Karpathy is the strongest evidence of methodology-preservation in second-order-derivative chain
- **Pattern #18 NEW sub-archetype #9 candidate "agentic-research-framework-with-constraint-architecture"** — CAN/CANNOT allowlist + 6-step setup + LOOP-FOREVER define the constraint architecture
- **Pattern #21 SDD-related?** — no; autoresearch is research-experiment-loop, not specification-driven-development
- **Pattern #51 vibe-coding-spectrum** — N/A; program.md is metric-driven-not-vibe-positioned (separate axis)
- **Library-vocabulary candidate "Context-Window-Protection as agent-skill-directive"** — program.md Step 4 redirect-discipline + Step 5 grep-extraction discipline are explicit context-protection instructions embedded in the agent-skill itself; corpus-first observation in v60+ window
- **Library-vocabulary candidate "Human-Asleep-as-Design-Target"** — explicit use-case section assumes overnight unattended operation; corpus-first observation
- **Library-vocabulary candidate "Never-Stop-Autonomy-Escalation-Discipline"** — explicit escalation policy at autonomy-end of spectrum; corpus-first observation

### 14. Counter-evidence + retroactive corrections

**No retroactive corrections triggered**.

**Cross-wiki spectrum positioning observation**: v79 program.md never-stop-autonomy sits at OPPOSITE END from v73 cc-switch + v77 easy-vibe + v78 ECC session-handoff disciplines. This SPECTRUM may itself be a Library-vocabulary item candidate — "Autonomy-vs-Session-Handoff-Continuum" — N=2 evidence (v79 vs cluster of v73/v77/v78 session-handoff subjects).

### 15. Phase 4b PRIMARY confirmation from Cluster 2

Cluster 2 strengthens Phase 4b PRIMARY = **Pattern #57 57g candidate** through:
- Methodology-verbatim-inheritance as evidence of second-order derivative-chain depth
- Explicit Karpathy → miolini → Thu Vu chain (intermediate adapter is NOT skill-modifier; only train.py-modifier)
- Skill-preservation at byte-level vs code-modification-at-MPS-level is a CLEAN separation between methodology-inheritance + technical-adaptation layers

→ Phase 3 Entity 3 = Pattern #57 57g entity (most-referenced cross-link target). Entity 1 (core product) + Entity 2 (distribution) will both cross-reference Entity 3 as PRIMARY deliverable.
