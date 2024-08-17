import numpy as np
import matplotlib.pyplot as plt

# Define parameters
kx = 2 * np.pi  # Wavenumber
omega = 2 * np.pi  # Angular frequency
d = 1  # Dimensional count
R = 3  # Example value for R

# Time domain
t = np.linspace(-5, 5, 1000)
R_t = np.exp(-t**2)  # Example function for R(t)

# Generalized wave function with scaling factor 3/R
psi_t = (3 / R) * R_t * (np.cos((3 / R) * (kx - omega * t)) + (1j**d) * np.sin((3 / R) * (kx - omega * t)))

# Solve for R(t)
R_t_calculated = np.abs(psi_t)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, np.real(psi_t), label='Real part')
plt.plot(t, np.imag(psi_t), label='Imaginary part', linestyle='--')
plt.title('Generalized Wave Function with Scaling Factor 3/R')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, R_t, label='Original R(t)')
plt.plot(t, R_t_calculated, label='Calculated R(t)', linestyle='--')
plt.title('Comparison of Original and Calculated R(t) with Scaling Factor 3/R')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()