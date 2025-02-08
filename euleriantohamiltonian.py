import networkx as nx

def eulerian_to_hamiltonian(eulerian_tour):
    visited_nodes = {}
    for node in eulerian_tour:
        visited_nodes.update({node : False})
    hamiltonian_path = []

    for node in eulerian_tour:
        if not visited_nodes[node]:
            hamiltonian_path.append(node)
        visited_nodes.update({node : True})
    return hamiltonian_path