# Open Questions — pi-mono wiki

**Wiki:** v1 (2026-04-23)

---

## Unresolved / deferred to later iterations

### 1. Is pi-ai deserving of its own dedicated wiki?

**Signal:** pi-ai is 20+-provider LLM abstraction built-in at T1 coding-agent scope. Pattern #28 Multi-Provider AI Support (CONFIRMED v25, N=6 data points) currently mixes abstraction-library-style (LiteLLM 100+ via TrendRadar v19 / crawl4ai v29) with DI-style (markitdown `llm_client` v28) and native-built-in (pi-ai v36). If a 2nd native-built-in-multi-provider-at-T1 emerges, Pattern #28 refinement to sub-variants will be useful — at which point pi-ai deserves isolated deep-dive for provider-by-provider detail.

**Defer-to-decision:** No action at v36. Flag for pattern-library mini-audit review of #28.

### 2. Is pi-pods its own archetype candidate?

**Signal:** pi-pods is "CLI for managing vLLM deployments on GPU pods" — GPU-infrastructure-for-agent-runtime. Currently N=1 in corpus (LlamaFactory v22 training-infra is T-infra-training, distinct from pi-pods T-infra-inference). Pattern candidate could be "Agent-Inference-Infrastructure Primitives" — but at N=1, consolidation-forward discipline rejects registration.

**Defer-to-decision:** Observational. If 2nd GPU-inference-infra tool emerges in corpus, register. For now, mention in Mario's ecosystem-portfolio entity.

### 3. Does Mario's cross-domain founder equity (libGDX → pi-mono) deserve its own pattern?

**Signal:** Mario brought ~25K-stars worth of Java game-dev community trust into AI-agent space. pi-mono reached 38.9K in 8.5 months = unusually high velocity for solo-without-corporate. Is this a **cross-domain-founder-equity sub-path** of Pattern #27 Community-Viral Scale Path?

**Defer-to-decision:** Observational N=1. Watch for 2nd case (e.g., well-known-game-engine-author → AI-tool). Currently noted inside Pattern #27 13th data point.

### 4. Does pi-mono's lack of MCP at T1 scale warrant Pattern #18 refinement now?

**Signal:** Pattern #18 Agent Runtime Standardization was CONFIRMED v15 primarily via MCP-consumer observations. pi-mono is first T1 at 38.9K scale to deliberately exclude MCP. Claude-hud v35 was extension-point-consumer (not MCP-based), but claude-hud is a narrow plugin (not a full coding-agent runtime). pi-mono is a full coding-agent runtime rejecting MCP = stronger counter-evidence.

**Defer-to-decision:** Observational counter-evidence at v36. Do NOT refine Pattern #18 yet (N=1 at T1-coding-agent-runtime-rejection). If 2nd T1 coding-agent-runtime emerges rejecting MCP, formalize "MCP-optional-via-extension-only" sub-variant. **Minor risk:** could also signal a splintering agent-runtime-standards ecosystem; monitor.

### 5. Does pi-mono's lockstep-monorepo-versioning with 200+ releases in 8.5 months reveal a release-cadence pattern?

**Signal:** ~23 releases/month sustained is extreme but could be a monorepo-style artifact (lockstep bumps even small packages). Multica v15 had 43 releases (43 months of project age at the time = ~1/month). BMAD v11 had 45K stars with more traditional release cadence.

**Defer-to-decision:** File as author-archetype observation inside Mario's entity page. No pattern registration at N=1. Watch for 2nd solo-monorepo-lockstep case.

### 6. Is `lgtm`/`lgtmi` + `🤖🤖🤖` convergence a new meta-pattern "Agent-Era Maintainer-Facing Governance Gates"?

**Signal:** v31 candidate #69 was `🤖🤖🤖` PR suffix (agent-authored opt-in). v36 observes `lgtm`/`lgtmi` (maintainer-authored approval keyword). Both are agent-era OSS-governance innovations that didn't exist pre-LLM-in-OSS-contribution era. At N=2 they're structurally distinct sub-variants (69a agent-side + 69b maintainer-side) but share the meta-pattern "OSS governance gates targeting AI-assisted contributor volume."

**Defer-to-decision:** v36 proposes **strengthening #69 to N=2 with sub-variants**; promotion-candidate at next mini-audit under structurally-unambiguous-N=2 criterion. Defer actual promotion decision to mini-audit.

### 7. What does Mario's OSS-session-sharing philosophy (`pi-share-hf` → Hugging Face) imply for Storm Bear's vault-sharing strategy?

**Signal:** Mario publicly publishes his own work sessions on HF dataset `badlogicgames/pi-mono`. Storm Bear's wikis are currently private Obsidian vault. Is the vault-publication-via-standardized-dataset a pattern worth examining?

**Defer-to-decision:** Strategic (Storm Bear-facing) — out-of-scope for pattern library. File as Phase 4b "Storm Bear implications" section, not as pattern candidate.

### 8. Does multi-tier-monorepo-under-single-flagship represent a Pattern #17 refinement to add "tight-flagship" sub-variant?

**Signal:** Pattern #17 Ecosystem-Layer Organizations has 10 data points across 4+ variants (individual-led / big-tech / commercial-startup / ecosystem-scale / solo-with-commercial / solo-one-hit-flagship — per v35 claude-hud observation). pi-mono is solo-with-monorepo-under-single-flagship — structurally similar to claude-hud's "solo-one-hit-flagship" but with **packaged-ecosystem-around-flagship** not just single-repo-flagship.

**Defer-to-decision:** At v36 pi-mono is registered as 11th data point strengthening #17. If N=2 emerges for "flagship-with-ecosystem-around-it" (e.g., if in corpus we later observe another solo author with flagship + 5+ companion packages), formalize as sub-variant. For now, observational.

---

*(C) Claude-generated 2026-04-23.*
