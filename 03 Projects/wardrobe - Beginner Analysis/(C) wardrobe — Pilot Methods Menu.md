# (C) wardrobe — Pilot Methods Menu

> Subject **v217** `tandpfun/wardrobe`. **Blunt framing:** the DOMAIN (personal clothing catalog) is off both your goals, and Claude appears nowhere (OpenAI Vision + gpt-image + Codex). **There is nothing to pilot into hireui or the Claude/agents practice as a product.** The genuine, on-goal value is a **read-and-borrow**: the `extract-clothing-cutouts` skill's **vision → confidence-scored structured JSON → anti-fabrication → QA-gate** discipline is a near-perfect **hireui CV-parsing template (Goal #2)**. This menu is an honest ~14 methods (mostly read / borrow / fence), not a padded 24.
>
> **⭐ One-thing path: A1 → B5 → B6** — read the skill's 8-stage discipline (zero install) → write the hireui **CV-parsing ADR** on that shape → spec the first LLM CV-parsing feature on an `agent-*` branch. Everything else is optional.

---

## A — Read & learn (zero install, highest ROI)

- **A1 ⭐** Read the published `extract-clothing-cutouts` gist as an **agent-skill engineering exemplar**: an 8-stage evidence-based pipeline (source-discovery → structured-inventory-with-confidence → generation-crops → evidence-based-imagegen-prompts → chroma-key → **QA visual-inspection gate** → conservative-dedup → store), governed by **"prefer omission over invention."** ~15 min. This is the whole point of the wiki.
- **A2** Read the repo README for the **product shape** — a local-first AI app that pairs a **web UI (BYO key)** with **agent skills (`$import-clothes` / `$generate-outfits`)** so the *same* pipeline runs interactively *or* under Codex. Note the "app + agent-skill twin interface" pattern (the geti v213 / palmier-pro v192 agent-native-retrofit shape).
- **A3** Note the **Codex-ecosystem** placement — the 3rd consecutive Codex-adjacent corpus subject (grok-build v215 vendor peer / Codex-Dream-Skin v216 / wardrobe v217 ships Codex skills). A landscape data-point on the OpenAI-Codex agent ecosystem; nothing to adopt.
- **A4** Note the **anti-fabrication lineage** — "prefer omission over invention" + per-item confidence + verify-against-source echoes **career-ops v200** and the vault's own verify discipline. A durable cross-domain principle worth internalizing.

## B — Borrow into hireui (the real Goal-#2 play, zero product-adoption)

- **B5 ⭐** Write a **hireui CV/résumé-parsing ADR** on the wardrobe pipeline's shape:
  | wardrobe | hireui CV-parse |
  |---|---|
  | detect every garment | extract every field (name / role / dates / skills) |
  | structured JSON + **confidence** per item | candidate record + **confidence** per field |
  | **prefer omission over invention** | never invent skills/experience the CV doesn't show; blank low-evidence fields |
  | **QA gate** vs the source crop | verify each field against the source region before storing |
  | conservative dedup (source-proven) | dedup candidate records only on strong evidence |
  On an `agent-*` branch, per hireui's CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; no LLM spend yet → **design/spec only**).
- **B6 ⭐** Spec hireui's **first LLM CV-parsing feature** as a fixed, legible, audited path behind the RATIFIED candidate-LLM legibility ADR + the Mosh A2 vendor-seam (compose with **miai-cv-matching** + **PixelRAG v211** [screenshot-vs-OCR] + **OfficeCLI v206** [render-and-verify] + **career-ops v200** [scoring rubric]).
- **B7** Steal the **confidence + QA-gate + anti-fabrication** trio into any hireui feature that reads candidate content into structured data — the same discipline hardens against garbage-in and hallucinated extractions.
- **B8** Steal the **evidence-based prompt** habit (prompt the model to reconstruct *only from visible evidence*, remove distractors, flag what it can't see) into hireui's extraction prompts.

## C — Optional hands-on (off-goal, personal use only)

- **C9** If you actually want a digital closet: `install-snapshot` first (NOT source-cloned → can't vouch for `npm install` postinstall) → clone → `npm install` → `.env` with your OpenAI key → `data/model-reference.png` → `npm run dev`. **⚠️ Your clothing photos + a photo of yourself egress to OpenAI's API** — personal-image-privacy call.
- **C10** If you run it, watch the **cost** — every import is vision + image-gen calls (gpt-image reconstruction per garment + modeled previews). BYO key, metered. Not free.
- **C11** Read what it writes locally (`data/` JSON DB + images) as a study of a **local-first structured-catalog store** — a clean, inspectable design.

## D — Vault-meta

- **D12** File wardrobe as a **corpus-knowledge data-point** on the Codex-ecosystem thread + the agent-native-retrofit SKILL vector (Codex-flavored, consumer-app; NO N-bump). Flag for the **~v221 audit**: the OpenAI-Codex agent ecosystem is now 3 consecutive ships — watch whether it becomes a cluster.
- **D13** Note the **NOT-world-first** landscape (populated AI-wardrobe genre) so the NO-MINT stands at audit.
- **D14** Record the **GA-vs-OFF-GOAL** judgment (both readings, streak both ways) for the operator to elect at audit.

---

## Fence (if you run it at all)

- `install-snapshot` before `npm install` (NOT source-cloned — can't verify postinstall) + `npm-security-check` the deps.
- BYO OpenAI key in `.env`, **never committed**; personal images egress to OpenAI → your privacy call (don't feed it anything you wouldn't send to OpenAI).
- Pin the commit (0 releases).
- **hireui borrows the PATTERN only** — never adopt the product; anything touching candidate data stays behind hireui's CONSTITUTION (I-2/I-8/GitNexus-first) + the candidate-LLM legibility ADR; no LLM spend yet → design/spec.
