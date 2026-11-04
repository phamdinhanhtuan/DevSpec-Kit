# 🌱 DevSpec Kit - Bộ Công Cụ Phát Triển Theo Đặc Tả (SDD)

> **Build with a spec, clarify ambiguity, and implement with precision — with your coding agent.**
> Bộ công cụ tiêu chuẩn hóa quy trình phát triển phần mềm theo đặc tả (**Spec-Driven Development - SDD**) do **Phạm Đình Anh Tuấn (phamdinhanhtuan)** phát triển độc lập, tối ưu riêng cho các trợ lý lập trình AI (Google Antigravity, Cursor, Copilot, Claude Code).

<p align="center">
    <a href="https://github.com/phamdinhanhtuan/spec-kit/actions/workflows/ci.yml"><img src="https://github.com/phamdinhanhtuan/spec-kit/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
    <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="Giấy phép"/></a>
    <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"/>
    <a href="https://github.com/phamdinhanhtuan"><img src="https://img.shields.io/badge/tác_giả-phamdinhanhtuan-orange.svg" alt="Tác giả"/></a>
</p>

<p align="center">
    <a href="./README.md">English</a> ·
    <strong>🇻🇳 Tiếng Việt</strong>
</p>

---

## 📌 Mục Lục
1. [Giới thiệu & Triết lý](#-giới-thiệu--triết-lý)
2. [6 Nguyên tắc Kỹ thuật Bất biến](#-6-nguyên-tắc-kỹ-thuật-bất-biến)
3. [Quy trình Spec-Driven Development 7 Bước](#-quy-trình-7-bước-chuẩn-mực)
4. [Cài đặt & Bắt đầu Nhanh](#-cài-đặt--bắt-đầu-nhanh)
5. [Hướng dẫn Sử dụng CLI](#-hướng-dẫn-sử-dụng-cli)
6. [Tích hợp với AI Coding Agents](#-tích-hợp-ai-coding-agents)
7. [Quy trình Sửa Lỗi (Bug Fixing)](#-quy-trình-sửa-lỗi-bug-fixing)

---

## 💡 Giới thiệu & Triết lý

Khi làm việc với các AI Coding Agents, vấn đề lớn nhất thường gặp là:
- AI tự ý viết code ngay khi chưa hiểu hết yêu cầu.
- Sinh ra code dư thừa (over-engineering), thêm thư viện ngoài phạm vi.
- Tự phỏng đoán khi gặp điểm mơ hồ, dẫn đến kết quả sai lệch so với mong muốn.
- Thiếu kiểm thử (tests) kiểm chứng, khó kiểm soát chất lượng khi dự án lớn dần.

**DevSpec Kit** giải quyết triệt để vấn đề này bằng cách thiết lập **Cổng Kiểm Soát Kỹ Thuật (Stage Gates)** chặt chẽ:
AI chỉ được phép code sau khi đã có bản đặc tả (`spec.md`), đã làm rõ các điểm mơ hồ (`clarify.md`), đã lập kế hoạch kiến trúc (`plan.md`) và phân rã thành các task nhỏ kiểm thử được (`tasks.md`).

---

## 🛡️ 6 Nguyên tắc Kỹ thuật Bất biến

Tất cả các thành viên và AI khi tham gia phát triển dự án phải tuân thủ:

1. **Đơn giản trước (Simplicity First)**: Ưu tiên giải pháp dễ hiểu, tường minh, ngắn gọn. Tuyệt đối không over-engineering.
2. **Bám sát đặc tả (Strict Spec Adherence)**: Không tự ý thêm thư viện ngoài hoặc tính năng nằm ngoài phạm vi spec.
3. **Kỷ luật kiểm thử (Test-Driven Discipline)**: Logic quan trọng bắt buộc có unit test / integration test. Code chưa test chưa được coi là hoàn tất.
4. **Không giả định khi mơ hồ (Zero Ambiguity Tolerance)**: Điểm nào mơ hồ thì **HỎI NGƯỜI DÙNG**, không tự đoán mò.
5. **Kiểm soát từng bước có duyệt (Step-by-Step Approval)**: Hoàn thành từng bước, báo cáo và chờ người dùng duyệt trước khi sang bước tiếp theo.
6. **Giao tiếp chuẩn mực (Clear Communication)**: Hỗ trợ tiếng Việt rõ ràng, kèm thuật ngữ kỹ thuật chuẩn.

---

## 🔄 Quy trình 7 Bước Chuẩn Mực

```text
[Yêu Cầu / Ý Tưởng Mới]
           │
           ▼
1. devspec constitution  ──► Thiết lập hiến pháp & nguyên tắc dự án (.devspec/constitution.md)
           │
           ▼
2. devspec spec <name>   ──► Soạn thảo bản đặc tả tính năng (spec.md)
           │
           ▼
3. devspec clarify <name>──► Rà soát điểm mơ hồ, hỏi và chốt với người dùng (clarify.md)
           │
           ▼
4. devspec plan <name>   ──► Thiết kế kiến trúc, tech stack, data models (plan.md)
           │
           ▼
5. devspec tasks <name>  ──► Phân rã công việc thành danh sách task tuần tự (tasks.md)
           │
           ▼
6. Triển khai theo task  ──► Viết test trước -> Code logic -> Chạy test pass 100% -> Đánh dấu [x]
           │
           ▼
7. devspec check         ──► Kiểm tra tính hội tụ (Convergence), đối chiếu nghiệm thu với spec
```

---

## 🚀 Cài đặt & Bắt đầu Nhanh

### 1. Cài đặt vào máy
```bash
git clone https://github.com/phamdinhanhtuan/spec-kit.git
cd spec-kit

# Cài đặt dạng editable
pip install -e .
```

Hoặc chạy trực tiếp không cần cài đặt:
```bash
./scripts/devspec.sh --help
```

### 2. Khởi tạo vào dự án của bạn
```bash
# Khởi tạo cho Google Antigravity IDE (mặc định)
devspec init my-project --agent agy

# Khởi tạo cho Cursor IDE
devspec init my-project --agent cursor

# Khởi tạo cho GitHub Copilot
devspec init my-project --agent copilot
```

---

## ⚡ Hướng dẫn Sử dụng CLI

| Lệnh CLI | Ý nghĩa | Sản phẩm tạo ra |
| --- | --- | --- |
| `devspec init` | Khởi tạo cấu trúc SDD cho dự án | Thư mục `.devspec/` & cấu hình Agent |
| `devspec constitution` | Tạo hoặc xem hiến pháp dự án | `.devspec/constitution.md` |
| `devspec spec <tên>` | Tạo đặc tả tính năng mới | `.devspec/specs/<slug>/spec.md` |
| `devspec clarify <tên>` | Tạo file rà soát làm rõ mơ hồ | `.devspec/specs/<slug>/clarify.md` |
| `devspec plan <tên>` | Lập kế hoạch kiến trúc kỹ thuật | `.devspec/specs/<slug>/plan.md` |
| `devspec tasks <tên>` | Phân rã nhiệm vụ triển khai | `.devspec/specs/<slug>/tasks.md` |
| `devspec bug <mô-tả>` | Khởi tạo quy trình sửa lỗi | `.devspec/bugs/<slug>/bug.md` |
| `devspec check` | Báo cáo tiến độ và tính tuân thủ | Bảng thống kê trực quan trên terminal |

---

## 🤖 Tích hợp AI Coding Agents

Sau khi chạy `devspec init --agent <loại>`, bộ kit sẽ tự động nạp các lệnh vào môi trường của AI:
- **Google Antigravity (`agy`)**: Tạo các skills trong `.agents/skills/` (gõ `/speckit-specify`, `/speckit-plan`, `/speckit-tasks`, v.v.).
- **Cursor**: Tạo file luật trong `.cursor/rules/spec-driven-development.mdc`.
- **GitHub Copilot**: Tạo prompt templates trong `.github/prompts/`.
- **Claude Code**: Tạo slash commands trong `.claude/commands/`.

---

## 🐛 Quy trình Sửa Lỗi (Bug Fixing)

Khi gặp lỗi trong quá trình vận hành, không sửa mò mà đi qua quy trình:
```bash
devspec bug "loi-dang-nhap-crash"
```
1. **Triệu chứng**: Ghi nhận chính xác bước tái hiện lỗi.
2. **Nguyên nhân gốc rễ (Root Cause)**: Tìm đúng dòng code gây lỗi.
3. **TDD Fix**: Viết test case tái hiện lỗi trước, đảm bảo test FAIL.
4. **Sửa code**: Áp dụng bản sửa tối thiểu an toàn, test PASS 100%.

---

## 📄 Bản Quyền & Tác Giả

- **Tác giả**: **Phạm Đình Anh Tuấn** ([@phamdinhanhtuan](https://github.com/phamdinhanhtuan))
- **Email**: tuanpham26261@gmail.com
- **Giấy phép**: [MIT License](./LICENSE) — Hoàn toàn mở, tự do sử dụng và tùy biến.
