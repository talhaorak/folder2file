import json
from typing import Dict, Any


def format_json(data: Dict[str, Any], no_newline: bool) -> str:
    """
    Format the data as a JSON string.

    Args:
        data: The data to format
        no_newline: Whether to remove newlines from the output

    Returns:
        The formatted JSON string
    """
    if no_newline:
        return json.dumps(data, separators=(',', ':'))
    return json.dumps(data, indent=2)
