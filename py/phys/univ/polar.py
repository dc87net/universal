import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1
omega = 1
t = np.linspace(0, 10, 1000)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # x in radians

# Specific angle
theta = 1 / np.sqrt(2)

# Generalized wave function in polar form
R_t = np.abs(np.cos(k * x[:, np.newaxis] - omega * t))
phase = np.angle(np.cos(k * x[:, np.newaxis] - omega * t) + np.sin(k * x[:, np.newaxis] - omega * t) * np.exp(1j * np.pi / 2))

# Plotting the wave function in polar coordinates
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(phase[:, 500], R_t[:, 500], label='Wave function')
ax.set_title('Polar Plot of Generalized Wave Function')
plt.legend()
plt.show()