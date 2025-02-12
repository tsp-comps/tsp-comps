import random
import networkx as nx

class SmallestInsertion(object):
    def __init__(self):
        pass

    def solve(self, graph):
        """
        Solve the smallest insertion problem.
        """
        # randomly select two nodes and set them as a graph g
        nodes = list(graph.nodes)
        tour = random.sample(nodes, 2)
        unvisited = [node for node in nodes if node not in tour]
        currweight = graph[tour[0]][tour[1]]['weight']

        while unvisited:
            best_cost_increase = float('inf')
            best_position = None

            # look at the unvisited node v
            for u in unvisited:

                for i in range(len(tour)):
                    # find the tentative cumulative edge weight of g by adding v to nearest node in g         
                    cand = graph[u][tour[i]]['weight'] + graph[u][tour[(i+1) % len(tour)]]['weight'] \
                            - graph[tour[i]][tour[(i+1) % len(tour)]]['weight']           
                    if cand < best_cost_increase:
                        best_cost_increase = cand
                        best_position = i + 1

                # insert the best node into the best position
                currweight += best_cost_increase
                tour.insert(best_position, u)
                unvisited[:] = [node for node in unvisited if node != u]

        print(tour)
        return currweight
