from typing import Dict, List, Any, Optional, Union


def format_markdown(data: Dict[str, List[Dict[str, Any]]], no_newline: bool, level: int = 0) -> str:
    """
    Format the data as a Markdown string.

    Args:
        data: The data to format
        no_newline: Whether to remove newlines from the content
        level: The current indentation level

    Returns:
        The formatted Markdown string
    """
    result: List[str] = []
    for folder_name, entries in data.items():
        result.append(f"{'  ' * level}- **{folder_name}/**")
        for entry in entries:
            result.extend(format_markdown_entry(entry, no_newline, level + 1))
    return "\n".join(result)


def format_markdown_entry(entry: Dict[str, Any], no_newline: bool, level: int) -> List[str]:
    """
    Format a single entry in the data as Markdown.

    Args:
        entry: The entry to format
        no_newline: Whether to remove newlines from the content
        level: The current indentation level

    Returns:
        A list of strings representing the formatted entry
    """
    result: List[str] = []
    for name, content in entry.items():
        if isinstance(content, list):  # It's a directory
            result.append(f"{'  ' * level}- **{name}/**")
            for sub_entry in content:
                result.extend(format_markdown_entry(
                    sub_entry, no_newline, level + 1))
        else:  # It's a file
            result.append(f"{'  ' * level}- **{name}**")
            if content is not None:
                if no_newline:
                    content = content.replace("\n", " ")
                result.append(f"{'  ' * (level + 1)}```")
                result.append(f"{'  ' * (level + 1)}{content}")
                result.append(f"{'  ' * (level + 1)}```")
            else:
                result.append(f"{'  ' * (level + 1)}`(content skipped)`")
    return result
