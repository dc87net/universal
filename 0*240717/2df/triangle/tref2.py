import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the trefoil knot in 5D parametric form
def trefoil_knot_5D(t):
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    z = -np.sin(3 * t)
    w = np.sin(4 * t)  # New real dimension
    v = np.cos(5 * t)  # New imaginary dimension
    return x, y, z, w, v

# Define rotation by π/4 in complex space across multiple dimensions
def rotate_by_pi_over_4_5D(x, y, z, w, v):
    rotation_factor = 1 / np.sqrt(2)  # For π/4 rotation
    x_rotated = rotation_factor * (x - y) + 1j * rotation_factor * (x + y)
    y_rotated = rotation_factor * (z - w) + 1j * rotation_factor * (z + w)
    z_rotated = rotation_factor * (v - 0) + 1j * rotation_factor * (v + 0)  # Rotating in v
    return x_rotated, y_rotated, z_rotated

# Generate the parametric values for t
t = np.linspace(0, 2 * np.pi, 500)
x, y, z, w, v = trefoil_knot_5D(t)

# Rotate the trefoil knot in complex space (5D)
x_rotated, y_rotated, z_rotated = rotate_by_pi_over_4_5D(x, y, z, w, v)

# Separate real and imaginary parts
x_real, x_imag = np.real(x_rotated), np.imag(x_rotated)
y_real, y_imag = np.real(y_rotated), np.imag(y_rotated)
z_real, z_imag = np.real(z_rotated), np.imag(z_rotated)

# Find points where real and imaginary parts are equal
tolerance = 0.5  # Adjust tolerance as needed
non_trivial_points = np.where((np.abs(x_real - x_imag) < tolerance) & (np.abs(y_real - y_imag) < tolerance) & (np.abs(z_real - z_imag) < tolerance))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the real part of the trefoil knot
ax.plot(x_real, y_real, z_real, color='blue', alpha=0.6, label='Trefoil Knot')

# Highlight the non-trivial zero points where Re = Im
ax.scatter(x_real[non_trivial_points], y_real[non_trivial_points], z_real[non_trivial_points], color='red', s=20, label='Non-Trivial Zeros')

# Add labels
ax.set_xlabel("$x$ (Real Part)")
ax.set_ylabel("$i$ (Imaginary Part)")
ax.set_zlabel("$z$ (Height)")

# Show the plot
ax.legend()
plt.show()
