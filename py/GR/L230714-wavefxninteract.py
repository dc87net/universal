import numpy as np
import plotly.graph_objs as go

# TUNABLES
V0 = 1.0        # Depth of the potential well
k = 1.0         # Determines the width of the well
omega = 1.0     # Angular frequency
t = np.linspace(0, 10, 400)   # t, Time
x = np.linspace(-5, 5, 400)         # x, Space
R0 = 1.0  # Initial value for R(t)
# CONSTANTS
G = 6.67430e-11     # G,  Gravitational Constant (m^3 kg^-1 s^-2)
c = 3.0e8           # C,  Speed of Light         (m/s)
M_sun = 1.989e30    # M☉, Mass of Sun            (kg)
M = 10 * M_sun      # M,  Mass of the black hole (kg)

# Create meshgrid for 3D plotting
X, T = np.meshgrid(x, t)

# Function to calculate R(t)
def R(t, d):
    if d % 2 == 0:
        return R0 * t**2
    else:
        return R0 * t**3

# Visualize d = 3 (time-evolving)
d = 3
V_X = -V0 * np.tanh(k * X)**2
cos_part = np.cos(k * X - omega * T)
sin_part = (1j ** d) * np.sin(k * X - omega * T)
wave_function = R(T, d) * (cos_part + sin_part)
real_part = np.real(wave_function)
imag_part = np.imag(wave_function)
probability_distribution = np.abs(wave_function)**2
probability_distribution /= np.max(probability_distribution)

# Real part of the wave function
real_surface = go.Surface(z=real_part, x=X, y=T, colorscale='Inferno', name='Real Part', opacity=0.7)

# Imaginary part of the wave function
imag_surface = go.Surface(z=imag_part, x=X, y=T, colorscale='Turbo', name='Imaginary Part', opacity=0.7)

# Probability distribution with false color
probability_surface = go.Surface(z=probability_distribution, x=X, y=T, colorscale='Plasma_r', name='Probability Distribution', opacity=0.7)

# Combined plot of real and imaginary parts
combined_surface = go.Surface(z=real_part + imag_part, x=X, y=T, colorscale='Magma', name='Combined Real and Imaginary Parts', opacity=0.7)

# Create subplots
fig = go.Figure()


fig.add_trace(probability_surface)  # Add probability distribution
fig.add_trace(real_surface)         # Add real part of the wave function
fig.add_trace(imag_surface)         # Add imaginary part of the wave function
# fig.add_trace(combined_surface)     # Add combined surface of real and imaginary parts

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

fig.update_layout(layout)

# Show the interactive plot
fig.show()