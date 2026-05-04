# (C) Open Questions — shannon v45

## Product / scope

1. Is Shannon Lite's 96.15% XBOW benchmark hint-free result reproducible by external evaluators? (repo link provided: KeygraphHQ/xbow-validation-benchmarks)
2. What's the competitive landscape for AI-pentesting? (Bishop Fox AI / CodeShield / Nuclei AI-variants / Burp Suite extensions)
3. How does Shannon compare to traditional DAST tools (ZAP / Burp / Rapid7 AppSpider) on non-LLM-category vulns?
4. What's the planned roadmap for expanded attack-domain coverage? (Pro tier includes SAST/SCA/secrets; what new dynamic domains?)

## Commercial

5. Keygraph funding / investor rounds — any announced?
6. Who are the 2 founders (or N founders) behind Keygraph?
7. HQ location for Keygraph?
8. What's the Shannon Pro pricing model? (seat-based? repo-based? scan-volume?)
9. What's Tower (managed service) pricing vs self-hosted?
10. Total Shannon Pro customer count (3 cited: Optexity, Scowtt, Mesmer — more?)

## Technical

11. How is the Claude Agent SDK's `bypassPermissions` mode balanced against security risk? (Shannon reads untrusted codebases)
12. How does Shannon handle prompt-injection attacks from malicious target repositories?
13. What's the cost-per-scan at scale beyond $50/run stated? (Pro enterprise volume?)
14. Does Shannon Pro's CPG support all 14+ languages like GitNexus v33? Or narrower?
15. Self-hosted runner data-plane details: how are LLM API keys stored? (envelope encryption? HSM?)
16. What LLM providers are OFFICIALLY NOT supported? (mentioned non-Claude models may be unstable)
17. Reproducibility: how are prompts versioned across releases? (answer: `apps/worker/prompts/` per-release)

## Governance / legal

18. Why issues-only-no-PRs? (common at AGPL commercial startups to control contribution licensing?)
19. What's the AGPL derivative boundary for Shannon Pro? (Pro tier is separate commercial license per product line clarification)
20. Has Shannon been approved for regulated-industry auditing? (SOC 2 compliance scan generation mentioned)

## Ecosystem

21. Are there OSS competitors to Shannon Pro's business-logic invariant-fuzzer approach?
22. Does Shannon integrate with existing SIEM/SOAR tools?
23. GitHub PR scanning mentioned in Pro — native app or GitHub Action?

## Storm Bear / meta

24. Is Shannon relevant to Storm Bear if Storm Bear builds web-app product?
25. Could Keygraph's commercial playbook (OSS lead-gen + Pro tier + SOC 2 + managed service Tower) inform Storm Bear commercialization strategy?
26. Is shannon a precedent for Storm Bear ethical-product-positioning (authorization-required + AGPL-derivative + responsible-disclosure)?

## Pattern Library

27. Will a 2nd AI-pentester framework emerge in corpus? (N=2 would formalize AI-pentester T5 sub-archetype with more confidence)
28. Is dedicated-Pro-tier-documentation-file (like SHANNON-PRO.md 26KB) a future Pattern #31 sub-variant? (needs N=2)
29. Does Shannon's issues-only-no-PRs governance warrant observation? (N=1 observational; needs N=2 for pattern registration)
30. Is XBOW benchmark a Pattern #8 Research-Benchmark data point at pentesting-domain? (8th benchmark family; different from WebBench / SWE-Bench / ICLR / ACL / ICSE venues)
