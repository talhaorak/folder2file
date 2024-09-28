# Folder To File

This Python-based tool converts a folder structure into either JSON or Markdown format. It's designed to be modular, easy to use, and extendable for future enhancements.

## Features

- Convert folder structures to JSON or Markdown format
- Option to remove unnecessary newlines from file contents

### Local Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/talhaorak/folder2file.git
   cd folder2file
   ```
3. Install the package:
   ```
   pip install .
   ```

### System-wide Installation

To install the Folder Structure Converter as a system-wide application:

1. Ensure you have Python 3.6 or higher and pip installed on your system.
2. Install directly from GitHub:
   ```
   pip install git+https://github.com/talhaorak/folder2file.git
   ```

## Usage

After installation, you can run the tool from anywhere in your system using:

```
folder2file <folder_path> <output_format> [options]
```

### Arguments:

- `<folder_path>`: Path to the folder you want to convert
- `<output_format>`: Choose between `json`, `markdown` or `text`

### Options:

- `--no-newline`: Remove unnecessary newlines from file contents
- `--skip-binaries`: Don't include binary files' content, only their names
- `--skip-content`: Don't include file contents in the output
- `--include-hidden`: Include hidden files and folders (default: False)
- `--print`: Print the generated content to the console (default: False)
- `--out FILENAME`: Specify the output filename (default: name of the processed folder)

### Examples:

Convert a folder to JSON, skipping binary files:
```
folder2file /path/to/your/folder json --skip-binaries
```

Convert a folder to Markdown, including hidden files and printing to console:
```
folder2file /path/to/your/folder markdown --include-hidden --print
```

Convert a folder to JSON and save to a specific file:
```
folder2file /path/to/your/folder json --out my_structure.json
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## TODO

- Add support for more output formats (e.g., YAML, XML)
- Implement file content filtering options
- Add option to limit recursion depth


If you have any suggestions or encounter any issues, please open an issue on the GitHub repository.