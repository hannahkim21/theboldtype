import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
import numpy

"""Creating inputs for 50.in"""
G_50 = nx.gnm_random_graph(50, 800)

for (u, v) in G_50.edges():
    if u == v:
        G_50.edges[u,v]['weight'] = 0
    G_50.edges[u,v]['weight'] = random.randint(1, 1000)

matrix50 = nx.to_numpy_matrix(G_50, weight='weight')
floydwarsh50 = dict(nx.floyd_warshall(G_50))
x = matrix50.shape[0]
y = matrix50.shape[1]
for i in range(x):
    for j in range(y):
        if floydwarsh50[i][j] < matrix50[i, j]:
            matrix50[i, j] = floydwarsh50[i][j]


f = open("inputs/50.in", "w")
"""The number of locations"""
f.write("50\n")

"""The number of homes"""
f.write("25\n")

"""The location names"""
for i in range(50):
    f.write(str(i)+" ")
f.write("\n")

"""The home names"""
for i in range(25):
    f.write(str(i)+" ")
f.write("\n")

"""The start location"""
f.write("0\n")

"""Writing the weights"""
x = matrix50.shape[0]
y = matrix50.shape[1]
for i in range(x):
    for j in range(y):
        if matrix50[i, j] == 0.0:
            f.write("x"+" ")
        else:
            f.write(str(matrix50[i, j])+" ")
    f.write("\n")

f.close()

"""FIXME ALEXIA"""
"""Creating outputs for 50.in"""
f = open("outputs/50.out", "w")
f.write("0  0\n")

"""The number of dropoff locations"""
f.write("1\n")

for i in range(25):
    f.write("0 " + str(i) + "\n")
f.close()

"""Creating inputs for 100.in"""
G_100 = nx.gnm_random_graph(100, 4000)

for (u, v) in G_100.edges():
    if u == v:
        G_100.edges[u,v]['weight'] = 0
    G_100.edges[u,v]['weight'] = random.randint(1, 1000)

matrix100 = nx.to_numpy_matrix(G_100, weight='weight')
floydwarsh100 = dict(nx.floyd_warshall(G_100))
x = matrix100.shape[0]
y = matrix100.shape[1]
for i in range(x):
    for j in range(y):
        if floydwarsh100[i][j] < matrix100[i, j]:
            matrix100[i, j] = floydwarsh100[i][j]


f = open("inputs/100.in", "w")
"""The number of locations"""
f.write("100\n")

"""The number of homes"""
f.write("50\n")

"""The location names"""
for i in range(100):
    f.write(str(i)+" ")
f.write("\n")

"""The home names"""
for i in range(50):
    f.write(str(i)+" ")
f.write("\n")

"""The start location"""
f.write("0\n")

"""Writing the weights"""
x = matrix100.shape[0]
y = matrix100.shape[1]
for i in range(x):
    for j in range(y):
        if matrix100[i, j] == 0.0:
            f.write("x"+" ")
        else:
            f.write(str(matrix100[i, j])+" ")
    f.write("\n")

f.close()

"""FIXME ALEXIA"""
"""Creating outputs for 100.in"""
f = open("outputs/100.out", "w")

"""The home names are the path taken by the car"""
f.write("0  0\n")

"""The number of dropoff locations"""
f.write("1\n")

for i in range(50):
    f.write("0 " + str(i) + "\n")


f.close()


"""Creating inputs for 200.in"""
G_200 = nx.gnm_random_graph(200, 16000)

for (u, v) in G_200.edges():
    if u == v:
        G_200.edges[u,v]['weight'] = 0
    G_200.edges[u,v]['weight'] = random.randint(1, 1000)

matrix200 = nx.to_numpy_matrix(G_200, weight='weight')
floydwarsh200 = dict(nx.floyd_warshall(G_200))
x = matrix200.shape[0]
y = matrix200.shape[1]
for i in range(x):
    for j in range(y):
        if floydwarsh200[i][j] < matrix200[i, j]:
            matrix200[i, j] = floydwarsh200[i][j]


f = open("inputs/200.in", "w")
"""The number of locations"""
f.write("200\n")

"""The number of homes"""
f.write("100\n")

"""The location names"""
for i in range(200):
    f.write(str(i)+" ")
f.write("\n")

"""The home names"""
for i in range(100):
    f.write(str(i)+" ")
f.write("\n")

"""The start location"""
f.write("0\n")

"""Writing the weights"""
x = matrix200.shape[0]
y = matrix200.shape[1]
for i in range(x):
    for j in range(y):
        if matrix200[i, j] == 0.0:
            f.write("x"+" ")
        else:
            f.write(str(matrix200[i, j])+" ")
    f.write("\n")

f.close()

"""FIXME ALEXIA"""
"""Creating outputs for 200.in"""
f = open("outputs/200.out", "w")

f.write("0  0\n")

"""The number of dropoff locations"""
f.write("1\n")

for i in range(100):
    f.write("0 " + str(i) + "\n")

f.close()
