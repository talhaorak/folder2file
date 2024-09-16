from .folder_processor import process_folder
from .out_json import format_json
from .out_md import format_markdown
from dataclasses import dataclass


@dataclass
class Config:
    folder_path: str
    output_format: str
    no_newline: bool = False
    skip_binaries: bool = False
    include_hidden: bool = False
    print_output: bool = False
    out_filename: str = None
