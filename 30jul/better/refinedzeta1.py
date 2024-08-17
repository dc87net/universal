import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10  # Finite range for normalization
rho = 0.5 + 14.1347j  # Example zero of zeta function
k = 1.0  # Wave number

# Define the range for s
s_real = np.linspace(rho.real - L/2, rho.real + L/2, 1000)
s_imag = np.linspace(rho.imag - L/2, rho.imag + L/2, 1000)
s = s_real + 1j * s_imag

# Wave function
phi_s = (1/np.sqrt(L)) * np.exp(1j * k * (s - rho))

# Probability density
prob_density = np.abs(phi_s)**2

# Plot wave function (real and imaginary parts)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(s_real, phi_s.real, label='Real Part')
plt.plot(s_real, phi_s.imag, label='Imaginary Part')
plt.xlabel('s (real part)')
plt.ylabel('phi(s)')
plt.title('Wave Function Near Zero')
plt.legend()

# Plot probability density
plt.subplot(1, 2, 2)
plt.plot(s_real, prob_density)
plt.xlabel('s (real part)')
plt.ylabel('Probability Density')
plt.title('Probability Density Near Zero')

plt.tight_layout()
plt.show()
