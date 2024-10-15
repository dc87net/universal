import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 10**6)

# Angular frequency that changes with respect to the derivative
omega = 7  # Base angular frequency

# Initial parametric equations
R = np.cos(omega * theta)  # Radius changing with cos(omega * theta)
x = R * np.cos(omega * theta)
y = R * np.sin(omega * theta)
z = np.sin(2 * theta)

# Calculate the magnitude (resultant) of the position vector
r = np.sqrt(x**2 + y**2 + z**2)

# Calculate the derivative of the resultant (dr/dtheta)
dr_dtheta = np.gradient(r, theta)

# Introduce exponential scaling based on the derivative
# This scales the angular frequency based on the current derivative
omega_adjusted = np.exp(dr_dtheta)

# New parametric equations where omega varies with the derivative
x_adjusted = R * np.cos(omega_adjusted * theta)
y_adjusted = R * np.sin(omega_adjusted * theta)
z_adjusted = np.sin(2 * theta)

# Normalize the derivative for color mapping
norm_dr_dtheta = (dr_dtheta - np.min(dr_dtheta)) / (np.max(dr_dtheta) - np.min(dr_dtheta))

# Create a 3D plot using Plotly
fig = go.Figure()

# Add the parametric curve to the plot with false coloring based on derivative
fig.add_trace(go.Scatter3d(
    x=x_adjusted, y=y_adjusted, z=z_adjusted,
    mode='lines',
    line=dict(
        color=norm_dr_dtheta,    # Color based on the normalized derivative
        colorscale='Jet',        # ROYGBIV-like color scale
        width=5                 # Line width
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
    title='3D Parametric Visualization with Exponentially Adjusted Angular Frequency',
)

# Set up the initial camera position, looking along the Y-axis for XZ projection
camera = dict(
    eye=dict(x=2.5, y=0.001, z=2.5),  # Small non-zero y to avoid a singular perspective
    up=dict(x=0, y=1, z=0)  # Ensuring the Z-axis is up
)

fig.update_layout(scene_camera=camera)

# Set up animation parameters for smooth rotation (30 frames per second)
frames = []
n_seconds = 5  # Duration of the animation in seconds
fps = 30  # Frames per second
n_frames = n_seconds * fps  # Total number of frames
angle_step = 2 * np.pi / n_frames  # Angle step for each frame

# Generate frames for the animation
for i in range(n_frames):
    angle = i * angle_step
    # Camera rotates around z-axis, looking at the origin, with the same projection against the XZ plane
    new_camera = dict(
        eye=dict(x=2.5 * np.cos(angle), y=0.001, z=2.5 * np.sin(angle))
    )
    frames.append(go.Frame(layout=dict(scene_camera=new_camera)))

# Add frames to the figure and configure the animation settings
fig.frames = frames

fig.update_layout(
    updatemenus=[dict(type='buttons',
                      showactive=False,
                      buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None, dict(frame=dict(duration=1000/fps, redraw=True),
                                                     fromcurrent=True, mode='immediate')])])])

# Display the figure with animation
fig.show()
