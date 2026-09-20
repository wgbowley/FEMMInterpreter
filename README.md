<!--
Color Palette:
#FFFFFF - pure white 
#00FFFF - pure, highly saturated shade of Cyan  

It's a simple piece of kit, but being able to integrate
FEMM solutions directly into the pipeline is extremely
useful.

- William Bowley, 2026-08-17

P.S: Thanks for downloading the ifemm repository `▽`ʃ♡
-->

### Overview

![Status](https://img.shields.io/badge/Status-Active-FFFFFF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-00FFFF?style=flat-square&color=00FFFF)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-FFFFFF?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/ifemm?label=downloads\&style=flat-square\&color=00FFFF)](https://pepy.tech/projects/ifemm)

A Python library for interpreting Finite Element Method Magnetic (FEMM) files and exposing FEMM solution data 
through a Python attribute-based interface. `ifemm` exposes the `A-field` as `A(x,y)`, independent of planar or axisymmetric coordinate systems.

#### Proposed Integration

```
FEMM Setup & Solve → FEMM (.ans) → ifemm → Reduced Order Models / Analytical Models
```

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

To install,

```
pip install ifemm
```

---

### Documentation

Full documentation is available in the [`docs/`](https://github.com/wgbowley/ifemm/tree/main/docs) folder, including API reference, changelog, and contributors.

---