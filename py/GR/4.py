import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import os

# Create a directory to store frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Physical constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 2.998e8  # Speed of light, m/s
hbar = 1.055e-34  # Reduced Planck constant, J*s
M = 1.989e30  # Mass of the black hole (Sun's mass), kg
m = 9.109e-31  # Mass of the particle (electron), kg

# Schwarzschild radius
r_s = 2 * G * M / c ** 2


# Define the potential term using hyperbolic functions
def V(x):
    return -G * M * m / (r_s * np.tanh(x))


# Define the modified Klein-Gordon equation in terms of a system of first-order ODEs
def modified_klein_gordon_eq(x, y):
    Phi, dPhi_dx = y
    d2Phi_dx2 = 2 * np.cosh(x) ** -2 * dPhi_dx - (m ** 2 * c ** 2 / hbar ** 2 + G * M * m / (r_s * np.tanh(x))) * Phi
    return np.vstack((dPhi_dx, d2Phi_dx2))


# Boundary conditions for bound states
def boundary_conditions(ya, yb):
    return np.array([ya[0], yb[0]])


# Solve the modified Klein-Gordon equation for a given x range
x = np.linspace(-5, 5, 400)
Phi_initial = np.zeros((2, x.size))

# Initial guess for the wave function
Phi_initial[0] = np.exp(-x ** 2)

# Solve the boundary value problem
solution = solve_bvp(modified_klein_gordon_eq, boundary_conditions, x, Phi_initial)

# Extract the wave function solution
Phi = solution.sol(x)[0]

# Time-dependent part of the wave function
t = np.linspace(0, 2 * np.pi, 100)

# Generate frames for the animation
for i, ti in enumerate(t):
    T = np.exp(-1j * (m * c ** 2 * ti / hbar - G * M * m * ti / (r_s * np.tanh(x))))
    psi = np.real(Phi * T)

    # Plot the frame
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(x, V(x), label='Potential $V(x)$', color='red', linewidth=2)
    ax.plot(x, psi, label=f'Wavefunction $\psi(x, t={ti:.2f})$', color='blue', linewidth=2)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title('Wave Function Evolution Over Time')
    ax.set_xlabel('x')
    ax.set_ylabel('Wavefunction $\psi(x, t)$')
    ax.legend()
    ax.grid(True)

    # Save the frame
    frame_filename = os.path.join(frames_dir, f'frame_{i:03d}.png')
    plt.savefig(frame_filename)
    plt.close(fig)

print("Frames have been generated and saved in the 'frames' directory.")