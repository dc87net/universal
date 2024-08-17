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
    real_part = (2**0.5 * (pi**(-(0.5 + 1j * t))).real * cos(pi * (0.5 + 1j * t) / 2).real *
                 gamma(0.5 + 1j * t).real * mp.zeta(s_conjugate_real - 1j * s_conjugate_imag).real)
    imag_part = (2**0.5 * (pi**(-(0.5 + 1j * t))).imag * cos(pi * (0.5 + 1j * t) / 2).imag *
                 gamma(0.5 + 1j * t).imag * mp.zeta(s_conjugate_real - 1j * s_conjugate_imag).imag)

    return float(real_part), float(imag_part)

# Define the range for the parameter t
t_values = np.linspace(0, 50, 1000)

# Compute zeta function values manually
zeta_vals = [zeta_symbolic(t) for t in t_values]
real_parts = np.array([val[0] for val in zeta_vals])
imag_parts = np.array([val[1] for val in zeta_vals])
magnitudes = np.sqrt(real_parts**2 + imag_parts**2)
phases = np.arctan2(imag_parts, real_parts)

# Generate prime numbers up to a certain limit
prime_limit = 200
primes = list(primerange(1, prime_limit))

# Compute zeta function values at prime numbers manually
prime_zeta_vals = [zeta_symbolic(p) for p in primes]
prime_real_parts = np.array([val[0] for val in prime_zeta_vals])
prime_imag_parts = np.array([val[1] for val in prime_zeta_vals])
prime_magnitudes = np.sqrt(prime_real_parts**2 + prime_imag_parts**2)
prime_phases = np.arctan2(prime_imag_parts, prime_real_parts)

# Create the 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the zeta function values
ax.scatter(phases, magnitudes, t_values, color='blue', lw=2, label='Zeta Function')

# Plot the primes as a scatter plot in 3D, using magnitudes and phases
ax.scatter(prime_phases, prime_magnitudes, primes, color='red', s=50, label='Prime Numbers')

# Set labels and title
ax.set_xlabel('Phase (radians)')
ax.set_ylabel('Magnitude')
ax.set_zlabel('Parameter t')
ax.set_title('3D Polar Visualization of the Symbolic Riemann Zeta Function and Prime Numbers')
ax.view_init(elev=30., azim=45)  # Isometric view

# Add a legend
ax.legend()

plt.show()