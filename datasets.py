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

    