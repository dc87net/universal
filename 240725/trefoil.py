import numpy as np
import plotly.graph_objects as go

# Define the parameter t
t = np.linspace(0, 2 * np.pi, 1000)

# Calculate the real and imaginary parts
realPart = np.sin(t) + 2 * np.sin(2 * t)
imaginaryPart = np.sin(t) + np.cos(2 * t)

# Create the 3D plot
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=realPart,
    y=t,  # Use t as the third dimension to trace the parametric path
    z=imaginaryPart,
    mode='lines',
    name='3D Parametric Plot'
))

fig.update_layout(
    title='3D Parametric Plot',
    scene=dict(
        xaxis_title='Real Part',
        yaxis_title='Parameter t',
        zaxis_title='Imaginary Part'
    )
)

# Show the plot
fig.show()