# (C) meetily — Verify Checklist + Prompt dò-bịa

*2026-07-05 · Claude-authored · quy trình kiểm tra biên bản trước khi ký (Trục 2 của kế hoạch cải thiện)*

> Lý do tồn tại: model cục bộ nhỏ **bịa** phần diễn giải (ý kiến, giải trình) dù lấy đúng dữ kiện. Vì vậy **luôn** verify bản nháp với transcript trước khi ký. Checklist này làm bước đó nhanh + có kỷ luật.

## Checklist đối chiếu (chạy mỗi biên bản, trước khi ký)

Mở **bản nháp biên bản** cạnh **transcript** (meetily giữ transcript). Tick từng dòng:

**Dữ kiện (thường model làm đúng — vẫn kiểm):**
- [ ] Giờ bắt đầu / giờ kết thúc đúng transcript
- [ ] Ngày, địa điểm đúng
- [ ] Sĩ số (tổng / có mặt / vắng) + tỷ lệ đúng con số trong transcript
- [ ] Tên **chủ trì** và **thư ký** đúng chính tả
- [ ] Mọi số liệu trích dẫn (số hộ, số chi bộ, số văn bản/chỉ thị...) khớp transcript

**Diễn giải (RỦI RO CAO — model hay bịa, soi kỹ nhất):**
- [ ] **Mỗi ý kiến** truy được về một lượt phát biểu THẬT trong transcript
- [ ] **Ý kiến gán đúng người** (không đổi tên người phát biểu)
- [ ] **Không có ý kiến/nội dung nào KHÔNG có trong transcript** (bịa thêm)
- [ ] Phần **giải trình / kết luận** đúng lời chủ trì, không phịa
- [ ] Không có "văn phong Đảng chung chung" mà transcript không nói (dấu hiệu bịa)

**Hoàn thiện:**
- [ ] Mọi `.....` đã điền tay (2 tên vắng, tài liệu, thông tin khác...)
- [ ] Tên riêng Whisper đọc sai đã sửa (đối chiếu danh sách đảng viên cố định)
- [ ] Header form (ĐẢNG BỘ / CHI BỘ) + khối chữ ký đầy đủ
- [ ] Phân công người đánh giá chất lượng sinh hoạt + ký (Chỉ thị 50 / Hướng dẫn 42)

→ **Chỉ ký khi tất cả đã tick.** Nếu một mục diễn giải không truy được nguồn → xoá/sửa nó, đừng để nguyên.

## Prompt "dò-bịa" (chạy 1 lượt máy trước khi verify tay)

Dán transcript + bản nháp vào model (cục bộ được), dùng prompt này để máy tự chỉ ra chỗ nghi bịa — thu hẹp việc soi tay:

```
Bạn là người kiểm tra biên bản. Tôi đưa BẢN GHI (transcript) và BẢN NHÁP biên bản.
Nhiệm vụ DUY NHẤT: liệt kê mọi câu/ý trong BẢN NHÁP mà KHÔNG có căn cứ trong BẢN GHI
(bịa, gán sai người, hoặc thêm nội dung không nói tới). Với mỗi mục ghi:
  - Câu trong bản nháp
  - Vì sao nghi ngờ (không có trong bản ghi / gán sai người / số liệu lệch)
KHÔNG viết lại biên bản. KHÔNG khen. Chỉ liệt kê chỗ nghi bịa. Nếu không thấy, ghi "Không phát hiện".

=== BẢN GHI (TRANSCRIPT) ===
[dán transcript]

=== BẢN NHÁP BIÊN BẢN ===
[dán bản nháp]
```

Lưu ý: lượt dò-bịa này **hỗ trợ**, không thay người. Vẫn phải verify tay theo checklist trên — chính model dò cũng có thể sót.

## Kỷ luật "đọc to trong họp" (làm transcript tốt hơn từ gốc)

Để dữ kiện vào transcript thay vì thành `.....`, trong cuộc họp nên đọc rõ + chậm:
- Sĩ số: "Tổng số N đồng chí, có mặt M, vắng K (nêu tên + lý do)"
- Giờ bắt đầu / giờ kết thúc
- Từng quyết định, từng kết luận
- Tỷ lệ biểu quyết ("thống nhất 100%")
- Tên người phát biểu trước mỗi ý kiến ("Mời đồng chí [Tên] cho ý kiến")
