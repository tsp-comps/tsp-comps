import networkx as nx
class NeareastNeighborOptimized:
    def __init__(self):
        pass
    def find_closest_no_sorting(self, graph_edges, visited):
        min = float("inf")
        min_edge = None
        for edge in graph_edges:
            if edge[1] not in visited and edge[2]['weight'] < min:
                min = edge[2]["weight"]
                min_edge = edge
        return min_edge
                
    def solve(self, graph):
        print("I'm running")
        #We need to keep track of the nodes we have visited so far
        visited = set()
        #We need to start the agorithm from somewhere, we arbitrarily choose
        #the first node network x spits when we ask it for nodes
        first_head = list(graph.nodes())[0]
        curr_head = first_head
        visited.add(curr_head)
        path = []
        path.append(curr_head)
        total_distance = 0
        while len(path) != graph.number_of_nodes():
            edges_head = list(graph.edges(curr_head, data = True))
            closest_node_to_head = self.find_closest_no_sorting(edges_head, visited)
            visited.add(closest_node_to_head[1])
            path.append(closest_node_to_head[1])
            curr_head = closest_node_to_head[1]
            total_distance += float(closest_node_to_head[2]['weight'])
        path.append(first_head)
        total_distance += float(graph.edges[curr_head, first_head]["weight"])
        return path, total_distance

