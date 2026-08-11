# pylint: skip-file
# FEMMInterpreter/__init__.py

from FEMMInterpreter.main import Parser

# Parser import
FEMMParser = Parser

# API Promises
__all__ = [
    "Parser",
]