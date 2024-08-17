import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.sparse import diags
from mpmath import zeta, mp

# Set decimal places of precision
mp.dps = 15

# Define the range for theta (t)
theta = np.linspace(0, 50, 500)

# Define the custom zeta function using mpmath for complex numbers
def custom_zeta_function(theta):
    s = 0.5 + 1j * theta
    zeta_values = np.array([zeta(complex(val)) for val in s], dtype=np.complex128)
    return np.real(zeta_values), np.imag(zeta_values)

# Get real and imaginary parts of the zeta function
real_part, imaginary_part = custom_zeta_function(theta)

# Define the Hamiltonian as a matrix (simplified for demonstration)
# For numerical solution, we need a discretized version of the Hamiltonian
N = len(theta)
dx = theta[1] - theta[0]
diagonals = [np.full(N, -2.0), np.ones(N-1), np.ones(N-1)]
laplacian = diags(diagonals, [0, -1, 1]) / dx**2

# Potential derived from the real part of the zeta function
V = diags([real_part], [0])

# Hamiltonian matrix
H = -laplacian + V

# Solve the eigenvalue problem
eigenvalues, eigenvectors = eigh(H.toarray())

# Plot the first few eigenfunctions
plt.figure()
for i in range(5):
    plt.plot(theta, eigenvectors[:, i], label=f'Eigenvalue {i}: {eigenvalues[i]:.2f}')
plt.xlabel('Theta')
plt.ylabel('Eigenfunction')
plt.legend()
plt.title('Eigenfunctions of the Hamiltonian')
plt.show()

# Plot the eigenvalues
plt.figure()
plt.plot(range(N), eigenvalues, 'r.', label='Eigenvalues')
plt.xlabel('Index')
plt.ylabel('Eigenvalue')
plt.legend()
plt.title('Eigenvalues of the Hamiltonian')
plt.show()
