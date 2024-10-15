import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

# Constants for hydrogen-like orbitals
n, l, m = 2, 1, 0  # Principal quantum number, azimuthal quantum number, magnetic quantum number

# Define the spherical harmonics Y_l^m(θ, φ)
def spherical_harmonic(theta, phi, l, m):
    return sph_harm(m, l, phi, theta)

# Radial part R_nl(r) (assuming normalized for simplicity)
def radial_part(r, n, l):
    # For simplicity, using a Gaussian as a radial part, real hydrogenic wavefunctions are more complex
    return np.exp(-r / n) * (r**l)

# Create a grid of angles
theta_vals = np.linspace(0, np.pi, 100)
phi_vals = np.linspace(0, 2 * np.pi, 100)

# Calculate the spherical harmonic on the grid
theta_grid, phi_grid = np.meshgrid(theta_vals, phi_vals)
Y_lm = spherical_harmonic(theta_grid, phi_grid, l, m)

# Radial part
r_vals = np.linspace(0, 20, 100)
R_nl = radial_part(r_vals, n, l)

# Create Cartesian coordinates for plotting
x_spherical = R_nl[:, None] * np.sin(theta_grid) * np.cos(phi_grid)
y_spherical = R_nl[:, None] * np.sin(theta_grid) * np.sin(phi_grid)
z_spherical = R_nl[:, None] * np.cos(theta_grid)

# Static projection in XY, XZ, YZ planes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].contourf(x_spherical, y_spherical, np.abs(Y_lm)**2)
axs[0].set_title('XY Projection')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

axs[1].contourf(x_spherical, z_spherical, np.abs(Y_lm)**2)
axs[1].set_title('XZ Projection')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')

axs[2].contourf(y_spherical, z_spherical, np.abs(Y_lm)**2)
axs[2].set_title('YZ Projection')
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')

plt.suptitle(f'Spherical Harmonics (n={n}, l={l}, m={m}) Projections')
plt.show()


# Klein Bottle Parameters
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(0, 2 * np.pi, 100)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)

# Klein Bottle Parametric Equations (Simplified for visualization)
x_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.cos(u_grid)
y_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.sin(u_grid)
z_klein = np.sin(u_grid / 2) * np.sin(v_grid) + np.cos(u_grid / 2) * np.sin(2 * v_grid)

# Static projection in XY, XZ, YZ planes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].contourf(x_klein, y_klein, np.abs(x_klein)**2 + np.abs(y_klein)**2)
axs[0].set_title('XY Projection')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

axs[1].contourf(x_klein, z_klein, np.abs(x_klein)**2 + np.abs(z_klein)**2)
axs[1].set_title('XZ Projection')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')

axs[2].contourf(y_klein, z_klein, np.abs(y_klein)**2 + np.abs(z_klein)**2)
axs[2].set_title('YZ Projection')
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')

plt.suptitle('Klein Bottle Projections')
plt.show()
