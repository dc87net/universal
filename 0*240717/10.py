import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function for the cosine term
def cos_term(t):
    return np.cos(np.pi * (0.5 + t) / 2)


# Define hyperbolic coordinates (use sinh and cosh to stretch out the space)
def hyperbolic_wave(t):
    # Radial component using the magnitude of the cosine term
    r = np.abs(cos_term(t))

    # Apply hyperbolic transformation
    theta = np.sinh(t)  # Stretch in one direction
    phi = np.cosh(t)  # Stretch in the other direction

    return r, theta, phi


# Define the range of t values (WIDENED range to capture more zeros)
t_values = np.linspace(0, 100, 5000)  # Larger range for better coverage

# Compute hyperbolic coordinates
r, theta, phi = hyperbolic_wave(t_values)

# Convert hyperbolic to Cartesian coordinates for 3D plotting
x = r * theta
y = r * phi
z = np.log(r)  # Use log to stretch out the structure

# Create a 3D plot to show the function in hyperbolic coordinates
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the hyperbolic wave-like behavior using Cartesian coordinates
ax.plot3D(x, y, z, label="Hyperbolic Wave", color="blue")

# Improve zero crossing detection by relaxing tolerance slightly
tolerance = 1e-2  # Relaxed tolerance
zero_crossings = np.where(np.abs(r) < tolerance)[0]  # Points where the wave collapses

# Highlight the zero crossings (to identify layer transitions)
ax.scatter(x[zero_crossings], y[zero_crossings], z[zero_crossings], color="red", s=50, label="Zeros")

# Add labels and title
ax.set_title("Wave Function in Hyperbolic Coordinates")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.legend()
plt.show()

# Print the first few zero values for inspection
print(f"First few zeros (layer transitions) occur at t = {t_values[zero_crossings[:10]]}")

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function for the cosine term
def cos_term(t):
    return np.cos(np.pi * (0.5 + t) / 2)


# Define spherical coordinates with layering and smoother transitions
def spherical_wave(t):
    # Magnitude of the cosine term as r (account for layering)
    r = np.abs(cos_term(t))  # Radial magnitude from cosine
    theta = np.angle(cos_term(t))  # Polar angle (phase)

    # Use a non-linear mapping for phi to account for layers
    phi = t * np.sin(theta)  # Azimuthal angle reflecting oscillation and layer transitions

    return r, theta, phi


# Define the range of t values
t_values = np.linspace(0, 40, 1000)  # Extend to include multiple oscillations and layers

# Compute spherical coordinates for the wave behavior
r, theta, phi = spherical_wave(t_values)

# Convert spherical to Cartesian coordinates
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Create a 3D plot to show the function in spherical coordinates with layers
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the layered wave-like behavior using Cartesian coordinates
ax.plot3D(x, y, z, label="Layered Wave in Spherical Coordinates", color="blue")

# Highlight the zero crossings to identify layers
zero_crossings = np.where(np.abs(r) < 1e-3)[0]  # Points where the wave collapses
ax.scatter(x[zero_crossings], y[zero_crossings], z[zero_crossings], color="red", s=50,
           label="Zeros (Layer Transitions)")

# Add labels and title
ax.set_title("Layered Oscillating Wave Function in Spherical Coordinates")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.legend()
plt.show()

# Print the first few zero values for inspection
print(f"First few zeros (layer transitions) occur at t = {t_values[zero_crossings[:5]]}")

import numpy as np
import matplotlib.pyplot as plt


# Define the function for the cosine term
def cos_term(t):
    return np.cos(np.pi * (0.5 + t) / 2)


# Define hyperbolic coordinates (use sinh and cosh to stretch out the space)
def hyperbolic_wave(t):
    # Radial component using the magnitude of the cosine term
    r = np.abs(cos_term(t))

    # Apply hyperbolic transformation
    theta = np.sinh(t)  # Stretch in one direction
    phi = np.cosh(t)  # Stretch in the other direction

    return r, theta, phi


# Define the range of t values (WIDENED range to capture more zeros)
t_values = np.linspace(0, 100, 5000)  # Larger range for better coverage

# Compute hyperbolic coordinates
r, theta, phi = hyperbolic_wave(t_values)

# --- Step 1: Extract Zero Crossings ---
# Improve zero crossing detection by relaxing tolerance slightly
tolerance = 1e-2  # Relaxed tolerance
zero_crossings = np.where(np.abs(r) < tolerance)[0]  # Points where the wave collapses

# Extract the zero points
x_zeros = theta[zero_crossings]
y_zeros = phi[zero_crossings]
z_zeros = np.log(r[zero_crossings])

# --- Step 2: Project Zeros Using Contour Integral and Roots of Unity ---
# Define the contour and map these to roots of unity
roots_of_unity = np.exp(2j * np.pi * np.arange(len(zero_crossings)) / len(zero_crossings))

# Define the projection onto the real plane (using symmetry and scale invariance)
projected_zeros = np.real(roots_of_unity)  # Real projection onto the real plane

# Scale the projected zeros
scale_factor = np.max(t_values[zero_crossings])  # Adjust based on the scale of t-values
projected_zeros *= scale_factor

# --- Step 3: Plot the Projected Zeros on the Real Plane ---
plt.figure(figsize=(8, 6))
plt.scatter(projected_zeros, np.zeros_like(projected_zeros), color='red', label='Projected Zeros on Real Plane')
print(f"Projected Zeroes: {projected_zeros}")

# Add labels and title
plt.title("Projected Zeros Mapped to the Real Plane")
plt.xlabel("Real Values")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

# Print the projected zero values for inspection
print(f"Projected zeros on the real plane: {projected_zeros}")
