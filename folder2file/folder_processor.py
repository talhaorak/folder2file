"""
Module for processing folder structures into dictionary representations.
"""
import os
import base64
from typing import Dict, List, Any, Callable, Union, Optional
from .gitignore_parser import parse_gitignore
from .config import Config


class process_folder:
    """
    Process a folder structure and convert it to a dictionary representation.
    """

    def __init__(self, config: Config):
        """
        Initialize the folder processor with the given configuration.

        Args:
            config: Configuration options for processing
        """
        self.config: Config = config
        self.gitignore_patterns: List[str] = []
        self.result: Dict[str, List[Dict[str, Any]]] = {}
        self.gitignore_matches: Callable[[str], bool]

        gitignore_path: str = os.path.join(config.folder_path, '.gitignore')
        if not config.no_gitignore and os.path.exists(gitignore_path):
            self.gitignore_matches = parse_gitignore(gitignore_path)
        else:
            self.gitignore_matches = lambda x: False

        folder_name: str = os.path.basename(config.folder_path)
        if folder_name == '.':
            folder_name = os.path.basename(os.path.abspath(config.folder_path))
        self.result[folder_name] = self.process_folder(config.folder_path)

    def process_folder(self, folder_path: str) -> List[Dict[str, Any]]:
        """
        Process a folder and its contents recursively.

        Args:
            folder_path: Path to the folder to process

        Returns:
            List of dictionaries representing the folder's contents
        """
        result: List[Dict[str, Any]] = []

        for item in os.listdir(folder_path):
            item_path: str = os.path.join(folder_path, item)
            item_name: str = item
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

    def process_file(self, file_name: str, file_path: str) -> Dict[str, Optional[str]]:
        """
        Process a file and its contents.

        Args:
            file_name: Name of the file
            file_path: Path to the file

        Returns:
            Dictionary with file name as key and content (or None) as value
        """
        if is_binary(file_path) and self.config.skip_binaries:
            return {file_name: None}

        if self.config.skip_content:
            return {file_name: None}

        try:
            with open(file_path, 'rb') as file:
                content: bytes = file.read()
                if is_binary(file_path):
                    return {file_name: base64.b64encode(content).decode('utf-8')}
                else:
                    return {file_name: content.decode('utf-8')}
        except Exception as e:
            return {file_name: f"Error reading file: {str(e)}"}


def is_binary(file_path: str) -> bool:
    """
    Check if a file is binary or text.

    Args:
        file_path: Path to the file to check

    Returns:
        True if the file is binary, False otherwise
    """
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read()
            return False
    except:
        return True
