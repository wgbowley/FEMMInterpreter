"""
Filename: deserialization.py

Description:
    Type conversion for .ans format values.
    
    Converts strings to Python primitives:
    (int, float, complex, bool, null/none, str).
"""


from __future__ import annotations
from typing import Any

from FEMMInterpreter.utilities.errors import FailedCasting


class Deserialize:
    """ Deserialization from text to primitives """
    @classmethod
    def cast(cls, text: str) -> int | float | complex | bool | None | str:
        """ Converts text to python primitives """
        if not isinstance(text, str):
            err = f"Expected str, got {type(text).__name__}"
            raise FailedCasting(text, err)

        text = text.strip()
        if cls.is_quoted(text):
            # Handles quoted strings first
            return str(cls.strip_quotes(text))

        # Try integer value
        try: return int(text)
        except ValueError: pass

        # Try float
        try: return float(text)
        except ValueError: pass

        # Try complex
        try: return complex(text)
        except ValueError: pass

        # Check boolean
        lower = text.lower()
        if lower == "true": return True
        if lower == "false": return False

        # Check null/None
        if text.lower() in ("null", "none"): return None

        # Default to string
        return str(text)

    @classmethod
    def cast_list(cls, items: list[str]) -> list[Any]:
        """ Casts values within list into primitives """
        casted_list = []

        for item in items:
            # Casts each item as a python primitive
            casted_list.append(cls.cast(item))

        return casted_list

    @classmethod
    def is_quoted(cls, text: str) -> bool:
        """ Check if text is surrounded by quotes """
        text = text.strip()
        if len(text) < 2:
            # Empty quoted text Ex. ("")
            return False

        if text.startswith('"') and text.endswith('"'):
            # Start and end with double quotes
            return True

        if text.startswith("'") and text.endswith("'"):
            # Start and end with single quotes
            return True

        return False

    @classmethod
    def strip_quotes(cls, text: str) -> str:
        """ Removes surrounding quotes if present """
        text = text.strip()
        if cls.is_quoted(text):
            # Removes double quotation ref. "{Text}"
            return text[1:-1]

        return text
