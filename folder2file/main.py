"""
Main module for the folder2file application.
"""
import sys
from typing import Dict, Any
from .config import Config
from .folder_processor import process_folder
from .out_json import format_json
from .out_md import format_markdown
from .out_text import format_text
from .out_xml import format_xml
from .cli import config_from_cli
from .cli_menu import run_interactive_menu


def main() -> None:
    """
    Main entry point for the folder2file application.
    Processes a folder structure and outputs it in the specified format.
    """
    # Check if any command line arguments were provided
    if len(sys.argv) == 1:
        # No arguments provided, use interactive CLI menu
        config: Config = run_interactive_menu()
    else:
        # Arguments provided, use traditional CLI parsing
        config: Config = config_from_cli()

    print(f"Processing folder: {config.folder_path}")
    folder_structure: Dict[str, Any] = process_folder(config).result

    print(f"Writing output: {config.out_filename}")
    formatted_output: str = format_output(folder_structure, config)
    if config.print_output:
        print(formatted_output)

    if config.out_filename:
        with open(config.out_filename, "w", encoding="utf-8") as f:
            f.write(formatted_output)

    print(f"✅ Conversion completed successfully!")


def format_output(data: Dict[str, Any], config: Config) -> str:
    """
    Format the output data according to the specified format.

    Args:
        data: The folder structure data to format
        config: The configuration options

    Returns:
        Formatted output string

    Raises:
        ValueError: If the output format is not supported
    """
    if config.output_format == "json":
        return format_json(data, config.no_newline)
    elif config.output_format == "markdown":
        return format_markdown(data, config.no_newline)
    elif config.output_format == "text":
        return format_text(data)
    elif config.output_format == "xml":
        return format_xml(data, config.no_newline)
    else:
        raise ValueError(f"Unsupported output format: {config.output_format}")


if __name__ == "__main__":
    main()
