"""Tests for DevSpec templates."""

from devspec.templates import (
    BUG_TEMPLATE,
    CLARIFY_TEMPLATE,
    CONSTITUTION_TEMPLATE,
    PLAN_TEMPLATE,
    SPEC_TEMPLATE,
    TASKS_TEMPLATE,
)


def test_constitution_template_has_6_principles():
    assert "Hiến Pháp Dự Án" in CONSTITUTION_TEMPLATE
    assert "1. Đơn giản trước" in CONSTITUTION_TEMPLATE
    assert "2. Bám sát Đặc tả" in CONSTITUTION_TEMPLATE
    assert "3. Kỷ luật Kiểm thử" in CONSTITUTION_TEMPLATE
    assert "4. Không giả định khi mơ hồ" in CONSTITUTION_TEMPLATE
    assert "5. Kiểm soát Từng bước có Duyệt" in CONSTITUTION_TEMPLATE
    assert "6. Giao tiếp & Tài liệu Chuẩn mực" in CONSTITUTION_TEMPLATE


def test_spec_template_formatting():
    formatted = SPEC_TEMPLATE.format(title="Đặt Phòng Khách Sạn", slug="booking", date="2026-11-04")
    assert "Đặt Phòng Khách Sạn" in formatted
    assert "booking" in formatted
    assert "Acceptance Criteria" in formatted


def test_plan_template_formatting():
    formatted = PLAN_TEMPLATE.format(title="Thanh Toán MoMo", slug="momo-payment")
    assert "Thanh Toán MoMo" in formatted
    assert "Tech Stack" in formatted


def test_tasks_template_formatting():
    formatted = TASKS_TEMPLATE.format(title="Xác Thực", slug="auth")
    assert "Pha 1" in formatted
    assert "Pha 2" in formatted
    assert "Task 1.1" in formatted


def test_bug_template_formatting():
    formatted = BUG_TEMPLATE.format(slug="login-crash", date="2026-11-04")
    assert "login-crash" in formatted
    assert "Root Cause Analysis" in formatted
