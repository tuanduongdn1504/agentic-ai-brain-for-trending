# Skills supply chain — second production observation (+ the `.well-known` mechanism)

## Source

- `gh api` tree + content fetches of adrianhajdin/react-native-lingua (2026-07-03, main-loop ground-truth); live fetch of https://visionagents.ai/.well-known/skills/index.json; transcript skill-install moments (02:25 Stream, 02:48 Vision Agents, PostHog wizard 02:00).

## What the repo ships (primary evidence)

- **`skills-lock.json` (version 1) with 21 skills from 4 sources:**
  - `expo/skills` ×10 (building-native-ui, expo-api-routes, expo-tailwind-setup, expo-deployment, eas-update-insights, expo-cicd-workflows, expo-dev-client, native-data-fetching, upgrading-expo, …) — **Expo publishes official vendor skills**
  - `clerk/skills` ×6 (clerk, clerk-setup, clerk-backend-api, clerk-custom-ui, clerk-expo-patterns, clerk-webhooks)
  - `GetStream/agent-skills` ×5 (stream, stream-builder, stream-cli, stream-docs, stream-react-native)
  - **`visionagents.ai` ×1 — `"sourceType": "well-known"`** (the others are `"github"`), each entry hash-locked (`computedHash` sha256)
- **`.agents/skills/` committed in full** — skills ship rich payloads: `references/*.md`, `templates/` (full Expo auth app), executable `scripts/*.sh`, and **`evals/evals.json`** (Clerk ships evals inside its skills — vendor skills are becoming tested artifacts, cf. [[prompt-evaluation/_index|prompt-evaluation]]).
- **`.claude/skills/*` symlinks (mode 120000) → `.agents/skills/*`** — the same Claude-Code bridge as ghost-ai.
- **One real (non-symlink) skill: `.claude/skills/integration-expo/` containing a `.posthog-wizard` marker** — the **PostHog wizard installed a skill** into `.claude/skills/` as part of setup. A second, independent skill-injection channel: setup wizards, not just `npx skills`.
- **Committed Claude Code auto-memory**: `.claude/projects/-Users-adrianhajdin-Desktop-duolingo-clone/memory/{MEMORY.md, project_clerk_api.md, project_lesson_screen.md}` — index + API-version pin + progress state. First corpus sighting of the auto-memory directory published in a repo ([[when-ai-knowledge-ends]]).

## The `.well-known` domain mechanism — VERIFIED end-to-end

1. Video command: `npx skills add https://visionagents.ai` (02:48, before scaffolding the Python service).
2. Live endpoint (fetched 2026-07-03): `https://visionagents.ai/.well-known/skills/index.json` returns `{"skills":[{"name":"agent", "description":"…", "files":["SKILL.md"]}]}`.
3. Lockfile records `"agent": {"source": "visionagents.ai", "sourceType": "well-known", "computedHash": "7eff513f…"}`.
4. Installed artifact committed at `.agents/skills/agent/SKILL.md` — frontmatter `metadata: mintlify-proj: agent` ⇒ the skill is **generated/served by Mintlify**, the docs platform. **Docs-platforms are becoming skill registries**: any vendor on Mintlify can expose an agent skill at a well-known URL.

⚠️ Three workflow verifiers REFUTED this mechanism ("Python-only, no SKILL.md, no npm package, aspirational framing, would fail") — **overridden** by the lockfile + live endpoint + committed artifact. They probed `/skill.md`, `/skills.json`, `/.well-known/skills` and missed `/.well-known/skills/index.json`, then over-generalized from "Vision Agents is a Python framework" (true) to "the domain serves no skill" (false). Logged in [[source-provenance]]; the recurring wiki-verify misfire pattern.

## Delta vs the first observation ([[jsm-six-file-context/skills-supply-chain|ghost-ai]])

| | ghost-ai (web, 2026-05-01) | react-native-lingua (mobile, 2026-05-15) |
|---|---|---|
| Lockfile | skills-lock.json | skills-lock.json (same v1 format) |
| Sources | 4 vendor GitHub repos | 3 vendor GitHub repos **+ 1 well-known domain** |
| Skill count | ~handful | **21** |
| .claude bridge | symlinks | symlinks **+ wizard-installed real dir** |
| Extras | — | **evals.json inside vendor skills; committed auto-memory** |

Two JSM productions two weeks apart, same supply chain, growing surface — this is becoming JSM house style, and at 1M+ subs it's mass-market default-setting. Queue for the Storm Bear Pattern-Library skills-thread (Pattern #18 Layer-2 / v66+ audit): the declarative-skills-dependency-management candidate now has N=2 same-author + a novel resolution mechanism (well-known domains).

## Key Takeaways

- Second production instance of `npx skills` + skills-lock.json + `.agents/skills` + `.claude` symlinks — now with hash-locking across 21 skills from 4 vendors.
- NEW mechanism confirmed: **well-known domain skills** (`/.well-known/skills/index.json`), with Mintlify auto-serving them for docs sites.
- NEW channel: setup wizards (PostHog) install skills directly into `.claude/skills/`.
- Vendor skills now carry references, templates, executable scripts, and **evals** — supply-chain surface area (and trust burden: executable `.sh` in skills!) keeps growing; compose with the vault's install-snapshot/npm-security-check discipline before adopting.
- Skills are still not auto-consulted every turn — the prompt pointer remains load-bearing ([[jsm-six-file-context/caveats-and-corrections|prior caveat holds]]).
