import argparse
import os
import sys
from gitignore_parser import parse_gitignore
from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern

__version__ = "0.2.0"

def get_gitignore_matchers(root_dir):
    matchers = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.gitignore' in filenames:
            gitignore_path = os.path.join(dirpath, '.gitignore')
            if os.path.isfile(gitignore_path):
                try:
                    match_fn = parse_gitignore(gitignore_path)
                    matchers.append((dirpath, match_fn))
                except Exception as e:
                    print(f"Warning: Could not parse {gitignore_path}: {e}", file=sys.stderr)
    return matchers

def is_ignored_by_gitignore(file_path, gitignore_matchers):
    file_abs = os.path.abspath(file_path)
    
    if any(part == '.git' for part in file_abs.split(os.sep)):
        return True
    
    for base_dir, match_fn in gitignore_matchers:
        if file_abs.startswith(base_dir):
            rel_path = os.path.relpath(file_abs, base_dir)
            if match_fn(rel_path):
                return True
    return False

def generate_tree_lines(nodes, prefix=''):
    lines = []
    for i, (name, children) in enumerate(nodes):
        is_last = i == len(nodes) - 1
        connector = '└── ' if is_last else '├── '
        if children is None:
            lines.append(f"{prefix}{connector}{name}")
        else:
            lines.append(f"{prefix}{connector}{name}/")
            extension = '    ' if is_last else '│   '
            next_prefix = prefix + extension
            sorted_children = sorted(children.items(), key=lambda x: x[0])
            lines.extend(generate_tree_lines(sorted_children, next_prefix))
    return lines

def main():
    parser = argparse.ArgumentParser(description='Generate codebase context for LLMs')
    parser.add_argument('files', nargs='*', help='Files or directories to include')
    parser.add_argument('--no-tree', action='store_true', help='Skip file tree structure')
    parser.add_argument('--ignore', action='append', default=[], help='Custom ignore patterns')
    parser.add_argument('-f', '--file', metavar='PATH', 
                       help='Save output to specified file')
    parser.add_argument('-c', '--clipboard', action='store_true',
                       help='Copy output to clipboard')
    parser.add_argument('-v', '--version', action='version', 
                       version=f'%(prog)s {__version__}')
    
    args = parser.parse_args()

    root_dir = os.getcwd()
    custom_ignore_spec = PathSpec.from_lines(GitWildMatchPattern, args.ignore)
    gitignore_matchers = get_gitignore_matchers(root_dir) if not args.files else []

    collected_files = []

    if args.files:
        for entry in args.files:
            if not os.path.exists(entry):
                print(f"Warning: '{entry}' does not exist, skipping.", file=sys.stderr)
                continue
            abs_entry = os.path.abspath(entry)
            if os.path.isfile(abs_entry):
                collected_files.append(abs_entry)
            else:
                for dirpath, _, filenames in os.walk(abs_entry):
                    for filename in filenames:
                        collected_files.append(os.path.join(dirpath, filename))
        # Filter based on custom ignores
        filtered_files = []
        for file_path in collected_files:
            rel_path = os.path.relpath(file_path, root_dir)
            if not custom_ignore_spec.match_file(rel_path):
                filtered_files.append(file_path)
            else:
                print(f"Ignoring '{rel_path}' due to custom ignore pattern", file=sys.stderr)
        collected_files = filtered_files
    else:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Process files
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if is_ignored_by_gitignore(file_path, gitignore_matchers):
                    continue
                rel_path = os.path.relpath(file_path, root_dir)
                if custom_ignore_spec.match_file(rel_path):
                    continue
                collected_files.append(file_path)

    # Sort files for consistent order
    collected_files.sort(key=lambda x: os.path.relpath(x, root_dir))

    # Build directory structure for tree
    dir_structure = {}
    for file_path in collected_files:
        rel_path = os.path.relpath(file_path, root_dir)
        parts = rel_path.split(os.sep)
        current = dir_structure
        for part in parts[:-1]:
            if part not in current or current[part] is None:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = None  # Mark as file

    output = []

    if not args.no_tree:
        sorted_root = sorted(dir_structure.items(), key=lambda x: x[0])
        tree_lines = generate_tree_lines(sorted_root)
        output.append("File structure:\n.")
        output.extend(tree_lines)
        output.append("\nFile contents:\n")

    for file_path in collected_files:
        rel_path = os.path.relpath(file_path, root_dir)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            output.append(f"--- {rel_path} ---\n{content}\n")
        except Exception as e:
            print(f"Error reading '{rel_path}': {e}", file=sys.stderr)

    
    output_str = '\n'.join(output)
    # File output
    if args.file:
        try:
            with open(args.file, 'w', encoding='utf-8') as f:
                f.write(output_str)
            print(f"Output saved to {os.path.abspath(args.file)}", file=sys.stderr)
        except Exception as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            sys.exit(1)

    # Clipboard handling
    if args.clipboard:
        try:
            import pyperclip
            pyperclip.copy(output_str)
            print("Output copied to clipboard 📋", file=sys.stderr)
        except ImportError:
            print("Clipboard feature requires pyperclip. Install with: pip install pyperclip", 
                  file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Clipboard error: {e}", file=sys.stderr)
            sys.exit(1)

    if not args.file or args.clipboard:
        print(output_str)

if __name__ == '__main__':
    main()
