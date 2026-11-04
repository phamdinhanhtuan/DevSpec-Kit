#!/usr/bin/env bash
# scripts/sync-upstream.sh
# Đồng bộ hóa bộ Spec Kit cá nhân với upstream chính thức của GitHub (https://github.com/github/spec-kit)
set -e

echo "=========================================================="
echo "🌱 Đang đồng bộ Spec Kit với https://github.com/github/spec-kit"
echo "=========================================================="

# 1. Kiểm tra remote upstream
if ! git remote | grep -q "^upstream$"; then
  echo "-> Đang thêm remote upstream..."
  git remote add upstream https://github.com/github/spec-kit.git
fi

# 2. Lấy dữ liệu mới nhất
echo "-> Đang fetch dữ liệu mới nhất từ upstream..."
git fetch upstream main --tags

# 3. Merge upstream/main
echo "-> Đang merge upstream/main vào nhánh hiện tại..."
CURRENT_BRANCH="$(git branch --show-current)"
git merge upstream/main -m "chore(sync): sync with upstream github/spec-kit" --allow-unrelated-histories

# 4. Đẩy lên repo cá nhân
echo "-> Đang push lên https://github.com/phamdinhanhtuan/spec-kit..."
git push origin "$CURRENT_BRANCH"

echo
echo "✅ Đồng bộ thành công! Mã nguồn đã được cập nhật mới nhất từ GitHub Spec Kit."
