import tsplib95
import networkx as nx

"""
https://tsplib95.readthedocs.io/en/stable/pages/usage.html
"""

def main():

    wi_set = tsplib95.load('datasets/tsp95/uy734.tsp')
    g_wi = wi_set.get_graph()
    print(nx.approximation.traveling_salesman_problem(g_wi))

    return

if __name__=="__main__":
    main()
