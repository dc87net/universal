import numpy as np
import plotly.graph_objects as go

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 299792458  # Speed of light (m/s)
pi = np.pi

# Parameters for angular velocity and theta
omega_vals = np.linspace(0.1, 10, 50)  # Range of angular velocities
theta_vals = np.linspace(0, 2 * np.pi, 50)  # Range of theta values

# Create meshgrid for omega and theta
omega_grid, theta_grid = np.meshgrid(omega_vals, theta_vals)

# Calculate G_theta_theta for each combination of omega and theta
G_theta_theta_vals = (3.2 * pi * G * omega_grid**2) / c**4

# Set up the 3D surface plot
fig = go.Figure(data=[go.Surface(
    x=omega_grid,
    y=theta_grid,
    z=G_theta_theta_vals,
    colorscale='Jet',
    colorbar=dict(title='G_θθ'),
    contours=dict(
        z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)
    ),
)])

# Update plot layout
fig.update_layout(
    title='Einstein Tensor Component G_θθ as a Function of Angular Velocity and Theta',
    scene=dict(
        xaxis_title='Angular Velocity (ω)',
        yaxis_title='Theta (θ)',
        zaxis_title='G_θθ',
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

# Show plot
fig.show()
