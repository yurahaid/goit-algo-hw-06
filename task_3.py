from networkx.classes import Graph
from graph_factory import create_graph

g = create_graph()

# Add weights
edges = [
    ("A", "B", 4), ("A", "C", 2),
    ("B", "D", 5), ("C", "E", 10), ("D", "E", 3),
    ("D", "F", 8), ("E", "G", 7), ("F", "G", 6)
]

g.add_weighted_edges_from(edges)


def dijkstra(graph: Graph, start: str):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attributes in graph[current_vertex].items():
            distance = distances[current_vertex] + attributes['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

print(dijkstra(g, "A"))

