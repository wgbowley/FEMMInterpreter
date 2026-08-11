"""
Filename: state.py

Description:
    This file contains the parser state
    allowing for access across modules
    without circular implements.
"""

from dataclasses import dataclass


@dataclass
class ParserState:
    """ Stores the state of the parser """
    index: int = 0
    section: str | None = None
    content: dict | None = None
