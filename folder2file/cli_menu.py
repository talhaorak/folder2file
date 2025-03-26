"""
Interactive CLI menu for folder2file.
"""
import os
import questionary
from typing import Dict, Any, List, Optional
from .config import Config


def run_interactive_menu() -> Config:
    """
    Run an interactive CLI menu to configure folder2file options.

    Returns:
        Config object with user-selected settings
    """
    print("\n🗂️  Folder2File - Interactive Mode 🗂️\n")
    print("Convert folder structures to various formats.\n")

    # Ask for input path
    folder_path = questionary.text(
        "Input folder path:",
        default="."
    ).ask()

    if folder_path is None:  # User pressed Ctrl+C
        print("\nOperation cancelled.")
        exit(0)

    # Determine default output filename based on folder path
    default_name = os.path.basename(os.path.abspath(folder_path))

    # Ask for output filename
    out_filename = questionary.text(
        "Output filename (without extension):",
        default=default_name
    ).ask()

    if out_filename is None:  # User pressed Ctrl+C
        print("\nOperation cancelled.")
        exit(0)

    # Ask for output format
    output_format = questionary.select(
        "Select output format:",
        choices=[
            {"name": "JSON - Structured data format", "value": "json"},
            {"name": "Markdown - Formatted documentation", "value": "markdown"},
            {"name": "XML - Hierarchical data format", "value": "xml"},
            {"name": "Text - Simple plain text representation", "value": "text"}
        ]
    ).ask()

    if output_format is None:  # User pressed Ctrl+C
        print("\nOperation cancelled.")
        exit(0)

    # Add appropriate extension if not already present
    if output_format == "json" and not out_filename.endswith('.json'):
        out_filename += '.json'
    elif output_format == "markdown" and not out_filename.endswith('.md'):
        out_filename += '.md'
    elif output_format == "text" and not out_filename.endswith('.txt'):
        out_filename += '.txt'
    elif output_format == "xml" and not out_filename.endswith('.xml'):
        out_filename += '.xml'

    # Ask for options
    options = questionary.checkbox(
        "Select options (use spacebar to toggle, arrow keys to navigate):",
        choices=[
            {"name": "Remove unnecessary newlines from content", "value": "no_newline"},
            {"name": "Skip binary file contents",
                "value": "skip_binaries", "checked": True},
            {"name": "Skip all file contents", "value": "skip_content"},
            {"name": "Include hidden files and folders", "value": "include_hidden"},
            {"name": "Don't apply .gitignore rules", "value": "no_gitignore"},
            {"name": "Print output to console", "value": "print_output"},
            {"name": "✓ Proceed with these settings", "value": "proceed"}
        ],
        validate=lambda x: True if "proceed" in x else "Please select 'Proceed' when you're done"
    ).ask()

    if options is None:  # User pressed Ctrl+C
        print("\nOperation cancelled.")
        exit(0)

    # Remove the proceed option as it's not a real option
    options.remove("proceed")

    # Create the config object
    config = Config(
        folder_path=folder_path,
        output_format=output_format,
        no_newline="no_newline" in options,
        skip_binaries="skip_binaries" in options,
        skip_content="skip_content" in options,
        include_hidden="include_hidden" in options,
        no_gitignore="no_gitignore" in options,
        print_output="print_output" in options,
        out_filename=out_filename
    )

    # Show summary and confirm
    print("\n📋 Summary:")
    print(f"• Input folder: {config.folder_path}")
    print(f"• Output format: {config.output_format.upper()}")
    print(f"• Output filename: {config.out_filename}")
    print("• Options:")
    print(f"  - Remove newlines: {'Yes' if config.no_newline else 'No'}")
    print(
        f"  - Skip binary content: {'Yes' if config.skip_binaries else 'No'}")
    print(f"  - Skip all content: {'Yes' if config.skip_content else 'No'}")
    print(f"  - Include hidden: {'Yes' if config.include_hidden else 'No'}")
    print(f"  - Ignore .gitignore: {'Yes' if config.no_gitignore else 'No'}")
    print(f"  - Print to console: {'Yes' if config.print_output else 'No'}")

    confirm = questionary.confirm(
        "Proceed with these settings?", default=True).ask()

    if confirm is None or not confirm:  # User pressed Ctrl+C or selected No
        print("\nOperation cancelled.")
        exit(0)

    return config
