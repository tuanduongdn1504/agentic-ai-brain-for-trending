# Original: skills.sh ecosystem (→ Find Skills)

*Deep-dive the skills.sh marketplace behind Ben AI's #5 Find Skills meta-skill, including ecosystem scale, supply-chain security, and vetting framework for third-party skill installations.*

## What is skills.sh?

skills.sh is **The Open Agent Skills Ecosystem**, a marketplace for reusable AI agent capabilities built by Vercel. It indexes ~788,000+ total skill installs across 20+ agent platforms including Claude Code, Cursor, GitHub Copilot, Gemini CLI, and 40+ others. The platform hosts hundreds of unique skills, ranked by installs, activity, trends, and topics. Skills are discovered via leaderboard browse, search, topic navigation, or trending filters (24h/All-Time/Hot).

**Top skills by installs** (as of 2026-06-20):
- find-skills: 2.1M+ installs (meta-skill that discovers other skills)
- frontend-design: 567.8K installs
- Microsoft Azure tools: highly installed
- Official Anthropic built-ins (PPTX, XLSX, DOCX, PDF creation): pre-installed

## Installation Model

**CLI-based discovery & install:**
```bash
npx skills add <owner/repo>
# e.g., npx skills add vercel-labs/skills
```

**Installation locations:**
- Project-scoped: `.claude/skills/` directory (project-only)
- Global-scoped: `~/.claude/skills/` directory (all projects)
- Claude Code auto-discovery: SKILL.md files detected in next session; no manual upload needed

**Claude.ai (Web UI):**
- Settings > Features > Skills > Upload as ZIP
- Requires code execution enabled
- User-scoped only (not org-wide)

**Discovery mechanisms:**
1. skills.sh leaderboard + search (direct browsing)
2. Claude Code "Find Skills" built-in search (if skill installed)
3. GitHub raw repos (many authors publish SKILL.md without registry listing)

## The "91,000+ skills" Claim — ⚠️ Unverified

Ben AI's video claims "more than 91,000 skills" in skills.sh. However, skills.sh reports ~788,224 **total installs** as of 2026-06-20, with actual unique-skill counts ranging 1,000–4,200 depending on platform scope. The original 91K figure appears outdated (~8.6x growth since April 2026 video) or conflates install-count with unique skills.

**Recommendation:** Rely on current install-counts + GitHub star-count (maturity signal) rather than marketplace-wide claims. Most-installed skills are typically official (Anthropic, Vercel) or high-velocity community entries.

## Supply-Chain Security & Vetting Framework

### The Vulnerability Landscape

**Snyk security audit (Feb 5, 2026) of 3,984 audited skills:**
- **36.82%** (1,467 skills) had at least one security flaw
- **13.4%** (534 skills) had CRITICAL-level vulnerabilities
- **76 active malicious payloads** identified; 8 publicly available at publication date

### Eight Vulnerability Categories

1. **Prompt injection** — 91% of malicious samples; invisibly alters Claude behavior
2. **Malicious code** — 100% confirmed destructive (not misconfiguration)
3. **Suspicious downloads** — 10.9% downloading unknown binaries
4. **Hardcoded secrets** — 10.9% embedding API keys/credentials
5. **Insecure credential handling** — 7.1% exposing tokens in logs/memory
6. **Third-party content exposure** — 17.7% fetching unvetted external content
7. **Unverifiable dependencies** — 2.9% depending on unsigned packages
8. **Direct financial account access** — 8.7% requesting card/banking integration

### Execution Permissions Reality

Skills execute with dangerous permissions by design:
- Shell access to machine
- Read-write file system
- Credential access (ENV variables, git config, ssh keys)
- Persistent memory modification

**Vetting is your responsibility.** No automated mechanism exists in Claude Code today.

### Pre-Installation Vetting Framework

**Tier 1 — Metadata signals (30 sec):**
- GitHub repo age (>6 months preferred)
- Star count (>100 stars = community review; <10 = unvalidated)
- Contributor diversity (multiple = distributed review; single = higher risk)
- Last commit recency (stale >6 months = unpatched)
- License present (MIT/Apache-2.0 preferred; no license = red flag)

**Tier 2 — SKILL.md code inspection (2–5 min):**
Look for red flags:
- Hardcoded secrets (API keys, tokens, passwords)
- Shell execution (`shell()`, `system()`, `exec()`) — verify necessity
- Network requests (`fetch()`, `HTTP`, `curl`) — check domain + exfiltration patterns
- File writes outside skill directory
- Credential access (`process.env`, `os.environ`, git config reads)
- Runtime package installation (red flag—must be pre-installed)
- Example outputs showing unusual behavior

**Tier 3 — Sandbox testing (5–15 min):**
- Install in isolated project
- Test with benign input ("hello world")
- Observe behavior, network calls, file creation
- Check `.claude/` and project files post-execution
- Review Claude's tool calls for suspicious patterns

**Tier 4 — Threat model (for sensitive tasks):**
- What data does this process? (source code, credentials, financial?)
- Blast radius if compromised?
- Author trustworthiness / skin in the game?
- Is there an official Anthropic equivalent?

## Official Anthropic Skills (Pre-Vetted)

Zero vetting burden:
- **PPTX Creator** — PowerPoint generation
- **XLSX Creator** — Excel generation
- **DOCX Creator** — Word generation
- **PDF Creator** — PDF generation

Anthropic-authored, safe for direct use.

## Key Takeaways

- **skills.sh ecosystem: ~788K installs, 1K–4.2K unique skills** (not 91K; Ben AI's figure outdated)
- **36.82% of audited skills had security flaws; 13.4% CRITICAL** per Snyk (Feb 2026)
- **Installing third-party skills grants shell + filesystem + credential access** — vetting essential, not optional
- **Prompt injection is #1 attack vector** (91% of malicious samples); invisibly alters Claude behavior
- **Use Tier 1–4 vetting framework** before install: metadata → code inspection → sandbox → threat model
- **Prefer Anthropic official skills** (PPTX/XLSX/DOCX/PDF) when available; pre-vetted and safe
- **Skill chains compound risk** — insert manual review between chained third-party skills
- **Find Skills (Skill #5) discovers from skills.sh, but you must vet before install**
- **Second-brain context amplifies both power and risk** — auto-pull skills can inadvertently expose sensitive data

## Cross-References

- [[claude-skills/the-eight-meta-skills]] — Ben AI's full 8-skill framework
- [[claude-skills/original-prompt-engineering-best-practices]] — Anthropic canonical techniques
- [[claude-skills/overview]] — Skills architecture & progressive disclosure
- [[harness-engineering/_index]] — Threat modeling for agent systems
- [[ai-operating-system/_index]] — Second-brain OS pattern

## Source

- **skills.sh homepage & leaderboard** — https://skills.sh
- **Snyk security audit: "Toxicskills: Malicious AI Agent Skills"** (Feb 5, 2026) — https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- **Ben AI: "8 Claude Skills I Can't Live Without"** (YouTube bXnRA3pJavE, April 18, 2026) — https://www.youtube.com/watch?v=bXnRA3pJavE
- **Anthropic Agent Skills documentation** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **Vercel skills GitHub** — https://github.com/vercel-labs/skills
- **FireCrawl: "Best Claude Code Skills"** — https://www.firecrawl.dev/blog/best-claude-code-skills
- **AgentSkills.io marketplace overview** — https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026
