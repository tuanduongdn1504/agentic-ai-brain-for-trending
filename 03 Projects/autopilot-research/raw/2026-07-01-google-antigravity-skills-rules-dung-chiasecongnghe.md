---
source: yt-dlp (Path 5) — Vietnamese auto-caption (vi), tv/web_safari/mweb client to bypass timedtext 429
topic: google-antigravity-skills
generated: 2026-07-01T13:24:02.428805+07:00
video_id: UFmV7YsVqlM
video_url: https://www.youtube.com/watch?v=UFmV7YsVqlM
title: "Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z"
channel: "Dũng - Chia Sẻ Công Nghệ"
channel_subscribers: 1320
upload_date: 2026-06-27
duration_seconds: 1359
views: 1093
likes: 34
language: vi
category: Science & Technology
deliverable: report
compiled: 2026-07-01
---
<!-- compiled: 2026-07-01 → wiki/google-antigravity-skills/ (11 files) -->


# RAW — Google Antigravity 2.0: How to Create AI Skills, Rules & Manage Skills (A-Z)

> **Video:** [UFmV7YsVqlM](https://www.youtube.com/watch?v=UFmV7YsVqlM) — "Google Antigravity 2.0: Cách tạo Skill AI, Rule Và Quản Lý Skill Từ A-Z"
> **Channel:** Dũng - Chia Sẻ Công Nghệ (1,320 subs) — small Vietnamese tech channel
> **Uploaded:** 2026-06-27 · 22:39 · 1,093 views · 34 likes
> **Ingest:** Path 5 (yt-dlp). Vietnamese timedtext 429'd on default client; downloaded with `--extractor-args "youtube:player_client=tv,web_safari,mweb"` + json/vtt fallback. VTT deduped by `clean_vtt.py`.

## Video description (verbatim, with linked resources)

Google Antigravity 2.0 không chỉ là một bản nâng cấp mà là một nền tảng AI Agent hoàn toàn mới. Trong video này, mình sẽ hướng dẫn bạn từ A-Z cách tạo Skill AI, thiết lập Rule, quản lý Skill, cũng như cách kết hợp các thành phần này để xây dựng những AI Agent có thể tự động hóa công việc một cách hiệu quả.

**Linked resources from the description:**
- Sample skill files (Google Drive): https://drive.google.com/drive/folders/1wA_3Lqu9ghwwqLMN5E1ctK4F3k1VscXA?usp=sharing
- n8n + AI (auto-generate contract file from Lark data): https://www.youtube.com/watch?v=u2SZejNipDQ
- Demo: build n8n workflow with Antigravity: https://www.youtube.com/watch?v=9dl1OVSm4LU
- Build n8n workflow with Antigravity: https://youtu.be/kBcYiKOWJvQ
- Antigravity guide: https://www.youtube.com/watch?v=0JLqxr9_tYI
- Obsidian + Antigravity guide: https://www.youtube.com/watch?v=fhC_j6o8TNI
- Antigravity + NotebookLM guide: https://www.youtube.com/watch?v=Fu6pZblCmM0
- Google Stitch: https://www.youtube.com/watch?v=nHQHhYRwY2A
- OpenCode guide: https://www.youtube.com/watch?v=j359vqWGSMo
- OpenClaw guide: https://www.youtube.com/watch?v=mZTxYxOhHBs

---

## Cleaned Vietnamese transcript (auto-caption, deduped)

> ⚠️ Auto-caption — garbles technical terms. Notable garbles the compiler must interpret against official docs, NOT transcribe literally:
> - "Asian triệt skill" / "giặt ngang skill" = the on-disk skill path (creator spoke an English path; **official docs = `.agent/skills/`**, NOT `.antigravity/skills`)
> - "titon" = Python · "power sell / Power Boy" = PowerShell · "ru / RU / rồi" = Rule · "CRW" = Rule · "agent ch mas down / agent.mdown" = agents.md / AGENTS.md · "chác/chát" = chat · "prom/brom/Rom" = prompt · "Facebook / facew" = the report file (garble) · "super skill" = "use the skill"

Bạn có bao giờ hướng dẫn cho một nhân
viên mới mà phải đứng kế bên hướng dẫn
từng ly từng tí như là lấy cái file này
đập vào file kia à chỉnh lại phông chữ
tính biểu đồ vân vân ngày nào cũng nói
bấy nhiêu đó thì anh chị có cảm thấy mệt
không ạ? Dùng ai bây giờ cũng y chang
như vậy. Mỗi lần nhờ nó làm một cái gì
thì cũng phải viết một cái brom dài dàng
giặt để giải thích những cái vấn đề mà
mình cần truyền tải đến cho nó quá oải
và tốn rất nhiều thời gian. Vậy tại sao
bạn không hướng dẫn cho nó một lần duy
nhất? Hôm nay mình sẽ hướng dẫn cho các
bạn cách tạo kỹ năng cho con v này vĩnh
viễn ở trên máy tích của các bạn. Bạn
hãy tưởng tượng như thế này nha. Chúng
ta sẽ nhân bạn chúng ta lên và cái người
nhân bạn đó sẽ biết được các cái kỹ
năng, các cái kiến thức như chúng ta
vậy. Và cái người nhân bạn đó sẽ làm
việc thay thế cho chúng ta. Đó chúng đó
gọi là cách tạo ra các cái skill để mà
để con AI nó sẽ làm việc cho chúng ta.
Video này sẽ không cần chúng ta biết cái
kiến thức về lập trình và khi các bạn
xem xong video này thì các bạn có thể
làm được và tạo ra một cái skill riêng
dành cho mình. Vậy chúng ta sẽ đi vào
phần thứ nhất của video này, đó chính là
tổng quan về skill trên antigravity 2.0.
Skill trên antigravity 2.0 là gì? Cực kỳ
đơn giản, thực chất nó chỉ là một cái
file thư mục nằm trong cái dự án à bên
bên dưới cái đường dẫn là Asian triệt
skill. Trong thư mục này chỉ có hai cái
thành phần quan trọng nhất đó chính là
skill và một cái thư mục đó là script.
Chứa các cái đoạn cố thực thì các cái
titon như titon hay là các cái power
sell. Điểm vi diệu của antigravity 2.0
đó chính là cơ chế auto discovery. Nghĩa
là khi bạn ra lệnh các cái nó sẽ quét
toàn bộ các cái thư mục skill của bạn để
xem cái skill nào khớp với cái mô tả nào
và nó sẽ tự động kích hoạt các cái skill
đó.
&gt;&gt; Ê việc của tao.
&gt;&gt; Thay vì [âm nhạc] chúng ta phải gọi lên
bằng thủ công. Nhiều bạn sẽ hỏi rằng tạo
cái skill ở thư mục này thì có dùng được
cái skill ở các thư mục khác không? Câu
trả lời là có. Vì sao? Vì thứ nhất ở
trong Antigravity chúng ta có thể phân
thư mục theo kiểu là workspace có nghĩa
là bạn có thể tạo skill theo từng dự án.
Hãy tưởng tượng bạn có hai ngôi nhà nằm
cạnh nhau. Workspace skill giống như máy
hút bụi được mua bằng tiền riêng. Agent
A ở nhà A xài thoải mái, còn Agent B ở B
không thể nào chạm tới được.
&gt;&gt; Nhưng nếu các bạn muốn dùng một skill
trên toàn bộ tất cả các cái file thư mục
của mình thì các bạn có thể bỏ vào trong
Antigravity ở cái mục là Global Skill.
Global Skill giống như cây đèn đường
được dựng ở khu vực công cộng giữa hai
nhà. Asian A và Asian B đều dùng được.
&gt;&gt; Ở đây có một điểm cực kỳ hay mà mọi
người hay nhậm lẫn đó là sự khác nhau
giữa skill và skill là gì? Skill đó
chính là các cái kỹ năng. Mình sẽ lấy
ngay một cái ví dụ thực tế như sau. Nếu
bạn làm một cái báo cáo Excel input đầu
vào bạn sẽ đưa cái file Excel đó cho nó.
Và skill là gì? Skill ở đây nó sẽ làm
báo cáo, xử lý số liệu các cái file liên
quan, bảo vệ các cái biểu đồ vân vân.
Còn CRW ở đây chúng ta sẽ đặt một cái
lệnh đó chính là không được cho phép
ngày dài xóa đi các cái dữ liệu gấp mà
chỉ cho phép nó tạo thêm một cái ship
mới là cái phần báo cáo và nếu đưa quy
tắc này vào skill thì chúng ta sẽ làm
rất nhiều skill và chúng ta sẽ à bổ sung
gáp lập đi lặp lại cái skill liên tục
thay vì đó thì chúng ta sẽ đưa vào cái
ru để cho các cái skill nó sẽ đọc cái ru
này và ở trong một dự án có thể là ba
đến bốn đến năm cái skill nhưng mà chỉ
có một cái ru duy Cho nên là ai nó sẽ tự
động nghe cái lệnh của RU đó và các
skill nó sẽ hoạt động ở phía là nhiệm vụ
chuyên môn. Để quản lý các cái skill vào
RU này thì ở trên màn hình Antigravity
các bạn bấm vào cái nút setting và chọn
vào cái customization trong đó sẽ hiển
thị các cái rule và các cái skill nằm ở
trong bảng này. Bây giờ chúng ta sẽ qua
phần thứ hai. Cách xây dựng skill như
thế nào? Ở đây sẽ có hai cách. Cách thứ
nhất đó chính là xây dựng theo thủ công.
Thủ công ở đây có nghĩa là gì? Chúng ta
sẽ vào từng thư mục của skill. từ thư
mục của project của mình để tạo ra các
cái skill. Ngay từ đầu mình có nói các
cái thư mục đó nó sẽ đi theo cái đường
dưng là giặt ngang skill. Ở trong cái
file skill đó thì mình sẽ điền các cái
thông tin liên quan tới các cái chuyên
môn của từng cái project. Ở đây mình
đang ví dụ một cái project về báo cáo
Excel ờ phân tích dữ liệu trong Excel.
Thì trong cái skill đó thì mình sẽ viết
những cái skill liên quan tới các cái
kiến thức. Ví dụ khi mình đưa cái input
đầu vào là file sale doanh số tháng 5
thì trong skill đó nó sẽ mình sẽ ghi là
phải phân tích được dữ liệu à tháng đó à
doanh số rồi phải vẽ biểu đồ. Ví dụ mình
ví dụ ba cái như vậy rồi sau này thì khi
đưa cái doanh số dữ liệu vào thì nó sẽ
tự động phân tích vẽ biểu đồ cho mình
toàn bộ từ a đến z cái ru cũng vậy các
bạn cũng có thể tự động tạo ra cho mình
một cái action và cái ru chúng ta sẽ
điền vào. Nhưng mình sẽ tạo cách phần
thứ hai rất nhanh và ai cũng làm được.
Cách này không cần bạn phải trực tiếp
vào trong thư mục mà mình làm trên con
anti antigravity 2.0 trên cái project
đó. Thứ nhất là các bạn đưa dữ liệu vào
và chúng ta sẽ làm việc với con ngày
hai. Chúng ta sẽ chỉnh sửa toàn bộ,
chúng ta sẽ nói nó làm báo cáo rồi xử lý
dữ liệu, rồi làm abc tất cả mọi thứ. Sau
đó chúng ta sẽ nói con antiravity rằng
tôi muốn tạo một cái skill bao gồm những
cái gì tôi đã làm việc với bạn trước đó.
Thì cái con antigravity nó sẽ tự động
tạo cái skill cho mình. Và ru cũng như
vậy. Nó cũng sẽ tạo những cái ru cho
mình hết toàn bộ mọi thứ và nó sẽ tự
động lưu tr các folder. Đây là cách
nhanh nhất mà mình cảm thấy rất là hay
có thể áp dụng cho tất cả mọi người làm.
Đây là toàn bộ các cái skill về các cái
file bảo cáo Excel. Thì cái những cái
skill liên quan tới các cái nghiệp vụ
văn phòng đó là một trong những cái
skill cực kỳ nhỏ. Các bạn cũng có thể
làm một những cái skill riêng về à lập
video, làm cái kịch bản rồi à viết
email. Ví dụ giả sử các bạn công ty các
bạn là có hai đối tượng khách hàng,
khách hàng nước ngoài và khách hàng
trong nước. Thì cái đối tượng khách hàng
nước ngoài các bạn sẽ có những cái phong
chữ, cái sai chữ nó khác hẳn với phong
chữ và sai chữ của khách Việt Nam. Thì
câu chuyện ở đây khi các bạn muốn viết
một email cho khách nước ngoài thì các
bạn chỉ cần nói một câu lệnh thôi. Đó
chính là tôi bây giờ tôi cần gửi một
email cho khách nước ngoài thì con skill
này nó sẽ tự động tìm đến cái skill mà
chúng ta đã viết trước đó là nó sẽ sử
dụng các cái phông chữ, các cái size
chữ, các cái format mà mình đã đặt ngay
từ đầu. Và khách trong nước cũng vậy. Và
đấy gọi là skill. Giới thiệu thì dài vậy
thôi nhưng khi làm thì nó sẽ rất là đơn
giản. Thì bây giờ mình sẽ demo cho các
bạn xem một đoạn ngắn cho các bạn biết
là cái cách tạo skill và ru sẽ như thế
nào. Tự tạo skill là cái cách tốt nhất
để cho chúng ta hướng dẫn cái con AI này
trở thành một cái trợ lý đắc lực của
mình. Thay vì chỉ cần chác qua chát lại
với nhau, mình sẽ à ném một cái file
skill và ru vào trong một cái folder để
cho các bạn muốn tham khảo ở trên driver
đặt cái dĩ phần mô tả này. Để đăng ký
kênh các bạn có thể bấm vào nút like,
share hoặc subscribe ở cái video này ấy.
Và nếu các bạn có thêm cái những cái ý
kiến về AI agent tạo skill có thể
comment ở dưới này để mình có thể học
hỏi thêm. Xin cảm ơn.
&gt;&gt; Let's go. Các bạn cách để tạo ra các cái
skill hoặc là các cái room. Ở đây mình
sẽ lấy một cái ví dụ giống như là đây là
cái doanh thu tháng 5 và tháng sáu. Cái
doanh thu tháng 5 bây giờ là hiện tại nó
sẽ có cái một cái bảng à tự như thế này.
Đây là một cái bảng file Excel cùng các
bạn có thể là à định dạng cái file này
có thể là tải từ các cái phần mềm xuống
để cho chúng ta có một cái bảng à chi
tiết về cái khách hàng. Ở đây là à khách
hàng tháng năm mình làm demo thôi. Thì
trong này sẽ có các cái họ tên sản phẩm,
số tiền rồi đã thu, chưa thu rồi trạng
thái thanh toán rồi các cái tỉnh thành.
Thì bây giờ mình tạo skill như thế nào?
Ok thì bây giờ mình sẽ à ở đây là cái
con antigravity của mình mình sẽ hướng
dẫn cho nó à làm việc với cái file này.
Bây giờ mình sẽ gõi là à hãy tạ à hãy
phân tích
dữ liệu doanh thu
tháng 5. Doanh thu tháng năm nha.
Ở đây là vì sao nó lại đọc được cái à
doanh thu tháng năm của mình? Vì thứ
nhất là mình đã à bỏ cái phần à cái
folder doanh số và trong cái thư folder
doanh số này mình đã bỏ cái phần thư mục
hai cái thư mục ở đây thì ở trên này các
bạn thấy là trong thư mục hiện tại của
mình ở phố đĩa D này project antigravity
và doanh số thì nó đã có các cái thư mục
doanh số và trong thục doanh số nó sẽ có
hai cái phần hai cái file tháng 5 tháng
sau thì bây giờ mình sẽ à lọc cái dữ
liệu tháng năm trước rồi à các bạn sẽ
xem à cái quá trình mình làm và cái cách
để mình tạo skill à bây giờ là phân tích
dữ hiệu danh phần năm này mình sẽ gõ vào
đây.
Thông thường các bạn khi làm việc với
chá GPT hoặc là Germin à cái kiểu mà
chúng ta chá qua chá về thì chúng ta
cũng có thể à cái bước đầu là cũng sẽ
như thế này. Chúng ta có đưa cái dữ liệu
của mình vào để cho nó đọc dữ liệu và
mình bắt nó để phải phân tích các cái à
dữ liệu. Thì à không ở ở đây cái câu
chuyện là mình sẽ tạo skill sau này là
mình sẽ à không có nói gì quá nhiều hết.
Đấy, ví dụ các bạn sẽ sử dụng các cái
prom để mà gọi là nhắn tin với nó là bây
giờ là cần lọc ra số liệu của khách hàng
này rồi. Ai là cái người gọi là đã thanh
toán rồi chưa thanh toán bao nhiêu tỷ lệ
người mua ở tỉnh thành nào là nhiều ấy.
Loại khách hàng đại lý hay khách hàng cá
nhân nó sẽ nhiều. Đây thì các bạn thấy
là nó cũng lọc ra y như rằng là cũng
giống như cái à cái chắ GVT vậy các bạn
thấy này. Đấy đúng không?
nó cũng phân ra được khách hàng cũng
công nợ. Đấy, hai nói chung lại là nó
giống nhau. Nhưng cái điểm khác biệt ở
đây á là mình sẽ tạo ra một cái cái
skill để làm gì? Để sau này mình khỏi
cái phải hỏi quá nhiều cái vấn đề này
nữa. Bây giờ mình sẽ à thử tạo ra một
skill nha. Ở đây mình sẽ có một cái prom
sẵn đầu tiên. Mình chỉ cần làm cái việc
này một lần thôi. Mình sẽ điền vào đây.
Ở đây bây giờ là mình sẽ có à một số cái
công việc này mình sẽ hỗ trợ nó này là
sẽ lọc ra các cái danh sách khách hàng
đã thanh toán và chưa thanh toán này.
Tổng hợp số liệu doanh thu à công nợ
này. Lọc ra các cái phần trăm khách hàng
tỉnh nào là mua nhiều nhất này. Lọc ra
các cái xả bộ sản phẩm nào là doanh số
nhiều nhất này. Đấy phân loại ra khách
hàng đại lý lễ này. Ở đây á thì mình sẽ
làm thêm một cái nữa là à ok thì tạm
thời như vậy kì đã phân tích ra số liệu
báo cáo
cho giám đốc à báo cáo lại cho giám đốc
facew Facebook file pdf gì cũng được và
à hãy tạo skill
ừ cho cái quy trình này luôn nha.
Bây bây giờ là mình sẽ không có à tạo
thủ công à ở trước đó thì mình đã có
hướng dẫn cho các bạn hai cách. Cách thứ
nhất là chúng ta sẽ tạo tay và thứ hai
là chúng ta sẽ à à qua qua quá trình làm
việc thì mình sẽ bảo với nó là bộ skill
này. Rồi ok mình sẽ bấm vào đây.
Đấy và sau khi tạo skill xong thì sau
này các bạn sẽ không có viết lại cái
đoạn này nữa. Đấy chúng ta sẽ có những
nhiều rất nhiều câu hỏi và chúng ta sẽ à
click ra các cái câu hỏi này. Và khi mà
chúng ta click xong cái câu hỏi này xong
thì chúng ta sẽ tạo bộ skill và sau này
mình sẽ nói với nó. Tí nữa mình sẽ phân
tích cái doanh thu tháng sáu mà sẽ không
cần lọc lại những cái câu hỏi này nữa.
Đấy, đây là những câu hỏi mình đã lên
sẵn rồi. Còn trong quá trình các bạn
làm, các bạn cũng có thể có hỏi từng câu
hỏi khác nhau ấy và hỏi ở cái này như
thế nào, cái kia ra như thế nào và chúng
ta sẽ làm ra sao thì cũng sẽ hỏi rất là
nhiều. Nhưng bây giờ à khi mà chúng ta
nén cái bộ skill lại thì sau này là nó
đi theo cái bộ skill và bộ quy trình đó.
Tí nữa mình sẽ cho các bạn xem cái bộ
skill nó sẽ như thế nào. Ở đây nó có lên
một cái plan cho mình này là à kế hoạch
trước khai và báo cáo doanh thu và thiết
lập skill quy trình này. Ở đây là kế
hoạch mục tiêu này, phân loại khách hàng
này, tổng hợp số liệu này, phân tích
này. Cái này ok chưa? Tạo skill này. Đây
là một định dạng skill à tự động hóa quy
trình phân tích file Excel này.
Đề xuất thay đổi này. Tạo lệnh. Rồi mấy
cái này thì thực ra là các bạn đọc để
mình định nghĩa skill này. Nội dung
skill này là như thế nào này.
Ok.
Bây giờ mình sẽ à báo với nó là triển
khai nha.
Ok. Sau khi xảy xong thì nó sẽ thông báo
lại cho mình này. Cái báo cáo Facebook
gửi cho giám đốc này là báo cáo ở đây
này được định dạng bởi chuyên nghiệp
này. Tự động tạo skill này. Bây giờ mình
sẽ à đi vào từng cái một nha. Thứ nhất
là mình sẽ đi vào cái phần báo cáo.
Trong cái file này này nó đã tự động báo
cho mình một cái báo cáo. Báo cáo ở đây
mình sẽ xem cái báo cáo như thế nào.
Rồi báo cáo nó sẽ kiểu như thế này. À
tổng quan số liệu tháng 5 2016 này. Đấy
thay vì chúng ta phải ngồi đếm ngồi đếm
cái cái ông phải sale đó thì bây giờ nó
sẽ tự động tách ra cho mình luôn. Đấy
doanh thu rồi công nợ phân tích các cái
phân cục khách hàng. Số liệu nó sẽ đối
chiếu từ cái bên kia qua.
Rồi tiếp theo là các cái biểu đồ so sánh
doanh thu, công nợ thực thu. Ở dưới này
là phân tục theo tỉnh thành này 36 triệu
này. Hà Nội, Thanh Hóa này. Rồi tức là
có nghĩa là trong quá trình tạo sức
chiêu nó sẽ xảy ra một số lỗi. Mình sẽ
mình sẽ phải kiểm tra lại hết toàn bộ
các cái cấu trúc của các cái à cái phần
này. Ở đây này công n0. Có thử mình xem
Hà Nội ở phía công Hà Nội công nợ có
không. Những khách hàng nào ở Hà Nội
không nè.
À đúng rồi. Hà Nội là không có à Thanh
Hóa cũng không có.
Đây. Ok. Và đây nó cũng có một cái bảng
và khi mà chúng ta cảm thấy nó làm đúng
rồi thì cái skill nó của nó đã đúng rồi.
Trong trường hợp cái dữ liệu nó sai có
nghĩa là sai sót của AI nó sẽ có chứ
không phải là không. Nhưng mà cái câu
chuyện mình sẽ tạo ra một cái skill
để làm gì? để thứ nhất là để cho nó đi
theo cái skill đó và nó sẽ làm việc.
Đấy, nếu trong này có cái sai số sai,
chứng tỏ skill mình đang bị sai và mình
sẽ dạy con ai thông qua con antigraffiti
này để cho nó đúng. Và khi mà dữ liệu nó
đúng thì skill nó bắt đầu chính xác. Thì
skill chính xác thì bắt đầu sau này
chúng ta đưa dữ liệu vào thì nó sẽ tùy
tô theo một cái dữ liệu như vậy. Rồi
tiếp theo đó là cái file báo cáo. File
thứ hai đó chính là cái à skill. À trước
đó mình có nói là cái skill nó sẽ nằm
trong một cái thư mục. Trong cái thư mục
nó sẽ có một cái mục skill. Đấy và trong
này sẽ có cái mục skill. Md thì ở đây á
là các bạn thấy là mình sẽ mở cái file
skill cho các bạn thấy anti gravity nó
sẽ đọc được cái file m down nha nhưng mà
nó sẽ nó không đọc được cái file doc
này. Cho nên là hai cái định dạng hai
cái chữ khác nhau.
Ở đây là sẽ có cái à tên này. Quy trình
phân tích báo cáo này. Đây đây đây là
skill của của mình nha. Quy trình hướng
dẫn phân tích này, yêu cầu hệ thống này.
Đó, xử lý dữ liệu này, đọc ghi đề file
Excel này. À vải biểu đồ trực quang này,
đọc và định dạng Facebook này. Cài đặt
các thư viện này. Đó.
Ok. Các bạn đọc ở đây. Biên x bộ cục
định dạng này. Sau này các bạn cũng có
thể là ừ điền chèn ở đây là à trang tiêu
đề kiểu như là phải là thẻ H1, H2 rồi
phông chữ là phải à robato hoặc là à tha
neoman. Rồi là những cái cấu trúc như
thế nào để đó cho nó đẹp. Đấy thì mình
đây mình đây mình làm demo thôi cho nên
là mình sẽ làm kiểu như thế này. Hoặc
các bạn có những cái file sẵn ở của công
ty của các bạn đấy. Các bạn cho nó đọc
cái file đó và yêu cầu nó là sau này
phải xuất ra đúng cái file đó cho mình.
Đó. Ok. Chúng đây. Ở đây có cái phân
tích cái mẫu. Các bạn chỉ cần đưa cái
file mẫu thôi. Đấy. Đ theo cái bổ cục
của công ty của mình.
Rồi một chỗ nữa đấy chính là cái à khi
các bạn gõ núc xyệt ở đây là các bạn
thấy nó có skill của các bạn ở đây. Đấy
và gọi lên skill ra. Đấy sau này các bạn
không cần phải gõ l
hiểu được cái bản chất của nó thôi. Sau
này à có một số bạn họ sẽ hỏi mình là à
khi mà chúng ta gọi như vậy thì nó sẽ
làm sao biết được là cái skill nào là
skill nào? Thực chất AI nó rất là thông
minh. Nó dựa vào cái cái mô tả của mình
và nó sẽ biết được cái mình đang dùng
skill nào. Cái đó là các bạn khỏi cần
phải lo lắng nha. Rồi tiếp theo là cái
ru bây giờ đó mình tạo skill xong rồi
thì bắt buộc mình phải tạo thêm một cái
cái ru nữa. Rồi ok thì mình sẽ tạo một
cái ru ở đây.
Rồi
khi thực hiện các cái thao tác này, phân
tích này, báo cáo doanh thu Excel này,
tuyệt đối không được tự ý xóa chỉnh sửa
hoặc ghi đè lên xích dữ liệu thô. Có
nghĩa là mình sẽ không muốn ừ không muốn
không muốn cái con AI ai á nó sẽ xóa hay
là chỉnh sửa hoặc là ghi những cái gì
lên cái dữ thệu liệu thô của mình cả. Dữ
liệu thô là dữ liệu chính xác nhất và
mình không muốn thay đổi cái gì đó. Nếu
mà các bạn không đưa ra thì có thể ngay
từ đầu các bạn có thể là không bị ghi
sửa xóa nhưng mà ai mà nó đôi lúc mà nó
vào nó chỉnh sửa tầm b một con số thôi
nó nó sẽ là một cái à rất rất rất là
nguy hiểm đối với cái tình hình à cái
cái tài chính của công ty. Đó thì bắt
đầu là mình phải dặn con ai này là sẽ
không giữ thiệu thô là phải đảm bảo 100%
là sẽ không được chỉnh sửa hoặc là xóa.
Rồi ok tiếp theo
cái này thì không cần này. Rồi dư
ok mình thấy là chỉ cần cái cái đó là
được. Ok. Rồi thì bây giờ mình sẽ nói
với nó là bây giờ mình muốn tạo cái rồi
và đây là một cái rule mà giống như sau
này các bạn có à tạo đây là file Excel.
File Excel là à quản lý báo cáo. Ừ rồi à
tạo biểu đồ. Nhưng mà sau này các bạn có
thể là không tạo Excel nữa mà chúng ta
sẽ tạo một skill của Power Boy hoặc là
skill định dạng Facebook hoặc là skill
về phân tích các cái dữ liệu nghiên cứu
thì ở đây á cái RU này nó sẽ chạy hết
toàn bộ luôn. nó sẽ không phân biệt cái
chạy skill nào hoặc là đây có nghĩa là
chúng ta sẽ à cái ru này nó sẽ chạy hết
cho toàn bộ các cái skill nằm trong cái
bảng doanh số này. Đây nếu mà ra khỏi
cái bảng doanh số hoặc là nằm qua cái
bảng kịch bản này thì nó lại không có
nữa. Cho nên là à cái một cái ru có thể
là đảm nhận à nhiều cái quy tắc của của
b các skill khác nhau. Thì đây là à các
bạn có thể là đi làm skill hoặc làm ru
cho từng cái project khác nhau. Các bạn
thấy là project của mình là có project
danh số này.
project của à la này. Đấy thì ở đây nếu
các bạn muốn làm một skill hoặc là một
cái ru cho toàn thể luôn thì các bạn có
thể là làm ở cái global skill nó sẽ một
cái quy ước nó sẽ áp dụng cho toàn bộ
các project. Ok thì bây giờ à các cái rã
đã hình thành rồi. Từ này các cái agent
nó sẽ à tung thuộc nghiêm ngắc các cái
tuyệt đối, các cái không chỉnh sửa này
hoặc ghi đề trên dữ thiệu thô này. Đấy
và à cho nó ghi đề đi. Nếu mà sau này
các bạn có muốn ghi đề thì đương nhiên
cái câu chuyện mình sẽ bảo với nó là khi
nào mình muốn ghi đề dữ liệu thì phải
hỏi lại mình và có mình xác nhận là ok
thì nó mới làm được. Rồi tiếp theo nha
mình sẽ vào cái phần à
cái đây
cái agent ch mas down này là chính là
cái cái ru của mình đây. Và sau này các
bạn cứ vừa làm vừa bổ sung vừa làm vừa
bổ sung. Cho nên là à cái này là cái quy
trình nhân bản nhân bản thân mình ra
thành một người thứ hai. Và cái con này
nó sẽ làm theo đúng cái quy trình của
mình đưa ra. Rồi ok bây giờ mình sẽ thử
cái à doanh số tháng năm nha. Mình sẽ
thử cái doanh số tháng năm.
À tháng n xong rồi mình sẽ giữ gửi doanh
số tháng 6. Rồi bây giờ à bạn hãy phân
tích doanh số tháng 6
theo skill giúp mình.
Đấy.
Ok.
Ok. Thì bây giờ nó sẽ à phân tích lại
cái doanh số tháng sáu dựa vào cái skill
mà à nó đã làm sẵn cho mình. coi thử nó
sẽ làm ra giống không ta. Ok thì bây giờ
là cái file skill à cái file doanh số
tậng sáu đã xà hoàn tất và ở đây mình
không sẽ không cần làm gì nhiều mình chỉ
cần là à hãy doanh số tháng sáu super
skill cho mình và nó sẽ tự động làm theo
các skill đấy các cái tệp mới nhất các
cái doanh thu định dạng nguyên nghiệp
chuyên nghiệp rồi một số điểm à nhấn
trong tháng sáu rồi ok bây giờ mình sẽ à
vào đây đấy cái file đây là file bảng
cáo tháng sáu này tháng 5 vừa rồi này
tháng sáu mình sẽ bật tháng sáu lên nha
rồi trong cái tháng sáu này á nó sẽ có
cái bảng à phân tích tỉ lệ thu hồi dòng
tiền ABC rồi khách hàng đại lý đó các
biểu đồ rồi phân tích tiến hành theo
tỉnh nó giống cái hồi nãy thì ờ thì cái
câu chuyện bây giờ là nó sẽ đi theo cái
mô tip mà mình đã à đưa ra cho nó rồi à
vì à mình sẽ xin nhắc lại một lần nữa đó
đó chính là vì sao là chọn skill nếu các
bạn không dùng skill thì ai mỗi lần phân
tích nó sẽ ra một cái bảng khác nhau
hoặc các bạn sẽ đưa ra các cái Rom rất
là dài và lần nào cũng làm như vậy thì
nó sẽ rất mất thời gian cho các bạn và
không phải khi nào cái prom của mình
cũng là giống y chang nhau đấy và mỗi
lần phân tích nó sẽ nó sẽ khác nhau hoàn
toàn. Bây giờ mình phải tạo ra một cái
con skill để mà nó đi theo cái skill và
các cái quy trình làm việc đó để cho
mình. Và khi mà à chúng ta đưa cái bảng
doanh số vào hoặc là bản những cái bảng
file Power Boy vào thiết kế ra một cái
Power Boy cực kỳ đẹp theo cái mẫu này
thì chúng ta sẽ cần bổ sung các cái
thông tin vào và nó sẽ tạo ra cái Power
Boy đúng như ý muốn. Và doanh số này
cũng vậy. Đấy và cái doanh số này khi mà
đưa vào thì nó cũng y chàng như là cái
mà mình đã phân tích trước đó. Đây các
bạn thấy là khi mà mình mới tạo cái đầu
tiên thì bây giờ là mình nói bây giờ
phân tích tranh thủ số thủ tháng sáu này
chỉ cần gõ một lần thôi và nó sẽ ra một
cái file như thế này cho chúng ta và à
cái ru ở đây là nó sẽ không bao giờ sổ
sổ chỉnh sửa hoặc xóa đi cái à danh cái
Facebook cả. Rồi ok mình sẽ hướng dẫn
cho các bạn mở cái mở cái xem cái à
skill và cái ru đó ở đâu nha. Các bạn
bấm vào nút setting cho mình. Rồi ở đây
các bạn sẽ thấy là à ở đây là sẽ có cái
ru này, skill này,
là cái này là mình sẽ không nói nha. Cái
này là mình đã trước đó mình cài đặt
rồi. Mình sẽ chủ yếu là cái ru với cái
skill ấy. Ru ở đây là sẽ có hai cái là
cái user global và cái agent. Cái
agent.mdown này là cái vừa rồi mình mới
tạo. Còn skill ở đây là skill à báo cáo
vừa rồi mà mình mới làm xong.
Ok thì chúng ta sẽ kiểm tra kiểm soát ở
đây. Các bạn thấy ở đây là cũng có cái
quy tắc ru này. Đấy.
Ok. Thì cái hướng dẫn của mình là sẽ như
vậy. Tuy nói th hơi dài nhưng mà cái
triển khai nó rất là nhanh và các bạn có
thể tạo ra hàng trăm cái skill. Những
cái kiến thức của mình mình sẽ đưa vào
đây hết. Và khi bạn nghĩ là mình nhân
bản con người mình ra thì bây giờ hiệu
suất của các bạn làm tầm khoảng rơi vào
khoảng à 80% 100%. Bây giờ các bạn có
thể nhân bản cái cái cái hiệu suất cái
công việc của mình ra thì các bạn sẽ
thấy được là cái công việc của mình nó
làm rất là nhanh. Rồi ok thì cái video
đến đây là hướng dẫn mình đã làm xong.
Cảm ơn bạn nhiều.
