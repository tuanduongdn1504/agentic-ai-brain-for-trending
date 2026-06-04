# The cost-displacement thesis — what each tool replaces, and the honest caveats

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (synthesis across all 8 items)
- Operator brief framing: "8 DevOps repos almost banned from existing — they silently cost enterprise software billions in revenue."

## The mapping (OSS → commercial tool it displaces)

| OSS tool | Category | Commercial tool displaced | Claimed cost (operator brief — UNVERIFIED) | License | Maturity |
|---|---|---|---|---|---|
| [[infisical]] | Secrets / PKI | HashiCorp Vault Enterprise | ~$22,000/yr per cluster | MIT core + `ee/` commercial | 27k★ mature |
| [[coolify]] | PaaS / deploy | Heroku, Netlify, Vercel | $25/dyno/mo; $19/user/mo | Apache-2.0 | 56k★ mature |
| [[buildah]] | Container build | (no SaaS — removes Docker daemon + root) | n/a (kills risk, not a bill) | Apache-2.0 | 8.8k★ mature |
| [[ctrlplane]] | Deploy orchestration | bespoke deploy scripts | n/a (kills toil) | **AGPL-3.0** | **146★ early-stage** |
| [[coroot]] | Observability/APM (eBPF) | Datadog / instrumented APM | — | Apache-2.0 | 7.7k★ mature |
| [[dozzle]] | Live container logs | Elasticsearch+Kibana / Loggly / Papertrail | — | MIT | 13k★ mature |
| [[groundcover-caretta]] | eBPF K8s service map | Datadog | ~$23/host (for the Groundcover *product*) | Apache-2.0 | **2k★, ~15mo stale** |
| [[dockprom]] | Metrics stack (glue) | (assembles free OSS — kills setup time) | n/a | MIT | 6.5k★ mature |

## How they compose into a self-hosted DevOps stack
- **Build:** [[buildah]] produces rootless OCI images.
- **Secrets:** [[infisical]] injects credentials into build + runtime.
- **Deploy:** [[coolify]] (simple, all-in-one PaaS for small fleets) **or** [[ctrlplane]] (policy/orchestration across many clusters/regions).
- **Observe:** [[coroot]] (eBPF full APM) and/or [[dockprom]] (exporter-based metrics) + [[dozzle]] (live logs). [[groundcover-caretta]] is a narrower, stale service-map alternative.

## The honest caveats (so this wiki doesn't oversell)
1. **"Free" = no license/SaaS fee, NOT zero cost.** You pay for servers (Coolify's own README says ~$4–5/mo per VPS) plus **your ops time** to install, secure, patch, back up, and stay on-call. For small teams that labor can exceed the SaaS bill the tool "saves."
2. **Pricing figures are unverified.** $22k Vault / $25 dyno / $19 user / $23 host are operator-brief numbers; vendor pricing changes and has tiers/free allowances. Verify current pricing before quoting these in a business case.
3. **Two tools have real adoption risk:** [[ctrlplane]] (146★, created 2024, **AGPL-3.0** network-copyleft) is early-stage; [[groundcover-caretta]] is ~15 months stale and is only a service-map (not the full Groundcover product). The other six are mature + actively maintained.
4. **Mixed/copyleft licensing matters:** Infisical's `ee/` features aren't free; Ctrlplane's AGPL-3.0 carries obligations if offered as a network service. "Open-source" ≠ "do anything for free."
5. **Scope boundaries:** Dozzle is live-tail (not log retention/search); Dockprom is glue (not a product); Caretta is a map (not APM). Match the tool to the actual job.
6. **"Almost banned" / "billions in lost revenue" is rhetoric**, not fact — these tools are openly published, widely starred, and several have *their own* paid Cloud/Enterprise tiers (Infisical, Coolify, Coroot, Groundcover). The OSS-vs-commercial relationship is coexistence + freemium, not suppression.

## Key Takeaways
- The list is a genuinely useful **self-hosting cost-reduction toolkit** — strongest where per-seat/per-host/per-dyno SaaS pricing scales badly (Infisical, Coolify, Coroot/Dozzle for many hosts).
- Decide per-tool on **TCO + maturity + license**, not on the "kill the enterprise bill" headline.
- For this vault's [[external|Storm Bear]] cost-discipline thread, the reusable insight: self-hosting trades a *predictable SaaS fee* for *variable ops labor + infra* — quantify both sides before switching.
- 6 of 8 are safe to pilot today; 2 (Ctrlplane, Caretta) need an explicit risk decision first.
