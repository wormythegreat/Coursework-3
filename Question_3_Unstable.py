from Question_2 import rdot,gdot
import matplotlib.pyplot as plt
import numpy as np
from math import floor,sin,cos,pi

plt.clf()
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Unstable Manifold")

def plot_line(start_r,start_g):
    max = 6
    t = 0.00001
    nstep = floor(max/t)
    t_total = [0]
    r = [start_r]   #make this the saddle point its self
    g = [start_g]
    j = 0

    while (abs(r[-1]) - 2 < 0.002) and (abs(g[-1] - 1 < 0.002)):
        r.append(r[j] + (t * rdot(r[j],g[j])))
        g.append(g[j] + (t * gdot(r[j],g[j])))
        t_total.append(float(t_total[j] + t))
        j = j + 1

    plt.plot(r,g,'green')

#saddle point (2,1)
h = 0.001
lines = 30
angles = np.linspace(0,2*pi,lines)
for a in angles:
    x = 2 + (h * cos(a))
    y = 1 + (h * sin(a))
    plot_line(x,y)
    
plt.savefig("./Unstable(Q3)")