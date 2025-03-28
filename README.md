# Folder To File

This Python-based tool converts a folder structure into JSON, Markdown, XML, or plain text format. It's designed to be modular, easy to use, and extendable for future enhancements.

## Features

- Convert folder structures to JSON, Markdown, XML, or text format
- Interactive CLI menu for easy configuration
- Option to remove unnecessary newlines from file contents
- Option to skip binary files' content
- Option to skip file contents entirely
- Option to include hidden files and folders
- Option to use rules from a .gitignore file

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

After installation, you can run the tool in two ways:

### Interactive Mode

Simply run the command without any arguments to start the interactive CLI menu:

```
folder2file
```

This will guide you through a series of prompts to:
- Select the input folder path
- Choose the output filename
- Select the output format using arrow keys
- Toggle various options with checkboxes
- Confirm your settings before processing

### Command Line Mode

If you prefer, you can also specify all options directly on the command line:

```
folder2file <folder_path> <output_format> [options]
```

#### Arguments:

- `<folder_path>`: Path to the folder you want to convert (default: current directory)
- `<output_format>`: Choose between `json`, `markdown`, `text`, or `xml` (default: `json`)

#### Options:

- `--no-newline`: Remove unnecessary newlines from file contents
- `--skip-binaries`: Don't include binary files' content, only their names
- `--skip-content`: Don't include file contents in the output (default: False)
- `--include-hidden`: Include hidden files and folders (default: False)
- `--no-gitignore`: Don't use rules from a .gitignore file (default: False)
- `--print`: Print the generated content to the console (default: False)
- `--out FILENAME`: Specify the output filename (default: name of the processed folder)
- `--version`: Show the version number and exit

### Examples:

Convert a folder to JSON, skipping binary files:
```
folder2file /path/to/your/folder json --skip-binaries
```

Convert a folder to Markdown, including hidden files and printing to console:
```
folder2file /path/to/your/folder markdown --include-hidden --print
```

Convert a folder to XML format:
```
folder2file /path/to/your/folder xml --out my_structure.xml
```

Convert a folder to JSON and save to a specific file:
```
folder2file /path/to/your/folder json --out my_structure.json
```

## Output Formats

### JSON
Produces a structured JSON representation of the folder hierarchy, with files and their contents.

### Markdown
Creates a Markdown document with folders and files represented as a nested list structure. File contents are included in code blocks.

### XML
Generates an XML document with a hierarchical representation of folders and files. File contents are enclosed in `<content>` tags.

### Text
Creates a simple plain text representation of the folder structure, with indentation to indicate nesting.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## TODO

- Add support for more output formats (e.g., YAML)
- Implement file content filtering options
- Add option to limit recursion depth
- Add progress indicators for large directories
- Improve XML output with attribute options

## Acknowledgments

- Thanks to [Michael Herrmann](https://github.com/mherrmann) for the [gitignore_parser](https://github.com/mherrmann/gitignore_parser) library which is used to handle .gitignore rules.

If you have any suggestions or encounter any issues, please open an issue on the GitHub repository.