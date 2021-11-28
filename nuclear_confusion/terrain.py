"""This module provides classes and methods to produce terrain"""

from typing import NamedTuple

class Hex(NamedTuple):
    """Hex represents a hexagon on a hexagonal co-ordinate system"""
    i: int
    j: int
    k: int

def generate_hexes(max_i, max_j, max_k):
    """generate_hexes creates a set of hexes"""
    hexes = set()
    for i in range(max_i):
        for j in range(max_j):
            for k in range(max_k):
                hexes.add(Hex(i, j, k))

    return hexes
