# (C) DeepTutor — Open Questions

> Questions surfaced during v38 wiki build. Some resolved via source reads; others parked for future iteration or operator discretion.

## Architecture

1. How does `ChatOrchestrator` route between `ChatCapability` (default) and deep capabilities (Deep Solve / Deep Question / Deep Research)? Source: `deeptutor/runtime/orchestrator.py`.
2. What is the exact relationship between `BaseTool` (Level 1) and `BaseCapability` (Level 2)? Can tools invoke capabilities? (source protocol files suggest uni-directional: capabilities call tools, not reverse).
3. Book Engine compiler.py 12.3K + engine.py 43.1K — what is the multi-agent pipeline? (outline proposal → source retrieval → chapter tree → page plan → block compile per 14 types).
4. How is persistent memory (Summary + Profile) implemented? SQLite? JSON? How is update frequency governed (every interaction vs batched)?
5. TutorBot Heartbeat system — how are reminders scheduled? Cron? APScheduler? Event-driven?

## Governance + maintainer

6. `@pancacake` is listed as the sole maintainer in CONTRIBUTING.md — what is the actual academic-lab team size at HKUDS contributing to DeepTutor? 48 GitHub contributors but lab composition (PhD students / postdocs / faculty) not disclosed publicly.
7. Relationship between DeepTutor and nanobot (HKUDS 40.7K-star sibling) — is nanobot an HKUDS project that predates DeepTutor, or was nanobot extracted from DeepTutor?
8. What is the role of `multi-user` branch? Multi-tenant deployment target, or experimental multi-user-session feature?
9. How is pre-commit-and-CI strict mode enforced? Which checks block PRs (Ruff / Bandit / MyPy) vs warn-only?

## arXiv + research

10. arXiv "Coming Soon" — which venue target (ACL / NeurIPS / ICLR / EMNLP)? Which year (2026 / 2027)?
11. Are there HKU PhD candidates / postdocs whose thesis work depends on DeepTutor? (Relevant for bus-factor and research-lineage observation.)
12. How does DeepTutor relate to HKUDS LightRAG EMNLP 2025 paper (confirmed academic publication)? Shared techniques / shared authors / complementary?

## Ecosystem-portfolio

13. Is HKUDS ecosystem-portfolio coordinated (shared roadmap / release cadence) or independent-project-parallel? README references 3 other HKUDS repos but integration pattern not clear.
14. LightRAG integration is on DeepTutor roadmap (🔜) — not yet integrated. How does timing affect cross-repo synergy?
15. CLI-Anything ("Making ALL Software Agent-Native") — is DeepTutor an example implementation of CLI-Anything methodology, or parallel development?
16. AutoAgent ("Zero-Code Agent Framework") vs DeepTutor agent-native architecture — different audiences or competing designs within same lab?

## VN + Storm Bear pilot

17. Does DeepTutor Vietnamese UI localization exist or planned? Currently 9-language README but UI i18n limited to `language: "en" | "zh"` in UnifiedContext. Could a VN UI PR be accepted?
18. Self-hosted deployment on consumer hardware (MacBook M1/M2) — realistic RAM + inference latency for DeepSeek + local-LLM (LM Studio / Ollama / llama.cpp)?
19. Copyright + knowledge-base legality — Storm Bear loading Scrum books (Agile Estimating and Planning / Scrum Guide / etc.) as private-KB — Apache-2.0 covers DeepTutor; book content is separate copyright. Any per-document licensing consideration?
20. TutorBot-as-VN-Scrum-coach — effort to build a Socratic Scrum Master persona via Soul Template + custom skills? Estimate: 2-4 weekends for Storm Bear operator.
