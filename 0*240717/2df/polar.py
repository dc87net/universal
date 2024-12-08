import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots

# Define the function f(x) = cos(x) + i * sin(cos(x) + i * sin(x))
def f(x):
    z = np.cos(x) + 1j * np.sin(x)
    sin_z = np.sin(z)
    return np.cos(x) + 1j * sin_z

# Generate x values
num_points = 1000
x_values = np.linspace(0, 2 * np.pi, num_points)
f_values = f(x_values)

# Extract real and imaginary parts
real = np.real(f_values)
imag = np.imag(f_values)

# Compute magnitude and angle
magnitude = np.abs(f_values)
angle = np.angle(f_values)
angle_unwrapped = np.unwrap(angle)  # To prevent angle discontinuities
angle_deg = np.degrees(angle_unwrapped)  # Convert to degrees for polar plot

# Determine ranges with padding
magnitude_min, magnitude_max = magnitude.min(), magnitude.max()

padding_mag = 0.1 * (magnitude_max - magnitude_min)

magnitude_min -= padding_mag
magnitude_max += padding_mag

# Create subplots: 1 row, 2 columns (Polar and Cartesian)
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "polar"}, {"type": "scatter"}]],
    subplot_titles=("Polar Representation", "Complex Plane Evolution")
)

# --- Left Subplot: Polar Plot ---

# Add Polar Path (static)
fig.add_trace(
    go.Scatterpolar(
        r=magnitude,
        theta=angle_deg,
        mode='lines',
        line=dict(color='lightgray', dash='dash'),
        name='Polar Path'
    ),
    row=1, col=1
)

# Add Polar Trail (initially empty)
polar_trail = go.Scatterpolar(
    r=[],
    theta=[],
    mode='lines',
    line=dict(color='blue', width=2),
    name='Polar Trail'
)
fig.add_trace(
    polar_trail,
    row=1, col=1
)

# Add Polar Moving Point (initial point)
polar_point = go.Scatterpolar(
    r=[magnitude[0]],
    theta=[angle_deg[0]],
    mode='markers',
    marker=dict(color='blue', size=10),
    name='Current Position'
)
fig.add_trace(
    polar_point,
    row=1, col=1
)

# --- Right Subplot: Cartesian Plot ---

# Add Cartesian Path (static)
fig.add_trace(
    go.Scatter(
        x=real,
        y=imag,
        mode='lines',
        line=dict(color='lightgray', dash='dash'),
        name='Complex Path'
    ),
    row=1, col=2
)

# Add Cartesian Trail (initially empty)
cartesian_trail = go.Scatter(
    x=[],
    y=[],
    mode='lines',
    line=dict(color='red', width=2),
    name='Complex Trail'
)
fig.add_trace(
    cartesian_trail,
    row=1, col=2
)

# Add Cartesian Moving Point (initial point)
cartesian_point = go.Scatter(
    x=[real[0]],
    y=[imag[0]],
    mode='markers',
    marker=dict(color='red', size=10),
    name='Current Position'
)
fig.add_trace(
    cartesian_point,
    row=1, col=2
)

# Create frames for animation
frames = []
for k in range(num_points):
    frame = go.Frame(
        data=[
            # Polar Trail up to current frame
            go.Scatterpolar(
                r=magnitude[:k+1],
                theta=angle_deg[:k+1],
                mode='lines',
                line=dict(color='blue', width=2),
                name='Polar Trail'
            ),
            # Polar Moving Point
            go.Scatterpolar(
                r=[magnitude[k]],
                theta=[angle_deg[k]],
                mode='markers',
                marker=dict(color='blue', size=10),
                name='Current Position'
            ),
            # Cartesian Trail up to current frame
            go.Scatter(
                x=real[:k+1],
                y=imag[:k+1],
                mode='lines',
                line=dict(color='red', width=2),
                name='Complex Trail'
            ),
            # Cartesian Moving Point
            go.Scatter(
                x=[real[k]],
                y=[imag[k]],
                mode='markers',
                marker=dict(color='red', size=10),
                name='Current Position'
            )
        ],
        name=str(k)
    )
    frames.append(frame)

fig.frames = frames

# Define animation buttons
animation_buttons = [
    dict(
        label="Play",
        method="animate",
        args=[None, {"frame": {"duration": 20, "redraw": True},
                     "fromcurrent": True,
                     "transition": {"duration": 0}}]
    ),
    dict(
        label="Pause",
        method="animate",
        args=[[None], {"frame": {"duration": 0, "redraw": False},
                       "mode": "immediate",
                       "transition": {"duration": 0}}]
    )
]

# Update layout with fixed axis ranges and buttons
fig.update_layout(
    updatemenus=[dict(
        type="buttons",
        buttons=animation_buttons,
        showactive=False,
        y=1.05,
        x=1.15
    )],
    # Set fixed ranges for polar plot (radial axis only)
    polar=dict(
        radialaxis=dict(
            range=[magnitude_min, magnitude_max],
            showticklabels=True,
            ticks='outside',
            title='|f(x)|'
        ),
        angularaxis=dict(
            direction='clockwise',
            rotation=90,
            tickmode='linear',
            tick0=np.degrees(x_values[0]),
            dtick=30,
            title='arg(f(x)) [degrees]'
        )
    ),
    # Set fixed ranges for Cartesian plot
    xaxis2=dict(
        title='Re(f(x))',
        range=[real.min() - 0.1 * (real.max() - real.min()), real.max() + 0.1 * (real.max() - real.min())]
    ),
    yaxis2=dict(
        title='Im(f(x))',
        range=[imag.min() - 0.1 * (imag.max() - imag.min()), imag.max() + 0.1 * (imag.max() - imag.min())]
    ),
    showlegend=False,
    height=600,
    width=1200
)

# Display the figure
pio.show(fig)



# # import numpy as np
# # import plotly.graph_objs as go
# # import plotly.io as pio
# #
# # # Define the function f(x) = cos(x) + i * sin(cos(x) + i * sin(x))
# # def f(x):
# #     z = np.cos(x) + 1j * np.sin(x)
# #     sin_z = np.sin(z)
# #     return np.cos(x) + 1j * sin_z
# #
# # # Generate x values from 0 to 2*pi
# # num_points = 1000
# # x_values = np.linspace(0, 2 * np.pi, num_points)
# # f_values = f(x_values)
# #
# # # Extract magnitude and angle
# # magnitude = np.abs(f_values)
# # angle = np.angle(f_values)
# # angle_unwrapped = np.unwrap(angle)  # To prevent angle discontinuities
# #
# # # Determine axis ranges with padding
# # magnitude_min, magnitude_max = magnitude.min(), magnitude.max()
# # angle_min, angle_max = angle_unwrapped.min(), angle_unwrapped.max()
# #
# # padding_mag = 0.1 * (magnitude_max - magnitude_min)
# # padding_ang = 0.1 * (angle_max - angle_min)
# #
# # magnitude_min -= padding_mag
# # magnitude_max += padding_mag
# # angle_min -= padding_ang
# # angle_max += padding_ang
# #
# # # Create a scatter trace for the complete path in polar coordinates
# # path = go.Scatterpolar(
# #     r=magnitude,
# #     theta=np.degrees(angle_unwrapped),  # Convert radians to degrees
# #     mode='lines',
# #     line=dict(color='lightgray', dash='dash'),
# #     name='Path of f(x)'
# # )
# #
# # # Create a scatter trace for the moving point with hover information
# # point = go.Scatterpolar(
# #     r=[magnitude[0]],
# #     theta=[np.degrees(angle_unwrapped[0])],
# #     mode='markers',
# #     marker=dict(color='blue', size=10),
# #     name='f(x)',
# #     hoverinfo='text',
# #     text=[f"x = {x_values[0]:.2f}<br>|f(x)| = {magnitude[0]:.2f}<br>arg(f(x)) = {np.degrees(angle_unwrapped[0]):.2f}°"]
# # )
# #
# # # Create the figure with polar layout
# # fig = go.Figure(data=[path, point],
# #                 layout=go.Layout(
# #                     title='Polar Evolution of $f(x) = \cos(x) + i \sin(\cos(x) + i \sin(x))$',
# #                     polar=dict(
# #                         radialaxis=dict(
# #                             range=[magnitude_min, magnitude_max],
# #                             showticklabels=True,
# #                             ticks='outside',
# #                             title='|f(x)|'
# #                         ),
# #                         angularaxis=dict(
# #                             range=[angle_min, angle_max],
# #                             direction='clockwise',
# #                             rotation=90,
# #                             tickmode='linear',
# #                             tick0=np.degrees(x_values[0]),
# #                             dtick=30,
# #                             title='arg(f(x)) [degrees]'
# #                         )
# #                     ),
# #                     showlegend=False,
# #                     updatemenus=[dict(
# #                         type='buttons',
# #                         buttons=[
# #                             dict(
# #                                 label='Play',
# #                                 method='animate',
# #                                 args=[None, {"frame": {"duration": 20, "redraw": True},
# #                                              "fromcurrent": True}]
# #                             ),
# #                             dict(
# #                                 label='Pause',
# #                                 method='animate',
# #                                 args=[[None], {"frame": {"duration": 0, "redraw": False},
# #                                                "mode": "immediate",
# #                                                "transition": {"duration": 0}}]
# #                             )
# #                         ],
# #                         direction="left",
# #                         pad={"r": 10, "t": 87},
# #                         showactive=False,
# #                         x=0.1,
# #                         xanchor="right",
# #                         y=0,
# #                         yanchor="top"
# #                     )]
# #                 ))
# #
# # # Create frames for animation
# # frames = []
# # for k in range(num_points):
# #     frame = go.Frame(
# #         data=[
# #             go.Scatterpolar(
# #                 r=[magnitude[k]],
# #                 theta=[np.degrees(angle_unwrapped[k])],
# #                 mode='markers',
# #                 marker=dict(color='blue', size=10),
# #                 text=[f"x = {x_values[k]:.2f}<br>|f(x)| = {magnitude[k]:.2f}<br>arg(f(x)) = {np.degrees(angle_unwrapped[k]):.2f}°"],
# #                 hoverinfo='text'
# #             )
# #         ],
# #         name=str(k)
# #     )
# #     frames.append(frame)
# #
# # fig.frames = frames
# #
# # # Display the figure
# # pio.show(fig)
#
# import numpy as np
# import plotly.graph_objs as go
# import plotly.io as pio
# from plotly.subplots import make_subplots
#
# # Define the function f(x) = cos(x) + i * sin(cos(x) + i * sin(x))
# def f(x):
#     z = np.cos(x) + 1j * np.sin(x)
#     sin_z = np.sin(z)
#     return np.cos(x) + 1j * sin_z
#
# # Generate x values
# num_points = 1000
# x_values = np.linspace(0, 2 * np.pi, num_points)
# f_values = f(x_values)
#
# # Extract real and imaginary parts
# real = np.real(f_values)
# imag = np.imag(f_values)
#
# # Compute magnitude and angle
# magnitude = np.abs(f_values)
# angle = np.angle(f_values)
# angle_unwrapped = np.unwrap(angle)  # To prevent angle discontinuities
# angle_deg = np.degrees(angle_unwrapped)  # Convert to degrees for polar plot
#
# # Determine ranges with padding
# magnitude_min, magnitude_max = magnitude.min(), magnitude.max()
# angle_min, angle_max = angle_deg.min(), angle_deg.max()
#
# padding_mag = 0.1 * (magnitude_max - magnitude_min)
# padding_ang = 10  # Degrees
#
# magnitude_min -= padding_mag
# magnitude_max += padding_mag
# angle_min -= padding_ang
# angle_max += padding_ang
#
# # Create subplots: 1 row, 2 columns (Polar and Cartesian)
# fig = make_subplots(
#     rows=1, cols=2,
#     specs=[[{"type": "polar"}, {"type": "scatter"}]],
#     subplot_titles=("Polar Representation", "Complex Plane Evolution")
# )
#
# # --- Left Subplot: Polar Plot ---
#
# # Add Polar Path (static)
# fig.add_trace(
#     go.Scatterpolar(
#         r=magnitude,
#         theta=angle_deg,
#         mode='lines',
#         line=dict(color='lightgray', dash='dash'),
#         name='Polar Path'
#     ),
#     row=1, col=1
# )
#
# # Add Polar Trail (initially empty)
# polar_trail = go.Scatterpolar(
#     r=[],
#     theta=[],
#     mode='lines',
#     line=dict(color='blue', width=2),
#     name='Polar Trail'
# )
# fig.add_trace(
#     polar_trail,
#     row=1, col=1
# )
#
# # Add Polar Moving Point (initial point)
# polar_point = go.Scatterpolar(
#     r=[magnitude[0]],
#     theta=[angle_deg[0]],
#     mode='markers',
#     marker=dict(color='blue', size=10),
#     name='Current Position'
# )
# fig.add_trace(
#     polar_point,
#     row=1, col=1
# )
#
# # --- Right Subplot: Cartesian Plot ---
#
# # Add Cartesian Path (static)
# fig.add_trace(
#     go.Scatter(
#         x=real,
#         y=imag,
#         mode='lines',
#         line=dict(color='lightgray', dash='dash'),
#         name='Complex Path'
#     ),
#     row=1, col=2
# )
#
# # Add Cartesian Trail (initially empty)
# cartesian_trail = go.Scatter(
#     x=[],
#     y=[],
#     mode='lines',
#     line=dict(color='red', width=2),
#     name='Complex Trail'
# )
# fig.add_trace(
#     cartesian_trail,
#     row=1, col=2
# )
#
# # Add Cartesian Moving Point (initial point)
# cartesian_point = go.Scatter(
#     x=[real[0]],
#     y=[imag[0]],
#     mode='markers',
#     marker=dict(color='red', size=10),
#     name='Current Position'
# )
# fig.add_trace(
#     cartesian_point,
#     row=1, col=2
# )
#
# # Create frames for animation
# frames = []
# for k in range(num_points):
#     frame = go.Frame(
#         data=[
#             # Polar Trail up to current frame
#             go.Scatterpolar(
#                 r=magnitude[:k+1],
#                 theta=angle_deg[:k+1],
#                 mode='lines',
#                 line=dict(color='blue', width=2),
#                 name='Polar Trail'
#             ),
#             # Polar Moving Point
#             go.Scatterpolar(
#                 r=[magnitude[k]],
#                 theta=[angle_deg[k]],
#                 mode='markers',
#                 marker=dict(color='blue', size=10),
#                 name='Current Position'
#             ),
#             # Cartesian Trail up to current frame
#             go.Scatter(
#                 x=real[:k+1],
#                 y=imag[:k+1],
#                 mode='lines',
#                 line=dict(color='red', width=2),
#                 name='Complex Trail'
#             ),
#             # Cartesian Moving Point
#             go.Scatter(
#                 x=[real[k]],
#                 y=[imag[k]],
#                 mode='markers',
#                 marker=dict(color='red', size=10),
#                 name='Current Position'
#             )
#         ],
#         name=str(k)
#     )
#     frames.append(frame)
#
# fig.frames = frames
#
# # Define animation buttons
# animation_buttons = [
#     dict(
#         label="Play",
#         method="animate",
#         args=[None, {"frame": {"duration": 20, "redraw": True},
#                      "fromcurrent": True,
#                      "transition": {"duration": 0}}]
#     ),
#     dict(
#         label="Pause",
#         method="animate",
#         args=[[None], {"frame": {"duration": 0, "redraw": False},
#                        "mode": "immediate",
#                        "transition": {"duration": 0}}]
#     )
# ]
#
# # Update layout with fixed axis ranges and buttons
# fig.update_layout(
#     title="Comprehensive Visualization of Thing",
#     updatemenus=[dict(
#         type="buttons",
#         buttons=animation_buttons,
#         showactive=False,
#         y=1.05,
#         x=1.15
#     )],
#     # Set fixed ranges for polar plot
#     polar=dict(
#         radialaxis=dict(
#             range=[magnitude_min, magnitude_max],
#             showticklabels=True,
#             ticks='outside',
#             title='|f(x)|'
#         ),
#         angularaxis=dict(
#             range=[angle_min, angle_max],
#             direction='clockwise',
#             rotation=90,
#             tickmode='linear',
#             tick0=np.degrees(x_values[0]),
#             dtick=30,
#             title='arg(f(x)) [degrees]'
#         )
#     ),
#     # Set fixed ranges for Cartesian plot
#     xaxis2=dict(
#         title='Re(f(x))',
#         range=[real.min() - 0.1 * (real.max() - real.min()), real.max() + 0.1 * (real.max() - real.min())]
#     ),
#     yaxis2=dict(
#         title='Im(f(x))',
#         range=[imag.min() - 0.1 * (imag.max() - imag.min()), imag.max() + 0.1 * (imag.max() - imag.min())]
#     ),
#     showlegend=False,
#     height=600,
#     width=1200
# )
#
# # Display the figure
# pio.show(fig)
