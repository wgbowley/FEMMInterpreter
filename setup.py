"""
Filename: setup.py

Description: 
    Local development / editable install for FEMMInterpreter
"""

from setuptools import setup, find_packages

setup(
    name="FEMMInterpreter",
    version="0.1",
    description="A python library for interpreting FEMM solution files",
    author="William Bowley",
    author_email="wgrantbowley@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"FEMMInterpreter": ["py.typed", "**/*.pyi"]},
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
