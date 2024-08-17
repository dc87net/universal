import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 2.998e8      # Speed of light, m/s
M_sun = 1.989e30 # Solar mass, kg

# Black hole parameters
M = 4e6 * M_sun  # Mass of the black hole in kg
a = 0.9          # Dimensionless spin parameter (0 < a < 1)

# Define the Schwarzschild radius
r_s = 2 * G * M / c**2  # Schwarzschild radius in meters

# Define the ranges for theta and phi
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
Theta, Phi = np.meshgrid(theta, phi)

# Calculate the event horizon and ergosphere radii
r_plus = r_s * (1 + np.sqrt(1 - a**2))  # Outer event horizon
r_ergosphere = r_s * (1 + np.sqrt(1 - (a * np.cos(Theta))**2))  # Ergosphere

# Convert spherical coordinates to Cartesian coordinates for both surfaces
X_horizon = r_plus * np.sin(Theta) * np.cos(Phi)
Y_horizon = r_plus * np.sin(Theta) * np.sin(Phi)
Z_horizon = r_plus * np.cos(Theta)

X_ergosphere = r_ergosphere * np.sin(Theta) * np.cos(Phi)
Y_ergosphere = r_ergosphere * np.sin(Theta) * np.sin(Phi)
Z_ergosphere = r_ergosphere * np.cos(Theta)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the event horizon
ax.plot_surface(X_horizon, Y_horizon, Z_horizon, color='black', alpha=0.7, edgecolor='none')

# Plot the ergosphere
ax.plot_surface(X_ergosphere, Y_ergosphere, Z_ergosphere, color='blue', alpha=0.3, edgecolor='none')

# Set the aspect ratio to be equal
ax.set_box_aspect([1,1,1])

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of a Rotating Black Hole (Kerr Black Hole)')

plt.show()