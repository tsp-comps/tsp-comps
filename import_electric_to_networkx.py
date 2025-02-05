import networkx

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
