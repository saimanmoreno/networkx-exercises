# diseñar una red de 6 nodos y encontrar todos los posibles 
# caminos entre un nodo origen y un nodo destino

import networkx

G = networkx.Graph()    # create an empty graph with no nodes and no edges

# graph is a collections of nodes (vertices) along with
# identified pairs of node (called edges, links, etc.)

G.add_node(1)   # add one node at time

G.add_nodes_from([2,3])     #add nodes from any iterable container, such as a list

# add nodes along with node attributes:

G.add_nodes_from([
    (4, {"colour": "red"}),
    (5, {"colour": "green"}),
])

G.add_edge(1,2)     # add one edge at a time

G.add_edges_from([(1,2), (1,3)])    # adding a list of edges

print(G.nodes)      # print all nodes of graph G
print(G.edges)      # print all edges of graph G

print(G.number_of_edges())  # see numbers of node
print(G.number_of_edges)    # see numbers of edges

G.degree[1]     # the number of edges incident to 1
list(G.adj[1])  # imprime a list of neighbours of node 1 or list(G.neighbors(1))

G.clear()       # remove all nodes and edges


