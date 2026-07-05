---
source: manual yt-dlp + GitHub raw (Path 5)
topic: miai-cv-matching-agent
generated: 2026-07-05
video: https://www.youtube.com/watch?v=7gIwR5SwM_0
video_title: "Xây dựng CV Matching AI Agent, tự động tìm việc phù hợp - Mì AI"
channel: Mì AI (~52,000 subs per yt-dlp channel_follower_count)
upload_date: 2026-07-04
duration: 43:59
views_at_fetch: 519
repo: https://github.com/thangnch/MiAI_CV_Matching_AI_Agent
repo_created: 2026-07-03T16:03:25Z
repo_license: NONE
deliverable: report
---

# Mì AI — CV Matching AI Agent (video 7gIwR5SwM_0) — raw source bundle

Operator-submitted first-party video (2026-07-05 session). Vietnamese auto-subs pulled via
`yt-dlp --write-auto-subs --sub-langs vi`, deduped VTT → plain text (~35.4K chars), **read in full
in the main loop**. All 8 repo files pulled from `raw.githubusercontent.com` at `main`
(one day older than the video), **read in full in the main loop**. Deep-dive + refute-first
verification: Workflow `wf_dd724957-cac`.

## Video description (yt-dlp)

> 🎯 Upload CV một lần, AI tự tìm những công việc phù hợp nhất cho bạn!
> Xây dựng một CV Matching AI Agent – hệ thống AI có khả năng đọc CV, phân tích kỹ năng và tự động
> so khớp với hàng nghìn tin tuyển dụng. Nội dung: AI đọc và phân tích CV bằng LLM; chuyển CV và JD
> thành Embedding, tìm kiếm bằng Vector Database; xếp hạng và gợi ý công việc; AI Agent phân tích,
> đánh giá, đưa lời khuyên; demo toàn bộ quy trình.
> Link github repo: https://github.com/thangnch/MiAI_CV_Matching_AI_Agent

---

## Full deduplicated Vietnamese transcript (auto-subs)

Hello anh em, chào mừng anh em quay lại với MaiI. Và hôm nay thì chúng ta sẽ cùng nhau từng bước từng bước xây dựng một con AI agent để làm công việc là CV matching. Có nghĩa là tự động tìm hiểu cái GD, cái mô tả công việc, phân tích cái CV của chúng ta. Sau đó thì xếp hạng là à công việc nào thì phù hợp nhất với chúng ta, công việc nào không phù hợp và recommend 
chúng ta những cái bước chúng ta có thể improve cái CV của chúng ta nha. Let's go anh em. &gt;&gt; [âm nhạc] &gt;&gt; Rồi thì à trước khi bắt đầu ấy thì mình cũng nói trước đây là một cái chủ đề khá là rộng. Nó rộng ở cái chỗ vì sao? Làm láp thì rất dễ nhưng à làm mà chạy được thì sẽ rất là khó và sẽ phải xử lý rất nhiều tác vụ. Đó. Thế nên trong cái bài này ấ là mình chỉ muốn anh 
em tập trung vào làm đó. Vì sao lại làm? Để chúng ta có cái mindset về một cái hệ thống, chúng ta có mindset về agent, chúng ta có cái mindset về ghép nối các cái thứ khác nhau vào để thành một cái chương trình mà chạy được. Đó. Thế còn lại anh em hoàn toàn mình sẽ chia sẻ cái mã nguồn này ở phần mô tả bình luận của video. Anh em tải về anh em phát triển thêm, anh em 
cài thêm những này kia hoàn toàn ok nhá. Lúc đó thì mình sẽ đưa một cái sản phẩm vào production được. Đó thì cái hình mà anh em đang xem màn hình là mình nhờ chatpt sinh ra đấy thì đại khái là nó đúng những gì mình nói về đầu tiên là nó phân tích cái GD một số công việc nó sau đó anh em up cái CV của của anh em lên. đó thì nó sẽ phân tích phân tích xong nó chấm điểm là à cái vị trí 
CV này thì phù hợp với công việc nào đó và điểm vì sao nó chọn công việc đấy vì điểm mạnh của anh như thế này vì và điểm yếu của anh như thế kia nên nó chấm được nơi điểm thôi và sau đó thì nó sẽ ờ đưa cho mình những cái recommend là mình nên làm gì để improve cái CV mình lên được chưa ạ? Rồi thì trước khi bắt đầu vào xây dựng thì mình có đi qua một loạt các cái ờ gọi là công nghệ đi. Nó không 
phải là công nghệ, nó có cả framework, nó cả tool, nó có cả library. Công nghệ đi. Đó, công nghệ thì đầu tiên là cái xương sống của cái agent này là mình dùng lang trên nhá. chưa dùng Lang Grap lang trên thôi. Mình đã có bài dùng về Lang Grap rồi nên bạn nào thắc mắc Lang Grap thì lên trên kênh YouTube của mình đó và search là lang grap ra ngay mà. Đó thì Lang trên 
là một cái xương sống, cái framework để chúng ta xây dựng những con agent một cách rất là đơn giản. Nó có hết từ A đến Z, có từ à định nghĩa agent có từ cái ngôn ngữ à gọi là gì nhỉ? LC đó là để nó làm cái những cái trên những cái trên mà lang trên nên là những cái trên chạy rất là ổn. Đó thì anh em có thể xem chi tiết cái video này của mình để mà chúng ta biết được đang chơi là gì. Thứ 
hai là chúng ta có fast API và UVCON làm gì. Thì trong cái bài này cái trong tí nữa mình xem cái sơ đồ mình sẽ biết là mình sẽ có một cái là expo API ra để những cái giao diện funnel nó có thể gọi vào đấy. Vì sao lại có fan nhỉ? có fan để họ upload cái CV lên fan đấy. Upload cái file JD à CV ấn next một cái thì là hệ thống nó sẽ gọi về backend. Backend gọi vào 
agent agent sẽ đọc cái CV đó hiểu cái CV đó. Sau đó thì so sánh với những cái GD đã lưu sẵn ở trong vectơ DB à xem là với cái CV vừa up ấy thì ba công việc phù hợp nhất là gì. Và trong từng công việc đó thì phân tích chi tiết hơn cái ưu nhược điểm và cái điểm cần recomand là gì. Đó thì fast API và UVCON nhá. Ờ rồi ok. Rồi và vectơ DB mình vừa nói vectơ DB đúng không? Mình sẽ 
phải craw những cái JD về để ở vectơ DB đúng không? Thì cái vectơ DB trong bài này mình dùng là chroma DB. Bạn nào mà follow kênh của mình thì sẽ thấy là gì? Mình sẽ có một cái video giải thích cơ bản về vectơ DB và ừ cho các bạn hiểu nó là cái gì, vì sao cần nó dùng có tốt không. Và rất nhiều video khác mình đã có video dùng files của Facebook đó. Nhưng trong bài này 
thì mình sẽ dùng à có bài dùng Quidran luôn rồi. Nhưng bài này mình sẽ dùng Chroma DB. Đó mình muốn là nó đa dạng phong phú để các bạn có thể là hôm nay thích dùng cái này, mai dùng cái kia hoặc là ở cơ quan các bạn dùng cái này, ở nước thực tập của các bạn đã dùng cái kia thì các bạn đều biết nhá. Đó thì vectơ DB là một nơi để lưu những cái à vecơ lưu những thành cái cái đoạn tex đoạn 
trăng vectơ trăng vectơ trong vectơ lưu vào đấy và chúng ta sẽ dùng cái tìm kiếm ở trên cái vectơ DB đấy tìm kiếm theo simulatory dùng theo cái sự gần gũi giữa các vecor tìm kiếm theo keyword tìm kiếm theo hybrid kết hợp cả hai vân vân ok chưa ạ rồi Một thứ nữa mình sẽ dùng đó là streamlist. Streamlist trong ngày này sẽ dùng đóng vai trò là gì? Đóng vai trò là 
xây dựng một cái fun. Đó. Funel thì bạn biết rồi. Mình muốn làm bằng gì cũng được. Bạn nào thích làm bằng HTML JavaScript ok. Bạn nào thích làm bằng Vu JS ok. React JS ok. Next JS ok. Và Angular JS cũng ok. Đó. Nhưng trong bài này để nhanh mình làm bằng streamlist nhá. Streamlist là một cái tool cái thư viện ở trong Python. Và cái việc mà dùng 
Streamlist để giựng lên cái UI ấy nó nhanh lắm, rất là đơn giản. Đó. Thì đây mình cũng có một cái video rồi. Đây triển khai module đất trong 1 phút. Ồ ố ok chưa? Thì anh em cũng vào đấy mà xem nhá. &gt;&gt; Hello anh em. &gt;&gt; Đấy rồi còn đây sau khi đi hết đầy đủ những cái công nghệ rồi thì mình sẽ đến cái phần là cái luồng cái luồng hoạt động của hệ thống của mình. Đó rất 
nhiều anh em có chia sẻ mình rất nhiều các cái thứ trên mạng nhưng mà quên mất một thứ là không cho người dùng cái bản đồ như thế này hay gọi là blueprint cũng được, bản vẽ kỹ thuật hoặc là gọi là cái map cũng được. Thì khi mà cho người dùng một cái bản đồ như này ấy thì họ sẽ dễ dàng hình dung cách chúng ta làm hơn là chúng ta cứ thế chúng ta code nhá. Rồi thì đây bây giờ mình sẽ 
đi vào phần đầu tiên là phần là đọc trang web và inject of vectơ DB. Thì mình sẽ kiếm một cái gì? Mình sẽ kiếm một cái website có job ở trên đấy. Đ anh em để ý nhá. Ở Việt Nam rất nhiều trang nào là Vietnam Work, Top CV, IT Việt là nhiều lắm. Thế nhưng mà những cái trang đấy ấ nó biết thừa là cho người craw nó nên nó có cơ chế chống craw khá là phức tạp. Và nếu như mình 
muốn craw từ đó thì mình sẽ phải áp dụng một số phương pháp. đặc biệt và thậm chí là có thể dùng proxy để tránh nó chặn cái IP của mình. Đó. Thế nhưng mà thôi, đấy là demo thôi mà. Đó, còn trong thực tế thì cái việc mà chúng ta craw thông tin một website như là Viet Namw ấy thì nó không phải là AI nên mình không focus vào nên trong bài này mình chọn một cái size là Google 
Job họ không chặn thoải mái CRW nhá. Thì craw xong thì mình sẽ có gì? HTML ở trên trang web đó đúng không ạ? thì mình sẽ trang king ra sau đó mình edding mình đưa vào trong vectơ DB mà chính là chroma DB đấy được chưa và ở bài này để tiện thì mình cũng không host một cái modeling nào cả đó và máy mình không có GPU để chạy nên mình gọi Open AI đó tất nhiên anh em có thể 
hoàn toàn sale host và expose ra bằng LLM Studio bằng VLM sau đó thì gọi vào cái đó để mà adding cho đỡ tốn tiền gọi open AI được chưa thì nhắc cái đây Đây thì mình cũng cảm ơn bạn Sử Minh Thành. Đó bạn Sử Minh Thành thì mình sẽ để cái trang web bán áo phông của bạn Sử Minh Thành ở trên màn hình đó thì bạn và ở dưới phần mô tả của video. Bạn Sử Minh Thành thì là một chuyên gia 
IT rất là tốt và bạn ấy cho mình mượn cái open AI API để chuyên làm một việc là xây dựng những video để phổ biến kiến thức cái cộng đồng nhá. Mình không dùng vào việc kinh doanh hay cá nhân của mình. Rồi thì các bạn nào mua áo thì ủng hộ bạn Sử Minh Thành thì bấm vào phần mô tả và bình luận của video nhá. Mua áo thun bạn sử minh Thành có áo thun rất đẹp. Ok rồi sau đó thì 
sau khi có ming rồi thì mình sẽ làm gì? Đưa vào vectơ DB. Đó thế thì trong này sẽ có một cái job vector. Tất cả các job sẽ được vectơ hóa để vào đây để mục đích là tí nữa đi CV vào ấy sẽ mưng cái CV đấy với cả cái vectơ DB này. Đó. Ok chưa? Rồi đấy là lúc chúng ta craw và insert vào. Thì cái việc này chỉ chạy một lần thôi. Trong ví dụ này chạy một lần thôi. Đó còn trong thực tế định kỳ 
có thể là một tuần một lần hoặc một tháng một lần tùy một quý một lần tùy vào nhu cầu của các bạn đọc hết trang job về đưa vào trong cái tầdb này để lưu trữ. Ok. Thứ hai là quy trình người dùng upload CV và tìm job phù hợp. Đó thì người dùng đây đó thì họ sẽ upload cái file lên cái gì? HR agent funnel đó mà một cái mình chỉ vừa nói mình làm bằng streamlist đó cái fun này nó sẽ 
gọi về backend và backend sẽ nhận cái file upload rồi sau đó thì gọi vào agent đó hr agent core đó thằng agent này sẽ làm gì dùng ngay một cái lm để nó phân tích cái đọc hiểu cái CV của người dùng đó sau đó nó gọi một cái tool đó tool này tool để mà search trong vectơ DB đó thì truyền vào cái thông tin vector của cái thằng CV nhá CV sẽ được Ming thành vector truyền 
vào đây. Đó cái này mình đã nói giản tiện các bước đi để cho nó dễ hiểu nhá. Đó sau đó thì thằng tool này sẽ so sánh nó tìm kiếm theo những cái tiêu chí ở trên cái thằng HRC này đó và nó trả ra kết quả thì HRC sẽ sử dụng cái kết quả trả ra. rồi dùng cái LLM của nó và cụ thể ở đây là gọi open ai để làm gì? Để chém gió ra độ phù hợp, để chém gió ra cái điểm mạnh, điểm yếu, chém gió ra cái 
recommendation cho người dùng rồi và trả về. Đó thế thôi. Và trong tất cả những quá trình làm việc này thì để cho nó thuận tiện thì con con agent core sẽ dùng một cái agent agent format để làm gì? nó chuẩn hóa cái dữ liệu vào ra cho cái hệ thống này thôi chứ thực ra mình không cần này cũng được mình viết ở trong ngày cũng được thế nhưng mình muốn là nó chuẩn hóa mình sẽ 
định nghĩa riêng ở ngoài một cái lớp và nó import thôi mà đó là cái phụ mình không muốn nói ở đây được chưa bây giờ mình sẽ làm từng bước nhá ok anh em anh em đăng ký kênh đăng ký kênh để ủng hộ mii nhá đăng ký kênh thì miễn phí nhưng mi ai rất vui khi anh em đăng ký rồi bước đầu tiên là mình sẽ đọc trang web và injest. Đó thì ở đây mình đã có một cái mình đã có một cái cái project rồi. Thì ở 
đây mình đã có cái project đó. Thì bây giờ mình có một file setup.txt. Trong này đã liệt kê tất cả những cái ừ thư viện mà mình cần dùng. Các bạn chỉ cần gõ chữ là à sau khi clone cái này của mình nhá. Link sột code mình để ở phần mô tả và bình luận của video. Các bạn clone về xong thì gõ một lệnh là pip install trừ r setup là có lệnh quen thuộc. Đó thì máy này mình cài rồi 
thì nó chạy vù phát xong. Còn bình thường các bạn đợi một chút nhá. Clear cho sạch sẽ nào. Ok. Bây giờ mình làm cái đầu tiên là cái à craw đúng không? Sẽ phải craw về đó. Job cross. Rồi thực ra là mình đã làm rồi nên là mình sẽ à không code lại 100% mà mình sẽ ờ nhấn những cái phần quan trọng để các bạn chú ý. Còn những phần khác thì mình sẽ phép là copy nhá. Chứ nếu bây giờ mình 
ngồi code lại hết cái file này chắc là đến đêm. Đó, đầu tiên là mình import các cái thư viện cần thiết. Được chưa ạ? Tiếp đến là mình gì? Mình đặt cho nó cái login. Đấy. À chết rồi. Sorry. Đấy. Loging như này cho nó nhìn cho nó dễ nhìn. Lúc nào mình cần lock cái gì mình lock. Tiếp đến này mình sẽ vừa nói là mình sẽ tìm kiếm một cái base URL là một cái trang web có ờ việc làm mà 
không chặn đúng không? Thì đây mình dùng cái trang này để mình mở bạn xem cái trang này là cái trang Google career của Google đây. Đấy. Ok chưa? Mình tìm ở khu vực Việt Nam thì nó có tất cả những cái shop ở đây và nó không hề chặn mình craw. Thế còn những size phức tạp hơn thì các bạn sẽ phải dùng đến những cái kỹ năng để lách cái chặn đấy thì mình không hướng dẫn ở đây. Rồi mình 
định nghĩa một cái header đó cái header. Header để làm gì? Để khi mình request vào cái trang web kia thì mình send cái header này để nó tưởng là mình đang truy cập từ một cái browser chứ không phải là mình craw đó. Không có chặn ngay đấy. Ok. Ờ rồi định nghĩa thêm một cái a tiếp đầu ngữ đó là tất cả những cái job mình sẽ bắt đầu bằng cái từ này đoạn này. Ok thì giờ mình sẽ làm 
gì đây? Mình sẽ phân tích từng bước một nhá. Với một cái hàm sin đó de ờ get job đúng job gợi ý kinh thế. À inest jobs. Rồi thì cái hàm này mình sẽ làm gì? Đầu tiên là mình log ra một câu đi. Lock ra một câu là biết là đã đến cái bước mà thập dữ liệu thì đầu tiên là mình làm gì? Một này là mình thu thập danh sách URL việc làm. Đó có nghĩa là gì? Đọc vào cái trang này của mình này. Đó 
trong đây là mỗi đây là một cái URL việc làm này. Đó rất nhiều việc làm thì mỗi việc làm n sẽ có URL riêng learn more này. Đó bạn nhìn không? Đó thì mình sẽ viết một cái hàm để mình à thu thập lại tất cả những cái URL việc làm đấy để làm một cái list. Sau đó mình sẽ craw từng cái URL đấy đúng không? Đây thì đơn giản thôi. Đây mình sẽ copy nhá. Đây copy xong giải thích rồi. Ok. Đấy job 
URL bằng red job và truyền vào cái bas đó và lật năm trang nhá. Thì nếu không tìm thấy thì báo luô luôn là không tìm thấy và dừng. Còn nếu không thì sẽ job URL sẽ chứa tất cả những cái URL trong công việc trong năm trang. Bây giờ mình cần viết hàm get job URL đúng không? Đó cần viết get job URL đây. Rồi copy lên trên này. Đó thì đây là một cái hàm rất là đơn giản thôi là 
mình sẽ à đây mình sẽ lúp trên cái trang của người ta. Xong cứ lúp từng trang từng trang một. Xong rồi gặp cái nào thì mình gọi các cái hàm tương ứng để mình extract ra thôi. Đây. Đó. Rồi đây loop này. Lúp từng page một này. Đó. Xong rồi là tải trang rồi lúp ra. Mình viết nốt mấy cái hàm mấy cái hàm phụ của nó nhé. Rồi p. Ok. Đó thì mấy cái hàm này là hàm phụ trợ để nó làm thì các 
bạn sẽ nghiên cứu sau. Nhưng mà tóm lại là nó sẽ làm gì? Nó sẽ lúp qua từng page đó. Và trên từng page nó sẽ lấy những cái URL ở những cái trang này. Đây này. Learn Me. Learn More là có URL hết này. Rồi thì lấy xong là sẽ có một tập những cái gì? URL đó. Mình từ print cho các bạn xem nhá. print này. Job ul chạy thử này. Python injest job p job ô à sorry các 
bạn. Đó chưa gọi bây giờ gọi vào ra đã. Ok rồi đó bắt đầu nó tải trang 1, trang 2. Đó đó đó đó. Và sau khi mình chạy một loạt xong mình sẽ có tập các URL. Đó. Ok chưa? Rồi bây giờ bước hai gì? Xử lý cái đống URL đấy. Đấy. Bước hai à xử lý cái đống URL đấy. Đây. Đây xử lý là gì? Tải đó tải song song các nội dung đó. Một đống drop URL đúng không? Bây giờ tải song song các nội dung thì cần nhữ 
cái hàm script URL đúng không? Thì này cũng là không phải là AI nữa rồi. Cái này nó là cái hàm ờ gọi là http. Rồi đây mình sẽ viết trên này bạn xem đó một cái hàm gọi là HTTP đơn thuần chứ không phải là fé content về sau đó thì là chích các thông tin đó. Đây đó lấy ra request về xong rồi bắt đầu là đưa vào một cái tập document và trả về. Đó thì không hề có cái gì AI ở đây cả. Đó thì đã tải được 
hết cái đống job ấy về. Mỗi job sẽ có một đống văn bản thể hiện cho cái job đấy. Thế bây giờ làm gì? Ứ bây giờ mình sẽ xóa cái ờ trắng cái vector DB. Đó mình sẽ dùng chroma DB ở local luôn nhá. Đó để cho minh họa mà nên mình sẽ xóa trắng cái dữ liệu cũ để đề phòng là khi mình inject thêm cái job về nó bị đè nó bị lẫn lộn mình xóa trắng hết xong mình inject về. Đó còn thực tế các bạn 
điều chỉnh như thế nào tùy đó. Cái này là lệnh làm việc chroma DB và cái mình giải thích thêm là cái Chroma DB này lưu ở local nó sẽ lưu trong thư mục là Chroma DB đó còn thực tế thì sẽ không dùng cái này đâu. Local này chết. Đó bước bốn này mình tạo một cái đối tượng cái embedding. Đó được chưa tạo một cái edding bằng cái là openeding và là text eding 3 small. Sau đó mình sẽ 
tạo một cái vector store là job posting và lưu vào thư mục coba 3DB và dùng cáiing này đểding những cái vector DB những cái văn bản đưa vào cái vector DB này. Đó rồi thì đơn giản thôi. Sau đó mình làm gì? Mình dùng cái trang mình em adding theo batch đó. Theo B nhá theo B để mình đưa lần lượt vào document vào cái vectơ DB. đó đưa do vào vectơ DP được chưa? Ứ và cứ 15 
văn bản một lần mình đưa vào vectơ này để eding cả cái văn bản mà mô tả công việc đấy. Đó thì sau khi nó em đing xong nó ra một cái vecơ đó và để cho nó nhanh thì mình chơi theo B 15 phát một lần 15 một lần chứ không chơi từng cái một lâu lắm. Đó thì sau bước này là gì? Mình sẽ có được cái gì? mình sẽ có được là tất cả những cái mô tả công việc góc kia mình craw được sẽ được bằng cái texting 
spa small và đưa vào chroma vector db được chưa ạ? Đó thì ở đây có một cái vấn đề là gì? Bạn sẽ bảo ô ông gọi open AI mà ông không có cái API key à. Đó thì nó ở đây chúng ta sẽ phải có một cái file.nv đó chnv đó. Và open AI API key sẽ bằng cái API key của các bạn nhá. Được chưa? Rồi này coi như mình đã đưa được cái thông tin API key vào cái file NV rồi nhá. Mình phải cắt video nếu 
không lỗ API key của bạn sửa Minh Thành. Rồi bây giờ xong rồi đấy. Vậy mình làm xong các bước về giờ mình kỳ vọng là khi mình chạy lại cái file này nó sẽ làm sao? tạo ra một cái chromb local và lấy tất cả những cái gding và đưa vào trong tdb đấy. Nào rồi. Ok chưa? Ok chưa? Rồi bắt đầu bắt đầu bắt đầu c đấy. Rất may là cái trang Google này họ không chặn rồi. Lập chỉ mục 
này. Lô 1/3 15 tài liệu đầu tiên. Ok đã xong. Đã xong. Đã xong rồi. Mình đã thấy là một cái thư mục Chrome ADB đã sinh ra và bên trong có những cái file quỳ quặc gì của họ. Đó SQL Line mà đó thì đã lưu hết vào Vector DB rồi. Như vậy là xong cái bước đầu tiên là bước craw. Chúng ta đã xong cái đầu tiên này. Cái phần đọc trang này nhá. Bây giờ mình sẽ làm cái phần thứ hai là khi 
người dùng upload cái job lên thì mình sẽ xây ngược từ dưới lên. Người dùng mình sẽ xây không bao giờ xây fun end trước back end sau rồi đến core mà mình xây ngược từ thà tử nhỏ nhất lên trên. Đó là xây dựng cái format trước và cái tool trước. Được chưa? [âm nhạc] Rồi bây giờ cái format này lưu một cái file HR agent format. Đó nó sẽ có cái gì đây? Nó đơn giản lắm nó là một cái định 
nghĩa như này. Đó dùng cái pentic ấ mà định nghĩa là gì? Trong cái kết quả phân tích của cái con agent trả ra sẽ có cái gì? Sẽ có một cái trường job id định danh của cái cái job đó. Đó mà khi mình craw và mình nhét vào trong cái vectơ l B ấy. ID của cái đó. Vị trí tuyển là gì? URL ứng tuyển là cái gì? Ở chỗ cái URL mà more ấy. Mh score đó là một cái điểm phù hợp do LM đánh giá 
từ 0 đến 100. Đó. Ở đây mình có điều kiện luôn này. Ge le đấy. Retter than à less than ạ. Đó. Rồi strength. Điểm mạnh của thí sinh là gì? Tại sao chọn công việc này? Ờ những skill mà người ta thiếu là gì và cách improve như nào? Đó. Và đây là một số cái mình để validation để mình kiểm tra. Đó thì mình sẽ cần phải kiểm tra xem là nó có trường reasoning hay không. Đó, nếu mà 
không có thì mình trả về rỗng rồi mình kiểm tra xem là có cái trường impr hay không. Nếu không thì mình cũng trả về à rỗng. Đó, rồi một số cái bước kiểm tra đó. Và nếu như mà cái trường reasoning đó thì mình kỳ vọng là model sẽ trả ra trường reasoning. Nhưng mà có lúc nó trả ra reason, lúc trả ra explanation, lúc trả ra nên mình làm một cái gì cứ for trong các cái biến 
này mà nếu mà trong dữ liệu trả về nó có một cái nào trong đây thì mình đều phải gán nó vào trườnging cả để đề phòng con LM nó bị không ổn định. Đó, tương tự như vậy, impr improvement cũng vậy. Lúc có trả về tip, lúc có trả về advice mình cũng làm thế, mình lấy lại giá trị của nó được chưa? Rồi. Đó, và mình trả về một cái là match là một cái list đó các cái trường là rồi description 
thôi. Đơn giản đó thì bạn để ý đây sẽ là nghĩa gì? Cái M res và M respond. Được chưa? Ok. Rồi xây dựng xong cái format. Bạn nào muốn hiểu kỹ phần này thì tìm về cái pedantic nó rất là dễ hiểu nhá. Mình sẽ không nói ờ chi tiết ở đây. Đó. Rồi mình đã có một quy định về format mà cái model phải trả. Bây giờ viết cho nó cái tool đó. HR agent tools đó. Đó để nó làm gì? Để nó chọc vào trong 
DB không lấy gì nó chọc đúng không ạ? Thì chúng ta sẽ phải làm gì? Chúng ta sẽ phải là import một số biến này đó và khai báo một số thông tin. Đây mình sẽ post cho các bạn xem. Đó khai báo cái gì? Khai báo cái collection name. Vừa nãy lúc chúng ta craw về và injest vào cái vector DB chúng ta dùng collection là job posting. Đó bạn nào mà làm việc vector DB 
hoặc là mongo db rồi sẽ quen với khái niệm collection. Đóding model là gì? Mình vừa mớiing bằng tex mding 3 small. Thì đây mình cũng phải dùng đúng cái model đấy chứ lại cross job về một model mà bây giờ dùng model khác để màing cái câu hỏi của người dùng ấy thì sai chắc chắn. Được chưa? Rồi thì mình sẽ viết một cái tool cho con agent. Đây tool đây. Đó tool này là 
tool gì? Tool search job. Đúng rồi. Mình vừa nói rồi mà cho nó cái tool search job nó chia vào cái câu truy vấn của người dùng trả ra năm cái dóc đầu tiên. Đó và we document là một câu lệnh thêm để cho nó search. Ngoài cái việc search về về similitary thì nó truyền cái weare vào để nó filter thêm một số cái văn bản là cái document ở trong cái collection này. 
Ví dụ nếu truyền string thì sẽ tìm kiếm theo cái có chứa string đấy. Nếu truyền dictionary thì sẽ truyền thẳng vào where à in document đấy. Đó vân vân. Đó cái này nó thiên về à vectơ DB. Đó. Rồi thì đầu tiên mình gì? Mình get vector store. Get vector store để làm gì? Vector để là đọc vào cái vector DB mà chroma DB local mình vừa tạo ở đây này. Đó, gán cor name, gán 
embedent function là bằng cái này. Rồi gán ờ dear là cái thư mục nào, thư mục này. Ok, xong được chưa ạ? Thì khi mà một cái vector DB nó đã được gán bằng một cái eding function như này rồi ấy thì tất cả những cái văn bản đưa thêm vào nó sẽ eding bằng đúng cái model đấy để nó sau khi nó nó ra được vectơ nó sẽ so sánh với những cái ở trong cái vectơ DB đó. Được chưa ạ? Rồi bắt đầu là 
tìm kiếm à normal filter. Ở đây có cái normal life filter là mình thật ra là mình để cho người dùng nhập vào cái cái cái filter này này có we này này thì mình sẽ dùng một cái hàm để mình chuẩn hóa lại cái đấy đề phòng người dùng gõ sai đó đại khái là mình sẽ chuẩn hóa lại đúng cái ngôn ngữ của we document của Chroma thôi đó rồi sau đó mình sẽ đc filter cho cái wewe vào lọc theo 
cái document trong cái collection đó và cuối cùng mình sẽ làm câu này này match doc bằng store là chính là cái vector store simary search query search param rồi query là gì lấy cái câu query là của người dùng mà câu query của người dùng đây là cái gì là cái file thông tin trong cái file CV của người dùng đó đưa vào query này và truyền thêm cái search 
parameter chính là cái filter document và gọi một cái lệnh này là thằng vector DB nó trả ra top 5 những cái cái GD mà tương đồng nhất với cả cái CV đó. Và sau đó mình trả về đó. Cái này cái tool này nó không có phán xét, nó không có ờ định gọi là nhận định gì ở đây cả. Nó là một cái tool để cho phép con LM nó có thể là search theo vecơ và nó trả ra cái đống văn bản à đống đống đống 
GD liên quan đến cái CV của người dùng. Đó. Sau khi con LM nó gọi được cái tool này, lấy được rồi ấy, nó có data rồi nó đưa vào prom ấy thì nó mới chém gió, nó mới nhận định, nó mới nhận xét. Ok chưa ạ? Đó, đóng cái tool nhá. Rồi bây giờ đến phần tiếp theo là chúng ta viết HR agent. Đó chính là cái core, cái core của của hệ thống. Thì đơn giản thôi, chúng ta cũng lại sẽ import và 
cấu hình một số cái log. Đó, được chưa? và đã nói là đây là một con agent dùng lm thì chúng ta sẽ có một cái prom cho nó đây. Prom prom cho nó đây. Đoạn này viết khá là dài. Đại khái bạn là một chuyên gia tuyển dụng thì bạn hãy review cái background của ứng viên, dùng cái search job để query những cái gd liên quan. Sau đó thì là ờ dựa vào những cái a CV JD trả về thì 
compare so sánh với cả CV của ứng viên. Sau đó thì là lấy ra ba cái công việc mà phù hợp nhất và mỗi cái mature thì bạn phải cấp đủ thông tin. Job ID, Job TI, URL, MCOR, bla bla chính là cái trường mà mình quyết định trong format này này. Đó nhưng mà LLM ấy nó không nghe mình 100% nhưng có lúc nó trả ra không đúng những trường đấy nên là mình phải rơi cái trò là đây 
validate đây này nhá. Rồi critical đó mình cố tình prom thêm để cho nó nó trả ra đúng ấy nhưng mà có lúc nó không trả đâu. Là reasoning field phải là không được rỗng đó. Và cái improvement phải là trả về string chứ không phải list. Ờ rồi cố mà prom rồi nhưng mà nó vẫn cứ dị dị lắm. Rồi thêm hai cái cấu hình LM mình sẽ dùng GPT 4 mini. Đó các bạn sẽ hỏi sao không dùng cái 
model xịn nhất GPT 5 chấm hoặc là bản Pro. Thật ra mình demo thôi. Mình dùng tiết kiệm cho bạn Xử Minh Thành nhá. Bạn Sử Minh Thành nhắc lại nữa là bạn Sử Minh Thành tài trợ cho mình cái API để làm video demo cho các bạn trên BAI. Bạn nào mua áo cho bạn Sử Minh Thành áo rất đẹp, áo về Open Claw thì bấm vào phần mô tả, phần bình luận của video để mà lấy link 
nhá. Rồi bây giờ chúng ta làm gì nào? Chúng ta sẽ build một cái hàm get agent. Đó, get agent đó. Get agent thì sẽ làm gì? Sẽ build lm đây. Rồi mình sẽ build một con agent bằng hàm create agent. Thế mọi người hỏi hàm này đâu ra? Lang trên đấy. Lang trên nó hỗ trợ mình nhanh lắm. Bình thường em viết legion ôi giời ôi lại phải đủ thứ đúng không? Bây giờ gì? Gán tool 
bằng cách thủ công. Prom cũng thủ công. Thì bây giờ tất cả đã có trên hỗ trợ đó. CP agent a bây giờ đấy dùng lm nào đây? Dùng lm bằng biến lm. Thế biến lm là gì? Đấy, chat open AI và truyền vào cái JPT4 và cái temperator mình vừa làm ở trên này. Đó, tool à search job. Ủa mọi search job ở đâu đây. Search job được import từ con HR agent tool này sang. Đó, truyền vào 
một cái là nó tự biết là có cái tool này để mà khi chúng ta gọi lệnh thì nó sẽ đưa cái job ấy vào để cái description của cái job ấy và cái cái tool ấy vào đó. Không có làm thủ công nữa. Đó. System prom đây. Ở trên này rồi. Ok. Respon format đó. Providersy mat respon. M respon ở đâu? Import từ con format. Đấy. Để mình nó sẽ phải theo cái format này của mình. Được chưa? F 
nó thôi. Ép bằng cái lệnh là sau đó sẽ đưa cái này vào trong system prom này để mà ép nó thôi. Nhưng mà à không phải mình sorry nhá. và prom mà mình sẽ ép nó bằng cách instruction để nó đưa ra được cái à ừ à format đúng của mình. Thế nhưng mà có lúc nó vẫn không đúng đâu. Đó rồi xong rồi. Cái này rất đơn giản không? Định nghĩa system prom định nghĩa là lm b một con agent đưa vào cái 
tool xong. Ok rồi. Thế bây giờ mình sẽ demo. Mình không biết là con agent này nó chạy có chuẩn không mình phải demo đúng không? viết một cái store demo đây. Đó cái hàm này sẽ để demo mình đưa vào cho nó khởi tạo agent sau đó mình đưa một số cái resoom vào xem nó có trả ra không. Nếu mà nó trả ra là chuẩn còn nếu không trả ra thì tỏ là tèo rồi. Đó thì công sức nãy giờ mình 
viết là tèo rồi nhá. Python hrent.P đó. Rồi đang xử lý resume. Ok. Có vẻ chuẩn đấy. Nào chạy được không? Đó eming rồi này. Ok. Đó nó đã tìm được ba cái quả phù hợp. Đó dựa vào cái công việc là trên này đây. John du rồi senior bla bla thì nó tìm ra ba công việc này và nó đưa lý do điểm mạnh điểm yếu rồi b la đó. Ồn thôi chạy ngon rồi. Tất nhiên là mình chưa kiểm tra là cái này có đúng 
không nhưng mà cái đấy thì dành cho các bạn nhá. Bạn kiểm tra và file tuning cái model sau khi à bạn test ngon lành bạn file tuning cho nó chuẩn. Bây giờ mình chỉ ghép nối các cái kỹ thuật vào để mình chứng minh là có một cái giải pháp chạy được. Rồi như vậy là cái agent đã ok rồi đấy. Bây giờ mình muốn thử thì mình phải làm một cái giao diện đúng không? giao diện để mà 
mình ố được CV chứ đúng không? Đó làm backend trước đấy. HR agent be backend. Backend khá đơn giản dùng UVC và fast API. Đó mình sẽ làm một cái gì? À một cái app đây à khai báo một cái app fast là trợ lý tuyển dụng AI đấy. API hỗ trợ phân tích CV gợi công việc và đây là call nghĩa là cho phép nó gọi từ bất kỳ cái endpint nào nhá. Thực tế sẽ không làm như thế này. Mình sẽ fix 
chỉ gọi được từ endp của mình thôi. Còn đây là mình đang test mình cho mở toa. Được chưa ạ? Rồi bao giờ cũng thế là một cái php sẽ có một cái hàm health để check đó để gọi vào xem là nó chạy không. Nếu mà chạy gõ health mà nó trả ra là hệ thống hoạt động bình thường như vậy gọi là hệ thống đang on. Thứ hai mới là hàm quan trọng hàm file job. Đó đây file job là hàm như thế nào? Đây là 
expo api mà người dùng sẽ đưa một cái file vào luôn đó. Upload file vào và mình sẽ nhiệm vụ là mình sẽ lấy cái file đó gọi agent để agent nó nó nó hiểu và nó ờ thực hiện cái tác vụ là so sánh với GD rồi trả ra là các kiểu đúng không? Rồi thì mình nốt vào đây. Đây mình nốt cho các bạn xem nhé. Nhận file đó PDF phân tích tìm kiếm phù hợp trả về dưới dạng SSE để cập nhật quá trình tìm 
kiếm rient time. Đó server send event là làm khi mà server nó client và server tạo một cái notion và khi server nó có cái action gì nó send về cái là client nó hiện lên luôn. Thay vì việc ngày xưa mình làm là cứ submit lên xong ngồi đợi đúng không? Rồi đầu tiên là chúng ta up file lên thì mình sẽ phải đọc file đấy. Đọc xong thì chuyển thành B64. Chuyển B để 
làm gì? Để đưa vào system à để đưa vào prom. Để đưa vào prom theo và gửi lên cho con LLM nó xử lý. Đó. Đây mình sẽ viết một cái hàm để mình trả về. Đây mình sẽ copy cho mình giải thích nhá. Rồi bước đầu là đây mình sẽ tạo ra một cái event generator để mình chính là sự kiện đấy. Tạo ra sự kiện mình sẽ xử lý ở trong cái hàm đấy và xử lý đến đâu mình tạo ra sự kiện mình bắn về cho thằng client 
cái đó. Rồi bắt đầu phân tích CV đó tên file này rồi dung lượng của file này. Ok bắt đầu mình bắn cho người cho cho client này. Đó trả về cho client là một cái data status là gì? đã nhận CV bắt đầu phân tích. Đó, lúc này nó sẽ hiện lên trên client là đã phân tích rồi. Sau đó mình sẽ tạo ra cái message content đúng theo chuẩn Open AI. Nào bắt đầu tiên là cái P đầu tiên nhá. P 
đầu tiên là text. Đây là CV của tôi. Hãy phân tích. P thứ hai là một cái file. Được chưa? Sau đó mình làm gì? Đây mình sẽ bắt đầu gọi gọi agent nhá. Gọi agent đây. Gọi agent và truyền vào cái message content. mình vừa mới làm ở trên này. Đó và khi agent nó thực thi nó lại tiếp tục là trả về những cái message. Đó thì là mình sẽ kiểm tra cái message trả về. Sau rồi nếu như 
trong cái máy trả về nó quyết định là gọi tool đây. Gọi tool đấy. Có chữ tool c đó thì mình làm gì? Mình sẽ gọi tool cho nó. Đây gọi tool bằng cái cách là mình gọi cái hàm à gì nhỉ? và tìm kiếm ấy. Đó, rồi sau đó thì là nó sẽ chạy cái tool đấy. Chạy tool xong thì nó sẽ trước khi chạy tool à chạ chạy tool ấy thì nó sẽ làm là nó sẽ bắn ra cho client một cái câu là đang tìm kiếm việc 
tool name để client biết là à nó đang tìm kiếm ở cái tool đấy. Được chưa? Rồi sau đó thì khi mà có kết quả trả về tool đó thì bắt đầu thấy hiện ra là đã tìm thấy công việc phân tích độ phù hợp. Đó vì tool trả ra kết quả thôi mà. Và nếu như cuối cùng nó trả ra một cái là message ty bằng AI là gì? Đây message type này ở trên này type bằng text này. Đó type bằng file này. Và nếu như 
type bằng AI đó và cái live assist mà có content nó không bị nun thì chứng tỏ là a thằng client à thằng server đã trả về rồi. Thằng AI agent đã trả về rồi và bắn cho người dùng câu là reson và content. Đó kết thúc và cho người dùng câu là đă để cho client biết là đă rồi và hoàn thiện cái việc mà xử lý đó thì chính là cái event generator hoạt động như vậy nhá. Tóm lại đại khái 
là gì? Event generator để tạo ra cái event bắn về cho client đó. Và client sẽ với server kết nối bằng server send event đó. Và sau đó thì nó sẽ upload file PDF lên. Đó gọi vào agent. Agent sẽ quyết định là có tool c hay không. sẽ quyết định là đủ thông tin rồi thì phân tích bla bla bla. Đó và đây chắc các bạn hỏi là ơ thế gửi lên PDF thì làm sao mà cái con LM nó nó 
đọc nó hiểu là tex ở trong đó thì cái việc mà chúng ta ờ upload cái file PDF lên ấy thì là đã có cái mini 4o nó đọc và nó xử lý cho chúng ta rồi. Đó cái cái thằng à chúng ta chỉ việc lấy cái text ra và chúng ta coi như là có text rồi và chúng ta sẽ ading và compare nó với cái ừ JD ở trong cái DB thôi. Đó và trong quá trình compare đó thì chúng ta sẽ gọi tool c để lấy ra 
và compare rồi chúng ta sẽ ừ bắn những cái event về cho client để client hiển thị và cuối cùng là đăng và cuối cùng chúng ta trả về một cái streaming response đó bằng cái evangelator này và kiểu là event stream đó thế là xong rồi đấy lúc này là xong cái hòn backend này rồi đó Và để chạy được nó thì chúng ta sẽ thêm một cái câu cuối cùng để chúng ta serve bằng UV con. Được 
chưa? Đó. Và port là bà chạy thử nào. Python HR agent B. Ok. Không báo lỗi và đã shop ở đây. Đó và chúng ta gọi lệnh heo mà nó hiện ra là đang hoạt động đặt. Ok rồi nhá. Rồi bây giờ chỉ còn thằng fan. Thằng fan dùng streamlist đúng không ạ? HR agent đó. FE đó thằng FE này thôi mình khỏi giải thích nhá. Nó không có yếu tố kỹ thuật gì ở đây cả. Nó chỉ là một cái file 
streamlist. Sau đó thì nó sẽ connect vào cái thằng server. À đây chỗ gọi cái chỗ server đâu rồi? Cái chỗ local đây đây đây đây đây đây đây đây đây đây đây đây. Đó. connect vào file gọi hàm file job khi mọi người dùng upload cv xong thì gọi hàm file job truyền cái file lên và sau đó lấy những cái thông tin trả về và hiển thị đó không có cái gì đặc sắc ở đây cả và nó cũng không phải ai 
nên mình sẽ tu nhanh qua phần này đó rồi thế giờ mình làm gì chạy backend lên rồi sang đây streamlistam list à hr run hr agent fe enter Rồi xong nhá. Backend đã chạy đây rồi. Fun thì mình gõ lệnh xong nó ra cái này. Cái này vì sao mình không nói rõ? Vì chắc chắn là trong thực tế các bạn sẽ không dùng streamlist để làm các hệ thống của các bạn. Cái này chỉ hoàn 
toàn làm demo. Đó còn thực tế bạn sẽ làm những cái công cụ khác như vừa nói là VGS React GS. Nhưng thôi để để mô nhanh thì mình dùng streamlist upload file CV lên. Đây mình có một cái file CV. File CP này mình dùng clot để viết ra nên tất cả thông tin trên này đều không có thật nha. Nhưng mà đại khái là mình bắt clot mô tả mình một người làm IT có một tí technical 
content cre ở Hồ Chí Minh có một số cái product như là Bal 2 antif đó upload lên rồi và nhấn phân tích. Đó nó sẽ gọi lên server đây này. Đó server bắt đầu chạy này. Bắt đầu phân tích CV này. Đó tìm kiếm job này đã tìm thấy việc này. Trả về rồi này. Đó và nó đang phân tích mức độ phù hợp chính là gọi HR Agent. Đó. HR Agent sẽ phân tích bằng LLM và trả ra kết quả. Rồi đây. Vậy nhiệm 
vụ của mình lúc này là gì? dùng HTML để render ra cái kết quả cho nó đẹp thôi. Thực ra chả dạng text nhưng mình sẽ render cho nó đẹp. Được chưa? Đây này. Chỗ render đây bạn xem này. À đâu rồi? Phân tích hoàn tất à đây đây đây đây. Trang trí một tí này. Đó trang trí lên xuống rồi trang trí score, trang trí reasoning, strang toàn trang trí thôi. Đó. Rồi bây giờ nhỉ ví dụ như 
mình cái customer solution constant platform thì lý do phù hợp là gì? À experience cloud AI ok điểm mạnh là gì? 10 năm software chuẩn điểm yếu là gì? Security concept và cloud platform đúng. Trong th của mình không hề có một cái chuyên thời gian nào mình làm về cloud nên nó giữ nó nó nó recommend mình là gì? Gain more experience trong việc là 
cloud focus roll. Đúng rồi, muốn vào cloud thì cần phải có kỹ năng cloud, không ai tuyển. Thứ hai này, associate partner là có vẻ bán hàng à. Ấn vào rồi. Technical project manager solution nhưng mà bổ sung này à serving industry và Android development. Ok thì là mình phải làm gì? Ờ file cho s with serving industry và sau đó thì là button 
sure. Ok. Dưới cùng là cluster manager. Ok. People management và advertising. Đúng rồi. Đây là có GTX đây này là quảng cáo này thì phải có cái advertising và tip của nó là gì? Enhance understanding in bl. Đó. T lại đại khái đấy. Và các link ứng tuyển là mình đều có ở đây. Bấm vào nó sẽ hiện ra cái link Google career. Được chưa ạ? Phần này hoàn toàn trang trí 
thôi, không có gì phức tạp cả. Rồi đại khái là mình đã xong một cái project về xây dựng một con AI agent CV Matching. Các bạn hoàn toàn có thể sử dụng cái sột code mình để phần mô tả bình luận của video để mà làm những cối riêng của bạn nhá. Nếu thấy hay cho mình like và đăng ký kênh để ủng hộ Mai nhá. Nhiều người xem nhưng quá cười đăng ký mãi không được nút bàn. Bye bye anh 
em.
---

## Repo files in full (thangnch/MiAI_CV_Matching_AI_Agent @ main, fetched 2026-07-05)

### README.md

```
# MiAI_CV_Matching_AI_Agent
Demo of building AI Agent for CV Matching

Video link:  https://youtu.be/7gIwR5SwM_0

#MìAI <br>
Fanpage: http://page.miai.vn<br>
Group trao đổi, chia sẻ: https://group.miai.vn<br>
Website: http://miai.vn<br>
Youtube: http://youtube.miai.vn<br> 
```

### setup.txt

```
fastapi
uvicorn
langchain
langchain-openai
langchain-chroma
chromadb
pydantic
python-multipart
python-dotenv
bs4
streamlit```

### hr_agent.py

```
"""Khởi tạo và cấu hình LangChain agent cho hệ thống resume matching."""

import asyncio
import logging

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy

from hr_agent_tools import search_jobs
from hr_agent_format import MatchResponse

load_dotenv()

logger = logging.getLogger(__name__)


# Prompt hệ thống hướng dẫn agent hành xử như một Career Coach
_SYSTEM_INSTRUCTION = (
    "You act as a seasoned talent advisor with deep knowledge of hiring practices.\n"
    "Your mission is to match a candidate's profile against available positions in the database.\n\n"
    "Follow these steps:\n"
    "1. Review the candidate's background, skills, and experience from their resume.\n"
    "2. Use the `search_jobs` tool to query relevant openings. Run multiple searches with different keywords if necessary.\n"
    "3. Compare each returned position against the candidate's strengths and gaps.\n"
    "4. Pick the 3 strongest matches overall.\n"
    "5. For each match, you MUST provide ALL of these fields:\n"
    "   - job_id: the job posting ID\n"
    "   - job_title: position title\n"
    "   - job_url: the source URL of the posting\n"
    "   - match_score: integer 0-100\n"
    "   - strengths: list of candidate strengths matching this role\n"
    "   - reasoning: a single string explaining WHY this job is a good fit (DO NOT skip this field)\n"
    "   - missing_skills: list of skills the candidate lacks for this role\n"
    "   - improvement_tips: a single string with actionable advice (NOT a list)\n\n"
    "CRITICAL: The 'reasoning' field must be a non-empty string. "
    "The 'improvement_tips' field must be a single string, NOT a list.\n"
)

# Cấu hình model LLM
_LLM_MODEL = "gpt-4o-mini"
_LLM_TEMPERATURE = 0

def _build_llm() -> ChatOpenAI:
    """Tạo instance ChatOpenAI với cấu hình đã định."""
    return ChatOpenAI(model=_LLM_MODEL, temperature=_LLM_TEMPERATURE)



def get_agent():
    """Tạo và trả về Career Coach agent đã được cấu hình đầy đủ."""
    llm = _build_llm()

    agent = create_agent(
        model=llm,
        tools=[search_jobs],
        system_prompt=_SYSTEM_INSTRUCTION,
        response_format=ProviderStrategy(MatchResponse),
    )
    return agent


async def _run_demo():
    """Chạy demo agent với một resume mẫu."""
    logging.basicConfig(level=logging.INFO)
    logger.info("Khởi tạo agent...")

    agent = get_agent()

    # Resume mẫu để test
    sample_resume = (
        "John Doe\n"
        "Senior Software Engineer\n"
        "Skills: Python, AWS, Docker, Kubernetes, FastAPI, React\n"
        "Experience: 5 years building cloud-native applications.\n"
    )

    logger.info("Gửi resume mẫu cho agent xử lý...")
    result = await agent.ainvoke({
        "messages": [{"role": "user", "content": f"Here is my resume:\n{sample_resume}"}]
    })

    # Parse structured response
    structured_data: MatchResponse = result["structured_response"]

    print(f"\nTìm được {len(structured_data.matches)} kết quả phù hợp:\n")
    for match in structured_data.matches:
        print(f"  {match.job_title} (Score: {match.match_score}/100)")
        print(f"    Lý do: {match.reasoning}")
        print(f"    Điểm mạnh: {', '.join(match.strengths)}")
        print(f"    Thiếu: {', '.join(match.missing_skills)}")
        print("-" * 50)


if __name__ == "__main__":
    asyncio.run(_run_demo())```

### hr_agent_format.py

```
"""Định nghĩa các Pydantic model cho response của hệ thống matching."""

from typing import List, Union

from pydantic import BaseModel, Field, field_validator, model_validator


class MatchResult(BaseModel):
    """Kết quả phân tích mức độ phù hợp giữa resume và một job posting."""

    job_id: str = Field(
        ...,
        description="ID định danh của job posting",
    )
    job_title: str = Field(
        ...,
        description="Tên vị trí tuyển dụng",
    )
    job_url: str = Field(
        default="",
        description="URL để ứng tuyển",
    )
    match_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Điểm phù hợp từ 0-100",
    )
    strengths: List[str] = Field(
        default_factory=list,
        description="Các điểm mạnh của ứng viên khớp với yêu cầu",
    )
    reasoning: str = Field(
        default="",
        description="Lý do tại sao phù hợp hoặc không phù hợp",
    )
    missing_skills: List[str] = Field(
        default_factory=list,
        description="Các kỹ năng quan trọng ứng viên còn thiếu",
    )
    improvement_tips: str = Field(
        default="",
        description="Gợi ý cải thiện để tăng cơ hội trúng tuyển (một chuỗi duy nhất)",
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_field_names(cls, data):
        """
        LLM đôi khi trả field name khác với schema.
        Map các alias phổ biến về đúng tên field.
        """
        if not isinstance(data, dict):
            return data

        # reasoning aliases
        if not data.get("reasoning"):
            for alias in ("reason", "explanation", "rationale", "match_reasoning", "fit_reason"):
                if alias in data and data[alias]:
                    data["reasoning"] = data[alias]
                    break

        # improvement_tips aliases
        if not data.get("improvement_tips"):
            for alias in ("tips", "improvement_tip", "advice", "suggestions", "recommendation"):
                if alias in data and data[alias]:
                    data["improvement_tips"] = data[alias]
                    break

        return data

    @field_validator("improvement_tips", mode="before")
    @classmethod
    def coerce_tips_to_str(cls, v):
        """Nếu LLM trả list thay vì string, nối lại thành chuỗi."""
        if isinstance(v, list):
            return "; ".join(str(item) for item in v)
        if v is None:
            return ""
        return v

    @field_validator("reasoning", mode="before")
    @classmethod
    def coerce_reasoning(cls, v):
        """Nếu LLM trả list hoặc None, xử lý cho đúng."""
        if v is None:
            return ""
        if isinstance(v, list):
            return "; ".join(str(item) for item in v)
        return v


class MatchResponse(BaseModel):
    """Response chứa danh sách kết quả matching."""

    matches: List[MatchResult] = Field(
        default_factory=list,
        description="Danh sách các job match đã được phân tích",
    )
```

### hr_agent_tools.py

```
"""Định nghĩa các tool phục vụ agent tìm kiếm việc làm."""

import asyncio
import logging
from typing import List, Dict, Union, Optional

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

logger = logging.getLogger(__name__)

# Cấu hình vector store dùng chung
_COLLECTION_NAME = "job_postings"
_EMBEDDING_MODEL = "text-embedding-3-small"
_PERSIST_DIR = "./chroma_db"



def _get_vector_store() -> Chroma:
    """Khởi tạo kết nối tới ChromaDB vector store."""
    embedding_fn = OpenAIEmbeddings(model=_EMBEDDING_MODEL)
    return Chroma(
        collection_name=_COLLECTION_NAME,
        embedding_function=embedding_fn,
        persist_directory=_PERSIST_DIR,
    )


def _normalize_filter(raw_filter: Optional[Union[str, Dict]]) -> Optional[Dict]:
    """Chuẩn hóa tham số lọc thành format where_document của Chroma."""
    if raw_filter is None:
        return None
    if isinstance(raw_filter, str):
        return {"$contains": raw_filter}
    if isinstance(raw_filter, dict):
        return raw_filter
    return None


def _format_result(metadata: Dict, content: str) -> Dict:
    """Ghép metadata và page_content thành một dictionary kết quả."""
    output = dict(metadata)
    output["content"] = content
    return output


@tool
async def search_jobs(query: str, top_k: int = 5, where_document: Optional[Union[str, Dict]] = None) -> List[Dict]:
    """
    Tìm kiếm các bài đăng tuyển dụng phù hợp dựa trên câu query ngôn ngữ tự nhiên.
    Dùng tool này để tìm việc khớp với kỹ năng và kinh nghiệm của ứng viên.

    Args:
        query: Chuỗi tìm kiếm (ví dụ: "Senior Python Developer with AWS experience")
        top_k: Số lượng kết quả trả về (mặc định: 5)
        where_document: Filter tùy chọn cho nội dung document.
                        - Nếu truyền string, sẽ thực hiện tìm kiếm "$contains" (phân biệt hoa thường).
                        - Nếu truyền dictionary, sẽ được truyền thẳng làm Chroma `where_document` filter.
                          Có thể dùng logical operator như "$and" và "$or".
                          Ví dụ: {"$and": [{"$contains": "Remote"}, {"$contains": "Python"}]}
    """
    store = _get_vector_store()

    # Xây dựng search params
    search_params: Dict = {"k": top_k}
    doc_filter = _normalize_filter(where_document)
    if doc_filter is not None:
        search_params["where_document"] = doc_filter

    # Gọi similarity_search trên vector store
    matched_docs = await store.asimilarity_search(query, **search_params)

    # Format kết quả trả về cho agent
    return [_format_result(doc.metadata, doc.page_content) for doc in matched_docs]
```

### hr_agent_be.py

```
import uvicorn
import json
import base64
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from hr_agent import get_agent

app = FastAPI(
    title="Trợ Lý Tuyển Dụng AI",
    description="API hỗ trợ phân tích CV và gợi ý công việc phù hợp bằng AI Agent",
    version="1.0.0",
)

# Cho phép CORS khi phát triển local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Kiểm tra trạng thái hoạt động của server."""
    return {"status": "ok", "message": "Hệ thống đang hoạt động bình thường"}


@app.post("/find_jobs")
async def find_jobs(resume: UploadFile = File(...)):
    """
    Nhận file CV (PDF), phân tích và tìm kiếm công việc phù hợp.
    Trả về kết quả dạng Server-Sent Events (SSE) để cập nhật tiến trình realtime.
    """
    # Đọc và mã hoá PDF sang base64
    content = await resume.read()
    base64_pdf = base64.b64encode(content).decode("utf-8")
    file_size_kb = len(content) / 1024

    async def event_generator():
        agent = get_agent()
        print(f"🚀 Bắt đầu phân tích CV: {resume.filename} ({file_size_kb:.1f} KB)")

        # Gửi thông báo bắt đầu xử lý
        yield f"data: {json.dumps({'type': 'status', 'content': '📄 Đã nhận CV, đang bắt đầu phân tích...'})}\n\n"

        # Xây dựng message đa phương tiện (text + file)
        msg_content = [
            {
                "type": "text",
                "text": "Đây là CV của tôi. Hãy phân tích và tìm các công việc phù hợp nhất cho tôi.",
            },
            {
                "type": "file",
                "base64": base64_pdf,
                "mime_type": "application/pdf",
                "filename": resume.filename,
            },
        ]

        # Stream quá trình thực thi của agent
        async for chunk in agent.astream(
                {"messages": [{"role": "user", "content": msg_content}]},
                stream_mode="values",
        ):
            # Kiểm tra message mới nhất trong cuộc hội thoại
            if "messages" in chunk:
                latest_message = chunk["messages"][-1]

                # 1. Agent quyết định gọi tool (tìm kiếm việc làm)
                if hasattr(latest_message, "tool_calls") and latest_message.tool_calls:
                    for tool_call in latest_message.tool_calls:
                        tool_name = tool_call.get("name", "unknown")
                        yield f"data: {json.dumps({'type': 'status', 'content': f'🔍 Đang tìm kiếm việc làm ({tool_name})...'})}\n\n"

                # 2. Kết quả trả về từ tool
                elif latest_message.type == "tool":
                    yield f"data: {json.dumps({'type': 'status', 'content': '✅ Đã tìm thấy việc làm, đang phân tích mức độ phù hợp...'})}\n\n"

                # 3. Kết quả cuối cùng từ AI
                elif latest_message.type == "ai" and latest_message.content:
                    content = latest_message.content
                    yield f"data: {json.dumps({'type': 'result', 'content': content})}\n\n"

        # Kết thúc stream
        print(f"✅ Hoàn tất phân tích CV: {resume.filename}")
        yield f"data: {json.dumps({'type': 'done'})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run("hr_agent_be:app", host="0.0.0.0", port=8000, reload=True)```

### hr_agent_fe.py

```
import streamlit as st
import requests
import json

st.set_page_config(page_title="Trợ Lý Tuyển Dụng AI", page_icon="📄", layout="wide")

# ── Custom CSS — Dark Mode ──
st.markdown("""
<style>
    /* Background tổng thể */
    .stApp {
        background: #0F1117 !important;
    }

    /* Text mặc định */
    .stApp, .stApp p, .stApp span, .stApp li, .stApp label, .stApp div {
        color: #E5E7EB !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #F9FAFB !important;
    }

    /* Header badge */
    .ai-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid #22C55E;
        border-radius: 20px;
        padding: 5px 14px;
        font-size: 13px;
        color: #4ADE80 !important;
        font-weight: 500;
        margin-bottom: 12px;
    }
    .ai-badge::before {
        content: "";
        width: 8px;
        height: 8px;
        background: #22C55E;
        border-radius: 50%;
    }

    /* Tiêu đề lớn */
    .hero-title {
        font-size: 2.6rem;
        font-weight: 700;
        color: #F9FAFB !important;
        line-height: 1.2;
        margin-bottom: 8px;
    }
    .hero-title span {
        color: #FB923C !important;
    }

    /* Mô tả phụ */
    .hero-desc {
        font-size: 1.05rem;
        color: #9CA3AF !important;
        line-height: 1.7;
        margin-bottom: 24px;
    }
    .hero-desc strong {
        color: #F9FAFB !important;
    }

    /* Metric cards */
    .metric-row {
        display: flex;
        gap: 16px;
        margin-top: 28px;
        margin-bottom: 20px;
    }
    .metric-card {
        flex: 1;
        background: #1F2937;
        border: 1px solid #374151;
        border-radius: 16px;
        padding: 20px 16px;
        text-align: center;
    }
    .metric-card .value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #FB923C !important;
    }
    .metric-card .label {
        font-size: 0.75rem;
        color: #9CA3AF !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 4px;
        font-weight: 500;
    }

    /* Upload widget */
    [data-testid="stFileUploader"] {
        background: #1F2937 !important;
        border: 2px dashed #FB923C !important;
        border-radius: 16px !important;
        padding: 16px !important;
    }
    [data-testid="stFileUploader"] * {
        color: #E5E7EB !important;
    }
    [data-testid="stFileUploader"] section {
        background: #1F2937 !important;
    }
    [data-testid="stFileUploader"] button {
        background: #FB923C !important;
        color: #1A1A1A !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }
    [data-testid="stFileUploader"] button:hover {
        background: #F97316 !important;
    }
    [data-testid="stFileUploader"] small {
        color: #6B7280 !important;
    }
    /* File name after upload */
    [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"],
    [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] * {
        background: #111827 !important;
        color: #E5E7EB !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
    }

    /* Primary button */
    .stButton > button[kind="primary"] {
        background: #FB923C !important;
        color: #111827 !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 12px 32px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    .stButton > button[kind="primary"]:hover {
        background: #F97316 !important;
    }

    /* Status widget */
    .stStatus, .stStatus * {
        color: #E5E7EB !important;
    }

    /* LIVE indicator */
    .live-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #374151;
        color: #F9FAFB !important;
        border-radius: 20px;
        padding: 6px 14px;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid #4B5563;
    }
    .live-indicator::before {
        content: "";
        width: 8px;
        height: 8px;
        background: #EF4444;
        border-radius: 50%;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }

    /* Result cards */
    .result-card {
        background: #1F2937;
        border: 1px solid #374151;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
    }
    .result-card .job-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #F9FAFB !important;
        margin-bottom: 8px;
    }
    .result-card .score-badge {
        display: inline-block;
        border-radius: 12px;
        padding: 4px 12px;
        font-size: 0.85rem;
        font-weight: 700;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: #1F2937 !important;
        color: #E5E7EB !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
    }
    .streamlit-expanderContent {
        background: #111827 !important;
        border: 1px solid #374151 !important;
        border-top: none !important;
    }

    /* Success / Warning / Error / Info boxes */
    .stAlert {
        background: #1F2937 !important;
        border: 1px solid #374151 !important;
        color: #E5E7EB !important;
    }

    /* Divider */
    hr {
        border-color: #374151 !important;
    }

    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ──
col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.markdown('<div class="ai-badge">AI Career Coach · phục vụ 24/7 · phân tích chính xác</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-title">
            Tìm việc <span>nhanh hơn</span>,<br>
            chính xác hơn với AI.
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="hero-desc">
            Tải lên CV chỉ <strong>1 bước</strong>, được AI phân tích kỹ năng,
            so khớp với hàng trăm vị trí tuyển dụng và đề xuất
            <strong>Top 3 công việc phù hợp nhất</strong> — kèm gợi ý cải thiện.
        </div>
    """, unsafe_allow_html=True)

    # Metric cards
    st.markdown("""
        <div class="metric-row">
            <div class="metric-card">
                <div class="value">~30s</div>
                <div class="label">Phân tích CV</div>
            </div>
            <div class="metric-card">
                <div class="value">100+</div>
                <div class="label">Vị trí tuyển dụng</div>
            </div>
            <div class="metric-card">
                <div class="value">24/7</div>
                <div class="label">AI - Trợ lý AI</div>
            </div>
            <div class="metric-card">
                <div class="value">Top 3</div>
                <div class="label">Gợi ý phù hợp</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("<br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "📤 Tải CV của bạn lên (PDF)",
        type=["pdf"],
        help="Hỗ trợ file PDF, tối đa 10MB"
    )

    if uploaded_file:
        st.success(f"📎 **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔍 Phân tích & Tìm việc phù hợp →", type="primary", use_container_width=True):
        if not uploaded_file:
            st.warning("⚠️ Vui lòng tải lên CV trước.")
        else:
            status_container = st.empty()
            status_container.markdown('<div class="live-indicator">LIVE — Đang phân tích</div>', unsafe_allow_html=True)

            try:
                files = {"resume": ("resume.pdf", uploaded_file, "application/pdf")}
                response = requests.post(
                    "http://localhost:8000/find_jobs",
                    files=files,
                    stream=True,
                )
                response.raise_for_status()

                final_json = None

                for line in response.iter_lines():
                    if not line:
                        continue
                    line = line.decode("utf-8") if isinstance(line, bytes) else line
                    if line.startswith("data: "):
                        payload = line[6:]
                        try:
                            data = json.loads(payload)
                            msg_type = data.get("type")
                            content = data.get("content")

                            if msg_type == "status":
                                status_container.status(content, state="running")

                            elif msg_type == "result":
                                final_json = content
                                status_container.status("✅ Phân tích hoàn tất!", state="complete")

                            elif msg_type == "done":
                                break

                        except json.JSONDecodeError:
                            pass

            except requests.exceptions.ConnectionError:
                st.error("❌ Không thể kết nối tới server. Kiểm tra backend đã chạy (port 8000).")
                final_json = None
            except Exception as e:
                st.error(f"❌ Lỗi kết nối: {e}")
                final_json = None

# ── HIỂN THỊ KẾT QUẢ ──
if "final_json" not in dir():
    final_json = None

if final_json:
    st.markdown("---")
    st.markdown("### 🎯 Kết quả phân tích")

    try:
        if isinstance(final_json, str):
            final_json = final_json.replace("```json", "").replace("```", "").strip()
            matches = json.loads(final_json)
        else:
            matches = final_json

        if isinstance(matches, dict) and "matches" in matches:
            matches = matches["matches"]

        for idx, job in enumerate(matches, 1):
            score = job.get("match_score", 0)
            title = job.get("job_title", "Không rõ")

            if score >= 80:
                score_color = "#4ADE80"
                score_bg = "rgba(34, 197, 94, 0.15)"
            elif score >= 60:
                score_color = "#FB923C"
                score_bg = "rgba(251, 146, 60, 0.15)"
            else:
                score_color = "#F87171"
                score_bg = "rgba(248, 113, 113, 0.15)"

            st.markdown(f"""
                <div class="result-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div class="job-title">#{idx} — {title}</div>
                        <div class="score-badge" style="background: {score_bg}; color: {score_color}; border: 1px solid {score_color};">
                            Điểm: {score}/100
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            with st.expander(f"Xem chi tiết — {title}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    reasoning = job.get("reasoning") or job.get("reason") or job.get("explanation") or ""
                    if not reasoning:
                        # Fallback: ghép strengths thành lý do
                        strengths_list = job.get("strengths", [])
                        reasoning = "; ".join(strengths_list) if strengths_list else "Không có thông tin"
                    st.markdown(f"**📝 Lý do phù hợp:** {reasoning}")

                    strengths_raw = job.get("strengths", [])
                    if isinstance(strengths_raw, list):
                        st.markdown(f"**💪 Điểm mạnh:** {', '.join(strengths_raw)}")
                    else:
                        st.markdown(f"**💪 Điểm mạnh:** {strengths_raw}")
                with col_b:
                    missing = job.get("missing_skills", [])
                    if missing:
                        if isinstance(missing, list):
                            st.markdown(f"**📚 Cần bổ sung:** {', '.join(missing)}")
                        else:
                            st.markdown(f"**📚 Cần bổ sung:** {missing}")

                    tip = job.get("improvement_tips", "")
                    # Xử lý nếu tip vẫn là list (do parse JSON trước khi qua Pydantic)
                    if isinstance(tip, list):
                        tip = "; ".join(str(t) for t in tip)
                    if tip:
                        st.info(f"💡 {tip}")

                job_url = job.get("job_url", "")
                if job_url:
                    st.markdown(f"[🔗 Ứng tuyển tại đây →]({job_url})")

    except Exception as e:
        st.error(f"❌ Lỗi khi xử lý kết quả: {e}")
        st.code(final_json)
```

### job_crawls.py

```
import asyncio
import logging
from typing import Optional
from urllib.parse import urljoin
from webbrowser import Chrome

import chromadb
import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# URL tìm kiếm cơ sở (không bao gồm tham số trang)
BASE_SEARCH_URL = "https://www.google.com/about/careers/applications/jobs/results?location=Vietnam"
_CAREERS_ORIGIN = "https://www.google.com/about/careers/applications/"

_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ),
}

def _build_page_url(base_url: str, page_number: int) -> str:
    """Xây dựng URL cho từng trang kết quả tìm kiếm."""
    separator = "&" if "?" in base_url else "?"
    return f"{base_url}{separator}page={page_number}"



def _extract_links_from_html(html_content: str) -> set[str]:
    """Phân tích HTML và trích xuất các liên kết tuyển dụng hợp lệ."""
    parsed = BeautifulSoup(html_content, "html.parser")
    collected = set()
    anchor_elements = parsed.select("a[href*='jobs/results/']")
    for anchor in anchor_elements:
        raw_href = anchor.get("href", "")
        if raw_href:
            absolute = urljoin(_CAREERS_ORIGIN, raw_href)
            collected.add(absolute)
    return collected


def _extract_job_content(parsed: BeautifulSoup) -> str:
    """
    Trích xuất chỉ phần nội dung job posting từ HTML đã parse.
    Lấy các section: Job title, Minimum/Preferred qualifications, About the job, Responsibilities.
    Bỏ qua navigation, footer, EEO policy, social links...
    """
    content_parts: list[str] = []

    # Lấy tiêu đề job (thường nằm trong h2 đầu tiên sau "Job Details")
    job_title_tag = parsed.find("h2")
    if job_title_tag:
        content_parts.append(job_title_tag.get_text(strip=True))

    # Các section chứa nội dung job thực sự
    target_sections = [
        "Minimum qualifications",
        "Preferred qualifications",
        "About the job",
        "Responsibilities",
    ]

    for heading in parsed.find_all("h3"):
        heading_text = heading.get_text(strip=True).rstrip(":")
        if heading_text in target_sections:
            # Lấy tất cả nội dung giữa heading này và heading tiếp theo
            section_content = []
            sibling = heading.find_next_sibling()
            while sibling and sibling.name not in ("h2", "h3"):
                text = sibling.get_text(separator="\n", strip=True)
                if text:
                    section_content.append(text)
                sibling = sibling.find_next_sibling()
            if section_content:
                content_parts.append(f"\n{heading_text}:\n" + "\n".join(section_content))

    return "\n\n".join(content_parts)



def get_job_urls(base_url: str, pages: int = 5) -> list[str]:
    """
    Thu thập liên kết việc làm từ nhiều trang kết quả tìm kiếm.
    """
    all_links: set[str] = set()

    with httpx.Client(headers=_REQUEST_HEADERS, follow_redirects=True, timeout=15.0) as client:
        for page_idx in range(1, pages + 1):
            target_url = _build_page_url(base_url, page_idx)
            logger.info("Đang tải trang %d: %s", page_idx, target_url)

            try:
                resp = client.get(target_url)
                resp.raise_for_status()
            except httpx.HTTPStatusError as err:
                logger.warning("Lỗi HTTP %d ở trang %d – bỏ qua", err.response.status_code, page_idx)
                continue
            except httpx.RequestError as err:
                logger.error("Lỗi mạng ở trang %d: %s", page_idx, err)
                continue

            page_links = _extract_links_from_html(resp.text)
            all_links.update(page_links)
            logger.info("Trang %d thu được %d liên kết (tổng: %d)", page_idx, len(page_links), len(all_links))

    logger.info("Hoàn tất crawl – thu được %d URL việc làm từ %d trang", len(all_links), pages)
    return sorted(all_links)



async def _fetch_page_content(client: httpx.AsyncClient, url: str) -> Optional[Document]:
    """Tải nội dung một trang job posting và trích xuất phần mô tả công việc."""
    try:
        resp = await client.get(url)
        resp.raise_for_status()
    except (httpx.HTTPStatusError, httpx.RequestError) as err:
        logger.warning("Không thể tải %s: %s", url, err)
        return None

    parsed = BeautifulSoup(resp.text, "html.parser")

    # Loại bỏ script/style trước khi xử lý
    for tag in parsed(["script", "style"]):
        tag.decompose()

    # Trích xuất chỉ nội dung job, không lấy toàn bộ trang
    job_content = _extract_job_content(parsed)

    if not job_content.strip():
        # Fallback: nếu không parse được theo cấu trúc, lấy text thô nhưng loại bỏ nav/footer
        for tag in parsed(["nav", "footer", "header"]):
            tag.decompose()
        job_content = parsed.get_text(separator="\n", strip=True)

    if not job_content.strip():
        return None

    # Lấy title từ thẻ <title> hoặc từ h2 đầu tiên
    title_tag = parsed.find("title")
    title_text = title_tag.get_text(strip=True) if title_tag else ""

    return Document(
        page_content=job_content,
        metadata={"source": url, "title": title_text},
    )



async def _scrape_all_urls(urls: list[str], concurrency: int = 8) -> list[Document]:
    """Tải song song nhiều URL với giới hạn số lượng kết nối đồng thời."""
    semaphore = asyncio.Semaphore(concurrency)
    documents: list[Document] = []

    async def _bounded_fetch(url: str) -> Optional[Document]:
        async with semaphore:
            return await _fetch_page_content(client, url)

    async with httpx.AsyncClient(headers=_REQUEST_HEADERS, follow_redirects=True, timeout=20.0) as client:
        tasks = [_bounded_fetch(u) for u in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Document):
            documents.append(result)
        elif isinstance(result, Exception):
            logger.warning("Lỗi không mong đợi khi scrape: %s", result)

    return documents

async def ingest_jobs():
    """Thu thập mô tả công việc từ web và lưu vào ChromaDB."""
    logger.info("Bắt đầu quy trình thu thập dữ liệu việc làm...")

    # Bước 1: Thu thập danh sách URL việc làm
    job_urls = get_job_urls(BASE_SEARCH_URL, pages=5)

    if not job_urls:
        logger.warning("Không tìm thấy URL việc làm nào – dừng thu thập.")
        return

    logger.info("Đang tải nội dung từ %d URL đã thu thập...", len(job_urls))
    print(job_urls)

    # Bước 2: Tải nội dung các trang song song
    documents = await _scrape_all_urls(job_urls)

    if not documents:
        logger.warning("Không tải được tài liệu nào từ các URL.")
        return

    logger.info("Đã tải thành công %d tài liệu", len(documents))

    # Bước 3: Xóa collection cũ (nếu tồn tại) để tránh dữ liệu trùng lặp
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    existing_collections = [c.name for c in chroma_client.list_collections()]
    if "job_postings" in existing_collections:
        chroma_client.delete_collection("job_postings")
        logger.info("Đã xóa collection cũ 'job_postings'")

    # Bước 4: Tạo embeddings và lưu vào vector store mới
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma(
        collection_name="job_postings",
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    chunk_size = 15
    total_chunks = (len(documents) + chunk_size - 1) // chunk_size

    for chunk_idx in range(total_chunks):
        start = chunk_idx * chunk_size
        end = start + chunk_size
        chunk = documents[start:end]
        logger.info("Đang lập chỉ mục lô %d/%d (%d tài liệu)...", chunk_idx + 1, total_chunks, len(chunk))
        try:
            await vector_store.aadd_documents(chunk)
        except Exception as exc:
            logger.error("Lỗi khi lập chỉ mục lô %d: %s", chunk_idx + 1, exc)

    total_indexed = vector_store._collection.count()
    logger.info("Hoàn tất thu thập – %d tài liệu đã được lưu trong vector store.", total_indexed)


if __name__ == "__main__":
    asyncio.run(ingest_jobs())```

