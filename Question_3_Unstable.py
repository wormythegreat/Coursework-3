import matplotlib.pyplot as plt
import numpy as np
from math import floor

def rdot(r,g):
    return r*(1-g)

def gdot(r,g):
    return g*(2-r)

plt.clf()
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Unstable Manifold")

max = 6
t = 0.1
nstep = floor(max/t)
t_total = [0]
r = [2.1]   #make this the saddle point its self
g = [1.1]
j=0

""" for j in range(nstep):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t)) """

while (abs(r[-1]) < 5) and (abs(g[-1] < 5)):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t))
    j = j + 1

plt.plot(r,g,'orange')
plt.show()