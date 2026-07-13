# Publish → Google Cloud Run

## What's real (and genuinely good)

- **One-click Publish → Cloud Run.** Click Publish → *Deploy app on Google Cloud* → pick a project (or the Default Gemini Project) → *Publish your app* → live on a stable auto-scaling HTTPS endpoint (scales to zero when idle). No terminal. ([docs](https://ai.google.dev/gemini-api/docs/aistudio-deploying), [Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/ai-studio-to-cloud-run-and-cloud-run-mcp-server)).
- **API key stays server-side.** AI Studio provisions `GEMINI_API_KEY` as a **server-side secret**; it is never in client code, headers, or the DOM. This is a real security win and a **pattern worth harvesting** (pilot **B2**). ✅ first-party confirmed.

## The material omissions (video says "free, A-to-Z"; reality has edges)

- **Starter Tier is limited:** **2 free apps max** per account, **region LOCKED** after the first deploy, **no custom domain** (you get a `*.run.app` / `*.ai.studio` URL). Custom domain ⇒ upgrade to Standard + Load Balancer/managed cert (~$12–24/mo).
- **"Free" ends fast at real throughput.** Cloud Run free tier (2M req/mo + compute buckets) is generous, but the bundled **Firestore free quota** is small (≈20K writes/day, shared) and **exhausting any quota can pause the database** — a production spike = outage. Realistic production cost estimate: **~$50–200/mo** depending on candidate throughput.
- **AI Studio is the source of truth.** You can re-deploy from AI Studio, but if you edit the Cloud Run source directly and then re-publish from AI Studio, **your Cloud Run edits are lost**. There is **no documented container/Dockerfile export** — moving off Cloud Run means manual extraction + re-containerization.
- **Region ≠ data residency.** Selecting a region places the *workload* there, but Google's own docs note it does **not** by itself guarantee all associated data (logs, metadata) stays in-region; binding GDPR residency needs **Assured Workloads** (org-level, not Starter Tier). See [[pricing-privacy-data]].

## Why it matters for hireui

- **Great for a throwaway demo; wrong for production.** The one-click path is a legitimate **deploy-layer datapoint** to compare against the self-hosted [[../fullstack-docker-cicd/_index|fullstack-docker-cicd]] SSH-deploy path — that's pilot **B1**. But for hireui production: region-lock + no-custom-domain + AI-Studio-source-of-truth + no-container-export all collide with **GitNexus-first + `agent-*` branches + CI/CD**. Deploying hireui production via AI Studio→Cloud Run is a **fence** (D1); if Cloud Run is ever used for hireui, use `gcloud run deploy --source .` from Git with your own Dockerfile + CI/CD, **not** AI Studio's managed flow.
- **The server-side-key model** is exactly the [[../jasonlee-claude-mobile-app/_index|keys-never-client]] ADR — harvest it as reference architecture for hireui's first LLM feature (**B2**).

## See also
[[_index]] · [[github-import]] · [[pricing-privacy-data]] · [[../fullstack-docker-cicd/_index|fullstack-docker-cicd]]
