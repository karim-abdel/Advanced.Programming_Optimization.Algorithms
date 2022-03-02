import numpy as np
import networkx as nx
file1 = open("P1.txt", "r")
data1 =[]
for row in file1:
    data1.append([int(x) for x in list(row)[:-1]])
#data1 = np.array(data1)
print("first",data1)

file2 = open("P2.txt", "r")
data2 =[]
for k in file2:
    data2.append([int(x) for x in list(k)[:-1]])
#data2= np.array(data2)
print("second",data2)


file3 = open("P3.txt", "r")
data3 =[]
for k in file3:
    data3.append([int(x) for x in list(k)[:-1]])
#data3= np.array(data3)
print("third",data3)

file4= open("P4.txt", "r")
data4 =[]
for k in file4:
    data4.append([int(x) for x in list(k)[:-1]])
#data3= np.array(data3)


file9 = open("P9.txt", "r")
data9 =[]
for k in file9:
    data9.append([int(x) for x in list(k)[:-1]])
#data3= np.array(data3)





G1 = nx.DiGraph()
for i in range(len(data1)):
    for j in range(len(data1[0])):
        p = ('1',i,j)
        G1.add_node(p,demand = -data1[i][j])
print(G1)
print(G1.nodes[('1',5,35)])

G2 = nx.DiGraph()
for i in range(len(data2)):
    for j in range(len(data2[0])):
        p = ('2',i,j)
        G2.add_node(p,demand= data2[i][j])
print(G2)

G3 = nx.DiGraph()
for i in range(len(data3)):
    for j in range(len(data3[0])):
        p = ('3',i,j)
        G3.add_node(p,demand = data3[i][j])
print(G3)

G4 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('4',i,j)
        G4.add_node(p,demand = data4[i][j])
print(G4)

G9 = nx.DiGraph()
for i in range(len(data9)):
    for j in range(len(data9[0])):
        p = ('9',i,j)
        G9.add_node(p,demand = data9[i][j])
print(G9)

column1 = 100
column2 = 100
column3 = 100
column4 = 100
column9 = 100

for i in range(len(data1)):
    for j in range(len(data1[0])):
        if data1[i][j] != 0:
            column1 = j
for i in range(len(data2)):
    for j in range(len(data2[0])):
        if data2[i][j] != 0:
            column2 = j

for i in range(len(data3)):
    for j in range(len(data3[0])):
        if data3[i][j] != 0:
            column3 = j

for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data4[i][j] != 0:
            column4 = j
for i in range(len(data9)):
    for j in range(len(data9[0])):
        if data9[i][j] != 0:
            column9 = j

print(column1, column2, column3,column4, column9)



G12 = nx.compose(G1,G2)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data2[j][k] != 0:
                    G12.add_edge(('1',f,h),('2',j,k),weight = column2 - column1)


G13 = nx.compose(G1,G3)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data3[j][k] != 0:
                    G13.add_edge(('1',f,h),('3',j,k),weight = column3 - column1)

G14 = nx.compose(G1,G4)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data4[j][k] != 0:
                    G14.add_edge(('1',f,h),('4',j,k),weight = column4 - column1)

G19 = nx.compose(G1,G9)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data9[j][k] != 0:
                    G19.add_edge(('1',f,h),('9',j,k),weight = column9 - column1)





print(nx.min_cost_flow_cost(G12))
print(nx.min_cost_flow_cost(G13))
print(nx.min_cost_flow_cost(G14))
print(nx.min_cost_flow_cost(G19))






