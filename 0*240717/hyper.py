import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, cosh, pi, gamma, mpc

# Set precision
mp.dps = 25

# Symbolic zeta function with hyperbolic trig functions
def zeta_symbolic(t, terms=1000):
    s = mpc(0.5, t)
    s_conjugate = mpc(0.5, -t)
    return (mp.power(2, mp.mpf(0.5) - 1j*t) * mp.power(pi, -(mp.mpf(0.5) + 1j*t)) * cosh(pi * (mp.mpf(0.5) + 1j*t) / 2) *
            gamma(mp.mpf(0.5) + 1j*t) * sum([1/mp.power(n, s_conjugate) for n in range(1, terms)]))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
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

# Customize the axes labels and title
ax.set_xlabel('Theta (t)')
ax.set_ylabel('Radius (r)')
ax.set_zlabel('Amplitude')
ax.set_title('3D Radial Visualization of Custom Zeta Function with Hyperbolic Trig Functions')

# Add legend
ax.legend()

# Show plot
plt.show()

# Generate primes based on the zeros identified
def generate_primes_from_zeros(zero_t_values):
    # Use a simple check to identify potential primes
    potential_primes = []
    for t in zero_t_values:
        candidate = int(t)
        if candidate > 1:
            is_prime = all(candidate % d != 0 for d in range(2, int(np.sqrt(candidate)) + 1))
            if is_prime:
                potential_primes.append(candidate)
    return potential_primes

# Generate primes
potential_primes = generate_primes_from_zeros(zeros_imag)

# Print the potential primes
print("Potential primes based on zero line mapping:")
for prime in potential_primes:
    print(prime)
