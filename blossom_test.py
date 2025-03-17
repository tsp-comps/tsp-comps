import networkx as nx
import matplotlib.pyplot as plt

# Drew from many sources in compiling this code together including CMU & Stanford
# To all those with other open source code on the internet I thank you
# Find the lowest common ancestor in the blossom tree
def lca(match, base, p, a, b):
    used = [False] * len(match)
    while True:
        a = base[a]
        used[a] = True
        if match[a] == -1:
            break
        a = p[match[a]]
    while True:
        b = base[b]
        if used[b]:
            return b
        b = p[match[b]]

# Mark the path from v to the base of the blossom
def mark_path(match, base, blossom, p, v, b, children):
    while base[v] != b:
        blossom[base[v]] = blossom[base[match[v]]] = True
        p[v] = children
        children = match[v]
        v = p[match[v]]

def find_path(graph, match, p, root):
    n = graph.number_of_nodes()
    used = [False] * n
    p[:] = [-1] * n
    base = list(range(n))
    used[root] = True
    q = [root]

    while q:
        v = q.pop(0)
        for to in graph.neighbors(v):
            if base[v] == base[to] or match[v] == to:
                continue
            if to == root or (match[to] != -1 and p[match[to]] != -1):
                curbase = lca(match, base, p, v, to)
                blossom = [False] * n
                mark_path(match, base, blossom, p, v, curbase, to)
                mark_path(match, base, blossom, p, to, curbase, v)
                for i in range(n):
                    if blossom[base[i]]:
                        base[i] = curbase
                        if not used[i]:
                            used[i] = True
                            q.append(i)
            elif p[to] == -1:
                p[to] = v
                if match[to] == -1:
                    return to
                to = match[to]
                used[to] = True
                q.append(to)
    return -1

# Implementation of Blossom Algorithm
def max_matching(graph):
    n = graph.number_of_nodes()
    match = [-1] * n
    p = [0] * n
    for i in range(n):
        if match[i] == -1:
            v = find_path(graph, match, p, i)
            while v != -1:
                pv = p[v]
                ppv = match[pv]
                match[v] = pv
                match[pv] = v
                v = ppv
    
    match_graph = nx.create_empty_copy(G)
    for i in range(n):
        match_graph.add_edge(i, match[i])
    return match_graph

def draw_graph(G):
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    plt.title("Fully Connected Graph with Random Weights")
    plt.show()


G = nx.complete_graph(20)
draw_graph(max_matching(G))