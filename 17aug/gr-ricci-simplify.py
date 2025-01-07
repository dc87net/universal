import sympy as sp

# Define the symbols
r, G, M, c = sp.symbols('r G M c', real=True, positive=True)

# Define the simplified Ricci tensor components
R_tt = (2*G*M)/(c**2 * r**2 * (1 - (2*G*M)/(c**2 * r))) - (4*G**2 * M**2)/(c**4 * r**3 * (1 - (2*G*M)/(c**2 * r)))
R_rr = (1 - (2*G*M)/(c**2 * r)) * (2*G*M)/(c**2 * r**2 - 2*G*M * r)
R_theta_theta_phi_phi = 2/r**3

# Sum the components to form the Ricci scalar R
R = R_tt + R_rr + R_theta_theta_phi_phi

# Simplify the Ricci scalar
R_simplified = sp.simplify(R)
print(R_simplified)
