# (C) Entity 2 — Distribution: uv-exclusive packaging + HF dataset integration + Apple Silicon hardware-substrate

**Subject:** Distribution + ecosystem-integration of `thu-vu92/autoresearch_folktales` — how the framework is delivered, what dependencies it touches, what platforms it targets, and how it relates to corpus packaging-and-distribution patterns.

## 13-section canonical format

### 1. Packaging tool: `uv` (exclusive)

**`uv`** = Rust-based modern Python package manager from astral-sh.

**README quick-start commands** (verbatim sequence):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run prepare.py
uv run train.py
```

**Files present**:
- `pyproject.toml` (PEP 621 modern format)
- `uv.lock` (reproducible-install lockfile)
- `.python-version` (uv reads this for Python-version constraint)

**No fallbacks**:
- No pip-fallback
- No poetry-fallback
- No conda-fallback
- No setup.py legacy

→ **CORPUS-FIRST single-tool-no-fallback packaging adoption** in v60+ window. Compare:
- v74 LLMs-from-scratch: uv + uv-pip via 3-OS test matrix (dual-tool)
- v76 agent-skills-standard: pnpm + npm (Node ecosystem with explicit dual)
- v77 easy-vibe: Node ≥18 + VitePress build (Node ecosystem)
- v78 ECC: pnpm + npm + GitHub App + Hermes operator (multi-tool)
- v79 autoresearch_folktales: uv ONLY (single-tool-no-fallback)

### 2. Hugging Face datasets integration

**Dataset**: [`merve/folk-mythology-tales`](https://huggingface.co/datasets/merve/folk-mythology-tales)

**Maintainer**: `merve` (Hugging Face user; distinct from Thu Vu, Karpathy, miolini)

**Integration mechanism**: `prepare.py` downloads + tokenizes; cached to `~/.cache/autoresearch/` (XDG-cache convention).

**Cache lifecycle**:
- Read-only after first preparation
- Reused across all subsequent experiments
- Manual `uv run prepare.py` re-trigger to refresh

→ **CORPUS-FIRST 4-distinct-authors-across-artifact-stack** (Karpathy framework + miolini adapter + Thu Vu MPS-port + merve dataset).

### 3. Apple Silicon hardware-substrate-pinned distribution

**Explicit hardware target (verbatim)**:
> *"Apple Silicon Mac (M1/M2/M3/M4 with Metal/MPS support)"*

**No fallback** for x86 / NVIDIA / AMD / Linux GPU. The framework is Apple-Silicon-only.

→ **Pattern #84 NEW sub-typology 84d candidate "Hardware-Substrate-Tolerance"** PROVISIONAL N=1:

Distinct from existing 84a/84b/84c:
- **84a Tool-tolerance** (v62 codex-plugin-cc) — works across coding-tool harnesses
- **84b Usage-enforcement** (v65 claude-code-system-prompts) — usage-policy across-tier consumers
- **84c Provider-Agnostic-By-Design** (v71+v72+v73+v75+v76+v77+v78 7-wiki arc CORPUS-RECORD) — provider-neutral framework architecture
- **84d Hardware-Substrate-Tolerance (NEW)** (v79) — agent-platform-tolerant BUT hardware-substrate-pinned

The NEW 84d sub-typology has an interesting structural inversion: instead of being PROVIDER-agnostic-and-substrate-tolerant (like 84c at runtime/distribution layers), 84d is **HARDWARE-SUBSTRATE-PINNED + agent-platform-TOLERANT** — a complementary dimension.

### 4. Agent-platform tolerance (within hardware-substrate pin)

**README explicit agent-platform list**:
- Claude Code (Anthropic)
- Mistral Vibe (Mistral AI)

**Implicit**: any agent capable of (a) reading `program.md`, (b) executing bash, (c) git-state-tracking, (d) editing single Python file.

**Missing from explicit list (notable absences)**:
- No Cursor mention
- No GitHub Copilot mention
- No Aider mention
- No OpenHands mention
- No Roo / Cline / Windsurf / Kiro / Trae

→ Distinct from v76 agent-skills-standard's 10+ explicitly-listed harnesses. v79 is **narrow-agent-platform-list with broad-implicit-tolerance**.

### 5. Project structure (verbatim file list)

```
prepare.py      — constants, data prep + runtime utilities (do not modify)
train.py        — model, optimizer, training loop (agent modifies this)
program.md      — agent instructions
pyproject.toml  — dependencies
```

**Other root-level entries** (from GitHub tree):
```
.github/
.gitignore
.python-version
README.md
analysis.ipynb
prepare.py
program.md
progress.png
pyproject.toml
results.tsv
train.py
uv.lock
```

→ **12 root entries total** — minimal repo surface. No `tests/`, no `docs/`, no `CLAUDE.md`, no `AGENTS.md`, no `SECURITY.md`, no `CONTRIBUTING.md`.

### 6. The analysis.ipynb post-experiment layer

**`analysis.ipynb`** — Jupyter notebook for post-experiment review (15.4% of repo language % = primary non-Python source).

**`progress.png`** — likely a plot of val_bpb vs experiment-index (typical autoresearch artifact).

**`results.tsv`** — agent's append-only experiment log per program.md schema (commit | val_bpb | memory_gb | status | description).

→ **3-artifact analysis layer**: code+plot+TSV. Manual-review-friendly outputs. Distinct from agent-execution-loop layer (program.md + train.py).

### 7. Optimizers (Muon + AdamW)

**Muon optimizer** — recent (2024+) optimizer for transformer training; momentum-orthogonalized methods. **CORPUS-FIRST Muon reference in v60+ window**.

**AdamW** — standard transformer training optimizer.

**Dual-optimizer setup** — both used in train.py (inferred from README "optimizers (Muon + AdamW)" wording).

### 8. Dependency-discipline observations

**Per program.md CAN/CANNOT allowlist**: agent CANNOT install new packages or add dependencies.

**Per README design-choices**: *"Minimal dependencies beyond PyTorch."*

→ **Pattern #66 within-pattern strengthening evidence**:
- Closed dependency set at agent-time (agent's action-space is bounded)
- Reproducible-install via `uv.lock`
- Agent-policy-enforced dependency stability

**But ALSO ABSENT from Pattern #66 evidence**:
- No SECURITY.md
- No supply-chain audit baseline (compare v78 ECC ecc-agentshield + Prompt Defense Baseline)
- No SBOM / no signed releases / no signed commits visible

→ Pattern #66 evidence is **discipline-by-constraint not by-defense** — distinct from v78 ECC's discipline-by-active-defense.

### 9. License + LICENSE-file status

**README declares**: *"License: MIT"*
**GitHub API reports**: `license: None` (verified via api.github.com 2026-05-20)
**No LICENSE file** in repo root tree

→ **Pattern #83 sub-mechanism 83f N=4 post-promotion strengthening + NEW sub-variant 83f.4 candidate**:

| Sub-variant | Prior wiki instance | Distinct mechanism |
|-------------|---------------------|---------------------|
| 83f.1 within-LICENSE mismatch | v74 LLMs-from-scratch (CITATION.cff vs LICENSE.txt) | Inside-LICENSE-file inconsistency |
| 83f.2 across-doc-LICENSE mismatch | v76 agent-skills-standard (README vs LICENSE) | README + LICENSE-file diverge |
| 83f.3 across-doc-API mismatch | v77 easy-vibe (README CC-BY-NC-SA vs API None) | README + API report diverge |
| **83f.4 NEW: README-declared-but-no-LICENSE-file** | v79 autoresearch_folktales (README "MIT" + no LICENSE file + API None) | README declares license + no LICENSE file exists |

→ 83f taxonomy 3-variant → 4-variant expansion at v79.

### 10. Cross-wiki distribution-pattern intersections

| Sibling | Distribution-pattern axis | v79 alignment |
|---------|---------------------------|---------------|
| v9 autoresearch (Karpathy) | git-clone-direct + manual setup | v79 INHERITS via README "git clone..." quick-start sequence |
| v63 forrestchang/karpathy-skills | Claude Code skill installable via `skills attach` | v79 = different distribution channel (uv-package vs skill) |
| v66 agentmemory | npm + MCP server | v79 = different domain (training-research vs agent-memory) |
| v74 LLMs-from-scratch | uv + uv-pip across 3 OS via test matrix | v79 narrows to uv-only single-OS (Apple Silicon) |
| v75 impeccable | 14-harness multi-target distribution | v79 narrows to 2-explicit-harnesses (Claude Code + Mistral Vibe) |
| v76 agent-skills-standard | npm + CLI-generates-native-formats 10+ harnesses | v79 narrows to no-CLI + 2-explicit-harnesses |
| v77 easy-vibe | 5-deploy-target auto-detection | v79 narrows to single-deploy-target (local Apple Silicon) |
| v78 ECC | 11+-harness dirs + pnpm + GitHub App + Hermes | v79 narrows to single-tool-no-fallback (uv) + single-hardware-substrate |

→ v79 is **CORPUS-FIRST DELIBERATELY-NARROW distribution profile** in v60+ window. Most v60+ subjects expand distribution surface; v79 contracts.

### 11. Active-deployment intent (fork_ratio analysis)

**Verified GitHub API 2026-05-20**:
- stars: 31
- forks: 15
- subscribers: 0
- open_issues: 0

**fork_ratio = 15/31 = 0.484 = 48.4%**

→ **NEW CORPUS-RECORD-HIGH active-deployment-intent**: exceeds v76 HoangNguyen0403/agent-skills-standard 0.296 prior record by **1.64×**.

**Interpretation**:
- Half of stargazers also forked → very HIGH active-deployment intent
- Correlated with: (a) Apple Silicon Mac owners wanting to run autoresearch locally without GPU, (b) Karpathy-fans curious about the MPS port, (c) the YouTube walkthrough audience following along
- The 0-subscribers + 0-issues pattern indicates: **try-it-once-and-move-on profile** (one-shot experimentation, not sustained project)

→ **Library-vocabulary item candidate "High-Fork-Ratio with Zero-Engagement-Signal = Try-Once-and-Move-On profile"** PROVISIONAL N=1.

### 12. Pattern Library tags

- **Pattern #84 NEW sub-typology 84d candidate** "Hardware-Substrate-Tolerance" (PROVISIONAL N=1)
- **Pattern #83 sub-mechanism 83f N=4** post-promotion strengthening + **NEW sub-variant 83f.4 candidate** "README-Declared-but-no-LICENSE-file"
- **Pattern #66 within-pattern** — minimal-dependency-discipline-by-constraint
- **Pattern #45 NEW sub-typology 45f candidate** OR Pattern #29 absent-LICENSE strengthening
- **Pattern #52** non-applicable (LOW-velocity 1.19/d)
- **Library-vocabulary item candidates**:
  - High-Fork-Ratio with Zero-Engagement-Signal = Try-Once-and-Move-On profile
  - Deliberately-Narrow Distribution Profile in v60+ window
  - Single-Tool-No-Fallback Packaging Adoption

### 13. Notable absences

- **No multi-harness `.cursor/.gemini/.codex/.kiro/` etc. config directories** (vs v75/v76/v77/v78 standard)
- **No i18n** (EN-only README)
- **No tests/ + no CI** (research-experiment artifact)
- **No release/changelog** discipline
- **No SECURITY.md** / no supply-chain SBOM
- **No docs/ site / GitHub Pages**
- **No issue templates / PR templates** (in .github/ — minimal)

→ All absences fit T3 Education research-experiment artifact profile. None constitute counter-evidence.
