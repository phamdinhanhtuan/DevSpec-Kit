"""AI Coding Agent Integrations Generator for DevSpec Kit.

Generates native configuration and commands for:
- Google Antigravity (agy)
- Cursor (cursor)
- GitHub Copilot (copilot)
- Claude Code (claude)
- Google Gemini CLI (gemini)
"""

from pathlib import Path

SKILLS = [
    {
        "id": "speckit-constitution",
        "name": "Project Constitution",
        "desc": "Thiết lập hoặc cập nhật 6 nguyên tắc kỹ thuật cốt lõi của dự án.",
        "prompt": "Đọc file .devspec/constitution.md. Hướng dẫn lập trình viên xác định các tiêu chuẩn kỹ thuật bất biến về chất lượng code, kiểm thử, và phong cách lập trình cho dự án này.",
    },
    {
        "id": "speckit-specify",
        "name": "Feature Specification",
        "desc": "Soạn thảo bản đặc tả tính năng mới (spec.md) từ yêu cầu người dùng.",
        "prompt": "Hỏi rõ yêu cầu của người dùng, phân tích bài toán, xác định phạm vi In-Scope / Out-of-Scope và viết tài liệu spec.md theo mẫu chuẩn trong .devspec/specs/<feature>/spec.md.",
    },
    {
        "id": "speckit-clarify",
        "name": "Clarification Gate",
        "desc": "Rà soát điểm mơ hồ, hỏi người dùng và chốt quyết định trước khi code.",
        "prompt": "Đọc bản spec hiện tại. Liệt kê 3-5 câu hỏi cụ thể đối với những điểm chưa rõ ràng hoặc các trường hợp ngoại lệ (edge cases). Chờ người dùng trả lời và cập nhật vào spec.",
    },
    {
        "id": "speckit-plan",
        "name": "Architecture Planning",
        "desc": "Lập kế hoạch kiến trúc, tech stack, cấu trúc thư mục và API contracts.",
        "prompt": "Dựa trên spec.md đã làm rõ, lập kế hoạch kỹ thuật chi tiết plan.md. Xác định rõ cấu trúc module, data models, các interfaces và chiến lược kiểm thử.",
    },
    {
        "id": "speckit-tasks",
        "name": "Task Breakdown",
        "desc": "Phân rã kế hoạch thành danh sách nhiệm vụ có thể kiểm chứng độc lập.",
        "prompt": "Chuyển đổi plan.md thành danh sách công việc tasks.md chia theo các pha tuần tự. Mỗi task phải có tiêu chí hoàn thành và bài test tương ứng.",
    },
    {
        "id": "speckit-implement",
        "name": "Disciplined Implementation",
        "desc": "Thực thi code tuần tự từng task trong tasks.md theo chuẩn TDD.",
        "prompt": "Thực hiện task tiếp theo chưa hoàn thành trong tasks.md. Viết test trước, viết code xử lý, chạy test pass 100%, sau đó đánh dấu hoàn thành [x] và báo cáo người dùng duyệt.",
    },
    {
        "id": "speckit-converge",
        "name": "Convergence & Verification",
        "desc": "Kiểm thử hội tụ, đối chiếu toàn diện với spec.md và nghiệm thu.",
        "prompt": "Chạy toàn bộ test suites của dự án, kiểm tra linter/type-check, và đối chiếu 100% acceptance criteria trong spec.md để xác nhận trạng thái Hoàn Tất (Converged).",
    },
    {
        "id": "speckit-bug",
        "name": "Bug Diagnostic & Fix",
        "desc": "Quy trình chẩn đoán, tái hiện bằng test, sửa lỗi và nghiệm thu an toàn.",
        "prompt": "Phân tích triệu chứng lỗi, xác định nguyên nhân gốc rễ, viết test case tái hiện lỗi, thực hiện bản sửa lỗi tối thiểu và xác nhận không có hồi quy.",
    },
]


def setup_antigravity(target_dir: Path) -> list[str]:
    """Generates skills for Google Antigravity IDE."""
    created = []
    base = target_dir / ".agents" / "skills"
    for skill in SKILLS:
        skill_dir = base / skill["id"]
        skill_dir.mkdir(parents=True, exist_ok=True)
        content = f"""---
name: {skill["id"]}
description: {skill["desc"]}
---

# {skill["name"]}

{skill["prompt"]}
"""
        skill_file = skill_dir / "SKILL.md"
        skill_file.write_text(content, encoding="utf-8")
        created.append(str(skill_file.relative_to(target_dir)))
    return created


def setup_cursor(target_dir: Path) -> list[str]:
    """Generates rules for Cursor IDE."""
    rules_dir = target_dir / ".cursor" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    rule_file = rules_dir / "spec-driven-development.mdc"

    commands_summary = "\n".join(
        [f"- `/{s['id']}`: {s['desc']}" for s in SKILLS]
    )

    content = f"""---
description: Spec-Driven Development (SDD) Workflow Rules
globs: ["**/*"]
alwaysApply: true
---

# Spec-Driven Development Workflow

Dự án này áp dụng phương pháp phát triển theo đặc tả (**Spec-Driven Development**).
Khi làm việc với người dùng, hãy tuân thủ các quy tắc sau:

1. **Hiến pháp**: Đọc và bám sát `.devspec/constitution.md`.
2. **Kỷ luật SDD**: Không được tự ý viết code nếu chưa có spec hoặc task tương ứng.
3. **Các lệnh hỗ trợ**:
{commands_summary}
"""
    rule_file.write_text(content, encoding="utf-8")
    return [str(rule_file.relative_to(target_dir))]


def setup_copilot(target_dir: Path) -> list[str]:
    """Generates prompts for GitHub Copilot."""
    prompts_dir = target_dir / ".github" / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    created = []
    for skill in SKILLS:
        pfile = prompts_dir / f"{skill['id']}.prompt.md"
        pfile.write_text(f"# {skill['name']}\n\n{skill['prompt']}\n", encoding="utf-8")
        created.append(str(pfile.relative_to(target_dir)))
    return created


def setup_claude(target_dir: Path) -> list[str]:
    """Generates commands for Claude Code."""
    commands_dir = target_dir / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)
    created = []
    for skill in SKILLS:
        cfile = commands_dir / f"{skill['id']}.md"
        cfile.write_text(f"# {skill['name']}\n\n{skill['prompt']}\n", encoding="utf-8")
        created.append(str(cfile.relative_to(target_dir)))
    return created


def generate_agent_integration(agent: str, target_dir: Path) -> list[str]:
    """Generates integration files for specified agent."""
    agent = agent.lower().strip()
    if agent in ("agy", "antigravity"):
        return setup_antigravity(target_dir)
    elif agent == "cursor":
        return setup_cursor(target_dir)
    elif agent == "copilot":
        return setup_copilot(target_dir)
    elif agent == "claude":
        return setup_claude(target_dir)
    else:
        # Default to antigravity & cursor
        res = setup_antigravity(target_dir)
        res.extend(setup_cursor(target_dir))
        return res
