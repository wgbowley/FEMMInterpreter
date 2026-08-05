"""
Filename: parser_errors.py

Description:
    Defines the parser errors classes to 
    ensure descriptive error messages are
    returned to the user
"""

from typing import Any


# Generic Errors
class ParserError(ValueError):
    """ Exception for Parser errors when parsing """
    def __init__(self, caller: str, error: str):
        """ Returns a custom error message """
        msg = f"'{caller}' raised error: {error}. "
        super().__init__(msg)


# Specific errors
class FailedCasting(ValueError):
    """ Exception for failure during casting """
    def __init__(self, text: Any, error: str):
        """ Returns a failed casting error """
        msg = f"Failed to cast {text!r} as python primitive, error: {error!r}"
        super().__init__(msg)
