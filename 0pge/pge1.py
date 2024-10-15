import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.optimize import minimize
from scipy.special import jn_zeros

# Constants
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)
m = 9.10938356e-31  # Mass of electron (kg)

# Spatial Domain
L = 1e-9  # Length of the box (meters)
N = 1000  # Number of discretization points
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Prime Numbers
primes = [2, 3, 5, 7, 11]  # First few primes for demonstration


def construct_hamiltonian(V):
    """
    Constructs the Hamiltonian matrix for the 1D Schrödinger equation.

    Parameters:
        V (array): Potential energy array.

    Returns:
        H (2D array): Hamiltonian matrix.
    """
    # Kinetic energy part using finite difference (second derivative)
    diag = np.ones(N) * (-2.0)
    off_diag = np.ones(N - 1)
    T = (-hbar ** 2 / (2 * m * dx ** 2)) * (np.diag(diag) +
                                            np.diag(off_diag, k=1) +
                                            np.diag(off_diag, k=-1))

    # Potential energy part
    V_matrix = np.diag(V)

    # Hamiltonian
    H = T + V_matrix
    return H


def objective(params):
    """
    Objective function to minimize: the difference between computed eigenvalues and primes.

    Parameters:
        params (array): Parameters defining the potential V(x).

    Returns:
        error (float): Sum of squared differences.
    """
    # Example potential: Harmonic oscillator with parameters
    # V(x) = a*x**2 + b*x + c
    a, b, c = params
    V = a * x ** 2 + b * x + c

    # Construct Hamiltonian
    H = construct_hamiltonian(V)

    # Compute eigenvalues
    eigenvalues, _ = eigh(H)

    # Select first few eigenvalues
    E_computed = eigenvalues[:len(primes)]

    # Define primes in energy units (Assuming primes are in eV)
    # Convert primes from eV to Joules if necessary
    # For simplicity, assume primes are directly comparable
    E_primes = np.array(primes)

    # Compute error (sum of squared differences)
    error = np.sum((E_computed - E_primes) ** 2)
    return error


# Initial guess for potential parameters [a, b, c]
initial_params = [1e20, 0, 0]  # Example starting values

# Optimization
result = minimize(objective, initial_params, method='Nelder-Mead')

# Extract optimized parameters
a_opt, b_opt, c_opt = result.x
print("Optimized Potential Parameters:")
print(f"a = {a_opt}")
print(f"b = {b_opt}")
print(f"c = {c_opt}")

# Construct optimized potential
V_optimized = a_opt * x ** 2 + b_opt * x + c_opt

# Reconstruct Hamiltonian and compute eigenvalues
H_optimized = construct_hamiltonian(V_optimized)
eigenvalues_opt, eigenvectors_opt = eigh(H_optimized)
E_computed_opt = eigenvalues_opt[:len(primes)]

print("\nComputed Eigenvalues (in Joules):")
for i, E in enumerate(E_computed_opt):
    print(f"Eigenvalue {i + 1}: {E:.3e} J (Prime: {primes[i]})")

# Plot the potential
plt.figure(figsize=(8, 6))
plt.plot(x, V_optimized, label='Optimized Potential V(x)')
plt.title('Optimized Potential')
plt.xlabel('Position x (m)')
plt.ylabel('Potential V(x) (J)')
plt.legend()
plt.grid(True)
plt.show()

# Plot the first few eigenfunctions
plt.figure(figsize=(10, 8))
for n in range(len(primes)):
    plt.plot(x, eigenvectors_opt[:, n] ** 2 + E_computed_opt[n], label=f'Eigenstate {n + 1}')
plt.title('First Few Eigenfunctions with Energy Levels')
plt.xlabel('Position x (m)')
plt.ylabel('Probability Density |ψ(x)|² + E')
plt.legend()
plt.grid(True)
plt.show()
