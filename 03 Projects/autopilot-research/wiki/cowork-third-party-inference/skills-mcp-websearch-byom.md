# Skills, MCP, and web search with non-Claude models

When you use a third-party model (Ollama, OpenRouter, etc.) with Cowork on 3P, you gain cost control and data sovereignty but lose access to Claude's built-in capabilities. This article covers what's missing and how to restore it.

## Source

- Video: Bart Slodyczka, "Claude Cowork + Ollama = 100% FREE & PRIVATE" (YouTube ME4flXK_6tQ, 2026-04-25, 18:41)
- Transcript: `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md`
- Anthropic: [Skills repo](https://github.com/anthropics/skills), [Cowork on 3P gateway docs](https://claude.com/docs/cowork/3p/gateway)
- Model Context Protocol: [modelcontextprotocol.io](https://modelcontextprotocol.io), [Brave Search MCP](https://github.com/brave/brave-search-mcp-server)
- Brave Search: [API setup guide](https://brave.com/search/api/guides/use-with-claude-desktop-with-mcp/)
- Ollama: [Anthropic Messages API support (January 2026)](https://ollama.com/blog)

---

## What you lose with non-Claude models

**Skills:** Paid Cowork bundles Anthropic's official skills (PDF, Excel, Word, PowerPoint, etc.). Cowork on 3P does not auto-include them.

**Web search:** Claude's Sonnet and Opus models have built-in web search. Non-Claude models (Gemma, Llama, MiniMax) have none.

**Harness training:** Non-Claude models aren't trained on Claude Desktop's internal system prompting and harness instructions. They struggle to drive the desktop app consistently, causing skill failures and retry loops.

**Note:** Claude Code (the CLI tool) does not support third-party inference gateways at all as of June 2026. Cowork 3P is for the Claude Desktop app only. If you need Claude Code with non-Anthropic models, consider using Ollama directly with `ANTHROPIC_BASE_URL` environment variables instead.

---

## How to restore skills

Skills must be manually imported in Cowork on 3P (unlike paid Cowork).

**Steps:**

1. Download the official Anthropic skills repository as a zip:
   - Go to [github.com/anthropics/skills](https://github.com/anthropics/skills)
   - Click the green code button and select "Download ZIP"

2. Extract the zip. Navigate to the `skills/` folder. You'll see individual skill folders: `pdf/`, `pptx/`, `xlsx/`, `docx/`, etc.

3. Right-click the desired skill folder (e.g., `pptx/` for PowerPoint) → **Compress** to create a `.zip` file of that folder alone.

4. Drag the `.zip` file into Claude Cowork's main window.

5. Verify the skill appears in the **Customize** panel under **Skills** section.

**Note:** If a new MCP connector or skill doesn't appear immediately, close and relaunch the Cowork app.

---

## How to restore web search via Brave Search MCP

Non-Claude models lack native web search. Restore it by configuring Brave Search as an MCP (Model Context Protocol) server.

### Prerequisites

- Brave Search API account (free tier: 2,000 queries/month)
- Access to Claude Desktop's configuration file

### Setup

1. **Get a Brave API key:**
   - Visit [brave.com/search/api/](https://brave.com/search/api/)
   - Create an account and generate an API key
   - Copy the key value

2. **Locate Claude Desktop config file:**
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

3. **Edit the config file to add Brave Search MCP:**
   - Open the file in a text editor
   - Find or create the `mcpServers` section
   - Add the Brave Search MCP block:
     ```json
     "mcpServers": {
       "brave-search": {
         "command": "npx",
         "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "http"],
         "env": {
           "BRAVE_API_KEY": "YOUR_API_KEY_HERE"
         }
       }
     }
     ```
   - Replace `YOUR_API_KEY_HERE` with your actual Brave API key
   - Save the file

4. **Reload Cowork:**
   - Close and reopen Claude Cowork
   - The Brave Search MCP should now appear in the **Developer** > **Settings** panel under **MCP connections**

5. **Disable the built-in web_search tool (critical):**
   - Go to **Sandbox** > **Workspace**
   - Look for the list of tools available to the model
   - **Disable** `web_search` (the built-in one)
   - This forces the model to use the Brave Search MCP instead of trying the non-existent built-in tool

**Test it:** Ask your model "Can you Brave search the latest AI news?" and confirm it returns current results.

---

## Why non-Claude models struggle with skills

The video demonstrates that non-Claude models (Gemma, MiniMax, etc.) often fail when executing skills, entering retry loops instead of completing the task in one shot.

**Root cause:** These models are not trained on Claude Desktop's harness. The desktop app sends underlying system prompting and harness-specific instructions with each request. Claude models (Opus, Sonnet) understand these instructions natively. Third-party models do not.

**Workaround (from the video):**

1. Run the skill once and let it fail
2. Inspect the failure logs (visible in Claude's console)
3. Ask the model directly: "I see you're struggling with this skill. Can you look at the error and tell me how to fix it so it works on the next attempt?"
4. The model corrects itself and learns the skill's quirks
5. On the second run, it usually executes without looping

This is a mitigation, not a fix. If a skill is critical to your workflow, consider using a Claude model (via paid Cowork or optimized API calls) instead.

---

## Note on Ollama setup and HTTP vs. HTTPS

The video demonstrates using Tailscale Serve to bridge Ollama's HTTP endpoint to HTTPS, which Anthropic's gateway requires. However, as of January 2026 (before the video's publication), Ollama v0.14.0 added native Anthropic Messages API support, eliminating the need for a Tailscale bridge for local development setups.

If you're using a recent version of Ollama, you may be able to point Cowork directly at `http://localhost:11434` without the HTTPS bridge. Test with your current setup; if the gateway requires HTTPS, the Tailscale approach shown in the video remains valid.

---

## Key Takeaways

- **Skills are manual:** Download Anthropic's GitHub skills repo, zip individual skill folders, drag into Cowork on 3P
- **Web search requires MCP:** Configure Brave Search MCP in Claude Desktop's config file with your API key
- **Disable built-in web_search:** Set it as disabled in Sandbox > Workspace so the model routes to Brave instead of failing
- **Non-Claude models need training:** Skills will fail on first attempt; run once, inspect failure, ask model to self-correct, re-run
- **Claude Code limitation:** As of June 2026, Claude Code does not support third-party inference gateways; use Cowork on 3P instead
- **Mitigation is temporary:** Heavy skill usage favors paid Cowork with Claude; 3P is best for light skill use + strong cost discipline

---

## Related articles

- tailscale-https-bridge.md — Setting up a local HTTPS tunnel for Ollama
- [[harness-engineering|Harness engineering]] — Why separating desktop harness from model matters
- [[claude-api-cost-optimization|Claude API cost optimization]] — Trade-offs between Cowork 3P, paid Cowork, and optimized API calls
