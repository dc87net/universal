import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
G = 6.67430e-11  # Gravitational constant
M = 1.989e30  # Mass of the black hole (e.g., 1 solar mass)
c = 3.00e8  # Speed of light in vacuum
Q = 1.602e-19  # Elementary charge (for the sake of the example)


# Define the scale factor function (example form)
def scale_factor(t):
    return 1 + 0.1 * t  # Simple linear scale factor for demonstration


# Define the metric tensor determinant function (example form)
def g_t(t):
    return -1 + 0.1 * np.sin(t)


# Scaling function
def R(t):
    return np.sqrt(-g_t(t))


# Define the grid for x and y
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
x, y = np.meshgrid(x, y)

# Create a figure and axis for the plot
fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')


# Function to update the plot for each frame
def update(frame):
    ax1.clear()
    ax2.clear()

    t = frame / 20  # Adjust the time scale for the animation
    rt = R(t)
    a_t = scale_factor(t)
    z_real = np.cosh((x ** 2 / a_t ** 2) + t) - np.sinh((y ** 2 / a_t ** 2) + t)
    z_imag = np.sinh((x ** 2 / a_t ** 2) + t) + np.cosh((y ** 2 / a_t ** 2) + t)

    # Real part
    ax1.plot_surface(x, y, z_real, cmap='viridis', edgecolor='none')
    ax1.set_xlabel('X axis')
    ax1.set_ylabel('Y axis')
    ax1.set_zlabel('Z axis')
    ax1.set_title('Hyperbolic Elliptic Paraboloid (Real Part)')

    # Imaginary part
    ax2.plot_surface(x, y, z_imag, cmap='plasma', edgecolor='none')
    ax2.set_xlabel('X axis')
    ax2.set_ylabel('Y axis')
    ax2.set_zlabel('Z axis')
    ax2.set_title('Hyperbolic Elliptic Paraboloid (Imaginary Part)')

    return ax1, ax2


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, blit=False)

# Save the animation as a GIF
ani.save('wave_function_evolution.gif', writer='imagemagick', fps=20)

# Alternatively, you can save it as a video
# ani.save('wave_function_evolution.mp4', writer='ffmpeg', fps=20)

plt.show()