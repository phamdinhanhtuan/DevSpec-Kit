#!/usr/bin/env bash
# scripts/quickstart.sh
# Khởi tạo nhanh dự án mới với Spec Kit và chuẩn của Tuấn
set -e

PROJECT_NAME="${1:-my-project}"
INTEGRATION="${2:-agy}" # agy (Antigravity), copilot, cursor-agent, claude, gemini

echo "=========================================================="
echo "🚀 Khởi tạo dự án: $PROJECT_NAME với Spec Kit"
echo "   Integration: $INTEGRATION"
echo "   Preset: tuan-standards"
echo "=========================================================="

# Cài đặt hoặc chạy specify CLI
if command -v specify >/dev/null 2>&1; then
  specify init "$PROJECT_NAME" --integration "$INTEGRATION" --preset tuan-standards
else
  echo "specify CLI chưa cài global. Sử dụng python module..."
  KIT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
  PYTHONPATH="$KIT_DIR/src" python3 -m specify_cli.main init "$PROJECT_NAME" --integration "$INTEGRATION" --preset tuan-standards
fi

echo
echo "✅ Đã tạo dự án thành công tại: $PROJECT_NAME"
echo "👉 Bước tiếp theo:"
echo "   cd $PROJECT_NAME"
echo "   Mở IDE với coding agent và gõ:"
echo "   1) /speckit-constitution  (Khởi tạo hiến pháp dự án)"
echo "   2) /speckit-specify <mô tả tính năng> (Tạo spec)"
echo "   3) /speckit-clarify       (Làm rõ mơ hồ nếu có)"
echo "   4) /speckit-plan          (Lập kế hoạch kiến trúc)"
echo "   5) /speckit-tasks         (Phân rã task)"
echo "   6) /speckit-implement     (Triển khai code)"
echo "   7) /speckit-converge      (Kiểm thử & hội tụ)"
