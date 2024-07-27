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
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = [zeta_symbolic(t) for t in t_values]

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)
amplitude = np.sqrt(real_parts**2 + imag_parts**2)

# Create a 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the Hamiltonian representation
H = amplitude
theta = t_values
r = H
z_real = real_parts
z_imag = imag_parts

# Plot the real part of the wave function in the Hamiltonian representation
ax.plot(theta, r, z_real, label='Real Part', color='blue')

# Plot the imaginary part of the wave function in the Hamiltonian representation
ax.plot(theta, r, z_imag, label='Imaginary Part', color='green')

# Customize the axes labels and title
ax.set_xlabel('Theta (t)')
ax.set_ylabel('Hamiltonian (H)')
ax.set_zlabel('Amplitude')
ax.set_title('3D Visualization of Custom Zeta Function in Hamiltonian Representation')

# Add legend
ax.legend()

# Show plot
plt.show()