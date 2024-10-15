import numpy as np
import matplotlib.pyplot as plt


# Define the scalar curvature as a function of theta and omega
def scalar_curvature(theta, omega):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    numerator = (-128 * sin_theta ** 4 + 128 * sin_theta ** 2 - 16) * (
                omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 2 + \
                (
                            -768 * omega ** 2 - 12288 * sin_theta ** 4 + 12288 * sin_theta ** 2 - 3072) * sin_theta ** 2 * cos_theta ** 2 * np.cos(
        2 * theta) ** 2
    denominator = (omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 4

    return numerator / denominator


# Parameters
omega = 8  # Angular frequency
theta_vals = np.linspace(0, 2 * np.pi, 1000)  # Range of theta values

# Compute the scalar curvature for each theta
scalar_curv_vals = scalar_curvature(theta_vals, omega)

# Plot the scalar curvature
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, scalar_curv_vals, label=f'Scalar Curvature (ω = {omega})')
plt.title('Scalar Curvature as a Function of Theta')
plt.xlabel('Theta')
plt.ylabel('Scalar Curvature')
plt.legend()
plt.grid(True)
plt.show()
