from math import floor
import matplotlib.pyplot as plt

#This sets some axes, axes titles and the graph title
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Foward Euler")

#Sets up the differential equations
#These are also used in later scripts and can be imported from this file
def rdot(r,g):
    return r*(1-g)

def gdot(r,g):
    return g*(2-r)

#Set up starting constraints
max = 6 #maximum time to go upto
t = 0.1 #The time-step starting with 0.1
nstep = floor(max/t) #How many steps are requuired to reach the max t
t_total = [0] #Sets up the list for the total time
r = [0.5] #Sets up the list for r
g = [0.116] # --  ~ -- for g

#For the number of steps required it will loop through using foward euler and add to the end of each list
for j in range(nstep):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t))

#Can then plot this r and g in orange
plt.plot(r,g,'orange',label = "t = 0.1")

#Set up new starting constraints
max = 6 #Same max t
t = 0.00548 #This is the t0 worded out in Q2
nstep = floor(max/t) #The new number of steps is worked out
t_total = [0] #Sets up the list for the total time
r = [0.5] #Sets up the list for r
g = [0.116] # --  ~ -- for g

#For the number of steps required it will loop through using foward euler and add to the end of each list
for j in range(nstep):
    r.append(r[j] + (t * rdot(r[j],g[j])))
    g.append(g[j] + (t * gdot(r[j],g[j])))
    t_total.append(float(t_total[j] + t))

#Plot the new list of r and g in red
plt.plot(r,g,'red',label = "t = t0")
plt.legend()
plt.savefig("./Foward_Euler.png")