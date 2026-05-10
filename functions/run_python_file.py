import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f"Error: Cannot execute '{file_path}' as it is outside the permitted working directory"

        if not os.path.isfile(target_file):
            return f"Error: '{file_path}' does not exist or is not a regular file"

        if not target_file.endswith(".py"):
            return f"Error: '{file_path}' is not a Python file"

        commands = ["python", target_file]
        if args:
            commands.extend(args)

        completed_process = subprocess.run(
            commands, capture_output=True, cwd=working_directory, timeout=30, text=True
        )

        output_lines = []

        if completed_process.returncode != 0:
            output_lines.append(
                f"Process exited with code {completed_process.returncode}"
            )

        if not completed_process.stdout and not completed_process.stderr:
            output_lines.append("No output produced")
        else:
            if completed_process.stdout:
                output_lines.append(f"STDOUT:\n{completed_process.stdout.strip()}")
            if completed_process.stderr:
                output_lines.append(f"STDERR:\n{completed_process.stderr.strip()}")

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of arguments to pass to the Python script",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)
