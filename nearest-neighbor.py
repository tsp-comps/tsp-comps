import networkx as nx


def smallest_insertion(graph):
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
        #print(curr_head)
        edges_head = list(graph.edges(curr_head, data = True))
        closest_nodes_to_head = sorted(edges_head, key = lambda x: float(x[2]['weight']))
        for node in closest_nodes_to_head:
            if node[1] not in visited:
                visited.add(node[1])
                path.append(node[1])
                curr_head = node[1]
                total_distance += float(node[2]['weight'])
                break
    path.append(first_head)
    return path, total_distance
    


