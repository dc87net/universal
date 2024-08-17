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

# Compute symbolic zeta function values and second derivative
zeta_vals = np.array([zeta_symbolic(t) for t in t_values], dtype=complex)
zeta_second_deriv = np.gradient(np.gradient(zeta_vals, t_values), t_values)

# Plot the original zeta function and its second derivative
plt.figure(figsize=(14, 7))

# Plot real parts
plt.subplot(1, 2, 1)
plt.plot(t_values, zeta_vals.real, label='Re(Zeta)', color='blue')
plt.plot(t_values, zeta_second_deriv.real, label='Re(Second Derivative)', color='red', linestyle='dashed')
plt.xlabel('t')
plt.ylabel('Real Part')
plt.title('Real Parts of Zeta Function and Its Second Derivative')
plt.legend()

# Plot imaginary parts
plt.subplot(1, 2, 2)
plt.plot(t_values, zeta_vals.imag, label='Im(Zeta)', color='blue')
plt.plot(t_values, zeta_second_deriv.imag, label='Im(Second Derivative)', color='red', linestyle='dashed')
plt.xlabel('t')
plt.ylabel('Imaginary Part')
plt.title('Imaginary Parts of Zeta Function and Its Second Derivative')
plt.legend()

plt.tight_layout()
plt.show()
