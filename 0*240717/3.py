import math, cmath

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpmath import zeta, gamma, cos, pi, mp


# Set precision
mp.dps = 25

# Custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t)) * cmath.exp(1j*math.pi/4)# * zeta(s_conjugate)

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = [zeta_symbolic(t) for t in t_values]

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)
dif        = np.where(np.abs(real_parts-imag_parts) < 0.01)
amplitude  = np.sqrt(real_parts**2 + imag_parts**2)

# Create a 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the representation
A = amplitude
theta = t_values * 1/(2*math.pi)
r = A
z_real = real_parts
z_imag = imag_parts


# Plot the wave function
ax.plot(theta, r, z_imag, label='Im', color='green')
ax.plot(theta, r, z_real, label='Re', color='blue')
ax.scatter(theta, np.where(WHATEVER < 0.1), color='red')


# Find where the difference changes sign (crossing points)


print(dif)
# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('√Amplitude')
ax.set_zlabel('√Amplitude')
ax.set_title('3D Visualization of Custom Zeta Function as Wavefunction')

# Add legend
ax.legend()

# Show plot
plt.show()
