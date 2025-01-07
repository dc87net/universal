import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the scalar curvature as a function of theta and omega
def scalar_curvature(theta, omega):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    numerator = (
        (-128 * sin_theta ** 4 + 128 * sin_theta ** 2 - 16) *
        (omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 2
        + (-768 * omega ** 2 - 12288 * sin_theta ** 4 + 12288 * sin_theta ** 2 - 3072) *
        sin_theta ** 2 * cos_theta ** 2 * np.cos(2 * theta) ** 2
    )
    denominator = (omega ** 2 + 16 * sin_theta ** 4 - 16 * sin_theta ** 2 + 4) ** 4
    return numerator / denominator

# Parameters for plot
omega_val = 8  # Angular frequency
theta_vals = np.linspace(0, 2 * np.pi, 1000)  # Range of theta values

# Compute the scalar curvature for each theta
scalar_curv_vals = scalar_curvature(theta_vals, omega_val)

# Plot the scalar curvature
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, scalar_curv_vals, label=f'Scalar Curvature (ω = {omega_val})')
plt.title('Scalar Curvature as a Function of Theta')
plt.xlabel('Theta')
plt.ylabel('Scalar Curvature')
plt.legend()
plt.grid(True)
plt.show()

# Define symbols for SymPy calculations
theta, omega, L, I, G, c = sp.symbols('theta omega L I G c')

# Define g_theta_theta as a symbolic expression
g_theta_theta = omega**2 + 16 * sp.sin(theta)**4 - 16 * sp.sin(theta)**2 + 4

# Compute the derivative of g_theta_theta with respect to theta
dg_dtheta = sp.diff(g_theta_theta, theta)

# Inverse of g_theta_theta
g_theta_theta_inv = 1 / g_theta_theta

# Christoffel symbol Γ^θ_θθ
Gamma_theta_theta_theta = (1/2) * g_theta_theta_inv * dg_dtheta
Gamma_theta_theta_theta_simplified = sp.simplify(Gamma_theta_theta_theta)

# Output the Christoffel symbol
print(f"Christoffel Symbol Γ^θ_θθ: {Gamma_theta_theta_theta_simplified}")

# Compute the Riemann curvature tensor component (1D case)
R_theta_theta_theta_theta = sp.diff(Gamma_theta_theta_theta, theta) - Gamma_theta_theta_theta**2
R_theta_theta_theta_theta_simplified = sp.simplify(R_theta_theta_theta_theta)

# Output the Riemann curvature tensor
print(f"Riemann Curvature Tensor R^θ_θθθ: {R_theta_theta_theta_theta_simplified}")

# Scalar curvature: R = R_theta_theta / g_theta_theta
scalar_curvature_expr = R_theta_theta_theta_theta_simplified / g_theta_theta
scalar_curvature_simplified = sp.simplify(scalar_curvature_expr)

# Output the scalar curvature
print(f"Scalar Curvature R: {scalar_curvature_simplified}")

# Define parametric equations for 3D space representation
x = sp.cos(omega * theta) * sp.cos(omega * theta)
y = sp.cos(omega * theta) * sp.sin(omega * theta)
z = sp.sin(2 * theta)

# Compute derivatives
dx_dtheta = sp.diff(x, theta)
dy_dtheta = sp.diff(y, theta)
dz_dtheta = sp.diff(z, theta)

# Compute metric tensor g_theta_theta from the parametric equations
g_theta_theta_parametric = dx_dtheta**2 + dy_dtheta**2 + dz_dtheta**2
g_theta_theta_parametric = sp.simplify(g_theta_theta_parametric)

# Output metric tensor
print(f"g_theta_theta (parametric): {g_theta_theta_parametric}")

# Compute Christoffel symbol for the parametric form
d_g_theta_theta_parametric = sp.diff(g_theta_theta_parametric, theta)
christoffel_parametric = (1 / 2) * (1 / g_theta_theta_parametric) * d_g_theta_theta_parametric
christoffel_parametric = sp.simplify(christoffel_parametric)

# Output Christoffel symbol for parametric form
print(f"Christoffel Symbol Γ^θ_θθ (parametric): {christoffel_parametric}")

# Compute Riemann curvature tensor R^θ_θθθ for parametric form
riemann_parametric = sp.diff(christoffel_parametric, theta) - christoffel_parametric**2
riemann_parametric = sp.simplify(riemann_parametric)

# Output Riemann curvature tensor for parametric form
print(f"Riemann Curvature Tensor R^θ_θθθ (parametric): {riemann_parametric}")

# Scalar curvature for the parametric form
scalar_curvature_parametric = riemann_parametric / g_theta_theta_parametric
scalar_curvature_parametric = sp.simplify(scalar_curvature_parametric)

# Output scalar curvature for parametric form
print(f"Scalar Curvature R (parametric): {scalar_curvature_parametric}")

# Stress-energy tensor in theta direction (from momentum space)
T_theta_theta = L**2 / I

# Compute Einstein Tensor G_θθ
einstein_tensor = R_theta_theta_theta_theta_simplified - (1/2) * scalar_curvature_simplified * g_theta_theta

# Output Einstein Tensor
print(f"Einstein Tensor G_θθ: {einstein_tensor}")

# Compare with stress-energy tensor (Einstein Field Equations)
G_factor = 8 * sp.pi * G / c**4
comparison = sp.Eq(einstein_tensor, G_factor * T_theta_theta)

# Output the Einstein Field Equation comparison
print(f"Einstein Field Equation Comparison: {comparison}")


# Define time as a symbolic variable
t = sp.symbols('t')
# Make g_theta_theta time-dependent by adding a time-dependent term, for example:
g_theta_theta_time_dependent = g_theta_theta + sp.sin(omega * t)

# Recalculate Christoffel symbols and Riemann tensor with this new metric
dg_dtheta_time_dependent = sp.diff(g_theta_theta_time_dependent, theta)
dg_dt_time_dependent = sp.diff(g_theta_theta_time_dependent, t)

# Christoffel symbol with time dependence
Gamma_theta_theta_theta_time_dependent = (1/2) * g_inv * dg_dtheta_time_dependent
Gamma_theta_theta_theta_time_dependent_simplified = sp.simplify(Gamma_theta_theta_theta_time_dependent)

print(f"Time-dependent Christoffel Symbol Γ^θ_θθ: {Gamma_theta_theta_theta_time_dependent_simplified}")

# Riemann curvature tensor with time dependence
R_theta_theta_theta_theta_time_dependent = sp.diff(Gamma_theta_theta_theta_time_dependent, theta) - Gamma_theta_theta_theta_time_dependent**2
R_theta_theta_theta_theta_time_dependent_simplified = sp.simplify(R_theta_theta_theta_theta_time_dependent)

print(f"Time-dependent Riemann Curvature Tensor R^θ_θθθ: {R_theta_theta_theta_theta_time_dependent_simplified}")
