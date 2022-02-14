from pulp import *

# OPEN THE FILE AND WRITE THE VALUES IN A LIST

a_file = open("part3.txt", "r")
list1= []
for line in a_file:
  stripped_line = line.strip()
  line_list= stripped_line.split()
  list1.append(line_list)
a_file.close()

#CREATE THE LP PROBLEM, THE OBJECTIVE AND ALL THE CONSTRAINTS

comp = []
for i in range(1,70):
  comp.append(i)
prob = LpProblem("Representatives",LpMinimize)
x_vars = LpVariable.dicts("x",comp,0)
#y_vars = LpVariable.dicts("Technicians",time,0)
prob += lpSum(x_vars[i] for i in comp)

## CLARIFICATION: TAKE THE FIRST VALUE FROM I-TH SUBLIST, SUM TO SECOND VALUE FOR I-TH SUBLIST, ADD THE CONSTRAINT
## PUTTING WHAT ABOVE BIGGER OR EQUAL THAN TWO

for i in range(0,len(list1)):
  prob += (x_vars[(int(list1[i][0]))] + x_vars[(int(list1[i][1]))]) >= 2


#SOLVE THE PROBLEM : KEEP TRACK OF HOW MANY REPRESENTATIVES, AND PROGRESSIVELY PRINT THE VALUE OF EACH ONE OF THE,

status = prob.solve(PULP_CBC_CMD(msg=False))
tot = 0.0
for v in prob.variables():
    tot += v.varValue
    print(v.name, ":", v.varValue)
print('The total number of representative is',tot)









