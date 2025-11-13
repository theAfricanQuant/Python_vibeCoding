# Aider: AI Pair Programmer

Aider is a terminal-based AI pair programmer that works directly with your local files and Git. It builds a map of your entire codebase for informed code editing.

## Installation

### Recommended: Using `uv`

This method creates an isolated environment and automatically installs Python 3.12 if needed.

```bash
# Install uv
python -m pip install uv

# Install aider
uv tool install --force --python python3.12 --with pip aider-chat@latest
```

<details>
<summary>Alternative Installation Methods</summary>

**One-Liners:**
```bash
# Mac/Linux
curl -LsSf https://aider.chat/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://aider.chat/install.ps1 | iex"
```

**Using pipx:**
```bash
python -m pip install pipx
pipx install aider-chat
```
</details>

---

## Configuration

Create `~/.aider.conf.yml` with your API keys and default model.

**Option 1: OpenRouter (Recommended - One key, many models)**
```yaml
api-key:
  - openrouter=sk-or-v1-xxx...  # Get from https://openrouter.ai

model: openrouter/anthropic/claude-3.5-sonnet
cache-prompts: true
```

**Option 2: Multiple Providers**
```yaml
api-key:
  - openrouter=sk-or-v1-xxx...     # https://openrouter.ai
  - gemini=AIza...                 # https://aistudio.google.com/api-keys
  - anthropic=sk-ant-xxx...        # https://console.anthropic.com/keys
  - deepseek=sk-xxx...             # https://platform.deepseek.com/api_keys

# Choose which to use by default
model: gemini/gemini-2.0-flash-exp
cache-prompts: true
```

### Install Provider Libraries

When using keys directly (not through OpenRouter), install the provider's library:

```bash
# For Gemini
uv tool run --from aider-chat pip install google-generativeai

# For Anthropic (Claude)
uv tool run --from aider-chat pip install anthropic
```

### Recommended Models (Fall 2025)

- `openrouter/z-ai/glm-4.6`
- `openrouter/qwen/qwen3-next`
- `openrouter/google/gemini-2.5-flash-preview`
- `openrouter/openai/gpt-5` (with reasoning set to low)
- `openrouter/anthropic/claude-3.5-sonnet`

---

## Git Integration

**Aider must run inside a git repository.** It automatically stages and commits every change with descriptive messages, creating an auditable history you can review or undo with standard git commands.

---

## Core Workflow: The Iterative Loop

Treat the AI as a junior developer you manage through structured iterations:

### 1. Define (Plan)
Plan before coding. Use `/ask` to discuss without editing files.

**Best Practice:** Create a `context/` directory with:
- `PRD.md` - Product requirements
- `TASKS.md` - Numbered task list

Example: `/ask "How should we structure this feature?"`

### 2. Execute (Generate)
Give specific instructions to write code.

Example: `"Implement task #1 from context/TASKS.md"`

Aider will show a diff and request permission to commit.

### 3. Check (Verify)
**Critical step:** Review the diff and run tests. Paste full error tracebacks into chat if tests fail.

### 4. Repeat (Feedback)
Provide specific feedback based on results.

- ❌ Weak: "That's wrong"
- ✅ Strong: "The test failed with TypeError. Cast user_input to integer before passing to calculate()"

---

## Essential Commands

- `/add [file]` / `/drop [file]` - Manage files in AI context
- `/ask [prompt]` - Discuss without editing files
- `/code [prompt]` - Default mode for code editing
- `/test [command]` - Run tests and auto-fix failures
- `/clear` - Clear chat history (saves tokens)
- `/tokens` - Check token usage
- `/model [name]` - Switch models mid-chat

---

## Modern Python Setup with `uv`

Use `uv` to manage projects you build with aider:

```bash
# Initialize project
uv init --library my-new-project
cd my-new-project
```

**Configure `pyproject.toml`:**
```toml
[dependency-groups]
dev = [
    "pytest>=8.3.5",
    "ruff>=0.13.1",
]
```

**Test inside aider:**
```bash
# Auto-fix on failure (-x stops on first error)
/test uv run pytest -x

# Manual review
!uv run pytest
```

The `-x` flag helps AI focus on one problem at a time.
