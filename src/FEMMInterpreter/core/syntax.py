"""
Filename: syntax.py

Description:
    Syntaxes for .ans format.
    
    Handles block section and data 
    section parsing.
"""

from FEMMInterpreter.core.state import ParserState


class BlockExtraction:
    """ Extract arbitrary block section data from .ans format """
    @classmethod
    def extract(cls, lines: list[str], state: ParserState) -> tuple[dict, ParserState]:
        """ Extracts the block section """
        _ = lines
        return {}, state


class DataExtraction:
    """ Extract arbitrary data section from .ans format """
    @classmethod
    def extract(cls, lines: list[str], state: ParserState) -> tuple[dict, ParserState]:
        """ Extracts the data section """
        _ = lines
        return {}, state


class SolutionExtraction:
    """ Extract arbitrary solution data from .ans format"""
    @classmethod
    def extract(cls, lines: list[str], state: ParserState) -> tuple[dict, ParserState]:
        """ Extracts the solution data """
        _ = lines
        return {}, state
