import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
M_app = M / 2  # Apparent mass due to entanglement
c = 2.998e8  # Speed of light, m/s
a = 0.9  # Spin parameter, dimensionless
r_s = 2 * G * M / c**2  # Schwarzschild radius, m
r_s_app = r_s / 2  # Apparent Schwarzschild radius

# Define a grid for r
r_min = 0.5 * r_s
r_max = 2 * r_s
N = 500
r = np.linspace(r_min, r_max, N)
dr = r[1] - r[0]

# Hyperbolic Tangent Model Potential
def potential_hyperbolic(r, r_s, G, M):
    x = r / r_s
    return -G * M / (r_s * np.tanh(x))

# Traditional Kerr Model Potential
def potential_kerr(r, G, M, a):
    return -G * M / (r * (1 + a**2 / r**2))

# Calculate the potentials for actual and apparent masses
V_hyperbolic = potential_hyperbolic(r, r_s, G, M)
V_hyperbolic_app = potential_hyperbolic(r, r_s_app, G, M_app)
V_kerr = potential_kerr(r, G, M, a)
V_kerr_app = potential_kerr(r, G, M_app, a)

# Construct the Hamiltonian matrix
def construct_hamiltonian(V, dr):
    N = len(V)
    H = np.zeros((N, N))
    for i in range(1, N-1):
        H[i, i] = 2 / dr**2 + V[i]
        H[i, i-1] = H[i, i+1] = -1 / dr**2
    H[0, 0] = H[N-1, N-1] = 1 / dr**2 + V[0]  # Boundary conditions
    return H

# Solve for eigenvalues and eigenvectors
H_hyperbolic = construct_hamiltonian(V_hyperbolic, dr)
H_hyperbolic_app = construct_hamiltonian(V_hyperbolic_app, dr)
H_kerr = construct_hamiltonian(V_kerr, dr)
H_kerr_app = construct_hamiltonian(V_kerr_app, dr)

eigenvalues_hyperbolic, eigenvectors_hyperbolic = eigh(H_hyperbolic)
eigenvalues_hyperbolic_app, eigenvectors_hyperbolic_app = eigh(H_hyperbolic_app)
eigenvalues_kerr, eigenvectors_kerr = eigh(H_kerr)
eigenvalues_kerr_app, eigenvectors_kerr_app = eigh(H_kerr_app)

# Plot the eigenvalues
plt.figure(figsize=(10, 6))
plt.plot(eigenvalues_hyperbolic, label='Hyperbolic (Actual Mass)')
plt.plot(eigenvalues_hyperbolic_app, label='Hyperbolic (Apparent Mass)')
plt.plot(eigenvalues_kerr, label='Kerr (Actual Mass)')
plt.plot(eigenvalues_kerr_app, label='Kerr (Apparent Mass)')
plt.xlabel('Eigenvalue Index')
plt.ylabel('Eigenvalue')
plt.title('Eigenvalue Comparison')
plt.legend()
plt.grid(True)
plt.show()

# Plot the first eigenvector
plt.figure(figsize=(10, 6))
plt.plot(r, eigenvectors_hyperbolic[:, 0], label='Hyperbolic (Actual Mass)')
plt.plot(r, eigenvectors_hyperbolic_app[:, 0], label='Hyperbolic (Apparent Mass)')
plt.plot(r, eigenvectors_kerr[:, 0], label='Kerr (Actual Mass)')
plt.plot(r, eigenvectors_kerr_app[:, 0], label='Kerr (Apparent Mass)')
plt.xlabel('Radial Distance (m)')
plt.ylabel('Eigenvector Amplitude')
plt.title('First Eigenvector Comparison')
plt.legend()
plt.grid(True)
plt.show()