import numpy as np
import plotly.graph_objects as go

# Define the spherical coordinate function
def spherical_function(theta, phi):
    # Set z to π/4
    z = np.pi/4 #/4 # HOLE@ { (π,√2); (π/4,1); (0,√2); (3π,√2); (4π,); (5π,); (,); (,); (,); }
    i = complex(0, 1)
    # Calculate the complex function
    #complex_result = (i * np.cos(2 * z) + 1) * np.exp(i * z)
    #complex_result2 = (i * np.cos(2 * z) + 1)*np.conjugate(i * np.cos(2 * z) + 1) * np.exp(i * z)
    complex_result = (np.cos(z) + i*np.sin(z))* np.exp(i * z)

    # Convert complex result to polar form
    print(f"CX Result:\n\n{complex_result}\nMagnitude: {np.abs(complex_result)}\n\n")
    radius = np.abs(complex_result)
    return radius

# Define theta and phi ranges for spherical coordinates
theta_vals = np.linspace(0, 2 * np.pi, 100)
phi_vals = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta_vals, phi_vals)

# Calculate radius using the function above
radius = spherical_function(theta, phi)

# Convert spherical coordinates to Cartesian for plotting
x = radius * np.sin(phi) * np.cos(theta)
y = radius * np.sin(phi) * np.sin(theta)
z = radius * np.cos(phi)

# Plot with Plotly
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale="Jet")])
fig.update_layout(
    title='3D Plot, ',
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    )
)
fig.show()
