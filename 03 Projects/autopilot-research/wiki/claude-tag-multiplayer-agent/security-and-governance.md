# Security & Governance

## What Anthropic built (first-party, strong)

- **Agent Proxy:** credentials stored outside the sandbox, never in model context, injected at request time; **default-deny egress** to non-allowlisted hosts ([docs security-and-data](https://claude.com/docs/claude-tag/concepts/security-and-data)).
- **Agent-centric identity:** Tag acts through **workspace-managed service accounts** ("its own account in each system it touches"), not user impersonation ([agent-identity blog](https://claude.com/blog/agent-identity-access-model)).
- **Channel-scoped isolation:** per-channel identities, memory and tool grants; private-channel memory never surfaces elsewhere; engineering/HR/legal Claudes architecturally separated.
- **Ephemeral sandboxes** per thread, discarded on idle.
- **Audit:** every Tag action logged with the requesting user (Anthropic side).
- **Compliance posture:** SOC 2 Type I/II, ISO 27001:2022, ISO/IEC 42001:2023, BAA for HIPAA, DPA for GDPR ([trust.anthropic.com](https://trust.anthropic.com)); Slack data **not used for training by default** (Marketplace listing); commercial terms govern Team/Enterprise data.

## The four structural gaps (independent analysis, mostly Zenity)

1. **Ambient mode = standing injection surface.** Tag continuously reads *all* channel content — pasted emails, forwarded docs, bot messages — as model input. **No Tag-specific prompt-injection mitigation is documented** in the docs read at ingest (in contrast to Claude Code's injection docs). [Zenity](https://zenity.io/blog/security/claude-tag-control-risk): every step toward autonomy is an opportunity for malicious instructions to hijack downstream tool execution. Compounded by the memory write-path: an injected "instruction" can persist as channel memory ([[memory-model]]).
2. **Membership-as-ACL / permission elevation.** Anyone in a channel where Tag holds GitHub/Jira/Drive credentials can have Tag act with them — channel invite lists silently become permission grants for tool actions users don't individually hold.
3. **Audit fragmentation at the boundary.** Downstream systems log the **service account**, not the requesting human; intent reconstruction requires manually joining Anthropic logs with GitHub/Jira logs. (The flip side of the — correct — decision not to impersonate users.)
4. **The DM seam.** DM interactions run on the sender's **personal** claude.ai account: personal-tier privacy policy, personal billing, outside org DLP/audit view. An org rolling out Tag gets a parallel ungoverned channel by default.

## Inherited-trust context

- claude.ai platform history: Oasis Security's "Claudy Day" set (invisible prompt injection via URL — patched; Files-API exfiltration + open redirect "being addressed") — platform-level, not Tag-specific, but the relevant prior for buyers.
- Sister-product gap: [TrueFoundry](https://www.truefoundry.com/blog/claude-cowork-security-risks) reports Cowork activity excluded from DLP alerts and compliance reporting — buyers extrapolate platform-family gaps to Tag until proven otherwise.
- No Tag-specific incidents on status.claude.com in the first two weeks.

## Governance checklist (condensed from BERI IT-guide + docs + Zenity)

- [ ] Ambient OFF by default; enable per-channel by explicit owner request
- [ ] Service accounts per connector with **least scopes**; no org-wide GitHub write if channel-scoped repos suffice
- [ ] Channel-membership review for every channel holding write-capable credentials (membership = ACL now)
- [ ] Log-correlation plan: map Tag service-account IDs → Anthropic audit stream before granting write tools
- [ ] Memory review cadence: admin reads channel memory weekly during pilot; delete-on-sight for anything resembling injected instructions
- [ ] DM policy: decide whether employees may use Tag DMs for work content at all (it's outside your controls)
- [ ] Spend caps + 75%/95% alerts before ambient goes on anywhere

## Key Takeaways

- Anthropic shipped an unusually explicit **credential/identity architecture** for a beta — the unsolved parts are the *seams*: ambient input, membership-as-ACL, split audit trails, personal-account DMs.
- The write-path (what becomes a standing instruction) is the highest-value red-team target; the read-path is comparatively well-defended.
- For this vault's pilots: same lesson as [[external|Storm Bear: elicit-verifiable-agent-dsl]] gateway isolation — *keep credentials out of model context* is now a 2-vendor convergent pattern; the operator's Telegram stack should mirror the ambient-off-by-default discipline.

Cross-links: [[architecture-and-execution-model]] · [[memory-model]] · [[admin-rollout-and-migration]] · [[reception-and-risks]]
