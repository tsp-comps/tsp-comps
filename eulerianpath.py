import networkx as nx

def is_odd(number):
     if number % 2 == 1:
          return True
     return False

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
    print(graph.edges)
    print(start)
    print(end)
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
        print(path)
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

G = nx.Graph()
nx.DiGraph(directed = False)
edges = [(1,2),(2,3),(3,4),(1,4)]
G.add_edges_from(edges)

print(fleurys_algorithm(G))
          
     
     
     
    
        
              