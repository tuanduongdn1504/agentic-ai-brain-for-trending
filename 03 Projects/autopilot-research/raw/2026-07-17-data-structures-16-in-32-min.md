# RAW — Tất Tần Tật Về Cấu Trúc Dữ Liệu Trong 32 Phút (16 Data Structures in 32 Minutes)

- **Source:** https://www.youtube.com/watch?v=uHpzKcm8qh0
- **Channel:** Học Giải Thuật Cùng HPN (Learning Algorithms with HPN)
- **Uploaded:** 2026-07-12 · **Duration:** 32:22 · **Views:** ~15,034 (at ingest 2026-07-17)
- **Language:** Vietnamese · **Ingest path:** 5 (yt-dlp `--write-auto-subs vi-orig` → VTT → deduped clean text, read in main loop)
- **Ingested:** 2026-07-17 · operator-submitted anchor URL
- **Captions:** `vi-orig` original auto-captions (301KB raw VTT → 715 deduped lines / ~27KB clean)
- **Subject:** 16 classic data structures, each with Big-O + historical origin (inventor + year) + a closing task→structure selection framework.

Structures covered (in order): array, linked list, stack, queue, hash table, binary search tree (BST), AVL tree, red-black tree, heap, graph (+ BFS/DFS traversal), trie, union-find (disjoint-set), skip list, bloom filter, B-tree, LSM-tree.

---

## Cleaned transcript (vi-orig, deduped)

Rồi xin chào các bạn nha. Trước khi vào
video hôm nay các bạn thử tưởng tượng
cái này một chút đã. Ngay trong cái điện
thoại đang cầm hay cái máy tính đang mở
trước mặt có hàng tỷ mẩu thông tin nằm
giải khắp trong đó. Tên người quen ảnh
chụp hôm trước, từng dòng tin nhắn, từng
con số để lộn xộn hết không theo trật tự
nào thì muốn tìm một thứ trong đó cũng
phải dò qua từng cái một. Nhưng nó không
để như vậy. Ngay từ đầu đống đó đã được
xếp vào những khuôn nhất định. Có lúc
dàn thành một hàng ngay ngắn. Ô này nối
liền ô kia, có lúc nối lại thành một
chuỗi, cái sau móc vào cái trước, có lúc
chia nhánh ra như một cái cây, từ một
gốc tỏa ra từng nhánh con, có lúc lại
răng ra thành một mạng, chỗ nào cũng bắt
được qua chỗ khác. Những cái khuôn đó
người ta gọi chung một cái tên đó là cấu
trúc dữ liệu. Và cả video này từ đầu tới
cuối sẽ đi qua gần hết những khuôn đó.
từ cái cơ bản nhất cho tới mấy cái chỉ
dần viết code lâu năm mới hay đụng tới.
Giờ thì bắt đầu từ cái cơ bản nhất trước
đã nhé.
Quay [âm nhạc] lại với mấy cái khuôn lúc
nãy nói tới, mảng, chuỗi, cây, mạng, mỗi
cái là một cách xếp dữ liệu khác nhau.
Nhưng xếp kiểu nào cũng được. Vậy lấy gì
ra so xem kiểu nào nhanh hơn kiểu nào.
Về ta không đo bằng dây vì máy nhanh máy
chậm mỗi nơi một khác. Đo dây xong đem
so với nhau chẳng có nghĩa gì cả. Cái
người ta đo là dữ liệu tăng ngưng gấp
đôi gấp 10 thì thời gian xử lý phình ra
nhanh cỡ nào. Cái thước đo đó có tên
riêng viết tắt bằng chữ O. Ví dụ nói một
cách tìm kiếm là ON nghĩa là dữ liệu
tăng gấp đôi thì thời gian tìm cũng tăng
gấp đôi theo. Còn Olog N thì dữ liệu
tăng gấp đôi, thời gian chỉ nhích thêm
một chút thôi. Chữ O này cũng không phải
mình đặt ra đâu. Nó xuất hiện từ năm
do một nhà toán học người Đức tên Paul
Bman viết ra. Sau đó Edmund Landow viết
thêm vào năm 1909. Còn người mang nó qua
ngành máy tính [âm nhạc] dùng để đo tốc
độ thuật toán là Donal Knut vào khoảng
thập niên 1970.
Giờ nhìn mấy đường cong này, O1 là đường
phẳng lì, dữ liệu tăng bao nhiêu cũng
không ảnh hưởng gì tới thời gian tìm. O
log N thì tăng rất chậm, ON tăng đúng
theo một đường thẳng. Còn ON bình phương
[âm nhạc] chỉ cần dữ liệu tăng gấp đôi
thôi, thời gian đã vọt lên gấp 4. Nhớ
mấy ký hiệu này thôi, không cần nhớ công
thức toán đằng sau nó. Cứ mỗi lần nói
tới một cấu trúc dữ liệu, video sẽ nhắc
lại nó nhanh cỡ nào bằng đúng mấy chữ
này. Giờ bắt đầu đi vào cái đầu tiên
nhá, đó là mản.
Lùi lại một chút. Nhìn nguyên 70 năm cấu
trúc dữ liệu đi qua những mốc nào nhé.
Năm 1945, ông V Newman viết một báo cáo
mô tả bộ nhớ máy tính đánh số liên tục
từng ô một. Gốc của mảng nằm ở đó.
Năm 1953, Hans Peter Lun ở IBM viết một
ghi chú nội bộ đề xuất chia dữ liệu vào
từng ngăn theo một phép tính riêng. Bảng
băm ra đời từ đó. Năm 1955, Bower với
Samelson ở Mich đề xuất nguyên tắc xếp
trồng lên nhau cấp bằng sáng chế năm
1957. Năn xếp bắt đầu thành hình. Cũng
năm đó, ba người ở Range là Newwell,
Shaw, [âm nhạc] Simon nối từng màu dữ
liệu lại bằng con trỏ. Danh sách liên
kết ra đời năm 1959 rồi 1960, cấu trúc
rẽ nhánh theo từng ký tự cũng xuất hiện
được đặt tên là Try. Năm 1962, Ederson
Velski với Landis cho ra cây tự cân bằng
đầu tiên trong lịch sử. Năm 1964,
Williams giới thiệu Hip. Cùng năm,
Galler với Fisher công bố cách cuộc
nhanh các nhóm rời dạc lại với nhau. Năm
1970, Blue nghĩ ra cách kiểm tra một
phần tử [âm nhạc] chỉ cần một giải buý
rất nhỏ. Cũng năm đó, Bayer với Marry
bắt đầu xây cây B công bố chính thức năm
1972.
Cũng chính Bayer năm 1972 đặt nền cho
một cây khác nữa được Gibass với Swig
đặt lại tên năm 1978
là cây đỏ đen. Năm 1990 Pe công bố Skip
list thêm hẳn mấy làn nhanh phía trên
một danh sách liên kết bình thường. Năm
1996 nhóm O'Neil công bố LSM3 cách ghi
dồn lớp giờ nằm bên trong hầu hết hệ
thống lưu chữ quy mô lớn.
Người nấy mốc thời gian cách nhau hàng
chục năm, giờ đứng chung trong một
video. Giờ chúng ta quay lại từ cái ra
đời sớm nhất là mảng nhé.
Mảng [âm nhạc] cái tên vừa lướt qua ở
bảng mốc thời gian lúc nãy. Giờ phân
tích kỹ ra xem nó hoạt động thế nào nhé.
Mảng là một dãy ô nhớ nằm sát nhau, ô nọ
liền ô kia. Mỗi ô có một địa chỉ riêng.
Y hệt cách bộ nhớ được đánh số trong báo
cáo của V Newman năm 1945 [âm nhạc]
vừa nhắc ở cảnh trước. Có một điểm dễ
nhầm mà mình cần nói rõ trước là mảng
đếm vị trí bắt đầu từ số 0 chứ không
phải từ số 1. Ô đầu tiên là vị trí số 0.
Ô tiếp theo là vị trí số 1. Cứ thế giờ
muốn lấy ô ở vị trí số bốn tức là ô thứ
năm nếu đếm từ đầu. Máy không cần dò lần
lượt qua từng ô một để tới đó. Địa chỉ ô
đó tính được ngay. Lấy địa chỉ gốc cộng
với bốn lần kích thước một ô, một phép
tính ra ngay. Đây chính là O1 nhắc ở
cảnh big âu. Nhưng chèn thêm một phần tử
vào giữa dãy thì khác hẳn. Ô sau phải
nhường chỗ cho ô mới, kéo theo ô sau nữa
cũng phải dịch chuyển, cứ thế tới hết
dãy. Chèn một chỗ động vào gần như toàn
bộ. Đây là oni gọn lại là mảng cực nhanh
khi lấy đúng một phần tử theo vị trí.
Nhưng chậm khi cứ phải nhét thêm, rút
bớt ở giữa liên tục. Cũng vì cái chậm
đó, người ta mới nghĩ ra một cách khác
để nối dữ liệu lại, không cần nằm sát
nhau nữa. Chúng ta sang cấu trúc tiếp
theo thôi.
Câu hỏi để lại cuối cảnh trước đó là
không nằm sát nhau nữa thì nối kiểu gì?
Câu trả lời nằm ở danh sách liên kết.
Quay lại năm 1955-156,
ba người ở Rand Corporation là Newwell,
Shaw, Simon đang cần một cách lưu dữ
liệu để chạy một chương trình khá đặc
biệt là chương trình đầu tiên tự chứng
minh định lý toán học tên là Logic
Theory Machine. Từ đó, danh sách liên
kết ra đời. Ý tưởng đó khác hẳn mảng.
Mỗi phần tử giờ gọi là một nút gồm hai
phần, dữ liệu [âm nhạc] và một con trỏ
chỉ sang nút kế tiếp. Các nút không cần
nằm sát nhau trong bộ nhớ nữa, chỉ cần
con trỏ chỉ đứng chỗ là đủ. Vậy nên chen
một nút mới vào đầu danh sách cực nhanh,
chỉ cần đổi một con trỏ là xong ngay.
Nhưng muốn lấy phần tử thứ năm thì không
tính địa chỉ trực tiếp được như mảng
nữa. Phải đi từ nút đầu qua từng nút một
tới đúng nút cần tìm. Độ phức tạp lên
honor. Có phiên bản thì chỉ nối một
chiều, biết nút sau chứ không biết nút
trước gọi là danh sách liên kết đơn. Có
phiên bản nối hai chiều, mỗi nút vừa
biết nút sau vừa biết nút trước. đi tới
đi lui đều được, gọi là danh sách liên
kết đôi. Sự đánh đổi ở đây rõ ràng đó là
nó mất khả năng tính địa chỉ tức thời
đổi lại chen xóa ở đầu danh sách gần như
miễn phí. Nhưng nối tự do kiểu này lại
không theo một cái quy luật nào cả. Muốn
vào lúc nào cũng được, muốn ra lúc nào
cũng được. Cấu trúc tiếp theo đặt hẳn
một quy luật riêng cho việc đó.
Phân nhắc ở cuối cảnh trước gọi là ngăn
xếp. Quy luật của nó chỉ đúng một câu,
cái nào vào sau thì ra trước. Ý tưởng
này được manh nha từ trước. Chính Alan
Churing từng nhắc tới bằng một cặp thuật
ngữ riêng của ông nhưng chưa thành hình
rõ ràng. Phải tới năm 1955, hai người ở
Đại học kỹ thuật Minion là Bauer với
Sion mới đặt hẳn thành một nguyên tắc
tiếng Đức gọi là Kor Princip. Dịch nôm
na là nguyên tắc dưới hầm được cấp bằng
sáng chế năm 1957. Tưởng tượng một trồng
đĩa trong [âm nhạc] quán ăn, đĩa rửa
xong đặt lên trên cùng. Đĩa lấy ra dùng
cũng lấy từ trên cùng xuống, không ai
chọc tay vào giữa trồng đĩa để rút một
cái ra cả. Trong máy tính, mỗi lần gọi
thêm một hàm, một khoảng nhớ mới lại đặt
lên trên khoảng nhớ của hàm gọi nó. Gọi
lồng nhau bao nhiêu lớp thì trồng lên
bấy nhiêu lớp. Và hàm nào chạy xong
trước? Đúng là hàm được gọi sau cùng, ở
lớp trên cùng. Kết thúc trước tiên, y
hệt cái đĩa trên cùng luôn được lấy ra
trước. Thêm một phần tử gọi là push đặt
thẳng lên đỉnh. Lấy ra gọi là pop cũng
chỉ đúng đỉnh đó. Chỉ động vào một chỗ
duy nhất nên push với pop luôn là O1,
không quan tâm trồng đang cao hay thấp.
Nút Andu trong trình soạn thảo cũng chạy
y hệt kiểu này. Gõ thêm vài chữ, vài
trạng thái mới lại trồng lên trên. Bấm
undu trạng thái mới nhất bị lấy ra
trước, nó lùi đúng một bước gần nhất,
không phải bước nào khác cả.
Nhưng quy luật vào sau ra trước này
không phải lúc nào cũng hợp lý. Nếu có
việc cần thì phải làm ngược hẳn lại. Ví
dụ ai đứng xếp hàng trước phải được phục
vụ trước.
Rồi cái cấu trúc mà xếp hàng trước được
phục vụ trước ấy gọi là hàng đợi. Nó
hoạt động ngược hẳn với ngăn xếp. Ngăn
xếp thì đứa vào sau thì ra trước. Hàng
đợi thì đứa vào trước thì ra trước. Y
hệt cảnh xếp hàng chờ tới lượt. Ai đứng
đầu hàng thì được giải quyết trước. Ai
mới tới thì đứng cuối thì phải đợi. Phần
tử mới luôn vào ở một đầu gọi là rear.
Phần tử được xử lý luôn lấy ra ở đầu kia
gọi là front. Vào ở rear còn ra thì ở
front. Không đảo ngược không chen ngang
giữa hàng. Một ứng dụng của hàng đợi mà
thấy ngay trong máy tính là hàng đợi
[âm nhạc] lệnh in. Tài liệu gửi in trước
thì in trước gửi sau xếp hàng chờ. Hay
việc xử lý tác vụ trong hệ điều hành.
Tác vụ nào tới trước được xử lý trước,
không nhảy cóc. Vào cũng như ra đều chỉ
động vào đúng một đầu tương ứng, không
phải dò qua phần tử nào khác nên cả hai
thao tác đều là O1. Có một bản mở rộng
khác nữa là cho phép vào ra ở cả hai đầu
luôn gọi là Deek, không còn giữ nguyên
tắc một chiều cứng nhắc nữa mà linh hoạt
cả hai phía luôn. Ngăn xếp với hàng đợi
coi vậy chứ không chỉ nắm yên làm nền
tảng suông đâu. Lát nữa khi đi vào duyệt
một mạng lưới các bạn sẽ thấy chính hai
đứa này đứng sau điều khiển toàn bộ cách
dượt. Đấy,
cái chuyện duyệt mạng lưới từ từ. Khoan
để đó đã. Quay lại một câu hỏi cũ hơn là
việc tra cứu theo một cái tên, một cái
khóa bất kỳ chứ không phải theo số thứ
tự thì làm sao cho nhanh cơ nhỉ? Vào
tháng 1 năm 1953, một người ở IBM tên
Hans Peter Loon viết một ghi chú nội bộ
đề xuất một cách là đưa dữ liệu vào từng
ngăn riêng. Ngăn nào và ngăn đó được
tính sẵn từ chính cái khóa, không cần dò
tuần tự. Bảng băm ra đời từ ghi chú đó.
Cách hoạt động là ta đưa khóa qua một
phép tính gọi là hàm băm. Nó ra ngay một
con số. Cái con số đó chính là vị trí
ngăn cần tới. Không phải dò từ ngăn một
ngăn hai mà nó tính một lần là biết luôn
ngăn nào. Đây lại là một dạng O1 khác
giống mảng ở cảnh trước ấy. Nhưng lần
này tra theo khóa bất kỳ chứ không phải
theo số thứ tự liền nhau. Ví dụ nhá, đưa
một khóa như user 2.1024
qua hàm băm, nó ra thẳng một chỉ số
ngăn. Khóa rơi đúng ngăn đó, nó sáng lên
một cái xong luôn. Nhưng hai khóa khác
nhau hoàn toàn, vẫn có thể rơi chúng
cùng một ngăn gọi là va chạm. Cách xử lý
phổ biến nhất là nối các khóa trùng ngăn
lạng bằng một danh sách liên kết ngay
tại ngăn đó. Cái này đúng cấu trúc vừa
học ở phần trước, giờ ta dùng lại luôn.
Có một cách khác nữa, không nối thêm gì
cả mà nếu ngăn đã có người ở, cứ dò sang
ngăn kế bên, ngăn nào trống thì đặt vào
đó. Hàm băm tốt thì va chạm hiếm khi xảy
ra, tra cứu gần như luôn nhanh. Nhưng
bảng băm có một cái thiếu là nó không
giữ thứ tự nào của dữ liệu cả. Muốn dữ
liệu luôn có thứ tự phải sang một cấu
trúc khác.
Cái cấu trúc khác đó là cây tìm kiếm nhị
phân. Quy luật của nó cũng chỉ đúng một
thứ là mỗi nút có tối đa hai nhánh con.
Nhánh trái luôn chứa giá trị nhỏ hơn nút
tra. Nhánh phải luôn chứa giá trị lớn
hơn nút tra. Đúng luật này lặp lại ở mọi
nút không có ngoại lệ. Tìm một giá trị
bắt đầu từ gấp. Giá trị cầm tìm nhỏ hơn
nút hiện tại thì rẽ [âm nhạc] trái, lớn
hơn thì rẽ phải. Cứ so sánh rồi rẽ như
vậy. Mỗi lần rẽ là loại bỏ hẳn một nửa
số nhánh còn lại, không cần nhìn tới
nữa. Ví dụ tìm giá trị 40 nhé. Gốc là
50, 40 nhỏ hơn nên rẽ trái. Gặp 30 40
lớn hơn nên rẽ phải. Gặp đúng 40 thì
dừng lại. Ba lần so sánh xong. Trong khi
nhánh bên phải gốc coi như không lúc
tới. Nếu cây chia đều hai bên như vậy,
mỗi lần rẽ bỏ được một nửa, tốc độ tìm
là O log N, rất nhanh. Nhưng nếu chèn dữ
liệu theo đúng thứ tự tăng dần 10, 20,
30, 40, 50, cây sẽ không chia nhánh gì
cả. Mỗi nút chỉ có đúng một nhánh phải
xếp thẳng xuống như một cái đuôi, nhìn
chẳng khác gì danh sách liên kết lúc
nãy. Lúc này tốc độ tìm kiếm lại tụt về
ON cùng một cấu trúc, mà một cách chèn
cho tốc độ cực nhanh, cách khác lại kéo
về chậm như cũ. Phần sau sẽ sửa đúng cái
chỗ này.
Phần trước để lại một vấn đề đó là chèn
dữ liệu theo đúng thứ tự, cây tự biến
thành một cái đuôi thẳng đơ chậm y như
chưa từng có cây gì cả. Giờ ta sửa đúng
chỗ đó. Năm 1962, hai người Liên Xô là
Adamson Velski với Landis công bố cách
sửa đầu tiên trong lịch sử. Sau mỗi lần
chèn, cây tự kiểm tra bên nào cao hơn
bên kia quá một bậc thì tự xoay
[âm nhạc] lại cho cân. Gọi là cây AVL
lấy từ chữ cái đầu tên của hai ông. Ví
dụ trên liền ba giá trị 10, 20, 30. Nếu
cứ để yên chúng xếp thẳng xuống một hàng
y hệt cái đuôi ở cành trước. Nhưng cây
AVL phát hiện ngay độ lệch. Nó xoay một
cái, 20 lên làm gốc, 10 với 30 cách sang
hai bên. Chỉ một lần xoay, cây nó cân
lại ngay. 10 năm sau, vào năm 1972, một
người Đức tên Rudolph Bayer nghĩ ra một
cách khác để giữ cân bằng. Ông gọi nó là
cây b nhị phân đối xứng. 6 năm sau nữa,
mới năm 1978, Leonidas Gibas với Robert
Squck làm việc tại Serox SPK dựng lại
cấu trúc đó và đặt cho nó một cái tên
mới tên là cây đỏ đen. Lý do chọn màu đỏ
nghe khá là đời thường thôi, đó là vì
cái máy in laser màu ở chỗ họ làm việc
lúc đó in màu đỏ cạnh nền đen là đẹp
nhất. Mỗi nút trong cây giờ mang đúng
một trong hai màu đỏ hoặc đen theo một
bộ luật riêng, không còn so chiều cao
như cây AVL nữa. Quy luật đơn giản thôi,
gốc luôn phải đen. Một nút đỏ thì không
được có nút con cũng đỏ và đi từ gốc
xuống bất kỳ chỗ trống nào, số nút đen
trên đường đi phải bằng nhau hết. Giữ
đúng ba luật này, cây không bao giờ suy
biến thành cái đuôi nữa. Hai cây hai
cách giữ cân bằng khác nhau nhưng cùng
chung một mục đích đó là không để chuyện
suy biến ở cảnh trước lặp lại. Cấu trúc
tiếp theo [âm nhạc] lại quay về hình
dạng cây nhưng phục vụ một việc khác hẳn
đó là luôn biết ngay ai đang đứng đầu.
Nay phần trước mình có nhắc là một cái
cấu trúc luôn biết ai đứng đầu. Đúng thứ
ta cần bây giờ. Một cấu trúc lúc nào
cũng biết ngay phần tử lớn nhất hay nhỏ
nhất đang nằm ở đâu. Năm 1964, một người
tên Williams công bố một thuật toàn sắp
xếp đăng trên tạp chí của ACM gọi là
Algorithm 232 Hip Sort. Cùng lúc đó, ông
giới thiệu luôn cấu trúc đứng sau thật
toán này gọi là Hip. Cũng năm đó, Floyd
nghĩ ra cách giận hip nhanh hơn nữa. Hip
là một cây gần như đầy kín, tầng nào
cũng lấp hết trước khi qua tầng tiếp
theo. Luật của nó là mỗi nút cha luôn
lớn hơn hoặc bằng hai nút con gọi là Max
Hip. Và vì cây lúc nào cũng đầy kín kiểu
này, toàn bộ cây lại nhét gọn được vào
một mảng. Y hệt cấu trúc ở cảnh nói về
mảng lúc trước. Nút thứ y, con trái nằm
ở 2y + 1, con phải nằm ở 2y + 2. Thêm
một giá trị mới, đặt hẳn vào cuối mảng
trước rồi so với cha, cha nhỏ hơn thì
đổi chỗ, cứ thế đi ngược lên gốc tới khi
cha lớn hơn thì dừng. Gọi là shift up.
Lấy phần tử lớn nhất ra chính là gốc.
Gốc rời đi, phần tử cuối mảng được kéo
lên thay vào gốc. Rồi so với hai con,
con nào lớn hơn thì đổi chỗ, cứ thế đi
xuống. tới khi cha lớn hơn cả hai con
thì dừng gọi là shift [âm nhạc] down.
Nhờ vậy dù nhét bao nhiêu phần tử vào
theo thứ tự lộn xộn cỡ nào Hip vẫn luôn
trả lời được ngay là phần tử ưu tiên cao
nhất đang nằm đúng ở gốc rồi. Cái cấu
trúc tiếp theo không còn dừng ở hình cây
nữa mà nới rộng ra thành một mạng quan
hệ nhiều chiều hơn hẳn.
Năn xếp với hàng đợi ở hai phần trước,
mình nói là sẽ dùng lại. Giờ đúng là lúc
dùng thật nhưng trong một cấu trúc rộng
hơn hẳn đó là đồ thị. Đồ thị chỉ gồm hai
thứ là đỉnh và cạnh nối giữa các bỉnh.
Cây ở mấy cảnh trước thực ra chỉ là một
dạng đồ thị đặc biệt, không có vòng lọc
quay lại. Đồ thị thì không bị giới hạn,
vậy một đỉnh nối tới bao nhiêu đỉnh khác
cũng được. Mình lấy bảy đỉnh này làm ví
dụ. Đặt tên từ A tới G. Nối với nhau
theo vài đường nhất định. Muốn lưu đồ
thị này trong máy, phổ biến nhất là ghi
lại mỗi đỉnh nối với những đỉnh nào gọi
là danh sách kề. Giờ ta đi thử hai cách
duyệt qua hết bảy đỉnh này xem sao nhé.
Cách thứ nhất là bắt đầu tại A, cho A
vào một hàng đợi, lấy A ra ghi nhận đã
ghé thăm, cho hết các đỉnh nối trực tiếp
với A là B với C và hàng đợi. Lấy B ra
thăm xong cho D với E vào hàng. Lấy C ra
thăm xong cho F vào hàng. Cứ lấy ra ở
đầu ghé thăm rồi cho đỉnh mới vào cuối
hàng không khác gì hàng đợi ở cảnh
trước. Kết quả là gì? Từng lớp một gần A
ghé trước xa A ghé sau. Cách này gọi là
duyệt theo tầng. Được nghĩ ra từ năm
1945 bởi Conradus nhưng luận án bị từ
chối mãi năm 1972 mới công bố. Edward
Moore tái phát minh lại năm 1959 để tìm
đường ngắn nhất trong một mê cung. Cách
thứ hai là cũng bắt đầu tại A nhưng lần
này cho vào một ngăm xếp. Lấy A ra khỏi
đỉnh, ghé xong đẩy B với C vào. Lấy B ra
ghé xong đẩy D với E vào. Lấy D ra ghé
xong D hết đường đi tiếp không đẩy gì
thêm cả. Lấy tiếp phần tử đang ở đỉnh là
E. Ghé xong đẩy G vào. Lấy G ra hết
đường thì không đẩy gì nữa. Năn xếp giờ
chỉ còn C lấy ra ghé đẩy ép vào. Lấy ép
ra hết đường xong đi [âm nhạc] một mạch
cho tới hết đường mới quay lại đúng luật
vào sau ra trước của ngăn xếp. Cách này
gọi là duyệt theo chiều sâu, gốc từ cách
giải mê cung của Tro khoảng thập nhiên
1880, [âm nhạc]
được Eduar Lucas ghi lại năm 1883
và Cherry quan sát một cách làm tương tự
năm 1895.
Cùng với bảy đỉnh công mấy đường nối đó,
nhưng đổi công cụ điều khiển thôi, hình
dạng đường đi thay đổi hẳn luôn. Hàng
đợi thì cho ra từng lớp lan rộng, năm
xếp thì cho ra một mạch đi thẳng rồi lùi
dần.
Sang cấu trúc tiếp theo vẫn mang dáng
cây nhưng rẽ nhánh không theo giá trị
lớn nhỏ nữa mà rẽ theo từng ký tự một.
Cái cấu trúc lúc nãy mình nói đến gọi là
try. Năm 1959, [âm nhạc] Rene de La
Briandez mô tả cách này lần đầu trong
bối cảnh máy tính.
&gt;&gt; [âm nhạc]
&gt;&gt; Một năm sau và năm 1960, Edward Fredkin
độc lập mô tả lạ và đặt cho nó cái tên
là try lấy từ đúng bốn chữ cái ở giữa từ
retrieval nghĩa là truy suất. Luật của
nó là mỗi cạnh đi xuống mang đúng một ký
tự. Đi từ gốc qua hết một đường tới một
nút được đánh dấu là kết thúc từ thì
đúng dãy ký tự đi qua chính là một từ
hoàn chỉnh. Hai từ chung nhau vài ký tự
đầu thì dùng chung luôn đoạn đường đó
chỉ tách ra từ chỗ khác nhau. Ví dụ nhá.
dựng choi cho năm từ cat, car, cog.
Từ gốc rẽ hai nhánh C với D. Nhánh C đi
thêm chữ A rồi rẽ tiếp. Một bên ra chữ T
thành cat, một bên ra chữ R thành care.
Nhưng cor chưa dừng ở đó, nó lại rẽ thêm
hai nhánh nữa. Một ra cord, một ra care.
[âm nhạc] Còn core vẫn được đánh dấu là
một từ hoàn chỉnh dù nó nằm giữa đường
chứ không phải cuối nhánh. Nhánh D thì
tách hẳn đi riêng một đường ra dog không
dính gì tới nhánh C cả. Giờ gõ thử hai
ký tự C với A. Đường đi từ gốc qua đúng
hai cạnh đó sáng lên. Toàn bộ phần cây
phía dưới tức cat, core, cều
là những từ có thể gợi ý ngay lập tức vì
tất cả cùng nằm dưới nhánh vừa gõ. Gõ
thêm chữ R thành Cor, đường sáng dài
thêm một đoạn. Danh sách gợi ý thuệp lại
còn ba từ đó là car, ce.
C rơi ra ngoài vì cat không nằm trên
nhánh này nữa. Sang cấu trúc tiếp theo
thì nó không còn hình cây nữa mà quay về
xử lý một câu hỏi khác hẳn luôn là hai
phần tử này có đang cùng một nhóm hay
không?
Câu hỏi mình để lại cuối phần trước. Hai
phần tử này có đang cùng một nhóm hay
không? Vậy thì cái cấu trúc này sinh ra
để trả lời cực nhanh câu hỏi trên. Năm
1964, Bernard Galler với Michael Fisher
công bố cách quản lý các nhóm rời giạc
kiểu này. Ban đầu chưa ai chứng minh
được nó nhanh cỡ nào. Năm 1973, Hopcroft
với Woman chứng minh một cận đầu tiên.
Tới năm 1975, Robert Chargen chứng minh
cận chặt hơn hẳn, gần như hằng số. Nhờ
hai [âm nhạc] mẹo là nối theo hạ và nén
đường đi mỗi lần truy vấn. Nguyên lý của
nó chỉ có hai việc thôi. Một là
[âm nhạc] mỗi nhóm có một đại diện
chung. Hai là chỉ cần hỏi hai phần tử có
cùng đại diện không là biết ngay có cùng
nhóm hay không. Gộp hai nhóm lại đơn
giản là gộp hai đại diện lại thành một.
Ví dụ sáu điểm này nhé. Đặt tên từ 1 tới
6. Ban đầu mỗi điểm là một nhóm riêng.
đang xét từng cạnh của một mạng lưới
theo thứ tự trọng số tăng dần để dựng
một cây khung nhỏ nhất. Cách làm này gọi
là thuật toán Crossc. Ông Joseph Crossco
công bố năm 1956.
Cạnh 1 2 nhóm khác nhau gộp lại. Cạnh 3
4 khác nhóm gộp lại. Cạnh 5 6 khác nhóm
gộp lại. Cạnh 2 3 vẫn khác nhóm gộp nhóm
1 2 với nhóm 3 4 thành một khối. Cạnh 16
khối vừa gộp với nhóm 56 vẫn khác nhau
gộp nốt luôn. Giơ cả sáu điểm chung một
nhóm. Tới cạnh 4 năm. Hỏi 4 với 5 có
cùng đại diện không? Có. Vì cả hai đã
nằm chung khối từ bước trước. Cùng nhóm
rồi, gộp thêm cũng vô nghĩa mà còn tạo
ra một vòng lặp thừa trong cây khung. Bỏ
qua cạnh này không gộp. Nhờ cách hỏi cực
nhanh gần như tức thời này, không cần dò
lại từ đầu mỗi lần thật toán crosscore
mới chạy được trên hàng triệu cạnh mà
không tụt tốc độ. Sang cấu trúc tiếp
theo, không còn chắc chắn tuyệt đối như
thế này nữa mà chấp nhận một chút may
rủi, nhưng đổi lại tốc độ nhanh hơn hẳn.
Hai cấu trúc mình sắp nói tới là Skip
List và Bloom Filter.
Skiplist được William Pew công bố vào
năm 1990 trên tạp chí của ACM. Ý tưởng
là bên trên một danh sách liên kết đã
sắp xếp bình thường, dựng thêm vài làn
nhanh, mỗi làn bỏ qua một số phần tử.
Làn càng cao càng thưa càng nhảy xa.
Quyết định phần tử nào lên làn cao hơn
dựa vào việc tung một đồng xu ngẫu nhiên
khi chèn. Không cần tính cân bằng phức
tạp như mấy cái cây ở mấy phần trước. Ví
dụ như tìm số 25 trong dãy tám số 3, 6 9
12 17 21.
Bắt đầu từ làn cao nhất nhé. Chỉ có đúng
một điểm dừng là 17. 17 nhỏ hơn 25
[âm nhạc] nhảy tới đó. Từ 17, làn cao
nhất hết đường, tụt xuống làn giữa. Làn
giữa từ 17 điểm kế là 25. Bằng đúng mục
tiêu rồi nhưng chưa vội nhận, tụt tiếp
xuống làn gốc để xác nhận. Ở làn gốc từ
17 nhảy một bước tới 21 rồi bước tiếp
gặp đúng 25 khớp luôn. Cả hành trình chỉ
chạm đúng ba số thôi. 17 21.
Nó bỏ qua hẳn bốn số đầu nhờ là nhanh.
Blu future thì đi theo hướng khác hẳn.
Năm 1970, BNG Bloom công bố ý tưởng là
dùng một giải buý cùng vài hàm băm để
trả lời cực nhanh câu hỏi một phần tử có
nằm trong tập hay không. Chấp nhận việc
là đôi khi trả lời sai nhưng chỉ sai
theo một hướng duy nhất. Giải 12 bit ban
đầu toàn số 0. Đưa một khóa vào. Ba hàm
băm chỉ thẳng ba vị trí, bật cả ba lên
một lúc. đưa khóa thứ hai vào lại bật
thêm vài vị trí có vị trí trùng khóa
trước có vị trí mới. Giờ hỏi một cái
khóa khác có nằm trong tập không? Ba hàm
băm chỉ ba vị trí, một trong ba vẫn đang
là số không. Chắc chắn khóa này chưa
từng vào. Nhưng hỏi tiếp một khóa nữa.
Ba hàm băm lần này chỉ đúng ba vị trí đã
được bật sẵn từ trước. Dù khóa này chưa
từng được đưa vào bao giờ. Bảng vẫn trả
lời có thể có. Tức nó sai [âm nhạc]
nhưng không bao giờ báo thiếu, chỉ có
thể báo dư.
Đổi lại một chút rủi ro nhỏ đó, cả hai
cấu trúc này tiết kiệm cực nhiều bộ nhớ
và thời gian so với cách làm chắc chắn
tuyệt đối.
Sang cấu trúc tiếp theo, quay lại chuyện
chắc chắn tuyệt đối nhưng ở quy mô lớn
hơn hẳn luôn vì dữ liệu không còn nằm
gọi trong bộ nhớ máy nữa mà tràn ra tận
ổ đĩa.
Rồi. Cây bi hay b truy ấy? Mình nhắc lại
một chút nhá. Rudolphyer với Edward
McCracht làm việc ở Boeing bắt đầu từ
khoảng năm 1970, công bố chính thức năm
1972.
Khác cây nhị phân ở chỗ, cây nhị phân
mỗi nút [âm nhạc] chỉ chứa một giá trị,
còn mỗi nút cây B chứa được nhiều giá
trị cùng lúc, giảm hẳn số tầng cần đi
qua. Không chỉ cơ sở dữ liệu dùng nó,
nhiều hệ thống tệp hiện nay như BGRFS,
đúng nghĩa đen là hệ thống tệp KB hay
XFS hay chỉ mục thư mục của EXT4 bên
Linux cũng đều dùng cùng nguyên lý này
để tìm một tệp trong hàng triệu tệp thật
nhanh. Ví dụ một đút gốc chứa hai giá
trị 30 60. Ta tìm số 50 ta so với góc
một lần. 50 nằm giữa 30 và 60 [âm nhạc]
rẽ vào nhánh giữa. Nhánh giữa chứa hai
giá trị 40 50. Nó khớp ngay chỉ hai lần
so sánh đi qua đúng hai tầng. Dù cây có
phình [âm nhạc] ra hàng triệu bản ghi
phía dưới cũng vậy. Nhưng cây B có một
điểm yếu là khi ghi liên tục vào giữa
cây trên một ổ đĩa quay nó khác tốn
công. Năm 1996, nhóm Oni công bố một
cách khác hẳn gọi là LSM, viết tắt của
lock structured merch tree. Cách này
không ghi thẳng súng đĩa mỗi lần có dữ
liệu mới. Dữ liệu mới gom hết vào một
vùng nhớ tạm [âm nhạc] trong RAM trước,
vùng tạm đầy đổ nguyên khối đó xuống đĩa
thành một lớp đã sắp xếp sẵn. Dữ liệu
mới lại tiếp tục gom đầy lại đổ tiếp
thành một lớp khác nữa. Theo thời gian,
các lớp nhỏ trên đĩa được gộp dần lại
thành lớp lớn hơn. Sắp xếp lại cho gọn.
ta gọi là nén dồn. Nhớ cách này, ghi dữ
liệu gần như luôn nhanh vì chỉ cần thêm
vào cuối một vùng nhớ tạm không phải
chen vào giữa cấu trúc trên đĩa.
Cassandra, Rox DB, Level DB. Những hệ
thống lưu trữ chịu được khối lượng Smith
khổng lồ ngày nay đều chạy trên đúng
nguyên lý này. Cây B mạnh về đập, chịu
được ghi vừa phải. LSM mạnh về ghi, đánh
đổi bằng việc đọc đôi khi phải dò qua
vài lớp, không có bên nào thắng tuyệt
đối cả. Chọn bên nào tùy vào việc đang
cần đọc nhiều hay ghi nhiều hơn.
16 cấu trúc chúng ta đã đi qua hết rồi.
Giờ mình gộp lại thành một khung để chọn
nhanh. Việc đang cần làm thì khớp với
cấu trúc nào nhất? Rồi, nếu cần lấy đúng
phần tử theo chỉ số ngay lập tức không
quan tâm trên xóa dỡ dãy, ta chọn mảng.
Nếu cần thêm bớt liên tục ở đầu hoặc
cuối, không cần truy cập ngẫu nhiên,
chọn danh sách liên kết.
Nếu cần đúng luật vào sau ra trước, chọn
ngăn xếp. Còn nếu vào trước ra trước,
lấy hàng đợi. Nếu cần tra theo một khóa
bất kỳ, không quan tâm thứ tự dữ liệu,
chọn bảng băm. Nếu cần dữ liệu luôn có
thứ tự, tìm theo khoảng giá trị và cần
chắc chắn tuyệt đối không suy biến, ta
chọn cây AVL hoặc cây đỏ đen. Nếu cần
chấp nhận một chút nỗ nhiên, đổi lấy
cách làm đơn giản hơn hẳn, chọn luôn
Skip list. Nếu cần liên tục lấy ra đúng
phần tử ưu tiên cao nhất, bất kể thứ tự
đưa vào là gì, lấy luôn híp. Nếu cần
biểu diễn quan hệ nhiều chiều giữa các
thực thể không giới hạn một gốc, chọn
ngay đồ thị. Trong đó thì nếu cần biết
cực nhanh hai thứ có đang cùng một nhóm
hay không, ta chọn union file. Nếu cần
tra cứu theo tiền tố của một chuỗi ký
tự, kiểu gõ tới đâu gợi ý tới đó,
[âm nhạc] chọn luôn try. Nếu cần kiểm
tra khả năng một phần tử có thuộc tập
hay không mà tốn cực ít bộ nhớ, chấp
nhận đôi khi báo dư, chọn ngay Bloom
Filter. Dữ liệu đã vượt khỏi bộ nhớ
trong máy phải nằm trên đĩa đọc nhiều
hơn ghi. Chọn cây B, ghi liên tục khối
lượng lớn chọn NSM3.
Không có cấu trúc nào thắng tuyệt đối
tất cả các bên. Việc chọn đúng chỉ đơn
giản là chọn theo đúng việc bạn đang cần
làm mà thôi. Giờ mình khép lại toàn bộ
những gì vừa đi qua nhé.
Các bạn nhớ lại đoạn mở đầu video không?
Một đống hạt sáng lộn xộn dần dần xếp
thành mảng, [âm nhạc] thành chuỗi, thành
cây, thành mạng. Giờ đi hết một vòng,
quay lại đúng đống hạt sáng đó. Nhưng
giờ nhìn nó đã khác hẳn. 16 cái tên vừa
đi qua không phải một danh sách để học
thuộc lòng đâu. Nó là 16 cách trả lời
cho cùng một câu hỏi. Dữ liệu này cần
được xếp ra sao để việc đang làm trở nên
dễ hơn? Chọn đúng cách xếp, bài toán khó
tự nhiên nhẹ đi hơn hẳn. Tổng kết nhanh
cho dễ nhớ nhé. Mảng, bảng băm, năn xếp,
hàng đợi, híp hầu hết đều tức thời hoặc
gần tức thời cho đúng việc chúng sinh ra
để làm. Cây cân bằng cây B, skip list
thì ở quanh mức log n. Đồ thị đi hết
theo số đỉnh cộng số cạnh. Try đi theo
đúng độ dài chuỗi, không quan tâm từ
điển lớn cỡ nào. Cấu trúc dữ liệu là cái
nền. Cái nền dựng xong, phần chạy trên
cái nền đó tức là giải thuật mới chính
là câu chuyện tiếp theo. Sắp xếp, tìm
kiếm, quy hoạch động. Tất cả đều đứng
trên vai mấy cái tên vừa nhắc ở video
này. Nếu video này giúp thấy cấu trúc dữ
liệu bớt rối hơn một chút, bạn nhớ để
lại một like, bấm đăng ký kênh. Kênh sẽ
còn quay lại chủ đề giải thuật ở những
video sau nhé. Cảm ơn bạn đã xem hết
video.