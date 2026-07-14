---
source: yt-dlp-only (path 5, operator-submitted single video; NO NotebookLM)
video_id: K3UXUOJ3ac0
url: https://www.youtube.com/watch?v=K3UXUOJ3ac0
title: Hướng dẫn cài Skill "teach" và tạo lộ trình học theo năng lực
channel: Tự Học Cùng AI
upload_date: 2026-06-28
duration: 18:35
ingested: 2026-07-14
language: Vietnamese (vi-orig auto-captions)
tooling: yt-dlp --write-auto-sub --sub-lang vi-orig,vi,en --write-info-json; sed/grep/awk VTT-clean+dedupe (python3 denied under sandbox per prior session note)
---

# Hướng dẫn cài Skill "teach" và tạo lộ trình học theo năng lực

## Description (from info.json, VN original)

Bạn không biết bắt đầu học từ đâu, học cái gì, học như thế nào? Trong video này, mình hướng dẫn chi tiết cách cài đặt và sử dụng bộ Skill "teach" — một trợ lý AI giúp bạn học bất cứ chủ đề nào theo đúng năng lực của bản thân.

Khác với các khóa học đại trà (ai cũng học một nội dung như nhau), Skill "teach" cá nhân hóa bài học theo trình độ người học. Bạn càng học, dữ liệu càng nhiều, AI càng tạo ra bài học sát với năng lực của bạn nhất.

🔑 6 khái niệm cốt lõi của Skill "teach":
- Mission — Lý do & mục tiêu học, làm kim chỉ nam cho mọi bài học
- Lesson — Các bài học chính, được AI tạo theo mục tiêu của bạn
- Reference — Kiến thức đã đúc kết, tóm tắt lại để tham chiếu nhanh
- Learning Record — Ghi nhận tiến độ, điểm mạnh/yếu để cá nhân hóa bài tiếp theo
- Resource — Nguồn dữ liệu đầu vào (sách, tài liệu, link) để AI bám vào
- Note — Tùy chỉnh sở thích: độ dài, ngôn ngữ, văn phong, cách học

🧠 Triết lý 3 tầng học tập:
- Tầng 1 — Knowledge: Kiến thức từ các nguồn uy tín
- Tầng 2 — Skill: Thực hành qua bài tập để biến kiến thức thành kỹ năng
- Tầng 3 — Wisdom (Trí tuệ): Ứng dụng thực tế trong cộng đồng — tầng AI không làm thay được

🛠️ Trong video còn có:
- Demo cài đặt Skill "teach" vào Codex (dùng được cả tài khoản Free)
- Tạo project học "Tư duy hệ thống" và gọi skill
- Cơ chế lưu toàn bộ dữ liệu thành file → mở chat mới không mất tiến trình
- Tự động tạo bài học tiếp theo dựa trên kết quả bài trước

👉 Tải Codex tại trang chủ OpenAI để làm theo.

📌 Tham gia group "Tự học cùng AI" để nhận bộ skill và trao đổi thêm: facebook.com/groups/tuhoccungai (private Facebook group — the skill file itself is NOT publicly downloadable/linked; distribution is community-gated, not open-source)

#TựHọcCùngAI #SkillTeach #Codex #AIhọctập #HọcCùngAI

## Transcript (VN auto-captions, deduped; NOTE: auto-captions consistently mis-transcribe "Skill" phonetically as "skin" throughout — corrected to "Skill" in wiki articles per the description's own spelling)

Xin chào cả nhà. Hôm nay thì mình sẽ giới thiệu lại cũng như hướng dẫn chi tiết về cách sử dụng cái bộ skill mà hôm trước mình có chia sẻ lên group được học cùng AI.

Trước khi mà vào hướng dẫn chi tiết cụ thể thì mình sẽ chia sẻ qua một chút về cái bộ skill này nó là gì và tại sao chúng ta lại cần nó. Bây giờ thì trong cái thế giới phải gọi là hỗn loạn về mặt thông tin, chúng ta có rất là nhiều thứ mà chúng ta cần phải học thêm. Với những bạn nào mà có năng lực đào sâu nghiên cứu hoặc là tự tìm hiểu các cái nguồn trên mạng rồi đọc sách để tự học thì những bạn nào có năng lực đấy thì mình nghĩ là cũng không cần. Tuy nhiên thì với những ai mà chúng ta cần một trợ lý, cần một cái khung hướng dẫn giúp chúng ta học một cái nội dung nào đó một cách bài bản thì bộ skill này sẽ rất là có ích với mọi người. Chúng ta không biết bắt đầu từ đâu cả rồi nên học cái gì, học như thế nào. Đó thì bộ skill này sẽ hỗ trợ mọi người trong cái việc đó.

Thứ hai đó là cái bộ skill này ngoài cái việc là nó giúp cho chúng ta học về một cái gì đó, thay vì cái việc là lên các cái bài học là ai cũng như nhau thì cái bộ skill này nó sẽ giúp chúng ta customize theo đúng cái năng lực của người học. Chúng ta càng học với nó thì càng ngày AI và các dữ liệu mà chúng ta đã được thu thập nó sẽ càng nhiều, và lúc đấy thì những cái hướng dẫn hay là những cái bài học mà AI gen ra cho chúng ta nó sẽ càng sát với cái năng lực chúng ta nhất.

Phần thứ hai đó là phần liên quan đến các cái core concept — có nghĩa là với cái bộ skill này thì nó có những cái khái niệm nào là quan trọng nhất. Mình có liệt kê ra tất cả là có sáu cái khái niệm quan trọng nhất.

Đầu tiên là **Mission**. Mission là việc chúng ta đưa ra được cái lý do tại sao chúng ta lại muốn học cái kiến thức hay là kỹ năng đó. Khi chúng ta viết ra được cái đó, hoặc là nhờ AI viết cho chúng ta cái mission này, thì trong quá trình chúng ta học, những cái bài học của chúng ta sẽ được dựa vào cái nội dung này để nó gen ra sát với cái mục tiêu của chúng ta nhất.

Cái phần thứ hai là phần **Lesson**. Lesson là cái phần chính của chúng ta — các cái bài học mà AI gen ra cho chúng ta để chúng ta dần dần nắm bắt được cái kiến thức hay kỹ năng đấy. Cái này nó rất là đặc biệt bởi vì nó không phải là gen từ hư không. Nó dựa vào cái mission của chúng ta đã định nghĩa. Nó dựa vào những cái trải nghiệm học tập của chúng ta trong quá trình học. Nó dựa vào các cái nguồn mà chúng ta cung cấp là resource, và nó dựa vào các cái note, các cái chú thích thêm nếu có. Ví dụ như là tôi muốn học bằng tiếng Anh chẳng hạn hay tiếng Nhật thì chúng ta có thể note thêm. Thì toàn bộ những cái nguồn này nó sẽ là cái context, là cái đầu vào để cho AI dựa vào đó gen ra những cái bài học cho chúng ta. Đây gần như là cái rất là cốt lõi của cái bộ skill này. Nó sẽ giúp chúng ta học xuyên suốt chứ không phải là chỉ chat trong một cái luồng chat thôi là xong — sang luồng chat mới là mất. Chúng ta sang luồng chat mới chúng ta vẫn có đầy đủ các context để mà học tiếp.

Phần thứ ba là phần **Reference**. Reference là những cái nội dung mà đã được đóng gói, đúc kết lại từ bài học. Chúng ta tưởng tượng như đây là những cái nội dung được tóm tắt của bài học, để chúng ta có thể sau này tham chiếu lại hoặc là xem nhanh lại.

Phần thứ tư là phần **Learning Record**. Learning Record là cái phần mà trong quá trình chúng ta học thì chúng ta sẽ có bài tập. Trong lúc chúng ta làm bài tập đấy hoặc là hỏi đáp với AI thì AI nó sẽ tự nhận, nó ghi nhận những cái insight của chúng ta. Ví dụ như là cái độ khó của bài học nó như thế nào, những cái câu mà chúng ta hay sai nó như thế nào, để từ đấy nó làm đầu vào để nó tạo ra các cái lesson tiếp theo.

Phần thứ năm là **Resource** — là cái nguồn dữ liệu đầu vào. Nếu mà chúng ta không cung cấp thì nó sẽ dựa vào những cái mà AI nó biết. Nếu mà chúng ta cung cấp cái đầu vào có thể là một cuốn sách hay là một cái notebook chẳng hạn thì nó sẽ là những nguồn rất là tin cậy để mà gen ra những cái bài học cho chúng ta.

Phần cuối cùng là phần **Note**. Phần note là những cái chú thích về sở thích, về cách đọc, độ dài mỗi bài học hay là ngôn ngữ hay là văn phong. Cái này hoàn toàn là chúng ta có thể cá nhân hóa theo cái bài học của chúng ta — chúng ta có thể học theo kiểu là chơi game chẳng hạn.

Tiếp theo chúng ta sẽ đến với cái triết lý của cái bộ skill này — nó sẽ dạy chúng ta như thế nào. Bộ skill này được chia làm ba tầng.

Tầng thứ nhất là tầng **Knowledge** — đó là các cái kiến thức từ các cái nguồn uy tín mà chúng ta cung cấp, thì nó sẽ là tầng đầu tiên.

Tầng thứ hai là tầng **Skill**. Trong các cái bài học nó đều có những cái bài tập để chúng ta thực hành. Và từ những cái kết quả của cái bài tập đấy thì nó sẽ lại là cái dữ liệu đầu vào để tạo ra những cái bài sau tốt hơn. Nó có thể nhắc lại cái bài trước chúng ta đã học gì, nó có thể điều chỉnh lại độ khó hay là cách giải thích để cho phù hợp với năng lực của chúng ta.

Cái tầng thứ ba là cái tầng **Wisdom / Trí tuệ**. Đây là cái tầng mà AI nó không thể làm được. Nghĩa là với cái tầng trí tuệ này thì nó sẽ đề xuất cho chúng ta những cái nhóm hay những cộng đồng để chúng ta có cái nơi để thực hành thực tế. Từ đấy chúng ta sẽ có cái ứng dụng thực tế và đưa đến cái trải nghiệm sâu sắc nhất với cái kiến thức mà chúng ta đang học.

Đó là toàn bộ tổng quan về cái bộ skill này. Tiếp theo thì mình sẽ tiến hành demo về việc cài đặt skill cũng như là sử dụng thử để mọi người biết cái cách mà nó thực tế đang sẽ làm như thế nào.

Trong cái group Tự Học Cùng AI thì mình đã up cái folder skill lên rồi, mọi người có thể vào đây để download nó về. Hiện tại mình sẽ click vào để download cái bộ skill này về — mình sẽ để nó vào desktop. Rồi mình đã down về rồi. Đây là bộ skill đã được nén lại. Bây giờ mình sẽ giải nén nó ra — chúng ta sẽ có một cái folder. Trong đây nó sẽ có những cái file hướng dẫn của skill.

Bây giờ làm thế nào để cài đặt cái bộ skill này vào trong cái con AI của chúng ta? Trong lần này mình sẽ demo sử dụng **Codex** để mà cài đặt. Đây là cái giao diện Codex của mình. Để cài đặt cái bộ skill này cho Codex thì chúng ta phải biết cái chỗ để mà để cái bộ skill này cho nó phù hợp. Cái vị trí của cái bộ skill này nó sẽ nằm ở trong thư mục của user. Trong đây chúng ta sẽ có một thư mục ẩn là thư mục **.codex**. Chúng ta sẽ vào thư mục **.codex** này. Trong cái folder này nó sẽ có một cái thư mục là thư mục **skill**. Chúng ta sẽ kích vào đây — hiện tại chưa có skill nào cả. Bây giờ mình sẽ copy cái thư mục skill vào đây. Copy vào — đó là chúng ta đã hoàn thành cái việc cài đặt cái skill vào cho AI Codex.

Có một cái điểm chú ý đó là mọi người phải chú ý là trong cái thư mục Codex của chúng ta nó là thư mục ẩn. Cho nên là những anh chị nào mà không nhìn thấy thì có thể tìm cách để mà hiển thị cái thư mục ẩn lên. Với Mac OS thì chúng ta có thể giữ Shift + Command + . (dấu chấm) thì nó sẽ ẩn và hiện cái thư mục ẩn lên.

Rồi sau khi đã cài xong thì bây giờ mình sẽ tiến hành tạo một project để học. Lần này thì mình sẽ demo về việc học về **tư duy hệ thống**. Mình sẽ tạo một folder ở local này — học về tư duy hệ thống. Rồi mình đã tạo cả một project trên Codex để học tư duy hệ thống. Chúng ta sẽ thấy phần dưới này nó có cái chỗ chọn project, chúng ta phải để ý là chỗ này nó phải là project học về tư duy hệ thống.

Rồi tiếp theo thì mình sẽ gọi skill lên. Gọi skill ở bên phía Codex thì chúng ta sẽ dùng dấu **$** (đô la). Mình sẽ gọi skill này đi — "giúp tôi học về tư duy hệ thống". Hoàn toàn là đây là mình chat rất là đơn giản thôi. Hoàn toàn mọi người có thể ném một cái file dữ liệu hay là link mà mọi người muốn học vào, một cuốn sách nào đó.

Để sử dụng được Codex thì mọi người nên vào trang chủ của ChatGPT/OpenAI để có thể down về. Chúng ta hoàn toàn có thể sử dụng với cả tài khoản **free**. Hiện tại mình cũng đang sử dụng tài khoản free thôi, không phải là tài khoản Pro, không phải tài khoản trả phí. Tất nhiên là sẽ có giới hạn sử dụng, cho nên là những ai mà sử dụng nhiều thì chúng ta nên đăng ký gói subscription hàng tháng.

Bây giờ thì đang nó kiểm tra cái thư mục của chúng ta là chưa có mission. Cho nên là đầu tiên nó sẽ cần mình phải đưa ra cái mission — nghĩa là chúng ta học cái tư duy hệ thống này để làm gì. Nó có gợi ý cho chúng ta. Thì bây giờ mình sẽ tạo thử — "áp dụng quản lý đội nhóm... học kiểu phân tích ngắn cộng bài tập." Mọi người có thể ghi chi tiết hơn, trong demo thì mình sẽ không ghi quá chi tiết.

Với bài đầu tiên nó sẽ lấy nguồn là từ của **Donella Meadows** cho khái niệm hệ thống — điểm đòn bẩy (leverage points). Hiện tại nó đang đi thu thập thông tin để tạo ra bài học cho chúng ta. Rồi hiện tại nó đang ghi mission rồi. Ta sẽ xem mission này — chưa có gì. Chúng ta có thể mở panel bên phải ra, chọn file thì nó sẽ hiển thị ra toàn bộ các cái file ở trong folder của chúng ta. Chúng ta đợi một chút để cho nó tạo file. Chúng ta thấy nó đang tạo file mission này, file note này và file resource này.

Hiện tại thì bài học đầu tiên đã được tạo. Hiện tại đang kiểm tra lại cấu trúc file cho chúng ta. Rồi file đã được tạo. Giờ chúng ta quay lại Codex xem nó đã tạo cho chúng ta những file nào. Chúng ta sẽ thấy là nó tạo cho chúng ta đầu tiên là file **mission**. File mission này là gì? Tại sao, vì sao? Thành công trông như thế nào, ràng buộc và ngoài phạm vi. "Tôi muốn học tư duy hệ thống để quản lý đội nhóm tốt hơn. Nhìn ra vì sao một vấn đề lặp lại, tránh phá triệu chứng, và chọn can thiệp nhỏ nhưng có tác dụng bền. Việc học cần gắn với tình huống quản trị thật, không chỉ lý thuyết." Đó thì đây nó chính là cái tuyên bố là chúng ta học cái này để làm gì. Từ đó xuyên suốt khi mà tạo bài học nó sẽ dựa vào cái mission này để tạo cho chúng ta.

**Note**: "người học muốn áp dụng tư duy hệ thống qua đội nhóm, phong cách học muốn bài ngắn kèm bài tập, ưu tiên tình huống quản trị thật, có vòng phản hồi, tránh lý thuyết giả."

**Resource**: đây là các cái resource mà nó sử dụng để dạy cho chúng ta — nguồn để gen bài học cho chúng ta. Cuốn rất là nổi tiếng đó — "Thinking in Systems" của Donella Meadows, rồi cũng của Donella Meadows luôn là "Leverage Points" (điểm đòn bẩy) — vòng phản hồi cấu trúc của các cái vòng nhân quả, rồi cẩm nang thực hành systems thinking. Đây là các cái tài liệu mà nó sẽ dựa vào để gen ra cho chúng ta.

Bây giờ chúng ta sẽ xem luôn cái bài 1. Mình sẽ kích vào đây sẽ ra bài 1 cho mình luôn — "Nhìn vấn đề đội nhóm như vòng phản hồi." Mục tiêu bài này: khi thấy một vấn đề lặp lại trong đội, bạn biết hỏi vòng nào đang tự tạo ra nó trước khi vội sửa từng triệu chứng. Có ý chính, vòng phản hồi thường gặp, kiểm tra nhanh. Rồi có cả bài tập. Sau khi kết thúc bài chúng ta có một bài **tham chiếu nhanh** (Reference) — sơ đồ nhân quả, tham chiếu nhanh bốn thành phần, hai loại vòng.

Thì chúng ta sẽ học theo đúng cái hướng dẫn này. Chúng ta đọc kiến thức ở đây, làm bài tập — "Trong vòng trên, điểm can thiệp nào có tính hệ thống nhất? Nhắc đội cố gắng hơn? Tăng số lần báo cáo? Tạo nhịp tự điều phối?" Nhắc đội thế này không phải rồi. Tăng số lần báo cáo cũng không phải. Tự tạo nhịp tự điều phối — cái này đúng. Rồi bài tập 7 phút.

Trong quá trình này chúng ta hoàn toàn có thể hỏi thêm về các cái kiến thức ở trong đây — ví dụ "vòng lặp phản hồi là gì?" Có bất cứ câu hỏi nào chúng ta có thể hỏi thêm vào đây. Và khi kết thúc thì chúng ta sẽ nói "kết thúc bài học 1". Và một điểm hay là chúng ta hoàn toàn có thể mở một cái chat mới, bởi vì các cái dữ liệu của chúng ta đã đều được lưu thành file hết rồi. Cho nên là khi chúng ta mở cái chat mới chúng ta cũng không bị mất.

Chúng ta có thể tạo bài 2 — "tiếp tục bài 2" — và nó sẽ kiểm tra lại cái tình trạng hiện tại của chúng ta, chúng ta đang học đến đâu rồi, để nó đưa ra cái gợi ý hay là bài học tiếp theo cho phù hợp nhất. Chúng ta mở nó bằng Chrome — "đặt tên biến và gắn dấu quan hệ" — cũng có kiểm tra, cũng có bài tập. Và trong quá trình học thì toàn bộ những cái nội dung này nó sẽ được lưu hết lại thành file và được dùng để làm context, làm nội dung để mà gen ra các bài tiếp theo. Rất là trực quan và rất là hay.

Sau cái video này thì mình đã giới thiệu cho mọi người cái cách mà chúng ta cài đặt cái bộ skill "teach" cũng như là sử dụng nó như thế nào. Mình thấy là cái bộ skill này sẽ rất là hay và rất là hữu dụng cho anh chị cho những ai mà mong muốn học thêm cái gì đó mà chúng ta đang không biết bắt đầu từ đâu, không biết bắt đầu như thế nào. Chúng ta sẽ có một trợ lý hỗ trợ chúng ta trong cái việc học những cái kiến thức mới. Xin cảm ơn cả nhà.

---

## Transcript editor's notes (garble corrections made against the info.json description, not fabricated)

- Auto-captions consistently render "Skill" (Skill) as "skin" — corrected throughout using the video's own description text as ground truth ("bộ Skill 'teach'").
- Auto-captions render "Donella Meadows" as "Donelamedo" / "Donan Mido" and "leverage points" ("điểm đòn bẩy") as "điểm đoàn 7" / "điểm đoàn bảy" — corrected against the well-known public attribution (Donella Meadows, *Thinking in Systems: A Primer* + the "Leverage Points: Places to Intervene in a System" essay); flagged for independent verification in the compile workflow rather than assumed.
