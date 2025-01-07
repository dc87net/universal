import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for the Klein bottle surface
def klein_bottle(u, v):
    # Standard parameters for simplicity, modify as desired
    a, b, c = 2, 0.5, 1.5
    x = (a + b * np.cos(u)) * np.cos(v)
    y = (a + b * np.cos(u)) * np.sin(v)
    z = b * np.sin(u) + c * np.cos(v / 2)
    return x, y, z

# Define rotation by π/4
def rotate_by_pi_over_4(x, y, z):
    rotation_factor = 1 / np.sqrt(2)  # For π/4 rotation
    x_rotated = rotation_factor * (x - y) + 1j * rotation_factor * (x + y)
    y_rotated = rotation_factor * (z - 0) + 1j * rotation_factor * (z + 0)  # Modify as needed for 4D
    return x_rotated, y_rotated

# Generate mesh grid
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, 2 * np.pi, 50)
u, v = np.meshgrid(u, v)
x, y, z = klein_bottle(u, v)

# Rotate Klein bottle in complex space
x_rotated, y_rotated = rotate_by_pi_over_4(x, y, z)

# Real and imaginary parts after rotation
x_real, x_imag = np.real(x_rotated), np.imag(x_rotated)
y_real, y_imag = np.real(y_rotated), np.imag(y_rotated)

# Find points where real and imaginary parts are equal
tolerance = 1e-5  # Adjust tolerance as needed
non_trivial_points = np.where((np.abs(x_real - x_imag) < tolerance) & (np.abs(y_real - y_imag) < tolerance))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the basic Klein bottle structure
ax.plot_surface(x, y, z, color='cyan', alpha=0.6, edgecolor='none')

# Highlight non-trivial zero points
ax.scatter(x[non_trivial_points], y[non_trivial_points], z[non_trivial_points], color='red', s=20, label='Non-Trivial Zeros')

# Customize plot
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the basic Klein bottle structure
ax.plot_surface(x, y, z, color='cyan', alpha=0.6, edgecolor='none')

# Highlight non-trivial zero points
ax.scatter(x[non_trivial_points], y[non_trivial_points], z[non_trivial_points], color='red', s=20, label='Non-Trivial Zeros')

# Add meaningful labels
ax.set_xlabel("$x$ (Position)")
ax.set_ylabel("$i$ (Imaginary/Phase)")
ax.set_zlabel("$t$ (Time)")

# Customize plot
ax.legend()
plt.show()
