import numpy as np
import matplotlib.pyplot as plt

# Speed of light
c = 3e8  # meters per second

# Define parameters
kx = 2 * np.pi  # Wavenumber
omega = 2 * np.pi  # Angular frequency
d = 1  # Dimensional count
v = 0.8 * c  # Relative velocity (80% of the speed of light)
gamma = 1 / np.sqrt(1 - (v / c)**2)

# Space and time domain
x = np.linspace(-10, 10, 1000)
t = np.linspace(-10, 10, 1000)
X, T = np.meshgrid(x, t)

# Lorentz-transformed coordinates
x_prime = gamma * (X - v * T)
t_prime = gamma * (T - v * X / c**2)

# Generalized wave function in the transformed frame
R_t = np.exp(-T**2)  # Example function for R(t)
psi_prime = R_t * (np.cos(kx * x_prime - omega * t_prime) + (1j**d) * np.sin(kx * x_prime - omega * t_prime))

# Magnitude squared of the wave function
psi_mag_squared = np.abs(psi_prime)**2

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.contourf(X, T, np.real(psi_prime), levels=50, cmap='RdBu_r')
plt.title('Real Part of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar()

plt.subplot(3, 1, 2)
plt.contourf(X, T, np.imag(psi_prime), levels=50, cmap='RdBu_r')
plt.title('Imaginary Part of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar()

plt.subplot(3, 1, 3)
plt.contourf(X, T, psi_mag_squared, levels=50, cmap='viridis')
plt.title('Magnitude Squared of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')
plt.colorbar()

plt.tight_layout()
plt.show()