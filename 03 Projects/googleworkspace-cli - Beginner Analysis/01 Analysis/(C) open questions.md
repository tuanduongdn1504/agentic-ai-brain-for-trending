# (C) Open Questions — googleworkspace/cli

## Questions surfaced Phase 0

1. **Community channels** — no Discord/Slack in README. Where does community interact? GitHub issues only?
2. **Maintainer team composition** — not named. How many FTE at Google on this project?
3. **Pre-1.0 discipline** — 44 releases, aggressive churn. How often are breaking changes?
4. **Rust choice rationale** — why Rust not Go (Google's usual)? Performance? Distribution? Security?
5. **Dynamic Discovery overhead** — what's the cold-start cost to build clap tree from Discovery JSON?
6. **Model Armor availability** — is it Google Cloud paid service or free? Accessible outside GCP?
7. **Persona skills quality** — 10 personas is curated. How maintained? Updated when services change?
8. **Recipe skills completeness** — 56 recipes seems broad. Any SLA on breakage when APIs change?
9. **Enterprise vs consumer Workspace support parity** — Admin API is enterprise-only. Consumer-scope users?
10. **Headless/CI auth** — service account support mentioned. Domain-wide delegation works out of box?
11. **Breaking changes policy** — pre-1.0 is "expect breaking changes" per README. Formal deprecation windows?
12. **vs notebooklm-py** — googleworkspace/cli covers 11+ services but NOT NotebookLM. Why excluded? Is NotebookLM a Workspace service officially?
13. **OAuth scope "recommended" preset (85+)** — is this curated list published or dynamic?
14. **VN/multi-language docs** — zero non-EN READMEs. Google typically multi-lang. Will VN come?
15. **MCP support** — no MCP mention in README. Will this evolve to MCP-native?
16. **Relation to Apps Script** — Apps Script (gws script service) is covered. Does gws replace Apps Script or complement?
17. **Testing mode quotas** — "testing-mode apps limited to ~25 scopes". Production OAuth verification process?
18. **Storm Bear enterprise angle** — VN Google Workspace adoption is extensive. Pilot candidate for Scrum automation?
19. **Gemini extension vs Claude support** — Gemini has explicit extension; Claude CLAUDE.md is 1-liner pointer. Feature parity?
20. **Helper command anti-pattern** — README says "do not wrap single API calls". Does repository enforce this? PR reviews reject?
21. **Agent safety beyond Model Armor** — Model Armor is response sanitization. Prompt injection on input side?
22. **Pagination default 100ms delay** — why this default? Rate limit avoidance?
23. **Changeset tool** — JavaScript project infrastructure (changeset npm tool) on Rust project. Why?
24. **gws schema caching** — are Discovery Documents cached locally? TTL?
25. **Nix flake target audience** — Nix is niche. Why include? Google internal uses Nix?
