"""
Filename: magnetic.py

Description:
    Magnetic attribute structure
    for FEMM magnetostatics and
    AC simulations.
"""


class MagneticData:
    """ Magnetic Attribute Data """
    def __init__(self, data: dict) -> None:
        """ Initializes the class and loads data into attributes """
        self.data = data

        # Loads variables into attributes
        self._load_top_level()

    def _load_top_level(self) -> None:
        """ Loads the top level sections from the solution """
        # File & Version
        self.format_version: float = self.data["format"]

        # Problem Definition
        self.frequency_hz: float = self.data["frequency"]
        self.solver_precision: float = self.data["precision"]
        self.min_angle_deg: float = self.data["minangle"]

        # Mesh Settings
        self.model_depth: float = self.data["depth"]
        self.length_unit: str = self.data["lengthunits"]
        self.problem_type: str = self.data["problemtype"]
        self.coordinate_system: str = self.data["coordinates"]

        # Metadata
        self.comment_text: str = self.data["comment"]
