import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 5.5 * 1.989e30  # Mass of the black hole in kg
c = 2.998e8  # Speed of light, m/s
a = 0.9  # Spin parameter, dimensionless
r_s = 2 * G * M / c**2  # Schwarzschild radius, m

# Critical points near the Schwarzschild radius
critical_r = np.array([0.95 * r_s, r_s, 1.05 * r_s])
theta = np.pi / 2  # Equatorial plane

# Hyperbolic Tangent Model Potential
def potential_hyperbolic(r, r_s, G, M):
    x = r / r_s
    return -G * M / (r_s * np.tanh(x))

# Traditional Kerr Model Potential (simplified)
def potential_kerr(r, G, M, a):
    try:
        return -G * M / (r * (1 + a**2 / r**2))
    except ZeroDivisionError:
        return np.nan

# Calculate potentials at critical points
V_hyperbolic_critical = potential_hyperbolic(critical_r, r_s, G, M)
V_kerr_critical = potential_kerr(critical_r, G, M, a)

# Calculate gradients at critical points (radial component)
def gradient_field(V, dr):
    try:
        grad_r = np.gradient(V, dr)
        return grad_r
    except Exception as e:
        return np.nan

dr = critical_r[1] - critical_r[0]

grad_r_hyperbolic = gradient_field(V_hyperbolic_critical, dr)
grad_r_kerr = gradient_field(V_kerr_critical, dr)

# Print the results
print("Critical Points Evaluation\n")
for i, r in enumerate(critical_r):
    print(f"r = {r:.2e} m")
    print(f"  Hyperbolic Tangent Model Potential: {V_hyperbolic_critical[i]:.2e} J")
    print(f"  Traditional Kerr Model Potential: {V_kerr_critical[i]:.2e} J")
    print(f"  Hyperbolic Tangent Model Gradient (r): {grad_r_hyperbolic[i]:.2e} J/m")
    print(f"  Traditional Kerr Model Gradient (r): {grad_r_kerr[i]:.2e} J/m")
    print()