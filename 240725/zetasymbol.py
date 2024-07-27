import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, gamma, cos, pi

# Define the critical line
sigma = 0.5
t_values = np.linspace(0, 50, 1000)

# Define the zeta function along the critical line using numerical methods
def zeta_numerical(t):
    s = complex(0.5, t)
    return zeta(s)

# Generate values using the numerical approach
zeta_numerical_values = [zeta_numerical(t) for t in t_values]
real_numerical = [z.real for z in zeta_numerical_values]
imaginary_numerical = [z.imag for z in zeta_numerical_values]

# Define the zeta function along the critical line using the recursive symbolic approach
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Generate values using the symbolic approach
zeta_symbolic_values = [zeta_symbolic(t) for t in t_values]
real_symbolic = [z.real for z in zeta_symbolic_values]
imaginary_symbolic = [z.imag for z in zeta_symbolic_values]

# Plotting the results
plt.figure(figsize=(14, 7))

# Plot numerical results
plt.plot(t_values, real_numerical, label='Numerical Real Part', color='blue')
plt.plot(t_values, imaginary_numerical, label='Numerical Imaginary Part', linestyle='--', color='orange')

# Plot symbolic results
plt.plot(t_values, real_symbolic, label='Symbolic Real Part', color='green', alpha=0.7)
plt.plot(t_values, imaginary_symbolic, label='Symbolic Imaginary Part', linestyle='--', color='red', alpha=0.7)

# Overlay the two plots
plt.title('Comparison of Numerical and Symbolic Values of the Riemann Zeta Function along the Critical Line (Re(s) = 0.5)')
plt.xlabel('Imaginary part of s (t)')
plt.ylabel('Zeta(s)')
plt.legend()
plt.grid(True)
plt.show()
