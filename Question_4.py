#Question 4

import matplotlib.pyplot as plt
import numpy as np

#Set up plot
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Nullclines of r and g")

#Nullclines

#for r_dot = 0
#g=1-r

def null_r(r):
    g = 1 - r
    return g

#for g_dot = o
#r=2-3g

def null_g(g):
    r = 2 - (3 * g)
    return r

#Plotting nuclides with r as x-axis and g as y-axis

Nr = np.linspace(-2,2,500)
Ng = []
index = 0
for count in Nr:
    Ng.append(null_r(Nr[index]))
    index = index + 1

plt.plot(Nr,Ng,'r',label="R dot Nullcline")
plt.axvline(0,0,1,color="r")

Ng = np.linspace(-2,2,500)
Nr = []
index = 0
for count in Ng:
    Nr.append(null_g(Ng[index]))
    index = index + 1

plt.plot(Nr,Ng,'b',label="G dot Nullcline")
plt.axhline(0,0,1,color="b")

plt.plot(0.5,0.5,'gX',label="Equilibrium Points")
plt.plot(0,0,'gX')
plt.plot(0,2/3,'gX')
plt.plot(1,0,'gX')

plt.legend()
plt.savefig("./Nullclines.png")