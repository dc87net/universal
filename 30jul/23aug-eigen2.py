import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, mp

# Set precision
mp.dps = 25

# Custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    return zeta(s)

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = np.array([zeta_symbolic(t) for t in t_values], dtype=complex)

# Compute the magnitude and phase
real_vals = zeta_vals.real
imag_vals = zeta_vals.imag
abs_vals = np.abs(zeta_vals)

# Plot the real and imaginary parts
plt.figure(figsize=(12, 6))
plt.plot(t_values, real_vals, label='Real Part')
plt.plot(t_values, imag_vals, label='Imaginary Part')
plt.plot(t_values, abs_vals, label='Magnitude', linestyle='--')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Riemann Zeta Function along the Critical Line')
plt.grid(True)
plt.legend()
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpmath import zeta, mp
#
# # Set precision
# mp.dps = 25
#
# # Custom symbolic zeta function method
# def zeta_symbolic(t):
#     s = complex(0.5, t)
#     s_conjugate = complex(0.5, -t)
#     return (2**(0.5 - 1j*t) * np.pi**(-(0.5 + 1j*t)) * np.cos(np.pi * (0.5 + 1j*t) / 2) *
#             mp.gamma(0.5 + 1j*t) * zeta(s_conjugate))
#
# # Define the range for the imaginary part of s
# t_values = np.linspace(0, 50, 1000)
#
# # Compute symbolic zeta function values
# zeta_vals = np.array([zeta_symbolic(t) for t in t_values], dtype=complex)
#
# # Plot the real and imaginary parts of zeta_vals
# plt.figure(figsize=(12, 6))
# plt.plot(zeta_vals.real, zeta_vals.imag, label='Eigenvalues', linestyle='-', marker='o')
# plt.xlabel('Real Part')
# plt.ylabel('Imaginary Part')
# plt.title('Eigenvalue Representation of the Symbolic Zeta Function')
# plt.grid(True)
# plt.legend()
# plt.show()
