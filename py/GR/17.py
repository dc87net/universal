import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 2.998e8      # Speed of light, m/s
M_sun = 1.989e30 # Solar mass, kg

# Black hole parameters (smallest stellar-mass black hole plus 10%)
M = 5.5 * M_sun  # Mass of the black hole in kg
a = 0.9          # Dimensionless spin parameter (0 < a < 1)

# Define the Schwarzschild radius
r_s = 2 * G * M / c**2  # Schwarzschild radius in meters

# Define the ranges for r, theta, and phi
r = np.linspace(r_s * 1.01, 10 * r_s, 100)  # Focus on a region to better visualize changes
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

# Create a mesh grid in spherical coordinates
R, Theta, Phi = np.meshgrid(r, theta, phi)

# Hyperbolic transformation
def hyperbolic_transformation(r):
    return r_s * np.tanh(r / r_s)

# Apply the hyperbolic transformation
R_transformed = hyperbolic_transformation(R)

# Calculate the rate of change for false color mapping
rate_of_change = np.abs(np.gradient(R_transformed, axis=0))

# Convert spherical coordinates to Cartesian coordinates for both surfaces
X = R_transformed * np.sin(Theta) * np.cos(Phi)
Y = R_transformed * np.sin(Theta) * np.sin(Phi)
Z = R_transformed * np.cos(Theta)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the hyperbolically transformed mesh grid with false color
norm = plt.Normalize(vmin=rate_of_change.min(), vmax=rate_of_change.max())
colors = plt.cm.viridis(norm(rate_of_change))

# We need to plot the surface for each Phi slice to ensure the array dimensions are correct
for i in range(Phi.shape[2]):
    ax.plot_surface(X[:, :, i], Y[:, :, i], Z[:, :, i], facecolors=colors[:, :, i], alpha=0.7, rstride=1, cstride=1, edgecolor='none')

# Set the aspect ratio to be equal
ax.set_box_aspect([1,1,1])

# Add color bar for the rate of change
mappable = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=norm)
plt.colorbar(mappable, ax=ax, label='Rate of Change')

# Add labels and title
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('3D Visualization of Hyperbolic Spacetime Curvature around a Rotating Black Hole with False Color Mapping')

plt.show()