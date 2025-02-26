import networkx as nx
import pulp as pl

def blossom_algorithm(graph):
    
    edges_list = graph.edges.data("weight")
    cvals = [edge[2] for edge in edges_list]
    
    model = pl.LpProblem("Blossom Alg Primal", pl.LpMinimize)

    for 