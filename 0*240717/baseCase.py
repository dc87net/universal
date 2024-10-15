import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pyparsing import alphas
from sympy.abc import alpha

# Constants
r = 1  # Constant radius
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
phi = np.linspace(0, np.pi, 100)  # Polar angle

# Create a meshgrid
Theta, Phi = np.meshgrid(theta, phi)

# Compute Cartesian coordinates
X = r * np.sin(Phi) * np.cos(Theta)
Y = r * np.sin(Phi) * np.sin(Theta)
Z = r * np.cos(Phi)

# Compute the function values
F = np.exp(1j * np.exp(1j * Theta))  # Your function

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(np.angle(F) / (2 * np.pi)), linewidth=0, antialiased=False, alpha=0.4)

plt.show()


import numpy as np
import plotly.graph_objects as go

# Constants
r = 1  # Constant radius
theta = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
phi = np.linspace(0, np.pi, 100)  # Polar angle

# Create a meshgrid
Theta, Phi = np.meshgrid(theta, phi)

# Compute Cartesian coordinates
X = r * np.sin(Phi) * np.cos(Theta)
Y = r * np.sin(Phi) * np.sin(Theta)
Z = r * np.cos(Phi)

# Compute the function values
F = np.exp(1j * np.exp(1j * Theta))  # Your function

# Calculate the color values based on the angle of the complex function
angle_F = np.angle(F)

# Normalize angle_F to the range [0, 1] for **coloring**
normalized_angle = (angle_F + np.pi) / (2 * np.pi)

# Create the surface plot
fig = go.Figure(data=[go.Surface(
    x=X, y=Y, z=Z,
    surfacecolor=normalized_angle,
    colorscale='Jet',
    cmin=0, cmax=1,
    opacity=0.4
)])

# Update layout for better 3D visualization
fig.update_layout(
    title="3D Surface Plot",
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
)

# Show plot
fig.show()
