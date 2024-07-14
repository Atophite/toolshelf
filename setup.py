from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '0.0.5' 
DESCRIPTION = 'A versatile tool management utility for developers'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="toolshelf", 
    version=VERSION,
    author="Atophite",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/Atophite/toolshelf",
    packages=find_packages(),
    install_requires=["textual", "rich", "sqlalchemy", "pyperclip"], 
    include_package_data=True,
    package_data={
        "toolshelf": ["styling/*.tcss"],
    },
    keywords=['python', 'command-line', 'tool', 'TUI', 'Terminal User Interface'],
    classifiers= [
        "Programming Language :: Python :: 3",
    ],
    py_modules=["toolshelf"],
    entry_points={
        'console_scripts': [
            'toolshelf=toolshelf.entry_points.toolshelf_runner:run_toolshelf',  # 'toolshelf' is the command, and 'main' is the function to execute
        ],
    }

)