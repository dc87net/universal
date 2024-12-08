#!/usr/bin/env python3
## Klein Bottle
## 15 Nov 2024

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parametric equations for the Klein bottle
def klein_bottle(u, v):
    """
    Parametric equations for the Klein bottle.

    Parameters:
    u, v : array-like
        Parameters ranging from 0 to 2π.

    Returns:
    x, y, z : array-like
        Cartesian coordinates of the Klein bottle surface.
    """
    # Standard parametric equations for the Klein bottle
    x = (2 + np.cos(u)) * np.cos(v)
    y = (2 + np.cos(u)) * np.sin(v)
    z = np.sin(u)
    return x, y, z

# Define the critical trace on the Klein bottle
def critical_trace(t):
    """
    Defines a critical trace on the Klein bottle surface.

    Parameters:
    t : array-like
        Parameter ranging from 0 to 2π.

    Returns:
    x, y, z : array-like
        Cartesian coordinates of the critical trace.
    """
    # The critical trace is defined by specific functions of t
    u = np.pi + np.sin(t)      # Adjusted to create a meaningful path
    v = np.cos(t)
    return klein_bottle(u, v)

# Generate a mesh grid for the Klein bottle surface
u_vals = np.linspace(0, 2 * np.pi, 200)
v_vals = np.linspace(0, 2 * np.pi, 200)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)
x_surface, y_surface, z_surface = klein_bottle(u_grid, v_grid)

# Compute the critical trace
t_values = np.linspace(0, 2 * np.pi, 500)
x_trace, y_trace, z_trace = critical_trace(t_values)

# Visualization
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Plot the Klein bottle surface
ax.plot_surface(x_surface, y_surface, z_surface, color='cyan', alpha=0.7, rstride=5, cstride=5, edgecolor='none')

# Plot the critical trace
ax.plot(x_trace, y_trace, z_trace, color='red', linewidth=3, label='Critical Trace')

# Ensure axes are equally scaled
max_range = np.array([x_surface.max() - x_surface.min(), y_surface.max() - y_surface.min(), z_surface.max() - z_surface.min()]).max() / 2.0
mean_x = (x_surface.max() + x_surface.min()) / 2.0
mean_y = (y_surface.max() + y_surface.min()) / 2.0
mean_z = (z_surface.max() + z_surface.min()) / 2.0
ax.set_xlim(mean_x - max_range, mean_x + max_range)
ax.set_ylim(mean_y - max_range, mean_y + max_range)
ax.set_zlim(mean_z - max_range, mean_z + max_range)

# Labels and title
ax.set_xlabel('$x$ (Position)')
ax.set_ylabel('$y$ (Position)')
ax.set_zlabel('$z$ (Position)')
ax.set_title('Klein Bottle with Critical Trace')

# Add legend
ax.legend()

# Show the plot
plt.show()
