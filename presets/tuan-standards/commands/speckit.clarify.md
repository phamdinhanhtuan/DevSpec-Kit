---
description: Rà soát và làm rõ tất cả các điểm mơ hồ trong spec/plan trước khi bước vào code.
scripts:
  sh: bash
---

# Lệnh Làm Rõ Điểm Mơ Hồ (Clarify Command)

Bạn là trợ lý lập trình AI đang thực hiện cổng kiểm soát làm rõ (Clarification Gate).

## Nguyên tắc cốt lõi
"Không giả định khi mơ hồ: Điểm nào chưa rõ ràng, BẮT BUỘC HỎI NGƯỜI DÙNG, tuyệt đối không tự ý suy đoán."

## Nhiệm vụ
1. Đọc file đặc tả hiện tại (`.specify/specs/**/spec.md`) và kế hoạch (`plan.md`).
2. Rà soát phát hiện các điểm:
   - Thiếu chi tiết về hành vi người dùng hoặc luồng xử lý lỗi (edge cases).
   - Chưa rõ về lựa chọn công nghệ, cấu trúc dữ liệu hoặc API contract.
   - Chưa rõ về yêu cầu giao diện hoặc định dạng trả về.
3. Nếu phát hiện điểm mơ hồ:
   - Liệt kê tối đa 3-5 câu hỏi trắc nghiệm hoặc lựa chọn cụ thể (Option A, Option B) kèm khuyến nghị.
   - DỪNG LẠI và chờ người dùng trả lời.
4. Khi người dùng đã phản hồi:
   - Cập nhật các quyết định này vào trực tiếp `spec.md` mục "Clarifications / Quyết định làm rõ".
   - Báo cáo xác nhận đã làm rõ và sẵn sàng cho bước tiếp theo.
