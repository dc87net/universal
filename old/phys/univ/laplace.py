import numpy as np
import matplotlib.pyplot as plt

# Constants
omega = 1
a = 1  # Decay rate for R(t) = e^{-at}
s = np.linspace(0.1, 10, 1000) + 1j * np.linspace(0.1, 10, 1000)

# Laplace transform components
cos_transform = s / (s**2 + omega**2)
sin_transform = omega / (s**2 + omega**2)
R_transform = 1 / (s + a)

# Combined Laplace transform
psi_transform = R_transform * (cos_transform + 1j * sin_transform)

# Magnitude and phase
magnitude = np.abs(psi_transform)
phase = np.angle(psi_transform)

# Plotting the magnitude
plt.figure(figsize=(12, 6))
plt.plot(s.real, magnitude, label='Magnitude')
plt.title('Magnitude of the Laplace Transform of $\Psi(x, t, d)$')
plt.xlabel('Real part of s')
plt.ylabel('Magnitude')
plt.legend()
plt.grid()
plt.show()

# Plotting the phase
plt.figure(figsize=(12, 6))
plt.plot(s.real, phase, label='Phase')
plt.title('Phase of the Laplace Transform of $\Psi(x, t, d)$')
plt.xlabel('Real part of s')
plt.ylabel('Phase')
plt.legend()
plt.grid()
plt.show()