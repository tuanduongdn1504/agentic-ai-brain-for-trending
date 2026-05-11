# Entity 4 — Storm Bear Meta-Entity (INCLUDE per Phase 0.9 STRICT 2-of-4 PASS)

## Phase 0.9 STRICT amendment check (post-v55 session 66)

| Criterion | Status | Evidence |
|---|---|---|
| (a) Author archetype = structural peer | **FAIL-leaning / borderline** | Solo-individual GitHub user; no public coach / VN / Asian-diaspora / portfolio-at-Storm-Bear-publishing-scale signal. Conservative FAIL. |
| (b) Operational tool vault could deploy directly | **PASS** ✅ | Storm Bear vault uses Claude Code routinely. free-claude-code provides direct cost-reduction (route non-critical wiki-build prompts to OpenRouter / DeepSeek / Ollama). Concrete deployment ~1h setup. |
| (c) Methodology-influence-node | **FAIL** | No Karpathy / Lam / Cherny / SDD / TDD / agentic-engineering lineage. AGENTS.md is internal-discipline document. |
| (d) In-corpus reference | **PASS** ✅ | Tagline cites OpenClaw (Pattern #18 Layer 2 corpus runtime standard with 5+ in-corpus references). Pattern #57 57c forward-citation positive-comparison-parallel sub-variant. |

**SUM: 2 PASS** ≥ 1 threshold → **INCLUDE Storm Bear meta-entity.**

## Streak counter

- v59 AutoGPT broke 41-streak at 1st disciplined-skip (0/4 PASS)
- **v60 free-claude-code restarts streak at 1** (1-consecutive Storm Bear meta post-v59 reset)
- Phase 0.9 amendment 5-instance window: v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS = 4 INCLUDE / 1 SKIP = 80% INCLUDE rate, validates STRICT amendment is regularly satisfiable AND disciplined-skip works as designed.

## Storm Bear pilot relevance — HIGH-OPERATIONAL

**This is the highest direct-pilot-utility wiki since claude-howto v32.** Direct cost-savings utility for active vault Claude-Code workflow.

### Pilot deployment scenario

Setup time: ~1h
1. `git clone github.com/Alishahryar1/free-claude-code`
2. `cp .env.example .env` + populate OpenRouter API key (cheapest cloud) + Ollama local for Haiku tier
3. `uv run server.py` → starts proxy on port 8082
4. Set `ANTHROPIC_BASE_URL=http://localhost:8082` + dummy `ANTHROPIC_AUTH_TOKEN` in shell env
5. Run a wiki-build prompt via Claude Code → traffic routed through proxy → upstream provider

### Cost-reduction pilot (1 week)

- Baseline: track current Anthropic API spend during wiki-build (~6 wikis/week typical)
- Pilot: route wiki-build prompts through proxy with:
  - Opus tier → OpenRouter GLM-5 (~50% cheaper for similar quality)
  - Sonnet tier → DeepSeek (~70% cheaper)
  - Haiku tier → Ollama local llama.cpp (free)
- Measure: spend delta + quality delta + velocity delta
- Decision: keep / partial keep (only Sonnet routing) / revert

### Quality risk

Routine v2.1 has high context-pressure tolerance. Cheap-backend routing might degrade wiki output quality (false claims, missed pattern observations, weaker synthesis). Mitigation: route ONLY non-critical phases (e.g., source ingestion clusters which are mostly verbatim extraction) through cheap backend; keep entity pages + Phase 5 iteration log on Anthropic native.

### Stack composition with prior pilots

claude-howto v32 (#1) + claude-hud v35 (#2) + free-claude-code v60 (#3 NEW):
- claude-howto = how-to-use-Claude-Code skill collection
- claude-hud = statusline / observability
- free-claude-code = backend-routing / cost-reduction
- Composition: zero-conflict (orthogonal layers); could deploy all 3 simultaneously
- 4-plugin Claude-Code augmentation stack possibility: claude-hud + claude-context (vault semantic search) + claude-howto + free-claude-code

## Storm Bear pilot ranking refresh

Post-v60:
1. **claude-howto v32** — VN solo, direct vault skill-deployment (held #1)
2. **claude-hud v35** — statusline / observability (held #2)
3. **free-claude-code v60 🆕** — Claude-Code cost-reduction proxy (DIRECT-OPERATIONAL utility, NEW #3)
4. **spec-kit v17** — methodology-lineage SDD reference
5. **pi-mono v36** — solo-monorepo flagship
6. **OMC v27** — Korean OpenClaw-fork peer
7. **claude-context v40** — vault semantic-search pilot
8. **graphify v16** — graph-based code search
9. **claude-code-best-practice v34** — education
10. **markitdown v28** — doc conversion

## Cautionary observations

- License (MIT) permits commercial use → vault deployment legally clean
- Solo-community 22.1K-star repo with no releases published → version-pinning required for reproducibility (commit SHA)
- 569 commits + active dev → API may change; pin to known-good commit before pilot
- Voice transcription / Discord-Telegram features = supply-chain surface IF used (Whisper API call surface; bot deployment surface). Caveats per Pattern #66 OBSERVATION-TRACK supply-chain-awareness.

## Vault routine v2.1 impact

- Phase 0.5 cross-wiki check: free-claude-code is 1st T4 protocol-translation entrant; suggests routine v2.2 candidate "T4 sub-archetype taxonomy formalization" at next routine refactor
- Phase 0.9 5-instance window data point: 4 PASS / 1 SKIP = 80% INCLUDE rate validates strict-amendment is regularly satisfiable (not over-tight)
- Phase 4b routing: NEW combined-mode "T4-archetype-expansion + 57c-polarity-emergence + cross-pattern-coupled-design"

## Cross-references

- claude-howto v32 (Storm Bear pilot #1) / claude-hud v35 (#2) / free-claude-code v60 (#3 NEW)
- mattpocock-skills v57 (Phase 0.9 3/4 PASS) / OpenSpec v58 (3/4 PASS) / AutoGPT v59 (0/4 SKIP) / free-claude-code v60 (2/4 PASS) — 4-wiki Phase 0.9 window
- OpenClaw cross-wiki references reinforced by free-claude-code in-tagline citation
