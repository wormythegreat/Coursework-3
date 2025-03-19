from Question_2 import rdot,gdot
import matplotlib.pyplot as plt
import numpy as np
from math import floor,sin,cos,pi,sqrt

#Sets up the axis and titles
plt.clf()
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")

#Defines the main function that will plot the path of the populations fowards and backwards in time from a particlar starting point
#By calling this function multiple times, multiple paths can be drawn on the plot
def plot_line(start_r,start_g,colour,time,tag):
    #Set up start conditions
    t = 0.001 #Time-step
    t_total = [0] #Time starts at 0
    r = [start_r] #Start coords
    g = [start_g]
    j = 0 #A counter for indexing

    if time  == "forward": #For moving forward in time so foward euler
        while ((abs(r[-1] - 2) < 0.2) and (abs(g[-1] - 1 < 0.2))): #Will run until the point has moved a distance of 0.2 away from the saddle
            r.append(r[j] + (t * rdot(r[j],g[j])))
            g.append(g[j] + (t * gdot(r[j],g[j])))
            t_total.append(float(t_total[j] + t))
            j = j + 1
    else: #For moving backwards in time so backwards euler
        while ((abs(r[-1] - 2) < 0.2) and (abs(g[-1] - 1 < 0.2))): #Will run until the point has moved a distance of 0.2 away from the saddle
            r.append(r[j] - (t * rdot(r[j],g[j])))
            g.append(g[j] - (t * gdot(r[j],g[j])))
            t_total.append(float(t_total[j] + t))
            j = j + 1
    
    if tag == "null": #Doesnt add a label for that line otherwise there will be duplicate labels in the legend for the same colour
        plt.plot(r,g,colour)
    else: #Plots the line with a label
        plt.plot(r,g,colour, label=tag)



#Plot of manifolds

#Defines a function to plot 2 lines on opposite sides of the saddle according the vector passed in and either foward or backwards in time
def plot_manifold(vx,vy,h,colour,time,tag):
    plot_line(2 + (h * vx),1 + (h * vy),colour,time,tag)
    plot_line(2 - (h * vx),1 - (h * vy),colour,time,"null")

#Plots the lines using the function
plot_manifold(-sqrt(2),1,0.001,"red","forward","Unstable")
plot_manifold(sqrt(2),1,0.001,"blue","backwards","Stable")

plt.legend()
plt.title("Plot of Manifolds")
plt.savefig("./Manifolds.png") #Saves the plot as a .png
