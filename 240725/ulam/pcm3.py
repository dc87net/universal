import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.spatial.distance import cosine

# Given sequence
sequence = [11, 9, 0, 13, 0, 4, 14, 15, 12, 11]

# Define the phase phi(t) by integrating the sequence
phi_t = np.cumsum(sequence)

# Compute instantaneous radian frequency omega_i(t)
omega_i_t = np.gradient(phi_t)

# Define the function r(phi)
def r_phi(phi, A=1, B=1, N=10):
    return A / np.log(B * np.tan(phi / (2 * N)))

# Plot phi(t) and omega_i(t)
plt.figure(figsize=(12, 6))

# Plot phi(t)
plt.subplot(121)
plt.plot(phi_t, label='phi(t)')
plt.title('Phase phi(t)')
plt.xlabel('t')
plt.ylabel('phi(t)')
plt.grid(True)
plt.legend()

# Plot omega_i(t)
plt.subplot(122)
plt.plot(omega_i_t, label='omega_i(t)')
plt.title('Instantaneous Radian Frequency omega_i(t)')
plt.xlabel('t')
plt.ylabel('omega_i(t)')
plt.grid(True)
plt.legend()

plt.show()

# Compute r(phi)
phi_range = np.linspace(min(phi_t), max(phi_t), 100)
r_values = r_phi(phi_range)

# Plot r(phi)
plt.figure(figsize=(10, 4))
plt.plot(phi_range, r_values, label='r(phi)')
plt.title('Function r(phi)')
plt.xlabel('phi')
plt.ylabel('r(phi)')
plt.grid(True)
plt.legend()
plt.show()

# Cosine similarity with a sample prime pattern (example)
prime_pattern = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Truncated for simplicity
sequence_normalized = sequence[:len(prime_pattern)]
cos_sim = 1 - cosine(sequence_normalized, prime_pattern[:len(sequence_normalized)])

print(f'Cosine similarity with prime pattern: {cos_sim}')