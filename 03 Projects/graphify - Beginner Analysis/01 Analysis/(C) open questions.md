# (C) Open Questions — graphify

## Q1-Q10 from Phase 0

1. Why `graphifyy` (double-y) on PyPI? Branding vs naming collision?
2. What is penpax.ai product? Sister project / commercial overlay?
3. Is v4 branch the default? Are there v1/v2/v3 historical branches?
4. How does Leiden clustering choose community count k?
5. What's the LLM cost tradeoff on first run vs cache reuse?
6. What tree-sitter grammars are shipped vs fetched dynamically?
7. Is there a Storm Bear vault test — does graphify handle Obsidian-style wikilinks?
8. How does `--update` detect changed files? Mtime vs hash?
9. What's the storage footprint per 1K files?
10. Is the knowledge graph portable between machines / team members?

## Q11-Q20 new at Phase 2

11. What's the MCP server auth model? (Any access control?)
12. How does confidence scoring work for INFERRED edges? Probabilistic threshold?
13. Are there rate limits on Claude vision calls for image extraction?
14. How does `--wiki` handle circular references in community graphs?
15. Does `--watch` mode handle renamed files correctly?
16. What's the behavior on extremely large files (>100MB)?
17. How does graphify handle private/secret content detection?
18. Is the Neo4j export Cypher or APOC-compatible?
19. Does `--obsidian` generate proper wikilinks or just flat markdown?
20. What's the extraction quality on non-code multimedia (e.g. whiteboard photos)?

## Q21-Q30 strategic

21. Is safishamsi considering commercial offering (penpax.ai pricing)?
22. Will graphify support non-Claude vision (Gemini / GPT-4V / LLaVA)?
23. What's the roadmap for multi-repo graphs?
24. Team/collab features planned?
25. Enterprise features (SSO, audit logs)?
26. How does graphify compare with Cursor's built-in code indexing?
27. Is there benchmark methodology published for 71.5x claim?
28. What datasets were used for benchmark reproducibility?
29. Has Karpathy engaged with the project (GitHub interactions)?
30. How does graphify output integrate with Claude Code Projects feature?
