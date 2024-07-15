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

# Plotting
plt.figure(figsize=(12, 8))

# AM Plot
plt.subplot(3, 1, 1)
plt.plot(theta, np.real(psi_am), label='Real part')
plt.plot(theta, np.imag(psi_am), label='Imaginary part', linestyle='--')
plt.title('Amplitude Modulation (AM)')
plt.xlabel('Phase angle (radians)')
plt.ylabel('Amplitude')
plt.legend()

# FM Plot
plt.subplot(3, 1, 2)
plt.plot(theta, np.real(psi_fm), label='Real part')
plt.plot(theta, np.imag(psi_fm), label='Imaginary part', linestyle='--')
plt.title('Frequency Modulation (FM)')
plt.xlabel('Phase angle (radians)')
plt.ylabel('Amplitude')
plt.legend()

# PM Plot
plt.subplot(3, 1, 3)
plt.plot(theta, np.real(psi_pm), label='Real part')
plt.plot(theta, np.imag(psi_pm), label='Imaginary part', linestyle='--')
plt.title('Phase Modulation (PM)')
plt.xlabel('Phase angle (radians)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()