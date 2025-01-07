import plotly.graph_objects as go
import numpy as np

# Parameters for the parametric equations
theta = np.linspace(0, 2 * np.pi, 100)
omega = 2  # Angular frequency
R = np.cos(omega * theta)  # Assume the radius is changing with cos(omega * theta)

# Parametric equations for x, y, z
x = R * np.cos(omega * theta)
y = R * np.sin(omega * theta)
z = R * np.sin(2 * theta)  # Some variation in Z for visualization

# Project along the line x = y = z
# The projection involves collapsing along the vector (1, 1, 1)
# Normalize projection onto (1, 1, 1)
projection = (x + y + z) / np.sqrt(3)

# Project orthogonally onto a 2D plane (perpendicular to x=y=z line)
# For this, we keep the "perpendicular" components by subtracting projection
proj_x = x - projection / np.sqrt(3)
proj_y = y - projection / np.sqrt(3)

# Create a 2D plot using Plotly
fig = go.Figure()

# Add the 2D projection (rotated curve) to the plot
fig.add_trace(go.Scatter(
    x=proj_x, y=proj_y,
    mode='lines',
    line=dict(
        width=5  # Line width
    ),
    marker=dict(
        color=np.linspace(0, 1, len(proj_x)),    # Color mapping based on position
        colorscale='Jet',                       # Use ROYGBIV-like colorscale
        showscale=True                          # Show color bar
    ),
    name='Diagonal Projection Curve (x=y=z)'
))

# Update the layout for better visualization
fig.update_layout(
    xaxis_title='Projected X',
    yaxis_title='Projected Y',
    title='Projection along the x=y=z Line with ROYGBIV Coloring',
)

# Display the figure
fig.show()
