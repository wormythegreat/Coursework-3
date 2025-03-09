import matplotlib.pyplot as plt
import numpy as np

R = np.linspace(0, 1.3, 30)
G = np.linspace(0, 0.8, 30)
r, g = np.meshgrid(R,G)
F = r * (1 - r - g)
H = g * (2 - r - (3 * g))
fig, ax = plt.subplots()
ax.quiver(r, g, F, H)
plt.xlabel("Red Squirrels (r)")
plt.ylabel("Grey Squirrels (g)")
plt.title("Quiver Plot of r and g")
plt.savefig("./Quiver.png")