import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
A = 1  # Amplitude
omega_1 = 2 * np.pi * 1  # Frequency 1 (1 Hz)
omega_2 = 2 * np.pi * 2  # Frequency 2 (2 Hz)
phi_omega_1 = 0  # Phase shift for omega_1
phi_omega_2 = np.pi / 4  # Phase shift for omega_2
c = 299792458  # Speed of light in m/s
k_c = 1e7  # Wave number for the carrier frequency
omega_c = k_c * c  # Carrier frequency
t = np.linspace(0, 1, 1000)  # Time vector

# Composite signal
signal = (A / 2) * (np.cos(omega_1 * t + phi_omega_1) + np.cos(omega_2 * t + phi_omega_2)) * np.cos(omega_c * t)

# Squaring the composite signal
squared_signal = signal ** 2

# Real and imaginary parts of the signal
real_part = np.cos(omega_1 * t + phi_omega_1)
imaginary_part = np.sin(omega_2 * t + phi_omega_2)

# Create a 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the squared signal
ax.plot(real_part, imaginary_part, squared_signal, label='Squared Signal')

# Labels and title
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Magnitude (Squared)')
ax.set_title('3D Plot of Squared Composite Signal with Real and Imaginary Parts')

# Legend and grid
ax.legend()
ax.grid(True)

# Show the plot
plt.show()