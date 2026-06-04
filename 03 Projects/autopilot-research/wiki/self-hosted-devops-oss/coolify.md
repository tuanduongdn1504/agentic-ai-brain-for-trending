# Coolify — self-hostable PaaS (Heroku/Netlify/Vercel alternative)

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 2)
- Repo: https://github.com/coollabsio/coolify · Site: https://coolify.io · Docs: https://coolify.io/docs
- Metadata (GitHub API, 2026-06-04): **56,420★** · PHP (Laravel) · Apache-2.0 · created 2021-01-25 · last push 2026-06-03 (default branch `v4.x`; very active)

## What it is
- Open-source, self-hostable **Platform-as-a-Service** — an alternative to Heroku / Netlify / Vercel.
- Manages your servers, applications, and databases on **your own hardware** (VPS, bare metal, Raspberry Pi) over just an SSH connection.
- Deploys static sites, databases, full-stack apps, and 280+ one-click services.

## What it replaces (operator claim — vendor figures unverified)
- **Heroku** ($25/dyno/month), **Netlify** ($19/user/month), **Vercel**.
- The pitch: "the ease of a cloud but with your own servers," unlimited apps, no per-dyno/per-user metering.

## How it works / why it's sticky
- **No vendor lock-in** — all app/database configs are saved *to your server*. If you stop using Coolify you keep your running resources (you lose the automations/UI, not the workloads).
- One Coolify control server + one-or-more resource servers is the recommended topology.

## Install
```bash
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash
# docs: https://coolify.io/docs/installation
```

## Cost reality check (important)
- Coolify itself is free (Apache-2.0). But the README states a server is **~$4–5/month** — so the true cost is the VPS, not $0.
- A paid **Cloud** version exists (managed Coolify + HA + email notifications + support) for those who don't want to self-host the control plane.
- Net: you remove Heroku/Netlify's per-unit SaaS fees; you take on VPS cost + ops responsibility.

## Key Takeaways
- The most popular repo of the 8 (56k★) and the headline "kill the PaaS bill" tool — strong, mature, actively developed.
- Biggest savings when you have *many* apps/sites (per-dyno/per-seat pricing scales badly); smallest benefit for a single tiny app.
- "Self-host = free" is a license claim, not a TCO claim — budget the server + your maintenance time (the README is honest about this).
- Pairs with [[infisical]] (secrets for deployed apps), [[dozzle]] (live logs of Coolify-run containers), and [[dockprom]]/[[coroot]] (monitoring). See [[cost-displacement-thesis]].
