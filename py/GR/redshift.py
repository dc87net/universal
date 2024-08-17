import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
r_s = 2 * G * M / (2.998e8)**2  # Schwarzschild radius, m

# Define a grid for r and theta
r = np.linspace(r_s, 10 * r_s, 500)
theta = np.linspace(0, 2 * np.pi, 500)
R, Theta = np.meshgrid(r, theta)

# Hyperbolic Tangent Model Potential
def potential_hyperbolic(r, r_s, G, M):
    x = r / r_s
    return -G * M / (r_s * np.tanh(x))

# Traditional Kerr Model Potential (simplified)
def potential_kerr(r, G, M):
    return -G * M / r

# Calculate the potentials
V_hyperbolic = potential_hyperbolic(R, r_s, G, M)
V_kerr = potential_kerr(R, G, M)

# Calculate the gradients
def gradient_field(V, dr, dtheta):
    grad_r = np.gradient(V, dr, axis=0)
    grad_theta = np.gradient(V, dtheta, axis=1)
    return grad_r, grad_theta

# Radial and angular step sizes
dr = r[1] - r[0]
dtheta = theta[1] - theta[0]

# Gradient fields for both models
grad_r_hyperbolic, grad_theta_hyperbolic = gradient_field(V_hyperbolic, dr, dtheta)
grad_r_kerr, grad_theta_kerr = gradient_field(V_kerr, dr, dtheta)

# Plot all visualizations in a 3x3 grid
fig, axes = plt.subplots(3, 3, figsize=(18, 18))

# Hyperbolic Tangent Model Potential
ax = fig.add_subplot(3, 3, 1, projection='3d')
ax.plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_hyperbolic, cmap='viridis')
ax.set_title('Hyperbolic Tangent Model Potential')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')

# Traditional Kerr Model Potential
ax = fig.add_subplot(3, 3, 2, projection='3d')
ax.plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_kerr, cmap='viridis')
ax.set_title('Traditional Kerr Model Potential')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')

# Placeholder for combined plot if needed
ax = fig.add_subplot(3, 3, 3, projection='3d')
ax.set_title('Combined Model Potential')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential')

# Hyperbolic Tangent Model Gradient (r component)
ax = fig.add_subplot(3, 3, 4)
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_r_hyperbolic * np.cos(Theta), grad_r_hyperbolic * np.sin(Theta))
ax.set_title('Hyperbolic Tangent Model Gradient (r)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Traditional Kerr Model Gradient (r component)
ax = fig.add_subplot(3, 3, 5)
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_r_kerr * np.cos(Theta), grad_r_kerr * np.sin(Theta))
ax.set_title('Traditional Kerr Model Gradient (r)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Placeholder for combined plot if needed
ax = fig.add_subplot(3, 3, 6)
ax.set_title('Combined Model Gradient (r)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Hyperbolic Tangent Model Gradient (theta component)
ax = fig.add_subplot(3, 3, 7)
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_theta_hyperbolic * np.cos(Theta), grad_theta_hyperbolic * np.sin(Theta))
ax.set_title('Hyperbolic Tangent Model Gradient (theta)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Traditional Kerr Model Gradient (theta component)
ax = fig.add_subplot(3, 3, 8)
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_theta_kerr * np.cos(Theta), grad_theta_kerr * np.sin(Theta))
ax.set_title('Traditional Kerr Model Gradient (theta)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Placeholder for combined plot if needed
ax = fig.add_subplot(3, 3, 9)
ax.set_title('Combined Model Gradient (theta)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.tight_layout()
plt.show()