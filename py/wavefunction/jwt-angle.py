import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
A = 1  # Amplitude
omega = 2 * np.pi * 1  # Carrier frequency (1 Hz)
beta = 1  # Modulation index
omega_m = 2 * np.pi * 0.1  # Message frequency (0.1 Hz)
theta = np.linspace(0, 2 * np.pi, 1000)  # Phase angle

# Message signal m(theta)
m_theta = np.sin(omega_m * theta)

# Amplitude Modulation (AM)
psi_am = (A + m_theta) * (np.cos(theta) + 1j * np.sin(theta))

# Frequency Modulation (FM)
psi_fm = A * (np.cos(theta + beta * np.sin(omega_m * theta)) + 1j * np.sin(theta + beta * np.sin(omega_m * theta)))

# Phase Modulation (PM)
psi_pm = A * (np.cos(theta + beta * m_theta) + 1j * np.sin(theta + beta * m_theta))

# Create 3D plot
fig = plt.figure(figsize=(18, 6))

ax = fig.add_subplot(111, projection='3d')

# Plot AM
ax.plot(np.real(psi_am), np.imag(psi_am), theta, label='AM')
# Plot FM
ax.plot(np.real(psi_fm), np.imag(psi_fm), theta, label='FM')
# Plot PM
ax.plot(np.real(psi_pm), np.imag(psi_pm), theta, label='PM')

ax.set_title('3D Plot of Modulation Types (AM, FM, PM)')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Phase Angle (theta)')
ax.legend()

plt.show()