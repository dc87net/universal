import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, gamma, cos, pi, mp

# Set precision
mp.dps = 25

# Define the custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the parametric equations for the real and imaginary parts
def parametric_real(t, params):
    # Replace with your actual parametric equation for the real part
    return params[0] * np.cos(t) + params[1] * np.sin(t)

def parametric_imag(t, params):
    # Replace with your actual parametric equation for the imaginary part
    return params[0] * np.sin(t) - params[1] * np.cos(t)

# Parameters for the parametric equations
params = [1, 0.5]

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = [zeta_symbolic(t) for t in t_values]

# Extract real and imaginary parts from the zeta function
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)
amplitude = np.sqrt(real_parts**2 + imag_parts**2)

# Calculate the parametric real and imaginary parts
param_real_parts = [parametric_real(t, params) for t in t_values]
param_imag_parts = [parametric_imag(t, params) for t in t_values]

# Plotting the results
plt.figure(figsize=(14, 7))

# Plot real parts
plt.plot(t_values, real_parts, label='Zeta Real Part', color='blue')
plt.plot(t_values, param_real_parts, label='Parametric Real Part', linestyle='--', color='cyan')

# Plot imaginary parts
plt.plot(t_values, imag_parts, label='Zeta Imaginary Part', color='green')
plt.plot(t_values, param_imag_parts, label='Parametric Imaginary Part', linestyle='--', color='lime')

# Customize the plot
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.title('Comparison of Zeta Function and Parametric Forms')
plt.legend()
plt.show()
