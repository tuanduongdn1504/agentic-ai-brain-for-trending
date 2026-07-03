# MVP scoping method — AI-drafted, human-curated

> Ep-3's first hour opens with the series' scope decision: what the e-commerce project MUST contain. The method itself — prompt the AI for an MVP checklist, then audit it — is the teachable artifact.

## Source
- Video #3 osISSsyTJJ8 (livestreamed Mon 2026-06-22, VOD Wed 2026-06-24), ~06:15–23:30 — raw: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`
- Concept originals verified via `wf_f3c7237f-4c4`: MVP coined by Frank Robinson (~2001, SyncDev), popularized by Steve Blank + Eric Ries (*Lean Startup*, 2011)

## The method as demonstrated
1. **Name the concept first** — MVP = "bản demo nhưng cần thể hiện được workflow... những tính năng cốt lõi nhất" (a demo that must show the core workflow / most-essential features).
2. **Prompt the AI in-context** — "tôi coding web thương mại điện tử, MVP là gì?" — deliberately unpolished: "chúng ta nghĩ cái gì trong đầu thì chúng ta gõ vào thôi" (direction over prompt technique).
3. **Audit the AI's checklist on camera** — he catches the missing item live: no user management. *"Nó đang thiếu... trang quản lý user... Nếu mà không có user thì hệ thống này thì làm kiểu gì"* [00:23:02]. Rule stated: *"Bắt buộc... phải đọc và chúng ta đánh giá... không thể copy paste và tôi không phản biện"* [00:15:32].
4. **Paste the curated result into the course doc** — the doc, not the chat, is the scope record.

## The scope that survived
- **Buyer (4 pages):** listing (image/name/price/buy+cart buttons) · product detail · cart · checkout.
- **Admin (3 modules):** users (his addition) · inventory · orders.
- **Deferred, with reasons:** auth ("optional" for MVP!) · online payment → **COD** (cash-on-delivery; ~60–85% of VN e-commerce prefers COD — verified prevalence, rational MVP cut) · reviews · discount codes + campaigns · advanced inventory/search · **deployment** (existing series covers it; costs money).
- **Work order:** user module first ("một cái huyền thoại"), admin before buyer UI (data has to exist), or backend + fake data; easy→hard so later modules can be vibe-code-accelerated once the pattern is set.

## Why (his stated rationale)
- *"Câu chuyện liên quan về tiền... đây chính là cái yếu tố sống còn"* — money is THE survival factor; over-building pre-validation = "vứt tiền qua cửa sổ" (throwing money out the window). Shopee = a version-N product; v1→N iteration; **rebuilding v1 entirely at v2 is normal**.
- Anti-blind-vibe frame: vibe-coding 100K lines you don't understand = technical debt, *"quả bom nổ chậm"* (a time bomb).
- Anti-panic calibration: a real e-commerce platform (Magento, his past job) has hundreds of DB tables (Magento 2.4.3 = 411 verified; his "~200+" recall fits older versions) — but it's organized per-module; learn one module's thinking and transfer it.

## Canonical-definition gap (flagged, not a contradiction)
- The Lean-Startup core — **validated learning** (build-measure-learn against real customers) — is absent from his framing; his MVP is cost-bounded scope control for a *learning* project, which is coherent for the audience but narrower than Ries' definition.

## Key Takeaways
- The transferable unit is the **procedure**: AI drafts the scope checklist → human audits for missing structural items → curated result gets pinned in a document, not a chat.
- The on-camera catch (missing user management) is the pedagogy: AI scope output is a draft to be red-penned, and the red pen requires domain knowledge.
- Deferral list quality > feature list quality: every cut has a stated reason (cost, complexity, existing material) — cf. [[jsm-six-file-context/_index]] Scope-Limits sections.
- COD-first is a *market-informed* simplification, not laziness — defer the payment integration, keep the checkout flow.
- Cross-links: [[beginner-pedagogy-model]] (phases), [[series-project-and-materials]] (the doc as scope record), [[docs-first-ai-second]] (AI as helper frame).
