from setuptools import setup, find_packages
import re
with open("ctx/cli.py") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="ctx-cli",
    version=version,
    packages=find_packages(),
    install_requires=[
        'gitignore-parser',
        'pathspec',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'ctx = ctx.cli:main'
        ]
    },
    author="Aditya Sahani",
    description="CLI tool to generate codebase context for LLMs",
    url="https://github.com/Aditya-en/ctx-cli"
)