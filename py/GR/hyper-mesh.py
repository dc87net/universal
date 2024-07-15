import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the wave function
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

# Create a figure for overlaying real and imaginary parts on different planes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the real part on the xy-plane
ax.plot_surface(X, T, real_part, cmap='viridis', alpha=0.7, label='Real Part')

# Plot the imaginary part on the xz-plane
ax.plot_surface(X, imag_part.imag, T, cmap='plasma', alpha=0.7, label='Imaginary Part')

ax.set_title('Overlay of Real and Imaginary Parts in Spacetime')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Amplitude')
ax.view_init(elev=30, azim=45)  # Isometric view

plt.show()
