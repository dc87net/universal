import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 100)
omega = 1  # Angular frequency
R = np.cos(omega * theta)  # Assume the radius is constant

# Parametric equations
x = R * np.cos(omega * theta)
y = R * np.sin(omega * theta)
z = R * np.sin(2 * theta)  # Some variation in Z for visualization

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name='Parametric Curve'))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Parametric Visualization of the Rotating Triangle System',
)

# Display the figure
fig.show()
input("t")
