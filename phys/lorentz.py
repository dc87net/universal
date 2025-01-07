import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
x, t, kx, omega, v, c = sp.symbols('x t kx omega v c')
R_t = sp.Function('R')(t)

# Define Lorentz transformation
gamma = 1 / sp.sqrt(1 - v**2 / c**2)
X = gamma * (x - v * t)
T = gamma * (t - v * x / c**2)

# Define the generalized wave function
Psi = R_t * (sp.cos(kx * x - omega * t) + sp.I * sp.sin(kx * x - omega * t))

# Apply Lorentz transformation
Psi_prime = Psi.subs({x: X, t: T})

# Simplify the expression
Psi_prime_simplified = sp.simplify(Psi_prime)

# Lambdify the simplified expression
Psi_prime_func = sp.lambdify((x, t, kx, omega, v, c, R_t), Psi_prime_simplified)

# Example values for plotting
x_vals = np.linspace(-10, 10, 1000)
t_vals = np.linspace(-10, 10, 1000)
x_grid, t_grid = np.meshgrid(x_vals, t_vals)
kx_val = 2 * np.pi
omega_val = 2 * np.pi
v_val = 0.5
c_val = 1.0

# Example function for R(t)
def R_t_example(t):
    return np.exp(-t**2)

# Print debug information
print("x_grid shape:", x_grid.shape)
print("t_grid shape:", t_grid.shape)
print("R_t_example(t_grid) shape:", R_t_example(t_grid).shape)

# Evaluate the lambdified function
try:
    Psi_prime_vals = Psi_prime_func(x_grid, t_grid, kx_val, omega_val, v_val, c_val, R_t_example(t_grid))
except Exception as e:
    print("Error during function evaluation:", e)

# Plot the results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.contourf(x_vals, t_vals, np.real(Psi_prime_vals), cmap='RdBu')
plt.colorbar()
plt.title('Real Part of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')

plt.subplot(3, 1, 2)
plt.contourf(x_vals, t_vals, np.imag(Psi_prime_vals), cmap='RdBu')
plt.colorbar()
plt.title('Imaginary Part of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')

plt.subplot(3, 1, 3)
plt.contourf(x_vals, t_vals, np.abs(Psi_prime_vals)**2, cmap='viridis')
plt.colorbar()
plt.title('Magnitude Squared of Transformed Wave Function')
plt.xlabel('x')
plt.ylabel('t')

plt.tight_layout()
plt.show()