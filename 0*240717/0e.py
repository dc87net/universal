import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the wave function using sech distribution
def wave_function(omega, width, phase_shift=0.0):
    """
    Returns the value of a sech wave function at a given frequency with a specific width and phase shift.
    """
    return np.cosh(width * omega) ** -1 * np.exp(1j * phase_shift * omega)

# Define the interaction integral function
def interaction_integral(width1, width2, phase_shift, omega_range=(-10, 10)):
    """
    Computes the interaction integral over a specified frequency range between two sech wave functions
    with different widths and a given phase shift.
    """
    # Define the integrand as the product of two sech wave functions
    def integrand(omega):
        psi1 = wave_function(omega, width1, 0)
        psi2 = wave_function(omega, width2, phase_shift)
        return np.real(np.conj(psi1) * psi2)

    # Compute the integral using quad (numerical integration)
    integral_result, _ = quad(integrand, omega_range[0], omega_range[1])
    return integral_result

# Simulation parameters
width_A = 1.0  # Width of Alice's wave function
width_B = 1.0  # Width of Bob's wave function
phase_shift = 0.0  # Phase difference between Alice and Bob
omega_range = (-10, 10)  # Range of frequency space for integration

# Compute the interaction integral for initial conditions
result = interaction_integral(width_A, width_B, phase_shift, omega_range)
print(f"Interaction Integral Result (Initial): {result:.4f}")

# Visualization
omega_values = np.linspace(omega_range[0], omega_range[1], 1000)
psi_A_values = [wave_function(omega, width_A, 0) for omega in omega_values]
psi_B_values = [wave_function(omega, width_B, phase_shift) for omega in omega_values]

plt.figure(figsize=(12, 6))
plt.plot(omega_values, np.abs(psi_A_values), label='Wave Function A (Alice)', color='blue')
plt.plot(omega_values, np.abs(psi_B_values), label='Wave Function B (Bob)', color='orange')
plt.title('Comparison of Wave Functions A and B in Frequency Space')
plt.xlabel('Frequency (ω)')
plt.ylabel('Amplitude |ψ|')
plt.legend()
plt.grid(True)
plt.show()

# Testing different phase shifts
phase_shifts = np.linspace(0, 2 * np.pi, 100)
interaction_results = [interaction_integral(width_A, width_B, shift, omega_range) for shift in phase_shifts]

plt.figure(figsize=(12, 6))
plt.plot(phase_shifts, interaction_results, color='green')
plt.title('Interaction Integral as a Function of Phase Shift')
plt.xlabel('Phase Shift (radians)')
plt.ylabel('Interaction Integral Value')
plt.grid(True)
plt.show()
