# test_tsp_solver.py
import unittest
import sys
import networkx as nx

class TestTSP(unittest.TestCase):

    def create_test_graph(self):
        self.graph = nx.Graph()
        self.graph.add_weighted_edges_from([
            (0, 1, 10),
            (0, 2, 15),
            (1, 2, 35),
            (1, 3, 25),
            (2, 3, 30),
            (0, 3, 20)
        ])

    def test_tsp_solution(self):
        expected_path = (0, 1, 3, 2) 
        expected_cost = 60
        
        #path, cost = solve_tsp(self.graph)

        self.assertEqual(set(path), set(expected_path))
        self.assertEqual(cost, expected_cost)

    def test_empty_graph(self):
        empty_graph = nx.Graph()
        with self.assertRaises(ValueError):
            #solve_tsp(empty_graph)

    def test_single_node_graph(self):
        single_node_graph = nx.Graph()
        single_node_graph.add_node(0)
        path, cost = solve_tsp(single_node_graph)
        self.assertEqual(path, (0,))
        self.assertEqual(cost, 0)

if __name__ == '__main__':
    unittest.main()
