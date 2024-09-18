def format_markdown(data, no_newline, level=0):
    result = []
    for folder_name, entries in data.items():
        result.append(f"{'  ' * level}- **{folder_name}/**")
        for entry in entries:
            result.extend(format_markdown_entry(entry, no_newline, level + 1))
    return "\n".join(result)


def format_markdown_entry(entry, no_newline, level):
    result = []
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
