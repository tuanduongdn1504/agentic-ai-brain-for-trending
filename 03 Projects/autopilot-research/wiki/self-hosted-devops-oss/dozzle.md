# Dozzle — real-time web log viewer for containers

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 6)
- Repo: https://github.com/amir20/dozzle · Site: https://dozzle.dev
- Metadata (GitHub API, 2026-06-04): **13,169★** · Go (+ Vue frontend) · MIT · created 2018-10-30 · last push 2026-06-03 (very active)

## What it is
- A lightweight, **web-based real-time log viewer** for containers (Docker, Swarm, Kubernetes).
- Explicitly **does not store logs** — it's purely for live tailing. Tiny image (~7 MB compressed).

## What it replaces (operator claim)
- The heavy "just let me see the logs" use case otherwise served by Elasticsearch + Kibana / Loggly / Papertrail — without their infrastructure or cost.

## Key features
- Fuzzy container-name search; **regex** and **SQL-query** log search.
- Split-screen multi-log view; live CPU/memory stats; dark mode.
- Multi-user authentication + forward-proxy auth (e.g. Authelia).
- **Swarm mode** (global service) and **Agent mode** (monitor multiple Docker hosts).
- Works with Docker, Colima, and Podman (Docker Engine 19.03+ / API 1.40+).

## Honest scope limit (from the README — don't oversell it)
- "Dozzle doesn't support offline searching. Products like Loggly, Papertrail, or Kibana are better suited for full search capabilities."
- → Dozzle is **live-tail + recent-log viewing**, NOT log retention, archival, or historical search. It complements a logging backend; it doesn't replace one if you need history/compliance.

## Install
```bash
docker run --name dozzle -d \
  --volume=/var/run/docker.sock:/var/run/docker.sock \
  -v dozzle_data:/data -p 8080:8080 amir20/dozzle:latest
# → http://localhost:8080   (add --no-analytics to disable anonymous Google Analytics)
```

## Key Takeaways
- The lowest-friction tool of the 8 — one `docker run`, mount the socket, done. Highest "value per minute of setup."
- Right framing: it kills the cost of a logging stack **for live debugging**, not for log warehousing — know that boundary before retiring Kibana.
- MIT, mature, very active, tiny footprint → essentially zero adoption risk.
- Sits alongside metrics tools [[dockprom]]/[[coroot]] (logs vs metrics) and pairs naturally with [[coolify]]-hosted containers. See [[cost-displacement-thesis]].
