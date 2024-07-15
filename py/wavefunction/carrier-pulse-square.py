import numpy as np
import matplotlib.pyplot as plt

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

# Plotting the signal
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label='Composite Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Composite Signal with Carrier Frequency Modulation')
plt.legend()
plt.grid(True)
plt.show()