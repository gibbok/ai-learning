import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Define the layout for NetworkX plot
pos = nx.spring_layout(G)

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot NetworkX graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1500,
    edge_color="black",
    linewidths=1,
    font_size=15,
    ax=ax1,
)
ax1.set_title("NetworkX Graph")

# Plot linear chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax2.plot(x, y, marker="o", color="r")
ax2.set_title("Linear Chart")

# Display the plot
plt.tight_layout()
plt.show()
