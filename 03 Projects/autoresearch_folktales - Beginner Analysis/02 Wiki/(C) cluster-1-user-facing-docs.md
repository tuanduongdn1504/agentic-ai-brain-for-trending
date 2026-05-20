# (C) Cluster 1 — User-facing docs (README)

**Source:** `README.md` on branch `autoresearch/apr10` (default branch); fetched 2026-05-20 via raw.githubusercontent.com.

## 15-section format

### 1. Cluster scope

User-facing README — the entire public surface of the repo aside from `program.md` (agent skill, see Cluster 2) and the Python implementation (see Cluster 3). Covers: project positioning, methodology lineage to Karpathy, Apple Silicon adaptation rationale, install + run sequence, project structure, dataset, design-choices design notes, credits, MIT license declaration.

### 2. Positioning / tagline / first-impression

**Tagline**: *"An adaptation of Andrej Karpathy's autoresearch for training a small LLM on folktales dataset, running on Apple Silicon Mac."*

**One-line positioning**: Apple Silicon (MPS) port + folktale-dataset retraining of Karpathy's `autoresearch` framework, retaining the autonomous-agent research-loop methodology.

**Positioning corpus-first signals**:
- **CORPUS-FIRST Apple Silicon / MPS adaptation in v60+ window** — first corpus subject scoped exclusively to Apple Silicon (M1/M2/M3/M4 Macs) as deployment platform
- **CORPUS-FIRST second-order derivative-chain of v9 corpus subject via intermediate adapter** — Karpathy autoresearch (v9 corpus parent) → miolini/autoresearch-macos (intermediate Mac-OS adapter) → Thu Vu autoresearch_folktales (v79 second-order derivative)
- **CORPUS-FIRST folktale / folklore-mythology dataset as LLM training corpus** in v60+ window (educational pedagogy context)
- **CORPUS-FIRST single-push-and-done activity profile** in v60+ window (repo created + pushed 2026-04-24, no follow-up commits since)

### 3. 10-section table-of-contents (verbatim header sequence)

1. About the original project
2. Overview
3. How it works
4. Quick start
5. Running the agent
6. Project structure
7. Dataset
8. Design choices
9. Credits
10. License

### 4. Key verbatim claims (preserved as quotes)

**On methodology preservation despite throughput collapse**:
- *"~85–90 optimizer steps in 5 minutes vs. 1000s on a fast GPU"*

**On single-modifiable-file design**:
- *Three essential files: prepare.py (Fixed constants, one-time data preparation, runtime utilities), train.py (The single modifiable file containing GPT architecture, optimizers (Muon + AdamW), and training loop), program.md (Baseline agent instructions)*

**On evaluation metric stability**:
- *"val_bpb remains vocab-size-independent so architectural changes are fairly compared"*

**On fixed time budget**:
- *"fixed 5-minute time budget (wall clock, excluding startup/compilation)"*

**On agent invocation**:
- Recommended prompt: *"Hi have a look at program.md and let's kick off a new experiment!"*

**On design-choices for MPS**:
- FlashAttention-3 removed; native PyTorch SDPA with manual sliding window causal masking substituted
- `torch.compile` MPS-incompatible paths disabled
- Single-file modification scope keeps agent interaction manageable

### 5. Methodology lineage (Karpathy → miolini → Thu Vu)

**Direct citation chain extracted from Credits section**:

1. **Andrej Karpathy** — `github.com/karpathy/autoresearch` (v9 corpus subject; methodology source)
2. **miolini/autoresearch-macos** — `github.com/miolini/autoresearch-macos` (intermediate adapter; macOS layer)
3. **Thu Vu** — `github.com/thu-vu92/autoresearch_folktales` (v79 second-order derivative; Apple Silicon MPS + folktale-dataset)

**Additional Karpathy artifact cited**: `github.com/karpathy/nanochat` (underlying training implementation — the simplified single-GPU LLM training codebase from which `autoresearch` itself derives)

This 4-artifact chain (autoresearch → nanochat as Karpathy-internal lineage + miolini macOS-adapter + Thu Vu MPS-port) demonstrates **CORPUS-FIRST 2-hop derivative-chain via documented intermediate adapter**.

### 6. Quick-start sequence (verbatim install commands)

```bash
git clone https://github.com/thu-vu92/autoresearch_folktales.git
cd autoresearch_folktales
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run prepare.py
uv run train.py
```

**Requirements (verbatim)**:
> *"Apple Silicon Mac (M1/M2/M3/M4 with Metal/MPS support), Python 3.10+, uv, and an AI coding agent such as Claude Code or Mistral Vibe"*

### 7. Project structure (verbatim file list)

```
prepare.py      — constants, data prep + runtime utilities (do not modify)
train.py        — model, optimizer, training loop (agent modifies this)
program.md      — agent instructions
pyproject.toml  — dependencies
```

Root-level files in repo (from GitHub tree):
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

**12 root entries total** — extremely lean surface. No `CLAUDE.md`, no `AGENTS.md`, no `CONTRIBUTING.md`, no `SECURITY.md`, no `tests/`, no `docs/`. Single agent-skill file = `program.md`.

### 8. Dataset

**Source**: [`merve/folk-mythology-tales`](https://huggingface.co/datasets/merve/folk-mythology-tales) (Hugging Face)

**Maintainer of dataset**: `merve` (Hugging Face username; not Thu Vu; CORPUS-FIRST evidence of dataset-author ≠ project-author at v79)

**Subject domain**: folklore / mythology tales — pedagogically interesting + small (suitable for MPS 5-minute experiment budget); editorial choice not justified in README

**Processing**: README states *"Automated downloading and tokenization occur via prepare.py"* — agent doesn't manage dataset prep, it's a fixed pre-experiment step.

### 9. Design choices section (verbatim list)

- Single-file modification scope keeps agent interaction manageable
- Fixed time budgets enable direct experimental comparability
- FlashAttention-3 removed; native PyTorch SDPA with manual sliding window causal masking substituted
- `torch.compile` MPS-incompatible paths disabled
- No distributed training or complex configurations required
- Metric-driven: `val_bpb` (validation bits per byte) for vocabulary-size-independent comparisons

### 10. Credits section (verbatim list)

- Original autoresearch: Andrej Karpathy
- macOS/MPS adaptation: miolini/autoresearch-macos
- Dataset: merve/folk-mythology-tales

**Note**: Thu Vu credits BOTH the upstream methodology AND the intermediate macOS adapter. This is **CORPUS-FIRST explicit intermediate-adapter attribution** in v60+ window (typical Karpathy-derivative attribution credits only Karpathy; miolini intermediate-layer credit is unusual + supplies the audit-trail evidence for Pattern #57 sub-variant 57g).

### 11. License section

**README declares**: *"License: MIT"*

**GitHub API reports**: `license: None` (verified via api.github.com/repos/thu-vu92/autoresearch_folktales 2026-05-20)

**No LICENSE file** present in repo's root-level file list (verified via WebFetch of repo tree).

→ **Pattern #83 sub-mechanism 83f N=4 strengthening evidence**: README declares MIT, but no LICENSE file exists + GitHub API cannot detect license format. Identical pattern to:
- v74 LLMs-from-scratch (CITATION.cff "Apache-2.0" vs LICENSE.txt modified Apache) — 83f.1 within-LICENSE mismatch
- v76 agent-skills-standard (README "MIT" vs LICENSE Apache-2.0) — 83f.2 across-doc-LICENSE mismatch
- v77 easy-vibe (CC BY-NC-SA 4.0 README vs GitHub API "None") — 83f.3 across-doc-API mismatch
- **v79 autoresearch_folktales (README "MIT" vs GitHub API "None" + no LICENSE file) — 83f.4 NEW sub-variant candidate: declared-in-README-but-no-LICENSE-file**

Pattern #83 sub-mechanism 83f was PROMOTION-LOCKED-IN at v77 with N=3 PROMOTION-LOCKED-IN. v79 = N=4 post-promotion strengthening with NEW sub-variant 83f.4 candidate (extends taxonomy 83f.1/83f.2/83f.3 → 83f.1/83f.2/83f.3/83f.4 4-variant).

### 12. Cross-wiki pattern intersections (Pattern Library pre-check)

| Pattern | Intersection | Status |
|---------|-------------|--------|
| **#57 corpus-recursive** | DIRECT — v9 Karpathy autoresearch parent + nanochat citation + miolini intermediate adapter | **PRIMARY (57g NEW sub-variant)** |
| **#83 sub-mechanism 83f** | README "MIT" vs GitHub API "None" + no LICENSE file | N=4 post-promotion strengthening; NEW 83f.4 sub-variant candidate |
| **#84 sub-typology 84d NEW candidate** | Apple Silicon MPS port = hardware-substrate-portability | PROVISIONAL N=1 |
| **#66 minimal-dependency** | Pyproject.toml is the only dependency file + agent CANNOT install new packages | within-pattern strengthening |
| **#52 velocity** | 1.19 stars/day = LOW; not applicable to viral sub-class | N/A |
| **#45 NEW sub-typology 45f candidate** | README-Declared-MIT-without-LICENSE-file | OR Pattern #29 absent-LICENSE strengthening |
| **#19 sub-mechanism 19j NEW candidate** | Vietnamese-Diaspora-Data-Scientist-YouTuber-with-LLM-derivative-experiments | PROVISIONAL N=1 |
| **#18 sub-archetype #9 NEW candidate** | agentic-research-framework-with-constraint-architecture | PROVISIONAL N=1 |
| **#21 SDD-related** | NO — autoresearch is research-loop not SDD-methodology | N/A |

### 13. Absences (counter-evidence + null observations)

**Notable ABSENCES from README**:
- **No CLAUDE.md / AGENTS.md** at root — `program.md` is the agent skill, not the typical claude-code-format `.claude/CLAUDE.md` convention
- **No multi-harness support** — Claude Code + Mistral Vibe mentioned, but no `.cursor/` `.gemini/` `.codex/` directories (compare to v75 impeccable 14-harness or v76 agent-skills-standard 10+-harness CLI-generated)
- **No supply-chain disclosure** beyond MIT-declaration — no `SECURITY.md`; no Pattern #66 explicit supply-chain-discipline-at-velocity (compare to v78 ECC `ecc-agentshield` + Prompt Defense Baseline)
- **No i18n** — EN-only README (no VN README despite author's likely Vietnamese-diaspora identity); compare to v76 + v77 + v78 which all had VN/i18n locales
- **No tests/** directory — research-experiment repo; testing-via-agent-loop is the testing philosophy
- **No documentation site** — no docs/ dir, no GitHub Pages, no MkDocs
- **No prompt-injection defense baseline** — only generic agent guidance via program.md; no explicit Prompt Defense Baseline per v78 ECC discipline
- **No release/changelog discipline** — no GitHub Releases, no CHANGELOG.md

### 14. Counter-evidence flags + retroactive correction signals

**No retroactive corrections triggered**: v79 evidence does NOT contradict any prior wiki's Pattern Library register.

**1-wiki rapid-evolution check (v2.2 NEW)**: v78 just registered 57f sub-variant candidate (anchor-self-reference) PROVISIONAL N=1. v79 adds 57g sub-variant candidate (derivative-chain via intermediate adapter) PROVISIONAL N=1. This is **2-wiki consecutive Pattern #57 sub-variant accumulation** = Library-vocabulary item #10 1-wiki-rapid-pattern-evolution observational track strengthening at sub-variant-layer (distinct from prior item #10 instances at top-level-pattern-layer).

### 15. Phase 4b PRIMARY pre-registration confirmation

Pre-registered at Phase 0: **Pattern #57 NEW sub-variant 57g candidate "Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter"** PROVISIONAL N=1 registration.

**Cluster 1 confirms**:
- Karpathy = source-celebrity (corpus-foundation individual, v9 corpus subject)
- miolini = explicit intermediate adapter (corpus-first attribution evidence)
- Thu Vu = second-order derivative author (this wiki subject)
- Methodology preserved verbatim (`program.md`); architectural changes localized to `train.py` for MPS support
- All 4 source-celebrity-derivative-distillation criteria PASS (author ≠ source; explicit URL attribution; public observations; installable artifact packaging)

→ Phase 3 Entity 3 = Pattern #57 57g PRIMARY entity (most-referenced cross-link target).
