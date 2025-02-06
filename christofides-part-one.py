import networkx as nx

def find(parent, n):
    if parent[n] == n:
        return n
    return find(parent, parent[n])

def union(parent, x, y):
    x_set = find(parent, x)
    y_set = find(parent, y)
    if x_set != y_set:
        parent[x_set] = y_set

# takes a networkx graph and returns a minimum spanning tree of that graph using Kruskal's algorithm
def minimum_spanning_tree(graph):
        mst = nx.Graph()    
        
        edges = sorted(list(graph.edges(data=True)), key=lambda x: x[2]['weight'])

        i = 0
        e = 0

        parent = {node: node for node in graph.nodes()}

        while e < graph.number_of_nodes() - 1:
            u, v, w = edges[i]
            i += 1
            x = find(parent, u)
            y = find(parent, v)
            if x != y:
                e += 1
                mst.add_edge(u, v, weight=w['weight'])
                union(parent, x, y)

        return mst

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
    print(nx.minimum_spanning_tree(g).edges(data=True))

if __name__ == "__main__":
    main()