import networkx as nx

def find(parent, n):
    if parent[n] == n:
        return n
    return find(parent, parent[n])

# takes a networkx graph and returns a minimum spanning tree of that graph using Boruvka's algorithm
def minimum_spanning_tree(graph):
        mst = nx.Graph()    
        parent = []

        for node in graph.nodes():
            parent.append(nx.graph().add_node(node))
        
        cheapest = [-1] * len(parent)

        while len(parent) > 1:
            for i in range(graph.number_of_edges()):
                u, v, w = graph.edges[i]
                set1 = find(parent, u)
                set2 = find(parent, v)
                if set1 != set2:
                    mst.add_edge(u, v, weight=w)
                    nx.union(parent, set1, set2)
                 
                

        return mst