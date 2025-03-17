from math import floor
import matplotlib.pyplot as plt

plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Foward Euler")


def rdot(r,g):
    return r*(1-g)

def gdot(r,g):
    return g*(2-r)

max = 6
t = 0.1
nstep = floor(max/t)
t_total = [0]
r = [0.5]
g = [0.116]

for j in range(nstep):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t))

plt.plot(r,g,'orange',label = "t = 0.1")
print("R:",r[-1])
print("G:",g[-1])
print("t:",t_total[-1])

max = 6
t = 0.00548
nstep = floor(max/t)
t_total = [0]
r = [0.5]
g = [0.116]

for j in range(nstep):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t))

plt.plot(r,g,'red',label = "t = t0")
plt.legend()
plt.savefig("./Foward_Euler.png")

plt.clf()
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.plot(t_total,r,'red')
plt.ylabel("Red Squirrels (r)")
plt.xlabel("Time (t)")
plt.savefig("./R_Foward_Euler.png")

plt.clf()
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.plot(t_total,g,'grey')
plt.xlabel("Time (t)")
plt.ylabel("Grey Squirrels (g)")
plt.savefig("./G_Foward_Euler.png")

