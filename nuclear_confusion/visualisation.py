'''This module provides functions to visualise the terrain'''

from terrain import Hex, HexGrid
from matplotlib.patches import RegularPolygon

import matplotlib.pyplot as plt
import numpy as np

def display_graph(colour_map):
    '''display_graph displays a colour map'''

    # Define plot figure and axes
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Add hexagons
    for h in colour_map:
        # Convert from hexagonal co-ordinate to cartesian co-ordinate
        x = h.j * np.sqrt(3) / 2 - h.k * np.sqrt(3) / 2
        y = h.i + h.j / 2 + h.k / 2

        # Create hexagon
        hexagon = RegularPolygon((x,y),
                                 numVertices=6,
                                 radius=np.sqrt(3) / 3.0,
                                 orientation=np.radians(30),
                                 facecolor=colour_map[h],
                                 alpha=0.2,
                                 edgecolor='k')
        ax.add_patch(hexagon)
        ax.scatter(x, y, alpha=0)

    # Display plot
    plt.show()
