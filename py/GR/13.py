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

# Define the range for r and theta
r = np.linspace(r_s, 10 * r_s, 100)
theta = np.linspace(0, np.pi, 50)

# Create a mesh grid in spherical coordinates
R, Theta = np.meshgrid(r, theta)

# Fix phi to get a 2D cross-section
phi = 0

# Convert spherical coordinates to Cartesian coordinates
X = R * np.sin(Theta) * np.cos(phi)
Y = R * np.sin(Theta) * np.sin(phi)
Z = R * np.cos(Theta)

# Hyperbolic transformation for Kerr metric (simplified representation)
# Radial distortion factor
epsilon = 1e-6  # Small constant to avoid division by zero
radial_distortion = 1 / np.sqrt(np.maximum(1 - (r_s / R) * (1 - a**2 * np.cos(Theta)**2), epsilon))

# Apply the radial distortion
X_distorted = X * radial_distortion
Y_distorted = Y * radial_distortion
Z_distorted = Z * radial_distortion

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the distorted mesh grid
ax.plot_wireframe(X_distorted, Y_distorted, Z_distorted, color='cyan', alpha=0.5)
ax.set_title('3D Visualization of Spacetime Curvature around a Rotating Black Hole (Snapshot in Time)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-10 * r_s, 10 * r_s)
ax.set_ylim(-10 * r_s, 10 * r_s)
ax.set_zlim(-10 * r_s, 10 * r_s)

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Constants
# G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
# c = 2.998e8      # Speed of light, m/s
# M_sun = 1.989e30 # Solar mass, kg
#
# # Black hole parameters
# M = 4e6 * M_sun  # Mass of the black hole in kg
# a = 0.9          # Dimensionless spin parameter (0 < a < 1)
#
# # Define the Schwarzschild radius
# r_s = 2 * G * M / c**2  # Schwarzschild radius in meters
#
# # Define the range for r, theta, and phi
# r = np.linspace(r_s, 10 * r_s, 100)
# theta = np.linspace(0, np.pi, 50)
# phi = np.linspace(0, 2 * np.pi, 50)
#
# # Create a mesh grid in spherical coordinates
# R, Theta, Phi = np.meshgrid(r, theta, phi)
#
# # Convert spherical coordinates to Cartesian coordinates
# X = R * np.sin(Theta) * np.cos(Phi)
# Y = R * np.sin(Theta) * np.sin(Phi)
# Z = R * np.cos(Theta)
#
# # Hyperbolic transformation for Kerr metric (simplified representation)
# # Radial distortion factor
# epsilon = 1e-6  # Small constant to avoid division by zero
# radial_distortion = 1 / np.sqrt(np.maximum(1 - (r_s / R) * (1 - a**2 * np.cos(Theta)**2), epsilon))
#
# # Apply the radial distortion
# X_distorted = X * radial_distortion
# Y_distorted = Y * radial_distortion
# Z_distorted = Z * radial_distortion
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot the distorted mesh grid
# ax.plot_wireframe(X_distorted, Y_distorted, Z_distorted, color='cyan', alpha=0.5)
# ax.set_title('3D Visualization of Spacetime Curvature around a Rotating Black Hole (Snapshot in Time)')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_xlim(-10 * r_s, 10 * r_s)
# ax.set_ylim(-10 * r_s, 10 * r_s)
# ax.set_zlim(-10 * r_s, 10 * r_s)
#
# plt.show()