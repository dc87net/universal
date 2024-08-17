import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
r, t, d = sp.symbols('r t d')
kx, omega = sp.symbols('kx omega')
R_t = sp.Function('R')(t)
G = sp.symbols('G')  # Gravitational constant
c = sp.symbols('c')  # Speed of light
kappa = 8 * sp.pi * G / c**4

# Define a more nuanced wave function incorporating spatial variation and horizon smearing
Psi = R_t * (sp.exp(-r**2) * (sp.cos(kx * r - omega * t) + sp.I**d * sp.sin(kx * r - omega * t)))

# Compute derivatives analytically
Psi_t = sp.diff(Psi, t)
Psi_t_conjugate = sp.diff(Psi.conjugate(), t)
Psi_r = sp.diff(Psi, r)
Psi_r_conjugate = sp.diff(Psi.conjugate(), r)

# Energy-momentum tensor components
T00 = sp.simplify(Psi_t * Psi_t_conjugate)
T11 = sp.simplify(Psi_r * Psi_r_conjugate)

# Trace of the energy-momentum tensor
T = T00 - T11

# Ricci tensor components (simplified example)
R00 = sp.simplify(kappa * (T00 - 0.5 * T))
R11 = sp.simplify(kappa * (T11 - 0.5 * T))

# Evaluate derivatives analytically
R00_evaluated = R00.doit()
R11_evaluated = R11.doit()

# Lambdify for numerical evaluation
R00_lambdified = sp.lambdify((r, t, kx, omega, d, R_t), R00_evaluated)
R11_lambdified = sp.lambdify((r, t, kx, omega, d, R_t), R11_evaluated)

# Numerical values
r_vals = np.linspace(2, 10, 1000)
t_val = 0
kx_val = 2 * np.pi
omega_val = 2 * np.pi
d_val = 1
R_t_val = 1

# Evaluate numerically
R00_vals = R00_lambdified(r_vals, t_val, kx_val, omega_val, d_val, R_t_val)
R11_vals = R11_lambdified(r_vals, t_val, kx_val, omega_val, d_val, R_t_val)

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(r_vals, np.abs(np.exp(-r_vals**2) * (np.cos(kx_val * r_vals - omega_val * t_val) + 1j**d_val * np.sin(kx_val * r_vals - omega_val * t_val)))**2, label='Psi Mag Squared (t=0)')
plt.title('Magnitude Squared of Generalized Wave Function')
plt.xlabel('r')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(r_vals, R00_vals, label='Schwarzschild g_tt')
plt.plot(r_vals, R11_vals, label='Schwarzschild g_rr')
plt.title('Schwarzschild Metric Components')
plt.xlabel('r')
plt.ylabel('Metric Component Value')
plt.legend()

plt.tight_layout()
plt.show()