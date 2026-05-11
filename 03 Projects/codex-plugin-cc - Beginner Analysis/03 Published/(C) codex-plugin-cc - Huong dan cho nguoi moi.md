# codex-plugin-cc — Hướng dẫn cho người mới (bilingual VN + EN)

> **Subject:** [`openai/codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) — *"Use Codex from Claude Code to review code or delegate tasks."*
> **Wiki:** Storm Bear corpus v62 / 2026-05-08
> **Tier:** T4 (Bridge — competitor-platform-bridge-as-plugin)
> **Stars:** 17.8K / **License:** Apache-2.0 / **Lang:** JavaScript 100% / **Author:** OpenAI corporate

---

## 1. Đây là gì? / What is it?

**VN:** codex-plugin-cc là **plugin OpenAI publish CHO Anthropic Claude Code** — đây là sự kiện đầu tiên trong corpus 62 wiki: một AI provider lớn (OpenAI) publish plugin cho IDE của đối thủ (Anthropic). Plugin cho phép gọi Codex (OpenAI) từ trong Claude Code (Anthropic) qua 7 slash commands để review code và delegate tasks.

**EN:** codex-plugin-cc is **OpenAI publishing a plugin FOR Anthropic Claude Code** — corpus-first cross-vendor cooperation observation in 62-wiki history. Plugin enables calling Codex (OpenAI) from inside Claude Code (Anthropic) via 7 slash commands for code review and task delegation.

**Tagline verbatim:** *"Use Codex from Claude Code to review code or delegate tasks."*

---

## 2. Corpus-first signals

10 corpus-firsts at v62:

1. **Competitor-published plugin for rival platform** — OpenAI for Anthropic Claude Code (no precedent in 61 prior wikis)
2. **Apache-2.0 corporate-default at OpenAI scale** (matches spec-kit Microsoft + magika Google = corporate AI-tool default)
3. **`/codex:adversarial-review` as prompt-framing variant** — counter-evidence narrowing Pattern #76 architectural scope
4. **Cross-vendor authentication-required plugin** (Claude Code host + Codex backend = separate auth flows)
5. **4-command background-task lifecycle primitive** (rescue + status + result + cancel)
6. **6-primitive plugin architecture at corporate scale** (agents + commands + hooks + prompts + schemas + skills)
7. **Plugin namespace `org-namespace` convention** (vs solo single-segment naming)
8. **T4 Layer 2 cross-vendor-bridge-as-plugin sub-archetype** (3rd Pattern #18 Layer 2 mechanism after runtime API translation v60 + install-time format translation v61)
9. **Corporate-org Pattern #59 Claude Code Plugin Marketplace publication** (was solo OMC v27 + claude-hud v35; now corporate)
10. **Implicit-host-platform citation** as Pattern #57 observation (Claude Code is corpus subject; install command references it)

---

## 3. Tier placement

**T4 (Bridge — competitor-platform-bridge-as-plugin).**

**VN:** codex-plugin-cc bridges 2 platforms khác nhau (Codex backend OpenAI + Claude Code host Anthropic). Surface là slash commands trong Claude Code, nhưng function là cross-vendor delegation. T4 framing chính xác hơn T1 augmentation.

**EN:** codex-plugin-cc bridges 2 distinct platforms (Codex backend OpenAI + Claude Code host Anthropic). Surface in Claude Code, function = cross-vendor delegation. T4 framing more accurate than T1 augmentation.

**3rd Pattern #18 Layer 2 sub-archetype:**
- v60 free-claude-code: api-protocol-translation-proxy
- v61 cc-sdd: install-time-per-platform-skill-format-translator
- **v62 codex-plugin-cc: cross-vendor-platform-bridge-as-plugin (NEW)**

---

## 4. Cài đặt / Installation

**VN:** Cài qua Claude Code plugin marketplace:

**EN:** Install via Claude Code plugin marketplace:

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Requirements:**
- ChatGPT subscription HOẶC OpenAI API key
- Node.js 18.18+
- Claude Code installed (host)

---

## 5. 7 slash commands / Workflow chính

### Review (2 commands)

```
/codex:review                     # Standard read-only review
/codex:adversarial-review         # Steerable challenge review (design-decision focus)
```

**VN:** `/codex:review` review thường (uncommitted changes hoặc branch comparison). `/codex:adversarial-review` reframe REVIEW SAME function với adversarial prompt — pressure-test design decisions, không chỉ implementation details. Hỗ trợ `--base <ref>` + custom focus text.

**EN:** `/codex:review` standard review. `/codex:adversarial-review` reframes same review function with adversarial prompt — targets design decisions over implementation. Supports `--base <ref>` + custom focus text.

### Task delegation (1 command)

```
/codex:rescue [--background] "task description"
```

**VN:** Delegate investigation/fix/continuation work to Codex. Optional `--background` mode for long-running.

### Background-task lifecycle (3 commands)

```
/codex:status                     # Display running + recent jobs
/codex:result <session-id>        # Retrieve final output
/codex:cancel <session-id>        # Stop active task
```

### Setup (1 command)

```
/codex:setup                      # Verify install + auth
```

---

## 6. So sánh với cc-sdd v61 (Pattern #76 counter-evidence)

**VN:** cc-sdd v61 vừa được register Pattern #76 ở v63 mini-audit (1 wiki trước) với evidence: separate `kiro-review` subagent + auto-debug + completion gate = ARCHITECTURAL-ROLE-SEPARATION.

codex-plugin-cc v62 ship 1 wiki sau với `/codex:adversarial-review` cũng tên adversarial-review. Nhưng mechanism khác fundamental:

| Dimension | cc-sdd v61 | codex-plugin-cc v62 |
|---|---|---|
| Reviewer role | Separate `kiro-review` subagent | Same review function |
| Stratum | **Architectural** (role separation) | **Prompt-engineering** (template variation) |
| Auto-debug-on-rejection | Yes | No |
| Completion gate | Yes | No |

**EN:** cc-sdd has separate-role architectural primitive. codex-plugin-cc has prompt-framing variant within same review function. Same outcome category (adversarial review) via fundamentally different implementation strata.

→ Counter-evidence narrowing Pattern #76 scope to "architectural-role-separation specifically." NEW sister candidate "prompt-framing variant" registered N=1 at v62.

---

## 7. So sánh với T4 Bridge corpus siblings

**VN:** Pattern #18 Layer 2 sub-archetype emerging:

**EN:** Pattern #18 Layer 2 sub-archetype:

| Sub-archetype | Wiki | Mechanism | Cross-org |
|---|---|---|---|
| api-protocol-translation-proxy | free-claude-code v60 | Anthropic API ↔ providers | Yes |
| install-time-skill-format-translator | cc-sdd v61 | Per-platform skill format | Yes (8 platforms) |
| **cross-vendor-platform-bridge-as-plugin** | **codex-plugin-cc v62** | **Cross-vendor IDE delegation** | **Yes (OpenAI ↔ Anthropic)** |

3 sub-archetypes at N=1 each. Future audits may consolidate as meta-pattern if 5+ accumulate.

---

## 8. Ethical framing + Caveats

### 8.1 Cross-vendor supply-chain risk

**VN:** Plugin bridges 2 vendor stacks (Anthropic Claude Code + OpenAI Codex). Trust boundary spans both. Một bên compromise affects user.

**EN:** Cross-vendor trust boundary; either Anthropic or OpenAI compromise affects user.

### 8.2 Cost overhead

**VN:** ChatGPT subscription cost (gate). Codex token consumption khi sử dụng review/delegate. Track cost via `/codex:status`.

**EN:** ChatGPT subscription cost gate. Codex token consumption from reviews/delegations.

### 8.3 OpenAI strategic motive (open question)

**VN:** Tại sao OpenAI publish FOR Claude Code? Không rõ rõ ràng. Hypotheses:
- Marketshare retention (developers prefer Claude Code UX)
- Distribution acquisition (footprint trong rival marketplace)
- Codex commodification (position as backend service)
- Symmetric-cooperation invitation (expecting Anthropic for Codex)

**EN:** OpenAI strategic motive unclear. Multiple hypotheses; corpus-first observation deserves monitoring.

### 8.4 Apache-2.0 vs MIT signaling

**VN:** OpenAI ship Apache-2.0, không MIT. Apache-2.0 có patent grant explicit. Match corporate-AI-tool default (spec-kit + magika + codex-plugin-cc all Apache-2.0).

**EN:** Apache-2.0 has explicit patent grant; matches corporate-AI-tool default observed across corpus.

### 8.5 No multi-platform (single-host)

**VN:** codex-plugin-cc chỉ chạy trong Claude Code. Không phải multi-platform plugin (vs cc-sdd 8 platforms). Nếu vault sau này dùng Cursor/Codex CLI, codex-plugin-cc không cover.

**EN:** Single-host (Claude Code only). Doesn't cover multi-IDE workflow.

---

## 9. Storm Bear vault relevance

**VN:** **Pilot ranking #1.5 NEW** (post-cc-sdd v61 #1, before free-claude-code v60 #2).

Lý do:
- Best deployed AS COMPARISON-PILOT to cc-sdd v61 (apple-to-apple adversarial-review evaluation: architectural vs prompt-framing)
- Storm Bear has ChatGPT subscription (gate satisfied)
- Apache-2.0 commercial-friendly
- 3-of-4 Phase 0.9 STRICT PASS = legitimate Storm Bear meta-entity inclusion

Caveats:
- Single-host plugin (Claude Code only) — narrower leverage
- Cross-vendor cost (ChatGPT tokens) on top of Anthropic API
- Best NOT standalone pilot (cc-sdd already provides review-augmentation); best as comparison

**Recommended pilot scope:**
1. Install codex-plugin-cc + cc-sdd both in 1 sandbox vault project
2. Run `/codex:review`, `/codex:adversarial-review`, AND `cc-sdd /kiro-impl autonomous mode` on SAME diff
3. Measure: review quality / detection rate / latency / cost / ergonomics
4. Document `04 Reviews/(C) 2026-05-XX adversarial-review comparison pilot.md`

**EN:** Pilot ranking #1.5 NEW (post-cc-sdd #1). Best deployed as comparison-pilot to cc-sdd. Single-host limitation; cross-vendor cost overhead. Recommended apple-to-apple comparison on same diffs.

---

## 10. Roadmap học 4 tuần / 4-week learning roadmap

### Week 1 — Surface understanding
- Đọc README.md + workflow examples
- Cài thử trong sandbox project: `/plugin marketplace add` + install + setup
- Chạy `/codex:review` + `/codex:adversarial-review` trên 1 small diff

### Week 2 — Background-task primitive
- Test `/codex:rescue --background "fix race condition"` flow
- Quan sát `/codex:status` + `/codex:result` lifecycle
- Compare with cc-sdd `/kiro-impl` autonomous mode

### Week 3 — Adversarial-review comparison
- Run cc-sdd `kiro-review` AND `/codex:adversarial-review` on same diff
- Compare: detection quality / false positives / design-decision targeting
- Document mechanism distinction (architectural vs prompt-framing)

### Week 4 — Cross-vendor stack evaluation
- Stack: cc-sdd (methodology) + codex-plugin-cc (review) + free-claude-code (proxy) + claude-hud (status)
- Evaluate: zero-conflict orthogonal-layer composition
- Decision: sustainable for daily vault use, or pilot-only?

---

## 11. Tradeoffs + Limitations

**Trade-offs:**
- ✅ Cross-vendor expertise + Apache-2.0 OSS + corporate-quality docs ↔ ❌ Cross-vendor auth + ChatGPT subscription cost
- ✅ Adversarial-review prompt-framing low-cost ↔ ❌ Less-robust than architectural role-separation
- ✅ Background-task explicit lifecycle ↔ ❌ Single-host (Claude Code only)
- ✅ Pattern #59 corporate-marketplace publication ↔ ❌ Plugin abandonment risk if OpenAI strategy shifts

**Limitations:**
- Single-host (Claude Code only)
- ChatGPT subscription required
- Cross-vendor authentication overhead
- One-direction integration (Claude Code → Codex only; no reverse)
- EN-only documentation
- No MCP integration

---

## 12. Caveats + safety notes / Lưu ý

- **Pin plugin version** for production stability
- **Audit cross-vendor data flow** — what code/diffs are sent to Codex backend?
- **Token cost monitoring** — Codex calls add to ChatGPT subscription usage
- **Adversarial-review brittleness** — prompt-template may degrade across model versions; less robust than role-separation
- **Cross-vendor trust boundary** — both Anthropic + OpenAI compromise possibilities

---

## 13. References + Next action

**Repository:** https://github.com/openai/codex-plugin-cc

**Documentation:**
- README.md — overview + 7 slash commands + workflow + FAQ + configuration
- CHANGELOG.md — release history
- LICENSE — Apache-2.0
- NOTICE — Apache-2.0 attribution requirements

**Sibling corpus wikis:**
- [cc-sdd v61](../../cc-sdd%20-%20Beginner%20Analysis/) — Pattern #76 architectural-role-separation N=1 baseline
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/) — T4 api-protocol-translation-proxy
- [spec-kit v17](../../spec-kit%20-%20Beginner%20Analysis/) — Microsoft corporate-strategic predecessor
- [markitdown v28](../../markitdown%20-%20Beginner%20Analysis/) — Microsoft corporate T4 sibling
- [oh-my-claudecode v27](../../oh-my-claudecode%20-%20Beginner%20Analysis/) — Pattern #59 N=1 marketplace
- [claude-hud v35](../../claude-hud%20-%20Beginner%20Analysis/) — Pattern #59 N=2 marketplace

**Phase 4b deliverable:** `03 Published/(C) Pattern 76 counter-evidence - adversarial-review-mechanism-distinction at v62.md`

**Next action / Bước tiếp theo:**

1. **Storm Bear comparison pilot:** Install codex-plugin-cc + cc-sdd v61 trong cùng sandbox vault project. Chạy adversarial-review trên cùng diff. Document findings.
2. **Pattern Library v66 mini-audit:** apply counter-evidence-driven refinement to Pattern #76 + register NEW sister candidate (prompt-framing variant) + register NEW Pattern #77 candidate (cross-vendor cooperation) + register Pattern #18 Layer 2 cross-vendor-bridge sub-archetype
3. **Corpus monitoring v63-v66:** watch for 2nd cross-vendor cooperation observation (Anthropic for Codex CLI? Google Gemini for Claude Code? Microsoft Copilot for non-VSCode?) → un-stale-flag NEW Pattern #77
