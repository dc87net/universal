import math
import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 1000)
phi = np.pi / 3  # Example fixed value for phi (60 degrees)
omega = 2  # Base angular frequency

# Derived normalized equations for shadow areas
R = (1 * np.sin(omega * theta) + 1)  # A = 1, r_0 = 1 as example values
A_xy_norm = (R**2) * (np.sin(phi)**2) * (np.sin(theta) * np.cos(theta))
A_xz_norm = (R**2) * (np.sin(2 * phi - theta) + np.sin(2 * phi + theta)) / 4
A_yz_norm = (R**2) * (np.cos(2 * phi - theta) - np.cos(2 * phi + theta)) / 4

# Normalized shadow volume based on the above
V_shadow_norm = (R**6) * (np.sin(phi)**4) * (np.sin(theta)**2) * (np.cos(phi)**2) * (np.cos(theta)**2)

# For visualization, scale and use derived expressions
x = A_xy_norm * np.cos(theta)
y = A_xy_norm * np.sin(theta)
z = A_yz_norm  # Using one component for simplicity

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot with false coloring based on V_shadow_norm
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(
        color=V_shadow_norm,        # Color based on the normalized shadow volume
        colorscale='Jet',        # ROYGBIV-like color scale
        width=5                 # Line width
    ),
    name='Normalized Shadow Volume'
))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Visualization with Normalized Shadow Volume Scaling',
)

# Display the figure
fig.show()
