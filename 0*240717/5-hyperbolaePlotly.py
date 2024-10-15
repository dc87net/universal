import numpy as np
import plotly.graph_objects as go

RESOLUTION = 10**4

# Define the ranges for x (real part) and y (imaginary part)
x_range = np.linspace(-2, 2, RESOLUTION)
y_range = np.linspace(-2, 2, 10)
x, y = np.meshgrid(x_range, y_range)

# Complex numbers z = x + iy
z = x + 1j*y
z_conj = np.conj(z)

# Define the cosine and sine functions of complex z and its conjugate
cos_z = np.cos(np.pi * z / 2)
sin_z_conj = np.imag(1)*np.sin(np.pi * z_conj / 2)

# Calculate the magnitude squared for cosine and sine
cos2_z = np.abs(cos_z)**2
sin2_z_conj = np.abs(sin_z_conj)**2

# Compute the sum cos^2(zπ/2) + sin^2(z*π/2)
sum_cos_sin = cos2_z + sin2_z_conj

# Create a 3D surface plot to visualize
fig = go.Figure()

fig.add_trace(go.Surface(
    z=sum_cos_sin,
    x=x, y=y,
    colorscale='Viridis',
    contours={"z": {"show": True, "start": 0, "end": 2, "size": 0.25}}
))

# Add labels and titles
fig.update_layout(
    title="Visualization of cos²(zπ/2) + sin²(z*π/2)",
    scene=dict(
        xaxis_title="Real part (x)",
        yaxis_title="Imaginary part (y)",
        zaxis_title="Sum (cos² + sin²)"
    )
)

# Save the plot as an interactive HTML file
fig.write_html("plot_cos_sin.html")

# Display the figure
fig.show()
