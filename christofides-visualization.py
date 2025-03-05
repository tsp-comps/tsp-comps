import networkx as nx
from datasets import Datasets
import sys
from graphtour_visualization import *
import matplotlib.pyplot as plt
from christofides import Christofides

sys.setrecursionlimit(2147483647)

'''runs the christofides algorithm as in Christofides.py with a visualization for each step.'''
def vis_cf(graph, pointset):
        cf = Christofides()

        #draw the input graph without edges for readability
        draw_nx_graph(nx.Graph(), pointset, just_nodes=True, title="Input Graph")

        # Create and draw a minimum spanning tree of graph.
        mst = cf.kruskals_algorithm(graph)
        draw_nx_graph(mst, pointset, title="Minimum Spanning Tree")

        # Find the odd degree vertices of the mst and draw them alongside the even degree nodes in a different color
        odd_degree = cf.find_odd_degree(mst, graph)
        draw_nx_graph(odd_degree, pointset, just_nodes=True, title="Odd Degree Vertices")

        # Find a minimum-weight perfect matching in the subgraph induced in G by O and draw it alongside the other nodes in the input
        mpm = cf.blossom_algorithm(odd_degree)
        draw_nx_graph(mpm, pointset, title="Minimum Weight Perfect Matching")

        # Combine the edges of the mst and the mpm to form a connected multigraph in which each vertex has even degree. Draw it
        multigraph = cf.combine_graphs(mst, mpm)
        draw_nx_graph(multigraph, pointset, title="Multigraph")

        # Form an Eulerian circuit in H and draw its edges on the input nodes
        circuit = cf.fleurys_algorithm(multigraph)
        draw_tsp_paths_euclidean(circuit, pointset)

        # Make the circuit found in previous step into a Hamiltonian circuit by skipping repeated vertices (shortcutting).
        tour = cf.eulerian_to_hamiltonian(circuit)

        # Draw the final tour
        draw_tsp_paths_euclidean(tour, pointset)

# depicts a networkx graph
def draw_nx_graph(graph, pointset, just_nodes=False, title="Graph"):
    xvals = []
    yvals = []
    coords = pointset.as_name_dict()["node_coords"].values()

    # draws the input nodes in grey
    for point in coords:
        xvals.append(point[0])
        yvals.append(point[1])
    plt.scatter(xvals, yvals, color='grey')

    # draws the edges of the graph in green and fills in nodes in graph in green
    if not just_nodes:
        for edge in graph.edges():
            plt.plot([xvals[edge[0]-1], xvals[edge[1]-1]], [yvals[edge[0]-1], yvals[edge[1]-1]], 'go-', label='path', linewidth=2)
    
    # draws no edges if specified
    else:
        for node in graph.nodes():
            plt.scatter(xvals[node-1], yvals[node-1], color='green')
            
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    G = nx.Graph()
    filename = 'datasets/tsp95/dj38.tsp'
    G = Datasets.process_tsp95(filename)
    G_pts = tsplib95.load(filename)
    tour = vis_cf(G, G_pts)