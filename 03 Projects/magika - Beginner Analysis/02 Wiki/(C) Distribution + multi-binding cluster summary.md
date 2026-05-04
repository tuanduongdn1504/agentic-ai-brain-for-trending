# (C) Cluster 2 — Multi-binding distribution + 6-channel ecosystem + integrations

> **Sources ingested:** `dist-workspace.toml` / `Dockerfile` / root directory layout / `rust/README.md` / `js/package.json` / `python/pyproject.toml` / `go/README.md` / `.github/workflows/*` (19 files)
> **Date:** 2026-04-24

## 1. Five-language multi-binding distribution

| # | Language | Package | Scope | Status |
|---|----------|---------|-------|--------|
| 1 | **Rust** | `magika` (lib) + `magika-cli` (bin) on crates.io | Primary CLI (since v0.6.0 Python package ships the pre-compiled Rust binary) + reusable library | Stable |
| 2 | **Python** | `magika` on PyPI | Python API + CLI wrapper (platform-specific wheels with Rust binary + pure-Python fallback) | Stable (v1.0.2) |
| 3 | **JavaScript/TypeScript** | `magika` on npm | Node + browser (WASM model) | Experimental |
| 4 | **Go** | `github.com/google/magika/go` | ONNX bindings | **WIP** |
| 5 | **Rust crate (lib-only)** | `magika` on crates.io | Library for Rust embedders | Stable |

**Corpus-first observation:** 5-language-multi-binding-with-pre-compiled-binary-distribution pattern (Python package embedding platform-specific Rust CLI wheels + pure-Python fallback for unsupported platforms).

## 2. Six distribution channels (corpus-most-multi-channel)

| # | Channel | Install | Target audience |
|---|---------|---------|-----------------|
| 1 | **pipx** | `pipx install magika` | CLI users (isolated Python env) |
| 2 | **pip** | `pip install magika` | Python developers |
| 3 | **brew** | `brew install magika` | macOS / Linux users |
| 4 | **curl installer script** | `curl -LsSf https://securityresearch.google/magika/install.sh \| sh` | Unix power users |
| 5 | **powershell installer** | `powershell -ExecutionPolicy Bypass -c "irm https://securityresearch.google/magika/install.ps1 \| iex"` | Windows users |
| 6 | **cargo** | `cargo install --locked magika-cli` | Rust developers |
| 7 | **npm** | `npm install magika` | JS/TS developers |
| 8 | **Docker** | `Dockerfile` bundled (pip-install-based) | Container users |

**Counting:** if we group pipx+pip as single Python channel, powershell+curl as single installer-script channel → 6 distinct channels. If we split all → 8. Either way, this is the **corpus-most-multi-channel observation** (exceeds claude-code-best-practice v34 etc.).

## 3. dist-workspace.toml (cargo-dist self-updating installer)

- **cargo-dist version:** 0.31.0
- **CI:** GitHub Actions
- **Installers generated:** shell + powershell
- **Target platforms (4):**
  - `aarch64-apple-darwin` (Apple Silicon Mac)
  - `aarch64-unknown-linux-gnu` (ARM64 Linux)
  - `x86_64-unknown-linux-gnu` (x86_64 Linux)
  - `x86_64-pc-windows-msvc` (Windows x86_64)
- **Auto-updater:** `install-updater = true` (installer includes self-update capability)
- **GitHub Attestations:** enabled (cryptographic build provenance)

## 4. Docker distribution (minimal Dockerfile)

```dockerfile
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base
WORKDIR /magika
RUN pip install magika
ENTRYPOINT ["magika"]
```

Simple Python:3.11-slim base + pip install + entrypoint. No multi-stage build optimization. Intended as reference, not production-hardened.

## 5. Nineteen GitHub workflow CI/CD primitives

| Workflow | Purpose |
|----------|---------|
| `cli-release.yml` | Multi-platform Rust CLI release (12.8 KB — largest) |
| `cli-latest.yml` | Latest CLI tag tracking |
| `codeql.yml` | Security scanning (CodeQL) |
| `docs-check.yml` | Docs CI |
| `github-issue-labeler.yml` | Automated issue labeling |
| `github-pages.yml` | GitHub Pages deployment (for docs/website) |
| `go-test.yml` | Go bindings CI |
| `js-check-import-scenarios.yml` | JS import compatibility (Node + browser + various module formats) |
| `js-docs-builder.yml` | TypeScript docs builder |
| `js-publish.yml` | npm publish |
| `js-test.yml` | JS unit tests |
| `python-build-and-release-package.yml` | Python package build + release (17.1 KB — 2nd largest; multi-platform wheel builds) |
| `python-test-published-package.yml` | Post-publish validation |
| `python-test-published-rc-package.yml` | Release candidate validation |
| `python-test-suite.yml` | Python unit tests |
| `rust-test.yml` | Rust unit tests |
| `scorecard.yml` | OpenSSF Scorecard |
| `website-test.yml` | Website CI |

**Observation:** This is the most CI/CD-heavy outside-scope project in corpus. 19 workflows cover: Rust + Python + JS + Go (4 languages) × build + test + release + publish (4 lifecycle phases) + security (CodeQL + OpenSSF Scorecard) + docs + website + automation (issue labeler). Reflects Google-Research-OSS governance discipline.

## 6. Industrial-scale deployment

| Integration | Role | Scale |
|-------------|------|-------|
| **Gmail** | File-type routing → security/content-policy scanners | Billions of attachments/week |
| **Google Drive** | File-type routing | Billions of uploads/week |
| **Safe Browsing** | File-type classification for URL-based file threats | Billions of samples/week |
| **VirusTotal** | Classifier integration (malware research community) | Millions of samples analyzed/day |
| **abuse.ch (Bazaar)** | Malware consortium classifier | Thousands of malware samples |

**Aggregate claim (verbatim from README):** "processing hundreds billions samples on a weekly basis"

This is **industrial-deployment-scale** distinct from **community-viral-scale** (the latter is star-count-based corpus metric). Within-Pattern-#27 observational sub-distinction.

## 7. Platform-specific wheels (Python)

Python package distribution notes (from `python/README.md`):
> "Beginning with version 0.6.0, the magika Python package includes a pre-compiled Rust-based command-line tool, replacing the previous Python version. This binary is distributed as platform-specific wheels for most common architectures. For unsupported platforms, a pure-Python wheel is also available, providing the legacy Python client as a fallback."

**Pattern observation:** Python-wheel-embeds-Rust-binary + pure-Python-fallback = corpus-first hybrid distribution pattern. Distinct from pure-Python (most of corpus) and pure-Rust (gws v13).

## 8. Web demo via TensorflowJS (JS bindings)

- Browser demo at `https://securityresearch.google/magika/demo/magika-demo/`
- Uses TensorflowJS to load ONNX model in browser
- Runs entirely client-side (no server inference)
- WASM model file served from website URL
- Configurable via `modelURL` + `configURL` parameters for embedding

**Corpus-first observation:** Fully-local browser-ML-inference-for-OSS-security-tool. Distinct from LlamaFactory v22 (training only) + fish-speech v20 (requires heavy infra for inference).

## 9. Node.js bindings split (MagikaNode vs Magika)

From `js/README.md`:
- **`MagikaNode`** — loads ONNX model from local filesystem (Node context)
- **`Magika`** (browser) — loads ONNX model from URL (fetch-based)

Separate entry points via `magika/node` submodule import.

## 10. Shell scripts (Rust workflow automation)

From `rust/` directory:
- `changelog.sh` — changelog automation
- `color.sh` — shell library for colored output
- `latest.sh` — latest version tracking
- `publish.sh` — crates.io publication (generates merge-commit)
- `sync.sh` — library sync on new model release
- `test.sh` — test runner (used in CI)

Shell-automation-over-Python consistent with Rust project discipline (GitOps-via-shell).

## 11. Cargo-dist tag-namespace convention

`tag-namespace = "cli"` in `dist-workspace.toml` means CLI releases are tagged `cli-vN.N.N` rather than plain `vN.N.N`. This allows separate versioning of CLI vs Python package vs JS package — **multi-package monorepo with namespaced release tags** (similar to pi-mono v36 lockstep model but here explicitly decoupled per-language).

## 12. Pattern Library observations (Phase 2 per cluster)

1. **Pattern #2 Distribution Evolution** — 5-language-multi-binding + 6-channel distribution = **corpus-most-multi-channel observation**. Strengthens #2 with corpus-maximum data point.
2. **Pattern #17 variant 2 big-tech-curator** — Google 2-entrant (gws v13 + magika v44) for variant 2. Microsoft 3-entrant (v6 + v28 + v34). **Total variant 2: 5 data points (corpus-first confirmed variant at 5 data points).**
3. **Pattern #27 Community-Viral** — industrial-deployment-scale observational sub-distinction ("hundreds billions weekly at Google internal" is distinct from star-count community-viral).
4. **Pattern #31 Open-Core counter-evidence observation** — Google magika is fully-OSS-no-commercial-tier; does not invalidate #31 (which is about commercial entities with OSS+commercial split); observational.
5. **Pattern #58 Branding Divergence OT** — `website/` (Svelte) + `website-ng/` (Astro migration) = **3rd observation watch** after OMC v27 + ruflo v42. Website-transition-within-same-repo sub-variant 58c.
6. **Pattern #12 Governance-Depth** — 19 GitHub workflows + OpenSSF Best Practices badge #8706 + CodeQL + `.gemini/` + CLA + dependabot.yml + CODEOWNERS + scorecard.yml = Google corporate baseline at strong level.

## 13. Corpus-first observations (from cluster 2)

1. **5-language multi-binding at ML-classifier scope** (Rust + Python + JS + Go + WASM)
2. **6-channel distribution (pipx/brew/curl/pip/npm/cargo)** — corpus-most
3. **Python-wheel-embeds-Rust-binary + pure-Python-fallback hybrid distribution**
4. **dist-workspace.toml cargo-dist with self-updating installer + GitHub Attestations**
5. **Fully-local browser-ML-inference at Google Research OSS scale** (TensorflowJS + ONNX WASM)
6. **19 CI/CD workflows at medium-scale (16.6K stars) outside-scope project**

## 14. Cross-references

- Pattern #2 Distribution Evolution: reinforced at corpus-maximum with magika
- Pattern #17 variant 2: 5-data-point milestone (with gws v13)
- Pattern #42: cluster 3 handles peer-reviewed venue lineage
- website/ vs website-ng/ duality: Pattern #58 OT 3rd watch data point
- Python-wheel-embeds-Rust-binary: distinct from all 43 prior wikis (none used this distribution pattern)
