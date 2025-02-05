import networkx as nx
import random
import matplotlib.pyplot as plt

def create_test_graph(num_nodes):
    G = nx.complete_graph(num_nodes)
    
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 100)

    return G

def draw_graph(G):
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title("Fully Connected Graph with Random Weights")
    plt.show()

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes for the fully connected graph: "))
    graph = create_test_graph(num_nodes)
    draw_graph(graph)
