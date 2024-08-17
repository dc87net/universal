import numpy as np
import matplotlib.pyplot as plt

# Parameters for the potential well
V0 = 1.0  # Depth of the potential well
k = 1.0  # Determines the width of the well
x = np.linspace(-5, 5, 400)

# Potential well using hyperbolic tangent function
V_x = -V0 * np.tanh(k * x) ** 2

# Plot the potential well
plt.figure(figsize=(10, 6))
plt.plot(x, V_x, label=r'$V(x) = -V_0 \cdot \tanh^2(kx)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Potential Well using Hyperbolic Tangent Function')
plt.xlabel('x')
plt.ylabel('V(x)')
plt.legend()
plt.grid(True)
plt.show()

# Parameters for the wave function
omega = 1.0  # Angular frequency
d = 1  # Dimensional factor (integer)
t = 0  # Time
k_wave = 1.0  # Wave number

# Wave function components
real_part = np.cos(k_wave * x - omega * t)
imag_part = (1j ** d) * np.sin(k_wave * x - omega * t)
wave_function = real_part + imag_part

# Plot the wave function components
plt.figure(figsize=(10, 6))
plt.plot(x, real_part, label=r'Real Part: $\cos(kx - \omega t)$')
plt.plot(x, imag_part.imag, label=r'Imaginary Part: $(i^d) \sin(kx - \omega t)$', linestyle='--')
plt.plot(x, wave_function.real, label=r'Wave Function: $\cos(kx - \omega t) + (i^d) \sin(kx - \omega t)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Wave Function Components')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

# Hyperbolic tangent function
tanh_x = np.tanh(x)

# Plot the hyperbolic tangent function
plt.figure(figsize=(10, 6))
plt.plot(x, tanh_x, label=r'$\tanh(x)$', color='purple')
plt.axhline(1, color='red', linestyle='--', label=r'$y = 1$')
plt.axhline(-1, color='red', linestyle='--', label=r'$y = -1$')
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Hyperbolic Tangent Function')
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.legend()
plt.grid(True)
plt.show()
