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
