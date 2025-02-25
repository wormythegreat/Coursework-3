import matplotlib.pyplot as plt
import numpy as np

R = np.linspace(0.3, 0.7, 30)
G = np.linspace(0.3, 0.7, 30)
r, g = np.meshgrid(R,G)
F = r * (1 - r - g)
H = g * (2 - r - (3 * g))
fig, ax = plt.subplots()
ax.quiver(r, g, F, H)
plt.savefig("./Quiver.png")