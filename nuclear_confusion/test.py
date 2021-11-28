from terrain import HexGrid, create_terrain_map, create_colour_map
from visualisation import display_graph
from random import choice

hex_grid = HexGrid(20)
terrain_map = create_terrain_map(hex_grid)
colour_map = create_colour_map(terrain_map)

colour_map[choice(list(hex_grid.hexes))] = 'red'

display_graph(colour_map)
