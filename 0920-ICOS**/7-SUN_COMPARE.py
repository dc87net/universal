# spacetime_visualization.py

import numpy as np
import plotly.graph_objects as go
from scipy.spatial import ConvexHull
from math import sqrt

# Constants
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
c = 2.99792458e8         # Speed of light (m/s)
pi = np.pi

# Parameters for the icosahedron
mass = 1.989e30          # Total mass equivalent to the Sun (kg)
num_moles = 1.97e33      # Number of moles calculated
scale_factor = num_moles # Scaling the effect by the number of moles

# Spatial grid
grid_size = 100                                    # Resolution of the grid
x_range = y_range = np.linspace(-10, 10, grid_size) # Space in arbitrary units
X, Y = np.meshgrid(x_range, y_range)
R = np.sqrt(X**2 + Y**2)  # Radial distance from the center

# Avoid division by zero at the center
R[R == 0] = 1e-6

# Calculate the spacetime curvature (simplified for visualization)
# We'll use a gravitational potential analog: Phi = -G * M / R
# And represent the curvature as a deformation: Z = scaling_factor * Phi / c^2
Phi = -G * mass * scale_factor / R
Z = Phi / c**2  # Deformation of the spacetime "sheet"

# Generate vertices of an icosahedron
t = (1.0 + sqrt(5.0)) / 2.0

vertices = np.array([
    [-1,  t,  0],
    [ 1,  t,  0],
    [-1, -t,  0],
    [ 1, -t,  0],
    [ 0, -1,  t],
    [ 0,  1,  t],
    [ 0, -1, -t],
    [ 0,  1, -t],
    [ t,  0, -1],
    [ t,  0,  1],
    [-t,  0, -1],
    [-t,  0,  1],
])

# Create a ConvexHull to get the faces of the icosahedron
hull = ConvexHull(vertices)

# Create the 3D surface plot
fig = go.Figure()

# Add the spacetime curvature surface
fig.add_trace(go.Surface(
    x=X,
    y=Y,
    z=Z,
    colorscale='Viridis',
    colorbar=dict(title='Spacetime Curvature'),
    showscale=True,
    opacity=0.9,
    name='Spacetime Curvature'
))

# Add the icosahedron mesh to the figure
fig.add_trace(go.Mesh3d(
    x=vertices[:,0],
    y=vertices[:,1],
    z=vertices[:,2],
    i=hull.simplices[:,0],
    j=hull.simplices[:,1],
    k=hull.simplices[:,2],
    color='gold',
    opacity=1.0,
    name='Icosahedron'
))

# Update the layout for better visualization
fig.update_layout(
    title='Spacetime Curvature Caused by Scaled Icosahedra',
    scene=dict(
        xaxis_title='X (arbitrary units)',
        yaxis_title='Y (arbitrary units)',
        zaxis_title='Curvature Deformation (Z)',
        xaxis=dict(
            backgroundcolor="black",
            gridcolor="gray",
            showbackground=True,
            zerolinecolor="gray",
        ),
        yaxis=dict(
            backgroundcolor="black",
            gridcolor="gray",
            showbackground=True,
            zerolinecolor="gray",
        ),
        zaxis=dict(
            backgroundcolor="black",
            gridcolor="gray",
            showbackground=True,
            zerolinecolor="gray",
        ),
    ),
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=65, r=50, b=65, t=90),
    scene_camera=dict(
        eye=dict(x=1.5, y=1.5, z=1.5)
    )
)

# Export the plot to an HTML file suitable for a web server
fig.write_html("spacetime_curvature_visualization.html")

# Optionally, display the plot in a browser
fig.show()
