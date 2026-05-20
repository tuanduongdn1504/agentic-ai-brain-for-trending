# (C) autoresearch_folktales — Hướng dẫn cho người mới

> **Subject**: [`thu-vu92/autoresearch_folktales`](https://github.com/thu-vu92/css/thu-vu92/autoresearch_folktales)
> **Wiki version**: v79 (FIFTEENTH under routine v2.2)
> **Storm Bear strength**: **STRONG INCLUDE 3/4** (a + c + d PASS; b FAIL)
> **Bilingual**: VN primary, EN technical

## Phần 1 — Đây là gì? (What is it?)

**Tóm tắt 1 câu (VN):** `autoresearch_folktales` là phiên bản fork của framework `autoresearch` (do Andrej Karpathy viết) — đã được Thu Vu (`thu-vu92`) chuyển sang chạy trên Apple Silicon Mac (M1/M2/M3/M4 với Metal/MPS) và huấn luyện lại LLM nhỏ trên dataset folk-mythology-tales (truyện dân gian thế giới).

**One-line (EN):** Apple Silicon (MPS) port of Karpathy's `autoresearch` framework, retrained on Hugging Face's `merve/folk-mythology-tales` dataset, preserving Karpathy's autonomous-agent research-loop methodology verbatim.

**Lineage 3 bước (3-hop chain)**:
```
Karpathy autoresearch  →  miolini/autoresearch-macos  →  Thu Vu autoresearch_folktales
(v9 corpus parent)        (intermediate adapter)         (v79 corpus subject)
```

→ Đây là **CORPUS-FIRST 2-hop codebase-derivative-chain via documented intermediate adapter** trong cửa sổ v60+. Pattern Library implications cụ thể (Pattern #57 NEW sub-variant 57g) → xem `01 Analysis/(C) Pattern-57-57g-... .md`.

## Phần 2 — Tín hiệu corpus-first / Corpus-first signals

**5 quan sát corpus-first (CORPUS-FIRST observations)**:

1. **CORPUS-FIRST Apple Silicon / MPS adaptation** trong cửa sổ v60+ (first corpus subject scoped exclusively to Apple Silicon)
2. **CORPUS-FIRST second-order derivative-chain of v9 corpus subject via intermediate adapter** (Karpathy → miolini → Thu Vu)
3. **CORPUS-FIRST folklore-mythology dataset as LLM training corpus** trong cửa sổ v60+ (Hugging Face `merve/folk-mythology-tales`)
4. **CORPUS-FIRST single-push-and-done activity profile** trong cửa sổ v60+ (repo created + pushed both 2026-04-24; no follow-up commits since)
5. **NEW CORPUS-RECORD-HIGH fork_ratio 0.484 = 48.4%** active-deployment-intent (exceeds v76 0.296 prior record by 1.64×)

**1 quan sát corpus-record** (CORPUS-RECORD): fork_ratio 15/31 = 0.484 — half of stargazers also forked = NEW HIGHEST active-deployment-intent signal trong 79-wiki corpus history.

## Phần 3 — Tier placement & Archetype

**Tier**: T3 Education — agentic-research-framework as pedagogical artifact

**Archetype**: solo-VN-diaspora-data-scientist-YouTuber (NEW Pattern #19 sub-mechanism 19j candidate; distinct from v76 HoangNguyen0403 VN-LOCATED archetype)

**Scale**: small (<5K stars; 31 stars at 26 days)

**Verified GitHub metadata (2026-05-20)**:
- stars: 31
- forks: 15 (fork_ratio 0.484 = NEW CORPUS-RECORD-HIGH)
- subscribers: 0
- open_issues: 0
- created_at: 2026-04-24
- pushed_at: 2026-04-24 (single-push-and-done)
- default_branch: `autoresearch/apr10`
- license: README says MIT; GitHub API says None; no LICENSE file in repo

## Phần 4 — Cài đặt nhanh (Quick installation)

**Yêu cầu (Requirements)**:
- Apple Silicon Mac (M1, M2, M3, hoặc M4) với Metal/MPS support
- Python 3.10+
- `uv` package manager (astral.sh tooling)
- AI coding agent (Claude Code hoặc Mistral Vibe)

**6-step setup (verbatim từ README)**:

```bash
# 1. Clone repo
git clone https://github.com/thu-vu92/autoresearch_folktales.git
cd autoresearch_folktales

# 2. Cài uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Đồng bộ deps qua uv
uv sync

# 4. Chuẩn bị dataset (chạy 1 lần)
uv run prepare.py

# 5. Chạy training baseline
uv run train.py
```

**Cài Claude Code** (nếu chưa có): theo hướng dẫn https://claude.ai/code.

**Khởi động autonomous agent**:
Sau khi setup xong, mở Claude Code trong repo này và gõ:
> *"Hi have a look at program.md and let's kick off a new experiment!"*

→ Agent sẽ tự đọc `program.md` và bắt đầu vòng lặp thí nghiệm tự động.

## Phần 5 — Cách sử dụng cốt lõi (Core usage pattern)

**Vòng lặp thí nghiệm 9 bước** (verbatim từ `program.md`):

1. Kiểm tra git state (branch + commit hiện tại)
2. Sửa `train.py` với 1 idea thí nghiệm
3. `git commit`
4. Chạy: `uv run train.py > run.log 2>&1` (KHÔNG dùng `tee` để tránh flood context)
5. Đọc kết quả: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. Nếu crash → đọc stack trace + thử sửa (tối đa "vài lần"; sau đó bỏ qua)
7. Ghi kết quả vào `results.tsv` (TAB-separated)
8. Nếu `val_bpb` giảm → **giữ commit, advance branch**
9. Nếu `val_bpb` bằng hoặc tăng → **git reset, bỏ commit**

**Output mỗi run** (verbatim từ training script):
```
---
val_bpb:          0.997900
training_seconds: 300.1
total_seconds:    325.9
peak_vram_mb:     45060.2
mfu_percent:      39.80
total_tokens_M:   499.6
num_steps:        953
num_params_M:     50.3
depth:            8
```

**Trên Apple Silicon (MPS)**: ~85-90 optimizer steps trong 5 phút (so với 1000+ steps trên GPU NVIDIA mạnh) → ~10× chậm hơn nhưng method được giữ nguyên (method-preserved-despite-throughput-collapse trade-off).

## Phần 6 — Khái niệm + lựa chọn kiến trúc mới mẻ (Novel concepts / key architectural choices)

**3-constraint architecture** (defining feature):

| Constraint | Định nghĩa (VN) | Why it matters |
|------------|------------------|----------------|
| **Single-modifiable-file** | Chỉ `train.py` agent được phép sửa; `prepare.py` + `program.md` + `pyproject.toml` read-only | Giới hạn cognitive load của agent; prevent runaway-scope thay đổi |
| **Fixed-5-min-time-budget** | Mỗi experiment chạy chính xác 5 phút wall-clock | Tất cả experiments so sánh trực tiếp được (apples-to-apples) |
| **Never-stop-autonomy** | Vòng lặp KHÔNG dừng cho đến khi human interrupt | Designed cho overnight unattended operation ("user goes to sleep") |

→ Đây là **Pattern #18 NEW sub-archetype #9 candidate "agentic-research-framework-with-constraint-architecture"** PROVISIONAL N=1 (v80 audit sẽ deliberate sub-archetype registration).

**Metric `val_bpb` (validation bits-per-byte)**:
- Đo loss per byte (not per token)
- Vocab-size-independent → cho phép so sánh fair giữa các thay đổi tokenizer + sequence-length + architecture
- Generalizable principle: "size-independent quality measure" — có thể apply rộng hơn ML

**Editorial judgment embedded in skill** (simplicity criterion verbatim):
> *"A 0.001 val_bpb improvement that adds 20 lines of hacky code? Probably not worth it. A 0.001 val_bpb improvement from deleting code? Definitely keep."*

→ Agent được instruct làm CURATOR có editorial judgment, không phải metric-maximizer thuần túy.

## Phần 7 — So sánh với các corpus framework khác (vs other corpus frameworks)

| Axis | v9 autoresearch (Karpathy) | v63 karpathy-skills (forrestchang) | v79 autoresearch_folktales (Thu Vu) |
|------|-----------------------------|-------------------------------------|-------------------------------------|
| **Relationship to Karpathy** | Original (corpus parent) | 1st-order public-tweet-observations distillation | 2nd-order codebase-derivative via miolini intermediate |
| **Form factor** | Python framework | Claude Code skill (`skills attach ...`) | Python framework with MPS adaptation |
| **Hardware target** | NVIDIA GPU (CUDA) | Any (skill-only, not training) | Apple Silicon MPS only |
| **Agent platforms** | Claude Code | Claude Code (skill consumer) | Claude Code + Mistral Vibe |
| **Dataset** | Web-text (original autoresearch) | N/A (skill, not training) | folk-mythology-tales (Hugging Face) |
| **Methodology preservation** | Source | Distilled tweets into skill | Verbatim preservation of `program.md`; train.py modified for MPS |
| **License** | (verify) | (verify) | README "MIT" + no LICENSE file (Pattern #83 83f.4 NEW sub-variant) |
| **Distribution surface** | git clone direct | Claude Code skill registry | uv-installable (single-tool-no-fallback) |

| Axis | v74 LLMs-from-scratch (Raschka) | v79 autoresearch_folktales (Thu Vu) |
|------|----------------------------------|-------------------------------------|
| **Tier** | T3 (Educational-Book-Companion) | T3 (Education / agentic-research-framework) |
| **LLM-training pedagogy** | Manning book companion code | Apple Silicon MPS framework |
| **Methodology preservation** | Print-book-constrained main + open-bonus folders | Verbatim Karpathy + train.py MPS modifications |
| **Hardware** | Multi-OS (uv + uv-pip 3-OS test matrix) | Apple Silicon MPS only (single-tool-no-fallback) |
| **License** | Apache-2.0 with Book-Content-Exclusion (45d NEW sub-typology) | README "MIT" + no LICENSE file (83f.4 NEW sub-variant) |

## Phần 8 — Ethical framing / Khung đạo đức

**Autonomy considerations**:
- `program.md` instructs the agent **NEVER STOP** until human interrupts → designed cho extended unattended operation
- Agent operates on `train.py` only → action-scope bounded
- Agent CANNOT install new packages → supply-chain risk bounded by `pyproject.toml`
- Agent runs experiments locally on user's Apple Silicon Mac → resource consumption visible to user

**Risks**:
- **Resource exhaustion**: agent có thể consume battery + system resources cho overnight (intentional design feature; not exploit)
- **Crash recovery cap**: "tối đa vài lần" attempts → agent có thể give up; user phải check progress
- **Output integrity**: `results.tsv` append-only; nếu agent record sai → no auto-correction
- **Dataset trust**: `merve/folk-mythology-tales` từ Hugging Face → kế thừa trust model của HF datasets hub

**Cautionary signals**:
- **No prompt-injection defense baseline** trong `program.md` (so với v78 ECC 6-axis Prompt Defense Baseline)
- **No SECURITY.md** trong repo
- **No supply-chain SBOM** / no signed releases / no signed commits

→ **Recommendation**: chạy local-only; không expose endpoints; verify dataset source nếu fork sang corporate work; treat all generated `train.py` code as untrusted-by-default + diff-review before any production use.

## Phần 9 — Storm Bear relevance (VN operator + Scrum coach fit)

**Storm Bear strength**: **STRONG INCLUDE 3/4** (a + c + d PASS; b FAIL)

| Criterion | Status | Tóm tắt |
|-----------|--------|---------|
| (a) Author-archetype peer | **STRONG PASS** | Thu Vu = solo-VN-diaspora-data-scientist-YouTuber (VN-given-name + VN-family-name + 10-year GitHub + bio "data nerd" + YouTube walkthrough creator); CORPUS-FIRST VN-DIASPORA distinction trong v60+ window (v76 was VN-LOCATED) |
| (b) Vault-deployable for Scrum | **FAIL** | LLM training framework; domain mismatch với Scrum coaching workflow; Apple Silicon hardware-pin |
| (c) Methodology-influence-node | **STRONG PASS** | Karpathy methodology lineage; "fixed-time-budget" + "single-modifiable-file" + "never-stop-autonomy" + "size-independent-quality-metric" could inform vault routine v2.2+ design |
| (d) Corpus-recursive | **STRONG PASS** | Direct 2nd-order derivative of v9 corpus subject `karpathy/autoresearch`; CORPUS-FIRST 2-hop derivative-chain via intermediate adapter |

**Methodological takeaways for vault**:
- **Fixed-time-budget per wiki-phase** (e.g., "5 phút scaffold + 20 phút Phase 2 cluster ingestion") — discipline-by-budget
- **Single-mutable-file architecture per wiki project** — explicit mutability matrix
- **Size-independent quality metric** — vault routine v2.2 could introduce "corpus-firsts per cluster-summary-line" or similar
- **Editorial judgment embedded in skill** — vault skills could explicitly embed simplicity criteria

**Spectrum positioning**:
- v79 (never-stop autonomy) ↔ v73/v77/v78 (session-handoff discipline) = OPPOSITE ENDS of autonomy-vs-handoff continuum
- Vault routine v2.2 currently aligns với v73/v77/v78 side; explicit acknowledgment của tension này có thể refine routine v2.3 codification

**Streak**: v79 extends Storm Bear meta-entity streak từ 14 (v65-v78) → **15 consecutive PASS post-v64-RESET = NEW CORPUS-RECORD extension by 1 wiki**.

## Phần 10 — 4-week learning roadmap

**Tuần 1: Setup + first run**
- [ ] Cài Apple Silicon Mac dev environment (Xcode CLI tools + Homebrew)
- [ ] Cài uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [ ] Clone repo + run baseline: `uv run prepare.py && uv run train.py`
- [ ] Đọc `program.md` + `README.md` đầy đủ
- [ ] Open `analysis.ipynb` trong Jupyter
- **Outcome**: baseline val_bpb established + workflow understanding

**Tuần 2: Manual experimentation**
- [ ] Tự sửa `train.py` (KHÔNG dùng agent) — đổi 1 hyperparameter
- [ ] Run + record kết quả vào `results.tsv`
- [ ] So sánh với baseline
- [ ] Lặp 5-10 manual experiments
- **Outcome**: hiểu được optimization-loop logic trước khi automation

**Tuần 3: Agent-driven experimentation**
- [ ] Khởi động Claude Code trong repo
- [ ] Gõ prompt: *"Hi have a look at program.md and let's kick off a new experiment!"*
- [ ] Đứng nhìn agent setup + run vài experiments
- [ ] Inspect `results.tsv` + git log sau session
- [ ] Học từ những thay đổi agent đã thử
- **Outcome**: hiểu agent's decision-making + intervention points

**Tuần 4: Methodology transfer**
- [ ] Đọc `karpathy/autoresearch` README để hiểu original design intent
- [ ] Đọc `miolini/autoresearch-macos` để hiểu intermediate-adapter contributions
- [ ] Compare với `karpathy/nanochat` (underlying training implementation)
- [ ] Synthesize: methodology principles có thể transfer sang domain khác (vault routine? Scrum process? code review automation?)
- **Outcome**: methodology-level takeaways độc lập với LLM-training domain

## Phần 11 — Tradeoffs + limitations

**Tradeoffs (intentional design choices)**:

| Trade-off | Reason | Cost |
|-----------|--------|------|
| MPS over CUDA | Apple Silicon accessibility | ~10× slower experiments (85-90 steps vs 1000s/5min) |
| Single-modifiable-file | Bounded agent scope | Cannot refactor `prepare.py` even when warranted |
| Fixed-5-min-budget | Fair comparison | Some valuable experiments need longer training |
| Never-stop autonomy | Overnight unattended | No safety net for runaway costs / bugs |
| 5-min time-budget | All experiments comparable | Variability from system load not normalized |

**Limitations**:
- **Single dataset**: folk-mythology-tales only; cần fork để thử dataset khác
- **No multi-device**: cannot scale to multi-GPU
- **No production deployment**: research-experiment artifact; output là training-loss insights, not deployable model
- **No CI / no tests**: agent-loop là testing philosophy; manual review still required
- **EN-only**: no VN/CJK README despite VN-diaspora author identity

## Phần 12 — Caveats + safety notes

**Supply-chain awareness**:
- README declares "MIT" but no LICENSE file in repo + GitHub API reports `license: None` → license enforceability uncertain trong commercial settings
- Dataset (`merve/folk-mythology-tales`) inherits Hugging Face datasets-hub trust model — verify-before-trust nếu used in production
- No SECURITY.md / no SBOM / no signed releases / no signed commits
- agent's `train.py` modifications happen on local machine → review diffs before commit-or-deploy if used in shared context

**Agent autonomy considerations**:
- "NEVER STOP" directive means agent will burn local resources until interrupted
- No built-in cost-tracking → user must monitor energy / battery / disk
- Crash-handler caps at "vài lần attempts" → agent may give up without notifying user
- Single-push-and-done activity profile (last push 2026-04-24) → maintenance status unclear; report bugs to fork-owner if encountered

**Vault operator-specific notes**:
- If Storm Bear adopts methodology takeaways → cite Karpathy + Thu Vu attribution chain
- Methodology takeaways are GENERALIZABLE PRINCIPLES; specific implementation details (Python + MPS + val_bpb) are domain-specific
- Compare to v73/v77/v78 session-handoff disciplines — autoresearch lies at OPPOSITE END of the autonomy-handoff spectrum

## Phần 13 — Tài liệu tham khảo + Bước tiếp theo

**External references** (từ README):
1. [Karpathy autoresearch](https://github.com/karpathy/autoresearch) — v9 corpus parent
2. [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) — intermediate adapter
3. [Karpathy nanochat](https://github.com/karpathy/nanochat) — underlying training implementation
4. [merve/folk-mythology-tales dataset](https://huggingface.co/datasets/merve/folk-mythology-tales) — Hugging Face source
5. [YouTube walkthrough](https://www.youtube.com/watch?v=XXR0zZ0_16M) — Thu Vu's video tutorial
6. [Claude Code](https://claude.ai/code) — recommended AI agent
7. [Mistral Vibe](https://mistral.ai) — alternative AI agent
8. [uv documentation](https://docs.astral.sh/uv/) — packaging tool docs

**Cross-wiki sibling references**:
- v9 [autoresearch (Karpathy)](../autoresearch%20-%20Beginner%20Analysis/) — DIRECT PARENT methodology
- v63 [andrej-karpathy-skills (forrestchang)](../andrej-karpathy-skills%20-%20Beginner%20Analysis/) — 1st-order Karpathy-derivative sibling
- v74 [LLMs-from-scratch (Raschka)](../LLMs-from-scratch%20-%20Beginner%20Analysis/) — T3 tier-peer + corpus-second-foundation-individual after Karpathy
- v76 [agent-skills-standard (HoangNguyen0403)](../agent-skills-standard%20-%20Beginner%20Analysis/) — VN-LOCATED solo developer comparison (v79 is VN-DIASPORA)
- v78 [ECC corpus-recursive revisit](../ECC-v78-recursive-revisit%20-%20Beginner%20Analysis/) — Pattern #57 sub-variant accumulation arc sibling (v78 57f + v79 57g)

**Next action suggestions (cho Storm Bear)**:
1. **Read `01 Analysis/(C) Pattern-57-57g-... .md`** for the formal Pattern Library proposal-document
2. **Compare with v9 autoresearch's** wiki to see how Karpathy original was treated vs second-order-derivative treatment
3. **Decide v80 audit scope** — Pattern #57 57g sub-variant administrative addition (PROVISIONAL N=1) + Library-vocabulary item #10 strengthening at sub-variant layer
4. **Consider Library-vocabulary candidates from v79** — 10 NEW candidates identified (highest single-wiki count under routine v2.2)
5. **Reflect on autonomy-vs-handoff spectrum** — v79 represents OPPOSITE END from v73/v77/v78; explicit spectrum acknowledgment could refine routine v2.3 codification

**Bước cụ thể nếu Storm Bear muốn thử framework**:
- Vault operator có Apple Silicon Mac? → có thể chạy local
- Có time-budget overnight? → designed cho 100+ experiments while sleeping
- Có vested interest in LLM training learning? → high-relevance methodology
- KHÔNG có vested interest? → methodology-level takeaways đủ; không cần chạy

→ **Recommendation**: skip running; harvest methodological takeaways từ entity pages + cross-pattern coupled-design observations.
