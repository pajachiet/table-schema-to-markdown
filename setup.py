from setuptools import setup

setup(
    name="table_schema_to_markdown",
    license="MIT",
    packages=["table_schema_to_markdown"],
    version="0.1",
    description="Generate Markdown documentation from a table schema file from Frictionless Data",
    author="Antoine Augusti",
    author_email="hi@antoine-augusti.fr",
    url="https://github.com/AntoineAugusti/table_schema_to_markdown",
    scripts=["bin/table-schema-to-md"],
    keywords=[
        "frictionlessdata",
        "documentation",
        "tableschema",
        "table-schema",
        "frictionless data",
        "open data",
        "json schema",
        "json table schema",
        "data package",
        "tabular data package",
    ],
    install_requires=[],
    extras_require={"dev": ["nose"]},
    python_requires=">=2.7, <4",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)