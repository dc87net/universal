import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
kx = 2 * np.pi  # Wavenumber        ##TODO: Let's discuss why you chose these--2pi=zero degress=0rad (Perhaps)? -- user input would be good
                                            ##TODO: where the user can also type `p` for pi, rNN[.NN] for sqrt
omega = 2 * np.pi  # Angular frequency
d = 2  # Dimensional count          ##TODO: Justify: 3 (or 4--likely 3), but not 1
c = 1  # Speed of light             ##TODO: c in normalized units (correct as is--should be)?
G = 1  # Gravitational constant     ##TODO: this should be G expressed in the normalized units
mass = 1  # Mass of the object      ##TODO: The mass should be >=1 solar masses; calc based on input prompt.

# Spatial grid
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
z = np.linspace(-10, 10, 500)


x_grid, y_grid, z_grid = np.meshgrid(x, y, z)

# Radial distance from the origin
r_grid = np.sqrt(x_grid**2 + y_grid**2 +z_grid**2)

# Example function for R(t)
R_t_example = np.exp(-r_grid**2)   ##TODO: Jusitfy

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


##TODO: We should consider having a gui interface, perhaps with two (or more) sliders, and a "regenerate" button
##TODO: We should save the data to an exportable format (table, or similar human-readable(and machine-readable) format).