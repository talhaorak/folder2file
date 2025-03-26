"""
Configuration module for folder2file.
"""
from dataclasses import dataclass
from typing import Optional

__version__ = "0.4.0"


@dataclass
class Config:
    """
    Configuration class for folder2file.

    Attributes:
        folder_path: Path to the folder to process
        output_format: Output format (json, markdown, or text)
        no_newline: Whether to remove unnecessary newlines
        skip_binaries: Whether to skip binary file contents
        skip_content: Whether to skip file contents entirely
        include_hidden: Whether to include hidden files and folders
        no_gitignore: Whether to ignore .gitignore rules
        print_output: Whether to print output to console
        out_filename: Output filename
    """
    folder_path: str = "."
    output_format: str = "json"
    no_newline: bool = False
    skip_binaries: bool = True
    skip_content: bool = False
    include_hidden: bool = False
    no_gitignore: bool = False
    print_output: bool = False
    out_filename: Optional[str] = None
