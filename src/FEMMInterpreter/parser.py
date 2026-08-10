"""
Filename: parser.py

Description:
    Domain specific language parser for .ans file
    
    Orchestrates parsing the files and producing
    field representations for layer.
"""


from pathlib import Path
from typing import IO, Any

from FEMMInterpreter.core.state import ParserState
from FEMMInterpreter.core.deserialization import Deserialize
from FEMMInterpreter.core.syntax import BlockExtraction, DataExtraction, SolutionExtraction
from FEMMInterpreter.core.constants import (
    FILE_TYPES, BLOCK_SECTIONS, DATA_SECTIONS, SOLUTION_SECTION
)

from FEMMInterpreter.utilities.errors import ParserError


class Parser:
    """ Parser for .ans file format. """
    @classmethod
    def open(cls, filepath: Path | str | IO | Any) -> dict:
        """ Parses .ans file into a field representation. """
        # Checks file type and reads lines into memory
        if isinstance(filepath, (str, Path)):
            path = Path(filepath)
            if path.suffix.lower() not in FILE_TYPES:
                raise ValueError(f"Expected {FILE_TYPES!r} file, got {path.suffix!r}")

        lines = cls._read_lines(filepath)
        return ParseLines.parse(lines)

    @staticmethod
    def _read_lines(filepath_or_file: Path | str | IO | Any) ->  list[str]:
        """ Read lines from file path or file-like object. """
        if hasattr(filepath_or_file, 'read') and hasattr(filepath_or_file, 'readlines'):
            # Check if it's a file-like object
            return filepath_or_file.readlines()

        # Convert to Path and validate
        filepath = Path(filepath_or_file)
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        with filepath.open('r', encoding='utf-8') as f:
            return f.readlines()


class ParseLines:
    """ Parses lines for .ans file format. """
    @classmethod
    def parse(cls, lines: list[str]) -> dict:
        """ Parses and extracts logic from raw text into structured results. """
        state = ParserState()
        state.content = {}

        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            is_section, section = cls._is_section(line)
            is_value, raw_value = cls._extract_section_value(line)

            value = Deserialize.cast(raw_value)

            if section.lower() in BLOCK_SECTIONS:
                # Parses block section syntaxes
                data, state = BlockExtraction.extract(lines, state)
                state.content[section] = data
                continue

            if section.lower() in DATA_SECTIONS:
                # Parses the data section syntaxes
                data, state = DataExtraction.extract(lines, state)
                state.content[section] = data
                continue

            if section.lower() in SOLUTION_SECTION:
                # Parse the solution section syntaxes
                data, state = SolutionExtraction.extract(lines, state)
                state.content[section] = data
                continue

            if is_section and is_value:
                # Adds the section value under section name
                state.content[section] = value
                continue

            return state.content
        return state.content

    @classmethod
    def _is_section(cls, line: str) -> tuple[bool, str]:
        """ Check if line defines a section [name]. """
        line = line.strip()
        if not line.startswith('['):
            return False, ""

        closing_bracket = line.find(']')
        if closing_bracket == -1:
            msg = "closing bracket not found in-line"
            raise ParserError(cls.__name__, msg)

        return True, line[1:closing_bracket]

    @classmethod
    def _extract_section_value(cls, line: str) -> tuple[bool, str]:
        """ Extract section or subsection values. """
        equal_sign = line.find("=")
        if equal_sign == -1:
            return False, ""

        return True, line[equal_sign+1:].strip()
