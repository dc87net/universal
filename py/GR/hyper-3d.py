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

# Plot the potential well in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, V_X, cmap='viridis')
ax.set_title('3D Potential Well using Hyperbolic Tangent Function')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Potential V(x)')
plt.show()

# Plot the real part of the wave function in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, real_part, cmap='viridis')
ax.set_title('3D Real Part of the Wave Function')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Real Part of Wave Function')
plt.show()

# Plot the imaginary part of the wave function in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, imag_part.imag, cmap='viridis')
ax.set_title('3D Imaginary Part of the Wave Function')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Imaginary Part of Wave Function')
plt.show()

# Plot the combined wave function in 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, wave_function.real, cmap='viridis')
ax.set_title('3D Combined Wave Function')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Wave Function')
plt.show()
