import networkx as nx
from datasets import Datasets

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

'''takes a networkx graph and returns a minimum spanning tree of that graph using Kruskal's algorithm'''
def kruskals_algorithm(graph):
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

def is_odd(number):
     if number % 2 == 1:
          return True
     return False

'''takes a networkx graph and returns a subgraph of the nodes with odd degree (part two of christofides algorithm)'''
def find_odd_degree(mst, graph):
    odd_degree = nx.Graph()
    for node in mst.nodes():
        if is_odd(mst.degree(node)):
            odd_degree.add_node(node)
    for u, v, w in graph.edges(data=True):
        if u in odd_degree.nodes() and v in odd_degree.nodes():
            odd_degree.add_edge(u, v, weight=w['weight'])
    return odd_degree

''' takes a graph and returns a minimum weight perfect matching of the graph'''
def blossom_algorithm(graph):
    # networkX function that returns the matching as a set of node pairs
    mpm_set = nx.algorithms.matching.min_weight_matching(graph, weight="weight")

    # creates a graph with the node pairs connected by their corresponding edges in the initial graph
    mpm = nx.Graph()
    for u, v in mpm_set:
        mpm.add_edge(u, v, weight=graph[u][v]['weight'])
    return mpm

'''takes two graphs and returns a multigraph'''
def combine_graphs(graph1, graph2):
    multigraph = nx.MultiGraph()
    for u, v, w in graph1.edges(data=True):
        multigraph.add_edge(u, v, weight=w['weight'])
    for u, v, w in graph2.edges(data=True):
        multigraph.add_edge(u, v, weight=w['weight'])
    return multigraph

def dfs_counter(graph, current, visited_nodes):
    neighbors = list(graph.neighbors(current))
    count = 1
    visited_nodes[current] = True
    for node in neighbors:
        if visited_nodes[node] == False:
            count += dfs_counter(graph, node, visited_nodes)
    return count

def is_valid_edge(graph, start, end):
    nodes = list(graph.nodes)
    start_degree = graph.degree(start)
    #valid if degree is 1
    if start_degree == 1:
        return True
     
    #valid if the edge is not a bridge
    visited_nodes = {}
    for node in nodes:
        visited_nodes.update({node : False})
    count1 = dfs_counter(graph, start, visited_nodes)

    for node in nodes:
        visited_nodes.update({node : False})
    graph.remove_edge(start,end)
    count2 = dfs_counter(graph, start, visited_nodes)
     
    graph.add_edge(start,end)

    if count1 > count2:
        return False
    return True
     
        
'''Finds the Eulerian tour for the given graph, beginning at the initial input current node'''
def get_eulerian_tour(graph, current, path):
    neighbors = list(graph.neighbors(current))
    for neighbor in neighbors:
        if is_valid_edge(graph, current, neighbor):
            path.append(neighbor)
            graph.remove_edge(current,neighbor)
            return get_eulerian_tour(graph,neighbor,path)
    return path
    
'''Takes an Eulerian graph and returns an Eulerian tour of the graph.'''
def fleurys_algorithm(graph):
    nodes = list(graph.nodes)
    start_node = nodes[0]
    for node in nodes:
        if is_odd(graph.degree[node]):
            start_node = node
            break
    return get_eulerian_tour(graph, start_node, [start_node])

'''takes an eulerian tour and converts it to a hamiltonian path'''
def eulerian_to_hamiltonian(eulerian_tour):
    visited_nodes = {}
    for node in eulerian_tour:
        visited_nodes.update({node : False})
    hamiltonian_path = []

    for node in eulerian_tour:
        if not visited_nodes[node]:
            hamiltonian_path.append(node)
        visited_nodes.update({node : True})

    hamiltonian_path.append(eulerian_tour[0])    
    return hamiltonian_path

'''takes a graph and returns a 1.5 approximation of the optimal TSP solution using christofides algorithm'''
def christofides_algorithm(graph):
    # broken into steps taken from the wikipedia page on Christofides

    # Create a minimum spanning tree of graph.
    mst = kruskals_algorithm(graph)
    #print('mst:', mst.edges)
    # Find the odd degree vertices of the mst
    odd_degree = find_odd_degree(mst, graph)
    #print('odd deg:', odd_degree.edges)
    # Find a minimum-weight perfect matching in the subgraph induced in G by O.
    mpm = blossom_algorithm(odd_degree)
    #print('mpm:', mpm.edges)
    # Combine the edges of the mst and the mpm to form a connected multigraph in which each vertex has even degree.
    multigraph = combine_graphs(mst, mpm)
    #print('multigraph:', multigraph.edges)
    # Form an Eulerian circuit in H.
    circuit = fleurys_algorithm(multigraph)
    #print('circuit:', circuit)
    # Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices (shortcutting).
    tour = eulerian_to_hamiltonian(circuit)
    return tour

# testing
G = nx.Graph()
G = Datasets.process_tsp95('datasets/tsp95/uy734.tsp')
# Create a weighted complete graph with 5 nodes
'''G.add_weighted_edges_from([
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 1),
    (0, 4, 4),
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 1),
    (2, 3, 4),
    (2, 4, 2),
    (3, 4, 3),
])
'''

def distance(tour, graph):
    total = 0
    for i in range(len(tour) - 1):
        total += graph[tour[i]][tour[i + 1]]['weight']
    return total

def unique(tour):
    visited = []
    for node in tour:
        if node not in visited:
            visited.append(node)
        elif node in visited and node != visited[0]:
            return False
    return True

print("our tour:", christofides_algorithm(G))
print("stops:", len(christofides_algorithm(G)))
print("distance = ", distance(christofides_algorithm(G), G))
if unique(christofides_algorithm(G)):
    print("unique")
else:
    print("not unique")
print("nx tour:", nx.algorithms.approximation.christofides(G, weight="weight"))
print("stops:", len(nx.algorithms.approximation.christofides(G, weight="weight")))
print("distance = ", distance(nx.algorithms.approximation.christofides(G, weight="weight"), G))
if unique(nx.algorithms.approximation.christofides(G, weight="weight")):
    print("unique")
else:
    print("not unique")