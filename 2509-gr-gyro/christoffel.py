import sympy as sp

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
