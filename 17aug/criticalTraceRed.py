import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Klein bottle parametric equations with parameters A and B
def klein_bottle(u, v, A, B):
    x = (A + B * np.cos(v)) * np.cos(u)
    y = (A + B * np.cos(v)) * np.sin(u)
    z = B * np.sin(v)
    return x, y, z

# Critical trace function
def critical_trace(t, A, B):
    u = np.pi + np.sin(t)
    v = np.cos(t)
    return klein_bottle(u, v, A, B)

# Parameters A and B (you can adjust these as needed based on your specific conditions)
A = 2
B = 1

# Create t values for the trace
t_values = np.linspace(0, 2 * np.pi, 100)

# Calculate the critical trace
x_vals, y_vals, z_vals = critical_trace(t_values, A, B)

# Visualization
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the Klein bottle
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)
x, y, z = klein_bottle(u, v, A, B)

ax.plot_surface(x, y, z, color='cyan', alpha=0.7, rstride=5, cstride=5)

# Plot the critical trace
ax.plot(x_vals, y_vals, z_vals, color='red', linewidth=2, label='Critical Trace')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Critical Trace on the Klein Bottle')

plt.legend()
plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# # Define the Klein bottle parameterization
# def klein_bottle(u, v):
#     x = (3 + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v)) * np.cos(u)
#     y = (3 + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v)) * np.sin(u)
#     z = np.sin(u / 2) * np.sin(v) + np.cos(u / 2) * np.sin(2 * v)
#     return x, y, z
#
# # Generate the u, v values
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, 2 * np.pi, 100)
# u, v = np.meshgrid(u, v)
#
# # Get the Klein bottle surface points
# x, y, z = klein_bottle(u, v)
#
# # Plot the Klein bottle
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# ax.plot_surface(x, y, z, color='cyan', alpha=0.6, rstride=5, cstride=5)
#
# # Define the critical trace on the surface (example trace, can be adjusted)
# # Highlighted in red
# critical_u = np.linspace(0, 2 * np.pi, 100)
# critical_v = np.pi / 2
# critical_x, critical_y, critical_z = klein_bottle(critical_u, critical_v)
#
# ax.plot(critical_x, critical_y, critical_z, color='red', linewidth=3)
#
# # Set labels and title
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Klein Bottle with Critical Trace')
#
# plt.show()
