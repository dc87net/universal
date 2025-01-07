import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(0, 2 * np.pi, 100)

# Projection plane (where we expect the closed loop/ellipse)
view_angle = {'elev': 30, 'azim': 60}  # Adjust angles to find the ellipse

# Calculate C based on the known major axis
# Example: If we've determined the major axis length is 2.5
C = 1

# Generate plots for covarying A and B using the calculated C
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Fixed axis limits for consistency
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Axis labels for clarity
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Loop through different values of A and B
for angle in np.linspace(0, 2 * np.pi, 5):
    A = C * np.cos(angle)
    B = C * np.sin(angle)

    # Parametric equations with covarying A and B
    x = A * np.sin(u_vals) * np.cos(v_vals)
    y = B * np.sin(u_vals) * np.sin(v_vals)
    z = np.cos(u_vals)

    # Plotting the trace
    ax.plot(x, y, z, label=f'A={A:.2f}, B={B:.2f}')

# Set viewing angle consistently
ax.view_init(elev=view_angle['elev'], azim=view_angle['azim'])

# Title and legend
plt.title("3D Plot with Covarying A and B (Major Axis as C)")
plt.legend()
plt.show()
