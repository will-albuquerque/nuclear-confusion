'''This module provides classes and methods to produce terrain'''

from perlin_noise import PerlinNoise
from enum import Enum
from random import choice
from math import e

class Hex:
    def __init__(self, i, j, k):
        if i + j + k != 0:
            print(i, j, k)
            raise ValueError('i, j, k do not sum to 0')
        self.i = i
        self.j = j
        self.k = k

class HexGrid:
    def __init__(self, max_radius):
        self.max_radius = max_radius
        self.hexes = set()
        x = 0
        y = 0
        x_in = 0
        z_in = 0
        for i in range(max_radius):
            x_in = i
            z_in = -i
            x = x_in
            y = 0
            for j in range(max_radius):
                self.hexes.add(Hex(x, y, z_in))
                x += 1
                y -= 1

class TerrainType(Enum):
    WATER = 0
    PLAIN = 1
    HILL = 2
    MOUNTAIN = 3

def create_terrain_map(hex_grid: HexGrid):
    terrain_map = {}
    noise = PerlinNoise(octaves=1, seed=100)
    for co_ord in hex_grid.hexes:
        x = noise([co_ord.i / hex_grid.max_radius,
                   co_ord.j / hex_grid.max_radius,
                   co_ord.k / hex_grid.max_radius])
        x *= 2
        if x < 0.1:
            terrain_map[co_ord] = TerrainType.WATER
            continue
        if x < 0.5:
            terrain_map[co_ord] = TerrainType.PLAIN
            continue
        if x < 0.8:
            terrain_map[co_ord] = TerrainType.HILL
            continue
        terrain_map[co_ord] = TerrainType.MOUNTAIN
    return terrain_map

def create_colour_map(terrain_map):
    colour_map = {}
    for co_ord, terrain_type in terrain_map.items():
        if terrain_type is TerrainType.WATER:
            colour_map[co_ord] = 'blue'
        elif terrain_type is TerrainType.PLAIN:
            colour_map[co_ord] = 'green'
        elif terrain_type is TerrainType.HILL:
            colour_map[co_ord] = 'yellow'
        else:
            colour_map[co_ord] = 'grey'
    return colour_map

def neighbours(co_ord):
    i, j, k = co_ord.i, co_ord.j, co_ord.k

    a = Hex(i + 1, j - 1, k)
    b = Hex(i + 1, j, k - 1)

    c = Hex(i, j + 1, k - 1)
    d = Hex(i - 1, j + 1, k)

    e = Hex(i - 1, j, k + 1)
    f = Hex(i, j - 1, k + 1)

    return a, b, c, d, e, f

def radiation_spread(terrain_map, rad, co_ord_1, co_ord_2):
    k = 1
    terrain_1 = terrain_map[co_ord_1]
    terrain_2 = terrain_map[co_ord_2]
    if terrain_1 >= terrain_2:
        return rad * pow(e, -k)
    constant = terrain_2.value - terrain_2.value + 2
    return rad * pow(e, -constant)

def create_radiation_map(terrain_map):
    radiation_map = {co_ord: 0 for co_ord in terrain_map.keys()}

    source = choice(list(radiation_map.keys()))
    radiation_map[source] = 100 # Initial radiation
    seen = set()
    to_be_calculated = [source]
    while to_be_calculated:
        co_ord = to_be_calculated.pop()
        seen.add(co_ord)
        for i in neighbours(co_ord):
            if i not in seen:
                radiation_map[i] += radiation_spread(terrain_map, radiation_map[co_ord], co_ord, i)
                to_be_calculated.append(i)

    return radiation_map
