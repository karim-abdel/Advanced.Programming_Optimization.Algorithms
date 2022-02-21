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
prob += lpSum(x_vars[i] for i in comp)
## CLARIFICATION: TAKE THE FIRST VALUE FROM I-TH SUBLIST, SUM TO SECOND VALUE FOR I-TH SUBLIST, ADD THE CONSTRAINT
## PUTTING WHAT ABOVE BIGGER OR EQUAL THAN TWO

for i in range(0,len(list1)):
  prob += (x_vars[(int(list1[i][0]))] + x_vars[(int(list1[i][1]))]) >= 2


#SOLVE THE PROBLEM : PRINT THE NUMBER OF REPRESENTATIVE FOR EACH COMPANY, AND PRINT THE TOTAL.

status = prob.solve(PULP_CBC_CMD(msg=False))
for i in comp:
    print("Representatives from company",i,":",value(x_vars[i]))
print('The total number of representative envolved is',value(prob.objective))










