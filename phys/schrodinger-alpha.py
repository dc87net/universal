import numpy as np
import matplotlib.pyplot as plt

# Define constants
hbar = 1.0545718e-34  # Planck's constant (J s)
m = 9.10938356e-31  # Mass of electron (kg)
alpha = 1  # Scaling factor (can be adjusted)
kx = 2 * np.pi  # Wavenumber
omega = hbar * (alpha * kx)**2 / (2 * m)  # Angular frequency for free particle
d = 1  # Dimensional count

# Time domain
t = np.linspace(-1e-10, 1e-10, 1000)  # Larger time range for better visualization
R_t = np.exp(-t**2)  # Example function for R(t)

# Generalized wave function
psi_t = R_t * (np.cos(alpha * kx * t - alpha * omega * t) + (1j**d) * np.sin(alpha * kx * t - alpha * omega * t))

# Calculate the Hamiltonian part
H_psi = - (hbar**2 * (alpha * kx)**2) / (2 * m) * psi_t

# Calculate the time derivative part
dpsi_dt = np.gradient(psi_t, t)
lhs = 1j * hbar * dpsi_dt

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, np.real(psi_t), label='Real part')
plt.plot(t, np.imag(psi_t), label='Imaginary part', linestyle='--')
plt.title('Generalized Wave Function with Scaling Factor α')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, np.real(lhs), label='Real part of LHS')
plt.plot(t, np.real(H_psi), label='Real part of RHS', linestyle='--')
plt.title('Verification of Schrödinger Equation with α')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()