# (C) Entity 1 — Core product: MPS-adapted autoresearch with constraint-architecture

**Subject:** `thu-vu92/autoresearch_folktales` core product = Apple Silicon (MPS) port of Karpathy's `autoresearch` framework, retrained on a folk-mythology-tales dataset, preserving the constraint-architecture (single-modifiable-file + fixed-5-min-time-budget + never-stop-autonomy).

## 13-section canonical format

### 1. What is it (one-paragraph)

`autoresearch_folktales` is a second-order derivative of [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) (v9 corpus subject; Andrej Karpathy's autonomous-agent ML-research framework). Thu Vu (thu-vu92) has adapted Karpathy's framework — via miolini/autoresearch-macos as intermediate adapter — to run on Apple Silicon Macs (M1/M2/M3/M4 with Metal Performance Shaders / MPS) instead of NVIDIA GPUs, and retrained the embedded GPT-class model on a folk-mythology-tales dataset (Hugging Face: `merve/folk-mythology-tales`) instead of the original web-text corpus. **The agent skill (`program.md`) is preserved VERBATIM from Karpathy's original**; modifications are localized to `train.py` (model + optimizer + training loop) and `pyproject.toml` (dependency tooling).

### 2. Tier placement + archetype

**Tier**: T3 Education — agentic-research-framework as pedagogical artifact (Apple Silicon learning surface)

**Archetype**: solo-VN-diaspora-data-scientist-YouTuber (Pattern #19 sub-mechanism 19j candidate)

**Scale**: small (31 stars / 15 forks at 26 days — fork_ratio 0.484 = NEW CORPUS-RECORD-HIGH active-deployment-intent)

**Source-celebrity-derivative-distillation criteria (v2.2 — all 4 PASS)**:
- (1) Author ≠ source individual ✅ (Thu Vu ≠ Karpathy ≠ miolini)
- (2) Explicit source attribution with URL ✅ (`github.com/karpathy/autoresearch` + `github.com/miolini/autoresearch-macos` + `github.com/karpathy/nanochat` all cited in README Credits)
- (3) Public observations as raw material ✅ (Karpathy's autoresearch is public; miolini's macOS port is public; Thu Vu derived from public artifacts)
- (4) Installable artifact packaging ✅ (uv-installable Python package)

**Distinction from v63 forrestchang/karpathy-skills**:
- v63 = 1st-order distillation of Karpathy's PUBLIC X-TWEET OBSERVATIONS into installable agent-skill
- v79 = 2nd-order derivative of Karpathy's PUBLIC CODEBASE via intermediate adapter

→ Both are Karpathy-derivatives but at distinct chain-depths + distinct source-material types (tweets vs codebase).

### 3. Constraint-architecture (3 dimensions)

| Constraint | Verbatim definition | Source |
|------------|---------------------|--------|
| **Single-modifiable-file** | Only `train.py` is agent-mutable; `prepare.py` + `program.md` + `pyproject.toml` are read-only | program.md "CANNOT" allowlist |
| **Fixed-5-min-time-budget** | Each experiment runs exactly 5 minutes wall-clock (excluding startup + compilation) | program.md "Experimentation" |
| **Never-stop-autonomy** | Agent runs LOOP FOREVER until human interrupts; no check-in pauses | program.md "NEVER STOP" |

**Combined: 3-constraint architecture defines the framework's identity**. Without all 3, the framework loses its character:
- Drop single-modifiable-file → agent scope balloons, debugging gets expensive
- Drop fixed-time-budget → experiments not directly comparable
- Drop never-stop → not autonomous overnight (defeats the use-case)

→ **Pattern #18 NEW sub-archetype #9 candidate "agentic-research-framework-with-constraint-architecture"** PROVISIONAL N=1 evidence.

### 4. The autoresearch experiment loop

**9-step procedure** (verbatim from program.md):
1. Look at git state
2. Tune `train.py` with experimental idea
3. git commit
4. Run experiment: `uv run train.py > run.log 2>&1`
5. Read results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. If crash: read stack trace, attempt fix (cap at "more than a few attempts")
7. Record results in TSV
8. If val_bpb improved (lower): advance the branch
9. If equal or worse: git reset

**Implications**:
- Git is the agent's state-machine (branch advances on improvement, resets on regression)
- TSV is the agent's append-only experiment-log
- val_bpb is the agent's quality function (vocab-size-independent, allowing fair architectural-change comparisons)
- Context-window protection is the agent's own responsibility (Step 4: "do NOT use tee or let output flood your context")

### 5. The val_bpb metric design

**Why bits-per-byte (not perplexity)**:
> *"val_bpb remains vocab-size-independent so architectural changes are fairly compared"*

Architectural experiments can:
- Change tokenizer (different vocab)
- Change sequence length
- Change context window
- Change embedding strategy

Perplexity (PPL = exp(loss)) depends on tokenizer's vocab. Two experiments with different tokenizers can't be compared in PPL terms. **Bits-per-byte normalizes for tokenizer differences**: loss-per-byte is dimensionally consistent across vocabs.

→ **Cross-wiki signal**: this is a generalizable design principle ("size-independent quality measure") that could apply to vault routine v2.2+ quality metrics for wiki output (e.g., "depth per file-size" or "corpus-firsts per line").

### 6. The simplicity criterion

**Verbatim**:
> *"All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win."*

> *"A 0.001 val_bpb improvement that adds 20 lines of hacky code? Probably not worth it. A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep."*

**Editorial-judgment-embedded-in-skill**: program.md doesn't just say "minimize val_bpb"; it instructs the agent to weigh complexity-cost against improvement-magnitude. The agent must be a CURATOR with editorial judgment, not a metric-maximizer.

→ **Library-vocabulary candidate "Editorial-Judgment-Embedded-in-Agent-Skill"** — corpus-first observation.

### 7. Apple Silicon MPS adaptation specifics

**4 explicit modifications** from Karpathy original:

1. **FlashAttention-3 → native PyTorch SDPA + manual sliding-window causal masking**
2. **`torch.compile` MPS-incompatible paths disabled** (preserves correctness at throughput cost)
3. **Metal-compatible optimizer states** (Muon + AdamW dtypes converted)
4. **No distributed training** (single-Apple-Silicon-device only)

**Performance trade-off**: ~85-90 optimizer steps in 5 minutes on MPS vs 1000s on fast GPU = **~10× throughput collapse**.

**Interpretation**: Thu Vu prioritizes METHOD-PRESERVATION (Karpathy's loop + budget + metric all intact) over THROUGHPUT-OPTIMIZATION (could have changed budget to compensate). This is a deliberate design choice: keep the FRAMEWORK's character intact, accept slower experiments.

→ **Library-vocabulary candidate "Method-Preserved-Despite-10×-Throughput-Collapse"** — corpus-first observation in v60+ window.

### 8. The "human asleep" use case

**Verbatim**:
> *"As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!"*

→ Design target = **overnight unattended operation**. The framework is designed assuming the human is unavailable for hours at a time. **CORPUS-FIRST explicit human-asleep-as-design-target use case** in v60+ window.

**Compare**:
- v77 easy-vibe: pedagogy for actively-engaged learner (opposite design target)
- v78 ECC: operator-system for active-during-day operator
- v79 autoresearch_folktales: designed for explicitly-absent operator

### 9. Dataset substitution: folk-mythology-tales

**Substitution rationale (not justified in README)**:
- Folk-mythology-tales is small enough for the 5-min experiment budget on MPS (CUDA original used larger web-text corpora)
- Folklore is editorially interesting (cultural / pedagogical / YouTube-audience-appealing)
- Dataset author `merve` ≠ Thu Vu — 3rd-party dataset reuse with explicit attribution

→ **CORPUS-FIRST dataset-author-different-from-project-author-AND-framework-author-AND-intermediate-adapter-author** quadruple-distinct-author-stack in v60+ window:
1. Karpathy (framework author)
2. miolini (intermediate adapter)
3. Thu Vu (this project)
4. merve (dataset author)

### 10. Cross-wiki sibling references (mandatory ≥3)

| Sibling wiki | Direction of reference |
|--------------|------------------------|
| **v9 autoresearch (Karpathy parent)** | DIRECT PARENT — methodology source via README Credits |
| **v63 andrej-karpathy-skills (forrestchang)** | sibling derivative-of-Karpathy at 1st-order distillation (distinct chain-depth) |
| **v74 LLMs-from-scratch (Raschka)** | T3 tier-peer + LLM-training pedagogy + author-archetype methodology-influence-node |
| **v68 zero (vercel-labs)** | sub-archetype-precedent for Pattern #18 #9 NEW candidate "constraint-architecture" |
| **v66 agentmemory** | platform-substrate-layer comparison (autoresearch = experiment-loop on top of training-substrate; agentmemory = platform-primitive substrate itself) |
| **v71 agents-best-practices** | execution-separation comparison ("model proposes, harness disposes" verbatim L0-L4 codification vs program.md's IMPLICIT CAN/CANNOT allowlist) |
| **v78 ECC** | corpus-recursive sibling (v78 57f anchor-self-reference + v79 57g derivative-chain) |

### 11. Pattern Library tags

- **Pattern #57 sub-variant 57g** (PRIMARY) — Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter
- **Pattern #18 NEW sub-archetype #9 candidate** — agentic-research-framework-with-constraint-architecture (PROVISIONAL N=1)
- **Pattern #19 sub-mechanism 19j candidate** — Vietnamese-Diaspora-Data-Scientist-YouTuber-with-LLM-derivative-experiments (PROVISIONAL N=1)
- **Pattern #84 NEW sub-typology 84d candidate** — Hardware-Substrate-Tolerance (Apple Silicon MPS substrate-pinned + agent-platform-tolerant)
- **Pattern #83 sub-mechanism 83f.4 NEW sub-variant** — README-Declared-MIT-without-LICENSE-file (N=4 post-promotion strengthening)
- **Pattern #45 NEW sub-typology 45f candidate** — README-Declared-MIT-without-LICENSE-file OR Pattern #29 absent-LICENSE strengthening
- **Pattern #66 within-pattern** — minimal-dependency-discipline-by-constraint (vs by-defense)

### 12. Novel observations + candidates

**Library-vocabulary candidates emerging from Entity 1**:
- **Editorial-Judgment-Embedded-in-Agent-Skill** (simplicity criterion verbatim quote)
- **Method-Preserved-Despite-10×-Throughput-Collapse** (MPS vs CUDA trade-off)
- **Human-Asleep-as-Design-Target** (explicit use-case section)
- **Context-Window-Protection-as-Agent-Skill-Directive** (Step 4 redirect discipline + Step 5 grep-extraction)
- **Try-Once-and-Move-On Profile** (fork_ratio 0.484 + 0 subscribers + 0 issues)

### 13. Notable absences (counter-evidence audit)

- No CLAUDE.md / AGENTS.md at root (program.md serves the role)
- No multi-harness support (Claude Code + Mistral Vibe only)
- No supply-chain disclosure beyond MIT-declared-but-no-LICENSE-file
- No i18n (EN-only)
- No tests/ / CI / GitHub Actions
- No docs/ / GitHub Pages
- No prompt-injection defense baseline
- No release/changelog discipline

→ All absences are **expected for T3 Education research-experiment artifact**. They reinforce the tier placement. None constitute counter-evidence to corpus patterns.
