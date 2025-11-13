# Aider: AI Pair Programmer

This guide covers the recommended installation, configuration, and core workflow for using `aider`, the terminal-based AI pair programmer.

Aider works directly with your local files and integrates deeply with **Git**. It builds a map of your entire codebase, allowing it to make more informed decisions when editing code.

## 🚀 Recommended Installation (with `uv`)

This is the preferred method for installing `aider`. It uses `uv` to create an isolated environment, preventing conflicts with other packages. If needed, `uv` will automatically install a separate Python 3.12 just for `aider` to use.

```bash
# 1. Install uv (if you don't have it)
python -m pip install uv

# 2. Install aider using uv's tool installer
uv tool install --force --python python3.12 --with pip aider-chat@latest
```

\<details\>
\<summary\>Other Installation Methods\</summary\>

### One-Liners (Mac, Linux & Windows)

These one-liners will install `aider` along with Python 3.12 if needed.

  * **Mac & Linux:**
    ```bash
    curl -LsSf https://aider.chat/install.sh | sh
    ```
  * **Windows (in PowerShell):**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://aider.chat/install.ps1 | iex"
    ```

### Install with `pipx`

```bash
# 1. Install pipx (if you need to)
python -m pip install pipx

# 2. Install aider
pipx install aider-chat
```

\</details\>

-----

## ⚙️ Configuration (Required)

Before you can use `aider`, you must provide an API key. The best way is in a config file.

1.  Create a file at `~/.aider.conf.yml`.
2.  Add your API key(s) and set a default model.

Using **OpenRouter** is highly recommended as it gives you access to many different models (like Claude, GPT, Gemini, etc.) through a single API.

Here is an example `.aider.conf.yml` using OpenRouter:

```yaml
# ~/.aider.conf.yml

# 1. Add your OpenRouter API key
# Get one from https://openrouter.ai
api-key:
 - openrouter=YOUR_OPENROUTER_API_KEY_HERE

# 2. Set your default model
# This uses Claude 3.5 Sonnet via OpenRouter
model: openrouter/anthropic/claude-3.5-sonnet

# 3. Optional: Enable caching to save on costs
cache-prompts: true
```

-----

## Git Integration (Important\!)

**Aider must be run inside a git repository.**

This is its core strength. Aider automatically **stages and commits** every change it makes with a descriptive commit message. This creates a perfect, auditable history of the AI's work, which you can review, amend, or undo with standard `git` commands.

-----

## 💻 Core Workflow: The Iterative Loop

The most effective way to use `aider` is not with a single "one-shot" prompt. Instead, treat the AI as a junior developer you manage through a structured, iterative process.

### 1\. Define (Plan Your Work)

Don't just start coding. First, plan your requirements.

  * Use the `/ask` command (e.g., `/ask "How should we structure this feature?"`) to discuss the plan with the AI *without* it editing files.
  * **Best Practice:** Create a `context/` directory. Inside, add a `PRD.md` (Product Requirements) and a `TASKS.md` (a numbered task list). This gives the AI a "brain" for the project.

### 2\. Execute (Generate Code)

Once you have a plan, tell the AI to perform a task.

  * Switch to the default `/code` mode (or just type your prompt).
  * Be specific: "Implement task \#1 from `context/TASKS.md`."
  * Aider will write the code, show you a `diff`, and ask for permission to commit.

### 3\. Check (Verify the Output)

**This is the most critical step.** You are the senior developer. Never trust the AI's output blindly.

  * Critically review the code `diff`.
  * Run your tests. If you see a failure, **paste the entire error traceback** directly into the chat.

### 4\. Repeat (Provide Feedback)

Based on your check, provide clear, specific feedback.

  * **Weak Feedback:** "That's wrong."
  * **Strong Feedback:** "The test failed with a `TypeError`. You need to cast the `user_input` variable to an integer before passing it to the `calculate` function."

Repeat this **Define -\> Execute -\> Check -\> Repeat** cycle for each task.

-----

## 🐍 Modern Python Setup (using `uv`)

`uv` is not just for installing `aider`; it's perfect for managing the projects you *build* with `aider`.

1.  **Initialize Your Project:**
    Use `uv` to create a modern project structure.

    ```bash
    uv init --library my-new-project
    cd my-new-project
    ```

    This creates a `src/` layout and a `pyproject.toml`.

2.  **Configure `pyproject.toml`:**
    Set up your development dependencies (like `pytest` and `ruff`) using `uv`'s `dependency-groups`.

    ```toml
    [dependency-groups]
    dev = [
        "pytest>=8.3.5",
        "ruff>=0.13.1",
    ]
    ```

3.  **Test with `uv` inside `aider`:**
    You can run `uv` commands directly from the `aider` prompt to test the AI's changes.

      * **Run and auto-fix:**

        ```
        /test uv run pytest -x
        ```

        This command runs `pytest` (using `uv`). If it fails, `aider` will automatically try to fix the error. The `-x` flag (stop on first error) is highly recommended as it makes it easier for the AI to focus on one problem at a time.

      * **Run and review manually:**

        ```
        !uv run pytest
        ```

        This runs the command and pastes the output into the chat for you to review.

-----

## 🔥 Essential Commands

  * `/add [file]` / `/drop [file]`: Add or remove files from the AI's context.
  * `/ask [prompt]`: Ask a question or plan *without* letting the AI edit files.
  * `/code [prompt]`: The default mode. Give instructions for the AI to edit files.
  * `/test [command]`: Run a test command and automatically try to fix failures.
  * `/clear`: Clears the chat history to start a new task with a clean slate (saves tokens\!).
  * `/tokens`: Check how many tokens your current context is using (and costing).
  * `/model [model_name]`: Switch models mid-chat (e.g., `/model openrouter/openai/gpt-4o`).

## 🧠 Recommended Models (as of Fall 2025)

  * `openrouter/z-ai/glm-4.6`
  * `openrouter/qwen/qwen3-next`
  * `openrouter/google/gemini-2.5-flash-preview`
  * `openrouter/openai/gpt-5` (with reasoning set to low)
