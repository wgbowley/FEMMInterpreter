"""
Filename: dipole.py

Description:
    This file is an example 
    of plotting a dipole.
"""

import matplotlib.pyplot as plt
from FEMMInterpreter import Parser

# Imports the parser and parses the .ans file
PATH = "examples/dipole.ans"
data = Parser.open(PATH)


# Returns the x, y and a spaces
x, y, a = data.field_potential()

# Plots the resulting spaces.
fig, ax = plt.subplots(figsize=(10, 8))

contour = ax.contourf(x, y, a, levels=50, cmap='viridis')
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('A (Wb/m)', fontsize=12)

ax.set_xlabel('x (m)', fontsize=12)
ax.set_ylabel('y (m)', fontsize=12)
ax.set_title('Magnetic Vector Potential A(x,y)', fontsize=14)
ax.axis('equal')
ax.grid(True, alpha=0.3)

plt.show()
