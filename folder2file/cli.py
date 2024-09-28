import argparse
import os

from folder2file import Config


def config_from_cli():
    parser = argparse.ArgumentParser(
        description="Convert folder structure to JSON or Markdown")
    parser.add_argument("folder_path", help="Path to the folder to process")
    parser.add_argument("output_format", choices=[
                        "json", "markdown", "text"], help="Output format (json, markdown or text)")
    parser.add_argument("--no-newline", action="store_true",
                        help="Remove unnecessary newlines")
    parser.add_argument("--skip-binaries", action="store_true",
                        help="Skip binary file contents")
    parser.add_argument("--skip-content", action="store_true",
                        help="Skip the file contents")
    parser.add_argument("--include-hidden", action="store_true",
                        help="Include hidden files and folders")
    parser.add_argument("--print", action="store_true",
                        help="Print output to console")
    parser.add_argument("--out", help="Output filename")
    args = parser.parse_args()
    out_filename = args.out or os.path.basename(args.folder_path)

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
        print_output=args.print,
        out_filename=out_filename
    )

    return config
