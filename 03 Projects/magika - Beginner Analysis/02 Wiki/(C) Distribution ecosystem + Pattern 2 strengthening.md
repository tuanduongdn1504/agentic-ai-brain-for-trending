# (C) Entity 2 — Distribution ecosystem + Pattern #2 corpus-most-multi-channel

> **Wiki #:** v44 | **Type:** Distribution / ecosystem entity | **Format:** 13-section canonical

## 1. What is this entity?

How magika is packaged and delivered across 5 language bindings and 6+ distribution channels — and how those deliverables integrate with industrial-scale consumers (Gmail + Drive + Safe Browsing + VirusTotal + abuse.ch).

## 2. Five-language multi-binding distribution

| # | Language | Package | Primary use | Maturity |
|---|----------|---------|-------------|----------|
| 1 | **Rust (CLI)** | `magika-cli` on crates.io | Production CLI (fastest); also embedded in Python wheels since v0.6.0 | Stable |
| 2 | **Rust (lib)** | `magika` on crates.io | Reusable library for Rust embedders | Stable |
| 3 | **Python** | `magika` on PyPI | Python API + CLI wrapper | Stable (v1.0.2 2026-02-27) |
| 4 | **JavaScript/TypeScript** | `magika` on npm | Node + browser (WASM model) | Experimental |
| 5 | **Go** | `github.com/google/magika/go` | ONNX bindings | **WIP** (per README) |

**Corpus-first observation:** 5-language-multi-binding-with-pre-compiled-binary-distribution. Python package since v0.6.0 ships platform-specific wheels embedding the pre-compiled Rust CLI binary; pure-Python wheel fallback available for unsupported platforms.

## 3. Six+ distribution channels (corpus-most-multi-channel)

| # | Channel | Install command | Target audience |
|---|---------|-----------------|-----------------|
| 1 | **pipx** | `pipx install magika` | CLI users (isolated env) |
| 2 | **pip** | `pip install magika` | Python developers |
| 3 | **brew** | `brew install magika` | macOS / Linux users |
| 4 | **curl installer (bash)** | `curl -LsSf https://securityresearch.google/magika/install.sh \| sh` | Unix power users |
| 5 | **powershell installer** | `powershell -ExecutionPolicy Bypass -c "irm https://securityresearch.google/magika/install.ps1 \| iex"` | Windows users |
| 6 | **cargo** | `cargo install --locked magika-cli` | Rust developers |
| 7 | **npm** | `npm install magika` | JS/TS developers |
| 8 | **Docker** | `Dockerfile` (pip-install-based) | Container users |

Grouping pip+pipx as single Python channel and bash+powershell as single installer-script channel → **6 distinct channels**. Ungrouped → 8 install paths.

**Either count is corpus-most-multi-channel**. Previous corpus entrants peak at 5 channels (pi-mono v36 monorepo lockstep / OMC v27 plugin-marketplace-plus-npm / crawl4ai v29 pip+Docker+CLI+FastAPI+browser).

## 4. dist-workspace.toml cargo-dist pipeline

From `dist-workspace.toml` (Rust cargo-dist 0.31.0):

- **CI:** GitHub Actions
- **Installers:** shell + powershell (auto-generated)
- **Target platforms (4):**
  - `aarch64-apple-darwin` (Apple Silicon Mac)
  - `aarch64-unknown-linux-gnu` (ARM64 Linux)
  - `x86_64-unknown-linux-gnu` (x86_64 Linux)
  - `x86_64-pc-windows-msvc` (Windows x86_64)
- **Install path:** `CARGO_HOME` (integrates with Rust toolchain)
- **`install-updater = true`** — installer includes self-update capability
- **`github-attestations = true`** — cryptographic build provenance (Sigstore-adjacent)
- **Tag namespace:** `cli` — CLI releases tagged `cli-vN.N.N` (separate from Python/JS packages)

**Observation:** cargo-dist with self-updating installer + GitHub Attestations = corpus-first Rust-tooling-with-cryptographic-provenance at outside-scope ML project. Reflects Google-Research-OSS security discipline baseline.

## 5. Hybrid Python-wheel + Rust-binary distribution

From `python/README.md`:
> "Beginning with version 0.6.0, the magika Python package includes a pre-compiled Rust-based command-line tool, replacing the previous Python version. This binary is distributed as platform-specific wheels for most common architectures. For unsupported platforms, a pure-Python wheel is also available, providing the legacy Python client as a fallback."

**Packaging topology (corpus-first hybrid):**
- Platform-specific wheels (Linux x86_64 / Linux aarch64 / macOS Apple Silicon / Windows x86_64) bundle Rust binary
- Pure-Python wheel fallback for unsupported platforms (uses Python ONNX runtime directly)
- `pip install magika` transparently picks correct wheel via pip's platform-detection

**Distinct from all 43 prior corpus wikis.** Pattern #2 Distribution Evolution strengthening observation.

## 6. Browser / WASM deployment

The JS bindings (`magika` on npm) use **TensorflowJS** to load the ONNX model in-browser:
- Full client-side inference (no server)
- Model served from `https://securityresearch.google/magika/` CDN
- Configurable via `modelURL` + `configURL` parameters for embedding
- `MagikaNode` vs `Magika` split (Node file-path loading vs browser URL-fetch)

**Web demo:** https://securityresearch.google/magika/demo/magika-demo/ — fully-local-browser-ML-inference corpus-first observation.

## 7. Industrial-scale consumers

Five named integrations:

| Integration | Role | Scale |
|-------------|------|-------|
| **Gmail** (Google internal) | Attachment file-type routing → security/content-policy scanners | Billions of attachments/week |
| **Google Drive** (Google internal) | Upload classification | Billions of uploads/week |
| **Safe Browsing** (Google internal) | URL-associated file classification | Billions of samples/week |
| **VirusTotal** (external consortium) | Classifier feed (malware research) | Millions of samples/day |
| **abuse.ch / Bazaar** (external malware research) | Malware sample classification | Thousands of samples |

**Aggregate claim (verbatim):** "processing hundreds billions samples on a weekly basis"

## 8. Pattern #2 Distribution Evolution — corpus-maximum strengthening

Pattern #2 has been strengthened across 43 prior wikis showing increasing distribution sophistication. Magika v44 establishes the **corpus-maximum** data point:
- 5 language bindings (previous max: 4 — pi-mono v36 monorepo)
- 6+ distribution channels (previous max: ~5 — crawl4ai v29 / pi-mono v36)
- 4 target-platform cross-compilation (Linux x86_64 / Linux ARM64 / macOS ARM64 / Windows x86_64)
- Self-updating installer + GitHub Attestations = unique discipline primitive

## 9. Pattern #17 variant 2 big-tech-curator — 5 data points

Google 2-entrant confirms variant 2 diversity:
- gws v13 — Google official corporate T4 (broad Workspace CLI)
- **magika v44** — Google Research outside-scope (narrow classifier)

Microsoft 3-entrant (v6 + v28 + v34) already established variant 2 at N=3. Google's 2nd entrant at v44 = **5th total data point for variant 2 = corpus-first confirmed-variant-at-5-data-points**.

## 10. Pattern #58 Branding Divergence OT — 3rd watch data point

`website/` (Svelte-based) + `website-ng/` (Astro-based next-gen) duality in repo = **Website-transition-within-same-repo sub-variant 58c** observational.

Pattern #58 OT prior observations:
- OMC v27 (branding vs package-name divergence)
- ruflo v42 (similar brand/version divergence)
- **magika v44 (website/ + website-ng/ Svelte→Astro migration-in-progress)**

**Status:** OBSERVATION-TRACK (episodic / case-by-case). Not promotion-ready (no structural pattern yet emerging).

## 11. Cross-references

- **Cluster 2:** Multi-binding + 6-channel distribution details
- **Cluster 3:** Governance + OpenSSF + CodeQL
- **Entity 1:** Core product (ML classifier)
- **Entity 3:** Pattern implications
- **Pattern #2:** Corpus-maximum distribution strengthening
- **Pattern #17 variant 2:** 5-data-point milestone
- **Pattern #58 OT:** 3rd observation watch

## 12. Storm Bear relevance

- **Direct utility:** magika via `pipx install magika` is zero-friction CLI — could verify file uploads in client Scrum-doc intake workflow
- **Composability:** magika → markitdown v28 → vault pipeline (classify-first, convert-second)
- **Observational:** corpus-maximum distribution sophistication as reference for any future Storm Bear OSS publication (multi-binding + multi-channel template)

## 13. Next action

- If Scrum-coach pipeline needs file-type validation: `pipx install magika; magika -r client_uploads/ --json | jq '.[] | .result.value.output.label'` in 5 minutes
- If building any OSS at scale: study magika's dist-workspace.toml as template for cargo-dist self-updating installer + GitHub Attestations
