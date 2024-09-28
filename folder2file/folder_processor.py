import os
import base64


def process_folder(config, path=None):
    if path is None:
        path = config.folder_path

    result = {}
    folder_name = os.path.basename(path)
    result[folder_name] = []

    for item in os.listdir(path):
        if not config.include_hidden and item.startswith('.'):
            continue

        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            result[folder_name].append(process_file(item, item_path, config))
        elif os.path.isdir(item_path):
            result[folder_name].append(process_folder(config, item_path))

    return result


def process_file(file_name, file_path, config):
    if is_binary(file_path) and config.skip_binaries:
        return {file_name: None}

    if config.skip_content:
        return {file_name: None}

    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            if is_binary(file_path):
                return {file_name: base64.b64encode(content).decode('utf-8')}
            else:
                return {file_name: content.decode('utf-8')}
    except Exception as e:
        return {file_name: f"Error reading file: {str(e)}"}


def is_binary(file_path):
    """
    Check if a file is binary or text.
    """
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read()
            return False
    except:
        return True
