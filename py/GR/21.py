import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, fftshift

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 1.989e30     # Mass of the black hole (Sun's mass), kg
r_s = 2 * G * M / (2.998e8)**2  # Schwarzschild radius, m

# Define the potential function in 2D
def V(x, y):
    r = np.sqrt(x**2 + y**2)
    return -G * M / (r_s * np.tanh(r))

# Define the range for x and y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = V(X, Y)

# Compute the 2D Fourier Transform
Z_fft = fft2(Z)
Z_fft_shifted = fftshift(Z_fft)  # Shift zero frequency component to the center
magnitude_spectrum = np.abs(Z_fft_shifted)

# Plot the original potential field
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

ax[0].contourf(X, Y, Z, cmap='viridis')
ax[0].set_title('Potential Field $V(x, y)$')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

# Plot the magnitude of the Fourier Transform
ax[1].imshow(np.log1p(magnitude_spectrum), extent=(-5, 5, -5, 5), cmap='viridis')
ax[1].set_title('Fourier Transform Magnitude Spectrum')
ax[1].set_xlabel('Frequency x')
ax[1].set_ylabel('Frequency y')

plt.colorbar(ax[1].imshow(np.log1p(magnitude_spectrum), extent=(-5, 5, -5, 5), cmap='viridis'), ax=ax[1])
plt.show()