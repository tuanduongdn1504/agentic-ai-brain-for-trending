# Original: MCP Builder skill + the Model Context Protocol (→ MCP Builder)

*The basis for Ben AI's #8: `mcp-builder` is a genuine, official Anthropic skill — it scaffolds a custom MCP server from a target API's docs.*

## Correction up front (Rule 12 — fail loud)

An earlier draft of this article claimed "MCP Builder is FALSE / not a real Anthropic skill." **That was wrong** — it was written when the dedicated research agent crashed ("prompt too long"), so the verifier guessed with no data. **Direct verification (GitHub API, 2026-06-20) confirms `mcp-builder` IS one of the official skills in [github.com/anthropics/skills](https://github.com/anthropics/skills).** Ben's "built-in Anthropic skill" framing is correct. The full official skill list at verification time:

`algorithmic-art · brand-guidelines · canvas-design · claude-api · doc-coauthoring · docx · frontend-design · internal-comms · `**`mcp-builder`**` · pdf · pptx · skill-creator · slack-gif-creator · theme-factory · web-artifacts-builder · webapp-testing · xlsx`

Note this list also confirms two other things Ben mentions: the **`skill-creator`** skill ("Claude's built-in skill creator") and **`frontend-design`** (the official analog of his #6 Front-end Slides).

## What MCP is

- **Model Context Protocol (MCP)** = an open standard (published by Anthropic, now adopted across 20+ agent platforms) for connecting an AI agent to external tools, data, and services.
- **Architecture:** an **MCP client/host** (Claude Code, Cowork, claude.ai, the API) talks to one or more **MCP servers** (a process wrapping GitHub, Slack, Postgres, or any custom API).
- **A server advertises three capability types:**
  - **Tools** — callable functions (e.g. `create_issue`, `send_message`)
  - **Resources** — readable data (files, query results)
  - **Prompts** — reusable instruction templates
- **Why it exists:** write the connector once as an MCP server and it works across every MCP-speaking agent — no per-tool, per-vendor reimplementation. (Skills and MCP are *distinct* primitives: a skill is filesystem-based instructions/procedure; an MCP server is an external connector. Ben's #8 is the skill that *generates* the latter.)

## What the `mcp-builder` skill does

Per Ben's demo + the skill's purpose:

1. You ask Claude to "use the MCP Builder skill to build an MCP server for `<software>`."
2. It reads the target's **API documentation** and asks you a few **capability questions** (which endpoints/actions you need, auth, etc.).
3. It outputs:
   - the **MCP server code**,
   - a **step-by-step install guide**, and
   - a **JSON config snippet** to register the server.
4. You add that JSON to the **Claude config file** — Ben's path: *Settings → Developer → Edit Config* (a JSON file you can open in any editor; if unsure, paste it back to Claude and ask it to merge). Once added, the connector appears in your connector list.

**Ben's examples:** he built MCP servers for **Circle.so** (his community platform — has an API, no official MCP) and **Reddit** (for YouTube ideation). ⚠️ His specific server implementations aren't public, so output quality/coverage isn't independently verified — but the workflow and the skill are real.

## Manual MCP config (the non-skill baseline)

Without the skill you wire servers by hand. In Claude Code, an `mcpServers` block (in `~/.claude.json` / project `.mcp.json` / settings):

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "ghp_..." }
    }
  }
}
```

The `mcp-builder` skill's value is producing both the *server* and this *config* for an API that has no off-the-shelf server.

## Why this matters for the operator

- **hireui (Goal #2):** a recruitment SaaS will need agents to reach an ATS / HRIS / Slack / calendar. Where no official MCP exists, `mcp-builder` is the standard way to wrap those APIs — generate the server from the API docs, then security-review before trusting it (treat output as a scaffold, not ship-ready). See the pilot menu.
- **The vault:** for sources without a clean connector (a niche API, an internal tool), `mcp-builder` can stand up an MCP server the autopilot pipeline can call — complementary to the existing yt-dlp / WebFetch ingestion paths.
- Composes with the broader connector/decoupling discussion in [[cowork-third-party-inference/_index]] and [[harness-engineering/_index]].

## Key Takeaways

- **`mcp-builder` is a real, official Anthropic skill** (verified in `anthropics/skills`, 2026-06-20) — Ben's #8 claim holds.
- **MCP ≠ Skill:** MCP is an external-connector protocol; a skill is filesystem-based instructions. `mcp-builder` is the skill that *writes an MCP server*.
- **The build flow** = read API docs → ask capability Qs → emit server code + install steps + JSON config → paste into the Claude config file.
- **Treat generated servers as scaffolds** — security-review (secrets handling, input validation, error handling) before production, especially for PII-bearing systems like hireui.

## Source

- **Verification:** `github.com/anthropics/skills` contents via GitHub API (2026-06-20) — `mcp-builder` directory confirmed.
- **Protocol:** `modelcontextprotocol.io` (open standard, Anthropic-published).
- **Video:** Ben AI, "8 Claude Skills I Can't Live Without" (`bXnRA3pJavE`, 2026-04-18) — MCP Builder = Skill #8.

## See also

- [[claude-skills/original-anthropic-agent-skills]] — skills vs MCP (distinct primitives)
- [[claude-skills/the-eight-meta-skills]] · [[claude-skills/video-to-original-crosswalk]] · [[claude-skills/source-provenance]]
- [[harness-engineering/_index]] · [[multi-agent-orchestration/_index]] · [[cowork-third-party-inference/_index]]
