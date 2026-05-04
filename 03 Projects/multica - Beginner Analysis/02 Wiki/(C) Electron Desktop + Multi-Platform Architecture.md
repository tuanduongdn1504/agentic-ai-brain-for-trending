# (C) Electron Desktop + Multi-Platform Architecture

> **Type:** Entity — novel architecture (first desktop app in corpus)
> **Parent:** [[(C) index]]
> **Sources:** [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] §2 (architecture + cross-platform rules + desktop-specific rules); root structure analysis
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

multica is the **first Storm Bear corpus project with a native Electron desktop app** alongside web UI. The architecture enforces **strict cross-platform discipline** via shared `packages/views` that work identically in Next.js 16 web and Electron desktop contexts, with platform-specific wiring isolated in `apps/*/platform/`. This dual-app strategy reflects multica's commitment to always-on agent workflows where web alone is insufficient. The **5 cross-platform rules** + **desktop-specific rules** in CLAUDE.md constitute the most granular dual-platform discipline in corpus.

## 2. Key claims

1. **Dual-app architecture:** `apps/web/` (Next.js 16) + `apps/desktop/` (Electron via electron-vite)
2. **Shared packages layer:** `packages/views/` used identically by both apps
3. **Cross-platform rules (5) NON-NEGOTIABLE** — shared code must work in both contexts
4. **Desktop-specific rules (5)** — session routes / transition flows / error states / workspace singleton / drag strip
5. **FIRST corpus project with native desktop** — unique differentiator
6. **electron-vite** build tooling — modern replacement for electron-forge / electron-builder
7. **Always-on use case** — desktop enables persistent daemon connection for agent monitoring

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| Dual apps | Root structure (apps/web + apps/desktop) | High |
| electron-vite | CLAUDE.md | High |
| 5 cross-platform rules | CLAUDE.md §Cross-Platform Rules | High |
| 5 desktop-specific rules | CLAUDE.md §Desktop-Specific Rules | High |
| Electron first in corpus | 15-wiki retrospective scan | High |

## 4. How it works — dual-app shared architecture

### Package boundary discipline (from CLAUDE.md)

```
packages/views/<domain>/
  ├── page.tsx               # Shared between apps
  ├── components/
  ├── hooks/
  │   └── useWorkspaceId()  # ← NO: don't call in shared code
  └── types.ts

apps/web/
  ├── app/<domain>/
  │   └── page.tsx           # Wires packages/views with Next.js routing
  └── platform/
      ├── useNavigation()    # Next.js implementation
      └── useWorkspaceId()   # Next.js implementation

apps/desktop/
  ├── renderer/<domain>/
  │   └── page.tsx           # Wires packages/views with Electron routing
  └── platform/
      ├── useNavigation()    # Electron implementation
      └── useWorkspaceId()   # Electron implementation
```

### 5 non-negotiable cross-platform rules

From CLAUDE.md verbatim:
1. **Add component to `packages/views/<domain>/`**
2. **Wire route in BOTH `apps/web/` AND `apps/desktop/`**
3. **Use `useNavigation().push()`** (never framework-specific APIs in shared code)
4. **Accept `wsId` as parameter** in hooks, don't call `useWorkspaceId()` internally
5. **Platform chrome** (drag strips, tab system) stays in app-specific code

**Implication:** shared code is platform-agnostic by construction. Platform-specific code is isolated in `apps/*/platform/`.

### Shared code sophistication

`packages/views` needs:
- No Next.js imports (`next/*` forbidden per constraint)
- No React Router (`react-router-dom` forbidden)
- No store access directly (receive via props)
- No framework-specific routing API

**This is aggressive architectural isolation.** Most projects don't enforce at package-boundary level.

## 5. Desktop-specific rules

From CLAUDE.md:

### Rule 1 — Route categories (3)
Routes fall into exactly 3 categories:
- **Session routes** — workspace-scoped (most content)
- **Transition flows** — pre-workspace (create workspace, accept invite)
- **Error states** — error boundary catches

### Rule 2 — Transition flows are NOT routes
Transition flows (e.g., "create workspace" modal) = `WindowOverlay` state, NOT browser route.

**Why:** Electron window state ≠ browser URL. Overlay is Electron-native UI primitive.

### Rule 3 — Workspace singleton
`setCurrentWorkspace(slug, uuid)` = **singleton source of truth** for current workspace. All code reads from this singleton.

### Rule 4 — Destructive operation sequence
Destructive operations must follow order:
1. **Clear workspace** (singleton)
2. **Navigate** (route change)
3. **Mutate** (API call)

**Why this order:** prevents stale workspace pointing to deleted data.

### Rule 5 — macOS window-move (drag strip)
Full-window views need **top drag strip** for macOS window-move capability.

**Why macOS specific:** macOS windows typically drag from title bar; custom full-window UI needs explicit drag zone.

## 6. Why desktop in addition to web

### Technical drivers

1. **Always-on daemon connection** — Electron stays running in tray, web tab may close
2. **Native notifications** — macOS/Windows system notifications on agent task completion
3. **File system deep access** — more direct than browser sandboxing
4. **Global keyboard shortcuts** — ⌘K-style palette works from anywhere
5. **Offline capability** — Electron can cache state, browser can't

### Product drivers

1. **"Real teammates" framing** — teammates live in chat apps, email, not browser tabs
2. **Workflow centrality** — agent coordination is constant task, not visit-based
3. **Team collaboration UX** — Slack-style always-present vs web-tab transient

### Contrast

- paperclip v14: server + UI, runs locally via `pnpm dev`, web UI in browser — no native app
- goclaw v4: CLI + web — no desktop
- **multica v15: CLI + web + Electron desktop** — most surfaces in corpus

## 7. Edges + failure modes

### Architectural risks

- **Shared-code drift** — `packages/views` accidentally imports platform API → breaks other app. Mitigation: lint rules + type errors.
- **Platform behavior divergence** — `useNavigation` in web vs desktop must behave identically. Testing required per-platform.
- **Electron-Next.js version skew** — Electron renders Next.js outputs; version mismatches possible.

### Desktop-specific risks

- **Workspace singleton bugs** — stale pointer = cross-workspace data leak
- **Drag strip platform variance** — macOS/Windows/Linux different; strip might be ignored
- **Electron memory** — desktop apps ~100-300MB vs web tab ~50MB

### Deployment risks

- **Electron auto-updater** — not mentioned in CLAUDE.md; unknown
- **Code signing** — macOS requires notarization; Windows SmartScreen
- **Distribution** — Homebrew handles CLI; desktop distribution path TBD

## 8. Related concepts

- [[(C) Linear-Analog Task Management for Agents]] — what the dual app exposes
- [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] — discipline context
- [[(C) Skills + Architecture + skills-lock cluster summary]] — broader tech stack

## 9. Cross-project comparison

### vs paperclip v14 (explicit competitor)

| Aspect | paperclip | multica |
|--------|-----------|---------|
| Desktop app | ❌ | ✅ Electron |
| Web UI | ✅ React | ✅ Next.js 16 |
| CLI | ✅ | ✅ |
| Always-on UX | Self-hosted server persistent | Desktop app tray |
| Distribution | Docker + npm | Homebrew + Desktop binary + Cloud |

→ multica has **broader UX surface**. paperclip's self-hosted server requires active browser tab; multica desktop achieves always-on natively.

### vs T1 IDE plugins (e.g., BMAD, codymaster)

- BMAD/codymaster etc live inside IDE (Claude Code / Cursor)
- multica desktop = **standalone app** (not IDE-dependent)
- Different use case: IDE plugins augment coding; multica desktop orchestrates agent work cross-IDE

### vs Linear (inspiration)

- Linear has web + desktop (Electron) + mobile
- multica currently web + desktop (mobile roadmap possibly)
- Linear paradigm native to multi-platform = multica inherits UX strategy

## 10. Open questions

- Electron auto-update mechanism? (new — Q40)
- Code signing strategy? (new — Q41)
- Desktop binary distribution (GitHub releases? own CDN?) (new — Q42)
- Mobile app roadmap? (new — Q43)
- Offline capability extent (new — Q44)
- tray-icon vs dock-only (macOS convention)? (new — Q45)

## 11. Decision log

- **Early versions:** likely web-only
- **v0.2.x:** Electron desktop added (apps/desktop/)
- **electron-vite choice:** modern build tooling (vs electron-forge / electron-builder)
- **5 non-negotiable rules:** codified to prevent drift
- **Future:** potential mobile; native macOS Swift?

## 12. Storm Bear relevance

### Desktop-app precedent for Storm Bear

Storm Bear vault is Obsidian (Electron-based). multica's desktop pattern = **reference architecture** for any future Storm Bear companion tool.

### Scrum team tool comparison

Scrum teams often use multiple tools:
- Linear / Jira — task management
- Slack / Teams — communication
- Confluence — docs
- Figma — design

multica desktop could replace Linear + partially replace Slack (agent status updates). Storm Bear should evaluate as one-tool-many-workflows option.

### Dev-ops recommendation

If Storm Bear pilots multica for personal productivity:
- Install CLI via Homebrew
- Install desktop app (when available in distribution)
- Use web for occasional access
- Evaluate Linear-replacement potential

## 13. References

- CLAUDE.md §Architecture Overview + §Cross-Platform Rules + §Desktop-Specific Rules
- Root structure (apps/web + apps/desktop)
- Parent: [[(C) index]]
- electron-vite documentation (cited, not fetched)
