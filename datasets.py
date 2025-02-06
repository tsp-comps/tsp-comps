"""
Datasets class for loading and processing the data.
"""

import tsplib95
import networkx as nx
import pandas as pd

class Datasets(object):
    def __init__(self):
        pass

    def process_tsp95(file_path):
        """
        https://tsplib95.readthedocs.io/en/stable/pages/usage.html
        """
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
        graph = nx.Graph()
        graph.add_weighted_edges_from(edges)
        return graph
    
    def load_protein_dataset(file_path):
        # First we read the data from the .tsv file and remove the columns we don't need
        protein_data = pd.read_csv(file_path, sep='\t')
        columns_to_delete = ['node1_string_id','node2_string_id','neighborhood_on_chromosome',
                         'gene_fusion','phylogenetic_cooccurrence','homology',
                         'coexpression','experimentally_determined_interaction',
                         'database_annotated','automated_textmining']
        protein_data.drop(columns=columns_to_delete, inplace=True)
        protein_data['combined_score'] = 1 - protein_data['combined_score']

        # Then we create a graph from the data
        graph = nx.Graph()
        for index, row in protein_data.iterrows():
            graph.add_edge(row['#node1'], row['node2'], weight=row['combined_score'])
        return graph
        


    