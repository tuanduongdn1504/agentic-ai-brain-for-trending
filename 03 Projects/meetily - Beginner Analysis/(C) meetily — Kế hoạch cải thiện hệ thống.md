# (C) meetily — Kế hoạch cải thiện hệ thống Trợ lý meeting

*2026-07-05 · Claude-authored · dựa trên: đọc source meetily @ `0281737`, dry-run qwen3.5, và biên bản thật ngày 04/7/2026*

## Kết luận thẳng (đọc cái này trước)

**Nút thắt KHÔNG phải ở template, mà ở chỗ: mô hình tóm tắt cục bộ nhỏ (qwen3.5) BỊA phần diễn giải (ý kiến, giải trình) trong khi vẫn lấy đúng các trường dữ kiện (giờ, sĩ số, tên chủ trì/thư ký).** Với một biên bản chi bộ — nơi độ trung thực là yêu cầu thủ tục — điều đó là *không chấp nhận được nếu không có bước người kiểm tra*.

→ **Nguyên tắc thiết kế của cả hệ thống:** *Ghi âm trung thực (Whisper + kỷ luật họp) → mô hình DỰNG BẢN NHÁP → người LUÔN đối chiếu phần diễn giải với bản ghi trước khi ký.* Đừng đi tìm "mô hình thần kỳ" để bỏ qua bước verify — hãy làm cho bước verify NHANH. Đây là kết luận cốt lõi; ba trục dưới đây đều phục vụ nó.

---

## Trục 1 — Mô hình STT / Summary

### 1a. Phiên âm (STT): Whisper, chọn đúng cỡ
- **Tiếng Việt → luôn dùng Whisper, KHÔNG dùng Parakeet** (Parakeet v3 chỉ ~25 ngôn ngữ châu Âu, không có tiếng Việt) — đã ghi trong runbook.
- **Cỡ model quyết định chất lượng:** `base`/`small` phiên âm tiếng Việt kém. **Tối thiểu `medium`; tốt nhất `large-v3` hoặc `large-v3-turbo`** (turbo gần bằng large-v3 nhưng nhanh 4–8×, hợp máy Mac Apple Silicon). Kiểm tra danh sách model trong meetily và tải cỡ lớn nhất máy chịu được.
- **Điểm yếu chí tử = tên riêng + thuật ngữ Đảng.** Whisper sẽ đọc sai "Võ Cường", "Dương Văn Tuấn", "chi ủy", "TDP", "CTMT", "Chỉ thị 50", "Nghị quyết"... Cách giảm:
  - Danh sách đảng viên chi bộ là **cố định** → thư ký sửa tên trong bản ghi (transcript) trước khi tóm tắt. Đây là việc bắt buộc, không né được.
  - Đọc rõ, chậm các tên + số liệu quan trọng trong cuộc họp.
  - (Nâng cao) whisper.cpp hỗ trợ "initial prompt" để mồi từ vựng — cần kiểm tra meetily có cho chỉnh không (chưa xác nhận trong bản đọc source).

### 1b. Tóm tắt (Summary): đây là mắt xích yếu — phải đổi
- **Bỏ qwen3.5 cho bước tóm tắt.** Nó là model *suy luận* (reasoning) → vòng lặp suy nghĩ + bịa nội dung. Dry-run đã chứng minh.
- **Dùng model instruct KHÔNG suy luận, càng lớn càng trung thực:**

  | Ưu tiên | Model | Điều kiện | Ghi chú |
  |---|---|---|---|
  | Tốt nhất | `qwen2.5:32b-instruct` hoặc `gemma2:27b` | RAM/unified ≥ 32GB | Trung thực rõ rệt, tiếng Việt tốt |
  | Trung bình | `qwen2.5:14b-instruct` | ~16–24GB | Cân bằng tốt |
  | Tối thiểu | `qwen2.5:7b-instruct` / `llama3.1:8b` | ~8–12GB | Vẫn cần verify nặng |

  `ollama pull qwen2.5:14b-instruct` (hoặc 32b) rồi đặt làm summary model trong meetily.
- **Context dài quan trọng:** cuộc họp 2 tiếng vượt ngữ cảnh → meetily chia nhỏ nhiều lượt (map-reduce) → mỗi lượt là một cơ hội bịa. Chọn model context lớn (qwen2.5 128k) để cả bản ghi vào 1 lượt → ít điểm bịa hơn.
- **⚠️ Căng thẳng riêng tư vs chất lượng (phải nêu thẳng):** model cloud (Claude) trung thực nhất, NHƯNG nội dung chi bộ **không được rời máy**. → Với họp chi bộ mật: **giữ cục bộ + bắt buộc verify**, KHÔNG dùng cloud. Với họp không nhạy cảm (coaching, nội bộ công ty): có thể dùng đường tóm tắt chất lượng cao hơn.

### 1c. Đường thay thế cho biên bản độ-trung-thực-cao
Biên bản thật hôm nay tôi dựng KHÔNG qua bước summary của meetily — mà bằng một **prompt được kiểm soát chặt** (trích-không-bịa / sao chép tên chính xác / thiếu thì ghi `.....`). Đó là đường cho fidelity cao nhất:
> **meetily = bắt âm + phiên âm (transcript). Dựng biên bản = chạy prompt kiểm soát (trong Claude Code với việc không nhạy cảm, hoặc model cục bộ lớn với việc mật) — KHÔNG dựa vào nút "summary" mặc định của meetily cho văn bản chính thức.**
Template `.md` của meetily chỉ điều khiển *các mục*, không điều khiển được system-prompt chống-bịa → giới hạn của nó là ở đó.

---

## Trục 2 — Quy trình verify (đòn bẩy lớn nhất)

Vì model cục bộ sẽ luôn không hoàn hảo, thiết kế để người LUÔN verify, và verify phải rẻ:

1. **Luôn giữ transcript** (meetily có sẵn). Không có transcript = không verify được = không ký được.
2. **Đối chiếu 2 cột:** bản nháp biên bản cạnh transcript; soi từng mục **Ý kiến / Giải trình / Kết luận** — mỗi câu phải truy được về một lượt phát biểu thật.
3. **Đọc to trong họp** các dữ kiện chốt (sĩ số, giờ, quyết định, tỷ lệ biểu quyết) → chúng vào transcript thay vì thành `.....`.
4. **Maker/checker (mẫu loop-engineering v189 của chính vault):** model = "maker", người = "checker" mặc-định-BÁC-BỎ. Có thể thêm **1 lượt máy dò-bịa**: đưa transcript + bản nháp cho model và hỏi "*câu nào trong bản tóm tắt KHÔNG có căn cứ trong transcript?*" — chạy cục bộ được, bắt phần lớn chỗ bịa.
5. **Checklist chuẩn hoá** (xem file `(C) meetily — Verify Checklist + Dò-bịa.md`): tên đúng? số đúng? mỗi ý kiến truy được nguồn? không nội dung bịa? các `.....` đã điền?
6. **Kỷ luật chữ ký** — chính cuộc họp 04/7 đã nêu **Chỉ thị 50, Hướng dẫn 42**: phân công người đánh giá chất lượng sinh hoạt và **ký vào biên bản**. Đưa người-đánh-giá-ký vào quy trình.

---

## Trục 3 — Chuẩn hoá template biên bản

Đã nâng cấp `bien_ban_chi_bo.json` **v1 → v2** (dựa trên cấu trúc thật của cuộc họp 04/7, mà v1 chưa phủ hết):
- Thêm: **Đại biểu mời dự**, **Phần ra mắt** (khi có), **Ý kiến chỉ đạo của cấp trên**, **Thủ tục khác** — v1 thiếu, cuộc họp thật đều có.
- Nhúng kỷ luật chống-bịa vào từng mục instruction: *"trích từ bản ghi, KHÔNG bịa; sao chép chính xác họ tên & số liệu; thiếu thì ghi `.....`"*.
- **Hai tầng template** (đừng lẫn):
  - **Template meetily (JSON)** = điều khiển các mục khi tóm tắt → sinh *nội dung*.
  - **Form Word chính thức** (header ĐẢNG BỘ/CHI BỘ + khối chữ ký) = *khung chứa*. Dán nội dung vào form; header + chữ ký ở form, không ở meetily.
- Cân nhắc 2 loại: **sinh hoạt thường kỳ** vs **hội nghị đặc biệt/ra mắt** (cuộc 04/7 là lai — ra mắt chi ủy + thường kỳ). v2 phủ được cả hai bằng các mục "khi có thì ghi".

---

## Thứ tự ưu tiên (làm gì trước)

1. **Đổi summary model** (`ollama pull qwen2.5:14b-instruct` / 32b) — bỏ qwen3.5. *(30 phút, tác động lớn nhất.)*
2. **Cài quy trình verify** (checklist + đối chiếu 2 cột + lượt dò-bịa). *(Đây mới là thứ đảm bảo chất lượng, không phải model.)*
3. **Dùng template v2** + tách form Word.
4. **Chạy thử 1 cuộc họp thật thấp rủi ro** với Whisper large-v3-turbo + qwen2.5-instruct, so với biên bản tay — ghi vào Pilot Log.
5. Nếu chất lượng transcript tên riêng vẫn kém → thư ký sửa tên trong transcript (danh sách cố định) là bước chuẩn.

**Việc của tôi (đã làm trong phiên này):** template v2 + checklist verify + prompt dò-bịa. **Việc của bạn:** pull model, đặt Whisper cỡ lớn, chạy thử, ghi log.
