# CTX - Codebase Context Generator 🔍

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

A CLI tool to generate consolidated codebase context for LLMs with intelligent file handling and structure visualization.

<!-- ![Example Output](https://via.placeholder.com/800x400.png?text=CTX+Output+Example+-+File+Tree+%2B+File+Contents) -->

## Features ✨

- **Smart Ignore System** 🔒  
  - Auto-detects `.gitignore` rules + custom ignores via `--ignore`
  - Ignores `.git` folder by default to reduce clutter
- **File Tree Visualization** 🌳  
  - Built-in directory structure display (disable with `--no-tree`)
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
|----------------|---------------------------------|--------------------------|
| `--ignore`     | Add custom ignore pattern (glob format) | `--ignore "*.csv"`     |
| `--no-tree`    | Disable file tree visualization | `--no-tree`             |
| `--output`     | Save output to file | `--output context.txt` |
| `--version`    | Show version information | `--version`             |

## Example Output 📄
```
File structure:
.
├── README.md
├── ctx/
│   ├── __init__.py
│   └── cli.py
└── setup.py

File contents:

--- README.md ---
# CTX - Codebase Context Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)

A CLI tool to generate consolidated codebase context for LLMs with intelligent file handling and structure visualization.
