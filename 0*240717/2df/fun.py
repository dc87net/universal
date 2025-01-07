import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for analytic continuation and rotation of y = x^2 - 2x + 1
r = np.linspace(0.5, 1.5, 100)  # Radius range to simulate different values of |z|
theta = np.linspace(0, 2 * np.pi, 100)  # Angle in radians

# Create a meshgrid for polar coordinates
R, Theta = np.meshgrid(r, theta)

# Convert polar to complex form: z = R * e^(i * Theta)
Z = R * np.exp(1j * Theta)

# Calculate y = z^2 - 2z + 1 in the complex plane
Y_complex = Z**2 - 2*Z + 1

# Rotate by e^(i * pi / 4)
rotation_factor = np.exp(1j * np.pi / 4)
Y_rotated = Y_complex * rotation_factor

# Extract real and imaginary components
Y_rotated_real = np.real(Y_rotated)
Y_rotated_imag = np.imag(Y_rotated)

# Calculate sum, difference, product, and magnitude of the real and imaginary parts
sum_values = Y_rotated_real + Y_rotated_imag
difference_values = Y_rotated_real - Y_rotated_imag
product_values = Y_rotated_real * Y_rotated_imag
magnitude_values = np.sqrt(Y_rotated_real**2 + Y_rotated_imag**2)

# Create 2x2 grid for 3D plots
fig = plt.figure(figsize=(16, 12))

# Sum of Real and Imaginary parts
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(R * np.cos(Theta), R * np.sin(Theta), sum_values, cmap="viridis")
ax1.set_title("Sum of Real and Imaginary Parts")
ax1.set_xlabel("Real Axis (X)")
ax1.set_ylabel("Imaginary Axis (Y)")
ax1.set_zlabel("Sum")

# Difference of Real and Imaginary parts
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(R * np.cos(Theta), R * np.sin(Theta), difference_values, cmap="plasma")
ax2.set_title("Difference of Real and Imaginary Parts")
ax2.set_xlabel("Real Axis (X)")
ax2.set_ylabel("Imaginary Axis (Y)")
ax2.set_zlabel("Difference")

# Product of Real and Imaginary parts
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(R * np.cos(Theta), R * np.sin(Theta), product_values, cmap="inferno")
ax3.set_title("Product of Real and Imaginary Parts")
ax3.set_xlabel("Real Axis (X)")
ax3.set_ylabel("Imaginary Axis (Y)")
ax3.set_zlabel("Product")

# Magnitude of the complex values
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(R * np.cos(Theta), R * np.sin(Theta), magnitude_values, cmap="magma")
ax4.set_title("Magnitude of Rotated Function (sqrt(real^2 + imag^2))")
ax4.set_xlabel("Real Axis (X)")
ax4.set_ylabel("Imaginary Axis (Y)")
ax4.set_zlabel("Magnitude")

plt.suptitle("3D Visualizations of Sum, Difference, Product, and Magnitude of Rotated Function Components")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
