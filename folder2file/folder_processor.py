import os
import base64
# import fnmatch
from .gitignore_parser import parse_gitignore


class process_folder:
    def __init__(self, config):
        self.config = config
        self.gitignore_patterns = []
        self.result = {}

        gitignore_path = os.path.join(config.folder_path, '.gitignore')
        if not config.no_gitignore and os.path.exists(gitignore_path):
            self.gitignore_matches = parse_gitignore(gitignore_path)
        else:
            self.gitignore_matches = lambda x: False

        folder_name = os.path.basename(config.folder_path)
        if folder_name == '.':
            folder_name = os.path.basename(os.path.abspath(config.folder_path))
        self.result[folder_name] = self.process_folder(config.folder_path)

    def process_folder(self, folder_path):
        result = []

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            item_name = item
            if os.path.isdir(item_path):
                item_name += '/'
            if not self.config.include_hidden and item.startswith('.'):
                continue

            if not self.config.no_gitignore and self.gitignore_matches(item_path):
                continue

            if os.path.isfile(item_path):
                result.append(
                    self.process_file(item, item_path))
            elif os.path.isdir(item_path):
                item_name = os.path.basename(item_path)
                result.append({
                    item_name:
                    self.process_folder(item_path)
                })

        return result

    def process_file(self, file_name, file_path):
        if is_binary(file_path) and self.config.skip_binaries:
            return {file_name: None}

        if self.config.skip_content:
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
