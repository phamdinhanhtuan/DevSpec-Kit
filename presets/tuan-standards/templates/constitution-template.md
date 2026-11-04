# Hiến Pháp Dự Án (Project Constitution)
<!-- Phiên bản: 1.0.0 | Tác giả: Phạm Đình Anh Tuấn (phamdinhanhtuan) -->

Tài liệu này xác định các nguyên tắc bất biến cho toàn bộ vòng đời phát triển dự án. Tất cả đặc tả (specs), kế hoạch (plans), nhiệm vụ (tasks) và code triển khai (implementation) BẮT BUỘC phải tuân thủ nghiêm ngặt các nguyên tắc dưới đây.

---

## 1. Đơn giản trước (Simplicity First)
- Luôn ưu tiên giải pháp dễ hiểu, tường minh, ngắn gọn nhất đáp ứng trọn vẹn yêu cầu.
- Tránh over-engineering, không tạo cấu trúc abstraction phức tạp khi chưa có bằng chứng thực sự cần thiết.
- Mã nguồn viết ra phải dễ bảo trì, dễ đọc cho người khác và cho chính mình sau này.

## 2. Bám sát Đặc tả (Strict Spec Adherence)
- Tuyệt đối không tự ý thêm thư viện ngoài (external dependencies) hoặc tính năng nằm ngoài phạm vi đặc tả (`spec.md`).
- Mọi thay đổi về phạm vi hay phát sinh tính năng mới phải được cập nhật lại vào `spec.md` và có sự đồng ý của người dùng trước khi code.

## 3. Kỷ luật Kiểm thử (Test-Driven Discipline)
- Tất cả các logic quan trọng (business logic, validation, edge cases, error handling) bắt buộc phải có automated unit test / integration test.
- Code không được coi là hoàn tất ("Done") nếu chưa pass 100% test suites liên quan.

## 4. Không giả định khi mơ hồ (Zero Ambiguity Tolerance)
- Điểm nào chưa rõ ràng, mơ hồ hoặc có nhiều phương án lựa chọn: **BẮT BUỘC HỎI NGƯỜI DÙNG**, tuyệt đối không tự ý phỏng đoán rồi làm sai lệch ý muốn của họ.
- Sử dụng lệnh `/speckit-clarify` hoặc hỏi trực tiếp để chốt phương án rõ ràng.

## 5. Kiểm soát Từng bước có Duyệt (Step-by-Step Approval)
- Tuân thủ đúng chu trình Spec-Driven Development (SDD):
  1. `Constitution` (Hiến pháp) -> 2. `Specify` (Đặc tả) -> 3. `Plan` (Kế hoạch) -> 4. `Tasks` (Nhiệm vụ) -> 5. `Implement` (Triển khai) -> 6. `Converge` (Hội tụ / Kiểm thử).
- Mỗi bước dừng lại báo cáo kết quả rõ ràng và chờ người dùng duyệt trước khi chuyển sang bước tiếp theo.

## 6. Giao tiếp & Tài liệu Chuẩn mực (Communication & Documentation)
- Mặc định giao tiếp, giải thích và viết tài liệu bằng Tiếng Việt rõ ràng, chuẩn kỹ thuật (kèm thuật ngữ chuẩn quốc tế khi cần).
- Đảm bảo commit messages chuẩn Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`).
