from typing import Dict, List, Any, Optional


def format_text(data: Dict[str, List[Dict[str, Any]]]) -> str:
    """
    Format the data as a plain text string.

    Args:
        data: The data to format

    Returns:
        The formatted text string
    """
    result: List[str] = []
    for folder_name, entries in data.items():
        result.append(f"{folder_name}/")
        for entry in entries:
            result.extend(format_text_entry(entry, 1))
    return "\n".join(result)


def format_text_entry(entry: Dict[str, Any], level: int) -> List[str]:
    """
    Format a single entry in the data as text.

    Args:
        entry: The entry to format
        level: The current indentation level

    Returns:
        A list of strings representing the formatted entry
    """
    result: List[str] = []
    for name, content in entry.items():
        if isinstance(content, list):  # It's a directory
            result.append(f"{'  ' * level}{name}/")
            for sub_entry in content:
                result.extend(format_text_entry(sub_entry, level + 1))
        else:  # It's a file
            result.append(f"{'  ' * level}{name}")
            if content is not None:
                result.append(f"{'  ' * (level + 1)}{content}")
    return result
