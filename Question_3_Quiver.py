import matplotlib.pyplot as plt
import numpy as np

R = np.linspace(0, 3, 30)
G = np.linspace(0, 2, 30)
r, g = np.meshgrid(R,G)
F = r * (1 - g)
H = g * (2 - r)
fig, ax = plt.subplots()
ax.quiver(r, g, F, H)
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("(Q3) Quiver Plot of r and g")
plt.savefig("./Quiver(Q4).png")