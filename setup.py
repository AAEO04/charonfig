# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="charonfig",
    version="0.1.0",
    author="Alli Ayomide eniola",
    author_email="allioladapo5@gmail.com",
    description="A flexible configuration management library with support for typed fields, encryption, and multiple formats.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AAEO04/charonfig",  # Replace with your repo URL
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "charonfig=charonfig.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=3.4",
        "PyYAML>=5.4",
    ],
    keywords="configuration, config, env, yaml, json, encryption",
)