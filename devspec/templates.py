"""Template engine for DevSpec Kit.

Provides standardized Spec-Driven Development templates.
"""

CONSTITUTION_TEMPLATE = """# Hiến Pháp Dự Án (Project Constitution)
<!-- Phiên bản: 1.0.0 | Tác giả: Phạm Đình Anh Tuấn (phamdinhanhtuan) -->

Tài liệu này xác định các nguyên tắc bất biến cho toàn bộ vòng đời phát triển dự án. Tất cả đặc tả (specs), kế hoạch (plans), nhiệm vụ (tasks) và mã nguồn triển khai (implementation) BẮT BUỘC phải tuân thủ nghiêm ngặt các nguyên tắc dưới đây.

---

## 1. Đơn giản trước (Simplicity First)
- Luôn ưu tiên giải pháp dễ hiểu, tường minh, ngắn gọn nhất đáp ứng trọn vẹn yêu cầu.
- Tránh over-engineering, không tạo cấu trúc abstraction phức tạp khi chưa có bằng chứng thực sự cần thiết.
- Mã nguồn viết ra phải dễ bảo trì, dễ đọc cho đồng đội và chính mình sau này.

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
  1. `Constitution` (Hiến pháp) -> 2. `Specify` (Đặc tả) -> 3. `Clarify` (Làm rõ) -> 4. `Plan` (Kế hoạch) -> 5. `Tasks` (Nhiệm vụ) -> 6. `Implement` (Triển khai) -> 7. `Converge` (Hội tụ / Kiểm thử).
- Mỗi bước dừng lại báo cáo kết quả rõ ràng và chờ người dùng duyệt trước khi chuyển sang bước tiếp theo.

## 6. Giao tiếp & Tài liệu Chuẩn mực (Communication & Documentation)
- Mặc định giao tiếp, giải thích và viết tài liệu bằng Tiếng Việt rõ ràng, chuẩn kỹ thuật (kèm thuật ngữ chuẩn quốc tế khi cần).
- Đảm bảo commit messages chuẩn Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`).
"""

SPEC_TEMPLATE = """# Đặc Tả Tính Năng: {title}
<!-- Feature Slug: {slug} | Trạng thái: Draft | Ngày tạo: {date} -->

## 1. Tổng quan & Mục tiêu
- **Mục tiêu**: Mô tả ngắn gọn tính năng này giải quyết vấn đề gì.
- **Giá trị mang lại**: Lợi ích cho người dùng cuối hoặc hệ thống.
- **Phạm vi (In Scope)**: Những gì tính năng NÀY bao gồm.
- **Ngoài phạm vi (Out of Scope)**: Những gì tính năng này KHÔNG làm.

## 2. Yêu cầu Người dùng (User Stories & Scenarios)
### Câu chuyện 1: [Tiêu đề người dùng]
- **Là một**: [Vai trò người dùng, ví dụ: Khách hàng / Quản trị viên]
- **Tôi muốn**: [Hành động mong muốn]
- **Để**: [Mục tiêu đạt được]

**Tiêu chí Chấp nhận (Acceptance Criteria / Gherkin):**
```gherkin
Given [Điều kiện ban đầu]
When [Hành động kích hoạt]
Then [Kết quả kỳ vọng xảy ra]
```

## 3. Quy tắc Nghiệp vụ & Dữ liệu
- **Quy tắc xác thực (Validation)**:
  - Trường bắt buộc, giới hạn độ dài, định dạng hợp lệ.
- **Xử lý ngoại lệ (Edge Cases)**:
  - Mạng gián đoạn, dữ liệu rỗng, trùng lặp, quyền truy cập bị từ chối.

## 4. Quyết định Làm rõ (Clarifications)
<!-- Điền sau khi chạy /speckit-clarify -->
- [x] Quyết định 1: ...
"""

CLARIFY_TEMPLATE = """# Rà Soát & Làm Rõ Yêu Cầu (Clarification Log)
<!-- Feature Slug: {slug} | Ngày: {date} -->

## Các Điểm Cần Làm Rõ Với Người Dùng
Vui lòng chọn hoặc trả lời trực tiếp các câu hỏi bên dưới trước khi tiến hành lập kế hoạch kỹ thuật (`plan.md`).

### Câu hỏi 1: [Vấn đề chưa rõ]
- [ ] **Lựa chọn A**: ...
- [ ] **Lựa chọn B**: ...
- [ ] **Khuyến nghị kỹ thuật**: ...

---
## Kết luận Đã Chốt
- **Quyết định**: ...
- **Tác động tới Spec**: ...
"""

PLAN_TEMPLATE = """# Kế Hoạch Kiến Trúc & Kỹ Thuật (Architecture Plan): {title}
<!-- Feature Slug: {slug} | Trạng thái: Planned -->

## 1. Ngăn Xếp Công Nghệ (Tech Stack)
- **Ngôn ngữ / Framework**:
- **Thư viện sử dụng** (Chỉ những thư viện đã có hoặc bắt buộc trong spec):
- **Cơ sở dữ liệu / Lưu trữ**:

## 2. Thiết Kế Kiến Trúc & Cấu Trúc Thư Mục
```text
project-root/
├── [module/component]/
│   ├── [source files]
│   └── [test files]
```

## 3. Thiết Kế Mô Hình & Giao Diện (Data Models & APIs)
- **Entities / Data Classes**:
- **API Contracts / Public Interfaces**:

## 4. Chiến Lược Kiểm Thử (Testing Strategy)
- **Unit Tests**: Kiểm tra các hàm nghiệp vụ, validations, edge cases.
- **Integration Tests**: Kiểm tra luồng tích hợp giữa các tầng (Data, Domain, Presentation).

## 5. Rủi Ro Kỹ Thuật & Giảm Thiểu
- **Rủi ro**: ... -> **Giải pháp**: ...
"""

TASKS_TEMPLATE = """# Danh Sách Nhiệm Vụ Triển Khai (Implementation Tasks): {title}
<!-- Feature Slug: {slug} | Trạng thái: In Progress -->

> **Nguyên tắc**: Triển khai tuần tự từng task, kiểm thử đầy đủ trước khi chuyển task tiếp theo.

## Pha 1: Chuẩn bị & Cấu trúc nền tảng
- [ ] **Task 1.1**: Tạo mô hình dữ liệu (Data models & interfaces)
  - File cần tạo: `...`
  - Tiêu chí hoàn thành: Models biên dịch thành công, không có lỗi linter.

## Pha 2: Logic nghiệp vụ cốt lõi & Unit Tests
- [ ] **Task 2.1**: Viết Unit Tests cho nghiệp vụ chính (TDD)
  - File test: `...`
  - Tiêu chí hoàn thành: Test phản ánh đúng acceptance criteria trong `spec.md`.
- [ ] **Task 2.2**: Triển khai logic xử lý nghiệp vụ
  - File mã nguồn: `...`
  - Tiêu chí hoàn thành: 100% unit tests của Task 2.1 vượt qua (PASS).

## Pha 3: Giao diện / Tích hợp đầu cuối
- [ ] **Task 3.1**: Tích hợp tầng UI / API Controller
  - Tiêu chí hoàn thành: Giao diện phản hồi đúng hành vi người dùng.
- [ ] **Task 3.2**: Xử lý các trường hợp ngoại lệ (Edge cases & validation)
  - Tiêu chí hoàn thành: Thông báo lỗi hiển thị rõ ràng, không crash.

## Pha 4: Hội tụ & Nghiệm thu (Convergence)
- [ ] **Task 4.1**: Chạy toàn bộ test suite dự án
- [ ] **Task 4.2**: Đối chiếu kiểm tra lại `spec.md` đã đáp ứng 100% tiêu chí chấp nhận.
"""

BUG_TEMPLATE = """# Nhật Ký Sửa Lỗi (Bug Diagnostic & Resolution)
<!-- Bug Slug: {slug} | Trạng thái: Triaged | Ngày tạo: {date} -->

## 1. Triệu Chứng Lỗi
- **Mô tả hiện tượng**: 
- **Môi trường xảy ra**: 
- **Các bước tái hiện (Steps to Reproduce)**:
  1. ...
  2. ...
- **Kết quả thực tế (Actual)**: 
- **Kết quả kỳ vọng (Expected)**: 

## 2. Phân Tích Nguyên Nhân Gốc Rễ (Root Cause Analysis)
- **Vị trí mã nguồn liên quan**: `path/to/file.ext#L10`
- **Nguyên nhân cốt lõi**: 

## 3. Kế Hoạch Sửa Chữa (Scoping the Fix)
- **Giải pháp tối thiểu, an toàn**: 
- **Nguy cơ hồi quy (Regression Risks)**: 

## 4. Kiểm Thử Xác Nhận (Verification)
- [ ] Đã viết test case tái hiện lỗi thành công trước khi sửa.
- [ ] Đã triển khai bản sửa lỗi.
- [ ] Test case đã PASS sau khi sửa.
- [ ] Toàn bộ test suite dự án PASS không hồi quy.
"""
