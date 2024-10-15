import numpy as np
import matplotlib.pyplot as plt

# Constants
a0 = 1.0  # Bohr radius (normalized)
Z = 1  # Atomic number for hydrogen

# Radial distance
r_vals = np.linspace(0, 10 * a0, 1000)

# Ground state wave function for hydrogen atom
def psi_1s(r):
    return (1 / np.sqrt(np.pi * a0**3)) * np.exp(-r / a0)

# Probability density (|ψ|^2)
def prob_density(r):
    return np.abs(psi_1s(r))**2

# Energy calculation for ground state
E_1s = -13.6 / (Z**2)  # in eV

# Plot the wave function and probability density
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(r_vals, psi_1s(r_vals), label=r'$\psi_{1s}(r)$')
plt.xlabel('r (Bohr radii)')
plt.ylabel(r'$\psi_{1s}(r)$')
plt.title('Hydrogen Atom Ground State Wave Function')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(r_vals, prob_density(r_vals), label=r'$|\psi_{1s}(r)|^2$', color='r')
plt.xlabel('r (Bohr radii)')
plt.ylabel(r'$|\psi_{1s}(r)|^2$')
plt.title('Probability Density of Hydrogen Atom')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(f"Ground State Energy (1s): {E_1s} eV")
