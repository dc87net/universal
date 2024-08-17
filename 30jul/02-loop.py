import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, mp, arg

# Set precision
mp.dps = 25

# Custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * np.pi**(-(0.5 + 1j*t)) * np.cos(np.pi * (0.5 + 1j*t) / 2) *
            mp.gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = np.array([zeta_symbolic(t) for t in t_values], dtype=complex)

# Compute the phase
phase_vals = np.angle(zeta_vals)

# Plot the phase loop
plt.figure(figsize=(12, 6))
plt.plot(t_values, phase_vals, label='Phase of Zeta Function')
plt.xlabel('t')
plt.ylabel('Phase')
plt.title('Phase Loop of the Riemann Zeta Function')
plt.grid(True)
plt.legend()
plt.show()
