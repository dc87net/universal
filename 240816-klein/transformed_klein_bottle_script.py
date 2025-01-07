
import numpy as np
import matplotlib.pyplot as plt

# Define the parametric equations with the exponential transformation
def transformed_klein_bottle(u, v, R=1):
    # Incorporating the exponential form based on the given transformation
    cos_u_half = np.cos(u / 2)
    sin_u_half = np.sin(u / 2)
    sin_v = np.sin(v)
    sin_2v = np.sin(2 * v)

    real_part = cos_u_half * sin_v - sin_u_half * sin_2v
    imag_part = sin_u_half * sin_v + cos_u_half * sin_2v
    
    x = (R + real_part) * np.cos(u)
    y = (R + real_part) * np.sin(u)
    z = imag_part
    
    return x, y, z

# Apply the hyperbolic stretching function for the radial coordinate
def hyperbolic_stretching(t, alpha=0.2):
    return np.exp(alpha * t)

# Generate the cross-sectional slice for a given point with updated transformation
def draw_transformed_klein_cross_section(t, label):
    # Generate the parametric grid
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    u, v = np.meshgrid(u, v)
    
    # Apply the hyperbolic stretching
    R = hyperbolic_stretching(t)
    
    # Calculate the Klein bottle coordinates with the transformation
    x, y, z = transformed_klein_bottle(u, v, R)
    
    # Plot the cross-sectional slice
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='g', alpha=0.7, rstride=5, cstride=5, edgecolor='k')

    # Add labels and title
    ax.set_title(f"Transformed Klein Bottle Cross-Section at Point {label}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set limits for better visualization
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    
    plt.show()

# Example Usage: Drawing cross-sectional slice at Point B with the updated transformation
draw_transformed_klein_cross_section(1, 'B')
