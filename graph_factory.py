import networkx as nx
from networkx.classes import Graph


def create_graph() -> Graph:
    g = nx.Graph()

    # Add vertex (city transport network)
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    g.add_nodes_from(nodes)

    # Add edges - roads
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E"),
        ("D", "F"),
        ("E", "G"),
        ("F", "G")
    ]

    g.add_edges_from(edges)

    return g
