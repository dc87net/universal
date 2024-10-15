import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpmath import gamma, cos, pi, mp
import os

from sympy.abc import alpha

# Set precision
mp.dps = 25

# ══ ZETA ══════════════════════════════════════════════════════════════════════

# ══ ZETA ══════════════════════════════════════════════════════════════════════
# Custom symbolic zeta function method corrected along the critical line with the functional equation
def zeta_symbolic(t):
    """
    Computes the Riemann zeta function along the critical line Re(s) = 0.5 using the functional equation.
    """
    s = 0.5 + 1j*t  # s on the critical line
    return (2**s * pi**(s-1) * cmath.sin(pi * s / 2) * gamma(1-s) * cmath.exp(-1j*math.pi/4))

def zeta_symbolicConj(t):
    """
    Computes the conjugate of the Riemann zeta function along the critical line.
    """
    s = 0.5 + 1j*t
    return np.conjugate(zeta_symbolic(t))

# # Custom symbolic zeta function method
# def zeta_symbolic(t):
#     # s = complex(0.5, t)
#     # s_conjugate = complex(0.5, -t)
#     return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cmath.sin(pi * (0.5 + 1j*t) / 2) *
#             gamma(0.5 + 1j*t) * cmath.exp(1j*math.pi/4))
# #
#
# def zeta_symbolicConj(t):
#     # s = complex(0.5, t)
#     # s_conjugate = complex(0.5, -t)
#     return np.conjugate(zeta_symbolic(t))
#     # return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cmath.sin(pi * (0.5 + 1j*t) / 2) *
#     #         gamma(0.5 + 1j*t)) * cmath.exp(-1j*math.pi/4)

# def zeta_symbolicConj(t):
#     s = complex(0.5, t)
#     s_conjugate = complex(0.5, -t)
#     return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cmath.sin(pi * (0.5 + 1j*t) / 2) *
#             gamma(0.5 + 1j*t)) * cmath.exp(-1j*math.pi/4)
 # ═════════════════════════════════════════════════════════════════════════════


# Define the range for the imaginary part of s

t_values = np.linspace(0, 100, 10**4)

# Compute symbolic zeta function values
zeta_vals   = [zeta_symbolic(t) for t in t_values]
zeta_valsC = [zeta_symbolicConj(t) for t in t_values]
zeta_valsT = np.pow(np.multiply(zeta_vals,zeta_valsC),1)


# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)

real_partsC = np.array([val.real for val in zeta_valsC], dtype=float)
imag_partsC = np.array([val.imag for val in zeta_valsC], dtype=float)

real_partsT = np.array([val.real for val in zeta_valsT], dtype=float)
imag_partsT = np.array([val.imag for val in zeta_valsT], dtype=float)



# Compute where the real and imaginary parts are close to each other (within tolerance)
tolerance = 0.05
dif = np.where(np.abs(real_parts - imag_parts) < tolerance)
difC = np.where(np.abs(real_partsC - imag_partsC) < tolerance)
difT = np.where(np.abs(real_partsT - imag_partsT) < tolerance)

# Compute amplitude
amplitude = np.sqrt(real_parts**2 + imag_parts**2)
amplitudeC = np.sqrt(real_partsC**2 + imag_partsC**2)
amplitudeT = np.sqrt(real_partsT**2 + imag_partsT**2)




# Create a 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')


# Define the representation
A = amplitude
theta = t_values * 1/(2*math.pi)  # Scaling t-values for clearer theta representation
r = A
z_real = real_parts; z_realC = real_partsC
z_imag = imag_parts; z_imagC = imag_partsC

# Plot the wave function (real and imaginary parts)
ax.plot(theta, r, z_imag, label='I', color='green', alpha=0.6)
ax.plot(theta, r, z_real, label='R', color='red', alpha=0.6)
ax.plot(theta, amplitudeC, z_imagC, label='I*', color='blue', alpha=0.6)
ax.plot(theta, amplitudeC, z_realC, label='R*', color='orange', alpha=0.6)
ax.plot(theta, amplitudeT, real_partsT, label='Tr', color='black', alpha=0.8)
ax.plot(theta, amplitudeT, imag_partsT, label='Ti', color='violet', alpha=0.8)
# ax.plot((theta, np.dot(amplitudeT,amplitude), label=)
print(np.dot(amplitudeT,amplitude))
print(np.dot(amplitudeT,amplitudeC))
print(np.dot(amplitudeC,amplitude))
print(np.inner(amplitudeT, amplitude))

# Scatter plot for intersections where real and imaginary are close
ax.scatter(theta[dif], r[dif], z_real[dif], color='red', label='Intersections')
ax.scatter(theta[difC], amplitudeC[difC], z_realC[difC], color='blue', label='Intersections Cx')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('√Amplitude')
ax.set_zlabel('Real/Imaginary Values')
ax.set_title('3D Visualization of Custom Zeta Function as Wavefunction')

# Add legend
ax.legend()

# Show plot
plt.show()

# Print the crossing points for inspection
print("Crossing points (indices where Re and Im are close):", dif)

# Perform the rotation on the intersection points
indices = dif[0]
indicesC = difC[0]
rotated_vals_dif = [zeta_vals[i] * cmath.exp(-1j * math.pi / 4) for i in indices]
rotated_vals_difC = [zeta_valsC[i] * cmath.exp(-1j * math.pi / 4) for i in indicesC]

# Extract real and imaginary parts of the rotated values
rotated_real_parts_dif = np.array([val.real for val in rotated_vals_dif], dtype=float)
rotated_imag_parts_dif = np.array([val.imag for val in rotated_vals_dif], dtype=float)

rotated_real_parts_difC = np.array([val.real for val in rotated_vals_difC], dtype=float)
rotated_imag_parts_difC = np.array([val.imag for val in rotated_vals_difC], dtype=float)

# t-values at the intersection points
t_crossings = t_values[indices]
t_crossingsC = t_values[indicesC]


# Plot the rotated real parts against t-values to keep track of where they are
plt.figure(figsize=(10, 6))
plt.plot(t_crossings, rotated_real_parts_dif, 'o', color='orange', label='Rotated R Parts')
plt.plot(t_crossingsC, rotated_real_parts_difC, 'x', color='blue', label='Rotated R* Parts')
# plt.plot(np.sqrt(t_crossingsC**2+t_crossings**2), np.sqrt(rotated_real_parts_difC**2+rotated_vals_dif**2), '*', color='blue', label='Rotated R* Parts')
rotated_real_parts_difC = np.array(rotated_real_parts_difC)
rotated_vals_dif = np.array(rotated_vals_dif)

# Truncate the arrays to the minimum length
minLength = min(len(t_crossingsC), len(t_crossings))
# Ensure arrays are converted to NumPy arrays with the correct complex type
rotated_real_parts_difC = np.array(rotated_real_parts_difC, dtype=np.complex128)
rotated_vals_dif = np.array(rotated_vals_dif, dtype=np.complex128)

# Truncate the arrays to the minimum length
minLength = min(len(t_crossingsC), len(t_crossings))

# Calculate magnitudes using np.abs for complex numbers
plt.plot(np.sqrt(t_crossingsC[:minLength]**2 + t_crossings[:minLength]**2),
         np.abs(rotated_real_parts_difC[:minLength]**2 + rotated_vals_dif[:minLength]**2),
         '*', color='blue', label='Rotated R* Parts')





# plt.plot(t_crossings, rotated_real_parts_dif
print(f"\nREAL ROATATED")
print([t_crossings, rotated_real_parts_dif])
print(f"\nREAL* ROATATED")
print([t_crossingsC, rotated_real_parts_difC])


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

print(t_crossings)
os.system(f"echo '{t_crossings}' > 4TCrossings.txt")

# Plot the rotated real parts projected onto the Re axis
theta_crossings = t_crossings * 1/(2*math.pi)
r_crossings = amplitude[indices]  # Use original amplitude for consistency
ax.scatter(theta_crossings, r_crossings, rotated_real_parts_dif, color='red', label='Rotated Intersections (Projected)')

# Customize the axes labels and title
ax.set_xlabel('Theta')
ax.set_ylabel('√Amplitude')
ax.set_zlabel('Rotated Real Values')
ax.set_title('Rotated Intersections Projected onto Re Axis')

# Add legend
ax.legend()


print(f"Theta:\n\t{theta_crossings}\n\n")
print(f"Intersections:\n\t{r_crossings}\n\n")
print(f"Rotated Diffs:\n\t{rotated_real_parts_dif}\n\n")

print(f"")
# print(f"\n{rotated_real_parts_dif}")
str=f"Drot%\n"
os.system(f"echo '{rotated_real_parts_dif}' > rotatedReal.txt")
str=f"Lrot%\n"
os.system(f"echo '{rotated_imag_parts_dif}' > rotatedImag.txt")

os.system(f"echo '{t_values}' > zeroes.txt")

print(f"\nREAL-R\n{rotated_imag_parts_dif}")
print(f"\nIMAG-R\n{rotated_real_parts_dif}")
print(f"\n")
# a=np.array()

# Show plot
plt.show()

input()
