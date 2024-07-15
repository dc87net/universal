import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
kx = 2 * np.pi  # Wavenumber
omega = 2 * np.pi  # Angular frequency
d = 1  # Dimensional count

# Define the domain
x = np.linspace(-10, 10, 1000)
R_t = np.exp(-x**2)  # Example function for R(t)

# Generalized wave function
psi = R_t * (np.cos(kx * x - omega * x) + (1j**d) * np.sin(kx * x - omega * x) * 1j)

# Calculate the phase angle using np.angle
phase_angle = np.angle(psi)

# 2D plot of the phase angle
plt.figure(figsize=(12, 6))
plt.plot(x, phase_angle, label='Phase Angle')
plt.title('Phase Angle of the Generalized Wave Function')
plt.xlabel('Position x')
plt.ylabel('Phase Angle (radians)')
plt.legend()
plt.grid(True)
plt.show()