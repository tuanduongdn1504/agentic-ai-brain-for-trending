# (C) GitNexus Open Questions

## About GitNexus framework

1. Is LadybugDB an Abhigyan-authored project or 3rd-party dependency? (Acknowledgments list it without attribution origin)
2. What's Abhigyan's academic affiliation? (CS student — which institution? Indian Institute of Technology? Assam University? Relevant for potential future Pattern #44 Academic-Lab extension.)
3. akonlabs.com: how old is the commercial entity? Pre-dates or post-dates GitNexus OSS launch?
4. Who else is on the akonlabs.com team besides Abhigyan? (founders@akonlabs.com uses plural)
5. What's the OSS-vs-Enterprise feature delta? README mentions PR Review + auto-wiki + auto-reindex + multi-repo + OCaml + priority-features as Enterprise-only
6. Discord member count? (2 Discords: community `MgJrmsqr62` + commercial `AAsRVT6fGb`)
7. Has GitNexus been listed in awesome-mcp-servers v31 directory? (85K-scale MCP directory)
8. How does 14-language support degrade at scale? Are there language-specific bugs?
9. Browser ~5K file limit: how does Storm Bear vault size (~32 wikis × ~10 files each = ~320 files) compare? Below limit, but what about Claude Code's own memory when indexing the indexed graph?
10. What's the relationship between `pi-gitnexus` community integration and pi.dev? Upstream or fork?
11. `gitnexus-stable-ops` (@ShunsukeHayashi) part of Miyabi ecosystem — is Miyabi a Japanese AI-agent community/framework? Potential future wiki?
12. Token efficiency claim — GitNexus says "reliable, token-efficient" AI assistance; is there a benchmark number? (Pattern #8 Research-Benchmark check)

## About the pattern-relevant observations

13. Is PolyForm Noncommercial 1.0.0 a first-time corpus observation, or have prior wikis had PolyForm? (Literature search needed — probably first based on manual check but verify)
14. How does PolyForm Noncommercial differ structurally from AGPL-3.0 + separate-enterprise-agreement (OpenHands v30) and Fish Audio Research License (fish-speech v20)?
15. Is "Indian-Regional-Archetype-T4" pattern-worthy? At what N does cross-tier regional become meta-pattern?
16. Abhigyan's 20 public repos — does he have companion GitNexus-adjacent projects, or is GitNexus his primary OSS contribution? (Companion-portfolio vs single-project archetype distinction for Pattern #17)
17. Sigstore-signed Docker + K8s policy-controller — first in corpus (verify) or has prior wiki shown it?
18. BM25 + semantic + RRF hybrid search — first in corpus? graphify v16 uses graph-topology clustering without embeddings.

## About Storm Bear applicability

19. Could GitNexus browser-UI be used to index Storm Bear vault as knowledge graph? (Vault = ~32 wiki folders × ~10 files each ≈ 320 files; well under 5K browser limit)
20. What would GitNexus extract from Storm Bear vault that `graphify` Python-local doesn't? (MCP integration = Claude Code could query vault structure via GitNexus MCP server)
21. PolyForm Noncommercial — does Storm Bear operator using GitNexus for personal Scrum-coaching practice count as commercial use? Need to read PolyForm text.
22. For Storm Bear vault-diagnostic (v27 HIGH bundle still pending), would GitNexus provide different/complementary insights vs direct Claude Code inspection?
23. If operator runs GitNexus on vault, what's the appropriate follow-on action? (Visualize cross-references? Find orphan wikis? Identify tightly-coupled pattern clusters?)

## About the wiki delivery

24. Phase 4a beginner guide: how prominent should PolyForm ethical framing be? (fish-speech v20 used ⚠️ warnings throughout; OpenHands v30 used milder framing; GitNexus is in between — PolyForm is standard license not custom-written, but commercial-gate is explicit)
25. Phase 4b T4 7-way: how to handle absence-of-observation (Indian-regional-at-T4 not-yet-pattern) without cluttering deliverable?
26. Should iteration log escalate v27 diagnostic HIGH bundle even more aggressively (now 9 sessions deferred)?
