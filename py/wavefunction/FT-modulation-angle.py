import numpy as np
import matplotlib.pyplot as plt

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

# Plotting the modulation types together
plt.figure(figsize=(18, 6))

# Combined AM, FM, PM
plt.subplot(131)
plt.plot(theta, np.real(psi_am), label='AM - Real')
plt.plot(theta, np.imag(psi_am), label='AM - Imaginary', linestyle='--')
plt.plot(theta, np.real(psi_fm), label='FM - Real')
plt.plot(theta, np.imag(psi_fm), label='FM - Imaginary', linestyle='--')
plt.plot(theta, np.real(psi_pm), label='PM - Real')
plt.plot(theta, np.imag(psi_pm), label='PM - Imaginary', linestyle='--')
plt.title('Combined Modulation Types (AM, FM, PM)')
plt.xlabel('Phase angle (theta)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()