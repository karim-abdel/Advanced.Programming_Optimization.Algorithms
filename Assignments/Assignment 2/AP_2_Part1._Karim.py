import networkx as nx
import numpy as np
##READ THE FILES

files = []
images = []
for i in range(1,13):
    pippo = f"P{i}.txt"
    insert = open(pippo, "r")
    files.append(insert)
for pluto in files:
    data = []
    for row in pluto:
        data.append([int(x) for x in list(row)[:-1]])
    images.append(np.array(data))

##NORMALIZE THE IMAGES
png_norm = []
for k in images:
    tot = 0
    for row in k:
        tot = sum(row) + tot
    if tot == 80:
        png_norm.append(k*39)
    else:
        png_norm.append(k*80)

    #png_norm.append(((k+tot-1)//tot)*1000)

#CREATE THE GRAPH CORRESPONDIG TO THE INITAL PICTURE 1

G1 = nx.DiGraph()
for i in range(10):
    for j in range(80):
        p = ('1',i,j)
        G1.add_node(p,demand = -png_norm[0][i][j])

#CREATE A LIST CONTAINING ALL THE OTHERS 11 GRAPHS

graphs = []
for k in range(1,12):
    Gr = nx.DiGraph()
    #Gr = G_f"{k+1}"
    for i in range(10):
        for j in range(80):
            p = (f"{k+1}", i, j)
            Gr.add_node(p, demand = png_norm[k][i][j])
    graphs.append(Gr)

#ITERATING OVER THE LIST OF GRAPHS, FOR EACH OF THEM CREATE A UNION WITH G1. NOW ADD EDGES BETWEEN NON-ZERO COMPONENTS,
#FOR EACH OF THIS COMBINATIONS CALCULATE THE DISTANCE BETWEEN THE TWO IMAGES

dist = {}
for i in range(1,12):
    gap = nx.compose(G1,graphs[i-1])
    for f in range(10):
        for h in range(80):
            for j in range(10):
                for k in range(80):
                    if png_norm[0][f][h] != 0 or png_norm[i][j][k] != 0:
                        gap.add_edge(('1',f,h),(f"{i+1}",j,k),weight = (k - h)%80)
    cost = nx.min_cost_flow_cost(gap)
    dist[f"{i+1}"] = cost


#WE KNOW THE DISTANCE FROM IMAGE 1 FROM ITSELF IS 0. NOW, SORT ALL THE OTHER DISTANCES AND PRINT THE OUTPUT

final = ['1']
for j in sorted(dist, key = dist.get):
    final.append(j)
print(final)

