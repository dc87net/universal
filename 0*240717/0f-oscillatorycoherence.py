import numpy as np
import matplotlib.pyplot as plt

# Define parameters
omega_0 = (np.pi/2)/(2*np.pi)  # Baseline angular frequency
alpha = 0.1  # Coupling strength or interaction term coefficient
dt = 0.01  # Time step
time = np.arange(0, 10, dt)  # Time array

# Initialize phase difference
Delta_theta = np.zeros_like(time)
Delta_theta[0] = 0.1  # Initial phase difference

# Define function to evolve the phase difference over time
def evolve_phase_difference(Delta_theta, omega_0, alpha, dt, time):
    for i in range(1, len(time)):
        # Update phase difference using a simple differential equation model
        Delta_theta[i] = Delta_theta[i-1] + dt * (omega_0 + alpha * np.sin(Delta_theta[i-1]))
    return Delta_theta

# Evolve the phase difference
Delta_theta = evolve_phase_difference(Delta_theta, omega_0, alpha, dt, time)

# Calculate coherence metric (oscillatory coherence)
coherence_metric = np.cos(Delta_theta)

# Plot the phase difference and coherence metric over time
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, Delta_theta, label="Phase Difference (Delta_theta)")
plt.title("Phase Difference Over Time")
plt.xlabel("Time")
plt.ylabel("Phase Difference (rad)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, coherence_metric, label="Coherence Metric (A(t))", color='orange')
plt.title("Oscillatory Coherence Over Time")
plt.xlabel("Time")
plt.ylabel("Coherence Metric")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the sine waves
A = 1.0  # Amplitude of Alice
B = 1.0  # Amplitude of Bob
omega = 2 * np.pi  # Angular frequency (in radians per second)
phi_A = 0.0  # Initial phase of Alice
phi_B = np.pi / 4  # Initial phase of Bob (introducing a phase difference)
dt = 0.01  # Time step
time = np.arange(0, 10, dt)  # Time array

# Define the sine waves for Alice and Bob
psi_A = A * np.sin(omega * time + phi_A)
psi_B = B * np.sin(omega * time + phi_B)

# Calculate the phase difference (which is constant in this simple case)
Delta_phi = phi_A - phi_B
coherence_metric = np.cos(Delta_phi)  # Coherence based on the constant phase difference

# Plot Alice and Bob's sine waves and the coherence metric
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, psi_A, label="Alice (ψ_A)")
plt.plot(time, psi_B, label="Bob (ψ_B)")
plt.title("Alice and Bob as Simple Sine Waves")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, coherence_metric * np.ones_like(time), color='orange', label="Coherence Metric (A(t))")
plt.title("Coherence Between Alice and Bob")
plt.xlabel("Time")
plt.ylabel("Coherence Metric")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
