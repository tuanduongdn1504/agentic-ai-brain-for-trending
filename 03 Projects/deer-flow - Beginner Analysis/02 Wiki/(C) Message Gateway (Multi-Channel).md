# (C) Message Gateway (Multi-Channel)

> Entity page — Integration concept
> Sources: README multi-channel section + architecture layered
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Message Gateway** = deer-flow's integration layer cho **multi-channel IM platforms**. Users submit tasks từ Telegram, Slack, Feishu, WeChat, WeCom (5 platforms) without opening web UI. Also receive progress updates + results in same channel.

Key concept: **deer-flow anywhere IM app users are.**

## 2. Why it matters / Sao quan trọng

### Web UI limitations

- User must open browser
- Must keep tab open for long tasks (minutes-hours)
- Notifications dependent on browser permissions
- Mobile UX suboptimal

### IM native benefits

- User submits task via Telegram message
- Goes about day
- Gets notification in Telegram when done
- Results delivered in same chat
- Mobile-first

**Philosophy:** Don't force user to come to deer-flow; deer-flow comes to user.

### Target market signal

Multi-channel = **deer-flow targets production deployment** where multiple humans submit tasks, not just solo dev running locally.

## 3. 5 Supported platforms

### Telegram
- **Why:** Global messaging app, developer-friendly bot API
- **Market:** Worldwide, especially strong in developer communities
- **Bot API:** Official, well-documented
- **Free tier:** Yes

### Slack
- **Why:** Business team messaging dominant in Western tech
- **Market:** Enterprise + startup teams
- **Bot API:** Official, rate-limited
- **Free tier:** Limited; paid for serious use

### Feishu (飞书)
- **Why:** ByteDance's own business messaging (ByteDance = deer-flow author)
- **Market:** China enterprise + international ByteDance clients
- **Bot API:** Official
- **Free tier:** Yes for small teams

### WeChat (微信)
- **Why:** China's dominant messaging, billion+ users
- **Market:** China business + personal
- **Bot API:** Limited public; requires WeChat Work typically
- **Free tier:** Yes for personal; enterprise has different rules

### WeCom (企业微信)
- **Why:** WeChat's enterprise version
- **Market:** China corporate
- **Bot API:** Enterprise-focused
- **Free tier:** Per company

### Market coverage

- **Western:** Telegram + Slack cover most audiences
- **China:** Feishu + WeChat + WeCom cover all major Chinese business segments
- **Missing:** Zalo (Vietnam), LINE (Japan/Taiwan), Discord (gaming/dev)

## 4. Gateway architecture

Inferred from layered design:

```
Telegram / Slack / Feishu / WeChat / WeCom
  ↓ (respective bot APIs)
Message Gateway (separate service or part of Gateway API)
  ↓ (internal REST)
LangGraph Server (agent orchestration)
  ↓ (progress callbacks)
Message Gateway
  ↑ (respective bot APIs)
Telegram / Slack / Feishu / WeChat / WeCom
```

### Bidirectional flow
- **Inbound:** User message → parse → task spec → submit
- **Outbound:** Progress updates → format → send to channel
- **Results:** Artifact link or inline content → deliver

### State per user per channel

Gateway tracks:
- User identity across platforms
- Active tasks (don't let user submit 5 parallel tasks by accident)
- Subscription preferences (which updates user wants)
- Language preference (per channel culture)

## 5. Authentication model

### Bot-based
Each platform = deer-flow registers as bot với that platform's API.

### User mapping
Platform user ID → deer-flow user ID mapping. Messages from Telegram user X map to deer-flow user profile.

### Credentials storage
API keys + bot tokens trong `config.yaml` + env vars:
- `TELEGRAM_BOT_TOKEN`
- `SLACK_BOT_TOKEN`
- `FEISHU_APP_ID` + `FEISHU_APP_SECRET`
- etc.

### Security implications
**Channel = attack surface.** 5 platforms = 5× exposure. Mitigation: local-trusted-network deployment (README explicitly recommends this).

## 6. Use case examples

### Use case 1: Researcher mobile
- Researcher on train commute
- Telegram: "Research Q3 competitive landscape, deliver PDF"
- deer-flow takes 30 min, Telegram notifies
- Researcher downloads PDF when arrived at office

### Use case 2: Team Slack workflow
- Team channel has deer-flow bot
- Product manager: "@deer-flow create presentation about user feedback themes"
- deer-flow processes, posts slides link
- Team reviews asynchronously

### Use case 3: Feishu ByteDance internal
- ByteDance employee on Feishu
- Feishu: "Summarize these 10 articles into exec briefing"
- deer-flow on company-internal instance handles
- Briefing arrives in Feishu inbox

### Use case 4: WeChat SME owner
- Small business owner Shanghai
- WeChat: "监控竞品新品发布" (monitor competitor new launches)
- deer-flow periodic research
- WeChat daily summary

## 7. Trade-offs / Limitations

### Strengths
- **User-friendly** — meet users where they are
- **Async-native** — long tasks fit IM async patterns
- **Notification built-in** — IM has notification infrastructure
- **Platform diversity** — global + China coverage

### Weaknesses
- **5-platform maintenance** — each platform's API breaks differently
- **Credentials sprawl** — 5 API keys to secure
- **UX inconsistency** — Slack threads vs Telegram forwards vs WeChat rich text = different UX models
- **No Vietnamese platform** — Zalo missing
- **No Discord** — devs use Discord
- **Attack surface** — 5 bot tokens + 5 inbound vectors

## 8. Comparison to sibling integration approaches

| Sibling | External integration |
|---------|---------------------|
| **ECC (T1)** | Plugin → user interacts via Claude Code only |
| **Superpowers (T1)** | Same |
| **gstack (T1)** | Same |
| **GSD (T1)** | Multi-harness support (integrates WITH other AI agents) |
| **goclaw (T2)** | Platform API for apps to integrate |
| **course (T3)** | N/A (learning resource) |
| **notebooklm-py (T4)** | Bridge to ONE service (NotebookLM) |
| **build-your-own-x (outside)** | N/A |
| **deer-flow (T5)** | **5 IM platforms for user ingress + egress** |

→ **deer-flow's integration = user-facing** (vs notebooklm-py's service-facing bridge).

### Different integration axis
- **notebooklm-py (T4)** = agents invoke external service
- **deer-flow (T5)** = external channels submit to agents
- **goclaw (T2)** = platform serves agents via API

All different integration axes. Not substitutable.

## 9. Comparison to web-UI-only patterns

| Pattern | Reach | Engagement | Complexity |
|---------|-------|------------|------------|
| **Web UI only** | Visitor users | Low | Low |
| **IM bot only** | IM platform users | High | Medium |
| **Web + IM (deer-flow)** | Both | High | High |

deer-flow picked high-complexity high-reach option. Justified for B2B + enterprise deployments.

## 10. Common pitfalls

1. **Credential leak** — bot token in git repo = bot hijacked
2. **Rate limit hits** — sending too many messages = bot banned
3. **Format mismatch** — Slack markdown ≠ Telegram markdown = broken UI
4. **Cross-channel confusion** — user submits in Slack, expects in Telegram = confused
5. **Long artifact handling** — IM message size limits; large artifacts need upload/link
6. **Privacy leak** — sensitive task results in group chat = security incident
7. **Platform API breakage** — Telegram updates API = bot breaks silently

## 11. When NOT to use multi-channel gateway

- **Internal personal use** — web UI enough
- **Audit-critical tasks** — IM easier to lose history; use structured logs
- **Compliance-bound industries** — finance/healthcare may ban IM bots
- **High-security contexts** — each channel adds attack surface
- **Non-technical users** — web UI may be more approachable

## 12. Storm Bear vault relevance

### VN market integration opportunity

deer-flow supports 5 platforms; **Zalo absent.**

**Contribution opportunity:**
- Add Zalo bot integration to deer-flow
- Unlock VN business market (Zalo dominant in VN enterprise messaging)
- Parallel to goclaw's Zalo × integration precedent

### Storm Bear vault access via deer-flow gateway

If Storm Bear vault ever hosted as deer-flow app:
- Scrum team submits via Slack
- Coach reviews in Telegram
- Multi-team managed across channels

**Not current design** but possible future.

### Gateway ≠ vault requirement

Storm Bear vault currently single-user (Cvtot + Claude Code). Doesn't need gateway.

**If vault scales to team** → deer-flow gateway pattern useful reference.

## 13. References / Nguồn

- Source: [[(C) README summary]] (multi-channel headline feature)
- Related entities:
  - [[(C) SuperAgent Harness Architecture]] (gateway = 1 of 5 components)
  - [[(C) Sub-Agent System (Parallel Fan-out)]] (gateway submits to sub-agents)
- Sibling integration comparisons:
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw).md`
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Agent Teams.md`
