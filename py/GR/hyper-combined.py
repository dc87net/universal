import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the potential well and wave function
V0 = 1.0  # Depth of the potential well
k = 1.0   # Determines the width of the well
omega = 1.0  # Angular frequency
d = 1  # Dimensional factor (integer)
t = np.linspace(0, 10, 400)  # Time
x = np.linspace(-5, 5, 400)  # Space

# Create meshgrid for 3D plotting
X, T = np.meshgrid(x, t)

# Potential well using hyperbolic tangent function
V_X = -V0 * np.tanh(k * X)**2

# Wave function components
real_part = np.cos(k * X - omega * T)
imag_part = (1j ** d) * np.sin(k * X - omega * T)
wave_function = real_part + imag_part

# Create a figure with subplots
fig = plt.figure(figsize=(20, 12))

# Plot the potential well in 3D
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, T, V_X, cmap='viridis')
ax1.set_title('Potential Well using Hyperbolic Tangent Function')
ax1.set_xlabel('Space (x)')
ax1.set_ylabel('Time (t)')
ax1.set_zlabel('Potential V(x)')
ax1.view_init(elev=30, azim=45)  # Isometric view

# Plot the real part of the wave function in 3D
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, T, real_part, cmap='viridis')
ax2.set_title('Real Part of the Wave Function')
ax2.set_xlabel('Space (x)')
ax2.set_ylabel('Time (t)')
ax2.set_zlabel('Real Part of Wave Function')
ax2.view_init(elev=30, azim=45)  # Isometric view

# Plot the imaginary part of the wave function in 3D
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, T, imag_part.imag, cmap='viridis')
ax3.set_title('Imaginary Part of the Wave Function')
ax3.set_xlabel('Space (x)')
ax3.set_ylabel('Time (t)')
ax3.set_zlabel('Imaginary Part of Wave Function')
ax3.view_init(elev=30, azim=45)  # Isometric view

# Plot the combined wave function in 3D
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, T, wave_function.real, cmap='viridis')
ax4.set_title('Combined Wave Function (Real Part)')
ax4.set_xlabel('Space (x)')
ax4.set_ylabel('Time (t)')
ax4.set_zlabel('Wave Function')
ax4.view_init(elev=30, azim=45)  # Isometric view

# Overlay the real and imaginary parts in 3D
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, T, real_part, cmap='viridis', alpha=0.7, label='Real Part')
ax5.plot_surface(X, T, imag_part.imag, cmap='plasma', alpha=0.7, label='Imaginary Part')
ax5.set_title('Overlay of Real and Imaginary Parts')
ax5.set_xlabel('Space (x)')
ax5.set_ylabel('Time (t)')
ax5.set_zlabel('Amplitude')
ax5.view_init(elev=30, azim=45)  # Isometric view

plt.tight_layout()
plt.show()
