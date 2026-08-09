"""
Filename: parser.py

Description:
    Domain specific language parser for .ans file
    
    Orchestrates parsing the files and producing
    field representations for layer.
"""

from pathlib import Path
from typing import IO, Any
from dataclasses import dataclass

from FEMMInterpreter.core.deserialization import Deserialize
from FEMMInterpreter.utilities.errors import ParserError


class Parser:
    """ Parser for .ans file format """
    @classmethod
    def open(cls, filepath: Path | str | IO | Any) -> dict:
        """ Parses .ans file into a field representation """
        # Checks file type and reads lines into memory
        if isinstance(filepath, (str, Path)):
            path = Path(filepath)
            if path.suffix.lower() != '.ans':
                raise ValueError(f"Expected .ans file, got {path.suffix}")
        lines = cls._read_lines(filepath)

        # Returns lines instead of data.
        data = ParseLines.parse(lines)
        return data

    @staticmethod
    def _read_lines(filepath_or_file: Path | str | IO | Any) ->  list[str]:
        """Read lines from file path or file-like object."""
        if hasattr(filepath_or_file, 'read') and hasattr(filepath_or_file, 'readlines'):
            # Check if it's a file-like object
            return filepath_or_file.readlines()

        # Convert to Path and validate
        filepath = Path(filepath_or_file)
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        with filepath.open('r', encoding='utf-8') as f:
            return f.readlines()


@dataclass
class ParseLineState:
    """Stores the state of the line parser"""
    index: int = 0
    section: str | None = None
    block: str | None = None
    content: dict | None = None


@dataclass(slots=True)
class PointData:
    """ Stores the state of a point """
    x: float
    y: float
    a: float
    boundary: int


class ParseLines:
    """ Parsel lines for .ans file format """
    BLOCK_PAIRS = {
        "<BeginBdry>":    "<EndBdry>",
        "<BeginBlock>":   "<EndBlock>",
        "<BeginCircuit>": "<EndCircuit>"
    }

    @classmethod
    def parse(cls, lines: list[str]) -> dict:
        """ Parses and extracts logic from raw text into structured results """
        state = ParseLineState()
        state.content = {}

        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            is_section, name = cls._is_section(line)
            if is_section:
                # Updates section if identified
                state.section = name
                state.content[name] = {}

                if name.lower() == "solution":
                    # Special Case for solution
                    state.content[name] = []

                # Checks for section value and casts the value into python primitives
                is_value, raw_value = cls._extract_section_value(line)
                value = Deserialize.cast(raw_value)

                # Adds the value to the section
                if is_value: state.content[name]["value"] = value

                continue

            if cls._is_new_blocks(line):
                # Checks if its a block section and updates the block if identified
                state.block = line.strip()
                state.content[state.section][state.block] = {}

                continue

            if state.block and cls._is_close_block(line, state):
                # Closes the block if closing block tag is identified
                state.block = None
                continue

            if state.block:
                # Extracts block and cases the values within the block
                name, value = cls._extract_block_value(line, state)
                value = Deserialize.cast(raw_value)

                # Adds the name and value to the block and section
                state.content[state.section][state.block][name] = value

            if state.section.lower() == "solution":
                values = line.split()
                if len(values) == 4:
                    # Records -> x | r, y | z, A, Boundary
                    point = PointData(values[0], values[1], values[2], values[3])
                    state.content[state.section].append(point)

        return state.content

    @classmethod
    def _is_section(cls, line: str) -> tuple[bool, str]:
        """ Check if line defines a section [name] """
        line = line.strip()
        if line.startswith('['):
            closing_bracket = line.find(']')

            # Closing bracket not found in-line
            if closing_bracket == -1:
                msg = "closing bracket not found in-line"
                raise ParserError(cls.__name__, msg)

            # Returns the contents if true
            return True, line[1:closing_bracket]
        return False, ""

    @classmethod
    def _extract_section_value(cls, line: str) -> tuple[bool, str]:
        """ Extract section or subsection values """
        equal_sign = line.find("=")
        if equal_sign != -1:
            # Returns the value if true and removes additional whitespaces
            return True, line[equal_sign+1:].strip()
        return False, ""

    @classmethod
    def _is_new_blocks(cls, line: str) -> bool:
        """ Checks if its a block section """
        if line in cls.BLOCK_PAIRS:
            return True

        return False

    @classmethod
    def _is_close_block(cls, line: str, state: ParseLineState) -> bool:
        if line in cls.BLOCK_PAIRS[state.block]:
            return True

        return False

    @classmethod
    def _extract_block_value(cls, line: str, state: ParseLineState) -> tuple[str, str]:
        """ Extract block name and value from line """
        equal_sign = line.find("=")
        if equal_sign == -1:
            # Malformed block section found inline
            msg = f"Malformed block section found in {line!r}, Index: {state.index}"
            raise ParserError(cls.__name__, msg)

        # Returns the name and value while removing additional whitespaces
        return line[:equal_sign-1].strip(), line[equal_sign+1:].strip()
