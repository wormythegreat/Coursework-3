import matplotlib.pyplot as plt
import numpy as np

#Set up plot and axes
plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Nullclines of r and g")

#Sets up the function for the sloped line when r_dot = 0
def null_r(r):
    g = 1 - r
    return g

#Sets up the function for the sloped line when g_dot = 0
def null_g(g):
    r = 2 - (3 * g)
    return r

#Plotting nuclides with r as x-axis and g as y-axis
Nr = np.linspace(-2,2,500) #Sets up an array of equally spacd values between -2 and 2
Ng = []
index = 0
for count in Nr: #For each Nr finds the corrosponding Ng and adds to an array
    Ng.append(null_r(Nr[index]))
    index = index + 1

#Plot r against g
plt.plot(Nr,Ng,'r',label="R dot Nullcline")
plt.axvline(0,0,1,color="r") #Also plots the vertical line r = 0 which is still a valid solution

Ng = np.linspace(-2,2,500) #Sets up an array of equally spacd values between -2 and 2
Nr = []
index = 0
for count in Ng: #For each Nr finds the corrosponding Ng and adds to an array
    Nr.append(null_g(Ng[index]))
    index = index + 1

#Plot r against g
plt.plot(Nr,Ng,'b',label="G dot Nullcline")
plt.axhline(0,0,1,color="b") #Also plots the horizontal line g = 0 which is still a valid solution

#Plots each of the equilibrium points on the graph
plt.plot(0.5,0.5,'gX',label="Equilibrium Points")
plt.plot(0,0,'gX')
plt.plot(0,2/3,'gX')
plt.plot(1,0,'gX')

#SOLUTIONS
#(0,0)
#(1/2,1/2)
#(0,2/3)
#(1,0)

plt.legend()
plt.savefig("./Nullclines.png") #Saves the figure as a .png