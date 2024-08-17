import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 2.998e8      # Speed of light, m/s
M_sun = 1.989e30 # Solar mass, kg

# Black hole parameters
M = 5.5 * M_sun  # Mass of the black hole in kg
a = 0.9          # Dimensionless spin parameter (0 < a < 1)

# Define the Schwarzschild radius
r_s = 2 * G * M / c**2  # Schwarzschild radius in meters

# Define the range for the light source and grid for calculation
theta = np.linspace(0, 2 * np.pi, 1000)
r_source = 20 * r_s  # Distance of the light source from the black hole

# Position of the light source in Cartesian coordinates
x_source = r_source * np.cos(theta)
y_source = r_source * np.sin(theta)

# Define the hyperbolic transformation function
def hyperbolic_transformation(r):
    return r_s * np.tanh(r / r_s)

# Apply the hyperbolic transformation to simulate the lensing effect
def lensing_effect(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    r_transformed = hyperbolic_transformation(r)
    x_lensed = r_transformed * np.cos(theta)
    y_lensed = r_transformed * np.sin(theta)
    return x_lensed, y_lensed

# Calculate the lensed positions of the light source
x_lensed, y_lensed = lensing_effect(x_source, y_source)

# Plot the original and lensed positions
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the original position of the light source
ax.plot(x_source, y_source, 'b.', markersize=0.5, alpha=0.5, label='Original Light Source')

# Plot the lensed position of the light source
ax.plot(x_lensed, y_lensed, 'r.', markersize=0.5, alpha=0.5, label='Lensed Light Source')

# Highlight the black hole region
circle = plt.Circle((0, 0), r_s, color='black', alpha=0.7)
ax.add_artist(circle)

# Set plot limits and labels
ax.set_xlim(-30 * r_s, 30 * r_s)
ax.set_ylim(-30 * r_s, 30 * r_s)
ax.set_aspect('equal')
ax.set_title('Gravitational Lensing by a Rotating Black Hole with Hyperbolic Spacetime Curvature')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.legend()

plt.show()
