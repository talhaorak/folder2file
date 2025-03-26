from setuptools import setup, find_packages
from folder2file.config import __version__

setup(
    name="folder2file",
    version=__version__,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "folder2file=folder2file.main:main",
        ],
    },
    author="Talha Orak",
    author_email="talhaorak.git@gmail.com",
    description="A tool to convert folder structures to JSON or Markdown",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/talhaorak/folder2file",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
