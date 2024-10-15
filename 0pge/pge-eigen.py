import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.optimize import minimize

# Constants
hbar = 1.0545718e-34  # Reduced Planck constant (J·s)
m_particle = 9.10938356e-31  # Mass of electron (kg)

# Spatial Domain
L = 1e-9  # Length of the box (meters)
N = 1000  # Number of discretization points
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Prime Numbers (Extend this list as needed)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


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
    T = (-hbar ** 2 / (2 * m_particle * dx ** 2)) * (np.diag(diag) +
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
    # Example potential: Quadratic + Linear + Constant
    a, b, c = params
    V = a * x ** 2 + b * x + c

    # Construct Hamiltonian
    H = construct_hamiltonian(V)

    # Compute eigenvalues
    eigenvalues, _ = eigh(H)

    # Select first few eigenvalues corresponding to the number of primes
    E_computed = eigenvalues[:len(primes)]

    # Define primes in energy units (assuming primes are directly comparable)
    E_primes = np.array(primes)

    # Compute error (sum of squared differences)
    error = np.sum((E_computed - E_primes) ** 2)
    return error


# Initial guess for potential parameters [a, b, c]
initial_params = [1e20, 0, 0]  # Example starting values

# Optimization
result = minimize(objective, initial_params, method='Nelder-Mead',
                  options={'maxiter': 10000, 'disp': True})

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

# Plot the optimized potential
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

# Compare Computed Eigenvalues with Primes
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(primes) + 1), primes, 'ro-', label='Prime Numbers')
plt.plot(range(1, len(primes) + 1), E_computed_opt, 'bs--', label='Computed Eigenvalues')
plt.title('Prime Numbers vs. Computed Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Value (J)')
plt.legend()
plt.grid(True)
plt.show()


def objective(params):
    """
    Objective function to minimize: the difference between computed eigenvalues and primes.

    Parameters:
        params (array): Parameters defining the potential V(x).

    Returns:
        error (float): Sum of squared differences.
    """
    # Example potential: Quadratic + Linear (c = 0)
    a, b = params
    V = a * x ** 2 + b * x  # c is omitted

    # Construct Hamiltonian
    H = construct_hamiltonian(V)

    # Compute eigenvalues
    eigenvalues, _ = eigh(H)

    # Select first few eigenvalues corresponding to the number of primes
    E_computed = eigenvalues[:len(primes)]

    # Define primes in energy units (assuming primes are directly comparable)
    E_primes = np.array(primes)

    # Compute error (sum of squared differences)
    error = np.sum((E_computed - E_primes) ** 2)
    return error


# Initial guess for potential parameters [a, b]
initial_params = [1e20, 0]  # Example starting values

# Optimization with only a and b
result = minimize(objective, initial_params, method='Nelder-Mead',
                 options={'maxiter': 10000, 'disp': True})

# Extract optimized parameters
a_opt, b_opt = result.x
print("Optimized Potential Parameters:")
print(f"a = {a_opt}")
print(f"b = {b_opt}")

# Construct optimized potential
V_optimized = a_opt * x**2 + b_opt * x

# Reconstruct Hamiltonian and compute eigenvalues
H_optimized = construct_hamiltonian(V_optimized)
eigenvalues_opt, eigenvectors_opt = eigh(H_optimized)
E_computed_opt = eigenvalues_opt[:len(primes)]

print("\nComputed Eigenvalues (in Joules):")
for i, E in enumerate(E_computed_opt):
    print(f"Eigenvalue {i+1}: {E:.3e} J (Prime: {primes[i]})")

# Plot the optimized potential
plt.figure(figsize=(8, 6))
plt.plot(x, V_optimized, label='Optimized Potential V(x)')
plt.title('Optimized Potential Without Constant Term')
plt.xlabel('Position x (m)')
plt.ylabel('Potential V(x) (J)')
plt.legend()
plt.grid(True)
plt.show()

# Plot the first few eigenfunctions
plt.figure(figsize=(10, 8))
for n in range(len(primes)):
    plt.plot(x, eigenvectors_opt[:, n]**2 + E_computed_opt[n], label=f'Eigenstate {n+1}')
plt.title('First Few Eigenfunctions with Energy Levels')
plt.xlabel('Position x (m)')
plt.ylabel('Probability Density |ψ(x)|² + E')
plt.legend()
plt.grid(True)
plt.show()

# Compare Computed Eigenvalues with Primes
plt.figure(figsize=(8,6))
plt.plot(range(1, len(primes)+1), primes, 'ro-', label='Prime Numbers')
plt.plot(range(1, len(primes)+1), E_computed_opt, 'bs--', label='Computed Eigenvalues')
plt.title('Prime Numbers vs. Computed Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Value (J)')
plt.legend()
plt.grid(True)
plt.show()


def objective(params):
    """
    Objective function to minimize: the difference between scaled computed eigenvalues and primes.

    Parameters:
        params (array): Parameters defining the potential V(x) and scaling factor alpha.

    Returns:
        error (float): Sum of squared differences.
    """
    # Example potential: Quadratic + Linear
    a, b, alpha = params
    V = a * x ** 2 + b * x

    # Construct Hamiltonian
    H = construct_hamiltonian(V)

    # Compute eigenvalues
    eigenvalues, _ = eigh(H)

    # Select first few eigenvalues corresponding to the number of primes
    E_computed = eigenvalues[:len(primes)]

    # Define scaled primes
    E_primes = alpha * np.array(primes)

    # Compute error (sum of squared differences)
    error = np.sum((E_computed - E_primes) ** 2)
    return error

# Initial guess for potential parameters [a, b, alpha]
initial_params = [1e20, 0, 1e-23]  # Example starting values

# Optimization with a, b, alpha
result = minimize(objective, initial_params, method='Nelder-Mead',
                 options={'maxiter': 10000, 'disp': True})

# Extract optimized parameters
a_opt, b_opt, alpha_opt = result.x
print("Optimized Potential Parameters:")
print(f"a = {a_opt}")
print(f"b = {b_opt}")
print(f"alpha = {alpha_opt}")

# Construct optimized potential
V_optimized = a_opt * x**2 + b_opt * x

# Reconstruct Hamiltonian and compute eigenvalues
H_optimized = construct_hamiltonian(V_optimized)
eigenvalues_opt, eigenvectors_opt = eigh(H_optimized)
E_computed_opt = eigenvalues_opt[:len(primes)]
E_primes_scaled = alpha_opt * np.array(primes)

print("\nComputed Eigenvalues (in Joules):")
for i, E in enumerate(E_computed_opt):
    print(f"Eigenvalue {i+1}: {E:.3e} J (Prime: {primes[i]})")

# Plot the optimized potential
plt.figure(figsize=(8, 6))
plt.plot(x, V_optimized, label='Optimized Potential V(x)')
plt.title('Optimized Potential Without Constant Term')
plt.xlabel('Position x (m)')
plt.ylabel('Potential V(x) (J)')
plt.legend()
plt.grid(True)
plt.show()

# Plot the first few eigenfunctions
plt.figure(figsize=(10, 8))
for n in range(len(primes)):
    plt.plot(x, eigenvectors_opt[:, n]**2 + E_computed_opt[n], label=f'Eigenstate {n+1}')
plt.title('First Few Eigenfunctions with Energy Levels')
plt.xlabel('Position x (m)')
plt.ylabel('Probability Density |ψ(x)|² + E')
plt.legend()
plt.grid(True)
plt.show()

# Compare Computed Eigenvalues with Scaled Primes
plt.figure(figsize=(8,6))
plt.plot(range(1, len(primes)+1), E_primes_scaled, 'ro-', label='Scaled Prime Numbers')
plt.plot(range(1, len(primes)+1), E_computed_opt, 'bs--', label='Computed Eigenvalues')
plt.title('Scaled Prime Numbers vs. Computed Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Value (J)')
plt.legend()
plt.grid(True)
plt.show()


def objective(params):
    """
    Objective function to minimize: the difference between scaled computed eigenvalues and primes.

    Parameters:
        params (array): Parameters defining the potential V(x) and scaling factor alpha.

    Returns:
        error (float): Sum of squared differences.
    """
    # Example potential: Quadratic + Linear + Cubic
    a, b, d, alpha = params
    V = a * x ** 2 + b * x + d * x ** 3  # Removed constant term

    # Construct Hamiltonian
    H = construct_hamiltonian(V)

    # Compute eigenvalues
    eigenvalues, _ = eigh(H)

    # Select first few eigenvalues corresponding to the number of primes
    E_computed = eigenvalues[:len(primes)]

    # Define scaled primes
    E_primes = alpha * np.array(primes)

    # Compute error (sum of squared differences)
    error = np.sum((E_computed - E_primes) ** 2)
    return error

# Initial guess for potential parameters [a, b, d, alpha]
initial_params = [1e20, 0, 0, 1e-23]  # Example starting values

# Optimization with a, b, d, alpha
result = minimize(objective, initial_params, method='Nelder-Mead',
                 options={'maxiter': 20000, 'disp': True})

# Extract optimized parameters
a_opt, b_opt, d_opt, alpha_opt = result.x
print("Optimized Potential Parameters:")
print(f"a = {a_opt}")
print(f"b = {b_opt}")
print(f"d = {d_opt}")
print(f"alpha = {alpha_opt}")

# Proceed similarly with plotting and analysis


import numpy as np
from scipy.special import ellipe

# Constants
a = 1  # Semi-major axis
b = 0.5  # Semi-minor axis
e = np.sqrt(1 - (b/a)**2)  # Eccentricity

# Complete elliptic integral of the second kind
total_arc_length = 4 * a * ellipe(e)

def arc_length(n):
    return total_arc_length / n

def find_resonance_primes(max_n):
    primes = []
    for n in range(2, max_n+1):
        ratio = arc_length(n-1) / arc_length(n)
        if is_resonant(ratio):
            primes.append(n)
    return primes

def is_resonant(ratio):
    # Placeholder for resonance condition; needs specific definition
    return np.isclose(ratio, round(ratio))
