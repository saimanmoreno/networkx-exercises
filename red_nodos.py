# diseñar una red de 6 nodos y encontrar todos los posibles 
# caminos entre un nodo origen y un nodo destino

import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

graph.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f'])

graph.add_edges_from([
    ('a', 'b'), ('a', 'c'), ('b', 'e'), ('b', 'd'), ('c', 'f')
])

networkx.draw(graph, with_labels=True, font_weight='bold')

# plt.show()

# generate all simple paths in the graph G from source to target

todos_caminos = networkx.all_simple_paths(graph, 'a', 'b')

print(todos_caminos)