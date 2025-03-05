from setuptools import setup, find_packages

setup(
    name="ctx-cli",
    version="0.2.0",
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