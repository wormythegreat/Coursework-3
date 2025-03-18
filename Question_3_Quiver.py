import matplotlib.pyplot as plt
import numpy as np

#Sets up equally spaced points to draw the quiver arrows from
R = np.linspace(0, 3, 30)
G = np.linspace(0, 2, 30)
r, g = np.meshgrid(R,G)
#These are the differential equations
F = r * (1 - g)
H = g * (2 - r)
fig, ax = plt.subplots()
ax.quiver(r, g, F, H)
#Axes, axes titles and plot titles
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.axhline(0,0,1,color="blue")
plt.axvline(0,0,1,color="blue")
plt.title("Quiver Plot of r and g")
plt.savefig("./Quiver(Q2).png")