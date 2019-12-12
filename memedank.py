#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import networkx as nx
import community
from community import community_louvain
import matplotlib.pyplot as plt

n = 10  # no. nodes
p = 0.9  # probability for edge creation
graph=nx.erdos_renyi_graph(n, p)
#graph=nx.random_geometric_graph(200, 0.125)
partition=community_louvain.best_partition(graph, weight='weight')
weight='weight'
pos = nx.get_node_attributes(graph, 'pos')

if graph.is_directed():
    raise TypeError("Bad graph type, use only non directed graph")

inc = dict([]) #Defining inc and deg as dictionaries
deg = dict([])
links = graph.size(weight=weight) #Each link = weight = an email
if links == 0:
    raise ValueError("A graph without link has an undefined modularity")

for node in graph: #For all nodes in graph
    com = partition[node] #com = list of all the nodes within partition
    #deg = number of connections to a node
    deg[com] = deg.get(com, 0.) + graph.degree(node, weight=weight) #If can't find com, return 0 +
    for neighbor, datas in graph[node].items():
        edge_weight = datas.get(weight, 1)
        if partition[neighbor] == com: #If neighbour is in same partition
            if neighbor == node:
                inc[com] = inc.get(com, 0.) + float(edge_weight) #Add weight
            else:
                inc[com] = inc.get(com, 0.) + float(edge_weight) / 2.

res = 0. #Define res = result
for com in set(partition.values()):
    res += (inc.get(com, 0.) / links) -                (deg.get(com, 0.) / (2. * links)) ** 2


print(res)


plt.figure(figsize=(8, 8))
nx.draw(graph)
#nx.draw_networkx_edges(graph, pos)
#nx.draw_networkx_nodes(graph, pos)


plt.show()