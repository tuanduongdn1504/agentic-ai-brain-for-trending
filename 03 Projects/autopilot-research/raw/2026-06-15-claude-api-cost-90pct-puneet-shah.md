---
source: yt-dlp-only (path 5)
topic: claude-api-cost-optimization
video_title: "Giảm 90% Chi Phí Claude API | Prompt Caching, Tool Search & Advisor Demo Thực Tế - Puneet Shah"
video_url: https://www.youtube.com/watch?v=y6hvZGpwf7E
channel: BizMate AI Official (re-upload, Vietnamese subtitles)
original_speaker: Puneet Shah (PM, Platform team, Anthropic)
original_event: Code with Claude — London (closing session)
upload_date: 2026-06-09
duration: 26:37
ingested: 2026-06-15
language: vi (auto-captions, deduplicated)
notebook_id: none (direct yt-dlp VTT ingest)
---

# Transcript — Claude API cost optimization (Puneet Shah, Anthropic)

> Vietnamese auto-caption track, deduplicated. Timestamps are caption start times.
> This is a re-upload; the speaker is Puneet Shah (Anthropic Platform PM) at "Code with Claude" London.

[00:00:17] Xin mời lên sân khấu Puneet Shah, nhân viên kỹ thuật tại Anthropic.
[00:00:31] Chào mừng buổi cuối của Code with Claude tại London.
[00:00:35] Hãy cùng vỗ tay chào đón tất cả những người đã đến trước.
[00:00:39] Tuyệt!
[00:00:42] Tôi là Product Manager thuộc đội Platform tại Anthropic, từng triển khai nhiều tính năng
[00:00:47] như cửa sổ ngữ cảnh 1 triệu token, FastMode và cải tiến về prompt caching. Điều này khiến tôi rất hào hứng với buổi này.
[00:00:57] Các bạn đã có quyết định đúng khi đến đây vì nội dung xoay quanh Cloud Platform.
[00:01:02] Chúng ta có những model xuất sắc, nhưng còn cả một lớp nền tảng phía trên, không chỉ cung cấp trí tuệ mà còn giúp xây dựng doanh nghiệp và sản phẩm thực sự mang lại giá trị cho người dùng.
[00:01:16] Vì đây là buổi cuối, hãy cùng tạo không khí sôi động.
[00:01:22] Nếu bạn đã xây agent nào đó, dù lớn hay nhỏ, hãy đứng lên.
[00:01:27] Tốt lắm, rất nhiều người xây agent ở đây, thật tuyệt.
[00:01:36] Nếu đã đưa vào production, hãy đứng yên, còn lại mời ngồi.
[00:01:44] Nếu hài lòng về chất lượng, chi phí và tốc độ, hãy đứng, còn lại mời ngồi.
[00:01:55] Tốt lắm, hãy nhìn xung quanh.
[00:01:58] Hãy nhớ những người này, họ là chuyên gia thực sự.
[00:02:00] Hãy tìm họ tại happy hour sau đó.
[00:02:03] Bây giờ mời mọi người ngồi. Cảm ơn đã ủng hộ.
[00:02:07] Mục tiêu buổi này là chia sẻ kinh nghiệm tối ưu hóa Claude Platform.
[00:02:15] Một trong những tính năng đầu tiên trên nền tảng mà tôi muốn nói đến là prompt caching.
[00:02:21] Nếu bạn chỉ nhớ một điều từ buổi này, hãy nhớ về prompt caching.
[00:02:25] Prompt caching là cách chúng ta xử lý input tokens, lưu lại trước khi tạo output tokens.
[00:02:35] Cache này sẽ được tái sử dụng khi cuộc hội thoại tiếp diễn.
[00:02:40] Khi có tin nhắn mới, ta chỉ xử lý token mới, phần còn lại lấy từ cache.
[00:02:49] Tại sao điều này hữu ích cho bạn?
[00:02:52] Lý do đầu tiên là bạn được giảm 90% chi phí vì không xử lý lại các token.
[00:02:59] Bạn được giảm 90%, tiết kiệm chi phí lớn khi xây dựng agent.
[00:03:06] Lý do thứ hai là bạn nhận được tăng tốc giới hạn tốc độ.
[00:03:11] Giới hạn tốc độ của chúng ta không tính các token đã được cache.
[00:03:16] Nếu tỷ lệ hit cache đạt 80%, nghĩa là 80% token được lưu cache, bạn sẽ có giới hạn tốc độ thực tế cao gấp năm lần.
[00:03:26] Điều đó rất tuyệt. Lợi ích cuối cùng là độ trễ.
[00:03:29] Khi bạn cache nhiều và cuộc hội thoại dài hơn, do không còn xử lý hết các token, thời gian nhận token đầu tiên sẽ giảm.
[00:03:40] Đây là những lợi ích lớn. Nếu bạn đang tìm mục tiêu khi xây dựng agentic
[00:03:45] ứng dụng, mức trên 80% là điểm mục tiêu lý tưởng để hướng tới.
[00:03:51] Nhưng nếu nhìn vào các khách hàng như Replit, Cursor, Perplexity, Clawd Code, họ đạt 90
[00:03:57] phần trăm trở lên. Những khách hàng này đã nỗ lực rất nhiều, tôi đã nói chuyện với họ,
[00:04:02] họ đã đầu tư rất nhiều để prompt caching hoạt động tốt nhờ các lợi ích đã nêu và Cotibed.
[00:04:08] Điều đầu tiên họ làm là hiểu tỷ lệ hit cache prompt của bạn là bao nhiêu, bạn đạt được mức nào.
[00:04:15] Đó là câu hỏi đầu tiên bạn cần hiểu.
[00:04:17] May mắn thay, vì hiểu rõ nỗ lực của họ, chúng tôi tự hỏi: sao không xây dựng nó cho bạn?
[00:04:22] Hôm nay, nếu truy cập console trên nền tảng cloud,
[00:04:28] tại console.anthropic.com, bạn sẽ thấy analytics ngay cạnh trang chi phí và mức sử dụng.
[00:04:33] Bạn có thể xem analytics về prompt caching.
[00:04:35] Ngay hôm qua, chúng tôi tiếp tục cải thiện tính năng này.
[00:04:38] Hôm qua, chúng tôi ra mắt cách xác định lý do cache bị lỗi.
[00:04:42] Hóa ra thứ tự tạo prompt ảnh hưởng rất lớn.
[00:04:45] Lỗi phổ biến là đưa timestamp vào system prompt.
[00:04:50] Biết ngày hôm nay rất hữu ích, nhưng nó làm thay đổi system prompt, từ đó phá vỡ cache.
[00:04:58] Các token phải giống hệt nhau.
[00:05:00] Bạn có thể xem lỗi xảy ra ở đâu trên trang analytics.
[00:05:05] Đây là điểm khởi đầu tuyệt vời.
[00:05:08] Nếu thấy 0%, đừng lo, đó là lý do bạn ở đây.
[00:05:10] Bạn có thể bắt đầu bằng thay đổi code một dòng với auto-caching.
[00:05:14] Nó thực hiện basic prompt caching.
[00:05:16] Hoặc tốt hơn, hãy vào Cloud API skill.
[00:05:19] Truy cập Cloud Code hoặc nhiều coding agents khác có skill tích hợp sẵn.
[00:05:25] Giúp bạn yêu cầu cải thiện cache hit rate và tối ưu prompt để đạt hiệu suất cao nhất.
[00:05:34] Prompt caching cực kỳ quan trọng.
[00:05:35] Chúng ta sẽ bàn thêm, nhưng tôi muốn chia sẻ dự án startup đang rất hào hứng này.
[00:05:45] Ngoài ra, tôi còn là CEO của HeroCorp, và CTO Ben đang ở đây, mời Ben ra sân khấu.
[00:05:53] Anh ấy điều hành đội công nghệ, hãy cùng vỗ tay cho Ben.
[00:05:59] Chúng ta có thể chuyển sang máy tính demo không?
[00:06:01] Khoan đã, Ben, đây là Clawed with Code. Đây là năm 2026.
[00:06:09] Giao diện này trông như từ thập niên 90.
[00:06:11] Chuyện gì thế? Ai muốn giao diện hiện đại hơn?
[00:06:15] Ừ, có vài cái like.
[00:06:17] Được rồi Ben, hãy cải thiện giao diện.
[00:06:18] Hãy chuẩn bị cho Code with Clawed.
[00:06:26] Để nó chạy.
[00:06:30] Tuyệt. Chúng tôi là HeroCorp.
[00:06:32] Chúng tôi là công ty siêu anh hùng thuê ngoài.
[00:06:36] Chúng tôi giúp chống tội phạm, giữ tàu chạy đúng giờ, tổ chức sinh nhật và đảm bảo đủ bóng bay.
[00:06:46] Chúng tôi làm tất cả. Một số người hiểu lầm về thế giới siêu anh hùng, nghĩ chúng tôi làm bừa.
[00:06:55] Chúng tôi phân tích, dùng OKR, lên kế hoạch, đó là lý do có dashboard.
[00:07:00] Dashboard này giúp chúng tôi theo dõi hiệu suất.
[00:07:03] Bạn thấy tỷ lệ giữ chân 90 ngày là 94%, có thể tốt hơn.
[00:07:07] Có một rủi ro bay, có lẽ do lương thấp. Tôi nên trả lương cao hơn.
[00:07:15] Bạn thấy các siêu anh hùng trong Vũ trụ Điện ảnh Anthropic.
[00:07:20] Luật sư yêu cầu dùng tên này thay vì tên khác.
[00:07:25] Được liệt kê cùng nhận định về tình hình hiện tại.
[00:07:28] Hãy mở bảng điều khiển developer mà ta đã xây.
[00:07:32] Tôi sẽ nhắc lại điều này nhiều lần.
[00:07:35] Luôn xem transcript agent để hiểu rõ diễn biến.
[00:07:39] Tại đây, ta thấy dữ liệu được kéo từ web, Slack, Gong.
[00:07:49] Từ Jira và các nguồn khác để tổng hợp cái nhìn toàn diện.
[00:07:56] Tỷ lệ hit cache của prompt là bao nhiêu?
[00:08:00] Bạn có muốn xem không?
[00:08:02] Không? Ben, cố lên nào.
[00:08:06] Được, hãy triển khai prompt caching.
[00:08:08] Đó chính là điểm khởi đầu.
[00:08:11] Tỷ lệ cache hit hiện ở mức 0, nhưng chúng ta sẽ cải thiện.
[00:08:15] Hiện tại chi phí khoảng 31 pounds, như bạn thấy trước khi nó biến mất.
[00:08:19] Chúng ta vừa triển khai prompt caching, kết quả bên phải hoàn toàn giống nhau.
[00:08:25] Output này giống hệt. Prompt caching không ảnh hưởng trí tuệ, chỉ tối ưu chi phí.
[00:08:33] Thay vì khối dài, ta lưu vào cache và tái sử dụng. Zoom vào sẽ thấy cache write 172 tokens.
[00:08:43] Ngay phía trên là cache hit 172 tokens.
[00:08:48] Dữ liệu được ghi vào cache, khi hội thoại tiếp tục, ta tái sử dụng tokens và tiết kiệm 90%.
[00:08:58] Chi phí agent đã giảm một nửa nhờ đạt tỷ lệ cache hit khoảng 58%.
[00:09:06] Rất tuyệt.
[00:09:08] Đây là bước khởi đầu tốt.
[00:09:10] Hãy xem phần còn lại của dashboard.
[00:09:15] Chờ đã, Ben, có tới năm OKR.
[00:09:18] Tôi cấp một triệu token context và đây là kết quả.
[00:09:23] Context window đã đầy, cần làm thêm việc. Hãy quay lại slide.
[00:09:30] Chúng ta cần context engineering, nghệ thuật và
[00:09:40] khoa học xác định context nào đưa cho Claude để agent
[00:09:45] hoạt động tốt nhất. Tôi đã nhắc nhiều lần, hãy xem
[00:09:50] transcript để biết mô hình thực sự nhìn thấy gì.
[00:09:56] Điều này sẽ cho thấy bạn đang gửi thừa thông tin không cần thiết hay giữ đúng trọng tâm.
[00:10:05] Hôm nay, ta sẽ điểm qua ba kỹ thuật chính để cải thiện context engineering cho mô hình của bạn.
[00:10:13] Đầu tiên là xác định công cụ nào cần truyền cho mô hình và thu hẹp phạm vi lựa chọn.
[00:10:20] Tiếp theo là lọc kết quả từ các công cụ đó gửi cho mô hình, giúp duy trì ngữ cảnh gần như vô hạn trong lịch sử hội thoại.
[00:10:33] Hãy cùng xem xét từng kỹ thuật một.
[00:10:36] Kỹ thuật đầu tiên là tìm kiếm công cụ.
[00:10:38] Các agent sử dụng rất nhiều công cụ.
[00:10:42] Một trong những yếu tố tạo nên agent xuất sắc chính là các lệnh gọi công cụ.
[00:10:46] Mô hình Claude đặc biệt giỏi trong việc tận dụng các công cụ này, với hàng chục thậm chí hàng trăm công cụ được dùng hiện nay.
[00:10:56] Tuy nhiên, vấn đề là khi định nghĩa và truyền tất cả công cụ cho mô hình, chúng sẽ chiếm dụng rất nhiều ngữ cảnh.
[00:11:05] Điều này làm giảm đáng kể không gian dành cho các tác vụ thực tế cần thực hiện trong mô hình.
[00:11:10] Như bạn thấy, ngữ cảnh đầy sau vài lượt trao đổi.
[00:11:15] Thay vào đó, ta dùng Tool Search Tool.
[00:11:18] Tool Search Tool xác định: bạn định nghĩa sẵn công cụ, nhưng chỉ truyền
[00:11:23] mô hình một công cụ hướng dẫn: khi cần, hãy gọi công cụ này, nó sẽ trả danh sách, rồi mới đưa định nghĩa thực vào ngữ cảnh.
[00:11:33] Nhìn hàng giữa, ta chỉ truyền các công cụ màu cam khi cần, dành nhiều chỗ hơn cho nội dung thực sự.
[00:11:43] Lovable đã thử cách này.
[00:11:44] Bobion vừa chia sẻ, nhờ Tool Search, họ giảm 10% token tiêu thụ chỉ với giải pháp này.
[00:11:57] Quan trọng hơn, hiệu suất mô hình của họ cũng được cải thiện.
[00:12:01] Vì giảm rác trong ngữ cảnh, chỉ đưa thông tin liên quan vào.
[00:12:08] Kết quả là mô hình hoạt động tốt hơn.
[00:12:11] Họ đã triển khai tính năng này cho tất cả người dùng.
[00:12:13] Vậy là đã xong phần tìm kiếm công cụ.
[00:12:15] Bạn sẽ xử lý kết quả từ các công cụ đó như thế nào?
[00:12:19] Bước tiếp theo là gọi công cụ theo lập trình.
[00:12:22] Với việc gọi công cụ theo lập trình, ý tưởng là lọc nội dung từ công cụ, chỉ giữ phần liên quan nhất.
[00:12:31] Điểm mấu chốt là Claude rất giỏi trong việc viết code.
[00:12:37] Nếu từng dùng Claude Code hay công cụ code khác, bạn đã thấy điều này. Chúng ta tận dụng lợi thế đó.
[00:12:47] Chúng ta để Claude viết một script Python đơn giản để gọi chính các công cụ đó.
[00:12:52] Script này lấy kết quả tương tự, nhưng sẽ lọc nội dung rồi gửi lại cho mô hình, chỉ giữ phần liên quan nhất.
[00:13:02] Các công ty như Quora đã sử dụng tính năng này.
[00:13:04] Họ đã áp dụng với nội dung HTML để loại bỏ thông tin không liên quan, giữ lại phần cốt lõi và cải thiện hiệu suất model.
[00:13:13] Cuộc trò chuyện tiếp tục.
[00:13:17] Bạn có thể đã nghe Lisa và Jeremy chia sẻ về cách
[00:13:22] model hiện có thể thực hiện công việc tự động trong nhiều giờ.
[00:13:27] Tất nhiên, bạn sẽ sớm chạm ngưỡng context một triệu token.
[00:13:30] Compaction cho phép bạn duy trì cuộc hội thoại thay vì
[00:13:36] bị dừng đột ngột khi đầy context. Nó tóm tắt ngữ cảnh cùng prompt, chuyển
[00:13:47] xuống mức thấp hơn, loại bỏ các lượt không cần thiết, rồi tiếp tục. Lặp lại quy trình.
[00:13:54] Từ đó, bạn có cảm giác context gần như vô hạn, giữ model đúng hướng nhờ compaction. Hex đã áp dụng và
[00:14:04] đơn giản hóa code, đồng thời thấy model vẫn hoạt động hiệu quả.
[00:14:12] Tốt. Quay lại bản demo.
[00:14:14] Ben, ta có vài giải pháp context engineering.
[00:14:19] Dẫn dắt tiếp.
[00:14:21] Xem thử. Ngay đây, bạn thấy
[00:14:26] thanh context window ở bên trái
[00:14:31] tăng chậm hơn do giảm context mỗi lượt. Khi chạm 400k, ngay đây.
[00:14:40] Bạn thấy nó giảm xuống?
[00:14:42] Ta đã chạm ngưỡng.
[00:14:44] Đặt ở 400k. Sẽ giải thích sau.
[00:14:47] Sau đó nén bằng compaction.
[00:14:52] Hãy xem cách hoạt động, có thể dùng tool search?
[00:15:00] Tìm thấy một cái. Đúng rồi.
[00:15:03] Chúng ta cần chỉ số giữ chân người dùng.
[00:15:06] Đây là doanh nghiệp phân tích.
[00:15:08] Cần hiểu về tỷ lệ giữ chân.
[00:15:09] Nó gọi model để hỏi công cụ nào giúp lấy chỉ số đó.
[00:15:18] Có công cụ chỉ số giữ chân người dùng.
[00:15:21] Lưu ý: tool này 14.000 token, danh sách 6.100.
[00:15:30] Tool tiếp theo 9.300. Tool lớn là bình thường.
[00:15:36] Vì chưa đưa vào ngữ cảnh, các công cụ không cần thiết chiếm ít chỗ hơn. Thay vào đó, ta gọi: đây là chỉ số giữ chân, đúng rồi.
[00:15:45] Nếu xem transcript để tìm, này đây, tuyệt.
[00:15:48] Những gì bạn thấy ở đây là định nghĩa chính xác của công cụ đó, chỉ công cụ đó, không phần nào khác.
[00:15:54] Và tuyệt, giờ model có thể dùng công cụ cần thiết, để lại chỗ cho mọi thứ khác. Nào, ta có công cụ cần, tiếp theo khi nhận kết quả sẽ ra sao?
[00:16:05] Hãy xem, đúng đây, Gong là, nếu bạn chưa quen,
[00:16:10] đó là công cụ ghi lại cuộc hội thoại của đội bán hàng, để bạn xem dữ liệu, phân tích,
[00:16:16] xem phản ứng thị trường với sản phẩm mới, và những đứa trẻ ba tuổi này, tôi yêu chúng, nhưng chúng rất quan tâm đến quả bóng xanh khi ta gửi siêu anh hùng đến.
[00:16:27] Chúng nói liên tục ba mươi phút, thậm chí sáu mươi phút, thực ra không liên quan lắm khi xây dashboard này.
[00:16:34] Tôi không cần toàn bộ dữ liệu, chỉ cần cảm xúc chung, không khí về cách họ
[00:16:39] cảm nhận cuộc hội thoại. Với việc gọi công cụ theo lập trình, model đã tạo script nhỏ này, đầu tiên xem 2.500 ký tự đầu.
[00:16:52] Nó hiểu cấu trúc và nhận ra ta chỉ cần tổng hợp cảm xúc.
[00:16:57] Nó viết vòng lặp để lấy cảm xúc tổng hợp từ nhiều cuộc gọi, rồi streaming vào dashboard.
[00:17:04] Kết quả khổng lồ trước giờ giờ chỉ còn lại phần cần thiết cho tác vụ hiện tại.
[00:17:14] Một lần nữa, giữ ngữ cảnh hẹp.
[00:17:16] Đừng quên, phiên này không phải về demo ấn tượng.
[00:17:19] Có nhiều demo AI hay. Tôi cũng thích chúng.
[00:17:21] Nhưng cốt lõi là đưa nó vào production thực tế.
[00:17:26] Khi đó, bạn phải đảm bảo ngữ cảnh khớp với nhu cầu để sản phẩm thành công.
[00:17:33] Vậy là xong mục thứ hai.
[00:17:36] Hãy nói về mục thứ ba, đó là compaction.
[00:17:38] Chúng ta đã chạm ngưỡng 400k, giờ cần giảm xuống. Chúng tôi chọn 400k.
[00:17:46] Giờ tôi khởi chạy ngữ cảnh một triệu.
[00:17:48] Tôi rất thích ngữ cảnh một triệu. Có nhiều tình huống dùng nó rất hiệu quả.
[00:17:51] Với kịch bản của bạn, sự kết hợp tối ưu giữa trí tuệ, chi phí và độ trễ có thể không phải là một triệu.
[00:17:58] Hãy bắt đầu với 500k, 400k thường là điểm khởi đầu tốt, nhưng tùy thuộc vào model.
[00:18:03] Chúng tôi đặt ngưỡng đó rồi tạo bản tóm tắt.
[00:18:07] Bạn cần tự tạo prompt để hướng dẫn nó.
[00:18:11] Sau đó nó tổng hợp các sự kiện cần thiết để tóm tắt tình hình,
[00:18:16] giữ cuộc hội thoại đúng hướng mà không mất ngữ cảnh sai, rồi thêm vào đây. Tiếp theo, chuyển sang hội thoại.
[00:18:25] Vậy là chúng ta đã triển khai kỹ thuật ngữ cảnh.
[00:18:29] Với những ai để ý con số, chi phí giờ chỉ còn khoảng 11 bảng Anh.
[00:18:34] Chúng ta đã giảm được khoảng một phần ba so với trước đây.
[00:18:37] Nhưng tôi phải thú nhận một điều.
[00:18:41] Đây là một ngành kinh doanh đầy thử thách.
[00:18:45] Siêu anh hùng Cryothane làm nhiều việc khiến phí bảo hiểm tăng vọt, thật là khó khăn.
[00:18:54] Biên lợi nhuận rất mỏng, nên chúng ta cần giảm chi phí xuống.
[00:18:59] Mỗi lần tải dữ liệu này, chi phí là 11 bảng Anh.
[00:19:01] Con số khá cao. Và chúng ta đang dùng model nào?
[00:19:05] Chúng ta dùng Opus 4.7, model tốt nhưng thông minh nên đắt. Liệu có thể dùng SONnet và Haiku mà vẫn đạt trí tuệ gần bằng Opus không?
[00:19:19] Hãy quay lại slide để xem kết quả.
[00:19:23] Được rồi, chúng ta có Advisor Strategy. Tất nhiên tôi đã có giải pháp cho vấn đề đó.
[00:19:32] Ý tưởng của Advisor Strategy là bạn có model, agent chạy cùng executor là Sonnet hoặc Haiku.
[00:19:40] Và điểm mấu chốt ở đây là nó có thể
[00:19:45] tự xác định cách xử lý các hình dạng khác nhau, trừ khi gặp phải một hình dạng kỳ lạ như bạn sẽ thấy ngay sau.
[00:19:52] Khi đó nó không biết làm gì, sẽ gọi advisor để hỏi, rồi nhận được lời khuyên về cách xử lý.
[00:20:00] Điểm mấu chốt là nếu từng làm việc với đội phát triển, bạn sẽ thấy kỹ sư cấp cao cặp với kỹ sư cấp thấp giúp họ mạnh mẽ hơn nhiều.
[00:20:09] Kỹ sư cấp thấp vẫn là người trực tiếp làm việc, nhưng với sự hướng dẫn, cố vấn, rà soát code và hỗ trợ kiến trúc
[00:20:19] từ kỹ sư cấp cao, họ đạt được nhiều hơn đáng kể, đôi khi tiệm cận kết quả mà kỹ sư cấp cao làm một mình.
[00:20:30] Đó chính là ý tưởng tương tự. Logic này cũng áp dụng được cho các model.
[00:20:33] Việc cặp đôi Sonnet Haiku giúp chi phí giảm trong khi trí thông minh tiệm cận Opus, mang lại boost trí tuệ lớn.
[00:20:42] Và các công ty như Bolt đã áp dụng điều này.
[00:20:46] Họ đưa ra quyết định kiến trúc tốt hơn, thấy rõ trên tác vụ phức tạp thì
[00:20:51] hiệu năng được cải thiện, còn tác vụ đơn giản thì không tốn thêm chi phí, chỉ không gọi tool.
[00:20:59] Đây là sự đánh đổi rất hợp lý.
[00:21:01] Đó là cách tối ưu Pareto để cải thiện chi phí và hiệu năng trí tuệ.
[00:21:08] Hãy quay lại máy demo và cùng xem.
[00:21:13] Chúng ta hãy bắt tay vào triển khai ngay.
[00:21:18] Tốt, chúng ta bắt đầu ở mức khoảng 11 pounds, bạn sẽ thấy thanh này tăng chậm hơn nhiều.
[00:21:28] Tất nhiên, giờ chúng ta đang dùng Sonnet.
[00:21:29] Như bạn thấy, có Sonnet 4.6 với Opus 4.7 Advisor.
[00:21:33] Rõ ràng chi phí sẽ giảm.
[00:21:37] Chúng ta chuyển sang model giá rẻ hơn nhưng giá trị cao hơn.
[00:21:43] Câu hỏi không phải là chất lượng có tốt hơn không?
[00:21:49] Mà là chi phí có thấp hơn không?
[00:21:51] Chất lượng có tốt hơn không? Dashboard có mất đi trí thông minh không?
[00:21:57] Nếu cuộn qua, ta thấy hợp đồng khó khăn này cần phải chốt.
[00:22:05] Tôi không biết liệu có huy động vốn vòng sau không.
[00:22:07] Nếu không có hợp đồng này. Đó là gia hạn Metropolis.
[00:22:10] Metropolis là khách hàng lớn nhất từ đầu.
[00:22:15] Họ là nhà tài trợ lớn của Hero Corp.
[00:22:17] Tôi cần giữ họ ở lại. Sonnet đã xem transcript và cho rằng việc gia hạn đang trên đà thành công.
[00:22:25] Chúng ta làm rất tốt. Nhưng điều này quan trọng, nên hãy hỏi Opus.
[00:22:28] Đây là một trong những cách công cụ Advisor có thể được sử dụng.
[00:22:31] Bạn có thể gửi một bản transcript cho nó.
[00:22:33] Nó sẽ xem xét. Có gì sai sót không?
[00:22:36] Nó sẽ báo lại rằng bạn có thể đã bỏ sót điều gì đó hoặc mọi thứ đều ổn.
[00:22:40] Trong trường hợp này, Sonnet nói mọi thứ ổn, nhưng Opus xem xét kỹ lưỡng hơn.
[00:22:45] Nó tỉ mỉ hơn và có thể nói rằng thị trưởng thực sự muốn Cryothene.
[00:22:50] Người làm tăng phí bảo hiểm của tôi, đúng vậy, ông ấy đặc biệt muốn anh ta.
[00:22:53] Anh ấy quá xuất sắc để mất, tôi biết điều đó. Dù sao anh ấy rất giỏi, nhưng anh ấy không khả dụng vào ngày đó.
[00:23:02] Và thực tế, điều này là sai.
[00:23:07] Gia hạn sẽ thất bại nếu anh ấy vắng mặt trong sự kiện lớn tại Tòa thị chính. Đây gọi là dưa hấu.
[00:23:15] Bên ngoài xanh nhưng bên trong lại đỏ thẫm.
[00:23:17] Opus ghi đè lên Sonnet, thông báo và bắt lỗi.
[00:23:26] Vậy là tốt rồi. Tuyệt vời.
[00:23:28] Chúng ta đã khôi phục trí tuệ và đạt hiệu suất cao.
[00:23:32] Vậy, quay lại, điều gì xảy ra trên dashboard này?
[00:23:36] Chi phí ban đầu gấp hơn 10 lần, nhưng ta đã giảm xuống nhờ một prompt.
[00:23:42] Caching. Chúng ta thấy tỷ lệ hit là 0, đã triển khai, và cách tốt là dùng Cloud API skill trong Cloud Code.
[00:23:52] Nó giúp bạn xử lý nhiều logic.
[00:23:54] Chúng tôi đã xem transcript để hiểu rõ diễn biến, sau đó áp dụng context engineering: đầu tiên giảm công cụ gửi cho model.
[00:24:03] Thứ hai, chọn lọc dữ liệu từ kết quả gửi lại cho model. Cuối cùng, tạo ngữ cảnh gần như vô hạn nhờ compaction.
[00:24:13] Phần cuối là giảm chi phí hơn nữa nhưng vẫn giữ trí tuệ thông qua Advisor Tool.
[00:24:21] Vậy là chúng tôi đã làm hết những điều này.
[00:24:24] Opus đã cung cấp nút bấm trong kỷ nguyên AI agents, CEO. Giờ tôi chỉ cần bấm nút.
[00:24:32] Vậy chúng ta có nên lưu hợp đồng Metropolis không?
[00:24:35] Được chứ?
[00:24:36] Làm đi. Làm luôn đi.
[00:24:38] Hãy bấm nút, Metropolis đã được lưu.
[00:24:41] Chúng ta sẽ nhận vòng tiếp theo, tôi nghĩ, hy vọng vậy.
[00:24:44] Để xem nào. Nếu có VC ở đây, ta sẽ nói chuyện sau.
[00:24:48] Vậy ta quay lại slide nhé.
[00:24:51] Được rồi, các điểm chính cần ghi nhớ.
[00:24:54] Nhắc lại, hôm nay ta đã đề cập những gì?
[00:24:56] Đầu tiên là prompt caching.
[00:24:58] Nếu chỉ làm một việc, hãy tìm tỷ lệ hit rate của prompt cache và áp dụng ngay.
[00:25:03] Cloud API skill là cách tuyệt vời để bắt đầu.
[00:25:05] Tiếp theo là các phần context engineering.
[00:25:08] Ta đã chọn lọc dữ liệu gửi model từ công cụ và kết quả, rồi nén lại khi hội thoại phát triển.
[00:25:17] Cuối cùng là chiến lược advisor, cách Pareto optimal để tối ưu chi phí và trí tuệ.
[00:25:25] Một sự đánh đổi tuyệt vời.
[00:25:26] Tôi vừa nói về các tính năng ra mắt trong 24 giờ qua.
[00:25:32] Nền tảng Cloud đang phát triển rất nhanh.
[00:25:34] Rất vui vì bạn tham gia, nhưng hành trình học tập chưa kết thúc.
[00:25:38] Chúng tôi sẽ nỗ lực giúp bạn xây dựng không chỉ demo xuất sắc
[00:25:43] mà cả agent production thực tế, phục vụ bạn và khách hàng, tạo doanh nghiệp trên nền tảng này. Chúng tôi sẽ làm điều này liên tục.
[00:25:52] Đó là cam kết của chúng tôi. Điều này nghĩa là cập nhật mọi tính năng mới.
[00:25:57] Thú thật, slide này không đủ chỗ liệt kê mọi thứ ra mắt năm 2026.
[00:26:01] Đây chỉ là một phần nhỏ những gì đã ra mắt năm nay.
[00:26:05] Tôi đặc biệt hào hứng với automatic prompt caching, cách triển khai prompt caching chỉ bằng một dòng lệnh, hoặc Cloud Platform trên AWS.
[00:26:16] Đây là một nền tảng rất thú vị, nơi nhiều người trong phòng đang dùng model của chúng tôi trên AWS.
[00:26:23] Mọi thứ đều có sẵn ở đó.
[00:26:25] Đây là cách tuyệt vời để bắt đầu.
[00:26:29] Tôi rất háo hức xem các bạn xây dựng gì, cảm ơn đã đến tham dự.
