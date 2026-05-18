# (C) opencode-antigravity-auth — Hướng dẫn cho người mới

> **Bilingual: VN primary, EN technical.** v67 wiki ship — 2026-05-18.
> Subject: [github.com/NoeFabris/opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth) (NPM `opencode-antigravity-auth`).

---

## 1. Nó là gì? / What is it?

**TL;DR (VN):** `opencode-antigravity-auth` là một **plugin xác thực OAuth** cho **Opencode** (một AI coding assistant mã nguồn mở, đối thủ của Claude Code) cho phép bạn truy cập Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3 Pro/Flash và Gemini 3.1 Pro **thông qua tài khoản Google cá nhân** thay vì trả phí trực tiếp cho Anthropic hay Google API. Plugin định tuyến yêu cầu qua **Google Antigravity** — một IDE / cổng API hợp nhất của Google đang ở giai đoạn beta — bằng cách giả lập danh tính của ứng dụng Antigravity Desktop chính thức.

**TL;DR (EN):** OAuth plugin for Opencode that intercepts model requests and routes them through Google's Antigravity Unified Gateway, giving users access to Claude + Gemini models billed against their Google Antigravity quota.

**⚠️ Cảnh báo chính (CRITICAL WARNING):** **Sử dụng plugin này vi phạm Terms of Service của Google.** Một số người dùng đã báo cáo tài khoản Google của họ bị **cấm vĩnh viễn** hoặc bị **shadow-banned** (khóa âm thầm). Đây không phải FUD — README của plugin xác nhận điều này bằng một khối `[!CAUTION]` ngay đầu trang. Đừng dùng tài khoản Google chính của bạn cho client work, file cá nhân quan trọng, hay business email; tạo Google account riêng cho plugin nếu vẫn muốn thử.

---

## 2. Tín hiệu corpus-first / Corpus-first signals

Plugin này có **9 đặc điểm corpus-first** (lần đầu xuất hiện trong vault 67 wiki cumulative):

1. **Tỷ lệ fork/star thấp nhất corpus**: 10,500 stars + 1 fork = **0.0001** (kỷ lục thấp trong toàn bộ 67-wiki corpus; corpus-record trước đó của v65 là 0.178 — cao hơn 1,780 lần). Đây là tín hiệu "drive-by stars" rất rõ — nhiều người star nhưng cực ít người clone/fork để chạy.
2. **Phát hành ToS-violation rõ nhất corpus**: `[!CAUTION]` block mở-mặc-định, danh sách 3 mục acknowledge risk trước khi cài đặt, và Legal footer củng cố. Đây là Pattern #83 Honest-Deficiency-Disclosure ở mức chỉ điểm.
3. **Velocity tác giả solo cao**: 91 releases trong 5 tháng = ~1.75-day cadence — cao nhất corpus cho subject solo-utility.
4. **Anti-detection architecture tích lũy**: header mimicry + timing jitter + fingerprint diversity + per-account fingerprint persistence + platform masquerading (Linux users masquerade as macOS) + soft quota threshold + backend-partition reassignment via fingerprint regeneration = 8+ sub-mechanisms tích hợp trong codebase.
5. **Antigravity là gateway nội-bộ Google được phát hiện-qua-thử-nghiệm**: API path `/v1internal:*`, OAuth scope `cclog` + `experimentsandconfigs` đều là Google-internal. Plugin tồn tại nhờ tính ổn định endpoint không có hợp đồng vendor.
6. **Quota arbitrage**: 1 tài khoản Google = 2 quota pool độc lập (Antigravity + Gemini CLI), nhân đôi effective Gemini quota.
7. **Multi-vendor brokering bởi vendor đóng**: Antigravity host Anthropic Claude + OpenAI GPT-OSS + Google Gemini cùng một gateway — Google đang broker mô hình của competitor inside IDE của mình.
8. **Issue-as-enforcement-signal pipeline**: từng issue (#178, #410, etc.) là tín hiệu cảnh báo về enforcement pattern từ vendor, không phải defect code thông thường. Author respond bằng release tiếp theo trong vòng 1-2 ngày.
9. **Plugin-ordering-as-correctness-concern**: thứ tự plugin trong `opencode.json` ảnh hưởng đến correctness (fetch interception order). Lần đầu corpus quan sát.

---

## 3. Phân loại theo Tier system (corpus taxonomy)

**Tier:** **T4 Bridge** (cầu nối giữa hai vendor / runtime).

| Trục phân loại | Giá trị |
|---------------|---------|
| Archetype | solo-community |
| Quy mô | medium (5-20K stars; hiện 10.5K) |
| Ngôn ngữ chính | TypeScript 97.6% |
| Đóng gói | npm |
| Origin story | individual-author-lineage (NoeFabris solo) |
| Methodology | KHÔNG có — pure utility plugin |
| Governance file count | 4 (README + AGENTS.md + CHANGELOG + LICENSE) — medium |
| i18n | EN-only |
| Influence cited | KHÔNG có methodology lineage |
| Living-Domain-Standards Tracking | KHÔNG |

So sánh với corpus siblings:
- **v62 codex-plugin-cc**: T4 Bridge cùng archetype nhưng do OpenAI corp publish (cross-vendor cooperation)
- **v65 claude-code-system-prompts**: corporate-org reverse-engineering archive (read-only vs. opencode-antigravity-auth's act-upon-API)
- **v66 agentmemory**: T2 Service, solo-author npm plugin nhưng Platform-Primitive Foundation

---

## 4. Cách cài đặt / Installation

**⚠️ Đọc warning ở Section 1 trước khi cài. Tạo Google account riêng nếu vẫn muốn thử.**

### Option A — "Bảo LLM tự cài" (recommended by author)

Paste vào bất kỳ AI coding agent nào (Claude Code, OpenCode, Cursor, etc.):

```
Install the opencode-antigravity-auth plugin and add the Antigravity model definitions to ~/.config/opencode/opencode.json by following: https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md
```

LLM agent sẽ đọc README + edit `opencode.json` + run `opencode auth login` thay bạn.

### Option B — Manual setup (4 bước)

1. **Thêm plugin** vào `~/.config/opencode/opencode.json`:
   ```json
   {
     "plugin": ["opencode-antigravity-auth@latest"]
   }
   ```
   (Hoặc `@beta` cho bleeding-edge.)

2. **Login** với Google account:
   ```bash
   opencode auth login
   ```
   OAuth flow sẽ mở browser, callback về `localhost:51121`.

3. **Add models** — chọn 1 trong 2:
   - Trong `opencode auth login` menu → "Configure models in opencode.json" (tự động ghi config)
   - Hoặc paste config từ README's `<details>` block "Full models configuration"

4. **Sử dụng:**
   ```bash
   opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
   ```

### Lỗi thường gặp khi cài đặt (most common pitfalls)

| Triệu chứng | Nguyên nhân | Fix |
|------------|-------------|-----|
| Safari "fail to authorize" sau khi login | Safari HTTPS-Only Mode block `http://localhost` callback | Dùng Chrome/Firefox, hoặc tắt HTTPS-Only Mode tạm thời |
| `403 rising-fact-p41fc` cho Gemini CLI models | Default project ID fall-back; works for Antigravity not Gemini CLI | Tạo GCP project, enable `cloudaicompanion.googleapis.com`, add `projectId` to accounts.json |
| `Unrecognized key "plugins"` | Sai tên key | Phải là `"plugin"` (số ít), không phải `"plugins"` (số nhiều) |
| Port `51121` đã in use | Process cũ chưa cleanup | `lsof -i :51121` → `kill -9 <PID>` |
| Docker/WSL2/SSH OAuth fail | Browser không reach localhost trên machine chạy Opencode | `ssh -L 51121:localhost:51121 user@remote` |

---

## 5. Cách sử dụng cơ bản / Core usage pattern

### 5.1 Single-account invoke

```bash
# Claude với thinking max budget
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max

# Gemini 3 Pro với high thinking
opencode run "Hello" --model=google/antigravity-gemini-3-pro --variant=high

# Gemini 3 Flash với minimal thinking (fastest)
opencode run "Hello" --model=google/antigravity-gemini-3-flash --variant=minimal
```

### 5.2 Multi-account (recommended — nhân đôi quota)

```bash
# Add account thứ 2:
opencode auth login
# Menu sẽ prompt: "(a)dd new account(s) or (f)resh start?" — chọn `a`

# Check quotas:
opencode auth login → Menu "Check quotas"

# Disable account (nếu cần "cool down" 1 account):
opencode auth login → Menu "Manage accounts" → select account → "Disable"
```

### 5.3 Variant invocation patterns

**Claude models (TOKEN-based thinking budget):**

```json
"variants": {
  "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
  "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
}
```

**Gemini 3 models (STRING-based thinking level):**

```json
"variants": {
  "minimal": { "thinkingLevel": "minimal" },  // Flash only
  "low":     { "thinkingLevel": "low" },       // Flash + Pro
  "medium":  { "thinkingLevel": "medium" },    // Flash only
  "high":    { "thinkingLevel": "high" }       // Flash + Pro
}
```

⚠️ Gemini 3 Pro chỉ chấp nhận `low` và `high`. Nếu gọi `minimal` hoặc `medium` trên Pro sẽ trả về 400.

---

## 6. Concept mới + Kiến trúc / Novel concepts + Architectural choices

### 6.1 Dual quota pool (key architectural insight)

1 Google account → 2 API quota độc lập:
- **Antigravity quota** — qua `cloudcode-pa.googleapis.com` `/v1internal:*` (default)
- **Gemini CLI quota** — qua `generativelanguage.googleapis.com` (fallback hoặc primary với `cli_first: true`)

Khi Antigravity quota cạn → plugin tự động fall back sang Gemini CLI pool trên cùng account. → **Hiệu quả nhân đôi Gemini quota.**

Claude và image models luôn dùng Antigravity (không có Gemini CLI fallback cho Claude).

### 6.2 Multi-account rotation (3 strategies)

| Strategy | Khi nào dùng |
|----------|-------------|
| `sticky` (default cho 1 account) | Long conversations → preserve Anthropic prompt cache |
| `round-robin` (5+ accounts) | Maximum throughput |
| `hybrid` (default cho 2-5 accounts) | Best overall — health score + token bucket + LRU |

### 6.3 Rate-limit scheduling (3 modes)

| Mode | Behavior |
|------|----------|
| `cache_first` (default) | Wait same account → preserve prompt cache |
| `balance` | Switch immediately on rate-limit |
| `performance_first` | Round-robin distribution |

### 6.4 Soft quota threshold (default 90%)

`soft_quota_threshold_percent: 90` → skip account when usage exceeds 90%. **Lý do**: tránh Google penalize account fully-exhausted-quota.

### 6.5 Claude thinking blocks: stripped ALL

Plugin **strip toàn bộ thinking blocks** từ outgoing Claude requests. Tradeoff:
- ✅ Zero signature errors (không thể có invalid signatures vì không gửi any)
- ✅ Same quality (Claude re-thinks fresh mỗi turn — full conversation context vẫn được nhìn thấy)
- ✅ Simpler code (no validation/restoration logic)
- ❌ Compute cost: Claude tốn thêm tokens cho thinking re-generation
- ❌ Latency: thinking re-generation thêm response time

### 6.6 Session recovery: synthetic message injection

Khi tool execution bị interrupted (ESC, timeout, crash) → API trả `tool_use ids were found without tool_result blocks`. Plugin response:
1. Detect via `session.error` event
2. Inject synthetic `tool_result` blocks với content "Operation cancelled"
3. Send via `client.session.prompt()`
4. Auto-resume với `"continue"`

Người dùng nhìn thấy như chưa từng có error.

---

## 7. So với corpus frameworks khác / vs other corpus frameworks

| Subject | Vendor relationship | Multi-account architecture | TOS framing |
|---------|--------------------|-----------------------------|-------------|
| **opencode-antigravity-auth** (v67) | **Adversarial** — vendor enforces against unauthorized use; plugin engineers anti-detection | YES — 3 strategies + 3 scheduling modes | **Explicit TOS-violation upfront** |
| **codex-plugin-cc** (v62) | Cooperative — OpenAI published the plugin themselves | NO — single ChatGPT subscription assumption | Commercial-vendor relationship; no TOS conflict |
| **claude-code-system-prompts** (v65) | Tolerant — Anthropic does not DMCA the reverse-engineering archive | NO — read-only archive | Disclosure: "Maintained by Piebald AI, not Anthropic" |
| **agentmemory** (v66) | Cooperative — uses iii-engine SDK as host platform | NO — single host platform | No TOS conflict |

**Diagnostic question vault operator should ask:** *"Does this tool require evading vendor visibility to operate?"* If YES → adversarial-tolerance-architecture; not safe for client work. If NO → vendor-cooperative architecture; safer to evaluate for deployment.

opencode-antigravity-auth is YES on the diagnostic. The other 3 corpus subjects above are NO. This is structural information, not value judgment.

---

## 8. Ethical framing / Khung đạo đức

⚠️ **Section này QUAN TRỌNG đối với plugin này vì nó là TOS-violation tool.**

### 8.1 Plugin author's stated framing (verbatim từ README)

**Intended Use:**
- Personal / internal development only
- Respect internal quotas and data handling policies
- Not for production services or bypassing intended limits

**Warning (full assumption of risk):**
- Terms of Service risk — may violate ToS of AI model providers
- Account risk — Providers may suspend or ban accounts
- No guarantees — APIs may change without notice
- Assumption of risk — You assume all legal, financial, and technical risks

**Disclaimer:**
- Not affiliated with Google. Independent open-source project.
- "Antigravity", "Gemini", "Google Cloud", and "Google" are trademarks of Google LLC.

### 8.2 Vault operator's perspective

Plugin này là sản phẩm legally-gray-utility. Author NoeFabris đã:
- ✅ Disclose risk rõ ràng và explicit (Pattern #83 honest-deficiency-disclosure)
- ✅ Document intended-use boundary ("personal / internal development only")
- ✅ Provide multi-account-rotation as defensive architecture
- ✅ Track issue reports (#178, #410, etc.) như enforcement-signal pipeline

Nhưng đối với Storm Bear / vault operator context (Scrum coach, client work):
- ❌ TOS-violation risk không acceptable cho production client engagement
- ❌ Account-ban catastrophic loss > savings on API spend
- ❌ "Personal / internal development only" disclaimer = incompatible với paid Scrum-coaching delivery

→ Plugin có thể dùng cho **personal experimentation / learning** (đặc biệt với throw-away Google account) nhưng **KHÔNG dùng cho client work**.

### 8.3 Đối với người mới (general guidance)

- Tạo Google account riêng cho plugin — **không dùng main account**
- Đừng test trong giờ làm việc — nếu bị ban account, work-related Google services có thể bị ảnh hưởng (Drive, Workspace, etc.)
- Đọc CHANGELOG để xem patterns bị enforce gần đây — tránh repeat behavior
- Plugin compatible với **rate-limited usage**, không phải production AI service

---

## 9. Liên quan tới Storm Bear / Storm Bear relevance (VN operator + Scrum coach fit)

**Phase 0.9 STRICT verdict:** **MODERATE INCLUDE** — 2/4 PASS:
- (a) PASS — NoeFabris solo independent engineer structural peer to Storm Bear (solo-engineer + Scrum coach)
- (b) **FAIL** — Storm Bear không deploy plugin này (vault uses Claude Code; TOS risk; intended-use mismatch)
- (c) FAIL — no methodology lineage cited
- (d) PASS — Opencode is sibling-product to Claude Code (v65 corpus subject); v62 codex-plugin-cc bridges Codex → Claude Code in same T4 archetype

**What Storm Bear can learn (despite NOT deploying):**

1. **Pattern #83 honest-deficiency-disclosure as branding asset** — 10.5K stars WITH `[!CAUTION]` warning. Honest disclosure không suppress adoption; nó strengthens credibility.
2. **CHANGELOG as evolution-evidence** — mỗi Fixed-#N entry là evidence về evolution under adversarial pressure. Vault iteration logs nên explicit name pressure-source, không chỉ describe refinement.
3. **Solo-velocity at 1.75-day cadence** — operationally viable nếu mỗi release scope hẹp + author-written CHANGELOG + no external coordination overhead. Vault weekly cadence comparison.
4. **Adversarial-Detection-Tolerant Architecture = inverse posture** — vault uses vendor-cooperative posture; recognizing adversarial-tolerance debt in candidate tools is operationally valuable diagnostic.

**Pilot ranking:** **NOT a pilot candidate** — TOS violation + alternative-runtime requirement + no deployment-context fit. Useful as comparative reference khi pilot khác T4 Bridge subjects.

---

## 10. Lộ trình học tập 4 tuần / 4-week learning roadmap (nếu vẫn muốn explore — for experimentation only)

### Tuần 1 — Hiểu architecture

- Đọc full README (24 KB) — paying attention to TOS warning + Models table + Configuration sections
- Đọc `docs/ARCHITECTURE.md` (302 lines) — hiểu fetch interception flow + Claude thinking strategy
- Đọc `docs/MULTI-ACCOUNT.md` (199 lines) — hiểu dual quota pool architecture
- KHÔNG cài plugin chưa — chỉ đọc

### Tuần 2 — Sandbox setup

- Tạo Google account riêng (throw-away, không link với main identity)
- Setup Opencode trên dev machine (không phải production work machine)
- Cài plugin theo Option B manual setup
- Test với 1 simple model (Gemini 3 Flash với minimal thinking — lowest-cost variant)
- Observe behavior 1-2 ngày

### Tuần 3 — Multi-account experimentation

- Tạo Google account thứ 2 (different identity / throw-away)
- Test multi-account rotation
- Test `opencode auth login` quota check menu
- Quan sát `~/.config/opencode/antigravity-accounts.json` structure
- Đọc `docs/ANTIGRAVITY_API_SPEC.md` (634 lines) — hiểu wire format requirements

### Tuần 4 — Enforcement-pattern observation

- Đọc CHANGELOG entries (v1.0.0 → v1.6.0, 91 releases)
- Identify từng "Fixed #N" entry và detection-pattern nó address
- Map từng pattern → defensive engineering response trong code
- Decision: tiếp tục dùng (cho personal exploration), uninstall (TOS risk too high), or migrate (chuyển sang vendor-cooperative alternative)

---

## 11. Tradeoffs + limitations

**Pros:**
- ✅ Access Claude 4.6 + Gemini 3 + GPT-OSS via single OAuth
- ✅ Multi-account quota multiplexing (1 account → 2× Gemini quota effective)
- ✅ Sophisticated session-recovery + thinking-block-handling
- ✅ Explicit TOS disclosure (no surprise enforcement)
- ✅ Active maintenance (91 releases / 5 months / ~1.75-day cadence)

**Cons:**
- ❌ **Violates Google Terms of Service** — account ban / shadow-ban risk
- ❌ Requires Opencode (not compatible với Claude Code, Cursor, Windsurf, etc.)
- ❌ Linux users masquerade as macOS — explicit platform misrepresentation
- ❌ Endpoint stability depends on Google's continued tolerance — no contract
- ❌ Per-account fingerprint storage = sensitive file (OAuth refresh tokens — mode 0600 enforced)
- ❌ "Personal / internal development only" disclaimer = not for paid client work
- ❌ Hidden cognitive cost: must understand vendor-enforcement patterns to avoid them

**Decision matrix:**

| Use case | Recommended? |
|----------|--------------|
| Production client work (Scrum coaching, paid engagement) | ❌ NO |
| Personal AI coding experimentation with throw-away account | ⚠️ Maybe (with caveats) |
| Learning the multi-account architecture without deploying | ✅ YES (read-only study) |
| Bridging Opencode to Antigravity quota for hobby projects | ⚠️ Maybe (after Tuần 4 evaluation) |
| Production team adoption | ❌ NO (TOS-incompatible with business operation) |

---

## 12. Caveats + safety notes / Ghi chú an toàn

**Supply-chain awareness:**

- Plugin tải về từ npm registry — kiểm tra package integrity trước khi cài (`npm install opencode-antigravity-auth` không có postinstall script visible nhưng best to verify)
- `~/.config/opencode/antigravity-accounts.json` chứa OAuth refresh tokens — **đối xử như password file** (mode 0600 enforced by plugin from v1.5.0)
- Plugin v1.6.0 strips outgoing telemetry headers (`X-Opencode-Tools-Debug` removed) — earlier versions had this; check upgrade path
- Plugin reads Antigravity's version-check endpoint at startup — your IP gets logged by Google as Antigravity Manager client

**Account safety:**

- Đừng share `antigravity-accounts.json` qua git, public storage, hay cloud sync
- Refresh tokens không expire automatically nhưng có thể bị Google revoke (e.g., on password change → triggers `invalid_grant` errors)
- Token revocation by Google = plugin automatically removes invalid account → user state machine handles
- Migrate accounts between machines: copy `antigravity-accounts.json` + ensure plugin installed on target

**Enforcement monitoring:**

- Watch CHANGELOG for new "Fixed #N" entries — they signal new enforcement patterns
- Watch GitHub Issues for community-reported account bans
- If your account gets 403 `validation_required` → plugin auto-disables it; verify via `opencode auth login` menu
- Soft quota threshold (90%) defaults are conservative; don't lower below 85% without operational reason

**Operational hygiene:**

- Quiet mode (`quiet_mode: true`) suppresses toast notifications — useful for batch / CI invocations
- Debug logging (`OPENCODE_ANTIGRAVITY_DEBUG=2`) writes to `~/.config/opencode/antigravity-logs/` — contains request bodies (sensitive)
- E2E test scripts (`test:e2e:models`, `test:e2e:regression`) hit live endpoints — don't run in CI without careful account isolation

---

## 13. References + next action

**Primary sources:**
- [README.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/README.md) (718 lines)
- [docs/ARCHITECTURE.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/ARCHITECTURE.md) (302 lines)
- [docs/MULTI-ACCOUNT.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/MULTI-ACCOUNT.md) (199 lines)
- [docs/ANTIGRAVITY_API_SPEC.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/ANTIGRAVITY_API_SPEC.md) (634 lines)
- [CHANGELOG.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/CHANGELOG.md) (267 lines)

**Corpus cross-references:**
- [v62 codex-plugin-cc — STRONG sibling](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md) — T4 Bridge corporate-published; inverse direction
- [v65 claude-code-system-prompts — closed-vendor-product-surface engagement axis](../../claude-code-system-prompts - Beginner Analysis/CLAUDE.md)
- [v66 agentmemory — recent solo-author plugin sibling](../../agentmemory - Beginner Analysis/CLAUDE.md)

**Wiki cross-references:**
- [Entity 1: OAuth bridge core](../02 Wiki/entity-1-oauth-bridge-core.md)
- [Entity 2: Multi-account quota-multiplexing](../02 Wiki/entity-2-multi-account-quota-multiplexing.md)
- [Entity 3: Antigravity Unified Gateway](../02 Wiki/entity-3-antigravity-unified-gateway.md) — Phase 4b PRIMARY
- [Entity 4: Storm Bear meta](../02 Wiki/entity-4-storm-bear-meta.md)
- [Pattern-83 promotion proposal](../01 Analysis/(C) Pattern-83 Honest-Deficiency-Disclosure N=3 promotion proposal.md)

**Next action (suggested):**

🎯 **Đối với Storm Bear / vault operator:** Không deploy plugin. Đọc CLAUDE.md v67 entry để hiểu Pattern #83 N=3 evidence + diagnostic question "tool requires evading vendor visibility?" — đây là vault-actionable lesson.

🎯 **Đối với người mới muốn learn:** Bắt đầu từ Tuần 1 (read-only study) trong roadmap section 10. Không cài plugin cho đến khi đã đọc full README + ARCHITECTURE + MULTI-ACCOUNT. Tạo throw-away Google account trước khi test.

🎯 **Đối với Opencode user đã có Opencode setup:** Đọc CHANGELOG carefully để hiểu enforcement patterns đã observed; decide based on personal risk tolerance + use-case alignment.
