---
source: yt-pipeline (single-video manual ingest)
topic: omnilogin-ai-coding
generated: 2026-06-20
video_id: ySEOr1q-Ve4
video_url: https://www.youtube.com/watch?v=ySEOr1q-Ve4
title: "Omnilogin AI Coding: Mô Tả Bằng Tiếng Việt, AI Tự Viết Kịch Bản Auto Login Gmail | Không Cần Code"
channel: Omnilogin
upload_date: 2026-04-23
duration_sec: 626
views_at_ingest: 1349
language: Vietnamese (auto-captions)
fetch_method: yt-dlp --write-auto-subs vi + vtt-to-md.py
---

# Omnilogin AI Coding — raw transcript + notes

> Single-video ingest (not a NotebookLM bundle). Verbatim Vietnamese auto-captions converted via `bin/vtt-to-md.py`, plus an English gloss of each step and the referenced "original resources" for deep-dive.

## What the video is

A vendor tutorial from the **Omnilogin** channel demonstrating Omnilogin's **new "AI Coding" feature**: the user describes an automation task in natural Vietnamese, and an LLM writes the **complete automation script + a configuration UI** for it. Demo task = auto-login Gmail across multiple antidetect-browser profiles. "No code, no drag-and-drop, no hiring a freelancer."

**Omnilogin** = an **antidetect browser** (multi-profile browser for managing many isolated browser identities — popular with MMO / multi-account e-commerce sellers). The AI Coding feature is a vertical "describe → generated browser-automation script" agent embedded inside that product, with a **bring-your-own-model (BYO-model)** API config. The demo uses **Kimi** (Moonshot AI) as the model.

## Original resources referenced (deep-dive targets)

1. **Omnilogin** — product + official docs: https://docs.omnilogin.net ; download: https://www.omnilogin.net/download/
2. **Kimi / Moonshot AI** — the LLM used via API: kimi.com (subscription + console for API key). Video states you must buy a plan (4 plans shown; presenter uses the **$39** plan), then create an API key in the Console.
3. Community: Telegram chat room (https://t.me/+m12r4ljlUUZhNDNl)

## Key mechanics shown

- **Where:** Omnilogin app → "Quy trình" (Workflows/Processes) → **AI Coding** → create new process.
- **Interface layout:**
  - Left: chat box to talk to the AI
  - Bottom: prompt input box
  - Right pane, 3 tabs:
    - **Script** — the generated automation code
    - **UI code** — the generated configuration UI (e.g., input fields for the account list) so a non-coder can run the script with their own data
    - **Output** — run results
- **Add an AI model** (Settings → Model). Fields:
  - `provider type` (pick the provider)
  - `provider name` (any nickname)
  - `Base URL` (endpoint to call the model)
  - `API key`
  - `model` (exact model name string)
  - For Kimi there is also a **`disable thinking`** toggle: turning it ON speeds up processing and **reduces cost**, but **accuracy may drop**.
- **Get the Kimi API key:** go to kimi.com → must buy a plan (4 plans; presenter uses $39) → Console → create new API key (named "Omi Login AI") → copy → paste into Omnilogin → name it "Kimi" → save.
- **Run config:** before running, attach a **profile** for the AI to use (e.g., profile 183) → Enter → AI plans + generates.

## Prompt-writing discipline taught (the transferable nugget)

The presenter explicitly breaks down "what a good prompt should contain":
1. **State what you HAVE** — e.g., "I have several Gmail accounts in this format, one account per line."
2. **State what you NEED** — e.g., "create an auto-login Gmail process with the following steps."
3. **Describe each step** — give the step-by-step procedure explicitly.
4. **Specify UI requirements** — e.g., "include a UI to paste the account list, with sample data."
5. **Provide sample data** — give a concrete example of the input data shape.

## Verify / iterate loop shown

- After AI finishes: **Accept** the Script tab, **Accept** the UI code tab to save.
- **Test:** clear the profile's data and run again to confirm the process is correct and error-free; if errors remain, ask the AI to fix (chat loop).
- Re-enter sample data → run → confirms success, no errors.

## Scale-out shown (multi-profile)

- Group management → create a new group "Gmail" → quick-create 2 new profiles in it.
- Select all → bulk utility → copy profile IDs → paste the 2 profile IDs into the generated input UI.
- Paste the Gmail accounts → save.
- Concurrency: set "profiles to run concurrently" = 2, select profiles by group (Gmail) → **Run** → both profiles complete successfully.

## ⚠️ Use-context flag (recorded honestly, per librarian rules)

The demo's headline use case (mass automated Gmail login across many antidetect profiles) sits in the multi-account / "MMO" space, which commonly conflicts with platform Terms of Service (Google prohibits automated/bulk account access). The **transferable, legitimate knowledge** here is the *technology pattern* — natural-language → generated automation script + self-generated config UI, BYO-model API config, and the prompt-structure discipline — not the specific Gmail-bulk-login use case. The wiki + pilot methods focus on the transferable techniques.

---

## Verbatim transcript (Vietnamese auto-captions, deduplicated)

**[00:04]** Chào các bạn. Như các bạn đang thấy trên màn hình cho chạy một kịch bản Auto login Gmail trên Omilogin. Và điều đặc biệt là kịch bản này được tạo ra hoàn toàn bởi AI. Hôm nay mình sẽ giới thiệu tới các bạn một tính năng hoàn toàn mới trong login. Bạn chỉ cần mô tả nhu cầu bằng ngôn ngữ tự nhiên, AI sẽ tự viết toàn bộ kịch bản cho bạn. Chắc hẳn thì nhiều người dùng Omilogin đều từng gặp phải một vấn đề quen thuộc, muốn xây dựng một kịch bản riêng cho công việc của mình nhưng lại chưa biết cách viết hoặc viết thì lại chưa thật sự hoàn

**[00:31]** chỉnh. Còn nếu đi thuê người viết thì vừa mất thời gian vừa tốn chi phí mà chưa chắc là đúng ý. Thì tính năng mới này sinh ra để giải quyết đúng bài toán đó. Bạn không cần viết code, không cần kéo thả, chỉ cần nói ra điều mình muốn và AI sẽ lo phần còn lại. Thì bây giờ mình sẽ cùng hướng dẫn các bạn từ cấu hình đến viết một kịch bản như mình. Trước tiên các bạn sẽ mở app Om login lên như mình hiện tại. Sau đó các bạn sẽ vào phần quy trình chọn AI Coding. Ở đây mình sẽ tạo một quy trình mới.

**[00:59]** Thì khi vào bên trong thì giao diện sẽ được chia thành các phần. Thì bên trái là khung chat để tương tác với AI. Bên dưới là ô nhập nội dung tức là ô các bạn nhập prom ấy. Bên phải gồm ba phần. Phần script là phần chứa code được tạo. Phần UI code là phần chứa giao diện để cấu hình cho script có thể chạy. Và phần output là phần hiển thị kết quả chạy. Bây giờ trước khi sử dụng thì các bạn cần thêm model AI. Ở đây mình sẽ nhấn vào biểu tượng setting. Nhấn vào phần model. Ở đây mình đã có

**[01:27]** sẵn một model. Mình sẽ xóa model này đi. Sau đó mình sẽ thêm một model mới. Thì các trường cần nhật bao gồm provider type. Ở đây là các bạn có thể chọn lại model để các bạn sử dụng. Provider name. Ở đây các bạn có thể đặt tên tùy ý sao cho dễ nhớ là được. Burl địa chỉ để gọi đến model này. Còn API key chính là khóa truy cập. Cuối cùng là model. Ở đây các bạn cần nhập tên chính xác của model. Kimi thì còn có thêm một option nữa đó

**[01:57]** là disable thinking. Thì khi bật tính năng này lên thì sẽ làm tăng tốc AI xử lý và giảm chi phí đi. Như nhân đổi lại thì độ chính xác lại có thể giả đi. Bây giờ mình sẽ đi lấy API key cho Kimi này. Mình sẽ thêm các bạn sẽ vào trang kimi.com Các bạn bắt buộc phải mua gói dưới đây để có thể sử dụng nhá. Ở đây đang có bốn

**[02:25]** gói thì mình đang sử dụng gói 39 đô đây. Sau đó mình sẽ vào phần console. Ở đây mình sẽ tạo một apy mới. Ở đây mình sẽ đặt tên là Omi Login AI đi. Sau đấy mình tạo sau đấy mình copy apy này. Mình dán vào đây. Tên ở đây thì mình sẽ đặt là Kimi. Sau đấy mình sẽ nhấn lưu. Bây giờ mình sẽ nhập prom. Mình đã có Sau đấy trước khi chơi chạy thì các bạn

**[03:01]** phải cấu hình profile để cho AI sử dụng. Ở đây mình sẽ chọn một profile 183 này đi. Bây giờ mình sẽ nhấn enter. Như vậy là AI đã bắt đầu xử lý để lên kế hoạch để tạo quy trình cho các bạn. Thì ở đây mình sẽ phân tích thêm là một prom nên có gì. Thì hiện tại các bạn phải mô tả là các bạn đã có gì. Ở đây mình đang nói sẵn là mình có một số tài khoản Gmail theo định dạng thì mỗi tài khoản nằm trên một dòng. Tiếp theo mình sẽ mô tả là mình cần gì thì mình nói là tạo cho tôi một quy trình auto login Gmail theo

**[03:29]** từng bước như thế này. Tiếp theo mình sẽ mô tả từng bước. Ở đây đang có từng bước có sẵn rồi. Tiếp theo đó mình sẽ nói đến yêu cầu về giao diện. Giao diện ở đây là giao diện để các bạn nhập danh sách tài khoản vào. Thì ở đây mình sẽ yêu cầu về giao diện là có sẵn cả giao diện để nhập danh sách tài khoản cho tôi với dữ liệu mẫu. Sau đấy mình sẽ đưa dữ liệu mẫu cho nó. Bây giờ AI đang bắt đầu xử lý. Thì phần này cũng khá là lâu và để tránh làm mất thời gian cho mọi người thì phần này mình sẽ tua nhanh đi.

**[06:01]** thì mình sẽ lưu quy trình này lại. Ở đây mình sẽ nhấn accept. Sau đó sang tab UI code thì mình cũng sẽ nhấn accept. Bây giờ mình sẽ xóa dữ liệu của profile này và chạy lại một lần nữa trong đây xem quy trình đã đúng ý mình chưa, có lỗi gì không. Nếu còn thì mình sẽ bỏ AI sửa tiếp. Mình sẽ xóa hết dữ liệu đi rồi sau đấy tắt đi. Sau đấy mình sẽ nhấn Trước tiên mình cần nhập lại dữ liệu mẫu

**[07:48]** Vậy là quy trình đã chạy xong, tức là quy trình này đã thành công, không có lỗi gì. Giờ mình sẽ hướng dẫn các bạn chạy quy trình này một cách hoàn chỉnh. Ở đây mình sẽ ví dụ với hai profile. Đầu tiên mình sẽ chọn quản lý nhóm. Ở đây mình sẽ tạo một nhóm mới. Mình sẽ đặt tên cho nhóm là Gmail đi. Sau đấy mình sẽ tạo sau đấy mình sẽ nhấn luôn vào nhóm này. Mình sẽ tạo hai profile mới. Ở đây mình sẽ nhấn luôn tạo nhanh hai profile.

**[08:15]** chọn nhóm các bạn thích nhá. Nhưng mà ở đây mình đang trong nhóm Gmail thì mình sẽ chọn nhóm Gmail. Sau đấy mình nhấn OK. Ở đây mình sẽ chọn tất cả. Sau đấy mình nhấn vào tiện ích hàng loạt này. Mình sao chép profile ID. Sau đấy mình quay lại phần AI coding mình ra back ra ngoài. Ở đây là giao diện để các bạn nhập Gmail để đăng nhập nhá. Ở đây mình sẽ paste hai cái profile ID này vào. Bây giờ mình sẽ dán các tài Sau đấy mình nhấn lưu. Như vậy phần

**[08:54]** input này mình đã cấu hình được danh sách tài khoản để đăng nhập rồi. Ở đây thì mình sẽ set up cho bạn cách chạy những profile nào và chạy như thế nào. Ở đây mình sẽ chọn số profile chạy đồng thời. Mình đã có hai profile, mình sẽ chọn số profile chạy đồng thời là 2. Ở phần chọn profile thì mình sẽ chọn theo nhóm đi. Mình sẽ chọn theo nhóm Gmail. Sau đấy mình sẽ nhấn run.

**[10:08]** Rồi như vậy cả hai profile đều đã chạy thành công. Thì như vậy là mình đã hướng dẫn xong cho các bạn cách sử dụng tính năng AI để tạo kịch bản trong Omi Login. Thì hy vọng với tính năng này thì sẽ giúp các bạn tiết kiệm thời gian hơn và dễ dàng hơn trong việc xây dựng các quy trình cho riêng mình. Cảm ơn các bạn đã theo dõi và hẹn gặp lại các bạn trong video tiếp theo.
