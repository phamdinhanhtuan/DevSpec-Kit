"""Command Line Interface for DevSpec Kit.

Built with Typer and Rich for elegant, interactive terminal experience.
"""

from datetime import date
from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from devspec import __version__
from devspec.generator import generate_agent_integration
from devspec.templates import (
    BUG_TEMPLATE,
    CLARIFY_TEMPLATE,
    CONSTITUTION_TEMPLATE,
    PLAN_TEMPLATE,
    SPEC_TEMPLATE,
    TASKS_TEMPLATE,
)
from devspec.validator import validate_project

app = typer.Typer(
    name="devspec",
    help="🌱 DevSpec Kit - Spec-Driven Development Toolkit for AI Coding Agents",
    add_completion=False,
)
console = Console()


def _slugify(text: str) -> str:
    return text.lower().replace(" ", "-").replace("_", "-").strip()


@app.command("version")
def version():
    """Hiển thị phiên bản DevSpec Kit."""
    rprint(f"[bold green]🌱 DevSpec Kit[/bold green] version [bold cyan]{__version__}[/bold cyan]")
    rprint("Author: [bold]Pham Dinh Anh Tuan[/bold] (@phamdinhanhtuan)")


@app.command("init")
def init(
    project_name: Optional[str] = typer.Argument(None, help="Tên thư mục dự án (để trống nếu khởi tạo tại thư mục hiện tại)"),
    agent: str = typer.Option("agy", "--agent", "-a", help="Trợ lý AI: agy (Antigravity), cursor, copilot, claude"),
):
    """Khởi tạo dự án mới với cấu trúc Spec-Driven Development chuẩn mực."""
    target_dir = Path(project_name) if project_name else Path.cwd()
    target_dir.mkdir(parents=True, exist_ok=True)

    devspec_dir = target_dir / ".devspec"
    specs_dir = devspec_dir / "specs"
    specs_dir.mkdir(parents=True, exist_ok=True)

    # Khởi tạo constitution nếu chưa có
    constitution_file = devspec_dir / "constitution.md"
    if not constitution_file.exists():
        constitution_file.write_text(CONSTITUTION_TEMPLATE, encoding="utf-8")

    # Sinh cấu hình cho Agent
    agent_files = generate_agent_integration(agent, target_dir)

    console.print(
        Panel.fit(
            f"[bold green]🌱 Đã khởi tạo DevSpec Kit thành công![/bold green]\n"
            f"Thư mục: [cyan]{target_dir.resolve()}[/cyan]\n"
            f"AI Agent: [yellow]{agent.upper()}[/yellow] ({len(agent_files)} cấu hình)",
            title="DevSpec Kit",
            border_style="green",
        )
    )


@app.command("constitution")
def constitution(
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo hoặc hiển thị hiến pháp dự án (.devspec/constitution.md)."""
    const_file = path / ".devspec" / "constitution.md"
    if not const_file.exists():
        const_file.parent.mkdir(parents=True, exist_ok=True)
        const_file.write_text(CONSTITUTION_TEMPLATE, encoding="utf-8")
        rprint(f"[green]✓ Đã tạo hiến pháp dự án tại:[/green] [cyan]{const_file}[/cyan]")
    else:
        rprint(f"[bold cyan]Hiến Pháp Dự Án ({const_file}):[/bold cyan]\n")
        console.print(Panel(const_file.read_text(encoding="utf-8"), title="Constitution", border_style="blue"))


@app.command("spec")
def spec(
    feature: str = typer.Argument(..., help="Tên hoặc mô tả ngắn tính năng"),
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo đặc tả tính năng mới (spec.md)."""
    slug = _slugify(feature)
    feature_dir = path / ".devspec" / "specs" / slug
    feature_dir.mkdir(parents=True, exist_ok=True)

    spec_file = feature_dir / "spec.md"
    if spec_file.exists():
        rprint(f"[yellow]! Đặc tả đã tồn tại tại:[/yellow] [cyan]{spec_file}[/cyan]")
    else:
        content = SPEC_TEMPLATE.format(title=feature, slug=slug, date=date.today().isoformat())
        spec_file.write_text(content, encoding="utf-8")
        rprint(f"[green]✓ Đã tạo đặc tả tính năng tại:[/green] [cyan]{spec_file}[/cyan]")


@app.command("clarify")
def clarify(
    feature: str = typer.Argument(..., help="Tên tính năng"),
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo file rà soát làm rõ mơ hồ (clarify.md)."""
    slug = _slugify(feature)
    feature_dir = path / ".devspec" / "specs" / slug
    feature_dir.mkdir(parents=True, exist_ok=True)

    clarify_file = feature_dir / "clarify.md"
    if not clarify_file.exists():
        content = CLARIFY_TEMPLATE.format(slug=slug, date=date.today().isoformat())
        clarify_file.write_text(content, encoding="utf-8")
    rprint(f"[green]✓ File rà soát làm rõ:[/green] [cyan]{clarify_file}[/cyan]")


@app.command("plan")
def plan(
    feature: str = typer.Argument(..., help="Tên tính năng"),
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo kế hoạch kiến trúc kỹ thuật (plan.md)."""
    slug = _slugify(feature)
    feature_dir = path / ".devspec" / "specs" / slug
    feature_dir.mkdir(parents=True, exist_ok=True)

    plan_file = feature_dir / "plan.md"
    if not plan_file.exists():
        content = PLAN_TEMPLATE.format(title=feature, slug=slug)
        plan_file.write_text(content, encoding="utf-8")
    rprint(f"[green]✓ Kế hoạch kiến trúc:[/green] [cyan]{plan_file}[/cyan]")


@app.command("tasks")
def tasks(
    feature: str = typer.Argument(..., help="Tên tính năng"),
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo danh sách nhiệm vụ triển khai tuần tự (tasks.md)."""
    slug = _slugify(feature)
    feature_dir = path / ".devspec" / "specs" / slug
    feature_dir.mkdir(parents=True, exist_ok=True)

    tasks_file = feature_dir / "tasks.md"
    if not tasks_file.exists():
        content = TASKS_TEMPLATE.format(title=feature, slug=slug)
        tasks_file.write_text(content, encoding="utf-8")
    rprint(f"[green]✓ Danh sách nhiệm vụ:[/green] [cyan]{tasks_file}[/cyan]")


@app.command("bug")
def bug(
    issue: str = typer.Argument(..., help="Mô tả ngắn lỗi cần sửa"),
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Tạo hồ sơ chẩn đoán và sửa lỗi (bug.md)."""
    slug = _slugify(issue)
    bugs_dir = path / ".devspec" / "bugs" / slug
    bugs_dir.mkdir(parents=True, exist_ok=True)

    bug_file = bugs_dir / "bug.md"
    if not bug_file.exists():
        content = BUG_TEMPLATE.format(slug=slug, date=date.today().isoformat())
        bug_file.write_text(content, encoding="utf-8")
    rprint(f"[green]✓ Hồ sơ sửa lỗi:[/green] [cyan]{bug_file}[/cyan]")


@app.command("check")
def check(
    path: Path = typer.Option(Path.cwd(), "--path", "-p", help="Thư mục dự án"),
):
    """Kiểm tra tính tuân thủ quy trình Spec-Driven Development trong dự án."""
    report = validate_project(path)

    table = Table(title="Báo Cáo Kiểm Tra Quy Trình SDD")
    table.add_column("Chỉ Số", style="cyan")
    table.add_column("Trạng Thái / Số Lượng", style="bold")

    table.add_row("Hiến pháp (Constitution)", "[green]Đã thiết lập[/green]" if report.has_constitution else "[red]Chưa có[/red]")
    table.add_row("Số lượng đặc tả (Specs)", str(report.specs_count))
    table.add_row("Tổng số nhiệm vụ (Tasks)", str(report.tasks_count))
    table.add_row("Nhiệm vụ hoàn thành", f"[green]{report.completed_tasks}[/green]")
    table.add_row("Nhiệm vụ đang chờ", f"[yellow]{report.pending_tasks}[/yellow]")

    console.print(table)

    if report.errors:
        for err in report.errors:
            rprint(f"[bold red]Lỗi:[/bold red] {err}")
    if report.warnings:
        for warn in report.warnings:
            rprint(f"[bold yellow]Cảnh báo:[/bold yellow] {warn}")


if __name__ == "__main__":
    app()
