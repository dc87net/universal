import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10  # Finite range for normalization
rho = 0.5 + 14.1347j  # First non-trivial zero of zeta function
k = 1.0  # Wave number

# Define the range for s
s_real = np.linspace(rho.real - L/2, rho.real + L/2, 1000)

# Define contributions from multiple nearby states
n_states = 5
coefficients = np.random.rand(n_states) + 1j * np.random.rand(n_states)  # Random complex coefficients
coefficients /= np.linalg.norm(coefficients)  # Normalize coefficients
rho_n = rho + (np.random.rand(n_states) - 0.5) + 1j * (np.random.rand(n_states) - 0.5)  # Nearby states

# Wave function as superposition
phi_s = np.zeros_like(s_real, dtype=np.complex128)
for n in range(n_states):
    phi_s += coefficients[n] * np.exp(1j * k * (s_real - rho_n[n].real))

phi_s /= np.sqrt(L)  # Normalize wave function

# Probability density
prob_density = np.abs(phi_s)**2

# Plot probability density
plt.figure(figsize=(8, 6))
plt.plot(s_real, prob_density)
plt.xlabel('s (real part)')
plt.ylabel('Probability Density')
plt.title('Probability Density Near Zero (Superposition)')
plt.axvline(rho.real, color='r', linestyle='--', label=f'Zero at {rho.real}')
plt.legend()

plt.show()
