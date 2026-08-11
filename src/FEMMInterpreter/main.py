"""
Filename: main.py

Description:
    Domain specific language parser for .ans file
    
    Orchestrates parsing the files and producing
    field representations for layer.
"""

from pathlib import Path

from FEMMInterpreter.parser.states import ParserState
from FEMMInterpreter.parser.deserialization import Deserialize
from FEMMInterpreter.parser.syntax import BlockExtraction, DataExtraction, SolutionExtraction
from FEMMInterpreter.constants import FILE_TYPES, BLOCK_SECTIONS, DATA_SECTIONS, SOLUTION_SECTION

from FEMMInterpreter.utilities.errors import ParserError, FileTypeNotSupport
from FEMMInterpreter.interpreter.attributes import AttributeLoader, MagneticData


class Parser:
    """ Parser for .ans file format. """
    @classmethod
    def open(cls, filepath: Path | str ) -> MagneticData:
        """ Parses .ans file into a field representation. """
        if not isinstance(filepath, (str, Path)):
            # Raises error for non supported path type
            msg = f"Invalid path type {type(filepath)!r} for {cls.__name__!r}"
            raise TypeError(msg)

        # Constructs a path and extracts file type
        path = Path(filepath)
        file_type = path.suffix.lower()

        # Raises error for non supported file type
        if file_type not in FILE_TYPES: raise FileTypeNotSupport(file_type)
            # Raises error for non supported file type

        lines = cls._read_lines(filepath)
        data = ParseLines.parse(lines)
        return AttributeLoader.load(data, file_type)

    @staticmethod
    def _read_lines(filepath_or_file: Path | str) ->  list[str]:
        """ Read lines from file path or file-like object. """

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

            if not line:
                # Skips empty lines
                continue

            # Extracts the solution and value than casts it in primitives
            is_section, section = cls._is_section(line)
            is_value, raw_value = cls._extract_section_value(line)

            value = Deserialize.cast(raw_value)

            if section in BLOCK_SECTIONS:
                # Parses block section syntaxes
                data, state = BlockExtraction.extract(lines, value, state)
                state.content[section] = data
                continue

            if section in DATA_SECTIONS:
                # Parses the data section syntaxes
                data, state = DataExtraction.extract(lines, value, state)
                state.content[section] = data
                continue

            if section in SOLUTION_SECTION:
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

        return True, line[1:closing_bracket].lower()

    @classmethod
    def _extract_section_value(cls, line: str) -> tuple[bool, str]:
        """ Extract section or subsection values. """
        equal_sign = line.find("=")
        if equal_sign == -1:
            return False, ""

        return True, line[equal_sign+1:].strip()
