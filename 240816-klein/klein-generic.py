import numpy as np
import plotly.graph_objects as go


# Define the parametric equations with the exponential transformation
def transformed_klein_bottle(u, v, R=1, a=1, b=1):
    # Incorporating the exponential form based on the given transformation
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


# Apply the hyperbolic stretching function for the radial coordinate
def hyperbolic_stretching(t, alpha=0.2):
    return np.exp(alpha * t)


# Generate the cross-sectional slice for a given point with updated transformation
def draw_transformed_klein_cross_section(t, label, a=1, b=1, alpha=0.2):
    # Generate the parametric grid
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)

    # Apply the hyperbolic stretching
    R = hyperbolic_stretching(t, alpha=alpha)

    # Calculate the Klein bottle coordinates with the transformation
    x, y, z = transformed_klein_bottle(u, v, R, a, b)

    # Create the 3D surface plot
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])

    # Add labels and title
    fig.update_layout(
        title=f"Transformed Klein Bottle Cross-Section at Point {label}",
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            xaxis=dict(range=[-3, 3]),
            yaxis=dict(range=[-3, 3]),
            zaxis=dict(range=[-3, 3])
        ),
    )

    fig.show()


# Example Usage: Drawing cross-sectional slice at Point B with the updated transformation
draw_transformed_klein_cross_section(1, 'B', a=.78539816339, b=.78539816339, alpha=0.3)
