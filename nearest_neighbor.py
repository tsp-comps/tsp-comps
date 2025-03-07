import networkx as nx
class NeareastNeighbor:
    def __init__(self):
        pass
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
            #We get and sort all of the nodes
            edges_head = list(graph.edges(curr_head, data = True))
            closest_nodes_to_head = sorted(edges_head, key = lambda x: float(x[2]['weight']))
            #We find the closest unvisited node
            for node in closest_nodes_to_head:
                if node[1] not in visited:
                    visited.add(node[1])
                    path.append(node[1])
                    curr_head = node[1]
                    total_distance += float(node[2]['weight'])
                    break
        #We finish the path by adding the original node back
        path.append(first_head)
        #Also updating distance
        total_distance += float(graph.edges[curr_head, first_head]["weight"])
        return path, total_distance
