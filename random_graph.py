import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
import numpy

G = nx.gnm_random_graph(50, 1000)

for (u, v) in G.edges():
    if u != v:
        G.edges[u,v]['weight'] = random.randint(0,10)
    else:
        G.edges[u,v]['weight'] = 0
matrix = nx.to_numpy_matrix(G, weight='weight')

def isValid():
	if g.is_metric():
		return "Graph is is_metric"
	else:
		shortest = dict(nx.floyd_warshall(G))
    for u, v, datadict in G.edges(data=True):
        if abs(shortest[u][v] - datadict['weight']) >= 0.00001:
        	G.edges[u,v]['weight'] = random.randint(0,10)
