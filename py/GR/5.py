import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 2.998e8      # Speed of light, m/s
M = 1.989e30     # Mass of the black hole (Sun's mass), kg

# Schwarzschild radius
r_s = 2 * G * M / c**2

# Define the metric components in hyperbolic coordinates
def g_tt(x):
    return -(1 - 2 * G * M / (r_s * np.tanh(x) * c**2))

def g_xx(x):
    return (1 - 2 * G * M / (r_s * np.tanh(x) * c**2))**-1 * r_s**2 * np.cosh(x)**-2

# Define the potential term using hyperbolic functions
def V(x):
    return -G * M / (r_s * np.tanh(x))

# Range for x
x = np.linspace(-5, 5, 400)

# Calculate metric components
g_tt_values = g_tt(x)
g_xx_values = g_xx(x)
V_values = V(x)

# Plot the metric components and potential term
plt.figure(figsize=(14, 8))

plt.subplot(2, 1, 1)
plt.plot(x, g_tt_values, label='$g_{tt}$ (Time component)', color='red')
plt.plot(x, g_xx_values, label='$g_{xx}$ (Radial component)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Metric Components in Hyperbolic Coordinates')
plt.xlabel('x')
plt.ylabel('Metric Component Value')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x, V_values, label='Potential $V(x)$', color='green')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Potential Term $V(x)$')
plt.xlabel('x')
plt.ylabel('Potential $V(x)$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
