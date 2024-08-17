import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define parameters
kx_val = 2 * np.pi  # Wavenumber
omega_val = 2 * np.pi  # Angular frequency
d_val = 3  # Dimensional count for space-like dimensions
G = 6.67430e-11  # Gravitational constant
c = 299792458  # Speed of light in m/s

# Time domain
t_vals = np.linspace(-5, 5, 1000)
R_t_vals = np.exp(-t_vals**2)  # Example function for R(t)

# Generalized wave function components
real_part = np.cos(kx_val * t_vals - omega_val * t_vals)
imag_part = (1j**d_val) * np.sin(kx_val * t_vals - omega_val * t_vals)
psi_vals = R_t_vals * (real_part + imag_part)

# Calculate magnitude (squared) of the wave function
magnitude_sq = np.abs(psi_vals)**2

# Calculate Ricci tensor components numerically
R00_vals = -4.0 * np.pi * G * (kx_val * np.real(imag_part - real_part) * R_t_vals * np.conj(kx_val) * np.conj(R_t_vals) * np.gradient(np.conj(t_vals)) +
                              ((np.real(imag_part) + np.imag(real_part)) * np.gradient(np.conj(R_t_vals), t_vals) +
                               (np.real(imag_part) - np.imag(real_part)) * np.conj(omega_val) * np.conj(R_t_vals) * np.gradient(np.conj(t_vals), t_vals)) *
                              (omega_val * np.real(imag_part) * R_t_vals - np.imag(real_part) * np.gradient(R_t_vals, t_vals))) / c**4
R11_vals = -8.0 * np.pi * G * (1.5 * kx_val * (np.real(imag_part) - np.imag(real_part)) * R_t_vals * np.conj(kx_val) * np.conj(R_t_vals) * np.gradient(np.conj(t_vals)) -
                              0.5 * ((np.real(imag_part) + np.imag(real_part)) * np.gradient(np.conj(R_t_vals), t_vals) +
                                     (np.real(imag_part) - np.imag(real_part)) * np.conj(omega_val) * np.conj(R_t_vals) * np.gradient(np.conj(t_vals), t_vals)) *
                              (omega_val * np.real(imag_part) * R_t_vals - np.imag(real_part) * np.gradient(R_t_vals, t_vals))) / c**4

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t_vals, np.real(psi_vals), label='Real part')
plt.plot(t_vals, np.imag(psi_vals), label='Imaginary part', linestyle='--')
plt.title('Generalized Wave Function')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_vals, magnitude_sq, label='Magnitude Squared')
plt.plot(t_vals, R00_vals, label='R00 Component', linestyle='--')
plt.plot(t_vals, R11_vals, label='R11 Component', linestyle=':')
plt.title('Components of the Ricci Tensor and Magnitude Squared')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()