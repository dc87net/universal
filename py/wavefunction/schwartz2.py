import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define symbols
x, t, r = sp.symbols('x t r')
kx, omega, G, M = sp.symbols('kx omega G M')
c = sp.symbols('c')  # Speed of light
d = 3  # Dimensional count for space-like

# Define the generalized wave function in flat spacetime
R_t = sp.Function('R')(t)
Psi = R_t * (sp.cos(kx * x - omega * t) + sp.I**d * sp.sin(kx * x - omega * t))

# Schwarzschild metric components
g_tt = 1 - (2 * G * M) / (r * c**2)
g_rr = 1 / (1 - (2 * G * M) / (r * c**2))

# Transform the GWF to curved spacetime
Psi_curved = Psi * g_tt

# Lambdify the transformed wave function for numerical evaluation
Psi_curved_func = sp.lambdify((x, t, r, kx, omega, G, M, c, R_t), Psi_curved)

# Define example values for numerical evaluation
x_vals = np.linspace(-10, 10, 1000)
t_vals = np.linspace(-10, 10, 1000)
r_vals = np.linspace(1, 10, 1000)  # Avoid r=0 to prevent singularity
kx_val = 2 * np.pi
omega_val = 2 * np.pi
G_val = 6.67430e-11  # Gravitational constant
M_val = 1.989e30  # Mass of the sun
c_val = 3e8  # Speed of light
R_t_example = np.exp(-t_vals**2)  # Example function for R(t)

# Compute the transformed wave function values
Psi_curved_vals = Psi_curved_func(x_vals, t_vals[:, None], r_vals[:, None, None], kx_val, omega_val, G_val, M_val, c_val, R_t_example[:, None])

# Plot the real and imaginary parts of the transformed wave function
plt.figure(figsize=(14, 8))

plt.subplot(3, 1, 1)
plt.plot(x_vals, np.real(Psi_curved_vals[:, :, 500]), label='Real part')
plt.plot(x_vals, np.imag(Psi_curved_vals[:, :, 500]), label='Imaginary part', linestyle='--')
plt.title('Real and Imaginary Parts of the GWF in Curved Spacetime')
plt.xlabel('Position x')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.imshow(np.abs(Psi_curved_vals[:, 500, :]), aspect='auto', extent=[r_vals.min(), r_vals.max(), t_vals.min(), t_vals.max()], origin='lower')
plt.colorbar(label='Magnitude')
plt.title('Magnitude of the GWF in Curved Spacetime')
plt.xlabel('Radius r')
plt.ylabel('Time t')

plt.subplot(3, 1, 3)
plt.imshow(np.angle(Psi_curved_vals[:, 500, :]), aspect='auto', extent=[r_vals.min(), r_vals.max(), t_vals.min(), t_vals.max()], origin='lower')
plt.colorbar(label='Phase Angle')
plt.title('Phase Angle of the GWF in Curved Spacetime')
plt.xlabel('Radius r')
plt.ylabel('Time t')

plt.tight_layout()
plt.show()