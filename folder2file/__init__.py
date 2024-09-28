from .folder_processor import process_folder
from .out_json import format_json
from .out_md import format_markdown
from .out_text import format_text
from dataclasses import dataclass


@dataclass
class Config:
    folder_path: str
    output_format: str
    no_newline: bool = False
    skip_binaries: bool = False
    skip_content: bool = False
    include_hidden: bool = False
    print_output: bool = False
    out_filename: str = None
