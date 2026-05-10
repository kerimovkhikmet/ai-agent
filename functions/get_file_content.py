import os

from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f"Error: Cannot read '{target_file}' as it is outside the permitted working directory"

        if not os.path.isfile(target_file):
            return f"Error: File not found or is not a regular file: '{file_path}'"

        with open(target_file) as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += (
                    f"\n[...File '{file_path}' truncated at {MAX_CHARS} characters]"
                )

        return file_content_string

    except Exception as e:
        return f"Error listing file contents: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        required=["file_path"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file relative to the working directory",
            ),
        },
    ),
)
