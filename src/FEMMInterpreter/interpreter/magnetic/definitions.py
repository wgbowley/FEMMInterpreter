"""
Filename: definitions.py

Description:
    Definitions for magnetic solutions.
"""

from __future__ import annotations
from typing import Any

from abc import ABC
from dataclasses import dataclass, fields


@dataclass(slots=True, repr=False)
class Definition(ABC):
    """ Abstract definition class """
    name: str

    def __repr__(self):
        """ Returns the loaders direct members """
        attributes = [field.name for field in fields(self)]
        items = ', '.join(attributes)
        if self.name is None:
            return f'Definition({items})'
        return f'{self.name}({items})'


@dataclass(slots=True, repr=False)
class MaterialDefinition(Definition):
    """ Defines a magnetic material """
    name: str
    permeability: tuple[float, float]
    coercive_force: float
    coercive_angle: float
    current_density: tuple[float, float]
    conductivity: float
    lamination_thickness: float
    hysteresis_angle: float
    hysteresis_angle_x: float
    hysteresis_angle_y: float
    lamination_type: int
    lamination_fill: float
    num_strands: int
    wire_diameter: float

    @classmethod
    def define(cls, entry: dict[str, Any]) -> MaterialDefinition:
        """ Self-constructs the magnetic material from entry """
        return cls(
            entry["<blockname>"],
            (entry["<mu_x>"], entry["<mu_y>"]),
            entry["<h_c>"],
            entry["<h_cangle>"],
            (entry["<j_re>"], entry["<j_im>"]),
            entry["<sigma>"],
            entry["<d_lam>"],
            entry["<phi_h>"],
            entry["<phi_hx>"],
            entry["<phi_hy>"],
            entry["<lamtype>"],
            entry["<lamfill>"],
            entry["<nstrands>"],
            entry["<wired>"]
        )


@dataclass(slots=True, repr=False)
class BoundaryDefinition(Definition):
    """ Defines a boundary condition """
    name: str
    boundary_type: int
    prescribed_a: float
    prescribed_a_x: float
    prescribed_a_y: float
    phase_angle: float
    mixed_c0: float
    mixed_c0_imag: float
    mixed_c1: float
    mixed_c1_imag: float
    mu_ssd: float
    sigma_ssd: float
    inner_angle: float
    outer_angle: float

    @classmethod
    def define(cls, entry: dict[str, Any]) -> BoundaryDefinition:
        """ Self-constructs the boundary condition from entry """
        return cls(
            entry["<bdryname>"],
            entry["<bdrytype>"],
            entry["<a_0>"],
            entry["<a_1>"],
            entry["<a_2>"],
            entry["<phi>"],
            entry["<c0>"],
            entry["<c0i>"],
            entry["<c1>"],
            entry["<c1i>"],
            entry["<mu_ssd>"],
            entry["<sigma_ssd>"],
            entry["<innerangle>"],
            entry["<outerangle>"]
        )


@dataclass(slots=True, repr=False)
class CircuitDefinition(Definition):
    """ Defines a circuit """
    name: str
    total_amps_real: float
    total_amps_imag: float
    circuit_type: int

    @classmethod
    def define(cls, entry: dict[str, Any]) -> CircuitDefinition:
        """ Self-constructs the circuit from entry """
        return cls(
            entry["<circuitname>"],
            entry["<totalamps_re>"],
            entry["<totalamps_im>"],
            entry["<circuittype>"]
        )
