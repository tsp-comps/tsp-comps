import networkx as nx
import random
import matplotlib.pyplot as plt
import christofides as cf
from datasets import Datasets
import tsplib95

#Creates a complete graph with specified number of nodes and random edge weights integers 1-100.
def create_test_graph(num_nodes):
    G = nx.complete_graph(num_nodes)
    
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 100)

    return G

#Assumes values of the pairs are distinct, ignores order.
def pair_has_samevalues(pair1,pair2):
    if pair1[0] != pair2[0] and pair1[0] != pair2[1]:
        return False
    if pair1[1] != pair2[0] and pair1[1] != pair2[1]:
        return False
    return True

#Returns shared edges of two paths.
def path_intersection(path1, path2):
    shared_edges =[]
    for edge1 in path1:
        for edge2 in path2:
            if pair_has_samevalues(edge1,edge2):
                shared_edges.append(edge1)
    return shared_edges

#Draws 1-3 tsp paths for a graph
def draw_tsp_paths_noneuclidean(G, path1=None, path2=None, path3=None):
    pos = nx.random_layout(G)  # positions for all nodes

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, font_size=10, font_color='black', font_weight='normal', arrows=True,width=0)

    # Highlight the path1 if provided
    if path1:
        first_node1 = path1[0]
        nx.draw_networkx_nodes(G, pos, nodelist=[first_node1], node_size=200, node_color='yellow')

        path1_edges = list(zip(path1, path1[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path1_edges, edge_color='yellow', width=1)
    
    #Highlight the path2 if provided
    if path2:
        first_node2 = path2[0]
        nx.draw_networkx_nodes(G, pos, nodelist=[first_node2], node_size=200, node_color='blue')

        path2_edges = list(zip(path2, path2[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path2_edges, edge_color='blue', width=1)
    
    #Highlight the path3 if provided
    if path3:
        first_node3 = path3[0]
        nx.draw_networkx_nodes(G, pos, nodelist=[first_node2], node_size=200, node_color='red')

        path3_edges = list(zip(path3, path3[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path3_edges, edge_color='red', width=1)

    #Highlight intersection of path1 and path2
    if path1 and path2:
        if first_node1 == first_node2:
            nx.draw_networkx_nodes(G, pos, nodelist=[first_node1], node_size=200, node_color='green')

        shared_edges12 = path_intersection(path1_edges,path2_edges)
        nx.draw_networkx_edges(G, pos, edgelist=shared_edges12, edge_color='green', width=1)

    #Highlift inersection of path2 and path3, and path3 and path1
    if path1 and path2 and path3:
        if first_node2 == first_node3:
            nx.draw_networkx_nodes(G, pos, nodelist=[first_node2], node_size=200, node_color='purple')
        
        if first_node1 == first_node3:
            nx.draw_networkx_nodes(G, pos, nodelist=[first_node1], node_size=200, node_color='orange')

        if first_node1 == first_node2 and first_node2 == first_node3:
            nx.draw_networkx_nodes(G, pos, nodelist=[first_node1], node_size=200, node_color='black')

        shared_edges23 = path_intersection(path2_edges,path3_edges)
        shared_edges13 = path_intersection(path1_edges,path3_edges)
        shared_edges123 = path_intersection(shared_edges23,shared_edges13)
        
        nx.draw_networkx_edges(G, pos, edgelist=shared_edges23, edge_color='purple', width=1)
        nx.draw_networkx_edges(G, pos, edgelist=shared_edges13, edge_color='orange', width=1)
        nx.draw_networkx_edges(G, pos, edgelist=shared_edges123, edge_color='black', width=1)

    plt.title("Graph Visualization")
    plt.show()

def draw_tsp_paths_euclidean(tspset, path):
    coords = tspset.as_name_dict()["node_coords"].values()
    tspgraph = tspset.get_graph()
    xvals = []
    yvals = []
    for point in coords: 
        xvals.append(point[0])
        yvals.append(point[1])

    plt.scatter(xvals,yvals)

    #plot path
    pathx = []
    pathy = []
    for node in path:
        pathx.append(xvals[node - 1])
        pathy.append(yvals[node - 1])
    
    plt.plot(pathx, pathy, 'go-', label='path', linewidth=2)

    plt.show()

    


    

if __name__ == "__main__":
    '''
    G = create_test_graph(1000)

    # Find the shortest path
    path1 = cf.christofides_algorithm(G)
    path2 = nx.algorithms.approximation.christofides(G, weight="weight")
    path3 =nx.approximation.greedy_tsp(G)
    
    print("Our path: ",path1)
    print("NX path: ",path2)
    print("Greedy tsp path: ",path3)

    # Draw the graph and highlight the paths
    draw_tsp_paths_noneuclidean(G, path1)
    '''

    tsp_set = tsplib95.load(f"datasets/tsp95/wi29.tsp")
    g_tsp = tsp_set.get_graph()
    
    christofides = cf.Christofides()
    tour = christofides.solve(g_tsp)


    print()
    print()
    draw_tsp_paths_euclidean(tsp_set,tour)

