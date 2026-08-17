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
        self.format_version = self.data["format"]

        # Problem Definition
        self.frequency_hz = self.data["frequency"]
        self.solver_precision = self.data["precision"]
        self.min_angle_deg = self.data["minangle"]

        # Mesh Settings
        self.model_depth = self.data["depth"]
        self.length_unit = self.data["lengthunits"]
        self.problem_type = self.data["problemtype"]
        self.coordinate_system = self.data["coordinates"]

        # Solver Configuration
        self.ac_solver_type = self.data["acsolver"]
        self.prev_solution_type = self.data["prevtype"]
        self.prev_solution_file = self.data["prevsoln"]

        # Metadata
        self.comment_text = self.data["comment"]
        self.point_properties = self.data["pointprops"]
        self.boundary_properties = self.data["bdryprops"]
