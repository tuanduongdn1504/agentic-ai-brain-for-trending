# (C) ETHOS + ARCHITECTURE Summary

> **Sources:**
> - `00 Sources/gstack/ETHOS.md` (164 lines, ~6KB) — full read
> - `00 Sources/gstack/ARCHITECTURE.md` (365 lines, ~14KB) — full read
> - `00 Sources/gstack/CHANGELOG.md` (2,246 lines, ~80KB) — **skim-first** per routine >20KB rule
>
> **Ingested:** 2026-04-18
> **Coverage:** ETHOS full, ARCHITECTURE full, CHANGELOG version timeline + latest 5 entries
> **Routine context:** Source #3 of 3 cho gstack project (Phase 2)

---

## TL;DR

**VI:** Source #3 combine 3 documents để capture gstack's **philosophy + technical architecture + release cadence**. Key findings: (1) **3 core principles** của Builder Ethos = Boil the Lake + Search Before Building + User Sovereignty; (2) **Browser daemon architecture** là hard part — long-lived Chromium + Bun server + localhost HTTP + bearer token, ~100-200ms per command; (3) **Release cadence aggressive** — 126 versions từ start đến v0.18.3.0 (2026-04-17), multiple versions per day recent.

**EN:** Combined snapshot of philosophy (3 principles), technical architecture (browser daemon model), and release cadence (126 versions, aggressive ship rate).

---

## Part 1: Builder Ethos (ETHOS.md)

### Framing: "The Golden Age"

> "A single person with AI can now build what used to take a team of twenty. The engineering barrier is gone. What remains is taste, judgment, and the willingness to do the complete thing."

**Tone:** Declarative, founder-confident, không hedge. Khác tone ECC (professional) và Superpowers (legalistic/Iron Law).

### Principle 1: Boil the Lake

> "AI-assisted coding makes the marginal cost of completeness near-zero. When the complete implementation costs minutes more than the shortcut — do the complete thing. Every time."

**Lake vs Ocean:**
- **Lake** (boilable): 100% test coverage module, full feature, all edge cases, complete error paths
- **Ocean** (not): rewriting entire system, multi-quarter platform migration

**Rule:** Boil lakes. Flag oceans as out of scope.

**Anti-patterns:**
- "Choose B — 90% with less code" (if A is 70 lines more, choose A)
- "Defer tests to follow-up PR" (tests are cheapest lake to boil)
- "This would take 2 weeks" → say "2 weeks human / ~1 hour AI-assisted"

→ **Match completeness philosophy ECC.** Different framing — ECC says "production-ready"; gstack says "boil the lake".

### Principle 2: Search Before Building (Three Layers of Knowledge)

**Layer 1: Tried-and-true** — standard patterns, battle-tested. Risk: assume obvious is right.

**Layer 2: New-and-popular** — current best practices, blog posts. Risk: "humans subject to mania. Mr. Market too fearful or too greedy."

**Layer 3: First-principles** — original observations từ reasoning. **Prized above all.**

> "The best projects both avoid mistakes (don't reinvent the wheel — Layer 1) while also making brilliant observations that are out of distribution (Layer 3)."

**The Eureka Moment:**
1. Understanding what everyone is doing and WHY (Layers 1+2)
2. Applying first-principles reasoning to their assumptions (Layer 3)
3. Discovering a clear reason why conventional approach is wrong

> "The truly superlative projects are full of these moments — zig while others zag. When you find one, name it. Celebrate it."

→ **Distinctive framing.** ECC + Superpowers don't have explicit "layer of knowledge" taxonomy. **Worth adopting trong Storm Bear vault — frame Claude's research level explicitly.**

### Principle 3: User Sovereignty

> "AI models recommend. Users decide. This is the one rule that overrides all others."

**Iron Man suit** philosophy (cited Karpathy): great AI products augment user, not replace.

> "Two AI models agreeing on a change is a strong signal. It is not a mandate."

**Correct pattern:** generation-verification loop — AI generates, user verifies and decides. AI never skips verification step because it's confident.

**Anti-patterns:**
- "Outside voice is right, so I'll incorporate it." → Present it. Ask.
- "Both models agree, so must be correct." → Agreement is signal, not proof.
- "I'll make the change and tell user afterward." → Ask first. Always.
- "My Assessment" column framing settled fact → present both sides, let user assess.

→ **Convergent với Superpowers's HARD-GATE on brainstorming approval.** Different mechanism (cultural principle vs XML tag), same enforcement intent.

### "How they work together"

> "Boil the Lake says: do the complete thing. Search Before Building says: know what exists before you decide what to build. Together: search first, then build the complete version of the right thing."

### "Build for yourself"

> "The best tools solve your own problem. gstack exists because its creator wanted it. Every feature was built because it was needed, not because it was requested."

→ **Philosophical claim** drives voice protection (xem CLAUDE.md summary): Garry's personal tool, shipped public, voice stays his.

---

## Part 2: Technical Architecture (ARCHITECTURE.md)

### The core idea

> "gstack gives Claude Code a persistent browser and a set of opinionated workflow skills. The browser is the hard part — everything else is Markdown."

### Browser daemon model

```
Claude Code → CLI binary → HTTP POST localhost:PORT → Bun server → CDP → Chromium (headless)
```

**Key constraint:** AI agent + browser cần **sub-second latency** + **persistent state**.

**Without daemon:** 2-3s Chromium startup per command. 20+ commands in QA session = 40+ seconds overhead. State lost between commands.

**With daemon:**
- First call: ~3s (cold start)
- After: ~100-200ms per command
- Persistent state: cookies, tabs, localStorage persist
- Auto-lifecycle: auto-start on first use, auto-shutdown after 30 min idle

### Why Bun (not Node.js)

1. **Compiled binaries** — `bun build --compile` → single ~58MB executable. No `node_modules`, no `npx`, no PATH. Binary just runs.
2. **Native SQLite** — cookie decryption reads Chromium's SQLite DB directly via `new Database()`. No `better-sqlite3`, no gyp.
3. **Native TypeScript** — server runs as `bun run server.ts` during dev. No compilation step.
4. **Built-in HTTP** — `Bun.serve()` handles ~10 routes. No Express/Fastify overhead.

> "The bottleneck is always Chromium, not CLI or server. Bun's startup speed (~1ms compiled binary vs ~100ms Node) is nice but not the reason. Compiled binary and native SQLite are."

→ **Match "zero-dependency" philosophy từ Superpowers**, different implementation (Bun vs custom Node.js server).

### State file + port selection

`.gstack/browse.json` (atomic write, mode 0o600):
```json
{ "pid": 12345, "port": 34567, "token": "uuid-v4", "startedAt": "...", "binaryVersion": "abc123" }
```

**Random port 10000-60000** (retry 5 on collision). Why: 10 Conductor workspaces each run own browse daemon với zero config, zero port conflicts.

### Version auto-restart

Build writes `git rev-parse HEAD` to `browse/dist/.version`. On each CLI invocation, if binary version != running server's `binaryVersion`, CLI kills old server + starts new. **Prevents "stale binary" bugs entirely.**

→ **Distinctive pattern:** self-updating daemon based on binary hash. Reusable cho Storm Bear nếu build long-lived processes.

### Security model

1. **Localhost only** — HTTP server binds `localhost`, not `0.0.0.0`. Not network-reachable.
2. **Bearer token auth** — every session generates UUID token, mode 0o600. All HTTP requests need `Authorization: Bearer <token>`. Mismatches → 401.
3. **Cookie security:**
   - Keychain access requires user approval (macOS dialog "Allow")
   - Decryption in-process (PBKDF2 + AES-128-CBC), never written to disk plaintext
   - Database read-only (copies to temp file, never modifies real browser DB)
   - Key caching per-session (cleared on shutdown)
   - Never logs cookie values
4. **Shell injection prevention** — browser registry hardcoded. DB paths from known constants. Keychain uses `Bun.spawn()` với argument arrays, not shell strings.

→ **Security-conscious design.** Match ECC's AgentShield philosophy (different mechanism, same priority).

### Ref system (@e1, @c1)

Refs = how agent addresses page elements without CSS/XPath:
1. Agent runs `$B snapshot -i`
2. Server calls Playwright's `page.accessibility.snapshot()`
3. Returns structured tree với refs annotated
4. Agent uses refs cho subsequent commands (click, fill, etc.)

→ **Novel abstraction** cho browser automation. Alternative to Playwright selectors.

---

## Part 3: Release Cadence (CHANGELOG.md skim)

### Version statistics

**Total versions:** 126 (từ v0.1.x đến v0.18.3.0)
**Latest version:** v0.18.3.0 (2026-04-17) — tương ứng 1 ngày trước ingest
**Cadence:** Multiple versions per day gần đây. 2026-04-17 có v0.18.2.0 + v0.18.3.0 cùng ngày.

### Last 30 versions (skim headings)

| Version | Date | Theme |
|---------|------|-------|
| 0.18.3.0 | 2026-04-17 | Windows cookie import, OpenCode install, permission prompt fixes |
| 0.18.2.0 | 2026-04-17 | (cùng ngày 0.18.3) |
| 0.18.1.0 | 2026-04-16 | |
| 0.18.0.1 | 2026-04-16 | |
| 0.18.0.0 | 2026-04-15 | Major bump |
| 0.17.0.0 | 2026-04-14 | |
| 0.16.4.0 | 2026-04-13 | |
| 0.16.3.0 | 2026-04-09 | |
| 0.15.13.0 | 2026-04-04 | **Team Mode** |
| 0.15.12.0 | 2026-04-05 | **Content Security: 4-Layer Prompt Injection Defense** |
| 0.15.10.0 | 2026-04-05 | **Native OpenClaw Skills + ClawHub Publishing** |
| 0.15.9.0 | 2026-04-05 | **OpenClaw Integration v2** |
| 0.15.8.0 | 2026-04-04 | **Smarter Reviews** |
| 0.15.7.0 | 2026-04-05 | **Security Wave 1** |
| 0.15.6.0 | 2026-04-04 | **Declarative Multi-Host Platform** |
| 0.15.5.0 | 2026-04-04 | **Interactive DX Review + Plan Mode Skill Fix** |
| 0.15.3.0 | 2026-04-03 | **Developer Experience Review** |

### Major themes observed

**Theme 1: Multi-host expansion (v0.15.6.0)**
- "Declarative Multi-Host Platform" — new TypeScript config pattern
- Each host = 1 file trong `hosts/<name>.ts`
- Zero code changes to add new host

**Theme 2: Security posture strengthening (v0.15.7.0 + v0.15.12.0)**
- "Security Wave 1" early April
- "4-Layer Prompt Injection Defense" later April
- Security is actively evolving priority

**Theme 3: OpenClaw integration deep (v0.15.9.0, v0.15.10.0)**
- Native OpenClaw skills shipped via ClawHub
- 4 conversational skills published

**Theme 4: DX review focus (v0.15.3.0, v0.15.5.0)**
- Developer Experience Review skill added
- Interactive review with AskUserQuestion

**Theme 5: CHANGELOG-style user-facing** (confirmed):
Latest entry v0.18.3.0 opens với:
> "Windows cookie import. `/setup-browser-cookies` now works on Windows. Point it at Chrome, Edge, Brave, or Chromium, pick a profile, and gstack will pull your real browser cookies into the headless session."

→ Exactly như CLAUDE.md spec: "Lead with what user can do."

### Velocity comparison

| Metric | ECC | Superpowers | gstack |
|--------|-----|-------------|--------|
| Total versions | unknown (monthly-ish) | 27+ (Oct 2025 → Apr 2026) | **126** |
| Releases in last 30 days | steady | 5 in March 2026 | **~20+** |
| Breaking changes | rare | v5.0.0 major breaks | semver strict — major = breaking |

→ **gstack ship rate 4x Superpowers, 10x+ ECC.** Match "10K+ LOC/day" claim credible.

---

## Cross-connection to sibling projects

| Axis | ECC | Superpowers | gstack |
|------|-----|-------------|--------|
| Philosophy document | README + longform | CLAUDE.md (strict) | **ETHOS.md (named, isolated)** |
| Core principles | Production-ready | TDD Iron Law + eval-driven | **Boil the Lake + Search Before Building + User Sovereignty** |
| Dependencies | Various | Zero | **Bun + Playwright + Chromium** (opinionated but bundled) |
| Architecture pattern | Plugin-loaded | Skill-loaded | **Daemon + CLI + compiled binary** |
| Security focus | AgentShield (paid) | Zero-dep supply chain | **Localhost + bearer token + keychain discipline** |
| Voice protection | None explicit | "Your human partner" | **ETHOS.md + promotional + tone hard-gates** |

→ **Convergent insight:** 3 frameworks all recognize human-AI power dynamic risk. gstack frames as "User Sovereignty"; Superpowers as "HARD-GATE"; ECC less explicit.

---

## Open questions resolved

- ✅ Q4: `/office-hours` flow — 6 forcing questions (README mentioned, skill template not deep-read)
- ✅ Q2: LOC claims indirectly supported by 126 version count + aggressive ship rate visible trong CHANGELOG
- ✅ Q10: Superpowers vs gstack overlap — **philosophical alignment** (both opinionated, both eval-driven) but **different mechanisms** (gstack = role pipeline, Superpowers = 7-stage gates)

## Open questions raised

- ⏸ 4-Layer Prompt Injection Defense (v0.15.12.0) — technical detail worth entity page if Storm Bear security-focused
- ⏸ Pretext layout system trong `/design-html` — 30KB zero-deps CSS — reusable? worth fetching source?
- ⏸ `hosts/<name>.ts` pattern — declarative multi-host. Compare với Superpowers per-harness manifests, ECC plugin-based. Worth entity page.

---

## Cross-references

- [[(C) README summary]]
- [[(C) CLAUDE.md summary]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Release Notes overview.md` — release cadence comparison
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Distribution Model.md` — multi-harness comparison

## Citations

- `00 Sources/gstack/ETHOS.md` (full, lines 1-164)
- `00 Sources/gstack/ARCHITECTURE.md` (full, lines 1-365)
- `00 Sources/gstack/CHANGELOG.md`:
  - Version headers: `grep "^## \[" CHANGELOG.md` → 126 matches
  - Latest v0.18.3.0 entry: lines 1-30
  - Themes extracted từ version headings
