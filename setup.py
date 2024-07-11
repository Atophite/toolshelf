from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
    name="toolshelf", 
    version=VERSION,
    author="Atophite",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["textual", "rich", "sqlalchemy", "pyperclip"], 
    include_package_data=True,
    package_data={
        "toolshelf": ["styling/*.tcss"],
    },
    keywords=['python', 'first package'],
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