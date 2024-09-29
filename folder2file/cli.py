import argparse
import os
import sys

from folder2file import Config, __version__


def config_from_cli():
    parser = argparse.ArgumentParser(
        description="Convert folder structure to JSON or Markdown")
    parser.add_argument("folder_path", nargs='?', default=".",
                        help="Path to the folder to process")
    parser.add_argument("output_format", nargs='?', default="json",
                        choices=["json", "markdown", "text"],
                        help="Output format (json, markdown or text)")
    parser.add_argument("--no-newline", action="store_true", default=False,
                        help="Remove unnecessary newlines")
    parser.add_argument("--skip-binaries", action="store_true", default=True,
                        help="Skip binary file contents")
    parser.add_argument("--skip-content", action="store_true", default=False,
                        help="Skip the file contents")
    parser.add_argument("--include-hidden", action="store_true", default=False,
                        help="Include hidden files and folders")
    parser.add_argument("--no-gitignore", action="store_true", default=False,
                        help="Don't apply patterns listed in .gitignore")
    parser.add_argument("--print", action="store_true", default=False,
                        help="Print output to console")
    parser.add_argument("--out", help="Output filename")
    parser.add_argument("--version", action="store_true",
                        help="Print version information")

    args = parser.parse_args()
    if args.version:
        print(f"folder2file version {__version__}")
        sys.exit(0)

    out_filename = args.out
    if out_filename is None:
        if args.folder_path == '.':
            out_filename = os.path.basename(os.path.abspath(args.folder_path))
        else:
            out_filename = os.path.basename(args.folder_path)

    if args.output_format == 'json' and not out_filename.endswith('.json'):
        out_filename += '.json'
    elif args.output_format == 'markdown' and not out_filename.endswith('.md'):
        out_filename += '.md'
    elif args.output_format == 'text' and not out_filename.endswith('.txt'):
        out_filename += '.txt'

    config = Config(
        folder_path=args.folder_path,
        output_format=args.output_format,
        no_newline=args.no_newline,
        skip_binaries=args.skip_binaries,
        skip_content=args.skip_content,
        include_hidden=args.include_hidden,
        no_gitignore=args.no_gitignore,
        print_output=args.print,
        out_filename=out_filename
    )

    return config
