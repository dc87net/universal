import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, mp

# Set decimal places of precision
mp.dps = 15

# Define the range for theta (t)
theta = np.linspace(0, 50, 500)

# Define the custom zeta function using mpmath for complex numbers
def custom_zeta_function(theta):
    s = 0.5 + 1j * theta
    zeta_values = np.array([zeta(complex(val)) for val in s], dtype=np.complex128)
    return np.real(zeta_values), np.imag(zeta_values)

# Get real and imaginary parts of the zeta function
real_part, imaginary_part = custom_zeta_function(theta)

# Calculate the phase and frequency components
phase = np.arctan2(imaginary_part, real_part)
frequency = np.gradient(phase, theta)

# Plot phase and frequency
plt.figure()
plt.plot(theta, phase, label='Phase')
plt.xlabel('Theta')
plt.ylabel('Phase (radians)')
plt.legend()
plt.title('Phase of the Zeta Function')
plt.show()

plt.figure()
plt.plot(theta, frequency, label='Frequency')
plt.xlabel('Theta')
plt.ylabel('Frequency')
plt.legend()
plt.title('Frequency of the Zeta Function')
plt.show()
