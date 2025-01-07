import numpy as np
import plotly.graph_objects as go

# Define parameters for optimized curve
omega_optimized = 1.6524444079044858  # Optimized omega value
theta_vals = np.linspace(0, 2 * np.pi, 1000)
A_val, r_0_val = 1, 0

# Calculate coordinates using the optimized omega value
x_vals_optimized = (A_val * np.sin(omega_optimized * theta_vals) + r_0_val)**2 * np.cos(omega_optimized * theta_vals)
y_vals_optimized = (A_val * np.sin(omega_optimized * theta_vals) + r_0_val)**2 * np.sin(omega_optimized * theta_vals)
z_vals_optimized = np.sin(2 * theta_vals)

# Plot the optimized parametric curve
fig_optimized = go.Figure()

# Add the optimized 3D surface to the plot
fig_optimized.add_trace(go.Scatter3d(
    x=x_vals_optimized, y=y_vals_optimized, z=z_vals_optimized,
    mode='lines',
    line=dict(color=z_vals_optimized, colorscale='Jet', width=4),
    name='Optimized Space-Time Curvature'
))

# Update the layout for better visualization
fig_optimized.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Curvature (Z)',
    ),
    title='Optimized Space-Time Curvature Visualization'
)

# Show the figure
fig_optimized.show()

# import numpy as np
# import plotly.graph_objects as go
#
# # Define a function to represent the space-time curvature sheet
# def space_time_curvature(theta, omega):
#     """
#     Generate a 3D surface representing space-time curvature influenced by the icosahedron model.
#     We use a simplified form where the curvature depends on angular displacement and frequency.
#     """
#     R = (np.cos(omega * theta))**2  # Simplified curvature function
#     x = R * np.cos(theta)
#     y = R * np.sin(theta)
#     z = np.sin(2 * theta)
#     return x, y, z
#
# # Parameters for the visualization
# theta = np.linspace(0, 2 * np.pi, 1000)
# omega = ((1 + np.sqrt(5)) / 2)**2 # Golden ratio, representing the icosahedron symmetry
#
# # Generate the space-time curvature surface
# x, y, z = space_time_curvature(theta, omega)
#
# # Create a 3D plot using Plotly
# fig = go.Figure()
#
# # Add the 3D surface to the plot
# fig.add_trace(go.Scatter3d(
#     x=x, y=y, z=z,
#     mode='lines',
#     line=dict(color=z, colorscale='Viridis', width=4),
#     name='Space-Time Curvature'
# ))
#
# # Update the layout for better visualization
# fig.update_layout(
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Curvature (Z)',
#     ),
#     title='Space-Time Curvature Visualization: icosahedron-influenced Field'
# )
#
# # Show the figure
# fig.show()
