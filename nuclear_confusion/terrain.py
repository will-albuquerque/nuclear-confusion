'''This module provides classes and methods to produce terrain'''

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
