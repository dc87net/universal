import numpy as np
from mpmath import zeta, gamma, cos, pi, mp
import plotly.graph_objects as go

# Set precision
mp.dps = 25

# Custom symbolic zeta function method
def zeta_symbolic(t):
    s = complex(0.5, t)
    s_conjugate = complex(0.5, -t)
    return (2**(0.5 - 1j*t) * pi**(-(0.5 + 1j*t)) * cos(pi * (0.5 + 1j*t) / 2) *
            gamma(0.5 + 1j*t) * zeta(s_conjugate))

# Define the range for the imaginary part of s
t_values = np.linspace(0, 50, 1000)

# Compute symbolic zeta function values
zeta_vals = [zeta_symbolic(t) for t in t_values]

# Extract real and imaginary parts
real_parts = np.array([val.real for val in zeta_vals], dtype=float)
imag_parts = np.array([val.imag for val in zeta_vals], dtype=float)
amplitude = np.sqrt(real_parts**2 + imag_parts**2)

# Define the Hamiltonian representation
H = amplitude
theta = t_values
r = H
z_real = real_parts
z_imag = imag_parts

# Create a 3D plot using Plotly
fig = go.Figure()

# Plot the real part of the wave function in the Hamiltonian representation
fig.add_trace(go.Scatter3d(
    x=theta,
    y=r,
    z=z_real,
    mode='markers',
    marker=dict(size=2, color='blue'),
    name='Real Part'
))

# Plot the imaginary part of the wave function in the Hamiltonian representation
fig.add_trace(go.Scatter3d(
    x=theta,
    y=r,
    z=z_imag,
    mode='markers',
    marker=dict(size=2, color='green'),
    name='Imaginary Part'
))

# Customize the axes labels and title
fig.update_layout(
    scene=dict(
        xaxis_title='Theta (t)',
        yaxis_title='Hamiltonian (H)',
        zaxis_title='Amplitude'
    ),
    title='3D Visualization of Custom Zeta Function in Hamiltonian Representation'
)

# Show plot
fig.show()
fig.write_html("/Users/douglas/Downloads/zeta/zeta.htm")
fig.write_json("/Users/douglas/Downloads/zeta/zeta.json")
# fig.write_json("/Users/douglas/Downloads/zeta/v)
fig.sa
