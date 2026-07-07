#!/usr/bin/env bash
# test-gemini-meetily.sh — kiểm tra Gemini (OpenAI-compat) trước khi tin dùng trong meetily.
# Cách chạy (key truyền qua biến môi trường, KHÔNG lưu trong file, KHÔNG gửi đi đâu ngoài Google):
#   GEMINI_KEY=your_key bash test-gemini-meetily.sh
# Đổi model (tùy chọn):  GEMINI_KEY=your_key MODEL=gemini-2.5-flash bash test-gemini-meetily.sh
set -uo pipefail

KEY="${GEMINI_KEY:-${1:-}}"
MODEL="${MODEL:-gemini-2.5-pro}"
BASE="https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
OUT="$HOME/Documents/gemini-bienban-test-output.md"

if ! command -v jq >/dev/null 2>&1; then echo "Cần jq (brew install jq)."; exit 1; fi
if [ -z "$KEY" ]; then
  echo "Chưa có key. Chạy:  GEMINI_KEY=your_key bash $0"
  exit 1
fi
echo "Model: $MODEL"

echo
echo "===== TEST 1: Kết nối + key ====="
req1=$(jq -n --arg m "$MODEL" '{model:$m,messages:[{role:"user",content:"Trả lời đúng MỘT câu tiếng Việt: bạn có đang hoạt động không?"}]}')
r1=$(curl -s -w $'\n%{http_code}' "$BASE" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" -d "$req1")
code1=$(printf '%s' "$r1" | tail -n1)
body1=$(printf '%s' "$r1" | sed '$d')
# Trích thông báo lỗi bất kể body là object {error:{message}}, {message}, hay array
emsg() { jq -r '[.. | .message? // empty][0] // "(không đọc được thông báo lỗi — xem body thô bên dưới)"' 2>/dev/null; }
echo "HTTP $code1"
case "$code1" in
  200) echo "✅ OK: $(printf '%s' "$body1" | jq -r '.choices[0].message.content // "(không có nội dung)"')" ;;
  400|401|403) echo "❌ $code1: $(printf '%s' "$body1" | emsg | head -c 400)"
       echo "   → ĐỌC message trên: nếu nhắc 'model' ⇒ sai tên model (liệt kê bên dưới); nếu nhắc 'API key'/'credential'/'permission'/'billing' ⇒ key sai hoặc chưa bật Generative Language API / chưa bật billing."
       echo "     Liệt kê model hợp lệ:  curl \"https://generativelanguage.googleapis.com/v1beta/models?key=\$GEMINI_KEY\" | jq -r '.models[].name'"
       echo "   (body thô, 300 ký tự đầu): $(printf '%s' "$body1" | tr -d '\n' | head -c 300)" ;;
  404) echo "❌ 404: SAI URL (không nên xảy ra — base URL đã được xác minh)." ;;
  *) echo "Phản hồi lạ:"; printf '%s\n' "$body1" | head -c 500 ;;
esac
if [ "$code1" != "200" ]; then echo; echo "Dừng lại — sửa lỗi TEST 1 trước khi nhập vào meetily."; exit 1; fi

echo
echo "===== TEST 2: Biên bản (fidelity) — transcript GIẢ, so với qwen3.5 ====="
SYS=$(cat <<'SYSEOF'
Bạn là thư ký ghi biên bản họp chi bộ. Dựa DUY NHẤT vào bản ghi (transcript) người dùng cung cấp, viết biên bản bằng tiếng Việt theo các mục sau, mỗi mục một tiêu đề in đậm:
Thông tin cuộc họp; Thành phần tham dự; Nội dung cuộc họp; Ý kiến đóng góp (ghi rõ AI nói gì); Giải trình của chủ trì; Biểu quyết và kết luận; Kết thúc.
KỶ LUẬT BẮT BUỘC: chỉ dùng thông tin CÓ trong bản ghi; TUYỆT ĐỐI không bịa; sao chép chính xác họ tên và số liệu; mục nào không có trong bản ghi thì ghi '.....'. KHÔNG thêm nội dung không được nói tới. KHÔNG viết phần suy nghĩ, chỉ xuất biên bản.
SYSEOF
)
USR=$(cat <<'USREOF'
[00:00] Chủ trì (đ/c Nguyễn Văn A): Hôm nay 19 giờ 30 ngày 5 tháng 7 năm 2026, tại nhà đồng chí Trần Văn B, chi ủy chi bộ Đông Trà 1 tổ chức sinh hoạt chi bộ thường kỳ tháng 7. Tổng số 15 đảng viên (14 chính thức, 1 dự bị), có mặt 13, vắng 2: đồng chí Lê Thị C vắng có lý do đi công tác, đồng chí Phạm Văn D vắng không lý do. Chủ trì: Nguyễn Văn A, bí thư. Thư ký: Hoàng Thị E.
[02:10] Chủ trì: Nội dung 1, đánh giá công tác tháng 6: thu đảng phí đạt 100%, tổ chức một buổi lao động vệ sinh khu dân cư, vận động ba hộ tham gia phong trào toàn dân đoàn kết.
[08:40] Chủ trì: Nội dung 2, kế hoạch tháng 7: chuẩn bị đại hội chi bộ nhiệm kỳ tới, phân công đồng chí Hoàng Thị E dự thảo báo cáo chính trị, xong trước ngày 20 tháng 7.
[15:05] Đ/c Trần Văn B: Đề nghị bổ sung nội dung tuyên truyền phòng chống dịch trong tháng 7 vì khu dân cư đang có ca bệnh.
[17:20] Đ/c Vũ Thị F: Góp ý báo cáo chính trị nên lấy ý kiến rộng rãi của tất cả đảng viên trước khi hoàn thiện, không nên chỉ giao cho một đồng chí.
[19:00] Chủ trì giải trình: Tiếp thu ý kiến đồng chí Trần Văn B, sẽ bổ sung tuyên truyền phòng chống dịch. Về ý kiến đồng chí Vũ Thị F, chi ủy sẽ tổ chức lấy ý kiến toàn thể đảng viên với dự thảo báo cáo chính trị trước khi trình đại hội.
[22:30] Chủ trì: Chi bộ biểu quyết thống nhất 100% đồng ý nội dung biên bản.
[24:00] Chủ trì: Cuộc họp kết thúc vào lúc 20 giờ 45 phút cùng ngày.
USREOF
)
req2=$(jq -n --arg m "$MODEL" --arg s "$SYS" --arg u "$USR" '{model:$m,messages:[{role:"system",content:$s},{role:"user",content:$u}]}')
r2=$(curl -s "$BASE" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" -d "$req2")
content=$(printf '%s' "$r2" | jq -r '.choices[0].message.content // empty')
if [ -z "$content" ]; then
  echo "❌ Không có nội dung. Lỗi: $(printf '%s' "$r2" | jq -r '[.. | .message? // empty][0] // "(không rõ)"' 2>/dev/null | head -c 300)"; exit 1
fi
printf '%s\n' "$content" > "$OUT"
echo "✅ Đã lưu biên bản Gemini vào: $OUT"
echo
echo "----- KIỂM CHÉO NHANH (transcript nói gì so với biên bản Gemini) -----"
echo "Ý kiến ĐÚNG phải là: (B) tuyên truyền phòng chống dịch · (F) lấy ý kiến rộng rãi về báo cáo chính trị."
echo "Nếu biên bản nhắc tới 'phát triển đảng viên/thu hút thanh niên' hay nội dung KHÔNG có ở trên => Gemini ĐANG BỊA (giống qwen3.5)."
echo -n "  - Có cụm 'phòng chống dịch' (đúng)?      : "; printf '%s' "$content" | grep -c "phòng chống dịch"
echo -n "  - Có cụm 'báo cáo chính trị' (đúng)?     : "; printf '%s' "$content" | grep -c "báo cáo chính trị"
echo -n "  - Có 'thu hút'/'thanh niên' (dấu hiệu bịa)?: "; printf '%s' "$content" | grep -c "thu hút\|thanh niên"
echo
echo "Mở file để đọc đầy đủ:  open \"$OUT\""
