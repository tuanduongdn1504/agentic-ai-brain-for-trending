# (C) PRIMARY — §C Library-vocab standalone: "Anti-Detect / Stealth Browser" (N=2)

**Filed:** v179 (2026-06-22) · **Status:** NEW §C standalone, **N=2** (NOT corpus-first) · **Counts:** 46/10 unchanged; §C surface ≈35 → ≈36

---

## The standalone

**Name:** *Anti-Detect / Stealth Browser — a purpose-built, fingerprint-spoofing browser delivered for automation (as opposed to a general browser-automation tool that treats stealth as one feature among many).*

**Defining axis:** a subject whose **primary reason to exist is fingerprint evasion** — it ships a browser (a real fork/build, not a plugin) whose anti-detection is **engineered into the engine**, and packages it for programmatic/automated use.

**Instances:**

| N | Subject | Author | Engine | Delivery | Anti-detect locus |
|---|---|---|---|---|---|
| 1 | **CloakBrowser** (v69) | CloakHQ (anonymous corp) | Chromium / ungoogled-chromium (+57 C++ patches) | **SDK + Playwright drop-in (CDP)** | compiled-binary patches + `--fingerprint-*` flags + `humanize=True` |
| 2 | **camofox-browser** (v179) | Jo, Inc (askjo.ai) | **Camoufox / Firefox** (C++-level spoofing) | **REST-API server + OpenClaw agent-plugin + token-efficient accessibility snapshots** | upstream Camoufox/Firefox C++ |

---

## Why N=2, not corpus-first N=1

CloakBrowser **v69** is recorded in `_state/03c` as the corpus's *"CORPUS-FIRST purpose-built-for-stealth subject"* — it holds priority. But that observation was a **v2.x phantom-count casualty**: it spawned observational candidates (OC-G…OC-J) and a Pattern #45 sub-typology, yet **was never registered as a §C standalone** (collision grep of `_patterns/06` confirms: no stealth/anti-detect-browser row exists).

This is **identically the codegraph v70 → codebase-memory-mcp v172 situation**, and is resolved the same way: rather than "re-register" (nothing is in the registry to re-register), **mint a NEW §C standalone and file it at N=2 to credit the un-registered first instance's priority** (the v172 critic's exact ruling).

## What camofox contributes (the N=2 facet — recorded, NOT separately minted)

- **Delivery shape:** an **agent-facing HTTP service** (REST + OpenClaw plugin + LLM-token-efficient accessibility snapshots with stable refs `e1,e2…`) vs CloakBrowser's **SDK/library** delivery. This is the goal-relevant facet (it's what makes camofox a Goal-#1 *agent tool*).
- **Engine:** **Firefox/Camoufox** vs CloakBrowser's **Chromium/ungoogled**.

Both are **within-species variations**. Minting a *separate* corpus-first standalone for "anti-detect browser **as agent server**" would be the **draw-the-circle-to-make-it-first** over-claim → declined. The agent-server facet is instead carried as an **adjacency cross-reference** to the agent-capability-layer cluster.

## DISTINCT FROM (adjacencies, not members)

- **browser-use v34 / Skyvern v24** — agent **browser automation**; stealth is one feature, not the reason to exist (the exact contrast CloakBrowser v69's entry draws).
- **Agent-Reach v174** (§C N=1) — multi-platform web/social **read+search** capability layer; *reads* content, doesn't drive a stealth browser to *act*.
- **crawl4ai v29** — LLM-friendly crawler/scraper **library**.
- **Scrapling v149** (Library-vocab #21) — undetectable **scraping library** + agent-tooling authoring chain (different layer: a library, not a browser).

## Promotion / maintenance

- **PROMOTION-ELIGIBLE to a CONFIRMED Library-vocab item at N=3** (a clean 3rd cross-author anti-detect *browser*). Do not promote without it (anti-inflation).
- **Stale/retire:** §C time-aware floor protects N=2 entries; first audit review at the next natural audit (~v180+, now overdue per the v167 deferred agenda).
- **Audit note:** reconcile against the §F tally; confirm CloakBrowser v69's priority is correctly credited here and not double-counted against its Pattern #45 45c registration (different axis — license structure, not the stealth-browser capability).
