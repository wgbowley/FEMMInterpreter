## Overview
A python library for interpreting FEMM solution files

> [!important]
> This tool will focus on the magnetic domain for now. And can be expanded in the future across all of FEMM solutions.

<div align="center">
  <img src="media/dipole_a_potential_plot.png" alt="Magnetic vector potential Plot" style="max-width: 600px">
    <p><em>Figure 1: Magnetic vector potential extracted from FEMM (.ans)</em></p>
</div>

## Quick Start

```py
from FEMMInterpreter import Parser

# Imports the parser and parses the .ans file
PATH = "development/magnetostatic.ans"
data = Parser.open(PATH)

# Defines local variables for solution
x = data.vector_x
y = data.vector_y
a = data.vector_a
```

## Documentation

All internal documentation can be found within this repo's [issues](https://github.com/wgbowley/FEMMInterpreter/issues).

### Tags
```
LX -> Documentation and project structure
L0 -> Requirements and Objectives
L1 -> Architecture and implementation
L2 -> Validation of the codebase
DS -> Descoped Feature, Descoped Analysis 
```
