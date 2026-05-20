# (C) Cluster 3 — Technical / distribution

**Sources:**
- `pyproject.toml` (via README inference + `uv.lock` presence)
- `prepare.py` (read-only per program.md skill; structure inferred from README design-choices)
- `train.py` (agent-mutable; current MPS-adapted state on branch `autoresearch/apr10`)
- `analysis.ipynb` + `progress.png` + `results.tsv` (analysis artifacts)
- GitHub API repo metadata (verified 2026-05-20)

## 15-section format

### 1. Cluster scope

Technical surface: Python implementation + uv packaging + Hugging Face datasets integration + Apple Silicon MPS adaptation specifics + analysis tooling (Jupyter notebook + progress.png + TSV results log). This cluster documents HOW the framework is deployed + WHAT differentiates Thu Vu's MPS-port from Karpathy's CUDA-original.

### 2. Packaging architecture

**Build tool**: `uv` (astral-sh/uv) — modern Rust-based Python package manager.

**Project file**: `pyproject.toml` (PEP 621 modern format).

**Lock file**: `uv.lock` — uv's dependency lockfile (reproducible-install discipline).

**Python version**: `.python-version` file present at repo root → uv reads this for the project's Python version constraint.

**README quick-start sequence**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run prepare.py
uv run train.py
```

→ uv-only workflow (no pip-fallback, no poetry-fallback, no conda-fallback). **CORPUS-FIRST uv-exclusive packaging in v60+ window** (v74 LLMs-from-scratch uses both uv + uv-pip via 3-OS test matrix; v79 is uv-only single-platform Apple Silicon).

### 3. Apple Silicon MPS adaptation

**4 explicit modifications** documented in README design-choices section:

1. **FlashAttention-3 removed** → substituted with native PyTorch SDPA (Scaled Dot-Product Attention) + manual sliding-window causal masking
2. **`torch.compile` MPS-incompatible paths disabled** — torch.compile cannot fully JIT-compile through Metal Performance Shaders; disabled paths preserve functional-correctness at throughput cost
3. **Metal-compatible optimizer states** — Muon + AdamW optimizers' state tensors converted to MPS-compatible dtypes
4. **No distributed training** — single-device only (Karpathy's original supports multi-GPU; Thu Vu's port is single-Apple-Silicon-device)

**Performance verbatim**: *"~85–90 optimizer steps in 5 minutes vs. 1000s on a fast GPU"* — **CORPUS-FIRST documented method-preserved-despite-10×-throughput-collapse trade-off** in v60+ window.

### 4. Single-modifiable-file architecture

**File mutability matrix** (per program.md skill):

| File | Agent mutability | Rationale |
|------|------------------|-----------|
| `prepare.py` | **READ-ONLY** | Fixed constants (5-min budget, sequence length, vocab) + data prep + tokenizer + `evaluate_bpb` ground-truth metric |
| `train.py` | **MUTABLE** | Model architecture (GPT-class), optimizer (Muon + AdamW), training loop, batch size, model size |
| `program.md` | **READ-ONLY** (not stated explicitly, but treated as fixed agent skill) | Verbatim Karpathy original |
| `pyproject.toml` | **READ-ONLY** (per CAN/CANNOT allowlist) | Fixed dependency set |
| `results.tsv` | **WRITE-ONLY APPEND** | Agent's experiment-log artifact |

→ **5-layer mutability discipline**: 1 mutable / 3 read-only / 1 append-only. **CORPUS-FIRST 5-layer mutability discipline at sub-10-file repo scale** in v60+ window.

### 5. Hugging Face datasets integration

**Dataset**: `merve/folk-mythology-tales` (Hugging Face datasets hub)

**Dataset author**: `merve` (HF username; not Thu Vu; not Karpathy) — **CORPUS-FIRST dataset-author-different-from-project-author + framework-author + intermediate-adapter** in v60+ window (three distinct authors across the artifact-stack).

**Integration mechanism**: `prepare.py` handles dataset download + tokenization. Cached to `~/.cache/autoresearch/` (verbatim path from program.md Setup step 4).

**Cache pattern**: dotfile-cache directory under home (`~/.cache/`); follows XDG-cache convention. Read-only after preparation; reused across all subsequent experiments.

### 6. Optimizers used

**Muon + AdamW dual-optimizer setup** (inferred from README "optimizers (Muon + AdamW)" mention).

**Muon optimizer** — recent (2024+) optimizer for transformer training; momentum-orthogonalized methods. **CORPUS-FIRST Muon optimizer reference in v60+ window**.

**AdamW** — standard transformer training optimizer; ubiquitous.

### 7. Evaluation metric

**`val_bpb`** = validation bits-per-byte.

**Why bits-per-byte (not perplexity)**:
> *"val_bpb remains vocab-size-independent so architectural changes are fairly compared"*

Architectural changes can alter the vocab + sequence-length budgets; bits-per-byte normalizes for this. Perplexity would skew if vocab changes between experiments.

→ **Cross-wiki signal**: this is **CORPUS-FIRST size-independent-quality-metric design principle** at sub-program scale in v60+ window. Could generalize to vault routine v2.2+ quality metrics for wiki output: "size-independent quality measure".

### 8. analysis.ipynb + progress.png

**`analysis.ipynb`** — Jupyter notebook for post-experiment analysis (15.4% of repo language % = primary non-Python source).

**`progress.png`** — likely a plot of val_bpb vs experiment-index (typical autoresearch artifact); not verified directly.

**`results.tsv`** — agent's append-only experiment log per program.md schema (commit | val_bpb | memory_gb | status | description).

→ **3-artifact analysis layer**: code+plot+TSV. Distinct from agent-execution-loop layer (program.md + train.py). Manual-review-friendly outputs (vs agent's autonomous loop).

### 9. Distribution + agent-platform tolerance

**README explicit agent-platform list**:
- Claude Code (Anthropic)
- Mistral Vibe (Mistral AI)

**Implicit**: any agent capable of (a) reading `program.md`, (b) executing bash, (c) git-state-tracking, (d) editing single Python file — should work.

→ **Pattern #84 NEW sub-typology 84d candidate "Hardware-Substrate-Tolerance"** evidence: Apple Silicon MPS is the explicit hardware substrate; the framework asserts portability to other "agent-capable" platforms — but the hardware substrate is hard-pinned. Distinct from 84a (Tool-tolerance) / 84b (Usage-enforcement) / 84c (Provider-Agnostic-By-Design).

Compare to:
- v75 impeccable 14-harness multi-target distribution at distribution layer
- v76 agent-skills-standard CLI-generates-native-formats across 10+ harnesses
- v77 easy-vibe curriculum-mediated harness exposure
- v79 hardware-substrate-pinned-but-agent-platform-tolerant = NEW sub-mechanism dimension

### 10. Dependency-discipline observations

**Per program.md CAN/CANNOT allowlist**: agent CANNOT install new packages or add dependencies.

**Per README design-choices**: "Minimal dependencies beyond PyTorch."

→ **Pattern #66 within-pattern strengthening evidence**:
- Closed dependency set at agent-time
- Reproducible-install via `uv.lock`
- Agent-policy-enforced dependency stability

But ALSO ABSENT from Pattern #66 evidence:
- No SECURITY.md
- No supply-chain audit baseline (compare v78 ECC ecc-agentshield + Prompt Defense Baseline)
- No SBOM / no signed releases / no signed commits visible

→ Pattern #66 evidence is **discipline-by-constraint not by-defense** — distinct from v78 ECC's discipline-by-active-defense.

### 11. Single-push-and-done activity profile

**GitHub API verified data**:
- `created_at`: 2026-04-24T21:04:16Z
- `pushed_at`: 2026-04-24T21:15:57Z
- Δ = 11 minutes 41 seconds between repo creation and last push

→ **CORPUS-FIRST single-push-and-done activity profile in v60+ window**: repo created + completed + published all within ~12 minutes. No follow-up commits since.

**But**: README mentions branch `autoresearch/apr10` with 58 commits — the branch internally has commit history (likely Karpathy upstream + miolini-adapter + Thu Vu-MPS-port commits). The pushed_at reflects the LAST push, which was the initial one.

→ Interpretation: Thu Vu prepared the codebase locally (likely through multiple iterations), then single-pushed the final state to GitHub. The repo's surface state is the "frozen final-state" of her preparation. Not active-development-after-publish.

### 12. Active-deployment intent (fork_ratio analysis)

**Verified GitHub API 2026-05-20**:
- stars: 31
- forks: 15
- subscribers: 0
- open_issues: 0

**fork_ratio = 15/31 = 0.484 = 48.4%**

→ **NEW CORPUS-RECORD-HIGH active-deployment-intent**: exceeds v76 HoangNguyen0403/agent-skills-standard 0.296 prior record by **1.64×**.

**Interpretation**:
- Half of stargazers also forked → very HIGH active-deployment intent (they want to RUN it, not just bookmark)
- Likely correlated with: (a) Apple Silicon Mac owners wanting to run autoresearch locally without GPU, (b) Karpathy-fans curious about the MPS port, (c) the YouTube walkthrough audience following along
- The 0-subscribers + 0-issues is striking — high fork-to-star ratio but zero ongoing engagement signals: this is a **try-it-once-and-move-on profile** (one-shot experimentation, not sustained project)

→ **Library-vocabulary item candidate "High-Fork-Ratio with Zero-Engagement-Signal = Try-Once-and-Move-On profile"** — corpus-first observation.

### 13. Pattern Library implications from Cluster 3

| Pattern | Evidence from Cluster 3 |
|---------|-------------------------|
| **#84 NEW sub-typology 84d candidate** | Apple Silicon MPS hardware-substrate pinning + agent-platform tolerance |
| **#66 within-pattern** | minimal-dependency discipline by constraint (not by defense) |
| **#52 LOW-velocity** | 1.19 stars/day at 26 days — well below all sub-class thresholds (EXTREME-VIRAL >300/d / HIGH-NOT-EXTREME 150-300/d / SUSTAINED-MODERATE-HIGH 25-150/d / LONG-SUSTAINED-MEDIUM 60-150/d × 1000+d / MULTI-MONTH-SUSTAINED-EXTREME-VIRAL >300/d × 90+d) |
| **#83 sub-mechanism 83f.4 NEW sub-variant** | README "MIT" declared + no LICENSE file + GitHub API license: None |
| **#45 NEW sub-typology 45f candidate** | README-Declared-MIT-without-LICENSE-file OR Pattern #29 absent-LICENSE strengthening |
| **#57 sub-variant 57g** | 2-hop derivative-chain documented via miolini intermediate-adapter (PRIMARY) |
| **Library-vocabulary candidate "Try-Once-and-Move-On profile"** | fork_ratio 0.484 + 0 subscribers + 0 issues |
| **Library-vocabulary candidate "Method-Preserved-Despite-10×-Throughput-Collapse trade-off"** | 85-90 optimizer steps in 5 min on MPS vs 1000s on GPU |

### 14. Counter-evidence + absent-feature audit

**ABSENT from typical corpus-v60+ subjects**:
- No `.claude/`, `.cursor/`, `.gemini/`, `.codex/`, `.kiro/` etc. agent-harness-config directories
- No multi-locale README (EN-only)
- No `AGENTS.md` (v75 + v76 + v77 + v78 standard); program.md serves the role but at root, not in standard location
- No tests/ + no CI badges + no GitHub Actions visible
- No release/changelog discipline
- No supply-chain SBOM / signed-commits / SECURITY.md
- No docs/ site / GitHub Pages
- No issue templates (.github/ exists but minimal)

**Cluster 3 absences** are all expected for a **research-experiment artifact** (vs production-or-distribution-aimed framework). They reinforce the **T3 Education tier** placement.

### 15. Phase 4b PRIMARY confirmation from Cluster 3

Cluster 3 strengthens Phase 4b PRIMARY = **Pattern #57 57g candidate** through:
- Technical-adaptation-only-at-train.py-layer (methodology preserved verbatim)
- Hardware-substrate-tolerance dimension (84d candidate) added at distribution layer
- uv-exclusive packaging discipline (corpus-first single-tool-no-fallback adoption)
- Try-once-and-move-on profile observation differentiates v79 from "active-deployment-target" subjects in corpus

→ All 3 clusters confirm Phase 4b routing: Pattern #57 57g sub-variant N=1 PROVISIONAL registration as PRIMARY proposal-document deliverable.
