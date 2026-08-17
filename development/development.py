"""
Filename: development.py

Description:
    This file is used for the 
    development of the FEMMinterpreter.
"""

from FEMMInterpreter import Parser

# Imports the parser and parses the .ans file
PATH = "development/magnet_plate.ans"
data = Parser.open(PATH)
