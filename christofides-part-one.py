import networkx as nx

# helper function to find the root of a given node in a dictionary
def find(parent, n):
    if parent[n] == n:
        return n
    return find(parent, parent[n])

# helper function to union two sets
def union(parent, x, y):
    x_set = find(parent, x)
    y_set = find(parent, y)
    if x_set != y_set:
        parent[x_set] = y_set

# takes a networkx graph and returns a minimum spanning tree of that graph using Kruskal's algorithm
def minimum_spanning_tree(graph):
        mst = nx.Graph()    
        
        edges = sorted(list(graph.edges(data=True)), key=lambda x: x[2]['weight'])

        # i is the index of the edge we are considering and e is the number of edges we have added to the mst
        i = 0
        e = 0

        # parent is a dictionary that keeps track of the parent of each node
        parent = {node: node for node in graph.nodes()}

        # while we haven't added all edges to our mst, we consider the next edge and if it doesn't
        # create a cycle, we add it to the mst.
        while e < graph.number_of_nodes() - 1:
            u, v, w = edges[i]
            i += 1

            # checks for cycle creation. If the roots of u and v are the same, then there is a cycle
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e += 1
                mst.add_edge(u, v, weight=w['weight'])
                union(parent, x, y)

        return mst

# takes a networkx graph and returns a subgraph of the nodes with odd degree (part two of christofides algorithm)
def find_odd_degree(graph):
    odd_degree = nx.Graph()
    for node in graph.nodes():
        if graph.degree(node) % 2 != 0:
            odd_degree.add_node(node)
    for u, v, w in graph.edges(data=True):
        if u in odd_degree.nodes() and v in odd_degree.nodes():
            odd_degree.add_edge(u, v, weight=w['weight'])
    return odd_degree

def main():
    g = nx.Graph()
    g.add_edge(0, 1, weight=10)
    g.add_edge(0, 2, weight=6)
    g.add_edge(0, 3, weight=5)
    g.add_edge(1, 3, weight=15)
    g.add_edge(1, 4, weight=12)
    g.add_edge(2, 4, weight=8)
    g.add_edge(3, 4, weight=7)
    g.add_edge(3, 5, weight=9)
    g.add_edge(4, 5, weight=11)
    g.add_edge(4, 6, weight=14)
    g.add_edge(5, 6, weight=13)

    print("input graph:", g.edges(data=True))
    mst = minimum_spanning_tree(g)
    print("mst:", mst.edges(data=True))
    print("odd degree nodes:", find_odd_degree(mst).edges(data=True))

if __name__ == "__main__":
    main()