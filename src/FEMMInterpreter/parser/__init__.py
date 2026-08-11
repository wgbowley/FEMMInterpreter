# pylint: skip-file
# FEMMInterpreter/main/__init__.py

from FEMMInterpreter.parser.main import Parser


# Parser import
FEMMParser = Parser


# API Promises
__all__ = [
    "Parser",
]