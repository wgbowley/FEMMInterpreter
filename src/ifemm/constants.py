"""
Filename: constants.py

Description:
    This file contains constants regarding
    to the parsing of .ans files.
"""

# Validate file types for the parser
FILE_TYPES = [
    ".ans"
]

# Validate File Formats
FILE_FORMATS = [
    4.0
]

# Validate Problem Parameters
PROBLEM_PARAMETERS = [
    "format",
    "frequency",
    "precision",
    "minangle",
    "depth",
    "lengthunits",
    "coordinates",
    "problemtype",
    "comment"
]

# Validate Block Section Names
BLOCK_SECTIONS = [
    "pointprops",
    "bdryprops",
    "blockprops",
    "circuitprops"
]

# Validate Block Pairs
BLOCK_PAIRS = {
    "<beginpoint>": "<endpoint>",
    "<beginbdry>":  "<endbdry>",
    "<beginblock>":  "<endblock>",
    "<begincircuit>": "<endcircuit>"
}

# Validate Data Section Names
DATA_SECTIONS = [
    "numblocklabels",
    "numarcsegments",
    "conductorprops",
    "numpoints",
    "numsegments",
    "numholes",
    "<bhpoints>",
]

# Validate Solution Section Name
SOLUTION_SECTION = [
    "solution"
]
