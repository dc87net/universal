from sympy import symbols, Matrix, simplify

# Define symbols
G, c = symbols('G c')
R = symbols('R')
g_mu_nu = Matrix([[1/R, 0, 0], [0, 1/R, 0], [0, 0, 1/R]])

# Substitute known Ricci scalar
Ricci_scalar = R  # Use your derived Ricci scalar here

# Compute Ricci tensor from the metric
R_mu_nu = Ricci_scalar * g_mu_nu

# Substitute into the Einstein field equations
Lambda = 0  # Cosmological constant can be zero
T_mu_nu = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])  # Stress-energy tensor assumed zero

EFE_lhs = R_mu_nu - 0.5 * g_mu_nu * Ricci_scalar
EFE_rhs = (8 * symbols('pi') * G / c**4) * T_mu_nu + g_mu_nu * Lambda

# Simplify the equation
EFE_result = simplify(EFE_lhs - EFE_rhs)
print("Result of the Einstein Field Equations:", EFE_result)
