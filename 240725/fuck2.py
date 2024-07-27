import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpmath import gamma, cos, pi, mp
from sympy import primerange

# Set precision
mp.dps = 25

# Define the symbolic zeta function method
def zeta_symbolic(t):
    s_real = 0.5
    s_imag = t
    s_conjugate_real = 0.5
    s_conjugate_imag = -t

    # Compute the real and imaginary parts separately
    real_part = float((2**0.5 * (pi**(-(0.5 + 1j * t))).real) * float(cos(pi * (0.5 + 1j * t) / 2).real) *
                      float(gamma(0.5 + 1j * t).real) * float(mp.zeta(s_conjugate_real - 1j * s_conjugate_imag).real))
    imag_part = float((2**0.5 * (pi**(-(0.5 + 1j * t))).imag) * float(cos(pi * (0.5 + 1j * t) / 2).imag) *
                      float(gamma(0.5 + 1j * t).imag) * float(mp.zeta(s_conjugate_real - 1j * s_conjugate_imag).imag))

    return real_part, imag_part

# Define the range for the parameter t
t_values = np.linspace(0, 50, 1000)

# Compute zeta function values manually
zeta_vals = [zeta_symbolic(t) for t in t_values]
real_parts = np.array([val[0] for val in zeta_vals], dtype=float)
imag_parts = np.array([val[1] for val in zeta_vals], dtype=float)

# Generate prime numbers up to a certain limit
prime_limit = 200
primes = list(primerange(1, prime_limit))

# Place primes on the xy-plane
prime_x = np.array(primes, dtype=float)
prime_y = np.zeros_like(prime_x)

# Create the 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the zeta function values
ax.plot(real_parts, imag_parts, t_values, color='blue', lw=2, label='Zeta Function')

# Plot the primes on the xy-plane
ax.scatter(prime_x, prime_y, np.zeros_like(prime_x), color='red', s=50, label='Prime Numbers')

# Set labels and title
ax.set_xlabel('Real Part (x)')
ax.set_ylabel('Imaginary Part (y)')
ax.set_zlabel('Parameter t (height)')
ax.set_title('3D Visualization of the Riemann Zeta Function and Prime Numbers')
ax.view_init(elev=90, azim=-90)  # Top-down view

# Add a legend
ax.legend()

plt.show()
