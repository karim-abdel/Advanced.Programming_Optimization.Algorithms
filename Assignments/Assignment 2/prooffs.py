import networkx as nx
import numpy as np

files = []
images = []
for i in range(1,13):
    call = f"P{i}.txt"
    insert = open(call, "r")
    files.append(call)
for obj in files:
    data = []
    for row in obj:
        data.append([int(x) for x in list(row)[:-1]])
    images.append(np.array(data))
png_norm = []
print(images)
for k in images:
    tot = 0
    for f in i:
        tot=sum(f) + x
    png_norm.append((k/tot)*1000)

G_1= nx.DiGraph()
for i in range(len(data_1)):
    for j in range(len(data_1[0])):
        p = ('1',i,j)
        G1.add_node(p,demand = -data_1[i][j])
print(G_1)
print(G1.nodes[('1',5,35)])
