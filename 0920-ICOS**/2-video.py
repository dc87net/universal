import math
import numpy as np
import plotly.graph_objects as go

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 10**4)  # Angular displacement

# Example values for amplitude and base radius
A_value = 1  # Amplitude of oscillation
r0_value = 1  # Base radius
omega_base = (1 + np.sqrt(5)) / 2  # Example: golden ratio

# Initial parametric equations based on derived shape
R = (A_value * np.sin(omega_base * theta) + r0_value)**6  # Scaled radius with Fourier components
x = R * np.cos(omega_base * theta)
y = R * np.sin(omega_base * theta)
z = np.sin(2 * theta)  # Variation in z-axis

# Calculate magnitude and derivative
r = np.sqrt(x**2 + y**2 + z**2)
dr_dtheta = np.gradient(r, theta)

# Exponential scaling based on derivative
omega_adjusted = np.exp(dr_dtheta)

# Adjusted parametric equations
x_adjusted = R * np.cos(omega_adjusted * theta)
y_adjusted = R * np.sin(omega_adjusted * theta)
z_adjusted = np.sin(2 * theta)

# Normalize derivative for color mapping
norm_dr_dtheta = (dr_dtheta - np.min(dr_dtheta)) / (np.max(dr_dtheta) - np.min(dr_dtheta))

# Define camera settings for animation
camera_path_x = x_adjusted
camera_path_y = y_adjusted
camera_path_z = z_adjusted

# Create figure for animation
fig = go.Figure()

# Add path to figure
fig.add_trace(go.Scatter3d(
    x=x_adjusted, y=y_adjusted, z=z_adjusted,
    mode='lines',
    line=dict(
        color=norm_dr_dtheta,  # Color based on normalized derivative
        colorscale='Jet',      # Color scale
        width=5                # Line width
    ),
    name='Path through Momentum Space'
))

# Initial camera position
initial_camera = dict(
    eye=dict(x=camera_path_x[0], y=camera_path_y[0], z=camera_path_z[0])
)

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='3D Animation: Riding Through the Wormhole',
    scene_camera=initial_camera
)

# Function to update camera position along the path
frames = []
for i in range(1, len(camera_path_x), 10):  # Update every 10th point for smoother animation
    camera_position = dict(
        eye=dict(x=camera_path_x[i], y=camera_path_y[i], z=camera_path_z[i])
    )
    frames.append(go.Frame(layout=dict(scene_camera=camera_position)))

# Add frames to animation
fig.frames = frames

# Animation settings
fig.update_layout(
    updatemenus=[dict(type='buttons',
                      showactive=False,
                      buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None, dict(frame=dict(duration=50, redraw=True),
                                                     fromcurrent=True,
                                                     mode='immediate')])])])

# Display the animation
fig.show()
