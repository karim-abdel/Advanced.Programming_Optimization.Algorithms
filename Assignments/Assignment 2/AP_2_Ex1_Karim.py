import numpy as np
import networkx as nx

#OPENING FILES
data = []
file1 = open("P1.txt", "r")
data1 =[]
for row in file1:
    data1.append([int(x) for x in list(row)[:-1]])
data.append(data1)
print("first",data1)

file2 = open("P2.txt", "r")
data2 =[]
for k in file2:
    data2.append([int(x) for x in list(k)[:-1]])
data.append(data2)
print("second",data2)


file3 = open("P3.txt", "r")
data3 =[]
for k in file3:
    data3.append([int(x) for x in list(k)[:-1]])
data.append(data3)
print("third",data3)

file4= open("P4.txt", "r")
data4 =[]
for k in file4:
    data4.append([int(x) for x in list(k)[:-1]])
data.append(data4)

file5= open("P5.txt", "r")
data5 =[]
for k in file5:
    data5.append([int(x) for x in list(k)[:-1]])
data.append(data5)

file6= open("P6.txt", "r")
data6=[]
for k in file6:
    data6.append([int(x) for x in list(k)[:-1]])
data.append(data6)

file7= open("P7.txt", "r")
data7 =[]
for k in file7:
    data7.append([int(x) for x in list(k)[:-1]])
data.append(data7)

file8= open("P8.txt", "r")
data8 =[]
for k in file8:
    data8.append([int(x) for x in list(k)[:-1]])
data.append(data8)


file9 = open("P9.txt", "r")
data9 =[]
for k in file9:
    data9.append([int(x) for x in list(k)[:-1]])
data.append(data9)

file10= open("P10.txt", "r")
data10 =[]
for k in file10:
    data10.append([int(x) for x in list(k)[:-1]])
data.append(data10)

file11= open("P11.txt", "r")
data11 =[]
for k in file11:
    data11.append([int(x) for x in list(k)[:-1]])
data.append(data11)

file12= open("P12.txt", "r")
data12 =[]
for k in file12:
    data12.append([int(x) for x in list(k)[:-1]])
data.append(data12)


##END OF OPENING FILES

##CREATING GRAPHS


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

G5 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('5',i,j)
        G5.add_node(p,demand = data5[i][j])
print(G5)

G6 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('6',i,j)
        G6.add_node(p,demand = data6[i][j])
print(G6)

G7 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('7',i,j)
        G7.add_node(p,demand = data7[i][j])
print(G7)

G8 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data8[0])):
        p = ('8',i,j)
        G8.add_node(p,demand = data8[i][j])
print(G8)





G9 = nx.DiGraph()
for i in range(len(data9)):
    for j in range(len(data9[0])):
        p = ('9',i,j)
        G9.add_node(p,demand = data9[i][j])
print(G9)
"""""""""""
G10= nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('10',i,j)
        G10.add_node(p,demand = data10[i][j])
print(G10)
"""""""""
G11 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('11',i,j)
        G11.add_node(p,demand = data11[i][j])
print(G11)

G0 = nx.DiGraph()
for i in range(len(data4)):
    for j in range(len(data4[0])):
        p = ('0',i,j)
        G0.add_node(p,demand = data12[i][j])
print(G0)

## Creating columns
column1 = 100
column2 = 100
column3 = 100
column4 = 100
column5 = 100
column6 = 100
column7 = 100
column8 = 100
column9 = 100
column10=100
column11 = 100
column12 = 100

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




for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data5[i][j] != 0:
            column5 = j



for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data6[i][j] != 0:
            column6 = j



for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data7[i][j] != 0:
            column7 = j



for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data8[i][j] != 0:
            column8 = j



for i in range(len(data9)):
    for j in range(len(data9[0])):
        if data9[i][j] != 0:
            column9 = j




for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data10[i][j] != 0:
            column10 = j




for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data11[i][j] != 0:
            column11 = j




for i in range(len(data4)):
    for j in range(len(data4[0])):
        if data12[i][j] != 0:
            column12 = 1



print(column1, column2, column3,column4,column5, column6,column7,column8, column9,column10, column11, column12)



G12 = nx.compose(G1,G2)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data2[j][k] != 0:
                    G12.add_edge(('1',f,h),('2',j,k),weight = (column2 - column1)%80)


G13 = nx.compose(G1,G3)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data3[j][k] != 0:
                    G13.add_edge(('1',f,h),('3',j,k),weight = (column3 - column1)%80)

G14 = nx.compose(G1,G4)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data4[j][k] != 0:
                    G14.add_edge(('1',f,h),('4',j,k),weight = (column4 - column1)%80)

G15 = nx.compose(G1,G5)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data5[j][k] != 0:
                    G15.add_edge(('1',f,h),('5',j,k),weight = (column5 - column1)%80)


G16 = nx.compose(G1,G6)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data6[j][k] != 0:
                    G16.add_edge(('1',f,h),('6',j,k),weight = (column6 - column1)%80)


G17 = nx.compose(G1,G7)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data7[j][k] != 0:
                    G17.add_edge(('1',f,h),('7',j,k),weight = (column7 - column1)%80)

G18 = nx.compose(G1,G8)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data8[j][k] != 0:
                    G18.add_edge(('1',f,h),('8',j,k),weight = (column8 - column1)%80)





G19 = nx.compose(G1,G9)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data9[j][k] != 0:
                    G19.add_edge(('1',f,h),('9',j,k),weight = (column9 - column1)%80)
"""""""""
G110 = nx.compose(G1,G10)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data10[j][k] != 0:
                    G110.add_edge(('1',f,h),('10',j,k),weight = (column10 - column1)%80)
"""""
G111 = nx.compose(G1,G11)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data11[j][k] != 0:
                    G111.add_edge(('1',f,h),('11',j,k),weight = (column11 - column1)%80)

G01 = nx.compose(G1,G0)
for f in range(10):
    for h in range(80):
        for j in range(10):
            for k in range(80):
                if data1[f][h] != 0 or data12[j][k] != 0:
                    G01.add_edge(('1',f,h),('0',j,k),weight = (column12 - column1)%80)







tot = []
P2= (nx.min_cost_flow_cost(G12))
tot.append(P2)
P3= (nx.min_cost_flow_cost(G13))
tot.append(P3)
P4= (nx.min_cost_flow_cost(G14))
tot.append(P4)
P9 = (nx.min_cost_flow_cost(G19))
tot.append(P9)
P7 = (nx.min_cost_flow_cost(G17))
tot.append(P7)
P12 = (nx.min_cost_flow_cost(G01))
tot.append(P12)
P11 = (nx.min_cost_flow_cost(G111))
tot.append(P11)
P5 = (nx.min_cost_flow_cost(G15))
tot.append(P5)
P6 = (nx.min_cost_flow_cost(G16))
tot.append(P6)
P8 = (nx.min_cost_flow_cost(G18))
tot.append(P8)
#P10 = (nx.min_cost_flow_cost(G110))
#tot.append(P10)




print(tot)






