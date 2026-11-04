"""Spec and Project conformance validator for DevSpec Kit."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ValidationReport:
    has_constitution: bool = False
    specs_count: int = 0
    tasks_count: int = 0
    completed_tasks: int = 0
    pending_tasks: int = 0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def validate_project(project_dir: Path) -> ValidationReport:
    """Validates the SDD artifacts inside a project."""
    report = ValidationReport()
    devspec_dir = project_dir / ".devspec"

    if not devspec_dir.exists():
        report.errors.append("Chưa tìm thấy thư mục cấu hình `.devspec/`. Hãy chạy `devspec init`.")
        return report

    constitution = devspec_dir / "constitution.md"
    if constitution.exists() and constitution.stat().st_size > 50:
        report.has_constitution = True
    else:
        report.warnings.append("Chưa có hiến pháp dự án `.devspec/constitution.md` hoặc nội dung còn trống.")

    specs_dir = devspec_dir / "specs"
    if specs_dir.exists():
        for feature_dir in specs_dir.iterdir():
            if feature_dir.is_dir():
                spec_file = feature_dir / "spec.md"
                if spec_file.exists():
                    report.specs_count += 1

                tasks_file = feature_dir / "tasks.md"
                if tasks_file.exists():
                    lines = tasks_file.read_text(encoding="utf-8").splitlines()
                    for line in lines:
                        clean = line.strip()
                        if clean.startswith("- [x]"):
                            report.tasks_count += 1
                            report.completed_tasks += 1
                        elif clean.startswith("- [ ]"):
                            report.tasks_count += 1
                            report.pending_tasks += 1

    return report
