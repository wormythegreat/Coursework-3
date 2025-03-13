from Question_2 import rdot,gdot
import matplotlib.pyplot as plt
import numpy as np
from math import floor

plt.clf()
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Unstable Manifold")

def plot_line(start_r,start_g):
    max = 6
    t = 0.1
    nstep = floor(max/t)
    t_total = [0]
    r = [start_r]   #make this the saddle point its self
    g = [start_g]
    j = 0

    while (abs(r[-1]) < 5) and (abs(g[-1] < 5)):
        r.append(r[j] + (t * rdot(r[j],g[j])))
        g.append(g[j] + (t * gdot(r[j],g[j])))
        t_total.append(float(t_total[j] + t))
        j = j + 1

    plt.plot(r,g,'orange')

plot_line(2.1,1.1)

plt.show()