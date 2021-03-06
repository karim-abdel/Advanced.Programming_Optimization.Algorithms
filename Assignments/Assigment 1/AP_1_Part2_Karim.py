from pulp import *

#create Lp Problem
prob = LpProblem("Part_2",LpMaximize)

#create variables

x0 = LpVariable('x0')
x1 = LpVariable("x1", lowBound= 0)
x2 = LpVariable("x2", lowBound= 0)
x3 = LpVariable("x3", lowBound= 0)
x4 = LpVariable("x4", lowBound= 0)
x5 = LpVariable("x5", lowBound= 0)
x6 = LpVariable("x6", lowBound= 0)

#Set Constraints

prob += x0
prob += -2*x2 +x3 + x4+ x5 +x6 >= x0
prob +=  2*x1 -2*x3 +x4 +x5+ x6 >= x0
prob += -x1 + 2*x2 - 2*x4 + x5 +x6 >= x0
prob += -x1 -x2 +2*x3 - 2*x5 + x6 >= x0
prob += -x1 -x2 -x3 +2*x4 -2*x6 >= x0
prob += -x1 -x2 -x3 -x4 +2*x5 >= x0


#SET A CONSTRAINT CONSIDERING PROBABILITIES HAS TO SUM UP TO 1 IN THIS CASE

prob += x1 + x2 + x3 + x4 + x5 + x6 == 1



# Solve the problem

status = prob.solve(PULP_CBC_CMD(msg=False))

# Print the optimal values
for v in prob.variables():
    print(v.name, "=", v.varValue)