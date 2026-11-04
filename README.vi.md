# 🌱 Spec Kit (Phiên bản Cá nhân hóa - Phạm Đình Anh Tuấn)

> **Build with a spec, fix a bug, or assess an idea — with your coding agent.**  
> Bộ công cụ tiêu chuẩn hóa quy trình phát triển theo đặc tả (**Spec-Driven Development - SDD**) dành riêng cho **Phạm Đình Anh Tuấn (phamdinhanhtuan)**, tương thích 100% với [github/spec-kit](https://github.com/github/spec-kit) và tự động đồng bộ liên tục.

<p align="center">
  <a href="https://github.com/phamdinhanhtuan/spec-kit"><img src="https://img.shields.io/badge/GitHub-phamdinhanhtuan%2Fspec--kit-blue?logo=github" alt="Repo"/></a>
  <a href="https://github.com/phamdinhanhtuan/spec-kit/actions/workflows/sync-upstream.yml"><img src="https://github.com/phamdinhanhtuan/spec-kit/actions/workflows/sync-upstream.yml/badge.svg" alt="Upstream Sync"/></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/phamdinhanhtuan/spec-kit" alt="License"/></a>
</p>

---

## 📌 Mục Lục
1. [Giới thiệu](#-giới-thiệu)
2. [6 Nguyên tắc Kỹ thuật cốt lõi (Tuan's Standards)](#-6-nguyên-tắc-kỹ-thuật-cốt-lõi)
3. [Quy trình Spec-Driven Development (Chuẩn mực)](#-quy-trình-spec-driven-development)
4. [Cài đặt & Khởi tạo](#-cài-đặt--khởi-tạo)
5. [Các Lệnh Slash Commands trong IDE / Agent Chat](#-các-lệnh-slash-commands)
6. [Sửa lỗi (Bug Fixing) & Đánh giá ý tưởng (Idea Assessment)](#-bug-fixing--idea-assessment)
7. [Cơ chế Tự động Cập nhật từ Upstream](#-cơ-chế-tự-động-cập-nhật-từ-upstream)

---

## 💡 Giới thiệu

**Spec Kit** là bộ công cụ mã nguồn mở cung cấp cho các AI Coding Agents (Antigravity, Cursor, GitHub Copilot, Claude Code, Gemini CLI, v.v.) quy trình làm việc có cấu trúc, khuôn mẫu tái sử dụng và kết quả được tài liệu hóa rõ ràng.

Thay vì yêu cầu AI "viết code ngay" dẫn đến việc code sai lệch, sinh ra lỗi tiềm ẩn hoặc over-engineering, Spec Kit buộc AI phải đi qua các cổng kiểm soát kỹ thuật:
- **Hiến pháp (Constitution)**: Định hình nguyên tắc kiến trúc và tiêu chuẩn code.
- **Đặc tả (Specify)**: Xác định rõ tính năng cần làm và giá trị mang lại.
- **Làm rõ (Clarify)**: Bắt buộc hỏi người dùng khi gặp điểm mơ hồ, không đoán mò.
- **Kế hoạch (Plan)**: Kiến trúc, stack công nghệ, cấu trúc thư mục.
- **Nhiệm vụ (Tasks)**: Phân rã công việc thành từng task nhỏ có thể kiểm chứng.
- **Triển khai (Implement)**: Code từng task một cách có kỷ luật.
- **Hội tụ (Converge)**: Đảm bảo code chạy đúng, vượt qua test suites.

---

## 🛡️ 6 Nguyên tắc Kỹ thuật cốt lõi

Được tích hợp sẵn trong preset `tuan-standards`:

1. **Đơn giản trước (Simplicity First)**: Ưu tiên cách dễ hiểu, tường minh nhất. Không over-engineering.
2. **Bám sát đặc tả (Strict Spec Adherence)**: Không tự ý thêm thư viện hoặc tính năng ngoài spec.
3. **Kỷ luật kiểm thử (Test-Driven Discipline)**: Logic quan trọng bắt buộc phải có automated unit/integration test.
4. **Không giả định khi mơ hồ (Zero Ambiguity Tolerance)**: Điểm nào mơ hồ thì **HỎI người dùng**, tuyệt đối không tự đoán.
5. **Kiểm soát từng bước có duyệt (Step-by-Step Approval)**: Hoàn thành từng bước, chờ người dùng duyệt trước khi sang bước tiếp theo.
6. **Giao tiếp chuẩn mực (Clear Communication)**: Hỗ trợ tiếng Việt và tiếng Anh chuẩn quy trình kỹ thuật.

---

## 🔄 Quy trình Spec-Driven Development

```text
[Người dùng đưa ý tưởng]
           │
           ▼
1. /speckit-constitution  ──► Thiết lập hiến pháp & nguyên tắc dự án
           │
           ▼
2. /speckit-specify       ──► Viết tài liệu đặc tả (spec.md)
           │
           ▼
3. /speckit-clarify       ──► Quét điểm mơ hồ, hỏi và chốt với người dùng
           │
           ▼
4. /speckit-plan          ──► Lập kế hoạch kiến trúc & công nghệ (plan.md)
           │
           ▼
5. /speckit-tasks         ──► Phân rã thành danh sách công việc (tasks.md)
           │
           ▼
6. /speckit-implement     ──► Thực thi code theo từng task
           │
           ▼
7. /speckit-converge      ──► Kiểm thử hội tụ, đối chiếu spec và nghiệm thu
```

---

## 🚀 Cài đặt & Khởi tạo

### 1. Khởi tạo dự án mới với script nhanh
```bash
# Cú pháp: ./scripts/quickstart.sh <tên-dự-án> <integration>
./scripts/quickstart.sh my-app agy
```

### 2. Sử dụng Specify CLI trực tiếp
```bash
# Cài đặt qua uv hoặc pip
pip install -e .

# Khởi tạo dự án với Antigravity (agy), Copilot, hoặc Cursor
specify init my-app --integration agy --preset tuan-standards
cd my-app
```

---

## ⚡ Các Lệnh Slash Commands

Chạy trực tiếp trong khung chat của Agent (Antigravity chat, Copilot chat, Cursor composer, Claude Code):

| Lệnh | Chức năng | Đầu ra |
| --- | --- | --- |
| `/speckit-constitution` | Tạo/cập nhật nguyên tắc dự án | `.specify/constitution.md` |
| `/speckit-specify <mô tả>` | Viết đặc tả tính năng mới | `.specify/specs/<feature>/spec.md` |
| `/speckit-clarify` | Làm rõ các điểm mơ hồ trước khi code | Cập nhật quyết định vào `spec.md` |
| `/speckit-plan` | Lập kế hoạch kỹ thuật, stack, thư viện | `.specify/specs/<feature>/plan.md` |
| `/speckit-tasks` | Chia nhỏ các đầu việc thực thi | `.specify/specs/<feature>/tasks.md` |
| `/speckit-implement` | Triển khai code theo từng task | Source code & Unit tests |
| `/speckit-converge` | Kiểm thử hội tụ & xác nhận hoàn thành | Báo cáo `Converged` |

---

## 🐛 Bug Fixing & Idea Assessment

### Sửa lỗi chuẩn quy trình (Bug Fixing)
```bash
specify extension add bug
```
Trong chat của Agent:
```text
/speckit-bug-assess "Mô tả triệu chứng lỗi" slug=ten-loi
/speckit-bug-fix slug=ten-loi
/speckit-bug-test slug=ten-loi
```

### Đánh giá ý tưởng (Idea Assessment)
```bash
specify extension add assess
```
Trong chat của Agent:
```text
/speckit-assess-intake "Ý tưởng tính năng mới" slug=ten-y-tuong
/speckit-assess-research slug=ten-y-tuong
/speckit-assess-define slug=ten-y-tuong
/speckit-assess-shape slug=ten-y-tuong
/speckit-assess-decide slug=ten-y-tuong
```

---

## 🔄 Cơ chế Tự động Cập nhật từ Upstream

Bộ kit này được cấu hình **2 cơ chế tự động đồng bộ** với bản gốc của GitHub (`https://github.com/github/spec-kit`):

### 1. Tự động qua GitHub Actions CI/CD (`sync-upstream.yml`)
- Chạy định kỳ vào mỗi Chủ nhật lúc 00:00 UTC.
- Cho phép kích hoạt thủ công bất kỳ lúc nào: Vào tab **Actions** trên repo `phamdinhanhtuan/spec-kit` -> Chọn **Sync Upstream Spec-Kit** -> Bấm **Run workflow**.

### 2. Đồng bộ bằng 1 lệnh từ Terminal máy bạn
```bash
./scripts/sync-upstream.sh
```
Script sẽ tự động fetch bản mới nhất từ `github/spec-kit`, merge sạch sẽ và push lên `https://github.com/phamdinhanhtuan/spec-kit` của bạn.

---

**Tác giả**: [Phạm Đình Anh Tuấn](https://github.com/phamdinhanhtuan)  
**Email**: tuanpham26261@gmail.com
