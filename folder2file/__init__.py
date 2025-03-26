"""
folder2file package for converting folder structures to various formats.
"""
# First, import version and Config from config
from .config import __version__, Config

# Then import everything else
from .out_json import format_json
from .out_md import format_markdown
from .out_text import format_text
from .out_xml import format_xml

# Import process_folder last to avoid circular dependencies
from .folder_processor import process_folder

__all__ = [
    'Config',
    'process_folder',
    'format_json',
    'format_markdown',
    'format_text',
    'format_xml',
    '__version__',
]
