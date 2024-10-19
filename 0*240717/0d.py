import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

# Create a grid of complex values for z
real_vals = np.linspace(-5, 5, 400)
imag_vals = np.linspace(-5, 5, 400)
z_real, z_imag = np.meshgrid(real_vals, imag_vals)
z = z_real + 1j * z_imag

# Calculate 2^(z_conjugate) * π^(-z)
z_conjugate = np.conjugate(z)
expression_1 = 2**z_conjugate * np.pi**-z

# Calculate the same expression multiplied by gamma(z)
expression_2 = expression_1 * gamma(z)

# Calculate the magnitudes of both expressions
mag_expression_1 = np.abs(expression_1)
mag_expression_2 = np.abs(expression_2)

# Plot the two expressions
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Plot |2^(z_conjugate) * π^(-z)|
c1 = axs[0].contourf(z_real, z_imag, mag_expression_1, levels=50, cmap='viridis')
axs[0].set_title('|2^(z_conjugate) * π^(-z)|')
axs[0].set_xlabel('Re(z)')
axs[0].set_ylabel('Im(z)')
fig.colorbar(c1, ax=axs[0])

# Plot |2^(z_conjugate) * π^(-z) * gamma(z)|
c2 = axs[1].contourf(z_real, z_imag, mag_expression_2, levels=50, cmap='plasma')
axs[1].set_title('|2^(z_conjugate) * π^(-z) * gamma(z)|')
axs[1].set_xlabel('Re(z)')
axs[1].set_ylabel('Im(z)')
fig.colorbar(c2, ax=axs[1])

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

# Create a grid of complex values for z
real_vals = np.linspace(-5, 5, 400)
imag_vals = np.linspace(-5, 5, 400)
z_real, z_imag = np.meshgrid(real_vals, imag_vals)
z = z_real + 1j * z_imag

# Calculate 2^(z_conjugate) * π^(-z)
z_conjugate = np.conjugate(z)
expression_1 = 2**z_conjugate * np.pi**-z

# Calculate the same expression multiplied by gamma(z)
expression_2 = expression_1 * gamma(z)

# Calculate the third expression: 2^(z_conjugate) * π^(-z) * gamma(z) * sin(πz/2)
expression_3 = expression_2 * np.sin(np.pi * z / 2)

# Calculate the magnitudes of all three expressions
mag_expression_1 = np.abs(expression_1)
mag_expression_2 = np.abs(expression_2)
mag_expression_3 = np.abs(expression_3)

# Plot all three expressions
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot |2^(z_conjugate) * π^(-z)|
c1 = axs[0].contourf(z_real, z_imag, mag_expression_1, levels=50, cmap='viridis')
axs[0].set_title('|2^(z_conjugate) * π^(-z)|')
axs[0].set_xlabel('Re(z)')
axs[0].set_ylabel('Im(z)')
fig.colorbar(c1, ax=axs[0])

# Plot |2^(z_conjugate) * π^(-z) * gamma(z)|
c2 = axs[1].contourf(z_real, z_imag, mag_expression_2, levels=50, cmap='plasma')
axs[1].set_title('|2^(z_conjugate) * π^(-z) * gamma(z)|')
axs[1].set_xlabel('Re(z)')
axs[1].set_ylabel('Im(z)')
fig.colorbar(c2, ax=axs[1])

# Plot |2^(z_conjugate) * π^(-z) * gamma(z) * sin(πz/2)|
c3 = axs[2].contourf(z_real, z_imag, mag_expression_3, levels=50, cmap='inferno')
axs[2].set_title('|2^(z_conjugate) * π^(-z) * gamma(z) * sin(πz/2)|')
axs[2].set_xlabel('Re(z)')
axs[2].set_ylabel('Im(z)')
fig.colorbar(c3, ax=axs[2])

plt.tight_layout()
plt.show()



# Let's apply the rotation e^(i*pi/4) to each of the expressions

# Rotation factor e^(i*pi/4)
rotation_factor = np.exp(1j * np.pi / 4)

# Apply the rotation to each expression
expression_1_rotated = expression_1 * rotation_factor
expression_2_rotated = expression_2 * rotation_factor
expression_3_rotated = expression_3 * rotation_factor

# Calculate the magnitudes of the rotated expressions
mag_expression_1_rotated = np.abs(expression_1_rotated)
mag_expression_2_rotated = np.abs(expression_2_rotated)
mag_expression_3_rotated = np.abs(expression_3_rotated)

# Plot the rotated expressions
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot |2^(z_conjugate) * π^(-z)| rotated
c1_rotated = axs[0].contourf(z_real, z_imag, mag_expression_1_rotated, levels=50, cmap='viridis')
axs[0].set_title('|2^(z_conjugate) * π^(-z)| Rotated by e^(iπ/4)')
axs[0].set_xlabel('Re(z)')
axs[0].set_ylabel('Im(z)')
fig.colorbar(c1_rotated, ax=axs[0])

# Plot |2^(z_conjugate) * π^(-z) * gamma(z)| rotated
c2_rotated = axs[1].contourf(z_real, z_imag, mag_expression_2_rotated, levels=50, cmap='plasma')
axs[1].set_title('|2^(z_conjugate) * π^(-z) * gamma(z)| Rotated by e^(iπ/4)')
axs[1].set_xlabel('Re(z)')
axs[1].set_ylabel('Im(z)')
fig.colorbar(c2_rotated, ax=axs[1])

# Plot |2^(z_conjugate) * π^(-z) * gamma(z) * sin(πz/2)| rotated
c3_rotated = axs[2].contourf(z_real, z_imag, mag_expression_3_rotated, levels=50, cmap='inferno')
axs[2].set_title('|2^(z_conjugate) * π^(-z) * gamma(z) * sin(πz/2)| Rotated by e^(iπ/4)')
axs[2].set_xlabel('Re(z)')
axs[2].set_ylabel('Im(z)')
fig.colorbar(c3_rotated, ax=axs[2])

plt.tight_layout()
plt.show()

# import ace_tools as tools; tools.display_matplotlib_to_user(fig, "Rotated Expressions by e^(iπ/4)")
