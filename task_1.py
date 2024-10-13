import networkx as nx
import matplotlib.pyplot as plt

from graph_factory import create_graph

g = create_graph()

# Analyze main characteristic
num_nodes = g.number_of_nodes()
num_edges = g.number_of_edges()
degrees = dict(g.degree())

print("Number of Nodes:", num_nodes)
print("Number of Edges:", num_edges)
print("Degree of Nodes:", degrees)

# Visualize
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15,
        font_weight='bold')
plt.title("Transport Network Graph", fontsize=16)
plt.show()

