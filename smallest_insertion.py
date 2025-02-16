class SmallestInsertion(object):
    def __init__(self):
        pass

    def solve(self, graph):
        """
        Solve the smallest insertion problem.
        """
        # randomly select two nodes and set them as a graph g
        nodes = list(graph.nodes)
        tour = [nodes[0], nodes[-1], nodes[0]]
        unvisited = [node for node in nodes if node not in tour]
        currweight = graph[tour[0]][tour[1]]['weight']*2

        while unvisited:

            # look at the unvisited node v
            for u in unvisited:
                best_position = None
                best_cost_increase = float('inf')

                for i in range(1, len(tour)-1):
                    # find the tentative cumulative edge weight of g by adding v to nearest node in g         
                    cand = graph[u][tour[i]]['weight'] + graph[u][tour[i + 1]]['weight'] - graph[tour[i]][tour[i + 1]]['weight']        
                    if cand < best_cost_increase:
                        best_cost_increase = cand
                        best_position = i + 1

                # insert the best node into the best position
                currweight += best_cost_increase
                tour.insert(best_position, u)
                unvisited[:] = [node for node in unvisited if node != u]

        return currweight
