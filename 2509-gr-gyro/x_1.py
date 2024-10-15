import sympy as sp

import sympy as sp

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Define the scalar curvature as a function of theta and omega
def scalar_curvature(theta, omega):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    numerator = (-128 * sin_theta ** 4 + 128 * sin_theta ** 2 - 16) * (
                omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 2 + \
                (
                            -768 * omega ** 2 - 12288 * sin_theta ** 4 + 12288 * sin_theta ** 2 - 3072) * sin_theta ** 2 * cos_theta ** 2 * np.cos(
        2 * theta) ** 2
    denominator = (omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 4

    return numerator / denominator


# Parameters
omega = 8  # Angular frequency
theta_vals = np.linspace(0, 2 * np.pi, 1000)  # Range of theta values

# Compute the scalar curvature for each theta
scalar_curv_vals = scalar_curvature(theta_vals, omega)

# Plot the scalar curvature
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, scalar_curv_vals, label=f'Scalar Curvature (ω = {omega})')
plt.title('Scalar Curvature as a Function of Theta')
plt.xlabel('Theta')
plt.ylabel('Scalar Curvature')
plt.legend()
plt.grid(True)
plt.show()


# Define symbols
theta, omega = sp.symbols('theta omega')

# Define g_theta_theta from your result
g_theta_theta = omega**2 + 16 * sp.sin(theta)**4 - 16 * sp.sin(theta)**2 + 4

# Compute the derivative of g_theta_theta with respect to theta
dg_dtheta = sp.diff(g_theta_theta, theta)

# Inverse of g_theta_theta for Christoffel symbol
g_theta_theta_inv = 1 / g_theta_theta

# Christoffel symbol
Gamma_theta_theta_theta = (1/2) * g_theta_theta_inv * dg_dtheta
Gamma_theta_theta_theta_simplified = sp.simplify(Gamma_theta_theta_theta)

# Output the Christoffel symbol
print(f"Christoffel Symbol Γ^θ_θθ: {Gamma_theta_theta_theta_simplified}")

# Compute the Riemann curvature tensor component (simplified 1D case)
R_theta_theta_theta_theta = sp.diff(Gamma_theta_theta_theta, theta) - Gamma_theta_theta_theta**2
R_theta_theta_theta_theta_simplified = sp.simplify(R_theta_theta_theta_theta)

# Output the Riemann curvature tensor
print(f"Riemann Curvature Tensor R^θ_θθθ: {R_theta_theta_theta_theta_simplified}")

# Continuing from the previous SymPy setup
R_theta_theta = R_theta_theta_theta_theta_simplified

# Scalar curvature: R = R_theta_theta / g_theta_theta
scalar_curvature = R_theta_theta / g_theta_theta
scalar_curvature_simplified = sp.simplify(scalar_curvature)

# Output the scalar curvature
print(f"Scalar Curvature R: {scalar_curvature_simplified}")


# Define symbols
theta, omega = sp.symbols('theta omega')
x = sp.cos(omega * theta) * sp.cos(omega * theta)
y = sp.cos(omega * theta) * sp.sin(omega * theta)
z = sp.sin(2 * theta)

# Compute derivatives
dx_dtheta = sp.diff(x, theta)
dy_dtheta = sp.diff(y, theta)
dz_dtheta = sp.diff(z, theta)

# Compute metric tensor g_theta_theta
g_theta_theta = dx_dtheta**2 + dy_dtheta**2 + dz_dtheta**2
g_theta_theta = sp.simplify(g_theta_theta)

# Output metric tensor
print(f"g_theta_theta: {g_theta_theta}")

# For Christoffel symbols, continue similarly using sp.diff and symbolic expressions.


# Define symbols
theta, omega = sp.symbols('theta omega')
x = sp.cos(omega * theta) * sp.cos(omega * theta)
y = sp.cos(omega * theta) * sp.sin(omega * theta)
z = sp.cos(omega * theta) * sp.sin(2 * theta)

# Compute derivatives
dx_dtheta = sp.diff(x, theta)
dy_dtheta = sp.diff(y, theta)
dz_dtheta = sp.diff(z, theta)

# Compute metric tensor g_theta_theta
g_theta_theta = dx_dtheta**2 + dy_dtheta**2 + dz_dtheta**2
g_theta_theta = sp.simplify(g_theta_theta)

# Output metric tensor
print(f"g_theta_theta: {g_theta_theta}")

# Christoffel symbols calculation (example for one component)
g_inv = 1 / g_theta_theta  # Inverse of the metric

# Christoffel symbol Γ^θ_θθ (for this 1D system, only θ dependence)
d_g_theta_theta = sp.diff(g_theta_theta, theta)
christoffel_theta_theta_theta = (1 / 2) * g_inv * d_g_theta_theta
christoffel_theta_theta_theta = sp.simplify(christoffel_theta_theta_theta)

print(f"Christoffel Symbol Γ^θ_θθ: {christoffel_theta_theta_theta}")

# Riemann curvature tensor calculation R^θ_θθθ
riemann_theta_theta_theta_theta = sp.diff(christoffel_theta_theta_theta, theta)
riemann_theta_theta_theta_theta = sp.simplify(riemann_theta_theta_theta_theta)

print(f"Riemann Curvature Tensor R^θ_θθθ: {riemann_theta_theta_theta_theta}")

# Scalar Curvature R for the 1D system (since it's reduced to θ only, it's a simpler form)
scalar_curvature = riemann_theta_theta_theta_theta / g_theta_theta
scalar_curvature = sp.simplify(scalar_curvature)

print(f"Scalar Curvature R: {scalar_curvature}")

# Compute Riemann Curvature Tensor R^θ_θθθ
riemann_theta_theta_theta_theta = sp.diff(christoffel_theta_theta_theta, theta)
riemann_theta_theta_theta_theta = sp.simplify(riemann_theta_theta_theta_theta)

# Output Riemann Curvature Tensor
print(f"Riemann Curvature Tensor R^θ_θθθ: {riemann_theta_theta_theta_theta}")


# Compute Scalar Curvature
scalar_curvature = riemann_theta_theta_theta_theta / g_theta_theta
scalar_curvature = sp.simplify(scalar_curvature)

# Output Scalar Curvature
print(f"Scalar Curvature R: {scalar_curvature}")

# Given the stress-energy tensor from momentum space, e.g., T_theta_theta = L^2 / I
# Assume L (angular momentum) and I (moment of inertia) are given

L = sp.symbols('L')  # Angular momentum
I = sp.symbols('I')  # Moment of inertia

# Stress-energy tensor in theta direction (from momentum space)
T_theta_theta = L**2 / I

import sympy as sp

# Define symbols
theta, omega = sp.symbols('theta omega')

# Metric tensor component g_theta_theta
g_theta_theta = omega**2 + 16 * sp.sin(theta)**4 - 16 * sp.sin(theta)**2 + 4

# Christoffel symbols calculation
d_g_theta_theta = sp.diff(g_theta_theta, theta)
g_inv = 1 / g_theta_theta
christoffel_theta_theta_theta = (1 / 2) * g_inv * d_g_theta_theta
christoffel_theta_theta_theta = sp.simplify(christoffel_theta_theta_theta)

# Compute Riemann Curvature Tensor R^θ_θθθ
riemann_theta_theta_theta_theta = sp.diff(christoffel_theta_theta_theta, theta)
riemann_theta_theta_theta_theta = sp.simplify(riemann_theta_theta_theta_theta)

# Compute Ricci Tensor (for 1D system, R_theta_theta is just R^θ_θθθ)
ricci_tensor = riemann_theta_theta_theta_theta

# Output Ricci Tensor
print(f"Ricci Tensor R_θθ: {ricci_tensor}")

# Compute Scalar Curvature
scalar_curvature = ricci_tensor / g_theta_theta
scalar_curvature = sp.simplify(scalar_curvature)

# Output Scalar Curvature
print(f"Scalar Curvature R: {scalar_curvature}")

# Compute Einstein Tensor G_θθ
einstein_tensor = ricci_tensor - (1/2) * scalar_curvature * g_theta_theta

# Output Einstein Tensor
print(f"Einstein Tensor G_θθ: {einstein_tensor}")

# Compare with stress-energy tensor
L = sp.symbols('L')  # Angular momentum
I = sp.symbols('I')  # Moment of inertia
T_theta_theta = L**2 / I

# Scale factor for Einstein Field Equations
G_factor = 8 * sp.pi * sp.symbols('G') / sp.symbols('c')**4
comparison = sp.Eq(einstein_tensor, G_factor * T_theta_theta)

print(f"Einstein Field Equation Comparison: {comparison}")

# Compare with Einstein tensor from position space curvature
einstein_tensor = ricci_tensor - (1/2) * scalar_curvature * g_theta_theta

# Scale by 8 pi G / c^4
G_factor = 8 * sp.pi * sp.symbols('G') / sp.symbols('c')**4
comparison = sp.Eq(einstein_tensor, G_factor * T_theta_theta)

print(f"Einstein Field Equation Comparison: {comparison}")
