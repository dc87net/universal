import numpy as np
import matplotlib.pyplot as plt
from mpmath import gamma, sin, pi, zeta

# Function to compute the factored-out part f(s)
def factored_zeta_without_zeta_1_minus_s(s):
    """
    Computes the expression 2^s * pi^(s-1) * sin(pi*s/2) * Gamma(1-s), without involving zeta(1-s).
    """
    gamma_term = gamma(1 - s)
    sine_term = sin(pi * s / 2)
    factor = (2**s) * (pi**(s - 1)) * sine_term * gamma_term
    return factor

# Function to compute the full zeta function as f(s) * ζ(1-s)
def full_zeta(s):
    """
    Computes the full Riemann zeta function via f(s) * zeta(1-s).
    """
    factored_part = factored_zeta_without_zeta_1_minus_s(s)
    zeta_1_minus_s = zeta(1 - s)
    return factored_part * zeta_1_minus_s

# Apply gain to the amplitude of the signal
def apply_gain_to_signal(signal, gain):
    """
    Applies gain to a given signal by multiplying its amplitude by the gain factor.
    """
    return gain * signal

# Define a range of values for s (critical line: Re(s) = 0.5)
t_values = np.linspace(0, 50, 5000)
s_values = 0.5 + 1j * t_values

# Compute the full zeta function values for s = 0.5 + it
full_zeta_values = np.array([full_zeta(s) for s in s_values])

# Compute the full zeta function values for 1 - s = 0.5 - it (reflection)
reflected_zeta_values = np.array([full_zeta(1 - s) for s in s_values])

# Apply gain to both sets of values
gain_factor = 10
amplified_full_zeta_values = apply_gain_to_signal(full_zeta_values, gain_factor)
amplified_reflected_zeta_values = apply_gain_to_signal(reflected_zeta_values, gain_factor)

# Apply the rotation by π/4 to both sets of amplified values
rotation_factor = np.exp(1j * np.pi / 4)
rotated_amplified_zeta_values = amplified_full_zeta_values * rotation_factor
rotated_reflected_zeta_values = amplified_reflected_zeta_values * rotation_factor

# Separate real and imaginary parts for s = 0.5 + it
rotated_real_parts_amplified = np.array([val.real for val in rotated_amplified_zeta_values])
rotated_imag_parts_amplified = np.array([val.imag for val in rotated_amplified_zeta_values])

# Separate real and imaginary parts for 1 - s = 0.5 - it
rotated_real_parts_reflected = np.array([val.real for val in rotated_reflected_zeta_values])
rotated_imag_parts_reflected = np.array([val.imag for val in rotated_reflected_zeta_values])

# Plot the real and imaginary parts of the amplified full zeta function (s) and its reflection (1 - s)
plt.figure(figsize=(10, 6))
plt.plot(t_values, rotated_real_parts_amplified, label=f"Real Part (s = 0.5 + it)", color='red')
plt.plot(t_values, rotated_imag_parts_amplified, label=f"Imaginary Part (s = 0.5 + it)", color='blue')
plt.plot(t_values, rotated_real_parts_reflected, label=f"Real Part (1 - s = 0.5 - it)", color='green', linestyle='dashed')
plt.plot(t_values, rotated_imag_parts_reflected, label=f"Imaginary Part (1 - s = 0.5 - it)", color='purple', linestyle='dashed')

plt.title(f"Reflection of Full Zeta Function: s = 0.5 + it vs 1 - s = 0.5 - it (Gain = {gain_factor})")
plt.xlabel("t (Imaginary part of s = 0.5 + it)")
plt.ylabel("Value (Rotated & Amplified)")
plt.legend()
plt.grid(True)
plt.show()
