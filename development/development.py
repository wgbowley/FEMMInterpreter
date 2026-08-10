"""
Filename: development.py

Description:
    This file is used for the 
    development of the FEMMinterpreter.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from FEMMInterpreter import Parser

# Imports the parser and parses the .ans file
PATH = "development/magnetostatic.ans"
data = Parser.open(PATH)

first_key = next(iter(data["Solution"]))
solution = data["Solution"][first_key]

# Convert to floats
x = []
y = []
a = []

for item in solution:
    x.append(float(item[0]))
    y.append(float(item[1]))
    a.append(float(item[2]))

# Create grid for interpolation
RESOLUTION = 300
x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)

# Add padding
PAD = 0.05
x_range = x_max - x_min
y_range = y_max - y_min
x_min -= PAD * x_range
x_max += PAD * x_range
y_min -= PAD * y_range
y_max += PAD * y_range

xi = np.linspace(x_min, x_max, RESOLUTION)
yi = np.linspace(y_min, y_max, RESOLUTION)
X, Y = np.meshgrid(xi, yi)

# Interpolate A onto grid
A_grid = griddata((x, y), a, (X, Y), method='linear')

# Plot just the A field
fig, ax = plt.subplots(figsize=(10, 8))

contour = ax.contourf(X, Y, A_grid, levels=50, cmap='viridis')
cbar = plt.colorbar(contour, ax=ax)
cbar.set_label('A (Wb/m)', fontsize=12)

ax.set_xlabel('x | r (m)', fontsize=12)
ax.set_ylabel('y | z (m)', fontsize=12)
ax.set_title('Magnetic Vector Potential A(x,y or r,z)', fontsize=14)
ax.axis('equal')
ax.grid(True, alpha=0.3)

plt.show()
