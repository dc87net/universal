# # import numpy as np
# # import matplotlib.pyplot as plt
# # import matplotlib.animation as animation
# #
# # import matplotlib
# # # matplotlib.use('TkAgg')  # or 'Agg' if saving only
# #
# # # Define the function f(x) = cos(x) + i * sin(cos(x) + i * sin(x))
# # def f(x):
# #     # Compute z = cos(x) + i sin(x)
# #     z = np.cos(x) + 1j * np.sin(x)
# #
# #     # Compute sin(z) using numpy's sin function for complex numbers
# #     sin_z = np.sin(z)
# #
# #     # Compute f(x) = cos(x) + i * sin(z)
# #     return np.cos(x) + 1j * sin_z
# #
# #
# # # Generate x values from 0 to 2*pi
# # num_points = 1000  # Increased for smoother animation
# # x_values = np.linspace(0, 2 * np.pi, num_points)
# # f_values = f(x_values)
# #
# # # Extract real and imaginary parts
# # real = np.real(f_values)
# # imag = np.imag(f_values)
# #
# # # Set up the figure and axis
# # fig, ax = plt.subplots(figsize=(8, 8))
# # ax.set_xlim(np.min(real) - 1, np.max(real) + 1)
# # ax.set_ylim(np.min(imag) - 1, np.max(imag) + 1)
# # ax.set_xlabel('Re(f(x))')
# # ax.set_ylabel('Im(f(x))')
# # ax.set_title('Evolution of $f(x) = cos(x) + i sin(cos(x) + i sin(x))$')
# #
# # # Plot the entire path as a light gray line
# # ax.plot(real, imag, color='lightgray', linestyle='--', label='Path of f(x)')
# #
# # # Initialize the point and trail
# # point, = ax.plot([], [], 'bo', label='$f(x)$')
# # trail, = ax.plot([], [], 'b-', linewidth=2, label='Trail')
# #
# # # Initialize legend
# # ax.legend()
# #
# #
# # # Initialization function for the animation
# # def init():
# #     point.set_data([], [])
# #     trail.set_data([], [])
# #     return point, trail
# #
# #
# # # Animation function which updates figure data
# # def animate(i):
# #     # Current point
# #     current_x = real[i]
# #     current_y = imag[i]
# #     point.set_data(current_x, current_y)
# #
# #     # Trail up to the current point
# #     trail.set_data(real[:i + 1], imag[:i + 1])
# #     return point, trail
# #
# #
# # # Number of frames
# # num_frames = len(x_values)
# #
# # # # Create the animation
# # ani = animation.FuncAnimation(fig, animate, frames=num_frames,
# #                               init_func=init, blit=True, interval=20, repeat=True)
# #
# # # Uncomment the following lines to save the animation as an MP4 file
# # # Requires ffmpeg installed on your system
# # # ani.save('function_evolution.mp4', writer='ffmpeg', fps=30)
# # #
# # # Display the animation
# # plt.show()
#
#
# import numpy as np
# import plotly.graph_objs as go
# import plotly.io as pio
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
# # Create a scatter trace for the path
# path = go.Scatter(
#     x=real,
#     y=imag,
#     mode='lines',
#     line=dict(color='lightgray', dash='dash'),
#     name='Path of f(x)'
# )
#
# # Create a scatter trace for the moving point
# point = go.Scatter(
#     x=[real[0]],
#     y=[imag[0]],
#     mode='markers',
#     marker=dict(color='blue', size=10),
#     name='f(x)'
# )
#
# # Create the figure
# fig = go.Figure(data=[path, point],
#                 layout=go.Layout(
#                     title='Evolution of $f(x) = \cos(x) + i \sin(\cos(x) + i \sin(x))$',
#                     xaxis_title='Re(f(x))',
#                     yaxis_title='Im(f(x))',
#                     updatemenus=[dict(type='buttons',
#                                       buttons=[dict(label='Play',
#                                                     method='animate',
#                                                     args=[None, {"frame": {"duration": 20, "redraw": True},
#                                                                  "fromcurrent": True}]),
#                                                dict(label='Pause',
#                                                     method='animate',
#                                                     args=[[None], {"frame": {"duration": 0, "redraw": False},
#                                                                    "mode": "immediate",
#                                                                    "transition": {"duration": 0}}])])]
#                 ))
#
# # Create frames for animation
# frames = [go.Frame(data=[go.Scatter(x=[real[k]], y=[imag[k]], mode='markers',
#                                    marker=dict(color='blue', size=10))],
#                    name=str(k)) for k in range(num_points)]
#
# fig.frames = frames
#
# # Display the figure
# pio.show(fig)

import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

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

# Determine the range for axes
real_min, real_max = real.min(), real.max()
imag_min, imag_max = imag.min(), imag.max()

# Add some padding to the ranges for better visualization
padding = 0.1  # 10% padding
real_range = real_max - real_min
imag_range = imag_max - imag.min()
real_min -= padding * real_range
real_max += padding * real_range
imag_min -= padding * imag_range
imag_max += padding * imag_range

# Create a color scale based on x to visualize progression
colors = x_values / (2 * np.pi)  # Normalize x to [0,1]

# Create a scatter trace for the path
path = go.Scatter(
    x=real,
    y=imag,
    mode='lines',
    line=dict(color='lightgray', dash='dash'),
    name='Path of f(x)'
)

# Create a scatter trace for the moving point
point = go.Scatter(
    x=[real[0]],
    y=[imag[0]],
    mode='markers',
    marker=dict(color='blue', size=10),
    name='f(x)'
)

# Create the figure with fixed axis ranges
fig = go.Figure(data=[path, point],
                layout=go.Layout(
                    title='Evolution of $f(x) = \cos(x) + i \sin(\cos(x) + i \sin(x))$',
                    xaxis=dict(title='Re(f(x))', range=[real_min, real_max],
                               scaleanchor='y', scaleratio=1),
                    yaxis=dict(title='Im(f(x))', range=[imag_min, imag_max]),
                    updatemenus=[dict(type='buttons',
                                      buttons=[dict(label='Play',
                                                    method='animate',
                                                    args=[None, {"frame": {"duration": 20, "redraw": True},
                                                                 "fromcurrent": True}]),
                                               dict(label='Pause',
                                                    method='animate',
                                                    args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                                   "mode": "immediate",
                                                                   "transition": {"duration": 0}}])])]
                ))

# Create frames for animation
frames = [go.Frame(data=[go.Scatter(x=[real[k]], y=[imag[k]], mode='markers',
                                   marker=dict(color='blue', size=10))],
                   name=str(k)) for k in range(num_points)]

fig.frames = frames

# Update layout to maintain aspect ratio across all frames
fig.update_layout(
    xaxis=dict(
        scaleanchor="y",
        scaleratio=1,
        range=[real_min, real_max]
    ),
    yaxis=dict(
        range=[imag_min, imag_max]
    )
)

# Display the figure
pio.show(fig)
