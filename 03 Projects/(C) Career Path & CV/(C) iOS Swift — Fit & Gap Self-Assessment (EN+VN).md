# iOS Developer Job Fit & Gap Self-Assessment

Use this rubric to score yourself honestly against the role's requirements. Fill in your self-rating (1–5) and evidence for each row. The "Close the gap" column gives you a concrete quick win if you're weak. After you score, follow the apply-readiness gate at the bottom.

---

## Fit & Gap Rubric

| Requirement | Type | Rating (1–5) | Your Evidence [FILL] | If weak (≤2): fastest way to close the gap |
|---|---|---|---|---|
| **Swift proficiency**: can read/write Swift code correctly; understand optionals, closures, protocols, error handling | Must | | [FILL: link to GitHub repo / Codewars profile / describe your biggest Swift problem solved] | Ship a small Swift CLI tool or algorithm solution (2–3 hours on LeetCode/HackerRank); pair it with a 2-min Loom walking through the code |
| **SwiftUI OR SnapKit**: hands-on experience building UI (>=1 real screen in production or portfolio app) | Must | | [FILL: app name + which framework used + App Store link or GitHub] | Rebuild ONE screen of an existing app in your chosen framework (4–6 hours); commit it to GitHub with a README explaining the layout logic |
| **Developed & released >=1 iOS app**: shipped to App Store, TestFlight, or public GitHub with real code | Must | | [FILL: app name + link (App Store / TestFlight / GitHub) + ship date or GitHub created date] | Ship a small single-feature app (Weather, Todo, Notes, Timer) this week; don't polish, just ship; GitHub is fine, App Store makes it stronger |
| **Works independently, hits deadlines, manages remote work**: delivers on time; proactively debugs; communicates async; no hand-holding | Must | | [FILL: describe a recent project you shipped solo + timeline + any blockers you unblocked yourself] | Write a half-page "My Remote Work & AI Workflow" doc: timezone, async comms style, how you track time, how you ask for help; share in interview |
| **Uses AI tools (ChatGPT, Claude, Gemini, Cursor, Codex) to boost productivity**: integrates AI into your coding loop; not just "I've used it once" | Must | | [FILL: which tools you use + 1 concrete example (e.g., "I use Claude in Cursor to refactor, ChatGPT for Stack Overflow replacements, Gemini for API docs")] | Record a 3–5 min Loom: open Cursor + your code, ask Claude to refactor one function, iterate on its suggestion, show how you verify the result; upload to a shared drive or Slack |
| **MVVM or similar architecture**: aware that View ≠ ViewModel ≠ Model; can organize code accordingly | Nice | | [FILL: link to a screen in your app where you separated concerns (even informally); describe the layers] | Pick the messiest View in your app; refactor it to strict MVVM (ViewController/ViewModel/Model); commit with a 1-line explanation: "Separated [old pattern] → ViewModel handles [logic], View only renders" |
| **Clean Code awareness**: avoids duplication, names things well, keeps functions small | Nice | | [FILL: example of a refactoring or design choice you made to reduce technical debt] | Find ONE code smell in your app (long function, confusing name, duplicated logic); fix it; commit with a 1-line explanation |
| **English proficiency for remote/international**: can write async Slack/email, not just code comments; can voice-call with non-native accent and be understood | Implied Must | | [FILL: examples of written comms (GitHub issues you've written, Slack threads, README clarity) + estimate your confidence (e.g., "native speaker", "fluent, 10 yrs experience", "intermediate, working on it")] | No action needed if comfortable; if uncertain, do a 2-min self-video intro ("Hi, I'm [name], I'm applying for the iOS role, I'm based in [timezone], I've shipped [app]") and watch it back |

---

## Scoring Guide

- **1–2**: Weak or missing. Blocker for this role unless you can close it *this week*.
- **3**: Adequate. You meet the requirement, but there's room to grow; the "close the gap" action would strengthen your candidacy.
- **4**: Strong. Clear evidence, recently used, confident in interviews.
- **5**: Very strong. You could teach this; excited to demonstrate it.

---

## Apply-Readiness Gate

**You are ready to apply if:**
- ✅ ALL Must-haves are self-rated ≥3, **AND**
- ✅ You have ≥1 real, shippable app (App Store, TestFlight, or public GitHub) with code you can talk through

**If any Must-have is <3 OR you have no shippable app:** DO NOT apply yet. Instead, pick the **top 1–2 highest-leverage actions below**, do them this week, then apply.

---

## Highest-Leverage Actions to Close Gaps (ranked by impact)

**If you're missing a shippable app:**
1. **SHIP a small single-feature app to App Store or GitHub this week.** Non-negotiable. The job posting says *"has developed or released at least 1 iOS app"* — this is the proof.
   - Weather app (fetch API, display in SwiftUI or SnapKit): 6–8 hours.
   - Todo app (CRUD, UserDefaults or Core Data): 4–6 hours.
   - Notes app (SwiftUI + FileManager): 5–7 hours.
   - Commit to GitHub with a 3-line README. That's it.

**If Swift is <3:**
2. **Spend 2 hours on LeetCode/HackerRank Swift problems.** Pick "Easy," nail 3–5, screenshot your solutions, add them to a GitHub repo called `swift-drills` or similar. In the interview, talk through one: "I solved [problem], the tricky part was [optionals / unwrapping / closures], I'd use this approach for..."

**If SwiftUI/SnapKit is <3:**
3. **Rebuild ONE screen of your app in your target framework.** If you used UIKit, rebuild it in SwiftUI. If you used SwiftUI, rebuild it in SnapKit to show flexibility. Commit with a message: "Refactored [screen name] to SwiftUI: VStack for layout, @State for toggling, NavigationStack for nav." 2–4 hours.

**If you don't use AI tools in your loop yet:**
4. **Install Cursor (or use Claude in your IDE).** Spend 1 hour: open your repo, ask Claude to explain your most complex function, then ask it to refactor one messy screen. Run the app, verify it still works. Record a 3-min Loom: "Here's how I use Claude to speed up refactoring — I paste the function, ask for a cleaner version, review the suggestion, then test." Send it to the hiring manager or mention it in the interview. **This is a differentiator for this specific role.**

---

## How to Present This Assessment in Your Interview or Application

1. **In your cover letter / application message:**
   > "I've self-assessed against the role using the fit & gap rubric. I'm strong on [Must-haves], and here's my evidence: [shippable app link], [GitHub repo]. For [optional area], I'm actively improving by [action]."

2. **In the interview:**
   - Walk through your shippable app: open Xcode, show the code, explain the architecture (even if informal MVVM).
   - Show your AI workflow: open Cursor, ask Claude a coding question, explain how you verify the answer.
   - Describe your remote work style: timezone, how you debug solo, how you ask for help.

3. **Red flags to avoid:**
   - "I've used ChatGPT once to explain closures" ← too vague. Instead: "I use Claude in Cursor every day — I paste a method, ask for clarity on the logic, then test it."
   - "I'm building an app, it's almost done" ← no. Ship it *this week*, even if it's 50% feature-complete. A shipped 50% app beats a half-written perfect app.
   - "I understand MVVM" ← show a refactored screen in your repo, not words.

---

**Your next move:** Fill in the table above, score yourself, then — if any Must-haves are <3 or you lack a shippable app — execute the top 1–2 actions this week. Then apply. You've got this. 🚀


---

# 🇻🇳 Phiên bản Tiếng Việt

# Tự Đánh Giá Độ Phù Hợp & Khoảng Cách cho Lập Trình Viên iOS

Sử dụng rubric này để đánh giá chính mình một cách trung thực dựa trên yêu cầu của vị trí. Điền vào điểm tự đánh giá (1–5) và bằng chứng cho từng hàng. Cột "Lấp lỗ hổng" cung cấp cho bạn một giải pháp nhanh chóng nếu bạn yếu. Sau khi bạn chấm điểm, tuân theo cổng sẵn sàng nộp đơn ở dưới.

---

## Thang Đánh Giá Độ Phù Hợp & Khoảng Cách

| Yêu Cầu | Loại | Điểm (1–5) | Bằng Chứng Của Bạn [FILL] | Nếu yếu (≤2): cách nhanh nhất để lấp lỗ hổng |
|---|---|---|---|---|
| **Swift thành thạo**: có thể đọc/viết mã Swift đúng; hiểu optionals, closures, protocols, xử lý lỗi | Bắt buộc | | [FILL: liên kết đến repo GitHub / hồ sơ Codewars / mô tả bài toán Swift phức tạp nhất bạn đã giải quyết] | Ship một công cụ CLI Swift nhỏ hoặc giải pháp thuật toán (2–3 giờ trên LeetCode/HackerRank); kèm theo video Loom 2 phút giải thích mã |
| **SwiftUI HOẶC SnapKit**: kinh nghiệm thực tế xây dựng UI (>=1 màn hình thực trong production hoặc ứng dụng portfolio) | Bắt buộc | | [FILL: tên ứng dụng + framework nào được sử dụng + liên kết App Store hoặc GitHub] | Tái cấu trúc MỘT màn hình của ứng dụng hiện có bằng framework bạn chọn (4–6 giờ); commit lên GitHub với README giải thích logic layout |
| **Đã phát triển & phát hành >=1 ứng dụng iOS**: đã ship lên App Store, TestFlight, hoặc GitHub công khai với mã thực | Bắt buộc | | [FILL: tên ứng dụng + liên kết (App Store / TestFlight / GitHub) + ngày phát hành hoặc ngày tạo GitHub] | Ship một ứng dụng nhỏ có một tính năng (Weather, Todo, Notes, Timer) tuần này; không cần đánh bóng, chỉ cần ship; GitHub được, App Store sẽ mạnh hơn |
| **Làm việc độc lập, đáp ứng deadline, quản lý làm việc từ xa**: giao hàng đúng thời hạn; tự sửa lỗi chủ động; giao tiếp async; không cần người hướng dẫn | Bắt buộc | | [FILL: mô tả một dự án gần đây bạn ship một mình + timeline + bất kỳ trở ngại nào bạn tự mở khóa] | Viết một tài liệu nửa trang "Quy Trình Làm Việc Từ Xa & AI của Tôi": múi giờ, phong cách giao tiếp async, cách bạn theo dõi thời gian, cách bạn yêu cầu giúp đỡ; chia sẻ trong phỏng vấn |
| **Sử dụng AI tools (ChatGPT, Claude, Gemini, Cursor, Codex) để tăng năng suất**: tích hợp AI vào vòng lặp coding; không chỉ "tôi đã sử dụng nó một lần" | Bắt buộc | | [FILL: công cụ nào bạn sử dụng + 1 ví dụ cụ thể (ví dụ: "Tôi sử dụng Claude trong Cursor để refactor, ChatGPT thay cho Stack Overflow, Gemini cho API docs")] | Ghi một video Loom 3–5 phút: mở Cursor + mã của bạn, yêu cầu Claude refactor một hàm, lặp lại đề xuất của nó, cho thấy cách bạn xác minh kết quả; tải lên ổ dùng chung hoặc Slack |
| **MVVM hoặc kiến trúc tương tự**: nhận thức rằng View ≠ ViewModel ≠ Model; có thể tổ chức mã theo đó | Tốt | | [FILL: liên kết đến màn hình trong ứng dụng của bạn nơi bạn tách biệt concerns (thậm chí không chính thức); mô tả các layers] | Chọn View lộn xộn nhất trong ứng dụng của bạn; refactor nó thành MVVM nghiêm ngặt (ViewController/ViewModel/Model); commit với giải thích 1 dòng: "Tách [mẫu cũ] → ViewModel xử lý [logic], View chỉ render" |
| **Nhận thức Clean Code**: tránh trùng lặp, đặt tên tốt, giữ hàm nhỏ | Tốt | | [FILL: ví dụ về refactoring hoặc lựa chọn thiết kế bạn đã thực hiện để giảm nợ kỹ thuật] | Tìm MỘT mùi mã trong ứng dụng của bạn (hàm dài, tên không rõ, logic bị trùng lặp); sửa nó; commit với giải thích 1 dòng |
| **Năng lực tiếng Anh cho làm việc từ xa/quốc tế**: có thể viết async Slack/email, không chỉ code comments; có thể gọi thoại với người không phải người bản xứ và được hiểu | Ngầm định Bắt buộc | | [FILL: ví dụ về giao tiếp bằng văn bản (GitHub issues bạn đã viết, Slack threads, độ rõ ràng README) + ước tính tự tin (ví dụ: "người bản xứ", "thành thạo, 10 năm kinh nghiệm", "trung bình, đang cải thiện")] | Không cần hành động nếu bạn cảm thấy thoải mái; nếu không chắc chắn, hãy quay một video giới thiệu 2 phút ("Xin chào, tôi là [tên], tôi đang nộp đơn cho vị trí iOS, tôi ở [múi giờ], tôi đã ship [ứng dụng]") và xem lại |

---

## Hướng Dẫn Chấm Điểm

- **1–2**: Yếu hoặc thiếu. Trở ngại cho vị trí này trừ khi bạn có thể lấp lỗ hổng *tuần này*.
- **3**: Đủ. Bạn đáp ứng yêu cầu, nhưng có chỗ để phát triển; hành động "lấp lỗ hổng" sẽ tăng cường tính cạnh tranh của bạn.
- **4**: Mạnh. Có bằng chứng rõ ràng, sử dụng gần đây, tự tin trong phỏng vấn.
- **5**: Rất mạnh. Bạn có thể dạy điều này; phấn khích muốn thể hiện nó.

---

## Cổng Sẵn Sàng Nộp Đơn

**Bạn sẵn sàng nộp đơn nếu:**
- ✅ TẤT CẢ các yêu cầu Bắt buộc có điểm tự đánh giá ≥3, **VÀ**
- ✅ Bạn có ≥1 ứng dụng thực, có thể phát hành (App Store, TestFlight, hoặc GitHub công khai) với mã bạn có thể thảo luận

**Nếu bất kỳ yêu cầu Bắt buộc nào <3 HOẶC bạn không có ứng dụng có thể phát hành:** KHÔNG nộp đơn bây giờ. Thay vào đó, chọn **1–2 hành động có hiệu ứng cao nhất dưới đây**, thực hiện chúng tuần này, sau đó nộp đơn.

---

## Hành Động Có Hiệu Ứng Cao Nhất để Lấp Lỗ Hổng (xếp hạng theo tác động)

**Nếu bạn thiếu ứng dụng có thể phát hành:**
1. **SHIP một ứng dụng nhỏ có một tính năng lên App Store hoặc GitHub tuần này.** Không thể thương lượng. Bài đăng việc làm nói *"đã phát triển hoặc phát hành ít nhất 1 ứng dụng iOS"* — đây là bằng chứng.
   - Ứng dụng Weather (fetch API, hiển thị trong SwiftUI hoặc SnapKit): 6–8 giờ.
   - Ứng dụng Todo (CRUD, UserDefaults hoặc Core Data): 4–6 giờ.
   - Ứng dụng Notes (SwiftUI + FileManager): 5–7 giờ.
   - Commit lên GitHub với README 3 dòng. Đó là tất cả.

**Nếu Swift <3:**
2. **Dành 2 giờ cho vấn đề Swift trên LeetCode/HackerRank.** Chọn "Easy", giải quyết 3–5 bài, chụp ảnh màn hình giải pháp của bạn, thêm chúng vào repo GitHub có tên `swift-drills` hoặc tương tự. Trong phỏng vấn, giải thích một bài: "Tôi đã giải quyết [vấn đề], phần khó khăn là [optionals / unwrapping / closures], tôi sẽ sử dụng cách tiếp cận này cho..."

**Nếu SwiftUI/SnapKit <3:**
3. **Tái cấu trúc MỘT màn hình của ứng dụng của bạn bằng framework mục tiêu.** Nếu bạn sử dụng UIKit, hãy tái cấu trúc nó trong SwiftUI. Nếu bạn sử dụng SwiftUI, hãy tái cấu trúc nó trong SnapKit để thể hiện tính linh hoạt. Commit với tin nhắn: "Refactored [tên màn hình] to SwiftUI: VStack cho layout, @State cho toggling, NavigationStack cho nav." 2–4 giờ.

**Nếu bạn chưa sử dụng AI tools trong vòng lặp của mình:**
4. **Cài đặt Cursor (hoặc sử dụng Claude trong IDE của bạn).** Dành 1 giờ: mở repo của bạn, yêu cầu Claude giải thích hàm phức tạp nhất của bạn, sau đó yêu cầu nó refactor một màn hình lộn xộn. Chạy ứng dụng, xác minh nó vẫn hoạt động. Ghi một video Loom 3 phút: "Đây là cách tôi sử dụng Claude để tăng tốc độ refactoring — tôi dán hàm, yêu cầu phiên bản sạch hơn, xem xét đề xuất, sau đó test." Gửi cho người quản lý tuyển dụng hoặc đề cập trong phỏng vấn. **Đây là điểm khác biệt cho vị trí cụ thể này.**

---

## Cách Trình Bày Tự Đánh Giá Này Trong Phỏng Vấn hoặc Đơn Xin Việc Của Bạn

1. **Trong thư xin việc / tin nhắn đơn xin việc của bạn:**
   > "Tôi đã tự đánh giá bản thân dựa trên rubric độ phù hợp & khoảng cách. Tôi mạnh trong [các yêu cầu Bắt buộc], và đây là bằng chứng của tôi: [liên kết ứng dụng có thể phát hành], [repo GitHub]. Đối với [lĩnh vực tùy chọn], tôi đang cải thiện chủ động bằng [hành động]."

2. **Trong phỏng vấn:**
   - Duyệt qua ứng dụng có thể phát hành của bạn: mở Xcode, hiển thị mã, giải thích kiến trúc (thậm chí nếu MVVM không chính thức).
   - Hiển thị quy trình làm việc AI của bạn: mở Cursor, hỏi Claude một câu hỏi về coding, giải thích cách bạn xác minh câu trả lời.
   - Mô tả phong cách làm việc từ xa của bạn: múi giờ, cách bạn sửa lỗi một mình, cách bạn yêu cầu giúp đỡ.

3. **Những dấu hiệu cảnh báo cần tránh:**
   - "Tôi đã sử dụng ChatGPT một lần để giải thích closures" ← quá mơ hồ. Thay vào đó: "Tôi sử dụng Claude trong Cursor mỗi ngày — tôi dán một phương thức, yêu cầu làm rõ logic, sau đó test nó."
   - "Tôi đang xây dựng một ứng dụng, nó sắp xong" ← không. Ship nó *tuần này*, thậm chí nếu nó chỉ 50% tính năng hoàn chỉnh. Một ứng dụng ship 50% đánh bại một ứng dụng bán hoàn thành hoàn hảo.
   - "Tôi hiểu MVVM" ← hiển thị một màn hình đã refactor trong repo của bạn, không phải lời nói.

---

**Bước tiếp theo của bạn:** Điền vào bảng trên, chấm điểm bản thân, sau đó — nếu bất kỳ yêu cầu Bắt buộc nào <3 hoặc bạn thiếu ứng dụng có thể phát hành — hãy thực hiện 1–2 hành động hàng đầu tuần này. Sau đó nộp đơn. Bạn sẽ làm được. 🚀
