# # # import numpy as np
# # # import plotly.graph_objs as go
# # # from plotly.subplots import make_subplots
# # #
# # # # Define the complex number in terms of x
# # # def complex_magnitude_phase(x):
# # #     real_part = np.pi**2 / (x**2 + 4)
# # #     imag_part = -2 * np.pi / (x**2 + 4)
# # #     magnitude = np.sqrt(real_part**2 + imag_part**2)
# # #     phase = np.arctan2(imag_part, real_part)
# # #     return magnitude, phase
# # #
# # # # Generate values of x for the plot
# # # x_values = np.linspace(-10, 10, 400)
# # #
# # # # Compute magnitude and phase for each x
# # # magnitude_values, phase_values = complex_magnitude_phase(x_values)
# # #
# # # # Create a 3D scatter plot
# # # fig = make_subplots(specs=[[{'is_3d': True}]])
# # #
# # # # Plot magnitude and phase vs. x
# # # trace = go.Scatter3d(
# # #     x=x_values,
# # #     y=magnitude_values,
# # #     z=phase_values,
# # #     mode='lines',
# # #     line=dict(color='blue', width=2),
# # # )
# # #
# # # # Add the trace to the figure
# # # fig.add_trace(trace)
# # #
# # # # Set the layout for the 3D plot
# # # fig.update_layout(
# # #     scene=dict(
# # #         xaxis_title="X (Real Domain)",
# # #         yaxis_title="Magnitude",
# # #         zaxis_title="Phase (Radians)",
# # #         aspectmode="cube",  # Ensures equal scaling for all axes
# # #     ),
# # #     title="3D Plot of Complex Magnitude and Phase",
# # # )
# # #
# # # # Show the plot
# # # fig.show()
# #
# #
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D
# #
# # # Define the complex number in terms of x
# # def complex_magnitude_phase(x):
# #     real_part = np.pi**2 / (x**2 + 4)
# #     imag_part = -2 * np.pi / (x**2 + 4)
# #     magnitude = np.sqrt(real_part**2 + imag_part**2)
# #     phase = np.arctan2(imag_part, real_part)
# #     return magnitude, phase
# #
# # # Generate values of x for the plot
# # x_values = np.linspace(-10, 10, 400)
# #
# # # Compute magnitude and phase for each x
# # magnitude_values, phase_values = complex_magnitude_phase(x_values)
# #
# # # Create 3D plot to visualize the complex number in polar form
# # fig = plt.figure(figsize=(8, 8))
# # ax = fig.add_subplot(111, projection='3d')
# #
# # # Plot the real (x), magnitude (y), and phase (z) as a 3D plot
# # ax.plot(x_values, magnitude_values, phase_values, color='b')
# #
# # # Labels and title
# # ax.set_xlabel('X (Real Domain)')
# # ax.set_ylabel('Magnitude')
# # ax.set_zlabel('Phase (Rad)')
# # ax.set_title('3D Representation of Complex Number in Polar Form')
# #
# # # Set equal scaling for axes
# # ax.set_box_aspect([1, 1, 1])
# #
# # # Show the plot
# # plt.show()

import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots


# Parameterize the spherical coordinates
def spherical_coords(x):
    real_part = np.pi ** 2 / (x ** 2 + 4)
    imag_part = -2 * np.pi / (x ** 2 + 4)

    # Magnitude (r) is the radial distance
    r = np.sqrt(real_part ** 2 + imag_part ** 2)

    # Azimuthal angle (theta), arctan of imaginary over real part
    theta = np.arctan2(imag_part, real_part)

    # Polar angle (phi), representing the z-axis angle (in spherical coordinates)
    phi = np.pi / 2  # Since we're working in the xy-plane, phi is pi/2

    return r, theta, phi


# Generate values of x for the plot
x_values = np.linspace(-10, 10, 400)

# Compute spherical coordinates for each x
r_values, theta_values, phi_values = spherical_coords(x_values)

# Convert spherical to Cartesian for plotting
x_cartesian = r_values * np.sin(phi_values) * np.cos(theta_values)
y_cartesian = r_values * np.sin(phi_values) * np.sin(theta_values)
z_cartesian = r_values * np.cos(phi_values)

# Create a 3D scatter plot
fig = make_subplots(specs=[[{'is_3d': True}]])

# Plot magnitude and phase vs. x
trace = go.Scatter3d(
    x=x_cartesian,
    y=y_cartesian,
    z=z_cartesian,
    mode='lines',
    line=dict(color='blue', width=2),
)

# Add the trace to the figure
fig.add_trace(trace)

# Set the layout for the 3D plot
fig.update_layout(
    scene=dict(
        xaxis_title="X (Real Domain)",
        yaxis_title="Y (Real Domain)",
        zaxis_title="Z (Real Domain)",
        aspectmode="cube",  # Ensures equal scaling for all axes
    ),
    title="3D Plot in Spherical Coordinates",
)

# Show the plot
fig.show()
