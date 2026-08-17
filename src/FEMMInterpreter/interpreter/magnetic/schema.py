"""
Filename: schema.py

Description:
    Magnetic attribute structure
    for FEMM magnetostatics and
    AC simulations.
"""

from numpy import column_stack as np_column_stack, array as np_array
from scipy.interpolate import NearestNDInterpolator

from FEMMInterpreter.interpreter.magnetic.definitions import (
    MaterialDefinition,
    BoundaryDefinition,
    CircuitDefinition
)

class MagneticData:
    """ Magnetic Attribute Data """
    def __init__(self, data: dict) -> None:
        """ Initializes the class and loads data into attributes """
        self.data = data

        # Loads variables into attributes
        self._load_top_level()
        self._load_boundaries()
        self._load_materials()
        self._load_circuits()

        # Creates the A potential map
        self._constructs_potential_map()

    def _constructs_potential_map(self) -> None:
        """ Constructs the vector potential map """
        solution = next(iter(self.data["solution"]))

        # Convert to three lists for each dimension
        self.vector_x = self.data["solution"][solution][0]
        self.vector_y = self.data["solution"][solution][1]
        self.vector_a = self.data["solution"][solution][2]

        # Convert to numpy arrays for interpolation
        points = np_column_stack((self.vector_x, self.vector_y))
        values = np_array(self.vector_a)

        # Create the interpolation function
        self._interpolator = NearestNDInterpolator(points, values)

    def vector_potential(self, x: float, y: float) -> float:
        """ Return the magnetic vector potential A at point (x, y). """
        result = self._interpolator(x, y)

        # NearestNDInterpolator always returns a value
        return result

    def _load_circuits(self) -> None:
        """ Loads materials section from the solution """
        circuits = self.data["circuitprops"]

        for key in circuits:
            # Sets the circuit definition as attribute
            circuit = CircuitDefinition.define(circuits[key])
            setattr(self, circuit.name, circuit)

    def _load_materials(self) -> None:
        """ Loads materials section from the solution """
        materials = self.data["blockprops"]

        for key in materials:
            # Sets the material definition as attribute
            material = MaterialDefinition.define(materials[key])
            setattr(self, material.name, material)

    def _load_boundaries(self) -> None:
        """ Loads boundaries section from the solution """
        boundaries = self.data["bdryprops"]

        for key in boundaries:
            # Sets the boundary definition as attribute
            boundary = BoundaryDefinition.define(boundaries[key])
            setattr(self, boundary.name, boundary)

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
