import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Define constants
A = 1        # Amplitude of oscillation
r0 = 1       # Base radius
phi = np.pi / 3   # Example value for phi (60 degrees)
theta = np.linspace(0, np.pi, 1000)  # Theta varies from 0 to pi
u = np.linspace(0, 2 * np.pi, 1000)  # u varies from 0 to 2pi

# Create meshgrid for theta and u to compute over all combinations
U, Theta = np.meshgrid(u, theta)

# Compute R(u)
R = A * np.sin(U) + r0

# Compute Normalized Shadow Areas
A_xy_norm = (R ** 2) * (np.sin(phi) ** 2) * np.sin(Theta) * np.cos(Theta)
A_xz_norm = (R ** 2) * (np.sin(2 * phi - Theta) + np.sin(2 * phi + Theta)) / 4
A_yz_norm = (R ** 2) * (np.cos(2 * phi - Theta) - np.cos(2 * phi + Theta)) / 4

# Compute Normalized Shadow Volume
V_shadow_norm = (R ** 6) * (np.sin(phi) ** 4) * (np.sin(Theta) ** 2) * (np.cos(phi) ** 2) * (np.cos(Theta) ** 2)

# For visualization, we'll plot V_shadow_norm as a function of u and theta
# We'll use a 3D surface plot

# Prepare data for plotting
X = U
Y = Theta
Z = V_shadow_norm

# Create a 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')])

# Update layout
fig.update_layout(
    title='Normalized Shadow Volume V_shadow_norm(u, θ)',
    scene=dict(
        xaxis_title='u (ωt)',
        yaxis_title='θ (theta)',
        zaxis_title='V_shadow_norm',
    ),
    autosize=False,
    width=800,
    height=800,
)

# Show the figure
fig.show()


# Choose a specific value of theta for plotting normalized shadow areas vs. u
theta_fixed = np.pi / 4  # 45 degrees
theta_index = np.abs(theta - theta_fixed).argmin()

# Extract data for the fixed theta
u_values = u
A_xy_norm_fixed_theta = A_xy_norm[theta_index, :]
A_xz_norm_fixed_theta = A_xz_norm[theta_index, :]
A_yz_norm_fixed_theta = A_yz_norm[theta_index, :]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(u_values, A_xy_norm_fixed_theta, label='A_xy_norm')
plt.plot(u_values, A_xz_norm_fixed_theta, label='A_xz_norm')
plt.plot(u_values, A_yz_norm_fixed_theta, label='A_yz_norm')
plt.title('Normalized Shadow Areas vs. u (at θ = 45°)')
plt.xlabel('u (ωt)')
plt.ylabel('Normalized Shadow Area')
plt.legend()
plt.grid(True)
plt.show()
