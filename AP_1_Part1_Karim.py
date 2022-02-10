from pulp import *
prob = LpProblem("Part_1",LpMinimize)
x = LpVariable("x", lowBound=-10)
y = LpVariable("y", upBound=10)
prob += 122*x + 143*y
prob += 3*x + 2*y <= 10
prob += 12*x + 14*y >= -12.5
prob += 2*x + 3*y >= 3
prob += 5*x -6*y >= -100
status = prob.solve(PULP_CBC_CMD(msg=False))
#print(LpStatus[status])
print("Optimal solution:", "x =", (value(x)) ,"and", "y =", value(y))
print("Objective Value:", value(prob.objective))
i = 1
j = 0
print("Tight constraints:")
for name, constraint in prob.constraints.items():
    if ((f"{constraint.value()==0.0}") == "False"):
        i += 1
    else:
        print(i)
        i += 1
        j += 1
if (j>=2):
    print(("Unique Optimal Solution: Yes"))
else:
    print(("Unique Optimal Solution: No"))






