<!-- compiled: 2026-07-11 -->
---
source: yt-dlp (path 5) — operator-submitted single video + double deep-dive into the original English resource
topic: api-security-7-techniques
generated: 2026-07-11
videos: 2 (LetDiv VN adaptation + Hayk Simonyan EN original)
notebook_id: — (no NotebookLM; transcripts read directly in main loop)
deliverable: report
---

# API Security — 7 Techniques (LetDiv VN video + Hayk Simonyan original) — RAW ingest

## Provenance (established in main loop 2026-07-11)

- **Operator-submitted video (ADAPTATION):** LetDiv "Học Lập Trình Đảm Bảo" — "7 Kỹ Thuật Bảo Mật API Bạn Phải Biết: Rate Limiting, CORS, SQL Injection, CSRF, XSS…", YouTube `XuzRt-BFIKU`, uploaded 2026-07-06, 423s (~7 min), 9,563 views, Vietnamese, channel 9,200 subs. Description promotes LetDiv's own Full Stack / Backend course (letdiv.com/khoa-hoc); cites NO source.
- **THE ORIGINAL RESOURCE (double-dive target):** Hayk Simonyan — "API Security Explained: Rate Limiting, CORS, SQL Injection, CSRF, XSS & More", YouTube `FsB_nRGdeLs`, uploaded **2025-08-12** (11 months earlier), 521s (~8.7 min), **438,198 views**, channel 136,000 subs. Sells a senior-engineer mentorship program (go.hayksimonyan.com).
- **Evidence LetDiv is the derivative:** (a) upload-date precedence 11mo; (b) title is a direct Vietnamese translation; (c) IDENTICAL 7-technique list AND order AND section boundaries (Intro / Rate Limiting / CORS / SQL & NoSQL Injection / Firewalls / VPNs / CSRF / XSS); (d) identical illustrative examples (SQL `--` bypass, bank-CSRF-via-session-cookie, blog-comment-XSS-steals-cookie, per-endpoint/per-IP/overall rate limiting). LetDiv localized the CORS domain example to letdiv.com, added concrete numbers (20 req / 5 min on video upload), and swapped Hayk's mentorship CTA for its own course CTA.
- Text reposts with the identical English title also exist (javarevisited.substack.com "API Security Explained: 7 Must-Know Protections"; c-sharpcorner.com) — downstream copies of Hayk's video (provenance chain verified in workflow wf_0d90e641-e67).

## Chapter map (both videos, same structure)

| Time (Hayk) | Time (LetDiv) | Technique |
|---|---|---|
| 0:00 | 0:00 | Introduction ("APIs are like doors into your system") |
| 0:18 | 0:24 | Rate Limiting |
| 2:39 | 2:33 | CORS |
| 4:05 | 3:06 | SQL & NoSQL Injection |
| 4:45 | 3:52 | Firewalls (WAF) |
| 5:21 | 4:23 | VPNs |
| 6:24 | 4:49 | CSRF |
| 7:17 | 5:56 | XSS |

---

## ORIGINAL — Hayk Simonyan (FsB_nRGdeLs) — full English transcript (auto-caption)

[00:00] APIs are like doors into your system. If
[00:02] you leave them unprotected, then
[00:04] attackers and anyone can walk right in
[00:07] and do whatever they want with your user
[00:09] data and overall the system. That&#39;s why
[00:12] in today&#39;s video, we&#39;ll look at seven
[00:14] proven techniques which will help you to
[00:15] protect your APIs from unwanted attacks.
[00:18] The first one we have in the list is
[00:20] rate limiting, which controls how many
[00:23] requests a client can make in a given
[00:25] time. For example, you can set a limit
[00:28] for user A to make, let&#39;s say, 100
[00:31] requests per some period of time to your
[00:33] API. And if they cross that limit and
[00:36] let&#39;s say make 101 requests, then you
[00:39] block the next request and allow some
[00:42] time to pass before they can send their
[00:44] next request. If you don&#39;t set this to
[00:46] your API, then attackers can overwhelm
[00:48] your system. they can send like
[00:50] thousands of requests per minute and
[00:53] then overwhelm your API which will take
[00:55] your system down or it can also brute
[00:57] force your data and these rate limits
[01:00] can be set per endpoint. For instance,
[01:02] let&#39;s say you have some / comments
[01:04] endpoint and here they can send a
[01:06] request to either create a comment or
[01:08] fetch comments. You can set that limit
[01:11] for endpoint level. So these comments
[01:13] endpoint will be set to some strict
[01:16] number of requests per minute. You can
[01:19] also set it per user or IP address.
[01:22] Let&#39;s say in A we have the IP address of
[01:24] first user and then B for the second C
[01:27] for this one and your attacker has some
[01:29] IP address which corresponds to D. If
[01:32] you get the 101 request from the D IP
[01:36] address then you will know that this
[01:38] user overused the API so you will block
[01:41] it at the user IP level. And there is
[01:44] also overall rate limiting to protect
[01:47] from DDOS attacks. Since you can set the
[01:50] rate limit to work per user or per IP
[01:53] address. That means that this attacker
[01:55] alone cannot send that many requests.
[01:57] You will block it with your rate
[01:59] limiting in the API. But what they can
[02:01] do is they can spin up some bots and
[02:04] each bot will have their own limit,
[02:06] right? Let&#39;s say you&#39;ve set it to 100
[02:08] per IP address. So each of these boats
[02:11] has 100 and overall they have more than
[02:14] you would allow or your system could
[02:16] handle. That&#39;s why you have also overall
[02:19] rate limitings which can be some bigger
[02:21] number. So whenever all the traffic
[02:24] coming into your server reaches or
[02:26] passes this number then you will
[02:28] temporarily block all requests until you
[02:31] find out the root cause. And of course
[02:33] these numbers are just examples. So in
[02:35] reality it&#39;s much more than thousand but
[02:38] that&#39;s just an example. The second one
[02:40] on the list is course which stands for
[02:42] cross origin resource sharing. This
[02:45] controls which domain can call your API
[02:48] from a browser and without proper course
[02:50] malicious websites could trick users
[02:53] browsers into making requests on their
[02:55] behalf. For instance, if your API is
[02:58] only meant to serve your front-end app
[03:00] which is at app.youdomain.com
[03:02] yourdommain.com
[03:04] then only requests from this source
[03:06] should be allowed. If anyone else sends
[03:09] you a request like up another domain.com
[03:11] then you should block this request and
[03:14] not allow them to use your API for
[03:16] authenticating or using any of its data.
[03:19] If you&#39;d like to learn these and other
[03:21] system design concepts in much more
[03:23] detail so that you can land senior
[03:26] developer roles with higher paying
[03:28] salaries, then you can check out the
[03:30] first link in the description which will
[03:31] be a link to my mentorship program.
[03:34] However, this is not for beginners. So,
[03:36] if you&#39;re an absolute beginner or you&#39;re
[03:38] a computer science graduate and you&#39;re
[03:40] just learning the fundamentals, then
[03:42] this is not for you. So, you should at
[03:44] least have one or more years of
[03:47] experience as a developer, and I&#39;ll help
[03:49] you to get to senior roles and higher
[03:52] paying salaries in the program with the
[03:54] one-on-one mentorship. So, fill out your
[03:56] details there to see if you qualify. And
[03:58] if you do, you&#39;ll meet in a call either
[04:00] with myself or someone from my team and
[04:03] we&#39;ll help you to get to that senior
[04:04] developer role. The third one is also a
[04:07] common one, which is SQL and NoSQL
[04:10] injections. Injection attacks can happen
[04:12] when the user input is directly included
[04:15] in the database query. For instance,
[04:17] attacker can modify it and send some
[04:20] queries to read or delete your data.
[04:23] Here for example, this part bypasses the
[04:26] checks entirely and then attacker can
[04:28] use this query to start reading data
[04:31] from your database or modify anything or
[04:34] they can also delete all the data all
[04:36] the user data and any other tables that
[04:38] you have in this database. So to fix
[04:41] this we always use parameterized queries
[04:44] or OM safeguards. The next technique to
[04:47] use is firewalls. A firewall acts as a
[04:51] gatekeeper filtering the malicious
[04:53] traffic from the other normal traffic.
[04:56] So typically you have it between your
[04:58] API and the incoming traffic. For
[05:00] example, if you use the AWS&#39;s web
[05:03] application firewall, these can block
[05:06] requests with unknown attack patterns
[05:08] such as suspicious SQL keywords or
[05:10] strange HTTP methods, which means it
[05:13] will block any suspicious requests from
[05:15] attackers, but it will allow others to
[05:18] bypass the request and reach to your
[05:20] API. Some APIs are also private and
[05:23] should only be accessed from specific
[05:26] networks. That&#39;s why we have also VPNs
[05:28] which stands for virtual private
[05:30] networks. The APIs that are within the
[05:33] VPN network can only be accessed by
[05:36] someone who is also within that same
[05:38] network. Which means that some APIs are
[05:40] public facing meaning these APIs will
[05:43] allow any requests from the internet
[05:45] from your users. But this for example
[05:48] can be within the VPN network. Which
[05:50] means if a user from web tries to reach
[05:53] your API then this request will be
[05:56] blocked because the user is not within
[05:58] the same network. But on the other hand
[06:00] if you have another user here which is
[06:02] within the VPN network they can make a
[06:05] request to these APIs and in this case
[06:08] they will bypass the checks and their
[06:10] request will reach to your APIs. This is
[06:13] useful where you have internal tools.
[06:15] Let&#39;s say you have internal admin
[06:16] dashboard and the API for this admin
[06:19] panel will only be reachable by
[06:21] employees connected to the company VPN.
[06:24] Next, we have CSRF, which stands for
[06:27] cross-sight request forgery. This tricks
[06:29] a logged in user&#39;s browser into making
[06:32] unwanted requests to the API. Let&#39;s say
[06:35] you as a user are logged in into your
[06:38] bank system and your bank system uses
[06:40] cookies for authentication. If the bank
[06:43] system is not secure and they only use
[06:46] session cookies, another malicious site
[06:48] might use your cookie and submit a
[06:50] hidden transferring money request
[06:52] through your cookie. So to prevent such
[06:55] attacks, companies also use CSRF tokens
[06:58] in combination with session cookie. So
[07:00] the banking system will check if the
[07:02] session cookie is present, but it will
[07:05] also check if the CSRF token matches
[07:07] with the one that they have. And if it
[07:09] doesn&#39;t then it will block this request
[07:12] from the other unknown source while it
[07:14] will allow request from your behalf. And
[07:17] the last one we have is XSS or it&#39;s also
[07:20] called cross-sight scripting. This lets
[07:22] attackers to inject scripts into web
[07:25] pages served to other users. For
[07:28] example, if you have a comment section
[07:30] and this comment gets submitted to your
[07:32] API. Next, your API will also store it
[07:35] in a database. You can get normal
[07:38] requests like nice picture or something
[07:40] like that and this will get to your API.
[07:42] Your API will store it in the database.
[07:45] So everything is fine there. But what if
[07:47] an attacker places a script in this
[07:50] comment section and within this script
[07:52] they can try to do many different
[07:55] things. For example, they can try to
[07:57] fetch the cookie for another user or
[07:59] they can try to inject something into
[08:01] your database. And if you allow this
[08:04] then it will reach to your server and
[08:06] the information will be written into the
[08:09] database. Later when the other users
[08:12] load this comments section on their
[08:14] screen, they will get also the injected
[08:17] comment directly into their web page and
[08:19] the browser will execute this malicious
[08:21] JavaScript code into the other users
[08:24] browser. These are the most common ways
[08:27] to attack an API and how you should
[08:29] protect it. If you&#39;d like to learn all
[08:31] of this hands-on with a real system and
[08:35] with my guidance, then check out the
[08:36] first link in the description to apply
[08:38] for the mentorship.

---

## ADAPTATION — LetDiv (XuzRt-BFIKU) — full Vietnamese transcript (auto-caption)

> Note: Vietnamese auto-caption; "IPI/ABI/IP" = API mis-transcriptions, "Ray/rain Limiting" = Rate Limiting, "C/cost" = CORS, "CFEF/CFA/CFF" = CSRF, "XXS" = XSS, "leddip.com" = letdiv.com, "OEM" = ORM.

[00:00] [âm nhạc] giống như cánh cửa dẫn vào hệ
[00:02] thống của bạn. Nhưng nếu bạn không biết
[00:04] cách bảo vệ ABI của mình, hacker có thể
[00:07] dễ dàng xâm nhập [âm nhạc] trái phép tự
[00:09] giá đánh cấp dữ liệu người dùng hoặc tệ
[00:11] hơn là chiếm quyền điều khiển toàn bộ hệ
[00:13] thống. Đó là lý do tại sao trong video
[00:16] này chúng ta sẽ cùng [âm nhạc] nhau tìm
[00:18] hiểu bay kỹ thuật bảo mật IPI tiêu chuẩn
[00:21] mà bất kỳ hệ thống nào cũng cần phải có.
[00:23] Đầu tiên là Ray Limiting. Đây là kỹ
[00:27] thuật giúp bạn kiểm soát được số lượng
[00:28] request tối đa mà một user có thể thực
[00:31] hiện trong một khoảng thời gian nhất
[00:33] định. Ví dụ bạn có thể đặt giới hạn cho
[00:36] user A chỉ có thể thực hiện tối đa 100
[00:39] request đến IPI trong một khoảng thời
[00:41] gian 15 phút. Trong khoảng thời gian
[00:43] này, nếu user A thực hiện nhiều hơn 100
[00:46] request, hệ thống sẽ tạm thời ngăn chặn
[00:48] cho đến khi 15 phút trôi qua thì mới
[00:51] được phép truy cập lại. Nếu bạn không
[00:53] thiết lập ray Limiting, hacker có thể
[00:55] gửi hàng nghìn request mọi phút dẫn đến
[00:57] quá tải và làm sập toàn bộ hệ thống máy
[01:00] chủ hoặc hacker có thể sử dụng kỹ thuật
[01:02] tấn công viết cạn liên tục spam request
[01:05] vào IPI login để dò tìm mật khẩu người
[01:08] dùng. Có ba cách phổ biến để bạn thiết
[01:10] lập rain limiting. Thứ nhất là thiết lập
[01:13] giới hạn cho từng API cụ thể. Giả sử bạn
[01:17] có một IP chuyên dùng để upload video.
[01:20] Mỗi khi IPI này được sử dụng sẽ tiêu tốn
[01:22] khá nhiều tài nguyên của hệ thống. Do đó
[01:25] bạn có thể thiết lập giới hạn là trong
[01:27] vòng 5 phút API này chỉ có thể tiếp nhận
[01:30] tối đa 20 request. Nghĩa là nếu user A
[01:33] thực hiện tổng cộng 15 request đến API
[01:36] upload video thì các user còn lại chỉ có
[01:39] thể thực hiện tổng cộng toa 5 request
[01:41] thôi. Bên cạnh đó, bạn cũng có thể thiết
[01:43] lập giới hạn cho mọi địa chỉ IP của
[01:46] người dùng. Giả sử hacker thực hiện spam
[01:48] liên tục 100 request đến IPI login nhưng
[01:51] đến lần request thứ tư đã bị chặn hoàn
[01:54] toàn do vượt ngưỡng giới hạn cho phép.
[01:56] Đương nhiên, hệ thống chỉ giới hạn địa
[01:58] chỉ IP của hacker, còn các địa chỉ IP
[02:00] khác vẫn có thể gọi IPI login như bình
[02:03] thường. Chính vì vậy, hacker có thể dễ
[02:05] dàng vượt qua lớp ba mặt này bằng cách
[02:07] tạo ra hàng trăm con bots. Mỗi con boss
[02:10] có địa chỉ IP riêng thì việc giới hạn IP
[02:13] cũng coi như vô dụng. Đây chính là kiểu
[02:15] tấn công DDOS nổi tiếng. Đó là lý do bạn
[02:18] cũng cần thiết lập giới hạn tổng quan
[02:20] cho toàn bộ hệ thống. Thường là một con
[02:22] số có giá trị khá lớn. Nếu tổng số lượng
[02:25] request tăng đột biến vượt qua giới hạn
[02:27] này, hệ thống sẽ tạm thời chặn tất cả
[02:29] các request cho đến khi mọi thứ ổn định
[02:31] trở lại. Kỹ thuật thứ hai là C. Đây là
[02:35] kỹ thuật giúp bạn giới hạn chỉ một số
[02:37] tên miền cụ thể mới được phép gọi IPI.
[02:40] Nếu không thiết lập cost, hacker có thể
[02:42] sử dụng trái phép IPI của bạn để đánh
[02:44] cấp thông tin người dùng. Ví dụ, nếu bạn
[02:47] thiết lập hệ thống chỉ nhận request từ
[02:49] tên miền leddip.com, mọi yêu cầu gọi IP
[02:52] từ các tên miền khác đều sẽ bị chặn lại.
[02:55] Nếu bạn muốn tự tay thiết kế và đưa các
[02:57] kỹ thuật bảo mật này vào bên trong dự án
[02:59] thực tế, bạn có thể tham khảo khóa học
[03:01] Full Stack hoặc Bend tại phần mô tả hoặc
[03:04] bình luận nhé. Một phương pháp tấn công
[03:06] khá phổ biến của hacker là SQL và No SQL
[03:10] injection. Lộ hỏng này xảy ra khi hệ
[03:12] thống lấy trực tiếp dữ liệu từ người
[03:14] dùng và ghép nối ngay vào câu lệnh chi
[03:17] vấn cơ sở dữ liệu khi chưa được xác thật
[03:19] hoặc kiểm tra độ an toàn. Như trong ví
[03:21] dụ ở đây, hacker cố tình chèn ký tự hai
[03:24] dấu gạch ngang để vô hiệu hóa hoàn toàn
[03:26] bước kiểm tra mật khẩu. Nghĩa là chỉ cần
[03:28] nhập đúng username là đã có thể đăng
[03:31] nhập vào hệ thống. Hoặc tệ hơn là hacker
[03:34] có thể chiếm quyền toàn bộ database và
[03:36] xóa sạch dữ liệu của bạn. Để khắc phục
[03:38] vấn đề này, bạn luôn cần phải tham số
[03:40] hóa dữ liệu đầu vào của người dùng hoặc
[03:43] sử dụng các tính năng bảo mật tích hợp
[03:44] sẵn trong các thư viện OEM thay vì tự
[03:47] viết các câu lệnh truy vấn SQL và nối
[03:49] SQL một cách thủ công. Kỹ thuật bảo mật
[03:52] tiếp theo là tường lửa. Nếu IPI là cánh
[03:55] cổng để vào hệ thống thì tường lửa chính
[03:57] là người gác cổng. Nó sẽ liên tục phân
[03:59] tích các request gửi đến và đối chiếu
[04:02] với các dấu hiệu tấn công trong lịch sử
[04:04] trước đó để lọc ra các request độc hại
[04:06] trước khi chúng đi đến ABI của bạn. Bạn
[04:09] không cần phải tự tay xây dựng tường lửa
[04:11] từ đầu. Thay vào đó, bạn nên sử dụng các
[04:14] dịch vụ cloud vô cùng mạnh mẽ từ các nhà
[04:16] cung cấp như AWS, Cloud Flare để tự động
[04:19] nhận diện và chặn đứng các request độc
[04:21] hại. Nếu hệ thống của bạn có các API nội
[04:25] bộ như API cho hệ thống quản trị admin,
[04:27] quản lý nhân sự, hệ thống kế toán vân
[04:29] vân. Vì vấn đề bảo mật các API này không
[04:32] nên được truy cập từ bên ngoài. Để làm
[04:34] được như vậy, bạn cần VBN tạm dịch là
[04:38] mạng nội bộ riêng tư. VBN chỉ cho phép
[04:40] những người dùng trong mạng nội bộ mới
[04:42] có thể truy cập IPI. Còn nếu có người
[04:45] dùng bên ngoài cố gắng truy cập IPI thì
[04:47] sẽ bị chặn lại. CFEF là phương thức tấn
[04:50] công mà hacker mượn chính trình duyệt
[04:53] của user để âm thầm gửi các request phá
[04:55] hoại đến IPI mà user không hề hay biết.
[04:58] Giả sử bạn đã đăng nhập thành công vào
[05:00] hệ thống ngân hàng và hệ thống này sử
[05:03] dụng cơ chế cookie để xác thực phiên
[05:05] đăng nhập của bạn. Nếu hệ thống ngân
[05:06] hàng không được bảo mặt kỹ càng, hacker
[05:09] có thể lừa bạn truy cận vào một trang
[05:11] web độc hại nào đó. Trang web này có thể
[05:13] sử dụng cookie được lưu trên trình duyệt
[05:15] của bạn để gửi một request chuyển tiền
[05:17] trái phép lên hệ thống ngân hàng. Tại vì
[05:20] cooky này hoàn toàn hợp lệ, hệ thống
[05:22] ngân hàng sẽ bị đánh lừa rằng chính bạn
[05:24] là người thực hiện thao tác chuyển tiền
[05:26] và cuối cùng là bạn bị mất hết toàn bộ
[05:28] số tiền trong tài khoản. Để ngăn chặn
[05:31] các cuộc tấn công như vậy, các hệ thống
[05:32] ngân hàng thường sử dụng mã CFA kết hợp
[05:35] với cookie. Khi có một request gửi lên,
[05:38] hệ thống không chỉ kiểm tra xem có hợp
[05:40] lệ hay không mà còn bắt buộc phải xem mã
[05:43] CFF có khớp với mã được hệ thống cấp
[05:45] phát trước đó hay không. Nếu không, hệ
[05:48] thống sẽ chặn reo này ngay lập tức.
[05:50] Ngược lại, nếu cả hai đều hợp lệ thì cho
[05:53] phép truy cập như bình thường. Cuối cùng
[05:55] là phương thức tấn công XXS. Đây là
[05:58] phương thức tấn công mà hacker sẽ tìm
[06:00] cách chèn trực tiếp mã đọc gia strip vào
[06:03] bên trong trang web để nó có thể thực
[06:05] thi trên trình duyệt của nạn nhân. Ví dụ
[06:07] khi bạn truy cập vào một trang blog, nếu
[06:10] bạn gửi một bình luận thì nội dung bình
[06:12] luận này sẽ được gửi đến IPI, sau đó là
[06:15] được lưu chữ bên trong database. Lúc này
[06:18] các user khác đều có thể nhìn thấy bình
[06:20] luận của bạn. Tuy nhiên, thay vì nhập
[06:22] nội dung bình luận như thông thường,
[06:24] hacker có thể chèn một đoạn mã đọc
[06:25] JavaScript để lấy giá trị cooky của
[06:28] người dùng. Khi những người dùng khác vô
[06:30] tình đọc nội dung bình luận của hacker
[06:32] thì trên duyệt sẽ tự động thực thi đoạn
[06:34] mã độc này và gửi cooky đến cho hacker.
[06:37] Để phòng chống các cuộc tấn công XXS,
[06:39] bạn cần phải vô hiệu hóa toàn bộ các ký
[06:41] tự đặc biệt trước khi hiển thị chúng lên
[06:44] diện. Như vậy chúng ta đã tìm hiểu qua
[06:46] các phương thức tấn công IP phổ biến
[06:48] nhất và bảy kỹ thuật bảo mật dùng để
[06:50] ngăn chặn các cuộc tấn công này. Để
[06:52] không chỉ hiểu bản chất mà còn tự tin áp
[06:55] dụng những kỹ thuật bảo mật này vào dự
[06:57] án thực tế. Bạn có thể tham khảo có học
[06:59] Fullst và Bend tại phần mô tả hoặc bình
[07:02] luận nhé. Ah.
---

## Canonical verification layer

Both videos verified against OWASP (API Security Top 10 2023 + CSRF/XSS/SQLi/CORS cheat sheets), MDN CORS, NIST Zero Trust (SP 800-207), RFC 6585, AWS/Cloudflare WAF docs via Workflow wf_0d90e641-e67 (dive + refute-first verify + completeness critic). See wiki/api-security-7-techniques/ for compiled findings.
