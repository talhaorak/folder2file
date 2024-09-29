from folder2file import process_folder, format_json, format_markdown, format_text
from .cli import config_from_cli


def main():
    config = config_from_cli()

    print("Processing folder: ", config.folder_path)
    folder_structure = process_folder(config).result

    print("Writing output: ", config.out_filename)
    formatted_output = format_output(folder_structure, config)
    if config.print_output:
        print(formatted_output)

    if config.out_filename:
        with open(config.out_filename, "w", encoding="utf-8") as f:
            f.write(formatted_output)


if __name__ == "__main__":
    main()


def format_output(data, config):
    if config.output_format == "json":
        return format_json(data, config.no_newline)
    elif config.output_format == "markdown":
        return format_markdown(data, config.no_newline)
    elif config.output_format == "text":
        return format_text(data)
    else:
        raise ValueError(f"Unsupported output format: {config.output_format}")
