import sympy as sp

# Define the necessary symbolic variables
theta, phi, omega_base = sp.symbols('theta phi omega_base', real=True)
A, r_0 = sp.symbols('A r_0', real=True)

# Define the parametric equations based on previous derivations
# Radial function with our specific form
R = (A * sp.sin(omega_base * theta) + r_0)**6

# Parametric equations for momentum space
x_momentum = R * sp.cos(omega_base * theta)
y_momentum = R * sp.sin(omega_base * theta)
z_momentum = sp.sin(2 * theta)

# Position vector in momentum space
momentum_vector = sp.Matrix([x_momentum, y_momentum, z_momentum])

# Initialize the metric tensor
metric_tensor = sp.Matrix.zeros(3, 3)

# Variables used for the tensor calculation
variables = [theta, phi, omega_base]

# Calculate each component of the metric tensor
for i in range(3):
    for j in range(3):
        element_sum = 0
        for var in variables:
            element_sum += sp.diff(momentum_vector[i], var) * sp.diff(momentum_vector[j], var)
        metric_tensor[i, j] = element_sum

# Output the unsimplified metric tensor to verify
metric_tensor_unsimplified = metric_tensor
metric_tensor_unsimplified

# Simplify each component of the metric tensor
metric_tensor_simplified = metric_tensor.applyfunc(lambda x: x.simplify())
metric_tensor_simplified

#Matrix([
# [                                                    (omega_base**2 + theta**2)*(A*sin(omega_base*theta) + r_0)**10*(-7*A*cos(omega_base*theta)**2 + A + r_0*sin(omega_base*theta))**2, (omega_base**2 + theta**2)*(A*sin(omega_base*theta) + r_0)**10*(7*A*sin(omega_base*theta) + r_0)*(7*A*cos(omega_base*theta)**2 - A - r_0*sin(omega_base*theta))*cos(omega_base*theta), 2*omega_base*(A*sin(omega_base*theta) + r_0)**5*(7*A*cos(omega_base*theta)**2 - A - r_0*sin(omega_base*theta))*cos(2*theta)],
# [(omega_base**2 + theta**2)*(A*sin(omega_base*theta) + r_0)**10*(7*A*sin(omega_base*theta) + r_0)*(7*A*cos(omega_base*theta)**2 - A - r_0*sin(omega_base*theta))*cos(omega_base*theta),                                                          (omega_base**2 + theta**2)*(A*sin(omega_base*theta) + r_0)**10*(7*A*sin(omega_base*theta) + r_0)**2*cos(omega_base*theta)**2,        2*omega_base*(A*sin(omega_base*theta) + r_0)**5*(7*A*sin(omega_base*theta) + r_0)*cos(2*theta)*cos(omega_base*theta)],
# [                                                          2*omega_base*(A*sin(omega_base*theta) + r_0)**5*(7*A*cos(omega_base*theta)**2 - A - r_0*sin(omega_base*theta))*cos(2*theta),                                                                  2*omega_base*(A*sin(omega_base*theta) + r_0)**5*(7*A*sin(omega_base*theta) + r_0)*cos(2*theta)*cos(omega_base*theta),                                                                                                           4*cos(2*theta)**2]])

# Define the Christoffel symbols as a matrix of zeros
n = len(variables)
christoffel_symbols = sp.MutableDenseNDimArray.zeros(n, n, n)

# Calculate Christoffel symbols Gamma^i_jk = 1/2 * g^im * (dg_mj/dx^k + dg_mk/dx^j - dg_jk/dx^m)
for i in range(n):
    for j in range(n):
        for k in range(n):
            # Calculate the sum over m
            gamma_sum = 0
            for m in range(n):
                gamma_sum += sp.diff(metric_tensor_simplified[m, j], variables[k]) \
                           + sp.diff(metric_tensor_simplified[m, k], variables[j]) \
                           - sp.diff(metric_tensor_simplified[j, k], variables[m])
            # Multiply by the inverse metric tensor and 1/2
            christoffel_symbols[i, j, k] = (1/2) * gamma_sum

# Simplify each Christoffel symbol
christoffel_symbols_simplified = christoffel_symbols.applyfunc(lambda x: x.simplify())

# Display a few Christoffel symbols as example
christoffel_symbols_simplified[0, 0, 0], christoffel_symbols_simplified[1, 1, 1], christoffel_symbols_simplified[2, 2, 2]
