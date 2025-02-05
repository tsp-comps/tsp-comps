import networkx as nx

def find(parent, n):
    if parent[n] == n:
        return n
    return find(parent, parent[n])

# takes a networkx graph and returns a minimum spanning tree of that graph using Kruskal's algorithm
def minimum_spanning_tree(graph):
        mst = nx.Graph()    
        
        edges = sorted(list(graph.edges(data=True)), key=lambda x: x[2]['weight'])

        i = 0, e = 0

        while e < graph.number_of_nodes() - 1:
            u, v, w = edges[i]
            i += 1


        return mst