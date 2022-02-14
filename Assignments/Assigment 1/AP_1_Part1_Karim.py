from pulp import *
import numpy as np

## CREATE THE LP PROBLEM, ADD THE OBJECTIVE FUNCTION AND THE COSTRAINTS

prob = LpProblem("Part_1",LpMinimize)
x = LpVariable("x", lowBound=-10)
y = LpVariable("y", upBound=10)
prob += 122*x + 143*y
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
for name, constraint in prob.constraints.items():
    if ((f"{constraint.value()==0.0}") == "False"):
        i += 1
    else:
        print(i)
        i += 1
        j += 1

## LET'S DEFINE TWO LIST: "OBJ" WILL CONTAIN THE COEFFICIENTS OF THE OBJECTIVE FUNCTION, WHILE "CON" WILL BE A LIST
# OF LIST THAT CONTAIN THE COEFFICIENTS OF THE CONSTRAINTS

obj = []
con = []
obj.append(list(prob.objective.values()))
norm = np.flip(obj)
v = norm[0][0]
norm[0][0]=-v
print(norm)
for o in range(i-1):
    con.append(list(list(prob.constraints.items())[o][1].values()))
q = np.array(con)
w = np.array(norm)

##CREATE A LIST THAT CONTAINS THE REMAINDERS OF DIVISION BETWEEN THE COEFFICIENTS OF THE OBJECTIVES AND OF THE CONSTRAINTS

#alpha = q % w



## NOW CHECK IF THERE IS A REMAINDER EQUAL TO 0. IF SO, THE SOLUTION IS NOT UNIQUE ( SINCE WE ARE IN R^2 THIS IS ENOUGH)
## I CHECK THE REMAINDER OF THE DIVISION AS A WAY TO CHECK IF THE OBJECTIVE FUNCTION IS COLLINEAR TO SOME CONSTRAINT

check = 0
for z in range(i-1):
   if (np.dot(q[z],w[0])==0):
        check +=1
   else:
        pass
if (check == 0):
    print(("Unique Optimal Solution: Yes"))
else:
    print(("Unique Optimal Solution: No"))



