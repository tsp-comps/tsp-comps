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
            best_node = None
            best_cost_increase = float('inf')
            best_position = None

            # look at the unvisited node v
            for u in unvisited:

                for i in range(len(tour)):
                    # find the tentative cumulative edge weight of g by adding v to nearest node in g                    
                    if graph[u][tour[i]]['weight'] < best_cost_increase:
                        best_cost_increase = graph[u][tour[i]]['weight']
                        # update the best solution
                        best_node = u
                        best_position = i + 1  

                # insert the best node into the best position
                currweight += best_cost_increase
                tour.insert(best_position, best_node)
                unvisited[:] = [node for node in unvisited if node != best_node]

        return currweight
    
# for testing purposes
from datasets import Datasets

if __name__ == "__main__":
    si = SmallestInsertion()
    graph = Datasets.process_tsp95("datasets/tsp95/wi29.tsp")
    print(si.solve(graph))
    sol = nx.approximation.traveling_salesman_problem(graph)
    print(sum([graph[sol[i]][sol[i+1]]['weight'] for i in range(len(sol)-1)]))
