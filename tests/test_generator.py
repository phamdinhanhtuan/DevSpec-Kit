"""Tests for Agent Integration generator."""

import tempfile
from pathlib import Path

from devspec.generator import (
    generate_agent_integration,
    setup_antigravity,
    setup_claude,
    setup_copilot,
    setup_cursor,
)


def test_setup_antigravity():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        files = setup_antigravity(tmp_path)
        assert len(files) == 8
        skill_dir = tmp_path / ".agents" / "skills" / "speckit-specify"
        assert skill_dir.exists()
        assert (skill_dir / "SKILL.md").exists()


def test_setup_cursor():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        files = setup_cursor(tmp_path)
        assert len(files) == 1
        rule_file = tmp_path / ".cursor" / "rules" / "spec-driven-development.mdc"
        assert rule_file.exists()


def test_setup_copilot():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        files = setup_copilot(tmp_path)
        assert len(files) == 8
        prompt_file = tmp_path / ".github" / "prompts" / "speckit-specify.prompt.md"
        assert prompt_file.exists()


def test_setup_claude():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        files = setup_claude(tmp_path)
        assert len(files) == 8
        cmd_file = tmp_path / ".claude" / "commands" / "speckit-specify.md"
        assert cmd_file.exists()


def test_generate_agent_integration():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        files = generate_agent_integration("agy", tmp_path)
        assert len(files) == 8
