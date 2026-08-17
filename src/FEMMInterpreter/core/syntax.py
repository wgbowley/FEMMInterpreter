"""
Filename: syntax.py

Description:
    Syntaxes for .ans format.
    
    Handles block section and data 
    section parsing.
"""

from FEMMInterpreter.core.states import ParserState
from FEMMInterpreter.utilities.errors import ParserError
from FEMMInterpreter.core.deserialization import Deserialize

from FEMMInterpreter.constants import BLOCK_PAIRS, DATA_SECTIONS


class BlockExtraction:
    """ Extract arbitrary block section data from .ans format """
    @classmethod
    def extract(
        cls, lines: list[str], items: int, state: ParserState
    ) -> tuple[dict, ParserState]:
        """ Extracts the block section """
        if items == 0:
            # If the entry has zero data. Returns None
            return {}, state

        block = {}
        num_item = 0

        # Initializes the first item
        block[num_item] = {}
        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            if cls._is_new_blocks(line):
                state.block = line.strip().lower()
                continue

            if state.block and cls._is_close_block(line, state):
                state.block = None
                num_item += 1

                # Returns the result after iteration across items
                if num_item == items: return block, state

                # Adds the entry for the next item
                block[num_item] = {}
                continue

            if state.block:
                # Extracts block and cases the values within the block
                name, raw_value = cls._extract_block_value(line, state)
                value = Deserialize.cast(raw_value)

                if name in DATA_SECTIONS:
                    # Parses the data section syntaxes
                    data, state = DataExtraction.extract(lines, value, state)
                    block[num_item][name] = data
                    continue

                # Adds the name and value to the block and section
                block[num_item][name] = value
                continue

        msg = f"Failed to parse block section, block: {block}, items: {items}"
        raise ParserError(cls.__name__, msg)

    @classmethod
    def _is_new_blocks(cls, line: str) -> bool:
        """ Checks if its a block section """
        if line.lower() in BLOCK_PAIRS:
            return True

        return False

    @classmethod
    def _is_close_block(cls, line: str, state: ParserState) -> bool:
        if state.block is None:
            return False

        if line.lower() in BLOCK_PAIRS[state.block]:
            return True

        return False

    @classmethod
    def _extract_block_value(cls, line: str, state: ParserState) -> tuple[str, str]:
        """ Extract block name and value from line """
        equal_sign = line.find("=")
        if equal_sign == -1:
            msg = f"Malformed block section found in {line!r}, Index: {state.index}"
            raise ParserError(cls.__name__, msg)

        # Returns stripped lower name and stripped value
        return line[:equal_sign-1].strip().lower(), line[equal_sign+1:].strip()


class DataExtraction:
    """ Extract arbitrary data section from .ans format """
    @classmethod
    def extract(
        cls, lines: list[str], items: int, state: ParserState
    ) -> tuple[dict, ParserState]:
        """ Extracts the data section """
        if items == 0:
            # If the entry has zero data. Returns None
            return {}, state

        data = {}
        num_item = 0
        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            # Splits the line into values
            values = line.split()
            data[num_item] = Deserialize.cast_list(values)

            num_item += 1

            # Returns the result after iteration across items
            if num_item == items: return data, state

        msg = "Failed to parse data section"
        raise ParserError(cls.__name__, msg)


class SolutionExtraction:
    """ Extract arbitrary solution data from .ans format"""
    @classmethod
    def extract(cls, lines: list[str], state: ParserState) -> tuple[dict, ParserState]:
        """ Extracts the solution data """
        data = {}
        rows = []
        current_item = None

        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            # Splits the line into values
            raw_values = line.split()
            cast_values = Deserialize.cast_list(raw_values)

            if len(raw_values) == 1:
                # Updates the section name based off items
                if current_item is not None and rows:
                    data[current_item] = cls._transpose(rows)
                    rows = []

                current_item = cast_values[0]
                continue

            # Skip orphaned data
            if current_item is None: continue

            rows.append(cast_values)

        if current_item is not None and rows:
            data[current_item] = cls._transpose(rows)

        return data, state

    @classmethod
    def _transpose(cls, rows: list[list]) -> list[list]:
        """ Transpose rows into columns """
        # Skips transposing and returns an empty array
        if not rows: return []

        # Creates a list of columns to transpose.
        num_cols = len(rows[0])
        transposed = [[] for _ in range(num_cols)]

        for row in rows:
            for col_idx, value in enumerate(row):
                transposed[col_idx].append(value)

        return transposed
