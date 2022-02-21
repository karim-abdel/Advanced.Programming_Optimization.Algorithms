from pulp import *

## CREATE THE LP PROBLEM, ADD THE OBJECTIVE FUNCTION AND THE CONSTRAINTS

prob = LpProblem("Part_1",LpMinimize)
x = LpVariable("x", lowBound=-10)
y = LpVariable("y", upBound=10)
prob += 122*x + 143*y
prob += x >= -10
prob += y <= 10
prob += 3*x + 2*y <= 10
prob += 12*x + 14*y >= -12.5
prob += 2*x + 3*y >= 3
prob += 5*x -6*y >= -100

## SOLVE THE PROBLEM

status = prob.solve(PULP_CBC_CMD(msg=False))

## PRINT THE VALUES THAT GIVES THE SOLUTION AND THE OBJECTIVE VALUE

print("Optimal solution:", "x =", (value(x)) ,"and", "y =", value(y))
print("Objective Value:", value(prob.objective))

## PRINT THE TIGHT COSTRAINTS

i = 1
j = 0
k = True
print("Tight constraints:")
for constraint in prob.constraints.values():
    if ((f"{constraint.value()==0.0}") == "False"):
        i += 1
    else:
        print(i)
        i += 1
        j += 1


firstx = value(x)
firsty = value(y)

k = 0
##UNIQUENESS - CREATE NEW LINEAR PROGRAMS TO CHECK THE UNIQUENESS

##First new LP
prob1 = LpProblem('Unique_1',LpMinimize)
x1 = LpVariable("x1", lowBound=-10)
y = LpVariable("y", upBound=10)
prob1 += x1
prob1 += x1 >= -10
prob1 += y <= 10
prob1 += 122*x1 + 143*y == -122
prob1 += 3*x1 + 2*y <= 10
prob1 += 12*x1 + 14*y >= -12.5
prob1 += 2*x1 + 3*y >= 3
prob1 += 5*x1 -6*y >= -100
status = prob1.solve(PULP_CBC_CMD(msg=False))
if value(x1) == firstx:
    pass
else:
    k += 1
#print("Optimal solution:", "x1 =", (value(x1)) )


##Second new LP
prob2 = LpProblem('Unique_2',LpMaximize)
x2 = LpVariable("x2", lowBound=-10)
y = LpVariable("y", upBound=10)
prob2 += x2
prob2 += x2 >= -10
prob2 += y <= 10
prob2 += 122*x2 + 143*y == -122
prob2 += 3*x2 + 2*y <= 10
prob2 += 12*x2 + 14*y >= -12.5
prob2 += 2*x2 + 3*y >= 3
prob2 += 5*x2 -6*y >= -100
status = prob2.solve(PULP_CBC_CMD(msg=False))
if value(x2) == firstx:
    pass
else:
    k +=1

#print("Optimal solution:", "x2 =", (value(x2)) )

#Third LP
prob3 = LpProblem('Unique_3',LpMaximize)
x = LpVariable("x", lowBound=-10)
y1 = LpVariable("y1", upBound=10)
prob3 += y1
prob3 += x >= -10
prob3 += y1 <= 10
prob3 += 122*x + 143*y1 == -122
prob3 += 3*x + 2*y1 <= 10
prob3 += 12*x + 14*y1 >= -12.5
prob3 += 2*x + 3*y1 >= 3
prob3 += 5*x -6*y1 >= -100
status = prob3.solve(PULP_CBC_CMD(msg=False))
if value(y1) == firsty:
    pass
else:
    k += 1
#print("Optimal solution:", "y1 =", (value(y1)) )

#Fourth LP
prob4 = LpProblem('Unique_4',LpMinimize)
x = LpVariable("x", lowBound=-10)
y2 = LpVariable("y2", upBound=10)
prob4 += y2
prob4 += x >= -10
prob4 += y2 <= 10
prob4 += 122*x + 143*y2 == -122
prob4 += 3*x + 2*y2 <= 10
prob4 += 12*x + 14*y2 >= -12.5
prob4 += 2*x + 3*y2 >= 3
prob4 += 5*x -6*y2 >= -100
status = prob4.solve(PULP_CBC_CMD(msg=False))
if value(y2) == firsty:
    pass
else:
    k +=1

#print("Optimal solution:", "y2 =", (value(y2)) )


#CHECK UNIQUENESS OF THE SOLUTION
if (k == 0):
    print(("Unique Optimal Solution: Yes"))
else:
    print(("Unique Optimal Solution: No"))

