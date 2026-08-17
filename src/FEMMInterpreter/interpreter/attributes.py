"""
Filename: attributes.py

Descriptions:
    Defines the `Attribute` structure
    for the `.ans` files.
"""

from __future__ import annotations

from FEMMInterpreter.constants import FILE_FORMATS
from FEMMInterpreter.utilities.errors import FormatNotSupported, AttributeLoadingFailed
from FEMMInterpreter.interpreter.magnetic import MagneticData


class AttributeLoader:
    """ Attribute loader for `.ans` files """
    @classmethod
    def load(cls, data: dict, file_type: str) -> MagneticData:
        """ Loads data into type specific structure """

        file_format = data["format"]
        if file_format not in FILE_FORMATS:
            # File format not supported currently by the interpreter
            raise FormatNotSupported(file_format)

        match file_type:
            case ".ans":
                # Returns the magnetic data as attribute class
                return MagneticData(data)

            case _:
                raise AttributeLoadingFailed(file_type)
