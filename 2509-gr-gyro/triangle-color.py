import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 10**5)
##NO## omega = (1+5**(1/2))/2  # Angular frequency
omega = 8
# Angular frequency
R = np.cos(omega * theta)  # Assume the radius is changing with c os(omega * theta)

# Parametric equations for x, y, z
x = R * np.cos(omega * theta)
y = R * np.sin(omega * theta)
z = R * np.sin(2 * theta)  # Some variation in Z for visualization

# Calculate the magnitude (resultant) of the position vector
r = np.sqrt(x**2 + y**2 + z**2)

# Calculate the derivative of the resultant (dr/dtheta)
dr_dtheta = np.gradient(r, theta)

# Normalize the derivative for color mapping
norm_dr_dtheta = (dr_dtheta - np.min(dr_dtheta)) / (np.max(dr_dtheta) - np.min(dr_dtheta))

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot with false coloring based on derivative
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines',
    line=dict(
        color=norm_dr_dtheta,    # Color based on the normalized derivative
        colorscale='Jet',        # Choose a color scale, e.g., Jet for ROYGBIV-like colors
        width=5                 # Line width
    ),
    name='Parametric Curve'
))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Parametric Visualization with False Coloring (Based on Derivative)',
)

# Display the figure
fig.show()
