import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# Define the Riemann zeta function using primitive operations
def eta(s, N_terms):
    """
    Compute the Dirichlet eta function η(s) = Σ [(-1)^(n-1)] / n^s for n=1 to N_terms.
    """
    n = np.arange(1, N_terms + 1)
    terms = ((-1) ** (n - 1)) / n ** s
    return np.sum(terms)

def zeta(s, N_terms=1000):
    """
    Compute the Riemann zeta function ζ(s) using the Dirichlet eta function:
    ζ(s) = η(s) / (1 - 2^(1 - s))
    """
    numerator = eta(s, N_terms)
    denominator = 1 - 2 ** (1 - s)
    return numerator / denominator

def compute_zeta_values(t_values, N_terms=1000):
    """
    Compute ζ(0.5 + it) for an array of t values.
    """
    s_values = 0.5 + 1j * t_values
    zeta_vals = np.array([zeta(s, N_terms) for s in s_values])
    return zeta_vals

# Define the range for the imaginary part of s
t_values = np.linspace(0, 100, 10**4)  # 10,000 points
delta_t = t_values[1] - t_values[0]     # 0.01

# Number of terms in the series (adjust for accuracy)
N_terms = 1000

# Compute ζ(s) for each t in t_values
zeta_vals = compute_zeta_values(t_values, N_terms)
zeta_valsC = np.conjugate(zeta_vals)      # ζ(s)*

# Compute |ζ(s)|^2
zeta_mod_squared = np.abs(zeta_vals) ** 2

# Define theta with scaling
theta = t_values / (2 * math.pi)         # θ = t / (2π)
delta_theta = delta_t / (2 * math.pi)   # Δθ = Δt / (2π)

# Extract real and imaginary parts
real_parts = zeta_vals.real
imag_parts = zeta_vals.imag

real_partsC = zeta_valsC.real
imag_partsC = zeta_valsC.imag

# Compute where the real and imaginary parts are close to each other (within tolerance)
tolerance = 0.05
dif = np.abs(real_parts - imag_parts) < tolerance
difC = np.abs(real_partsC - imag_partsC) < tolerance

# Compute amplitude |ζ(s)|
amplitude = np.abs(zeta_vals)
amplitudeC = np.abs(zeta_valsC)
amplitudeT = zeta_mod_squared

# **Normalization Step**
# Compute the sum of |ζ(s)|^2 * Δθ
sum_amplitude_squared = np.sum(zeta_mod_squared) * delta_theta

# Calculate scaling factor to normalize the wavefunction
scaling_factor = 1 / math.sqrt(sum_amplitude_squared)  # Ensures sum(|ψ|^2 * Δθ) = 1

# Apply scaling to amplitudes and real/imag parts
amplitude *= scaling_factor
amplitudeC *= scaling_factor
amplitudeT *= scaling_factor

real_parts_scaled = real_parts * scaling_factor
imag_parts_scaled = imag_parts * scaling_factor
real_partsC_scaled = real_partsC * scaling_factor
imag_partsC_scaled = imag_partsC * scaling_factor

# **Rotation by e^(iπ/4)**
rotation_factor = cmath.exp(1j * math.pi / 4)
rotated_zeta_vals = zeta_vals * rotation_factor
rotated_zeta_valsC = zeta_valsC * np.conjugate(rotation_factor)

# Extract real and imaginary parts of the rotated values
rotated_real_parts = rotated_zeta_vals.real * scaling_factor
rotated_imag_parts = rotated_zeta_vals.imag * scaling_factor

rotated_real_partsC = rotated_zeta_valsC.real * scaling_factor
rotated_imag_partsC = rotated_zeta_valsC.imag * scaling_factor

# Identify intersection points where Re(zeta) ≈ Im(zeta)
intersections = np.where(dif)
intersectionsC = np.where(difC)

# Extract data at intersection points
theta_intersections = theta[intersections]
amplitude_intersections = amplitude[intersections]
z_real_intersections = real_parts_scaled[intersections]

theta_intersectionsC = theta[intersectionsC]                 e
amplitude_intersectionsC = amplitudeC[intersectionsC]
z_realC_intersections = real_partsC_scaled[intersectionsC]

# Rotated values at intersection points
rotated_real_intersections = rotated_real_parts[intersections]
rotated_realC_intersections = rotated_real_partsC[intersectionsC]

# **Visualization**

# 1. 3D Plot of the Wavefunction Components
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot Real and Imaginary Parts
ax.plot(theta, amplitude, imag_parts_scaled, label='Imaginary Part', color='green', alpha=0.6)
ax.plot(theta, amplitude, real_parts_scaled, label='Real Part', color='red', alpha=0.6)

# Plot Conjugate Real and Imaginary Parts
ax.plot(theta, amplitudeC, imag_partsC_scaled, label='Imaginary Conj', color='blue', alpha=0.6)
ax.plot(theta, amplitudeC, real_partsC_scaled, label='Real Conj', color='orange', alpha=0.6)

# Plot |ζ(s)|^2 Components
ax.plot(theta, amplitudeT, real_parts_scaled, label='|ζ(s)|^2 Real', color='black', alpha=0.8)
ax.plot(theta, amplitudeT, imag_parts_scaled, label='|ζ(s)|^2 Imag', color='violet', alpha=0.8)

# Scatter Plot for Intersection Points
ax.scatter(theta_intersections, amplitude_intersections, z_real_intersections, color='red', label='Intersections')
ax.scatter(theta_intersectionsC, amplitude_intersectionsC, z_realC_intersections, color='blue', label='Intersections Cx')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Real/Imaginary Values')
ax.set_title('3D Visualization of Riemann Zeta Function as Wavefunction')

# Add legend
ax.legend()

# Show plot
plt.show()

# 2. Plot Rotated Real Parts at Intersection Points vs t-values
plt.figure(figsize=(10, 6))
plt.plot(t_values[intersections], rotated_real_intersections, 'o', color='orange', label='Rotated Real Parts')
plt.plot(t_values[intersectionsC], rotated_realC_intersections, 'x', color='blue', label='Rotated Real* Parts')

# Calculate magnitudes for additional insight
# Ensure that the lengths match by taking the minimum number of points
min_length = min(len(rotated_real_intersections), len(rotated_realC_intersections))
magnitudes = np.abs(rotated_realC_intersections[:min_length]**2 + rotated_real_intersections[:min_length]**2)
plt.plot(np.sqrt(t_values[intersectionsC][:min_length]**2 + t_values[intersections][:min_length]**2),
         magnitudes,
         '*', color='blue', label='Magnitudes')

plt.xlabel('t-values')
plt.ylabel('Rotated Real Part')
plt.title('Rotated Real Parts at Intersection Points vs t-values')
plt.legend()
plt.grid(True)
plt.show()

# 3. 3D Plot of Rotated Intersections Projected onto Re Axis
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the original wave function (less opaque for emphasis on projected points)
ax.plot(theta, amplitude, imag_parts_scaled, label='Imaginary Part', color='green', alpha=0.5)
ax.plot(theta, amplitude, real_parts_scaled, label='Real Part', color='blue', alpha=0.5)

# Plot the rotated real parts projected onto the Re axis
ax.scatter(theta_intersections, amplitude_intersections, rotated_real_intersections, color='red', label='Rotated Intersections (Projected)')

# Plot the rotated real* parts projected onto the Re axis
ax.scatter(theta_intersectionsC, amplitude_intersectionsC, rotated_realC_intersections, color='cyan', label='Rotated Intersections Cx (Projected)')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Rotated Real Values')
ax.set_title('Rotated Intersections Projected onto Re Axis')

# Add legend
ax.legend()

# Show plot
plt.show()

# **Save Data for Further Analysis**
np.savetxt("4TCrossings.txt", t_values[intersections], fmt='%.8f')
np.savetxt("rotatedReal.txt", rotated_real_intersections, fmt='%.8f')
np.savetxt("rotatedImag.txt", rotated_realC_intersections, fmt='%.8f')  # Adjusted to match 'rotatedRealC_intersections'
np.savetxt("zeroes.txt", t_values, fmt='%.8f')

# **Print Rotated Parts**
print(f"\nREAL ROTATED\n{rotated_real_intersections}")
print(f"\nREAL* ROTATED\n{rotated_realC_intersections}")

# **Verification of Normalization**
sum_amplitude_squared_scaled = np.sum(amplitude**2) * delta_theta
print(f"\nNormalization Sum (should be ~1): {sum_amplitude_squared_scaled}")
