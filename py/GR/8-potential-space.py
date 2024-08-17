import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 1.989e30     # Mass of the black hole (Sun's mass), kg
r_s = 2 * G * M / (2.998e8)**2  # Schwarzschild radius, m

# Define the potential function in 2D
def V(x, y):
    r = np.sqrt(x**2 + y**2)
    return -G * M / (r_s * np.tanh(r))

# Define the range for x and y
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = V(X, Y)

# Create the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_title('Potential $V(x, y)$ in Hyperbolic Coordinates')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Potential $V(x, y)$')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5, label='Potential $V(x, y)$')

plt.show()