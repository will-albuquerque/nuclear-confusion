from terrain import HexGrid, create_terrain_map, create_colour_map
from visualisation import display_graph

display_graph(create_colour_map(create_terrain_map(HexGrid(7))))
