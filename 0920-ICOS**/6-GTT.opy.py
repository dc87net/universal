import numpy as np
import plotly.graph_objects as go

# Define a grid for the space-time visualization
x, y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))

# Example function using G_theta_theta to modify curvature
def custom_gravity(x, y, G_theta_theta, scaling_factor=1):
    """
    Compute space-time curvature using the provided G_theta_theta values.
    This function represents the calculated space-time deformation.
    """
    r = np.sqrt(x**2 + y**2)
    z = -scaling_factor * G_theta_theta / (r + 0.1)  # Simplified curvature function using G_theta_theta
    return z

# Substituting actual G_theta_theta values (example placeholder values)
# In practice, use the calculated G_theta_theta values here.
G_theta_theta_values = 1e-42  # Example value, replace with your actual G_theta_theta results

# Compute the traditional gravity surface
#z_traditional = tra

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Space-Time Curvature',
    ),
    title='Space-Time Curvature with Calculated G_theta_theta',
    showlegend=True
)

# Show the plot
fig.show()
