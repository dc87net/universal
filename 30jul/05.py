import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, mp

# Ensure high precision calculations
mp.dps = 15  # Set decimal places of precision

# Define the range for theta (t)
theta = np.linspace(0, 50, 500)

# Define the custom zeta function using mpmath for complex numbers
def custom_zeta_function(theta):
    s = 0.5 + 1j * theta
    zeta_values = np.array([zeta(complex(val)) for val in s], dtype=np.complex128)
    return np.real(zeta_values), np.imag(zeta_values)

# Define a hypothetical Hamiltonian for demonstration
def hamiltonian(real_part, imaginary_part):
    # A simple example, where the Hamiltonian is proportional to the modulus squared of the zeta function
    H_real = real_part**2 - imaginary_part**2
    H_imag = 2 * real_part * imaginary_part
    return H_real, H_imag

# Get real and imaginary parts of the zeta function
real_part, imaginary_part = custom_zeta_function(theta)

# Get real and imaginary parts of the Hamiltonian
H_real, H_imag = hamiltonian(real_part, imaginary_part)

# Plot the 3D visualization with Hamiltonian and zeta function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(real_part, H_real, theta, label='Real Part', color='b')
ax.plot(imaginary_part, H_imag, theta, label='Imaginary Part', color='g')
ax.set_xlabel('Zeta Real Part')
ax.set_ylabel('Hamiltonian')
ax.set_zlabel('Theta (t)')
ax.legend()
plt.title('30jul-05 3D Visualization of Custom Zeta Function and Hamiltonian')
plt.show()

# Convert to radial coordinates for polar plot
radius = np.sqrt(real_part**2 + imaginary_part**2)
angle = np.arctan2(imaginary_part, real_part)

# Plot the radial coordinates in a polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angle, radius, label='Custom Zeta Function')
ax.set_rlabel_position(-22.5)  # Move radial labels away from plot line
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Radius')
ax.legend()
plt.title('Custom Zeta Function in Radial Coordinates')
plt.show()

# Plot the eigenvalues (assumed linear for demonstration)
eigenvalues = np.linspace(0, 50, 500)
plt.figure()
plt.plot(eigenvalues, np.zeros_like(eigenvalues), 'r.', label='Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Eigenvalue')
plt.legend()
plt.title('Linear Distribution of Eigenvalues')
plt.show()
