from setuptools import setup, find_packages
import re

with open("ctx/cli.py", "r", encoding="utf-8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

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
    author="Your Name",
    description="CLI tool to generate codebase context for LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aditya-en/ctx-cli",
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)