import networkx as nx

class SmallestInsertion(object):
    def __init__(self):
        pass

    def solve(self, graph):
        """
        Solve the smallest insertion problem.
        """
        # create a new graph to store the solution
        solution = nx.Graph()
        solution.add_node(0)

        # add the remaining nodes to the solution
        while len(solution.nodes) < len(graph.nodes):
            node = self.find_closest_node(graph, solution)
            solution.add_node(node)
            path = self.find_shortest_path(solution, node)
            solution = self.insert_node(solution, path, node)

        return solution