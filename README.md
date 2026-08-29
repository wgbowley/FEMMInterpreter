<!--
Color Palette:
#FFFFFF - pure white 
#00FFFF - pure, highly saturated shade of Cyan  

It's a simple piece of kit, but being able to integrate
FEMM solutions directly into the pipeline is extremely
useful.

- William Bowley, 2026-08-17

P.S: Thanks for downloading the FEMMInterpreter repository `▽`ʃ♡
-->

### Overview

![Status](https://img.shields.io/badge/Status-Active-FFFFFF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-00FFFF?style=flat-square&color=00FFFF)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-FFFFFF?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/femminterpreter?label=downloads\&style=flat-square\&color=00FFFF)](https://pepy.tech/projects/femminterpreter)

A Python library for interpreting Finite Element Method Magnetic (FEMM) files and exposing FEMM solution data 
through a Python attribute-based interface. `FEMMInterpreter` exposes the `A-field` as `A(x,y)`, independent of planar or axisymmetric coordinate systems.

#### Proposed Integration

FEMMInterpreter is intended to provide a bridge between FEMM's numerical
solutions and Python-based computational models.

```
FEMM Setup & Solve → FEMM (.ans) → FEMMInterpreter → Reduced Order Models / Analytical Models
```

---

<!-- Need to update that image before updating to PyPi -->

<div align="center">
  <img 
    src="https://raw.githubusercontent.com/wgbowley/FEMMInterpreter/main/media/dipole_a_potential_plot.png" 
    alt="Magnetic vector potential Plot" style="max-width: 600px"
  >
    <p>
      <em>
      Figure 1: Magnetic vector potential of a dipole extracted from FEMM (.ans)
      </em>
    </p>
</div>

> This example of a dipole being plotted can be found in [/examples](examples/) with `.ans` and `.py` files.

---

### Quick Start

```py
from ifemm import Parser

# Imports the parser and parses the .ans file
PATH = "examples/magnetostatic.ans"
data = Parser.open(PATH)

# Result as a float with implicit unit of wb/length_unit
a_potential = data.point_potential(0, 0)
```

---

### Installation

> This library is still under development and hasn't been fully documented nor fully test-covered. <br>
> The abstraction boundaries may change with future releases. 

To install,

```
pip install FEMMInterpreter
```

---

### Documentation

Full documentation is available in the [`docs/`](https://github.com/wgbowley/FEMMInterpreter/tree/main/docs) folder, including API reference, changelog, and contributors.

---