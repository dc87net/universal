import math
import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 10**5)  # Angular displacement

# Using derived parameters from our Fourier Transform calculations
# Example values for amplitude and base radius
A_value = 1  # Amplitude of oscillation
r0_value = 1  # Base radius

# Define angular frequency (example: golden ratio)
omega_base = (1 + np.sqrt(5)) / 2

# Initial parametric equations based on Fourier Transform insights
R = (A_value * np.sin(omega_base * theta) + r0_value)**6  # Scaled radius with the Fourier components
x = R * np.cos(omega_base * theta)
y = R * np.sin(omega_base * theta)
z = np.sin(2 * theta)  # Similar variation in z-axis as the example

# Calculate the magnitude of the position vector
r = np.sqrt(x**2 + y**2 + z**2)

# Calculate the derivative of the magnitude with respect to theta
dr_dtheta = np.gradient(r, theta)

# Introduce exponential scaling based on the derivative
omega_adjusted = np.exp(dr_dtheta)  # Adjust angular frequency with exponential scaling

# New parametric equations with adjusted frequency
x_adjusted = R * np.cos(omega_adjusted * theta)
y_adjusted = R * np.sin(omega_adjusted * theta)
z_adjusted = np.sin(2 * theta)

# Normalize the derivative for color mapping
norm_dr_dtheta = (dr_dtheta - np.min(dr_dtheta)) / (np.max(dr_dtheta) - np.min(dr_dtheta))

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot with color based on the normalized derivative
fig.add_trace(go.Scatter3d(
    x=x_adjusted, y=y_adjusted, z=z_adjusted,
    mode='lines',
    line=dict(
        color=norm_dr_dtheta,  # Color based on the normalized derivative
        colorscale='Jet',      # ROYGBIV-like color scale
        width=5                # Line width
    ),
    name='Parametric Curve with Exponential Scaling'
))

# Update the layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Parametric Visualization in Momentum Space',
)

# Display the figure
fig.show()
