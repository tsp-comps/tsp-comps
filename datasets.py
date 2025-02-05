"""
Datasets class for loading and processing the data.
"""

import tsplib95
import networkx as nx

class Datasets(object):
    def __init__(self):
        pass

    def process_tsp95(file_path):
        tsp_set = tsplib95.load(file_path)
        g_tsp = tsp_set.get_graph()
        return g_tsp

def load_electric_grid_dataset():
    #Here we read the cleaned data from a file, make their format friendly to networkx
    #and add them to an array. These are the edges of our graph
    file = open("datasets/electric-grid/electric_points.tsv", "r")
    edges = []
    for line in file:
        split_line = line.split("\t")
        edges.append(tuple(split_line))
    file.close()

    #Here we create the graph and load the edges
    graph = networkx.Graph()
    graph.add_weighted_edges_from(edges)
    return graph

    