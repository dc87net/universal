import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
A = 1  # Amplitude
omega = 2 * np.pi * 1  # Carrier frequency (1 Hz)
beta = 1  # Modulation index
omega_m = 2 * np.pi * 0.1  # Message frequency (0.1 Hz)
t = np.linspace(0, 1, 1000)  # Time vector

# Message signal m(t)
m_t = np.sin(omega_m * t)

# Amplitude Modulation (AM)
psi_am = (A + m_t) * (np.cos(omega * t) + 1j * np.sin(omega * t))

# Frequency Modulation (FM)
psi_fm = A * (np.cos(omega * t + beta * np.sin(omega_m * t)) + 1j * np.sin(omega * t + beta * np.sin(omega_m * t)))

# Phase Modulation (PM)
psi_pm = A * (np.cos(omega * t + beta * m_t) + 1j * np.sin(omega * t + beta * m_t))

# Create 3D plot
fig = plt.figure(figsize=(18, 6))

ax = fig.add_subplot(111, projection='3d')

# Plot AM
ax.plot(np.real(psi_am), np.imag(psi_am), t, label='AM')
# Plot FM
ax.plot(np.real(psi_fm), np.imag(psi_fm), t, label='FM')
# Plot PM
ax.plot(np.real(psi_pm), np.imag(psi_pm), t, label='PM')

ax.set_title('3D Plot of Modulation Types (AM, FM, PM)')
ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Time (t)')
ax.legend()

plt.show()