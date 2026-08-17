"""
Filename: parser_errors.py

Description:
    Defines the errors classes to ensure 
    descriptive error messages.
"""

from typing import Any

from FEMMInterpreter.constants import FILE_FORMATS, FILE_TYPES

# pylint: disable=line-too-long

# Generic Errors
class ParserError(ValueError):
    """ Exception for Parser errors when parsing """
    def __init__(self, caller: str, error: str):
        """ Returns a custom error message """
        msg = f"[] '{caller}' raised error: {error}. "
        super().__init__(msg)


# Specific errors
class FailedCasting(ValueError):
    """ Exception for failure during casting """
    CODE = "E001"

    def __init__(self, text: Any, error: str):
        """ Returns a failed casting error """
        msg = f"[{self.CODE}] Failed to cast {text!r} as Python primitive, error: {error!r}"
        super().__init__(msg)


class FileTypeNotSupported(Exception):
    """ Exception for file type not supported """
    CODE = "E002"

    def __init__(self, file_type: str):
        """ Returns a file type not supported error """
        msg = f"[{self.CODE}] Failed to parse {file_type!r} as not in supported list {FILE_TYPES!r}"
        super().__init__(msg)


class FormatNotSupported(Exception):
    """ Exception for format not supported """
    CODE = "E003"

    def __init__(self, file_format: str):
        """ Returns a format not supported error """
        msg = f"[{self.CODE}] Failed to parse {file_format!r} as not in supported list {FILE_FORMATS!r}"
        super().__init__(msg)


class AttributeLoadingFailed(Exception):
    """ Exception for attribute loading failing """
    CODE = "E004"

    def __init__(self, file_type: str):
        """ Returns a loading failure error """
        msg = f"[{self.CODE}] Failed to load {file_type!r} attributes into attribute structure"
        super().__init__(msg)
    