import numpy as np
import plotly.graph_objs as go
import plotly.figure_factory as ff

# Parameters for the wave function and potential
V0 = 1.0  # Depth of the potential well
k = 1.0   # Determines the width of the well
omega = 1.0  # Angular frequency
d = 1  # Dimensional factor (integer)
t = np.linspace(0, 10, 400)  # Time
x = np.linspace(-5, 5, 400)  # Space

# Create meshgrid for 3D plotting
X, T = np.meshgrid(x, t)

# Potential well using hyperbolic tangent function
V_X = -V0 * np.tanh(k * X)**2

# Wave function components
real_part = np.cos(k * X - omega * T)
imag_part = (1j ** d) * np.sin(k * X - omega * T)

# Calculate the probability distribution (square of the amplitude)
probability_distribution = np.abs(real_part + imag_part)**2

# Create 3D surface plot for potential well
potential_surface = go.Surface(z=V_X, x=X, y=T, colorscale='Viridis', name='Potential Well')

# Create 3D surface plot for probability distribution
probability_surface = go.Surface(z=probability_distribution, x=X, y=T, colorscale='Plasma', name='Probability Distribution')

# Define the layout for the plot
layout = go.Layout(
    title='Interactive Visualization of Spacetime Curvature and Wave Function',
    scene=dict(
        xaxis_title='Space (x)',
        yaxis_title='Time (t)',
        zaxis_title='Amplitude/Probability'
    ),
    width=1000,
    height=700
)

# Combine both surfaces into a single figure
fig = go.Figure(data=[potential_surface, probability_surface], layout=layout)

# Show the interactive plot
fig.show()
