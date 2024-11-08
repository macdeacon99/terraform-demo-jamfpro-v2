"""shared functions for other scripts in directory"""

import json


def open_artifact(path: str, formatted_string: bool = False) -> dict:
    """
    Opens and reads the outputs.json file created by a workflow and returns its contents as a dictionary.

    Returns:
        dict: The parsed JSON data from the outputs.json file

    Raises:
        FileNotFoundError: If the outputs.json file doesn't exist at DROPFILE_PATH
        JSONDecodeError: If the file contains invalid JSON
    """

    with open(path, "r", encoding="UTF-8") as f:
        if formatted_string:
            return json.dumps(json.load(f), indent=2)
        
        return json.load(f)
    


def wrap_json_markdown(json_string):
    """
    Wraps a JSON string in Markdown code block tags for improved formatting and readability.

    Args:
        json_string (str): The JSON string to be wrapped in Markdown formatting

    Returns:
        str: The input string wrapped in ```json code block tags

    Example:
        >>> wrap_json_markdown('{"key": "value"}')
        ```json
        {"key": "value"}
        ```
    """

    return f"```json\n{json_string}\n```"
