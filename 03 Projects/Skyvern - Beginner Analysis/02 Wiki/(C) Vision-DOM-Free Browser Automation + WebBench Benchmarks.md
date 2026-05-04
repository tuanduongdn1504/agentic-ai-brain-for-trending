# (C) Vision-DOM-Free Browser Automation + WebBench Benchmarks

> **Type:** Entity — core methodology + evaluation
> **Parent:** [[(C) index]]
> **Sources:** README + Skyvern 2.0 technical report blog
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Skyvern's core methodology: **vision + LLM replace DOM/XPath for browser automation**. Instead of brittle CSS selectors, Skyvern uses screenshots + LLM reasoning to decide actions. Validated via **WebBench 64.4% + WebVoyager 85.8%** (Skyvern 2.0 technical report). First T5 framework with domain-specific application focus + empirical browser-automation benchmarks in Storm Bear corpus.

## 2. Vision-DOM-free methodology

### The brittle-selector problem

Traditional browser automation (Playwright / Puppeteer / Selenium):
- XPath: `//*[@id="login"]/button[2]` breaks when DOM changes
- CSS selector: `.btn-primary` breaks on class rename
- Record-and-replay RPA: breaks on any UI refactor

**Result:** Automation scripts have high maintenance cost, frequent failures.

### Skyvern's approach

1. Take page screenshot
2. LLM analyzes screenshot (vision model)
3. Natural-language instruction ("click login button") mapped to screen coordinates
4. Execute action
5. Validate new page state

**Result:** Resilient to DOM changes. UI refactors don't break automation (unless visual layout fundamentally changes).

### 4 AI page commands implementing this

| Command | Methodology |
|---------|-------------|
| `page.act(prompt)` | Vision → LLM → action coordinates |
| `page.extract(prompt, schema)` | Vision → LLM → structured JSON |
| `page.validate(prompt)` | Vision → LLM → boolean |
| `page.prompt(prompt, schema)` | Arbitrary LLM query on page context |

## 3. Why vision works

### Trade-offs

| Dimension | DOM-based | Vision-based |
|-----------|-----------|--------------|
| Selector brittleness | High (breaks on refactor) | Low (resilient) |
| Speed | Fast (direct DOM query) | Slower (vision + LLM latency) |
| Cost | Free (no LLM call) | Per-action LLM cost |
| Accuracy on dynamic UIs | Low (races) | Higher (waits for visual) |
| Explainability | High (selector explicit) | Medium (LLM reasoning) |
| Complex UIs (iframes/shadow DOM) | Hard | Easier |

### When vision wins

- Long-lived automation where DOM changes
- UIs with iframes / shadow DOM / dynamic classes
- Cross-site automation (one codebase for N sites)
- Natural-language task descriptions

### When DOM still wins

- High-frequency automation (LLM latency dominates)
- Deterministic UIs (selectors stable)
- Cost-sensitive automation (no LLM budget)

## 4. WebBench benchmark

### 64.4% accuracy

WebBench is a 2024 benchmark for web-agent evaluation:
- Tasks: multi-step web workflows (e.g., booking flight, filling forms)
- Categories: READ (information extraction) / WRITE (form filling, logins, downloads)
- Skyvern scores **64.4% overall** + **best-in-class on WRITE tasks**

### What 64.4% means

Multi-step web tasks are hard — typical baselines (raw GPT-4 Vision) score <30%. Skyvern's 64.4% = significant improvement via:
- Vision-specific prompting
- Action grounding (coordinates + retry logic)
- Task decomposition (BabyAGI-style)
- Error recovery (validate step + retry)

## 5. WebVoyager benchmark

### 85.8% on Skyvern 2.0

WebVoyager = GPT-4V-era benchmark for web navigation:
- General web navigation tasks
- Cross-site evaluation
- Human-annotated success criteria

Skyvern 2.0 achieves **85.8%** — state-of-the-art at publication.

### Technical report

*"Skyvern 2.0: State-of-the-art Web Navigation with 85.8% on WebVoyager Eval"* — skyvern.com/blog.

Research-style publication, not peer-reviewed. Preprint-adjacent tier (Pattern #8 sub-classification).

## 6. Pattern #8 Research-Benchmark — 7th data point

### Evidence post-v24

| # | Wiki | Benchmark |
|---|------|-----------|
| 1 | codymaster v12 | SkillsBench +18.6pp |
| 2 | autoresearch v10 | val_bpb |
| 3 | graphify v16 | 71.5× token reduction |
| 4 | spec-kit v17 | 48× productivity |
| 5 | fish-speech v20 | Seed-TTS Eval + EmergentTTS-Eval |
| 6 | LlamaFactory v22 | ACL 2024 benchmarks |
| 7 | **Skyvern v24** | **WebBench 64.4% + WebVoyager 85.8%** |

### Rigor tiers

- **Peer-reviewed:** LlamaFactory v22 (ACL 2024) — highest
- **arXiv preprint:** fish-speech v20 (2 preprints)
- **Technical report blog:** Skyvern v24 (Skyvern 2.0), autoresearch v10
- **Documentation-embedded:** codymaster, graphify, spec-kit

Skyvern = technical-report tier.

## 7. Comparison with DOM-based browser frameworks

| Framework | Approach | Corpus presence |
|-----------|----------|-----------------|
| Playwright (Microsoft) | DOM | Outside corpus |
| Puppeteer (Google) | DOM | Outside corpus |
| Selenium | DOM | Outside corpus |
| UiPath | Record-replay RPA | Outside corpus |
| Power Automate | Record-replay RPA | Outside corpus |
| **Skyvern** | **Vision + LLM** | **Corpus (T5 v24)** |
| browser-use (external) | Vision + LLM | Not in corpus |
| Agent-E / LaVague | Vision + LLM variants | Not in corpus |

Skyvern = first vision-based browser framework in Storm Bear corpus.

## 8. Cross-T5 methodology comparison

| T5 framework | Methodology | Domain |
|--------------|-------------|--------|
| deer-flow v9 | SuperAgent long-horizon autonomy | Research |
| autoresearch v10 | program.md skill + git-based iteration | ML experiments |
| paperclip v14 | Constitutional governance + 9 primitives | Orchestration |
| **Skyvern v24** | **Vision + LLM + 4 page commands** | **Browser automation** |

**First T5 with domain-specific application focus.** Prior 3 were generalist/open-ended.

## 9. Pattern #19 community-viral lineage

### Verbatim citation

> *"Skyvern was inspired by the Task-Driven autonomous agent design popularized by BabyAGI and AutoGPT"*

### Sub-variant observation

**Pattern #19 archetypes:**
- 3a: Community-viral no-lineage (agency-agents v18 — Reddit-born, no predecessors named)
- 3b: Community-viral lineage (Skyvern v24 — acknowledges BabyAGI/AutoGPT community-viral ancestors)

**Sub-variant refinement candidate for Pattern #19.**

## 10. Edges + limitations

### Vision-based limitations

- **Latency** — each action requires LLM inference (seconds vs milliseconds for DOM)
- **Cost** — per-action LLM API cost adds up for long workflows
- **Non-determinism** — LLM outputs vary; retry logic needed
- **Small-text/dense-UIs** — vision models struggle with fine-grained text

### Benchmark caveats

- **64.4% leaves 35.6% failure rate** — not production-ready for mission-critical automation
- **WRITE-tasks best-in-class** but WRITE often simpler than multi-step READ+WRITE
- **Benchmark-specific** — real-world sites may differ from WebBench distribution

### Browser limitation

- **Chrome/Chromium only** — Firefox + WebKit not supported
- **Chrome 136+ workaround** required

## 11. Related concepts

- [[(C) Skyvern-AI Commercial Entity + Pattern 31 Promotion]] — commercial context
- [[(C) BabyAGI AutoGPT Lineage + Pattern 19 Community-Viral Strengthening]] — intellectual lineage
- [[(C) T5 Extends to N=4 + 4 Archetypes + Pattern Analysis]] — tier-level meta
- Pattern #8 — 7th data point
- Pattern #19 — community-viral lineage sub-variant
- Parent: [[(C) index]]

## References

- README core commands + benchmarks
- skyvern.com/blog — Skyvern 2.0 technical report
- WebBench + WebVoyager benchmark documentation

---

**Vision + LLM replace DOM/XPath (resilient to UI changes). 4 AI page commands (act/extract/validate/prompt) implement methodology. WebBench 64.4% + WebVoyager 85.8% empirical validation (Pattern #8 7th data point). First T5 with domain-specific application focus. Community-viral-lineage sub-variant (BabyAGI + AutoGPT acknowledgment).**
