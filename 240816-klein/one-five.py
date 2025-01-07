import numpy as np
import plotly.graph_objects as go


# Update the transformation function with specific values
def transformed_klein_bottle(u, v, R=np.pi, a=np.pi / 4, b=np.pi / 4):
    cos_u_half = np.cos(a * u / 2)
    sin_u_half = np.sin(a * u / 2)
    sin_v = np.sin(b * v)
    sin_2v = np.sin(b * 2 * v)

    real_part = cos_u_half * sin_v - sin_u_half * sin_2v
    imag_part = sin_u_half * sin_v + cos_u_half * sin_2v

    x = (R + real_part) * np.cos(u)
    y = (R + real_part) * np.sin(u)
    z = imag_part

    return x, y, z


# Generate the grid
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

# Calculate the surface
x, y, z = transformed_klein_bottle(u, v)

# Project onto a 2D plane
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])

# Adjust the view for the desired projection
fig.update_layout(
    scene=dict(
        camera=dict(eye=dict(x=0, y=0, z=2)),  # Looking down the z-axis for projection
    )
)

fig.show()
