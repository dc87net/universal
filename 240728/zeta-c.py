import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta

# Define the zeta wave function
def zeta_wave_function(t):
    s = complex(0.5, t)
    return zeta(s)

# Generate data points for the critical line
t_values = np.linspace(0, 40, 1000)  # Theta (t) values

# Calculate the real and imaginary parts
real_parts = np.array([zeta_wave_function(t).real for t in t_values])
imaginary_parts = np.array([zeta_wave_function(t).imag for t in t_values])

# Plot the real and imaginary parts
plt.figure(figsize=(10, 6))
plt.plot(t_values, real_parts, label='Real Part')
plt.plot(t_values, imaginary_parts, label='Imaginary Part')
plt.xlabel('Theta (t)')
plt.ylabel('Amplitude')
plt.title('Real and Imaginary Parts of Zeta Function at the Critical Line')
plt.legend()
plt.grid(True)
plt.show()


# import numpy as np
# import cmath
# from scipy.special import gamma
# from mpmath import zeta
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
#
# # Define the zeta wave function
# def zeta_wave_function(t):
#     s = complex(0.5, t)
#     s_conjugate = complex(0.5, -t)
#
#     # Components based on the functional equation
#     prefactor = 2 ** s * cmath.pi ** (s - 1)
#     sine_term = cmath.sin(cmath.pi * s / 2)
#     gamma_term = gamma(s_conjugate)
#     zeta_term = zeta(s_conjugate)
#
#     # Combine the terms to form the wave function representation
#     return prefactor * sine_term * gamma_term * zeta_term
#
#
# # Generate data points for the radial parametric form
# theta_values = np.linspace(0, 20, 1000)  # Theta (t) values
# radius_values = np.abs(0.5 + 1j * theta_values)  # Radius (r) as the magnitude of s
# amplitude_values = np.array([np.abs(zeta_wave_function(t)) for t in theta_values])  # Amplitude
#
# # Plot the data
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(theta_values, radius_values, amplitude_values)
#
# # Set the labels
# ax.set_xlabel('Theta (t)')
# ax.set_ylabel('Radius (r)')
# ax.set_zlabel('Amplitude')
#
# plt.show()


# import cmath
# from scipy.special import gamma
# from mpmath import zeta
#
#
# def zeta_wave_function(t):
#     s = complex(0.5, t)
#     s_conjugate = complex(0.5, -t)
#
#     # Components based on the functional equation
#     prefactor = 2 ** s * cmath.pi ** (s - 1)
#     sine_term = cmath.sin(cmath.pi * s / 2)
#     gamma_term = gamma(s_conjugate)
#     zeta_term = zeta(s_conjugate)
#
#     # Combine the terms to form the wave function representation
#     return prefactor * sine_term * gamma_term * zeta_term
#
