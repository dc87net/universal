import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import os

# Define the Riemann zeta function using primitive operations
def eta(s, N_terms):
    sum_eta = 0.0 + 0.0j
    for n in range(1, N_terms + 1):
        term = ((-1) ** (n - 1)) / n ** s
        sum_eta += term
    return sum_eta

def zeta(s, N_terms):
    numerator = eta(s, N_terms)
    denominator = 1 - 2 ** (1 - s)
    return numerator / denominator

def zeta_symbolic(t, N_terms=1000):
    s = 0.5 + 1j * t
    return zeta(s, N_terms)

def zeta_symbolicConj(t, N_terms=1000):
    return np.conjugate(zeta_symbolic(t, N_terms))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 100, 10**4)  # 10,000 points
delta_t = t_values[1] - t_values[0]     # 0.01
# Compute symbolic zeta function values
zeta_vals   = [zeta_symbolic(t) for t in t_values]
zeta_valsC = [zeta_symbolicConj(t) for t in t_values]
zeta_valsT = np.pow(np.multiply(zeta_vals,zeta_valsC),1)

# Define theta with scaling
theta = t_values * 1/(2*math.pi)  # Scaling t-values for clearer theta representation
delta_theta = delta_t * 1/(2*math.pi)  # 0.00159155

# Number of terms in the series (adjust for accuracy)
N_terms = 1000

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)

real_partsC = np.array([val.real for val in zeta_valsC], dtype=float)
imag_partsC = np.array([val.imag for val in zeta_valsC], dtype=float)

real_partsT = np.array([val.real for val in zeta_valsT], dtype=float)
imag_partsT = np.array([val.imag for val in zeta_valsT], dtype=float)

# Compute symbolic zeta function values
zeta_vals = np.array([zeta_symbolic(t, N_terms) for t in t_values])
zeta_valsC = np.conjugate(zeta_vals)
zeta_valsT = zeta_vals * zeta_valsC  # |ζ(s)|^2

# Extract real and imaginary parts
z_real = real_parts; z_realC = real_partsC
z_imag = imag_parts; z_imagC = imag_partsC

real_partsC = zeta_valsC.real
imag_partsC = zeta_valsC.imag

real_partsT = zeta_valsT.real
imag_partsT = zeta_valsT.imag

# Compute where the real and imaginary parts are close to each other (within tolerance)
tolerance = 0.05
dif = np.where(np.abs(real_parts - imag_parts) < tolerance)
difC = np.where(np.abs(real_partsC - imag_partsC) < tolerance)
difT = np.where(np.abs(real_partsT - imag_partsT) < tolerance)

# Compute amplitude
amplitude = np.abs(zeta_vals)
amplitudeC = np.abs(zeta_valsC)
amplitudeT = np.abs(zeta_valsT)

# **Normalization Step**
# Compute the sum of |ζ(s)|^2 * delta_theta
sum_amplitude_squared = np.sum(amplitude**2) * delta_theta

# Calculate scaling factor to normalize the wavefunction
scaling_factor = 1 / math.sqrt(sum_amplitude_squared)  # Ensures sum(|ψ|^2 * delta_theta) = 1

# Apply scaling
amplitude *= scaling_factor
amplitudeC *= scaling_factor
amplitudeT *= scaling_factor

# Now, sum(|amplitude|^2) * delta_theta ≈ 1

# Create a 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the representation
r = amplitude  # Since amplitude is scaled, r = amplitude
z_real = real_parts * scaling_factor
z_imag = imag_parts * scaling_factor

# Plot the wave function (real and imaginary parts)
ax.plot(theta, r, z_imag, label='Imaginary Part', color='green', alpha=0.6)
ax.plot(theta, r, z_real, label='Real Part', color='red', alpha=0.6)
ax.plot(theta, amplitudeC, z_imagC, label='Imaginary Conj', color='blue', alpha=0.6)
ax.plot(theta, amplitudeC, z_realC, label='Real Conj', color='orange', alpha=0.6)
ax.plot(theta, amplitudeT, real_partsT * scaling_factor, label='Tr', color='black', alpha=0.8)
ax.plot(theta, amplitudeT, imag_partsT * scaling_factor, label='Ti', color='violet', alpha=0.8)

# Scatter plot for intersections where real and imaginary parts are close
ax.scatter(theta[dif], r[dif], z_real[dif], color='red', label='Intersections')
ax.scatter(theta[difC], amplitudeC[difC], z_realC[difC], color='blue', label='Intersections Cx')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Real/Imaginary Values')
ax.set_title('3D Visualization of Riemann Zeta Function as Wavefunction')

# Add legend
ax.legend()

# Show plot
plt.show()

# Print the crossing points for inspection
print("Crossing points (indices where Re and Im are close):", dif)

# Perform the rotation on the intersection points
indices = dif[0]
indicesC = difC[0]
rotated_vals_dif = zeta_vals[indices] * cmath.exp(-1j * math.pi / 4)
rotated_vals_difC = zeta_valsC[indicesC] * cmath.exp(-1j * math.pi / 4)

# Extract real and imaginary parts of the rotated values
rotated_real_parts_dif = rotated_vals_dif.real * scaling_factor
rotated_imag_parts_dif = rotated_vals_dif.imag * scaling_factor

rotated_real_parts_difC = rotated_vals_difC.real * scaling_factor
rotated_imag_parts_difC = rotated_vals_difC.imag * scaling_factor

# t-values at the intersection points
t_crossings = t_values[indices]
t_crossingsC = t_values[indicesC]

# Plot the rotated real parts against t-values to keep track of where they are
plt.figure(figsize=(10, 6))
plt.plot(t_crossings, rotated_real_parts_dif, 'o', color='orange', label='Rotated R Parts')
plt.plot(t_crossingsC, rotated_real_parts_difC, 'x', color='blue', label='Rotated R* Parts')

# Calculate magnitudes using np.abs for complex numbers
magnitudes = np.abs(rotated_real_parts_difC[:len(t_crossings)]**2 + rotated_real_parts_dif[:len(t_crossings)]**2)
plt.plot(np.sqrt(t_crossingsC[:len(t_crossings)]**2 + t_crossings[:len(t_crossings)]**2),
         magnitudes,
         '*', color='blue', label='Rotated R* Parts')

plt.xlabel('t-values')
plt.ylabel('Rotated Real Part')
plt.title('Rotated Real Parts at Intersection Points vs t-values')
plt.legend()
plt.grid(True)
plt.show()

# Project the rotated points onto the Re axis in the 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the original wave function (less opaque for emphasis on projected points)
ax.plot(theta, r, z_imag, label='Imaginary Part', color='green', alpha=0.5)
ax.plot(theta, r, z_real, label='Real Part', color='blue', alpha=0.5)

# Plot the rotated real parts projected onto the Re axis
theta_crossings = theta[indices]
r_crossings = r[indices]  # Use scaled amplitude for consistency
ax.scatter(theta_crossings, r_crossings, rotated_real_parts_dif, color='red', label='Rotated Intersections (Projected)')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Rotated Real Values')
ax.set_title('Rotated Intersections Projected onto Re Axis')

# Add legend
ax.legend()

# Show plot
plt.show()

# Save data for further analysis
np.savetxt("4TCrossings.txt", t_crossings, fmt='%.8f')
np.savetxt("rotatedReal.txt", rotated_real_parts_dif, fmt='%.8f')
np.savetxt("rotatedImag.txt", rotated_imag_parts_dif, fmt='%.8f')
np.savetxt("zeroes.txt", t_values, fmt='%.8f')

print(f"\nREAL ROTATED\n{rotated_real_parts_dif}")
print(f"\nREAL* ROTATED\n{rotated_real_parts_difC}")
