# (C) browser-use — Open Questions

Questions surfaced during Phase 0/2/3 for later resolution or next-wiki investigation.

## About the project

1. Exact incorporation date + legal structure of Browser Use Inc./LLC (US or Switzerland)? Not disclosed in public repo.
2. Funding disclosure — is Browser Use VC-backed, bootstrapped, or funded by Cloud revenue? No TechCrunch/PitchBook visible from inside repo.
3. Team size beyond Magnus + Gregor — how many engineers + how many Zurich vs SF?
4. Does `bu-30b-a3b-preview` OSS model release imply broader open-weights strategy or one-off preview?
5. What fraction of 89.9K stargazers use Cloud vs OSS-local? Proxy: ChatBrowserUse API key adoption rate.

## About the architecture

6. Why `bubus` event bus instead of native asyncio + callbacks? Performance or testability rationale?
7. `cdp-use` vs Playwright native — what prompted forking CDP wrapper instead of adopting Playwright's existing CDP layer?
8. 5-watchdog architecture — were these observed emergent necessities, or designed up-front? (Architectural evolution signal)
9. Hybrid DOM+vision — what concrete tasks fail with DOM-only that screenshot-augmentation rescues? Benchmark decomposition needed.
10. `@sandbox` decorator — does it wrap local runtime or exclusively delegate to Cloud? (API design question)

## About the commercial model

11. Cloud pricing: per-session vs per-minute vs per-action? CLOUD.md mentions credits but no rate disclosure in public docs.
12. "15-minute session runtime limit" — is this technical (browser stability) or commercial (to push upgrades)?
13. Captcha-solving — is it ML-based internal, 3rd-party service (2captcha / Anti-Captcha), or undisclosed?
14. Proxies "residential" — who is the upstream residential-proxy provider (Bright Data / Oxylabs / own network)?
15. `browsermerch.com` — is it in-house merch operation or Shopify-delegated? Observational monetization signal.

## About Pattern Library impact

16. Pattern #47 refinement — should 3-point spectrum (vision-primary / hybrid / DOM-only) be formalized at v41 or wait for N=3 at each pole?
17. Pattern #48 promotion at N=2 — are there non-browser-agent domains where proprietary-anti-bot-commercial-moat pattern applies (e.g., scraping-as-a-service, bot-protection-on-other-domains)?
18. Pattern #46 un-stale — if promoted at N=2 structural, what are the sub-variant axes (engineering-background vs business/engineering mix; same-org-longstanding vs recent-co-founding)?
19. Should "bidirectional MCP server+client" become a candidate at N=2 once a 2nd corpus wiki is observed with bidirectional MCP? Currently watch-list.
20. Does browser-use at 89.9K MIT + Cloud invalidate v28 Microsoft markitdown variant-5 ecosystem-scale promotion logic? Different archetype (startup vs ecosystem-scale); should not conflict.

## About Storm Bear operator pilot

21. Can Storm Bear Scrum-coach use Browser-Use Cloud for 1-week evaluation under free-tier (5 free tasks) or immediately need paid credits?
22. Is there a Jira-MCP-server + browser-use-MCP-client combo that automates sprint-report generation without custom code?
23. Does browser-use Cloud session persistence (profiles) handle Atlassian SSO across Jira + Confluence + Trello?
24. What's the cost-per-sprint-report estimate (LLM tokens + Cloud session minutes) at Storm Bear scale (~10 clients × 2 ceremonies/week)?
25. Can `@sandbox` decorator run on GitHub Actions free-tier for scheduled retrospective-data collection?

## About corpus meta-implications

26. **30th consecutive Storm Bear meta-entity** — is round-number milestone worth formal documentation beyond standard Phase 0.9 per-wiki evaluation?
27. browser-use 4.2× larger than Skyvern at same T5+browser archetype — does scale-divergence within-archetype warrant pattern observation (archetype does not predict scale)?
28. 15+ LLM providers at T5 = most multi-provider-support in corpus. Does Pattern #28 have a scale-tier (bridge-level / framework-level / T5-application-level) sub-classification opportunity?
29. v27 diagnostic HIGH bundle now deferred 18 sessions. At what escalation point does operator-facing-backlog become hard-block?
30. 5 consecutive zero-new-candidate-registration wikis (v37/v38/v39/v40/v41) if v41 confirms — is this the new normal for corpus v41+ post-application-phase?
