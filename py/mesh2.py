import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parameters for the wave function and potential
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

# Spacetime curvature visualization
fig = plt.figure(figsize=(14, 8))

# Plot the potential well in 3D
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, T, V_X, cmap=cm.viridis, edgecolor='none')
ax1.set_title('Potential Well using Hyperbolic Tangent Function')
ax1.set_xlabel('Space (x)')
ax1.set_ylabel('Time (t)')
ax1.set_zlabel('Potential V(x)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
ax1.view_init(elev=30, azim=45)  # Isometric view

# Plot the combined wave function in 3D
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, T, real_part, cmap=cm.viridis, alpha=0.7, label='Real Part')
surf3 = ax2.plot_surface(X, T, imag_part.imag, cmap=cm.plasma, alpha=0.7, label='Imaginary Part')
ax2.set_title('Wave Function in Spacetime')
ax2.set_xlabel('Space (x)')
ax2.set_ylabel('Time (t)')
ax2.set_zlabel('Amplitude')
ax2.view_init(elev=30, azim=45)  # Isometric view

plt.show()