from setuptools import setup, find_packages

setup(
    name="ctx-cli",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        'gitignore-parser',
        'pathspec'
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