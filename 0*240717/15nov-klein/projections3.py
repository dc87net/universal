import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Rotation function
def rotate_parameters(u, v):
    theta = np.pi / 4
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    u_rotated = cos_theta * u - sin_theta * v
    v_rotated = sin_theta * u + cos_theta * v
    return u_rotated, v_rotated


# Define the parametric equations for the rotated Klein bottle
def klein_bottle_rotated(u, v):
    # Apply rotation by π/4
    u_rot, v_rot = rotate_parameters(u, v)

    # Parametric equations with rotated parameters
    x = (2 + np.cos(u_rot)) * np.cos(v_rot)
    y = (2 + np.cos(u_rot)) * np.sin(v_rot)
    z = np.sin(u_rot)
    return x, y, z


# Generate a mesh grid for the parameters
u_vals = np.linspace(0, 2 * np.pi, 200)
v_vals = np.linspace(0, 2 * np.pi, 200)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)

# Compute the rotated Klein bottle surface
x_surface, y_surface, z_surface = klein_bottle_rotated(u_grid, v_grid)

# Visualization
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the rotated Klein bottle surface
ax.plot_surface(x_surface, y_surface, z_surface, color='cyan', alpha=0.7, rstride=5, cstride=5, edgecolor='none')

# Ensure axes are equally scaled
max_range = np.array([x_surface.max() - x_surface.min(), y_surface.max() - y_surface.min(),
                      z_surface.max() - z_surface.min()]).max() / 2.0
mean_x = (x_surface.max() + x_surface.min()) / 2.0
mean_y = (y_surface.max() + y_surface.min()) / 2.0
mean_z = (z_surface.max() + z_surface.min()) / 2.0
ax.set_xlim(mean_x - max_range, mean_x + max_range)
ax.set_ylim(mean_y - max_range, mean_y + max_range)
ax.set_zlim(mean_z - max_range, mean_z + max_range)

# Labels and title
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_title('Rotated Klein Bottle (Rotation by π/4)')

# Show the plot
plt.show()
