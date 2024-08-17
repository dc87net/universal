import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from mpmath import zeta

def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * np.pi**(-(0.5 + 1j*t)) * np.cos(np.pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Example parameters extracted from visualizations
A_k = [1, 0.5]
omega_k = [2 * np.pi * 0.1, 2 * np.pi * 0.2]
phi_k = [0, np.pi / 4]
B_j = [0.3, 0.2]
nu_j = [2 * np.pi * 0.05, 2 * np.pi * 0.15]
theta_j = [np.pi / 6, np.pi / 3]
C_m = [0.4, 0.3]
lambda_m = [0.01, 0.02]
eta_m = [2 * np.pi * 0.1, 2 * np.pi * 0.2]
gamma_m = [np.pi / 2, np.pi]

def effective_potential(s, t, A_k, omega_k, phi_k, B_j, nu_j, theta_j, C_m, lambda_m, eta_m, gamma_m):
    V_stable_real = sum(A_k * np.cos(omega_k * np.real(s) + phi_k))
    V_stable_imag = sum(B_j * np.sin(nu_j * np.imag(s) + theta_j))
    V_time_dependent = sum(C_m * np.exp(lambda_m * t) * np.cos(eta_m * np.real(s) + gamma_m))
    return V_stable_real + V_stable_imag + V_time_dependent

# Example usage of the potential function
s = 0.5 + 0.5j
t = 1.0  # Example time
V_eff = effective_potential(s, t, A_k, omega_k, phi_k, B_j, nu_j, theta_j, C_m, lambda_m, eta_m, gamma_m)
print("Effective Potential:", V_eff)

# Plotting the wave function
theta_values = np.linspace(0, 50, 500)
real_part = [np.real(zeta_symbolic(theta)) for theta in theta_values]
imaginary_part = [np.imag(zeta_symbolic(theta)) for theta in theta_values]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(theta_values, real_part, zs=0, zdir='z', label='Real Part', color='blue')
ax.plot(theta_values, imaginary_part, zs=0, zdir='z', label='Imaginary Part', color='green')
ax.set_xlabel('Theta (t)')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Hamiltonian (H)')
plt.legend()
plt.show()
