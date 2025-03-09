import networkx as nx
#Finds the path using neareast neighbor, this is in theory faster than the regular nearest neighbor as it does not
#use sorting
class NeareastNeighborOptimized:
    def __init__(self):
        pass
    #Finds the closest node by iteration, no sorting needed, this runs in O(n)
    def find_closest_no_sorting(self, graph_edges, visited):
        #If we haven't seen any minimum, we start with -inf as the minimum
        min = float("inf")
        min_edge = None
        #We go through every edge, trying to see the smallest unvisited edge
        for edge in graph_edges:
            #If it is the minimum, then we update it
            if edge[1] not in visited and edge[2]['weight'] < min:
                min = edge[2]["weight"]
                min_edge = edge
        #We return the minimum edge
        return min_edge
                
    def solve(self, graph):
        print("I'm running")
        #We need to keep track of the nodes we have visited so far
        visited = set()
        #We need to start the agorithm from somewhere, we arbitrarily choose
        #the first node network x spits when we ask it for nodes
        #The first head, is the place we begin the tour, we need it to connect it with the last node
        #of the tour once we are done with the path
        first_head = list(graph.nodes())[0]
        #Node we are currently at
        curr_head = first_head
        visited.add(curr_head)
        path = []
        path.append(curr_head)
        total_distance = 0
        #This guarantees that we visit every single node, as we iterate untill all nodes are in the 
        #path 
        while len(path) != graph.number_of_nodes():
            edges_head = list(graph.edges(curr_head, data = True))
            closest_node_to_head = self.find_closest_no_sorting(edges_head, visited)
            visited.add(closest_node_to_head[1])
            path.append(closest_node_to_head[1])
            curr_head = closest_node_to_head[1]
            total_distance += float(closest_node_to_head[2]['weight'])
        #We finish the path by adding the original node back
        path.append(first_head)
        #Also updating distance
        total_distance += float(graph.edges[curr_head, first_head]["weight"])
        return path, total_distance

