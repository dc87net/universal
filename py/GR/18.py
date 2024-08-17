import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
c = 2.998e8  # Speed of light, m/s
a = 0.9  # Spin parameter, dimensionless
r_s = 2 * G * M / c**2  # Schwarzschild radius, m

# Define a grid for r and theta around critical points
r_critical = np.linspace(0.9 * r_s, 1.1 * r_s, 500)
theta = np.linspace(0, 2 * np.pi, 500)
R, Theta = np.meshgrid(r_critical, theta)

# Hyperbolic Tangent Model Potential
def potential_hyperbolic(r, r_s, G, M):
    x = r / r_s
    return -G * M / (r_s * np.tanh(x))

# Traditional Kerr Model Potential (simplified)
def potential_kerr(r, G, M, a):
    return -G * M / (r * (1 + a**2 / r**2))

# Calculate the potentials
V_hyperbolic = potential_hyperbolic(R, r_s, G, M)
V_kerr = potential_kerr(R, G, M, a)

# Calculate the gradients
def gradient_field(V, dr, dtheta):
    grad_r = np.gradient(V, dr, axis=0)
    grad_theta = np.gradient(V, dtheta, axis=1)
    return grad_r, grad_theta

# Radial and angular step sizes
dr = r_critical[1] - r_critical[0]
dtheta = theta[1] - theta[0]

# Gradient fields for both models
grad_r_hyperbolic, grad_theta_hyperbolic = gradient_field(V_hyperbolic, dr, dtheta)
grad_r_kerr, grad_theta_kerr = gradient_field(V_kerr, dr, dtheta)

# Plot all visualizations in a 2x2 grid for critical comparison
fig, axes = plt.subplots(2, 2, figsize=(14, 14))

# Hyperbolic Tangent Model Potential near critical points
ax = axes[0, 0]
c = ax.contourf(R * np.cos(Theta), R * np.sin(Theta), V_hyperbolic, cmap='viridis')
fig.colorbar(c, ax=ax)
ax.set_title('Hyperbolic Tangent Model Potential')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Traditional Kerr Model Potential near critical points
ax = axes[0, 1]
c = ax.contourf(R * np.cos(Theta), R * np.sin(Theta), V_kerr, cmap='viridis')
fig.colorbar(c, ax=ax)
ax.set_title('Traditional Kerr Model Potential')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Hyperbolic Tangent Model Gradient (r component) near critical points
ax = axes[1, 0]
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_r_hyperbolic * np.cos(Theta), grad_r_hyperbolic * np.sin(Theta))
ax.set_title('Hyperbolic Tangent Model Gradient (r)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Traditional Kerr Model Gradient (r component) near critical points
ax = axes[1, 1]
ax.quiver(R * np.cos(Theta), R * np.sin(Theta), grad_r_kerr * np.cos(Theta), grad_r_kerr * np.sin(Theta))
ax.set_title('Traditional Kerr Model Gradient (r)')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.tight_layout()
plt.show()