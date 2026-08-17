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
