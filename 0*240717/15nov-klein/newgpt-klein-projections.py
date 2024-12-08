import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

# Constants for hydrogen-like orbitals
n, l, m = 3, 3, 3  # Principal quantum number, azimuthal quantum number, magnetic quantum number

# Define the spherical harmonics Y_l^m(θ, φ)
def spherical_harmonic(theta, phi, l, m):
    return sph_harm(m, l, phi, theta)

# Radial part R_nl(r) using a Cauchy distribution
def radial_part(r, n, l):
    # Using a Cauchy distribution as radial part
    gamma = n  # scale parameter
    x0 = 0     # location parameter
    return (r**l) / (1 + ((r - x0) / gamma)**2)

# Create a grid of angles
theta_vals = np.linspace(0, np.pi, 100)
phi_vals = np.linspace(0, 2 * np.pi, 100)
theta_grid, phi_grid = np.meshgrid(theta_vals, phi_vals)

# Calculate the spherical harmonic on the grid
Y_lm = spherical_harmonic(theta_grid, phi_grid, l, m)

# Radial part
r_vals = np.linspace(0, 20, 100)
R_nl = radial_part(r_vals, n, l)

# Create Cartesian coordinates for plotting
x_spherical = R_nl[:, None] * np.sin(theta_grid) * np.cos(phi_grid)
y_spherical = R_nl[:, None] * np.sin(theta_grid) * np.sin(phi_grid)
z_spherical = R_nl[:, None] * np.cos(theta_grid)

# Static projection in XY, XZ, YZ planes with adjusted axes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

im1 = axs[0].contourf(x_spherical, y_spherical, np.abs(Y_lm)**2)
axs[0].set_title('XY Projection')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].set_aspect('equal')
fig.colorbar(im1, ax=axs[0])

im2 = axs[1].contourf(x_spherical, z_spherical, np.abs(Y_lm)**2)
axs[1].set_title('XZ Projection')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')
axs[1].set_aspect('equal')
fig.colorbar(im2, ax=axs[1])

im3 = axs[2].contourf(y_spherical, z_spherical, np.abs(Y_lm)**2)
axs[2].set_title('YZ Projection')
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')
axs[2].set_aspect('equal')
fig.colorbar(im3, ax=axs[2])

plt.suptitle(f'Spherical Harmonics (n={n}, l={l}, m={m}) Projections with Cauchy Distribution')
plt.show()

# Plot in Spherical Coordinates
fig, ax = plt.subplots(figsize=(8, 6))
c = ax.contourf(theta_grid, phi_grid, np.abs(Y_lm)**2, levels=50)
ax.set_title('Spherical Coordinates (θ, φ)')
ax.set_xlabel('θ (theta)')
ax.set_ylabel('φ (phi)')
ax.set_aspect('equal')
fig.colorbar(c)
plt.show()

# Compute cylindrical coordinates
rho_cylindrical = np.sqrt(x_spherical**2 + y_spherical**2)
z_cylindrical = z_spherical

# Static projection in Cylindrical Coordinates
fig, ax = plt.subplots(figsize=(8, 6))
c = ax.contourf(rho_cylindrical, z_cylindrical, np.abs(Y_lm)**2, levels=50)
ax.set_title('Cylindrical Coordinates (ρ, z)')
ax.set_xlabel('ρ (rho)')
ax.set_ylabel('z')
ax.set_aspect('equal')
fig.colorbar(c)
plt.show()

# Ensure that the axes are scaled appropriately in all plots
# Already set 'ax.set_aspect('equal')' in the plotting code above

# Klein Bottle Parameters
u_vals = np.linspace(0, 2 * np.pi, 1000)
v_vals = np.linspace(0, 2 * np.pi, 1000)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)

# Klein Bottle Parametric Equations (Simplified for visualization)
x_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.cos(u_grid)
y_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.sin(u_grid)
z_klein = np.sin(u_grid / 2) * np.sin(v_grid) + np.cos(u_grid / 2) * np.sin(2 * v_grid)

# Static projection in XY, XZ, YZ planes with adjusted axes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

im1 = axs[0].contourf(x_klein, y_klein, np.abs(x_klein)**2 + np.abs(y_klein)**2)
axs[0].set_title('XY Projection')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].set_aspect('equal')
fig.colorbar(im1, ax=axs[0])

im2 = axs[1].contourf(x_klein, z_klein, np.abs(x_klein)**2 + np.abs(z_klein)**2)
axs[1].set_title('XZ Projection')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')
axs[1].set_aspect('equal')
fig.colorbar(im2, ax=axs[1])

im3 = axs[2].contourf(y_klein, z_klein, np.abs(y_klein)**2 + np.abs(z_klein)**2)
axs[2].set_title('YZ Projection')
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')
axs[2].set_aspect('equal')
fig.colorbar(im3, ax=axs[2])

plt.suptitle('Klein Bottle Projections')
plt.show()
