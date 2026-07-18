# (C) wardrobe — Deep Dive

> LLM-wiki subject **v217** · built 2026-07-18 · INLINE + fully hand-verified (no workflow / no subagent — the ~205K shim overflows subagent context → prompt-too-long, the v200→v216 self-throttle). Source hand-fetched (repo page + README + the `extract-clothing-cutouts` gist); identity + landscape by WebSearch; collision by sanity-anchored hand-grep. **⚠️ NOT source-cloned** (WebFetch/README/gist/landscape-verified only — flagged).

---

## 1. One-line

`tandpfun/wardrobe` — **"Your clothes, extracted and organized with gpt-image."** A personal, local-first **AI web app** (Vite + Node 22, MIT) that points **OpenAI's Vision + gpt-image** models at photos of you wearing clothes: it **detects each garment**, **reconstructs a clean transparent-PNG "catalog cutout"** of it, optionally **renders a modeled editorial preview** on a reference model of you, and stores everything in a **local JSON database + images** you edit by drag/drop/paste/approve/regenerate. It also ships **two Codex agent skills** (`$import-clothes` / `$generate-outfits`) so OpenAI's Codex agent can drive the import + outfit-generation loop from the CLI.

**The corpus's FIRST personal-fashion / AI-wardrobe-cataloging DOMAIN subject, and its first OpenAI-employee-authored subject** (author works on robotics at OpenAI — a disclosed *individual*, NOT the org, NOT Anthropic).

---

## 2. Identity, provenance, metrics

| Field | Value (page/web-stated) |
|---|---|
| Repo | `github.com/tandpfun/wardrobe` |
| Tagline | *"Your clothes, extracted and organized with gpt-image."* |
| Author | **Thijs Simonian** — GitHub `tandpfun`, X `@cdngdev`; web-stated: Stanford student, full-stack dev, **works on robotics at OpenAI**. Announced open-sourcing on X (`@cdngdev`). |
| License | **MIT** |
| Language | **JavaScript 74.3% / CSS 25.1% / HTML 0.6%** (Vite frontend, Node ≥22) |
| Stars / forks / releases | **~915★ / ~133 forks / 0 releases** (page-stated §37.4 → **NOT #52**) |
| Trendshift | #84145 |
| Backends | OpenAI **Vision** (default reportedly `gpt-5.6-sol`, configurable) + **gpt-image** (image generation), both env-configurable |
| Storage | Local `data/` — JSON database + generated images; a `data/model-reference.png` reference photo of the user |
| Agent interface | **Codex skills** `$import-clothes` + `$generate-outfits` (OpenAI's Codex agent, not Claude); plus a **web UI** with BYO API key |

⚠️ **§41 identity discipline:** the author is a *disclosed individual who works at OpenAI* — a competitor lab, not Anthropic. His employer does not rescue criterion (a); §41 answers the disclosed-individual (a)-axis NO. First `tandpfun` / Thijs-Simonian author in the corpus (#19 19a data-point).

---

## 3. What it actually does (the pipeline)

The value is a **multi-stage vision-extraction + image-generation pipeline** wrapped in a local web app and an agent skill. From the repo README + the published `extract-clothing-cutouts` gist, the flow is:

**Import (per photo):**
1. **Source discovery** — normalize input photos (from the web upload or `~/Pictures/outfits`) into high-quality JPEG working copies with EXIF orientation applied.
2. **Detection / inventory** — an OpenAI **vision** call catalogs *every visible garment* (tops, bottoms, outerwear, footwear, accessories…) into a **structured JSON manifest** with **descriptions, confidence levels, and source references**.
3. **Generation references** — build padded crops around each target garment (preserve context, keep the garment dominant).
4. **Imagegen prompts** — construct **evidence-based** prompts that instruct **gpt-image** to *reconstruct the complete garment* while removing the wearer, body, under-layers, and background.
5. **Chroma-key extraction** — generate against a solid color key (default `#00ff00`), then remove it → a **transparent RGBA product PNG**.
6. **Quality assurance** — visual inspection against the source crop confirms identity, proportions, colors, construction details, and absence of artifacts; rejects failures and can regenerate.
7. **Deduplication** — *conservatively* merge only source-proven duplicates (avoid false matches from standardized AI poses).
8. **Store** — accepted PNGs → the local wardrobe, descriptive hyphenated filenames, entries in the JSON DB; intermediate artifacts deleted.

**Optional modeling / outfits:**
- The `$import-clothes` skill also **generates a modeled photo** of each item on the user's reference model.
- The `$generate-outfits` skill **composes outfit ideas from the catalog** and renders a **modeled lookbook**.

**Web UI:** drag / drop / paste photos, review the extracted items, edit/approve, regenerate; configure your own OpenAI key in the browser.

**The load-bearing design principle (from the gist):** *"prefer omission over invention"* — reconstruct **from visible evidence**, never guess hidden construction, unsupported branding, or unreadable text; treat obscured garments as reconstruction-from-evidence, not literal segmentation. Each catalog entry carries a **confidence** field, and a **QA visual-inspection gate** must pass before an item is accepted.

---

## 4. The two Codex skills (the agent-interface hook)

The repo bolts an agent interface onto the app via **OpenAI Codex skills** (the SKILL-file convention, Codex-flavored):

- **`$import-clothes`** — imports clothes from `~/Pictures/outfits`, runs the 8-stage extract-cutouts pipeline, creates modeled item photos, adds them to the wardrobe.
- **`$generate-outfits`** — creates modeled outfit ideas from the wardrobe and renders a modeled lookbook.

This is a genuine (if small, 2-skill) instance of the **agent-skills / SKILL.md pattern** the vault studies (agent-skills-standard v76, geti v213's first-party skill suite, TimesFM v193, agent-skills v184, ponytail v168) — here in its **product-ships-agent-skills-to-drive-itself** shape (the palmier-pro v192 / geti v213 / TimesFM v193 **agent-native-retrofit** thread, **SKILL vector**), but **Codex-flavored, not Claude**. It ships **no MCP server**.

---

## 5. Setup (documented, not cloned)

```
git clone https://github.com/tandpfun/wardrobe
cd wardrobe
npm install
cp .env.example .env          # add OPENAI_API_KEY
# place a PNG reference photo of yourself at data/model-reference.png
npm run dev                    # local dev server (Vite, ~:5173)
```

Env vars control the **vision model**, **image-generation model**, **quality**, and **data storage location**; `OPENAI_API_KEY` is mandatory. The importer stays **disabled** until the key + `data/model-reference.png` are present. Requires **Node 22+**.

---

## 6. Honest caveats

- **⚠️ NOT source-cloned** — this Deep Dive is built from the rendered repo page + README + the `extract-clothing-cutouts` gist + landscape/identity search, per the shim self-throttle. Line-level engineering (exact file layout, the JSON schema, the QA loop implementation) is README/gist-stated, not code-verified.
- **The hard AI is upstream** — wardrobe *orchestrates* OpenAI's Vision + gpt-image; it builds no model. The clever part is the pipeline discipline (evidence-based prompts, confidence, chroma-key, QA gate, conservative dedup), not novel AI.
- **Personal-project scope** — single-user, BYO-key, local-first, **0 releases**, ~915★. A polished, complete app *for its scope*, not a platform.
- **Domain is off both goals** — personal clothing/fashion is neither Claude/agents-for-software-dev (Goal #1) nor recruitment (Goal #2). Claude appears **nowhere**; the models are OpenAI's, the agent is Codex.
- **NOT world-first** — "AI wardrobe / virtual closet cataloger" is a heavily populated genre (Acloset, Google Photos Wardrobe, Pocket Wardrobe, Scenario Wardrobe Extractor, SELION, Whering + the GitHub `wardrobe-app` topic + other `Wardrobe` repos SwordPuffin/nadams019). The "detect-every-item → clean product image → structured catalog" pipeline is the commodity feature of that whole category.
- **Data egress + image privacy** — your clothing photos **and a reference photo of yourself** are sent to OpenAI's API for vision + image-gen. A personal-image-privacy note, not a supply-chain one.

---

## 7. The transferable idea (the reason this is worth reading)

Strip the fashion domain and what remains is a clean, reusable **"vision model extracts N structured entities from an image into a confidence-scored JSON manifest, with an anti-fabrication discipline and a QA visual-inspection gate."** That is *exactly* the architecture hireui needs for **CV/résumé parsing** (Goal #2):

| wardrobe stage | hireui CV-parsing analogue |
|---|---|
| detect every garment in a photo | extract every candidate field (name / role / dates / skills) from a CV image/PDF |
| structured JSON manifest + **confidence** per item | structured candidate record + **confidence** per extracted field |
| **"prefer omission over invention"** | never invent skills/experience the CV doesn't show; leave low-evidence fields blank |
| **QA visual-inspection gate** vs the source crop | verify each extracted field against the source region before storing |
| conservative dedup (source-proven only) | dedup candidate records only on strong evidence |

This anti-fabrication + confidence + verify-against-source discipline echoes **career-ops v200**'s anti-fabrication rule and the vault's own verify discipline — a genuinely borrowable pattern, not a product to adopt.

---

## 8. Corpus placement (cross-refs)

- **Codex-ecosystem adjacency** — 3rd consecutive Codex-adjacent ship: **grok-build v215** (Grok's Claude-Code peer) / **Codex-Dream-Skin v216** (themes Codex Desktop) / **wardrobe v217** (ships Codex skills). A landscape data-point on the OpenAI-Codex agent ecosystem (a Claude-Code competitor peer).
- **Agent-native-retrofit watch axis (SKILL vector)** — TimesFM v193 + geti v213 (Claude/cross-harness) + wardrobe v217 (Codex, consumer app); a Codex-flavored consumer data-point (NO N-bump, NOT a mint).
- **Vision-extraction-to-structured-data thread** — PixelRAG v211 (screenshot RAG), OfficeCLI v206 (render-and-verify), markitdown v28 (doc→markdown), miai-iphone-ocr-server / miai-cv-matching (OCR / CV parsing). Wardrobe = the "detect entities in an image → structured JSON + generate derived artifacts" member.
- **Competitor-lab thread** — GLM-5 v176 (Zhipu), DeepSpec v186 (DeepSeek), grok-build v215 (xAI/SpaceXAI); wardrobe = an **OpenAI-employee's** personal project on the **OpenAI** stack (disclosed individual → (a) FAIL, not the org).
- **Anti-fabrication / evidence-based discipline** — career-ops v200; the vault's own verify rule.
- **hireui (Goal #2)** — the CV-parsing architecture template above.

**See the Verdict for the full (a)/(b)/(c)/(d) call, the NO-MINT reasoning, the streak/§35 bookkeeping, and the reviewable OFF-GOAL alternative. See the Pilot Methods Menu for how (little) to apply it.**
