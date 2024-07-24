import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define111111111111111111111111111w parameters
kx = 2 * np.pi  # Wavenumber
omega = 2 * np.pi  # Angular frequency
d = 1  # Dimensional count
c = 1  # Speed of light
G = 1  # Gravitational constant
mass = 1  # Mass of the object

# Spatial grid
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
x_grid, y_grid = np.meshgrid(x, y)

# Radial distance from the origin
r_grid = np.sqrt(x_grid**2 + y_grid**2)

# Example function for R(t)
R_t_example = np.exp(-r_grid**2)

# Generalized wave function
Psi_real = R_t_example * np.cos(kx * r_grid - omega * r_grid)
Psi_imag = R_t_example * (1j**d * np.sin(kx * r_grid - omega * r_grid)).real

# Magnitude squared of the wave function
Psi_magnitude_squared = np.abs(Psi_real + 1j * Psi_imag)**2

# Create the 3D surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the surface
ax.plot_surface(x_grid, y_grid, Psi_magnitude_squared, cmap='viridis')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Magnitude Squared')
ax.set_title('Magnitude Squared of the Generalized Wave Function in 3D')

plt.show()