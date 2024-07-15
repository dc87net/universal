import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
M_app = M / 2  # Apparent mass due to entanglement
c = 2.998e8  # Speed of light, m/s
r_s = 2 * G * M / c ** 2  # Schwarzschild radius, m
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


# Calculate the potentials for actual and apparent masses
V_hyperbolic = potential_hyperbolic(r, r_s, G, M)
V_hyperbolic_app = potential_hyperbolic(r, r_s_app, G, M_app)


# Construct the Hamiltonian matrix for hyperbolic model
def construct_hamiltonian(V, dr):
    N = len(V)
    H = np.zeros((N, N))
    for i in range(1, N - 1):
        H[i, i] = 2 / dr ** 2 + V[i]
        H[i, i - 1] = H[i, i + 1] = -1 / dr ** 2
    H[0, 0] = H[N - 1, N - 1] = 1 / dr ** 2 + V[0]  # Boundary conditions
    return H


# Solve for eigenvalues and eigenvectors for hyperbolic model
H_hyperbolic = construct_hamiltonian(V_hyperbolic, dr)
H_hyperbolic_app = construct_hamiltonian(V_hyperbolic_app, dr)
eigenvalues_hyperbolic, eigenvectors_hyperbolic = eigh(H_hyperbolic)
eigenvalues_hyperbolic_app, eigenvectors_hyperbolic_app = eigh(H_hyperbolic_app)

# Plot the probability densities (square of the eigenvectors) for several energy levels
plt.figure(figsize=(14, 10))

for i in range(4):  # Plot first 4 eigenvectors for each model
    plt.subplot(4, 2, 2 * i + 1)
    plt.plot(r, eigenvectors_hyperbolic[:, i] ** 2, label=f'Level {i + 1}')
    plt.title(f'Hyperbolic (Actual Mass) - Level {i + 1}')
    plt.xlabel('Radial Distance (m)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)

    plt.subplot(4, 2, 2 * i + 2)
    plt.plot(r, eigenvectors_hyperbolic_app[:, i] ** 2, label=f'Level {i + 1}')
    plt.title(f'Hyperbolic (Apparent Mass) - Level {i + 1}')
    plt.xlabel('Radial Distance (m)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()