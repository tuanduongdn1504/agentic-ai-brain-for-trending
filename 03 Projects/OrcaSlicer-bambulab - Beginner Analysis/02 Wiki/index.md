# OrcaSlicer-bambulab — Wiki (v142, OFF-GOAL CAPTURE via 6th override)

> ⚠️ **Out-of-corpus-scope.** A 3D-printing slicer, force-built at operator election (STRICT Phase 0.9 = 0/4 SKIP → 6th lifetime override). Recorded as corpus-knowledge, NOT goal-#1 progress. No Pattern Library change.
> **Repo:** `FULU-Foundation/OrcaSlicer-bambulab` · AGPL-3.0 · C++ 82.5%.
> **§37 provenance:** ≈6.7k★ / 5.1k forks / latest release v1.0.0 dated 2026-05-12 (as of 2026-06, repo page — *stated, NOT API-verified; env mocks GitHub API*).

## What it is
A **fork of OrcaSlicer** (the open-source FDM 3D-printing slicer). README opener (verbatim):

> "This version of OrcaSlicer restores full BambuNetwork support for Bambu Lab printers. You are not limited to LAN only. It works over the internet just like before, through BambuNetwork, with full functionality for normal use and printing."

**The fork's entire value-add:** re-enabling **cloud/internet printing** to Bambu Lab printers via the proprietary **BambuNetwork** plugin — a capability the official OrcaSlicer keeps optional/gated (the BambuNetwork plugin depends on Bambu Lab's non-free libraries, and Bambu's 2025 firmware/auth changes restricted third-party cloud access). The team uses Claude Code internally to develop it (`.claude/commands`, `CLAUDE.md`, `AGENTS.md`) — but the **product has zero agent/Claude/MCP surface**; that scaffolding is internal engineering exhaust, not product function.

## OrcaSlicer — upstream / fork-lineage mapping (the "map related" ask)

```
Slic3r  →  PrusaSlicer  →  Bambu Studio  →  OrcaSlicer (SoftFever)  →  OrcaSlicer-bambulab (FULU-Foundation)
(Prusa-era      (Prusa Research)   (Bambu Lab's own        (community slicer,        (this fork — re-enables full
 origin)                            PrusaSlicer fork)        ~14.5k★, AGPL-3.0)        BambuNetwork cloud printing)
```

**Upstream OrcaSlicer** (`SoftFever/OrcaSlicer`, ~14.5k★, AGPL-3.0, C++ 76.4%):
> "G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.)"
- Maintained by **SoftFever** + community; grew well beyond its origins (also drew inspiration from SuperSlicer / Cura).
- Multi-vendor: supports Bambu, Prusa, Voron, Creality, etc. — not Bambu-exclusive.
- **The Bambu connectivity nuance:** OrcaSlicer's "Bambu networking plugin is based on **non-free libraries from Bambu Lab**" and is **optional** to OrcaSlicer. That optional/gated status is precisely what the FULU-Foundation fork sets out to "restore to full."

**How this fork relates to upstream:**
- It is a **downstream fork of OrcaSlicer** (one more node on the Slic3r→PrusaSlicer→BambuStudio→OrcaSlicer copyleft AGPL chain).
- It is **not** a general slicer improvement — its differentiator is the single concern of restoring **full internet/cloud BambuNetwork** printing (vs LAN-only), re-bundling/re-enabling the proprietary Bambu networking capability against the AGPL base.
- Interoperability / right-to-repair gray area (re-enabling vendor-gated cloud access). Benign-leaning; noted, not a safety issue.

## Tech
C++ 82.5% (+ CMake etc.); AGPL-3.0; desktop slicer (Windows/macOS/Linux per OrcaSlicer norms); latest release v1.0.0 (2026-05-12).

## Why it's in the corpus at all
Force-built via the **6th lifetime operator override** (v84+v116+v122+v127+v139+v142). It is **corpus-knowledge-of-an-outlier**, not goal-#1 progress, and **not a pilot**. See `01 Analysis/` for the 0/4 verdict + the override accounting (override-frequency re-trips 4-in-20).

## Corpus connectivity
- Only the incidental **"Claude-Code-as-internal-dev-tool exhaust"** thread (`.claude/`+`CLAUDE.md`+`AGENTS.md`) → N=3 with v122 dograh + v128 Echo Loop. An *observation* (the team builds with Claude Code), **not** product relevance.
- NO agentskills.io / MCP / skill / agent surface. NO Pattern Library mint.
