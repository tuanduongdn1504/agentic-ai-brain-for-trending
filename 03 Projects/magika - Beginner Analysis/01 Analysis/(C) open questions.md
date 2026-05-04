# magika open questions

> **Created:** 2026-04-24 (v44)
> **Format:** 20-30 questions to anchor wiki curation.

1. Is ICSE 2025 the first publication venue (conference) or was arXiv 2409.13768 preceded by another acceptance?
2. Which of the 12 authors are primary contributors to ongoing OSS maintenance vs paper-only co-authors?
3. How does Elie Bursztein's broader Google security-research portfolio relate to magika (graph-of-related-tools)?
4. What explains the 9 model-version evolution (v1 → v3_3 in ~3 years) — retraining cadence? dataset growth? architecture changes?
5. Why 216 content types in v3_3 (not 200+)? What drives the specific count?
6. Why does magika skip AGENTS.md / CLAUDE.md despite being Google-maintained? (Consistent pattern for outside-scope academic/ML tools)
7. Is the "hundreds billions samples per week" deployment scale number verifiable or is it PR-rounded?
8. What commercial alternatives exist at Google (internal-only models) vs the OSS magika?
9. What explains website/ + website-ng/ duality? Is this a Svelte-to-Astro migration-in-progress?
10. Does Go bindings WIP indicate delivery timeline or lower-priority maintenance?
11. How does magika's per-content-type-threshold system compare to libmagic (the classical Unix file(1) tool it aims to supersede)?
12. Is Gemini Code Assist config (.gemini/) a standard Google OSS discipline now or magika-specific?
13. What's the relationship between standard_v3_3 and the 2 special variants (fast_v2_1 + begonly_v2_1)?
14. Are there non-English content-type descriptions, or is "Python source" / "JavaScript source" EN-only?
15. Can magika be fine-tuned on private corpus (for e.g. internal company file type detection)?
16. What's the licensing posture on the 9 pre-trained model files — are they Apache-2.0 too or CC-BY or separate?
17. Does VirusTotal use magika as first-pass classifier or only for reporting?
18. How does abuse.ch (malware research consortium) integrate magika specifically?
19. What's the model's robustness to adversarial file-type spoofing (malware authors manipulating file headers)?
20. Why OpenSSF Best Practices badge project #8706 — what tier achieved?
21. Does CodeQL scan find security issues in Python+Rust+TS+Go+Svelte polyglot codebase or does each language use separate analyzers?
22. What's the TypeScript→ONNX→WASM pipeline for the web demo? How large is the WASM model?
23. Are prediction-mode thresholds (high/medium/best-guess) empirically tuned per content-type or uniform?
24. Why shell CI/CD scripts over Python (rust/scripts/*.sh)?
25. dist-workspace.toml cargo-dist suggests self-updating installer — security implications?
26. Is magika Google Project Zero–adjacent (Elie Bursztein's orbit) or independent security research?
27. What's the roadmap post-v1.0.2? (E.g., streaming classification, distributed inference, etc.)
28. Can magika classify inside containers (Docker layers, tar archives) or only top-level files?
29. Observational: does magika's "pure-OSS no-commercial-tier big-tech-research" archetype appear in other Google OSS (gws v13 also fits)? Is this a Google Research pattern?
30. Storm Bear relevance: is client-document-intake file-type-validation a realistic Scrum-coach pilot, or is magika observational-only?
