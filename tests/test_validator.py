"""Tests for DevSpec validator."""

import tempfile
from pathlib import Path

from devspec.validator import validate_project


def test_validate_nonexistent_project():
    with tempfile.TemporaryDirectory() as tmpdir:
        report = validate_project(Path(tmpdir))
        assert len(report.errors) > 0
        assert not report.has_constitution


def test_validate_healthy_project():
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        devspec = tmp_path / ".devspec"
        devspec.mkdir()
        (devspec / "constitution.md").write_text("# Constitution\n" + "x" * 100, encoding="utf-8")

        feature_dir = devspec / "specs" / "my-feature"
        feature_dir.mkdir(parents=True)
        (feature_dir / "spec.md").write_text("# Spec", encoding="utf-8")
        (feature_dir / "tasks.md").write_text("- [x] Task 1\n- [ ] Task 2\n", encoding="utf-8")

        report = validate_project(tmp_path)
        assert report.has_constitution
        assert report.specs_count == 1
        assert report.tasks_count == 2
        assert report.completed_tasks == 1
        assert report.pending_tasks == 1
        assert len(report.errors) == 0
