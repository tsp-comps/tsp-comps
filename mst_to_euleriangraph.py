import networkx as nx

def is_odd(number):
     if number % 2 == 1:
          return True
     return False

def oddnode_subgraph(graph, mst):
    odd_deg_nodes = []
    for node in mst.nodes:
        if is_odd(mst.degree[node]):
             odd_deg_nodes.append(node)
    return graph.subgraph(odd_deg_nodes)

def blossoms_algorithm(graph):
    matching = nx.Graph()
    matching.add_nodes_from(graph.nodes)
    for node in graph.nodes:
         