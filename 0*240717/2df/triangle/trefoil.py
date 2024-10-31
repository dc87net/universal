import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the trefoil knot in parametric form
def trefoil_knot(t):
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    z = -np.sin(3 * t)
    return x, y, z

# Define rotation by π/4 in complex space
def rotate_by_pi_over_4(x, y, z):
    rotation_factor = 1 / np.sqrt(2)  # For π/4 rotation
    x_rotated = rotation_factor * (x - y) + 1j * rotation_factor * (x + y)
    y_rotated = rotation_factor * (z - 0) + 1j * rotation_factor * (z + 0)  # Imaginary part for z
    return x_rotated, y_rotated

# Generate the parametric values for t
t = np.linspace(0, 2 * np.pi, 500)
x, y, z = trefoil_knot(t)

# Rotate the trefoil knot in complex space
x_rotated, y_rotated = rotate_by_pi_over_4(x, y, z)

# Separate real and imaginary parts
x_real, x_imag = np.real(x_rotated), np.imag(x_rotated)
y_real, y_imag = np.real(y_rotated), np.imag(y_rotated)


# Find points where real and imaginary parts are equal
tolerance = 1e-5  # Adjust tolerance as needed
non_trivial_points = np.where((np.abs(x_real - x_imag) < tolerance) & (np.abs(y_real - y_imag) < tolerance))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the trefoil knot
ax.plot(x_real, y_real, z, color='blue', alpha=0.6, label='Trefoil Knot')

# Highlight the non-trivial zero points where Re = Im
ax.scatter(x_real[non_trivial_points], y_real[non_trivial_points], z[non_trivial_points], color='red', s=20, label='Non-Trivial Zeros')

# Add labels
ax.set_xlabel("$x$ (Position)")
ax.set_ylabel("$i$ (Imaginary/Phase)")
ax.set_zlabel("$z$ (Height)")

# Show the plot
ax.legend()
plt.show()
