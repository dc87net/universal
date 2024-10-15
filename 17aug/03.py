import numpy as np
import matplotlib.pyplot as plt

# Parameters for the fixed state
A = 1.0  # Example value for A
B = 1.0  # Example value for B

# Define the u and v parameters (parameterize the surface)
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(0, 2 * np.pi, 100)

# Calculate the x, y, z coordinates using the parameterized equations
x = A * np.sin(u_vals) * np.cos(v_vals)
y = A * np.sin(u_vals) * np.sin(v_vals)
z = B * np.cos(u_vals)

# Plot XY Projection
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# XY Projection
ax[0].plot(x, y, color='b')
ax[0].set_title('XY Projection')
ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_xlim([-1.5, 1.5])
ax[0].set_ylim([-1.5, 1.5])

# XZ Projection
ax[1].plot(x, z, color='g')
ax[1].set_title('XZ Projection')
ax[1].set_xlabel('X')
ax[1].set_ylabel('Z')
ax[1].set_xlim([-1.5, 1.5])
ax[1].set_ylim([-1.5, 1.5])

# YZ Projection
ax[2].plot(y, z, color='r')
ax[2].set_title('YZ Projection')
ax[2].set_xlabel('Y')
ax[2].set_ylabel('Z')
ax[2].set_xlim([-1.5, 1.5])
ax[2].set_ylim([-1.5, 1.5])

plt.suptitle("Projections of the System's State")
plt.show()
