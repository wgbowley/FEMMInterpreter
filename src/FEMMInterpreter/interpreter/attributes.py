"""
Filename: attributes.py

Descriptions:
    Defines the `Attribute` structure
    for the `.ans` files.
"""

from __future__ import annotations

from FEMMInterpreter.constants import FILE_FORMATS
from FEMMInterpreter.utilities.errors import FormatNotSupported


class AttributeLoader:
    """ Attribute loader for `.ans` files """
    @classmethod
    def load(cls, data: dict, file_type: str) -> MagneticData:
        """ Loads data into type specific structure """

        # File format not supported currently by the interpreter
        file_format = data["format"]
        if file_format not in FILE_FORMATS: raise FormatNotSupported(file_format)

        match file_type:
            case ".ans":
                return MagneticData(data)

            case _:
                msg = f"Failed to load {file_type!r} attributes into attribute structure"
                raise RuntimeError(msg)


class MagneticData:
    """ Magnetic Attribute Data """
    def __init__(self, data: dict) -> None:
        """ Initializes the class and loads data into attributes """
        self.file_format = data["format"]
        self.frequency = data["frequency"]
        self.precision = data["precision"]
        self.minangle = data["minangle"]

        # Loads the field solutions
        self._load_vector_potential(data)

    def _load_vector_potential(self, data: dict) -> None:
        """ Loads the vector potential from solution """
        first_key = next(iter(data["solution"]))

        # # Convert to floats
        self.vector_x = data["solution"][first_key][0]
        self.vector_y = data["solution"][first_key][1]
        self.vector_a = data["solution"][first_key][2]
