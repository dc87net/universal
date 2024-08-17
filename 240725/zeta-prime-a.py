import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpmath import gamma, cos, pi, mp
from sympy import primerange

# Set precision
mp.dps = 25

# Define the symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * custom_zeta(s_conjugate))

# Define the custom zeta function recursively using the symbolic method
def custom_zeta(s):
    if s == 0:
        return complex(0)
    else:
        t = s.imag
        return zeta_symbolic(t)

# Define the range for the parameter t
t_values = np.linspace(0, 50, 1000)

# Compute zeta function values using the custom symbolic method
zeta_vals = np.array([custom_zeta(complex(0.5, t)) for t in t_values])
real_parts = np.real(zeta_vals)
imag_parts = np.imag(zeta_vals)
magnitudes = np.abs(zeta_vals)

# Generate prime numbers up to a certain limit
prime_limit = 200
primes = list(primerange(1, prime_limit))

# Compute zeta function values at prime numbers
prime_magnitudes = np.abs([custom_zeta(complex(0.5, p)) for p in primes])

# Create the 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the zeta function values
norm = plt.Normalize(magnitudes.min(), magnitudes.max())
colors = cm.viridis(norm(magnitudes))
ax.plot(real_parts, imag_parts, magnitudes, color='blue', lw=2, label='Zeta Function')

# Plot the primes as a scatter plot in 3D
ax.scatter(primes, [0]*len(primes), prime_magnitudes, color='red', s=50, label='Prime Numbers')

# Add a color bar to show the magnitude of the zeta function
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap='viridis'), shrink=0.5, aspect=5)
cbar.set_label('Magnitude')

# Set labels and title
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_zlabel('|Zeta|')
ax.set_title('3D Visualization of the Symbolic Riemann Zeta Function and Prime Numbers')
ax.view_init(elev=30., azim=45)  # Isometric view

# Add a legend
ax.legend()

plt.show()
