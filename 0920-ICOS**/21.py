import plotly.graph_objects as go
import numpy as np

# Parameters for the visualization
A_value = 1  # Example amplitude value
r0_value = 1  # Example base radius value
omega_values = np.linspace(-10, 10, 10**5)  # Frequency range for visualization

# Calculate the Fourier Transform components for the given omega range
F_omega = (
    2 * np.pi * r0_value**6
    + 15 * np.pi * A_value**2 * r0_value**4
    + 11.25 * np.pi * A_value**4 * r0_value**2
    + 0.625 * np.pi * A_value**6
)

# For simplicity, we use a constant value for visualization, in reality, we'd evaluate over omega

# Parametric coordinates based on Fourier components
x_momentum = omega_values
y_momentum = F_omega * np.cos(omega_values)
z_momentum = F_omega * np.sin(omega_values)

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot with color based on the magnitude of F_omega
fig.add_trace(go.Scatter3d(
    x=x_momentum, y=y_momentum, z=z_momentum,
    mode='lines',
    line=dict(
        color=np.abs(F_omega),        # Color based on the magnitude of the Fourier Transform
        colorscale='Jet',        # ROYGBIV-like color scale
        width=5                 # Line width
    ),
    name='Momentum Space Visualization'
))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='Omega (Frequency)',
        yaxis_title='Real Part',
        zaxis_title='Imaginary Part',
    ),
    title='3D Visualization of Momentum Space with Fourier Transform',
)

# Display the figure
fig.show()
