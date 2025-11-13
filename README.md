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

## The PEAR Loop 🍐: Your AI Management Framework

**P**lan → **E**xecute → **A**ssess → **R**epeat

Manage your AI pair programmer like a junior developer through this proven cycle:

### 1. Plan (Define Before Coding)

**Never start with code.** Planning in `/ask` mode prevents wasted effort and costly mistakes.

**Create Your Project Brain:**
```bash
mkdir context
```

**Step 1: Draft the PRD (Product Requirements Document)**

Use `/ask` mode to collaborate on requirements without triggering any code changes:

```
/ask Help me draft a context/PRD.md for a Python retirement planning library. 
Include a prime directive and core features like calculating future value of 
investments with regular contributions.
```

The AI will suggest a structure. Review it, refine it, then ask:
```
/code Create the context/PRD.md file with the requirements we just discussed.
```

**Step 2: Break Down Into Tasks**

Once you have requirements, create an actionable task list:

```
/ask Based on the PRD, create a numbered list of tasks for context/TASKS.md. 
Use Test-Driven Development (TDD). Start with a test for calculating future 
value of regular contributions.
```

Review the proposed tasks. Are they small enough? In the right order? Once satisfied:
```
/code Create context/TASKS.md with the task list we discussed.
```

**Why This Works:**
- `/ask` mode lets you iterate on ideas without creating files you'll immediately delete
- Clear requirements prevent the AI from making incorrect assumptions
- A task list gives you checkpoints to validate progress
- TDD ensures quality from the start

### 2. Execute (Run Specific Tasks)

With a plan in place, execute one task at a time. Be specific:

```
Implement task #1 from context/TASKS.md
```

**What Happens:**
1. Aider reads the task from your context files
2. It proposes changes and shows you a `diff`
3. It asks permission to commit
4. Upon approval, it commits with a descriptive message

**Pro Tips:**
- Work on ONE task at a time
- Reference tasks by number: "Implement task #3"
- Let Aider commit after each task for clean Git history

### 3. Assess (Critical Review Phase)

**This is your most important role.** You are the senior developer reviewing a junior's work.

**Review the Code:**
- Read the `diff` carefully before accepting
- Does the logic make sense?
- Are there edge cases missed?
- Does it follow the requirements?

**Run the Tests:**
```bash
!uv run pytest
```

The `!` prefix runs the command and pastes output into chat for your review.

**Common Issues to Check:**
- **Test Logic:** Is the test actually testing the right thing?
- **Edge Cases:** Zero values, negative numbers, empty inputs
- **Formula Accuracy:** Especially for calculations (compound interest, etc.)
- **Type Handling:** String vs. number conversions

**When Tests Fail:**
Paste the **entire error traceback** into the chat. Don't summarize—the AI needs full context.

### 4. Repeat (Provide Specific Feedback)

Based on your assessment, give clear, actionable feedback or move to the next task.

**Feedback Quality Matters:**

❌ **Vague (Unhelpful):**
- "That's wrong"
- "Doesn't work"
- "Fix the bug"

✅ **Specific (Effective):**
- "The test failed with `TypeError: unsupported operand type(s) for *: 'str' and 'int'`. Cast the `user_input` variable to int before passing to `calculate()`"
- "The formula should use compound interest (FV = P(1+r)^n), not simple interest"
- "Missing edge case: function should handle rate=0 without division by zero"

**When to Move Forward:**
- Tests pass ✓
- Code quality looks good ✓
- Edge cases handled ✓

Mark the task complete in `TASKS.md` and start the loop again with the next task.

**When to Clear Context:**
After completing several tasks, use `/clear` to start fresh and save tokens. The `context/` files persist, so your plan remains intact.

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
