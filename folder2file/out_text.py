def format_text(data):
    result = []
    for folder_name, entries in data.items():
        result.append(f"{folder_name}/")
        for entry in entries:
            result.extend(format_text_entry(entry, 1))
    return "\n".join(result)


def format_text_entry(entry, level):
    result = []
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
