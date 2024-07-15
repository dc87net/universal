import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
M_app = M / 2  # Apparent mass due to entanglement
c = 2.998e8  # Speed of light, m/s
a = 0.9  # Spin parameter, dimensionless
r_s = 2 * G * M / c**2  # Schwarzschild radius, m
r_s_app = r_s / 2  # Apparent Schwarzschild radius

# Define a grid for r and theta around critical points
r_critical = np.linspace(0.5 * r_s, 2 * r_s, 500)
theta = np.linspace(0, 2 * np.pi, 500)
R, Theta = np.meshgrid(r_critical, theta)

# Hyperbolic Tangent Model Potential
def potential_hyperbolic(r, r_s, G, M):
    x = r / r_s
    return -G * M / (r_s * np.tanh(x))

# Traditional Kerr Model Potential
def potential_kerr(r, G, M, a):
    return -G * M / (r * (1 + a**2 / r**2))

# Calculate the potentials for actual and apparent masses
V_hyperbolic = potential_hyperbolic(R, r_s, G, M)
V_hyperbolic_app = potential_hyperbolic(R, r_s_app, G, M_app)
V_kerr = potential_kerr(R, G, M, a)
V_kerr_app = potential_kerr(R, G, M_app, a)

# Calculate the redshift for actual and apparent masses
def redshift(G, M, r):
    return G * M / (c**2 * r)

redshift_actual_hyperbolic = redshift(G, M, R)
redshift_apparent_hyperbolic = redshift(G, M_app, R)
redshift_actual_kerr = redshift(G, M, R)
redshift_apparent_kerr = redshift(G, M_app, R)

# Plot the potential fields
fig, axes = plt.subplots(2, 2, figsize=(14, 14), subplot_kw={'projection': '3d'})

# Hyperbolic Tangent Model Potential
axes[0, 0].plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_hyperbolic, cmap='viridis')
axes[0, 0].set_title('Hyperbolic Tangent Model Potential (Actual Mass)')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('Y')
axes[0, 0].set_zlabel('Potential')

axes[0, 1].plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_hyperbolic_app, cmap='viridis')
axes[0, 1].set_title('Hyperbolic Tangent Model Potential (Apparent Mass)')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('Y')
axes[0, 1].set_zlabel('Potential')

# Traditional Kerr Model Potential
axes[1, 0].plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_kerr, cmap='viridis')
axes[1, 0].set_title('Traditional Kerr Model Potential (Actual Mass)')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')
axes[1, 0].set_zlabel('Potential')

axes[1, 1].plot_surface(R * np.cos(Theta), R * np.sin(Theta), V_kerr_app, cmap='viridis')
axes[1, 1].set_title('Traditional Kerr Model Potential (Apparent Mass)')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('Y')
axes[1, 1].set_zlabel('Potential')

plt.tight_layout()
plt.show()

# Plot the redshift values
plt.figure(figsize=(10, 6))
plt.plot(R[:, 0], redshift_actual_hyperbolic[:, 0], label='Hyperbolic (Actual Mass)')
plt.plot(R[:, 0], redshift_apparent_hyperbolic[:, 0], label='Hyperbolic (Apparent Mass)')
plt.plot(R[:, 0], redshift_actual_kerr[:, 0], label='Kerr (Actual Mass)')
plt.plot(R[:, 0], redshift_apparent_kerr[:, 0], label='Kerr (Apparent Mass)')
plt.xlabel('Radial Distance (m)')
plt.ylabel('Redshift')
plt.title('Gravitational Redshift Comparison')
plt.legend()
plt.grid(True)
plt.show()