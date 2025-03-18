from Question_2 import rdot,gdot
import matplotlib.pyplot as plt
import numpy as np
from math import floor,sin,cos,pi,sqrt

plt.clf()
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Unstable Manifold")

def plot_line(start_r,start_g,colour,time,tag):
    max = 6
    t = 0.001
    nstep = floor(max/t)
    t_total = [0]
    r = [start_r]   #make this the saddle point its self
    g = [start_g]
    j = 0

    if time  == "forward":
        while ((abs(r[-1] - 2) < 0.2) and (abs(g[-1] - 1 < 0.2))):
            r.append(r[j] + (t * rdot(r[j],g[j])))
            g.append(g[j] + (t * gdot(r[j],g[j])))
            t_total.append(float(t_total[j] + t))
            j = j + 1
    else:
        while ((abs(r[-1] - 2) < 0.2) and (abs(g[-1] - 1 < 0.2))):
            r.append(r[j] - (t * rdot(r[j],g[j])))
            g.append(g[j] - (t * gdot(r[j],g[j])))
            t_total.append(float(t_total[j] + t))
            j = j + 1
    
    if tag == "null":
        plt.plot(r,g,colour)
    else:
        plt.plot(r,g,colour, label=tag)


###################
#PLOT OF MANIFOLDS#
###################
plt.clf()

def plot_manifold(vx,vy,h,colour,time,tag):
    plot_line(2 + (h * vx),1 + (h * vy),colour,time,tag)
    plot_line(2 - (h * vx),1 - (h * vy),colour,time,"null")

plot_manifold(-sqrt(2),1,0.001,"red","forward","Unstable")
plot_manifold(sqrt(2),1,0.001,"blue","backwards","Stable")
plt.legend()
plt.title("Plot of Manifolds")
plt.savefig("./Manifolds.png")
