import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define the parametric equations with the exponential transformation
def transformed_klein_bottle(u, v, R=1, a=1, b=1):
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

# Generate the 2D projections with adjustable angles
def draw_interactive_2d_projections(t, label, a=1, b=1, alpha=0.2):
    # Generate the parametric grid
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)

    # Apply the hyperbolic stretching
    R = hyperbolic_stretching(t, alpha=alpha)

    # Calculate the Klein bottle coordinates with the transformation
    x, y, z = transformed_klein_bottle(u, v, R, a, b)

    # Create subplots for the 2D projections
    fig = make_subplots(rows=1, cols=3, subplot_titles=('Projection on XY Plane', 'Projection on XZ Plane', 'Projection on YZ Plane'))

    # Projection on XY plane (view from +∞ along z-axis)
    fig.add_trace(go.Scatter(x=x.flatten(), y=y.flatten(), mode='markers', marker=dict(size=2, color='blue')), row=1, col=1)

    # Projection on XZ plane (view from +∞ along y-axis)
    fig.add_trace(go.Scatter(x=x.flatten(), y=z.flatten(), mode='markers', marker=dict(size=2, color='green')), row=1, col=2)

    # Projection on YZ plane (view from +∞ along x-axis)
    fig.add_trace(go.Scatter(x=y.flatten(), y=z.flatten(), mode='markers', marker=dict(size=2, color='red')), row=1, col=3)

    # Set initial viewing angles
    initial_theta = 0
    initial_phi = 0

    # Update layout for better visualization
    fig.update_layout(
        title_text=f"Interactive 2D Projections of Transformed Klein Bottle at Point {label}",
        showlegend=False,
        sliders=[
            {
                "currentvalue": {"prefix": "Theta: "},
                "pad": {"t": 50},
                "steps": [
                    {
                        "args": [dict(scene_camera=dict(eye=dict(x=np.cos(t), y=np.sin(t), z=initial_phi)))],
                        "label": f"{np.round(t, 2)}",
                        "method": "relayout",
                    } for t in np.linspace(0, 2 * np.pi, 30)
                ],
            },
            {
                "currentvalue": {"prefix": "Phi: "},
                "pad": {"t": 20},
                "steps": [
                    {
                        "args": [dict(scene_camera=dict(eye=dict(x=initial_theta, y=np.cos(p), z=np.sin(p))))],
                        "label": f"{np.round(p, 2)}",
                        "method": "relayout",
                    } for p in np.linspace(0, 2 * np.pi, 30)
                ],
            }
        ]
    )

    fig.show()

# Example Usage: Drawing interactive 2D projections at Point B with the updated transformation
draw_interactive_2d_projections(1, 'B', a=np.pi/4, b=np.pi/4, alpha=0.3)
