# AI Agent

A small CLI coding agent built in Python. It takes a natural-language prompt, uses the Gemini API to inspect a local codebase, and can list files, read code, run Python scripts, and write changes back to disk. The agent works in a loop, calling tools step by step until it can return a final answer.

## Prerequisites

- Python 3.13+
- [`uv`](https://github.com/astral-sh/uv) for dependency management and running commands
- A Gemini API key

## Setup

1. Clone the repository.
2. Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

3. Install dependencies:

    ```bash
    uv sync
    ```

## Usage

Run the agent with a prompt:

```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

Verbose mode shows token usage and tool calls:

```bash
uv run main.py --verbose "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

## How It Works

The agent sends your prompt to Gemini along with a small set of file-system tools. It then loops until it reaches a final response or hits the max iteration count.

Available capabilities:

- List files and directories
- Read file contents
- Run Python files with arguments
- Write or overwrite files
- Restrict operations to a configurable working directory

## Dependencies

- google-genai - Gemini client SDK
- python-dotenv - loads environment variables from .env

## Extension Ideas

- Add a diff-aware editing tool instead of full-file overwrite
- Let the agent run test commands beyond Python scripts
- Add retry/backoff handling for API and subprocess failures
- Track tool-call history and summarize prior steps in verbose mode
- Add file search or grep-style tooling so the agent can locate symbols faster
- Improve the system prompt to enforce safer edit/verify workflows
- Support multiple models or providers behind a shared interface
- Add automated patch validation before writing changes
- Log agent sessions for debugging and prompt iteration
- Expand the example target app beyond the calculator into a larger codebase
