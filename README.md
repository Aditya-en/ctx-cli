# CTX - Codebase Context Generator 🔍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

A CLI tool to generate consolidated codebase context for LLMs with intelligent file handling and structure visualization.

## Features ✨

- **Smart Ignore System** 🔒  
  - Auto-detects .gitignore rules + custom ignores via --ignore
  - Ignores .git folder by default to reduce clutter
- **File Tree Visualization** 🌳  
  - Built-in directory structure display (disable with --no-tree)
- **Flexible Targeting** 🎯  
  - Specify files/directories or process the entire project
- **LLM-Optimized** 🤖  
  - Clean output format with file boundaries and metadata
- **Cross-Platform** 💻  
  - Works on Windows, macOS, and Linux

## Installation 📦

```bash
pip install git+https://github.com/Aditya-en/ctx-cli.git
```

### Prerequisites
- Python 3.6+
- Git (for installation from repository)

## Basic Usage 🚀

### Process the current directory:
```bash
ctx
```

### Target specific files/directories:
```bash
ctx src/ utils.py README.md
```
          
### Custom ignores and no tree:
```bash
ctx --ignore "*.log" --ignore tmp/ --no-tree
```

## Advanced Options ⚙️

| Option          | Description                                     | Example                    |
|----------------|-------------------------------------------------|----------------------------|
| --max-tokens   | Set maximum context size in tokens              | --max-tokens 100000        |
| --auto-skip    | Automatically skip large files                  | --auto-skip                |
| --ignore       | Add custom ignore pattern (glob format)         | --ignore "*.csv"           |
| --no-tree      | Disable file tree visualization                 | --no-tree                  |
| --tree         | Show ONLY the file tree structure               | --tree                     |
| --output, -f   | Save output to file                             | --output context.txt       |
| -c, --clipboard| Copy output to clipboard                        | --clipboard                |
| --version, -v  | Show version information                        | --version                  |

## Example Output 📄

The tool generates a consolidated view of your project, including:
- A hierarchical file tree structure
- Full contents of processed files
- Warning messages for large files
- Optional clipboard and file output

## Token Estimation and File Handling

- Uses a conservative token estimation method
- Provides interactive prompts for large files
- Configurable maximum token limit (default: 128,000 tokens)
- Supports custom ignore patterns and .gitignore rules

## Dependencies
- gitignore-parser
- pathspec
- pyperclip (optional, for clipboard feature)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.