# (C) Han Brothers Duo-Founder + Dual-License Strategy

> **Type:** Entity — organizational + licensing
> **Parent:** [[(C) index]]
> **Sources:** README citations + LICENSE file + GitHub metadata
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Unsloth organizational + licensing profile: **Daniel Han + Michael Han (likely brothers) + Unsloth team = duo-founder-plus-team archetype** (10th in corpus, new candidate #46). **Dual-licensing strategy** splits Apache-2.0 (core library) from AGPL-3.0 (Studio UI), deliberately protecting the WebUI from SaaS appropriation while keeping the framework commercially usable (new candidate #45). Strengthens Pattern #29 License-Category Diversity with 4th non-permissive data point (first AGPL in corpus).

## 2. Authorship + organization

### Known facts

- **Daniel Han + Michael Han** — named in citation / credits
- **Likely brothers** (same surname, duo founding pattern) — not formally confirmed
- **Unsloth team** — unnamed team members, size unclear
- **Unsloth AI** — organization name; incorporation status unclear (LLC/Inc unclear from README)
- No VC funding disclosed
- No academic affiliation disclosed

### Inferred archetype

**Duo-founder + team archetype:**
- 2 named principals (likely family relationship)
- Small unnamed team
- Open-source framework product
- Consumer-GPU community focus
- Performance-competitive-edge as competitive moat
- No academic publication (contrast LlamaFactory ACL 2024)

### Organizational archetype inventory (corpus post-v23)

| # | Archetype | Example |
|---|-----------|---------|
| 1 | Solo-community | Various |
| 2 | Solo-known-figure | Karpathy (autoresearch) / Jesse Vincent (Superpowers) |
| 3 | Founder-personal | Garry Tan (gstack) |
| 4 | Community-unattributed | GSD |
| 5 | LLC-formalized | BMad Code LLC (BMAD) |
| 6 | Solo-VN-author | Tody Le (codymaster) |
| 7 | Official-corporate | GitHub/Microsoft (spec-kit), ByteDance (deer-flow), Google (gws) |
| 8 | Academic-lab | hiyouga + Lab4AI (LlamaFactory) |
| 9 | Commercial-foundation-model | Fish Audio / 39 AI INC (fish-speech) |
| 10 | **Duo-founder + team** | **Han brothers + Unsloth team (Unsloth)** ← NEW v23 |

## 3. Pattern #46 candidate: Duo-Founder + Team Archetype

### Formal statement

> Some frameworks are authored by a founding pair (often family/co-founder relationship) plus a small unnamed team. Distinct from solo (1 person), LLC (formal legal entity), academic-lab (university affiliation), and corporate (pre-existing company).

### Evidence post-v23

| # | Wiki | Evidence |
|---|------|----------|
| 1 | Unsloth v23 | Daniel Han + Michael Han + Unsloth team |

### Status

**N=1 at v23** — register as candidate. Requires 2nd data point (ideally another duo-founder framework) to validate. May stay candidate indefinitely if pattern is rare.

### Why distinct

- **Not solo** — 2 named principals coordinating
- **Not LLC** — no formal incorporation disclosed
- **Not academic** — no university affiliation
- **Not pre-existing corporate** — Unsloth founded around product, not pre-existing company extending

## 4. Dual-licensing strategy

### License split

| Component | License | Rationale |
|-----------|---------|-----------|
| **Unsloth Core** (library + CLI + Python API) | **Apache-2.0** | Permissive; enables commercial code reuse |
| **Unsloth Studio** (WebUI) | **AGPL-3.0** | Strongest copyleft; protects SaaS appropriation |

### Why AGPL-3.0 for Studio specifically

**AGPL-3.0 trigger clause:** If a modified version is deployed as a network service, source must be provided to users. Closes the "SaaS loophole" in GPL-3.0 (which only triggers on distribution).

**Strategic implication:**
- Cloud vendor cannot wrap Unsloth Studio UI as paid SaaS without publishing their modifications
- Core library (Apache) remains permissive — commercial users can embed Unsloth training in their products freely
- **Protection is targeted at UI/product layer, not performance library**

### Corpus novelty

**First dual-license in corpus.** Previous patterns:
- Single Apache-2.0 (most frameworks)
- Single MIT (most T1 frameworks)
- Single GPL-3.0 (TrendRadar, system-prompts-leaks)
- Single custom non-OSI (fish-speech)

**Unsloth is first to deliberately split licenses within single product family.**

## 5. Pattern #45 candidate: Dual-Licensing Strategy

### Formal statement

> Some projects use different licenses for different components (typically permissive for core library + copyleft for UI/product layer) to balance commercial reuse with appropriation protection. Strategic license engineering as competitive positioning.

### Evidence post-v23

| # | Wiki | Evidence |
|---|------|----------|
| 1 | Unsloth v23 | Apache-2.0 (core) + AGPL-3.0 (Studio) |

### Status

**N=1 at v23** — register as candidate. Requires 2nd data point to validate. Likely to emerge as more OSS frameworks face cloud-vendor appropriation concerns.

### Speculative anchors

Future candidates to watch:
- Terraform → BSL (HashiCorp business-source-license transition)
- Elastic → SSPL (similar AGPL-style)
- Redis → various
- Frameworks with UI layers + enterprise concerns

## 6. Pattern #29 License-Category Diversity (confirmed v21)

### Evidence strengthening at v23

Non-permissive license corpus post-v23:

| License | Count | Wikis |
|---------|-------|-------|
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| **AGPL-3.0** | 1 | **Unsloth Studio v23** ← NEW |
| Custom non-OSI | 1 | fish-speech v20 |
| **Total non-permissive** | **4** | **17% of 23 wikis** |

### Observation

License category now genuinely diverse:
- **Permissive:** MIT (dominant) + Apache-2.0 (#2) + CC0 (rare) + ISC (rare)
- **Copyleft:** GPL-3.0 + **AGPL-3.0** (v23)
- **Non-OSI:** Custom terms (fish-speech)

Pattern #29 at N=4 reinforced. License diversity signals mature OSS ecosystem with deliberate license engineering.

## 7. Pattern #32 Research-Paper-Chain Lineage (promoted v22)

### Evidence strengthening at v23

Unsloth acknowledges upstream lineage:
- **llama.cpp** (Gerganov — inference framework)
- **HuggingFace** (transformers, TRL)
- **PyTorch**
- **Torch AO** (quantization)
- **NVIDIA NeMo DataDesigner**

### N=3 post-v23

| # | Wiki | Lineage evidence |
|---|------|------------------|
| 1 | fish-speech v20 | Research papers + TTS academic lineage |
| 2 | LlamaFactory v22 | Extensive (PEFT + TRL + QLoRA + FastChat + 100+ papers) |
| 3 | **Unsloth v23** | **llama.cpp + HF + PyTorch + Torch AO + NVIDIA NeMo** |

### Observation

Unsloth's lineage is **shorter than LlamaFactory's** but same archetype (research-paper-chain). Depth varies; pattern persists.

## 8. Strategic implications

### For Unsloth team

- **Dual-license protects Studio from commercial SaaS appropriation**
- **Core library remains permissive** — maximizes adoption
- **Community edge:** open-source commitment + performance leadership
- **Risk:** AGPL is controversial in some enterprise environments; may limit Studio adoption

### For corpus

- **License engineering becoming strategic concern** — Pattern #45 may validate as more frameworks face SaaS appropriation
- **Duo-founder archetype underrepresented** — Pattern #46 may stay rare
- **Research-paper-chain confirmed at N=3** — structurally stable

## 9. Comparison with LlamaFactory organizational profile

| Dimension | LlamaFactory v22 | Unsloth v23 |
|-----------|-------------------|--------------|
| Author archetype | Academic-lab (hiyouga + Lab4AI) | **Duo-founder + team (Han brothers)** |
| Academic publication | ACL 2024 peer-reviewed | None |
| Organizational formality | Academic affiliation | Company/team (incorporation unclear) |
| License | Apache-2.0 (single) | **Dual: Apache + AGPL** |
| Community | WeChat + Discord | Discord + Reddit r/unsloth + X |
| Community region | CN-primary | Western-primary |
| Funding | Not disclosed (academic infrastructure assumed) | Not disclosed (no VC mentioned) |

### Archetype diversity confirms Pattern #41 scope refinement

Training-Infrastructure Framework (Pattern #41) observed at N=2 across **2 distinct organizational archetypes** (academic-lab + duo-founder). Pattern is organizationally-agnostic — structural sub-type rather than archetype-specific.

## 10. Edges + limitations

### Known limitations

- **Han brothers identity unconfirmed** — "likely brothers" is inference from shared surname
- **Unsloth AI incorporation status unclear** — no LLC/Inc disclosed in README
- **Team size unknown** — "Unsloth team" unspecified
- **Funding model unclear** — no monetization path disclosed (Studio SaaS? Enterprise support?)

### Pattern implications

- **#45 Dual-Licensing at N=1** — single observation; may stay candidate
- **#46 Duo-Founder at N=1** — single observation; may be rare archetype
- **Cross-validation pending** at v24+

## 11. Related concepts

- [[(C) 500+ Models + Performance-Optimization Positioning]] — positioning context
- [[(C) Custom Triton Kernels + Pattern 43 Validation]] — technical differentiation
- [[(C) Training-Infra 2nd Entrant + Pattern 41 43 Validation + Storm Bear]] — validation analysis
- LlamaFactory v22 — academic-lab archetype peer
- Pattern #29 — license-category diversity strengthening
- Pattern #32 — research-paper-chain strengthening
- Pattern #45 — dual-licensing (new candidate)
- Pattern #46 — duo-founder archetype (new candidate)
- Parent: [[(C) index]]

## References

- README citations section
- LICENSE file (Apache-2.0 core)
- Unsloth Studio LICENSE (AGPL-3.0)
- GitHub metadata (org info, contributors)

---

**Han brothers duo-founder + Unsloth team = 10th organizational archetype (candidate #46). Dual-licensing strategy Apache-2.0 core + AGPL-3.0 Studio = deliberate license engineering protecting UI from SaaS appropriation while keeping core permissive (candidate #45). Strengthens Pattern #29 (AGPL-3.0 added, N=4 non-permissive) + Pattern #32 (research-paper-chain N=3).**
