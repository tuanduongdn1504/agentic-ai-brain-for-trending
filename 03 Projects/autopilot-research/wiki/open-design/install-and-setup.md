# Install & setup

## Source

`nexu-io/open-design` README + `QUICKSTART.md` (gh-api / WebFetch, 2026-07-01) + the video (chapter *Installing Open Design* 07:31). Workflow `wf_4a91a8b2-2bb` agents `opendesign-usage`, `license-security`. **Read the safety section before running anything** → [[open-design/caveats-and-safety]].

## Two install paths

### A. Native desktop app (recommended for a first look)

Download a prebuilt binary from GitHub Releases / [open-design.ai](https://open-design.ai):
- **macOS** — Apple Silicon **and** Intel
- **Windows** — x64
- **Linux** — AppImage (optional release lane)

"Supposedly you don't need to install any other dependencies if you go this route" (video). The DMG is ~200 MB.

### B. From source (what the video did — but the commands have drifted)

**Current documented path** (`QUICKSTART.md`, uses **pnpm**, Node ~24, pnpm 10.33.x pinned via `packageManager`):

```bash
git clone https://github.com/nexu-io/open-design
cd open-design
corepack enable
pnpm install
pnpm tools-dev run web      # launches the daemon + web UI on a localhost port
```

**What the video actually ran (2026-05-05, npm — likely an earlier state):**

```bash
git clone …            # repo ~100 MB
cd open-design
corepack enable
corepack npm --version # → 10.33.2
npm install            # ~20–30s
npm run dev            # ("npm tools dev" in the transcript) → opens localhost:<port>
```

⚠️ **Prefer the current pnpm path.** The npm commands in the video reflect the repo's state ~7 days after creation; the pinned package manager is now pnpm. If npm complains, that's expected — switch to `corepack enable && pnpm install`.

## First run

1. The daemon **PATH-scans** for coding-agent CLIs and shows what it found (the video detected **Claude Code, OpenCode, Copilot CLI, Kilo**).
2. **Pick a default model/CLI** — leave it CLI-driven, or force a specific model (e.g. Opus). No CLI? Use the **BYOK proxy** (paste an endpoint + key).
3. **Optionally add media-provider keys** (Suno / Midjourney / Fal / ElevenLabs / OpenAI GPT-image / MiniMax) and MCP connectors (**Composio**).
4. **Toggle skills + design systems** in settings; defaults to a `web-prototype` skill + a "Neutral Modern" design system.
5. Point it at a **project folder** — designs are stored per-project, locally.

## Wiring it into an existing agent (MCP)

```bash
od mcp install <agent>       # e.g. od mcp install claude-code
od mcp install <agent> --print     # dry-run: show what it would write
od mcp install <agent> --uninstall
```

This registers Open Design's MCP stdio server into the agent's config so a coding-agent session can query Open Design's skills/design-systems. → [[open-design/architecture-and-byoa]]

## Safety precautions before you `install` (do these)

Open Design is a **~2-month-old, 73K★, virally-growing** repo with a **postinstall script** and a **local daemon that spawns your coding-agent CLI**. That combination warrants the vault's install hygiene:

1. **Run `/npm-security-check`** on the package before `pnpm install` (the postinstall was verified network-free by a skeptic, but re-check for your version).
2. **Compose `install-snapshot`** so you have a clean uninstall diff (it writes a daemon data dir + config).
3. **Neutralize telemetry:** the README says "no telemetry" but the code has **opt-in PostHog** (no-op unless `POSTHOG_KEY` is set). Confirm `POSTHOG_KEY` is unset / disable telemetry in settings after first run.
4. **Keep it loopback:** leave `OD_BIND_HOST` unset (defaults to `127.0.0.1`); do **not** expose via a reverse proxy — the README's "SSRF protection" was **not confirmed in the code** a skeptic read, so loopback binding is your real mitigation.
5. **Pilot in a sandbox, not production:** it spawns your Claude Code CLI, which can edit files. Run it against a **mirror/staging copy** of hireui (or a throwaway `agent-*` worktree per hireui's I-2), never production data on day one. For hireui specifically, tool installs are the **operator's** job per its I-8 registry rule.

Full risk treatment: [[open-design/caveats-and-safety]].

## Key Takeaways

- Two paths: **native desktop binary** (macOS AS+Intel / Windows x64 / Linux AppImage) or **from source**.
- **From-source uses pnpm now** (`corepack enable && pnpm install && pnpm tools-dev run web`) — the video's `npm install / npm run dev` is stale (early-state).
- First run **PATH-scans your CLIs**, you pick a default (or BYOK proxy), toggle skills/design-systems, and point it at a project folder (local-per-project storage). Wire into agents with **`od mcp install <agent>`**.
- **Do the install hygiene:** `/npm-security-check` + `install-snapshot`, unset `POSTHOG_KEY`, keep it loopback, and sandbox-pilot (never production data first) — especially inside hireui, where installs are operator-gated (I-8).
