"""Tests for DevSpec CLI."""

import tempfile
from pathlib import Path

from typer.testing import CliRunner

from devspec.cli import app

runner = CliRunner()


def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "DevSpec Kit" in result.stdout
    assert "Pham Dinh Anh Tuan" in result.stdout


def test_cli_init():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(app, ["init", tmpdir, "--agent", "agy"])
        assert result.exit_code == 0
        assert (Path(tmpdir) / ".devspec" / "constitution.md").exists()
        assert (Path(tmpdir) / ".agents" / "skills").exists()


def test_cli_spec_and_check():
    with tempfile.TemporaryDirectory() as tmpdir:
        runner.invoke(app, ["init", tmpdir])
        res_spec = runner.invoke(app, ["spec", "User Profile", "--path", tmpdir])
        assert res_spec.exit_code == 0
        assert (Path(tmpdir) / ".devspec" / "specs" / "user-profile" / "spec.md").exists()

        res_check = runner.invoke(app, ["check", "--path", tmpdir])
        assert res_check.exit_code == 0
        assert "Báo Cáo Kiểm Tra" in res_check.stdout
