def format_markdown(data, no_newline, level=0):
    result = []
    for folder_name, folder_data in data.items():
        result.append(f"{'  ' * level}- **{folder_name}/**")
        result.extend(format_markdown_entry(
            folder_data, no_newline, level + 1))
    return "\n".join(result)


def format_markdown_entry(entry, no_newline, level):
    result = []
    if entry["type"] == "directory":
        for child in entry["children"]:
            for child_name, child_data in child.items():
                result.append(
                    f"{'  ' * level}- **{child_name}** ({child_data['type']})")
                if child_data["type"] == "directory":
                    result.extend(format_markdown_entry(
                        child_data, no_newline, level + 1))
                elif "content" in child_data:
                    content = child_data["content"]
                    if content:
                        if no_newline:
                            content = content.replace("\n", " ")
                        result.append(f"{'  ' * (level + 1)}- Content:")
                        result.append(f"```")
                        result.append(f"{content}")
                        result.append(f"```")
                    else:
                        result.append(
                            f"{'  ' * (level + 1)}- Content: `(empty)`")
    return result
