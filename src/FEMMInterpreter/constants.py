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

# Validate Block Section Names
BLOCK_SECTIONS = [
    "bdryprops",
    "blockprops",
    "circuitprops"
]

# Validate Block Pairs
BLOCK_PAIRS = {
    "<beginbdry>":    "<endbdry>",
    "<beginblock>":   "<endblock>",
    "<begincircuit>": "<endcircuit>"
}

# Validate Data Section Names
DATA_SECTIONS = [
    "numblocklabels",
    "conductorprops",
    "numpoints",
    "numsegments",
    "<bhpoints>"
]

# Validate Solution Section Name
SOLUTION_SECTION = [
    "solution"
]
