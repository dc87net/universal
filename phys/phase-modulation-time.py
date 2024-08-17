import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1  # Amplitude
k = 2 * np.pi  # Wave number
omega = 2 * np.pi * 1  # Carrier frequency (1 Hz)
beta = 1  # Modulation index
omega_m = 2 * np.pi * 0.1  # Message frequency (0.1 Hz)
t = np.linspace(0, 10, 1000)  # Time vector
x = 0  # Position (for simplicity, we consider x=0)

# Message signal m(t)
m_t = np.sin(omega_m * t)

# Amplitude Modulation (AM)
psi_am = (A + m_t) * (np.cos(k * x - omega * t) + 1j * np.sin(k * x - omega * t))

# Frequency Modulation (FM)
psi_fm = A * (np.cos(k * x - omega * t + beta * np.sin(omega_m * t)) + 1j * np.sin(k * x - omega * t + beta * np.sin(omega_m * t)))

# Phase Modulation (PM)
psi_pm = A * (np.cos(k * x - omega * t + beta * m_t) + 1j * np.sin(k * x - omega * t + beta * m_t))

# Plotting
plt.figure(figsize=(12, 8))

# AM Plot
plt.subplot(3, 1, 1)
plt.plot(t, np.real(psi_am), label='Real part')
plt.plot(t, np.imag(psi_am), label='Imaginary part', linestyle='--')
plt.title('Amplitude Modulation (AM)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# FM Plot
plt.subplot(3, 1, 2)
plt.plot(t, np.real(psi_fm), label='Real part')
plt.plot(t, np.imag(psi_fm), label='Imaginary part', linestyle='--')
plt.title('Frequency Modulation (FM)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

# PM Plot
plt.subplot(3, 1, 3)
plt.plot(t, np.real(psi_pm), label='Real part')
plt.plot(t, np.imag(psi_pm), label='Imaginary part', linestyle='--')
plt.title('Phase Modulation (PM)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()