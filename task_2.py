from collections import deque

import networkx as nx
from networkx.classes import Graph

from graph_factory import create_graph

g = create_graph()

def dfs_recursive(graph: Graph, vertex: str, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def bfs_iterative(graph: Graph, start: str):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


print("\nDFS Path from A to G:")
dfs_recursive(g, "A")

print("\nBFS Path from A to G:")
bfs_iterative(g, "A")