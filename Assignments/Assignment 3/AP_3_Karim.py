from pulp import *
from matplotlib import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#OPENING AND STORING DATA OF THE FILE
a_file = open("bakery.txt", "r")
data= []
for line in a_file:
  stripped_line = line.strip()
  line_list= stripped_line.split()
  data.append(line_list)
a_file.close()
for i in range(len(data)):
  for j in range(len(data[0])):
    data[i][j] = int(data[i][j])

#INITIALIZE LP PROBLEM

prob = LpProblem("bakery",LpMinimize)
comp = [i for i in range(0, 17)]
s_vars = LpVariable.dicts("s",comp,0, cat = "Integer")
y = LpVariable("y", lowBound= 0)
v = LpVariable.dicts("v", [(i, j) for i in range(17) for j in range(17)], cat="Binary")
#ADD OBJECTIVE AND CONSTRAINT, ALSO THE ONE INCLUDING THE M-METHOD
prob += y
M = 27001
for i in range(17):
    prob += s_vars[i] >= data[i][1]
    prob += s_vars[i] + data[i][3] <= data[i][2]
    prob += y >= s_vars[i] + data[i][3]
    for j in range(17):
        if j > i:
            prob += s_vars[i] + data[i][3] <= s_vars[j] + M * v[i, j]
            prob += s_vars[j] + data[j][3] <= s_vars[i] + M * (1 - v[i, j])

#SOLVE, PRINT THE RESULTS and STORE THEM FOR THE PLOT
l_st = []
l_end=[]
status = prob.solve(PULP_CBC_CMD(msg=False))
print('the process will finish at:',value(prob.objective))
dict = {}
for i in range(17):
    k = value(s_vars[i])
    l_st.append(k)
    l_end.append((k + data[i][3]))
    dict[i] = value(s_vars[i])
    print(f's_{i}:',value(s_vars[i]))
f = sorted(dict.items(), key=lambda x:x[1])

ppp = [str(x[0]) for x in f]


dur = []
##dur is the deadline in order of baking
for i in range(17):
    dur.append(data[int(ppp[i])][2])
#app is duration in order of baking
app = []
for i in range(17):
    app.append(data[int(ppp[i])][3])
##ofl is original starting time
ofl = []
for i in range(17):
    ofl.append(data[int(ppp[i])][1])

#ADJUST THE LIST TO MAKE THE PLOTS
l_st.sort()
ded = l_end
l_end.sort()
#CREATE THE PLOT, THE AXIS, SET THE TICKS ON THE X-AXIS, ETC
fig, ax = plt.subplots(1, figsize=(18,6))
plt.xlabel("Seconds when a pastry is removed/inserted",color = 'black')
plt.ylabel("Pastries",color = 'black')
plt.title("Bakery Scheduling", color = 'black')
ax.set_xticks(ded)
ax.set_xlim(0, 27200)
cmap =plt.cm.gist_rainbow
norm = colors.Normalize(vmin= 0, vmax= 9000)
ax.tick_params(axis='x',labelsize= 10, pad = 2, color = 'red', rotation = 90)

#REPRESENT THE SOLUTION, INSERT ALSO BLACK CONTOUR IF IT IS A CRITICAL PREPARATION

for i in range(17):
    ax.barh(f'Pastry {ppp[i]}', dur[i] - ofl[i], left=ofl[i], color='0.85', edgecolor='pink')
    ax.barh(f'Pastry {ppp[i]}', app[i], left=l_st[i], color=cmap(norm(dur[i] - l_end[i])), edgecolor='pink')
    if (l_st[i] == ofl[i]):
        ax.barh(f'Pastry {ppp[i]}', app[i], left= l_st[i], color=cmap(norm(dur[i] - l_end[i])), edgecolor = 'black')

    if  data[i][2] - l_end[i] < 60:
        ax.barh(f'Pastry {ppp[i]}', dur[i] - ofl[i], left=ofl[i], color='0.85', edgecolor='pink')
        ax.barh(f'Pastry {ppp[i]}', app[i], left= l_st[i], color=cmap(norm(dur[i]-l_end[i])), edgecolor = 'pink')
    ax.text(dur[i] + 3,f'Pastry {ppp[i]}' , f'DLN {dur[i]}', color = 'black', fontsize = 6)


#CREATE THE LEGEND, TEXT OF DEADLINES NEXT TO THE BOXES

red_line  = mlines.Line2D([], [], color='black', label='Critical Preparation')
pop_b = mpatches.Patch(color='0.85', label='Time when the pastry is available for baking')
plt.legend(handles=[pop_b,red_line],loc= (0.55,0.3), edgecolor = 'black')

ax.text(1.03, 0.5, "Seconds remaining before the deadline",
        rotation=90, size=9, weight='bold',
        ha='center', va='center', transform=ax.transAxes)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
fig.colorbar(sm)

plt.show()

