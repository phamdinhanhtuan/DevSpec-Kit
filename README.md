<div align="center">
    <h1>🌱 DevSpec Kit</h1>
    <h3><em>Build with a spec, clarify ambiguity, and implement with precision — with your coding agent.</em></h3>
    <p>A modern, lightweight, and independent Spec-Driven Development (SDD) toolkit designed for AI coding assistants.</p>
</div>

<p align="center">
    <a href="https://github.com/phamdinhanhtuan/DevSpec-Kit/actions/workflows/ci.yml"><img src="https://github.com/phamdinhanhtuan/DevSpec-Kit/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
    <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"/></a>
    <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.10+"/>
    <a href="https://github.com/phamdinhanhtuan"><img src="https://img.shields.io/badge/author-phamdinhanhtuan-orange.svg" alt="Author"/></a>
</p>

<p align="center">
    <strong>English</strong> ·
    <a href="./README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

---

## 🌟 What is DevSpec Kit?

**DevSpec Kit** provides AI coding agents (Google Antigravity, Cursor, GitHub Copilot, Claude Code) with a disciplined, reproducible engineering process:

1. **Constitution**: Establish immutable code quality and architectural principles.
2. **Specify**: Define features clearly before writing any code.
3. **Clarify**: Detect edge cases and actively ask the user rather than guessing.
4. **Plan**: Architecture, tech stack, data models, and API contracts.
5. **Tasks**: Break plans down into testable, discrete units of work.
6. **Implement**: Test-driven implementation, one task at a time.
7. **Converge**: Verify against acceptance criteria and test suites.
8. **Bug Fix**: Triage, reproduce with a test, fix cleanly, and verify no regressions.

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/phamdinhanhtuan/DevSpec-Kit.git
cd DevSpec-Kit

# Install locally in editable mode
pip install -e .
```

Or run directly without installation via script:
```bash
./scripts/devspec.sh --help
```

### 2. Initialize in your project

```bash
# For Google Antigravity IDE (default)
devspec init my-app --agent agy

# For Cursor
devspec init my-app --agent cursor

# For GitHub Copilot
devspec init my-app --agent copilot
```

---

## ⚡ CLI Commands

| Command | Description | Artifact Output |
| --- | --- | --- |
| `devspec init [name]` | Initialize SDD scaffold & agent skills | `.devspec/`, `.agents/skills/` |
| `devspec constitution` | Create or view project constitution | `.devspec/constitution.md` |
| `devspec spec <name>` | Create a new feature specification | `.devspec/specs/<slug>/spec.md` |
| `devspec clarify <name>` | Create clarification log for edge cases | `.devspec/specs/<slug>/clarify.md` |
| `devspec plan <name>` | Create technical & architecture plan | `.devspec/specs/<slug>/plan.md` |
| `devspec tasks <name>` | Break down plan into testable tasks | `.devspec/specs/<slug>/tasks.md` |
| `devspec bug <name>` | Create structured bug fix workspace | `.devspec/bugs/<slug>/bug.md` |
| `devspec check` | Validate SDD health and progress report | Interactive terminal table |

---

## 🤖 Supported AI Coding Agents

- **Google Antigravity (`agy`)**: Native skill definitions in `.agents/skills/`
- **Cursor**: Always-on rules in `.cursor/rules/spec-driven-development.mdc`
- **GitHub Copilot**: Prompt templates in `.github/prompts/`
- **Claude Code**: Custom slash commands in `.claude/commands/`

---

## 📄 License

Author: **Pham Dinh Anh Tuan** ([@phamdinhanhtuan](https://github.com/phamdinhanhtuan))
Licensed under the [MIT License](./LICENSE).
