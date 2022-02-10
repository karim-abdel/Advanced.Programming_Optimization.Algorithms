from pulp import *
a_file = open("part3.txt", "r")

list1= []
for line in a_file:
  stripped_line = line.strip()
  line_list= stripped_line.split()
  list1.append(line_list)
a_file.close()


comp = []
for i in range(1,70):
  comp.append(i)
prob = LpProblem("Representatives",LpMinimize)
x_vars = LpVariable.dicts("x",comp,0)
#y_vars = LpVariable.dicts("Technicians",time,0)
prob += lpSum(x_vars[i] for i in comp)

for i in range(0,len(list1)):
  prob += (x_vars[(int(list1[i][0]))] + x_vars[(int(list1[i][1]))]) >= 2

status = prob.solve(PULP_CBC_CMD(msg=False))
tot = 0.0
for v in prob.variables():
    tot += v.varValue
    print(v.name, ":", v.varValue)
print('The total number of representative is',tot)









