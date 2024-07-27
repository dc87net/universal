import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpmath import mp, cos, sinh, cosh, pi, gamma

# Set precision
mp.dps = 25

# Custom symbolic zeta function method with approximation
def custom_zeta(s, terms=1000):
    return sum([1/mp.power(n, s) for n in range(1, terms)])

def zeta_symbolic(t, terms=1000):
    s = mp.mpc(0.5, t)
    s_conjugate = mp.mpc(0.5, -t)
    return (mp.power(2, mp.mpf(0.5) - 1j*t) * mp.power(pi, -(mp.mpf(0.5) + 1j*t)) * cosh(pi * (mp.mpf(0.5) + 1j*t) / 2) *
            gamma(mp.mpf(0.5) + 1j*t) * custom_zeta(s_conjugate, terms))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values with a limited number of terms for convergence
terms = 1000  # Adjust the number of terms as needed for convergence
zeta_vals = [zeta_symbolic(t, terms) for t in t_values]

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)
amplitude = np.sqrt(real_parts**2 + imag_parts**2)

# Identify zeros (where both real and imaginary parts are close to zero)
epsilon = 1e-6  # Small threshold to identify zeros
zeros = [(0.5, t) for t, r, i in zip(t_values, real_parts, imag_parts) if abs(r) < epsilon and abs(i) < epsilon]
zeros_real = [zero[0] for zero in zeros]
zeros_imag = [zero[1] for zero in zeros]

# Create a 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Convert to polar coordinates
theta = t_values
r = amplitude
z_real = real_parts
z_imag = imag_parts

# Plot the real part of the wave function in polar coordinates
ax.plot(theta, r, z_real, label='Real Part', color='blue')

# Plot the imaginary part of the wave function in polar coordinates
ax.plot(theta, r, z_imag, label='Imaginary Part', color='green')

# Highlight the zeros
ax.scatter(zeros_imag, [0] * len(zeros_imag), zs=0, zdir='z', color='red', label='Zeros', depthshade=True)

# Add the critical sphere
# Calculate the critical radius
critical_radius = np.mean(amplitude)

# Create a sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = critical_radius * np.outer(np.cos(u), np.sin(v))
y = critical_radius * np.outer(np.sin(u), np.sin(v))
z = critical_radius * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the critical sphere
ax.plot_surface(x, y, z, color='red', alpha=0.3)

# Customize the axes labels and title
ax.set_xlabel('Theta (t)')
ax.set_ylabel('Radius (r)')
ax.set_zlabel('Amplitude')
ax.set_title('3D Radial Visualization of Custom Zeta Function with Hyperbolic Trig Functions')

# Add legend
ax.legend()

# Show plot
plt.show()

# Visualize prime number distribution approximation
x_values = np.arange(2, 1000)
pi_x = [len([p for p in range(2, int(x) + 1) if all(p % d != 0 for d in range(2, int(np.sqrt(p)) + 1))]) for x in x_values]
pi_x_approx = [x / np.log(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, pi_x, label='Prime Count $pi(x)$')
plt.plot(x_values, pi_x_approx, label='Prime Number Theorem Approximation $x/log(x)$', linestyle='--')
plt.xlabel('x')
plt.ylabel('Number of Primes $pi(x)$')
plt.title('Prime Number Distribution and Approximation')
plt.legend()
plt.grid(True)
plt.show()