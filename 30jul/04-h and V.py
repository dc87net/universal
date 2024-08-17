import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero, mp


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

# Parameters for the potential function
alpha = 1.0
beta = 1.0

# Define the potential function V(t)
def potential(t, alpha, beta):
    return alpha * np.cos(beta * t)

# Discretize the t-values
t_values = np.linspace(0, 50, 1000)
dt = t_values[1] - t_values[0]
n_points = len(t_values)

# Construct the Hamiltonian matrix
diagonal = potential(t_values, alpha, beta)
off_diagonal = -1 / dt**2 * np.ones(n_points - 1)

# Solve the eigenvalue problem
eigenvalues, eigenvectors = eigh_tridiagonal(diagonal, off_diagonal)

# Plot the eigenvalues
plt.figure(figsize=(12, 6))
plt.plot(eigenvalues, 'o', label='Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Eigenvalue')
plt.title('Eigenvalues of the Hamiltonian')
plt.legend()
plt.grid(True)
plt.show()



# Set precision
mp.dps = 25

# Compute the first N non-trivial zeros of the zeta function
N = 20
zeta_zeros = [zetazero(n).imag for n in range(1, N + 1)]

# Plot the eigenvalues and zeta zeros
plt.figure(figsize=(12, 6))
plt.plot(eigenvalues[:N], 'o', label='Eigenvalues')
plt.plot(zeta_zeros, 'x', label='Zeta Zeros')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Comparison of Eigenvalues and Zeta Zeros')
plt.legend()
plt.grid(True)
plt.show()

# Adjust parameters and redefine the potential function
alpha_new = 2.0
beta_new = 0.5

# Recompute the potential function V(t)
def potential_new(t, alpha_new, beta_new):
    return alpha_new * np.cos(beta_new * t)

# Construct the new Hamiltonian matrix
diagonal_new = potential_new(t_values, alpha_new, beta_new)
off_diagonal_new = -1 / dt**2 * np.ones(n_points - 1)

# Solve the eigenvalue problem again
eigenvalues_new, eigenvectors_new = eigh_tridiagonal(diagonal_new, off_diagonal_new)

# Plot the new eigenvalues and zeta zeros
plt.figure(figsize=(12, 6))
plt.plot(eigenvalues_new[:N], 'o', label='New Eigenvalues')
plt.plot(zeta_zeros, 'x', label='Zeta Zeros')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Comparison of New Eigenvalues and Zeta Zeros')
plt.legend()
plt.grid(True)
plt.show()
