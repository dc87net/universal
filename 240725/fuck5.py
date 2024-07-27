import matplotlib.pyplot as plt
from sympy import primerange
import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, gamma, cos, pi, mp

# Set precision
mp.dps = 25

# Custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = [zeta_symbolic(t) for t in t_values]

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)

# Identify zeros (where both real and imaginary parts are close to zero)
epsilon = 1e-6  # Small threshold to identify zeros
zeros = [(0.5, t) for t, r, i in zip(t_values, real_parts, imag_parts) if abs(r) < epsilon and abs(i) < epsilon]
zeros_real = [zero[0] for zero in zeros]
zeros_imag = [zero[1] for zero in zeros]

# Plot the zeta function values and zeros
plt.figure(figsize=(10, 6))
plt.plot(t_values, real_parts, label='Real Part', color='blue')
plt.plot(t_values, imag_parts, label='Imaginary Part', color='green')
plt.scatter(zeros_imag, [0] * len(zeros_imag), color='red', label='Zeros')
plt.xlabel('Imaginary Part of s')
plt.ylabel('Value')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0.5, color='red', linestyle='--', label='Critical Line (Re(s) = 0.5)')
plt.title('Values of the Custom Symbolic Riemann Zeta Function and Zeros')
plt.legend()
plt.show()
# Generate prime numbers up to a certain limit
prime_limit = 200
primes = list(primerange(1, prime_limit))

# Overlay prime numbers as red dots in the same 3D space
plt.figure(figsize=(10, 6))
plt.plot(t_values, real_parts, label='Real Part', color='blue')
plt.plot(t_values, imag_parts, label='Imaginary Part', color='green')
plt.scatter(zeros_imag, [0] * len(zeros_imag), color='red', label='Zeros')
plt.scatter([0.5] * len(primes), primes, color='orange', label='Prime Numbers', zorder=5)
plt.xlabel('Imaginary Part of s')
plt.ylabel('Value')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0.5, color='red', linestyle='--', label='Critical Line (Re(s) = 0.5)')
plt.title('Values of the Custom Symbolic Riemann Zeta Function, Zeros, and Prime Numbers')
plt.legend()
plt.show()