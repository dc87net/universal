import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 100)
omega = 1  # Angular frequency
phaseShift = np.pi / 4  # Phase shift for rotation

# Define rotation with complex exponential
R = np.cos(omega * theta)  # Assume the radius is constant
rotatedR = R * np.exp(1j * phaseShift)  # Apply rotation

# Real and Imaginary components after rotation
x = np.real(rotatedR) * np.cos(omega * theta)
y = np.real(rotatedR) * np.sin(omega * theta)
z = np.imag(rotatedR) * np.sin(2 * theta)  # Variation in Z for balance check

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', name='Rotated Parametric Curve'))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Rotated Parametric Visualization of the System',
)

# Display the figure
fig.show()
