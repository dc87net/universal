import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def parametricEllipseComplex(a, b, t):
    """
    Define an ellipse in the complex plane using a parametric function.
    a: semi-major axis length
    b: semi-minor axis length
    t: parameter from 0 to 2*pi for a full ellipse
    Returns: Ellipse as a complex-valued array z(t) = x(t) + i*y(t)
    """
    return a * np.cos(t) + 1j * b * np.sin(t)


def rotateComplexCurve(curve, theta):
    """
    Rotate the complex curve in a 3D complex space using the phase shift (theta).
    - theta: rotation angle around the z-axis in the complex plane
    Returns: Rotated complex-valued curve.
    """
    return curve * np.exp(1j * theta)


def plotPhasePlaneWithKeyPoints(curve, t):
    """
    Plot the phase plane with key points in t.
    - curve: The complex-valued curve to analyze.
    - t: The parameter array used to generate the curve.
    """
    # Calculate magnitude and phase (argument) of each point in the curve
    magnitude = np.abs(curve)
    phase = np.angle(curve)

    # Identify key points (e.g., peaks, troughs, zero-crossings of phase)
    key_indices = np.array([0, len(t) // 4, len(t) // 2, 3 * len(t) // 4, -1])  # Example key points based on t

    # Plot the phase plane (phase vs. magnitude) with trajectory
    plt.figure()
    plt.plot(phase, magnitude, label="Phase Plane")
    plt.scatter(phase[key_indices], magnitude[key_indices], color='red', zorder=5, label="Key Points")

    # Annotate key points with corresponding t values
    for idx in key_indices:
        plt.annotate(f"t={t[idx]:.2f}", (phase[idx], magnitude[idx]), textcoords="offset points", xytext=(5, 5),
                     ha='center')

    plt.xlabel("Phase (radians)")
    plt.ylabel("Magnitude")
    plt.title("Phase Plane Plot with Key Points")
    plt.grid(True)
    plt.legend()
    plt.show()


# Define ellipse parameters
a, b = 1, 0.5  # Semi-major and semi-minor axes

# Define rotation angles in radians
theta = np.pi / 4  # Rotate 45 degrees in the complex plane

# Define the parameter t for the ellipse
t = np.linspace(0, 2 * np.pi, 100)  # Parameter for the ellipse
ellipse = parametricEllipseComplex(a, b, t)

# Rotate the ellipse in the complex plane using theta
rotated_curve = rotateComplexCurve(ellipse, theta)

# Plot the phase plane with key points marked
plotPhasePlaneWithKeyPoints(rotated_curve, t)

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# def parametricEllipseComplex(a, b, t):
#     """
#     Define an ellipse in the complex plane using a parametric function.
#     a: semi-major axis length
#     b: semi-minor axis length
#     t: parameter from 0 to 2*pi for a full ellipse
#     Returns: Ellipse as a complex-valued array z(t) = x(t) + i*y(t)
#     """
#     return a * np.cos(t) + 1j * b * np.sin(t)
#
# def rotateComplexCurve(curve, theta, phi):
#     """
#     Rotate the complex curve in a 3D complex space.
#     - theta: rotation around one axis (in the "horizontal" complex plane)
#     - phi: rotation around the second axis (out of the horizontal plane)
#     Returns: Rotated curve as (x, y, z) coordinates
#     """
#     rotated_curve = curve * np.exp(1j * theta)  # Rotate in the complex plane
#
#     # Extract the real and imaginary parts after the first rotation
#     x = rotated_curve.real
#     y = rotated_curve.imag
#
#     # Create a third dimension z using phi
#     z = x * np.sin(phi)  # Map the real part to z-axis using phi
#     y = y * np.cos(phi)  # Adjust y component based on phi for a 3D rotation
#
#     return x, y, z, rotated_curve
#
# def plotPhasePlane(curve):
#     """
#     Plot the phase plane of a complex curve.
#     - curve: The complex-valued curve to analyze.
#     """
#     # Calculate magnitude and phase (argument) of each point in the curve
#     magnitude = np.abs(curve)
#     phase = np.angle(curve)
#
#     # Plot the phase plane (magnitude vs. phase)
#     plt.figure()
#     plt.plot(phase, magnitude, label="Phase Plane")
#     plt.xlabel("Phase (radians)")
#     plt.ylabel("Magnitude")
#     plt.title("Phase Plane Plot")
#     plt.grid(True)
#     plt.legend()
#     plt.show()
#
# def plotRotatedCurve3DAndPhase(a, b, theta, phi):
#     """
#     Plot the rotated parametric curve in 3D and its corresponding phase plane.
#     - a, b: Semi-major and semi-minor axes of the ellipse
#     - theta: rotation angle in the complex plane (around the z-axis)
#     - phi: rotation angle in the complex space (to introduce a third dimension)
#     """
#     # Define a parametric ellipse in the complex plane
#     t = np.linspace(0, 2 * np.pi, 100)  # Parameter for the ellipse
#     ellipse = parametricEllipseComplex(a, b, t)
#
#     # Rotate the ellipse in the complex space using theta and phi
#     x, y, z, rotated_curve = rotateComplexCurve(ellipse, theta, phi)
#
#     # Plot the 3D rotated curve
#     fig = plt.figure(figsize=(12, 6))
#     ax = fig.add_subplot(121, projection='3d')
#     ax.plot(x, y, z, label="3D Rotated Curve")
#     ax.set_xlabel("X axis")
#     ax.set_ylabel("Y axis")
#     ax.set_zlabel("Z axis")
#     ax.set_title("3D Complex Space Rotation")
#     ax.legend()
#
#     # Plot the phase plane
#     plt.subplot(122)
#     plotPhasePlane(rotated_curve)
#
# # Define the ellipse parameters
# a, b = 1, 0.5  # Semi-major and semi-minor axes
#
# # Define rotation angles in radians
# theta = np.pi / 4  # Rotate 45 degrees around the z-axis in the complex plane
# phi = np.pi / 6    # Tilt out of the plane by 30 degrees
#
# # Plot the rotated curve and its phase plane
# plotRotatedCurve3DAndPhase(a, b, theta, phi)
#
#
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D
# #
# # def parametricEllipseComplex(a, b, t):
# #     """
# #     Define an ellipse in the complex plane using a parametric function.
# #     a: semi-major axis length
# #     b: semi-minor axis length
# #     t: parameter from 0 to 2*pi for a full ellipse
# #     Returns: Ellipse as a complex-valued array z(t) = x(t) + i*y(t)
# #     """
# #     # Define the ellipse using a complex number representation
# #     return a * np.cos(t) + 1j * b * np.sin(t)
# #
# # def rotateComplexCurve(curve, theta, phi):
# #     """
# #     Rotate the complex curve in a 3D complex space.
# #     - theta: rotation around one axis (in the "horizontal" complex plane)
# #     - phi: rotation around the second axis (out of the horizontal plane)
# #     Returns: Rotated curve as (x, y, z) coordinates
# #     """
# #     # First, rotate the curve in the complex plane using a phase shift (rotation around z-axis)
# #     rotated_curve = curve * np.exp(1j * theta)
# #
# #     # Extract the real and imaginary parts after the first rotation
# #     x = rotated_curve.real
# #     y = rotated_curve.imag
# #
# #     # Introduce a second rotation out of the plane to create 3D complexity
# #     # Here, we use a simple trigonometric scaling to simulate a rotation into a third dimension
# #     z = x * np.sin(phi)  # Map the real part to z-axis using phi for the "vertical" tilt
# #
# #     # The y component can also be adjusted by phi to simulate a 3D rotation, if needed
# #     y = y * np.cos(phi)
# #
# #     return x, y, z
# #
# # def plotRotatedCurve3D(a, b, theta, phi):
# #     """
# #     Plot the rotated parametric curve in 3D complex space.
# #     - a, b: Semi-major and semi-minor axes of the ellipse
# #     - theta: rotation angle in the complex plane (around the z-axis)
# #     - phi: rotation angle in the complex space (to introduce a third dimension)
# #     """
# #     # Define a parametric ellipse in the complex plane
# #     t = np.linspace(0, 2 * np.pi, 100)  # Parameter for the ellipse
# #     ellipse = parametricEllipseComplex(a, b, t)
# #
# #     # Rotate the ellipse in the complex space using theta and phi
# #     x, y, z = rotateComplexCurve(ellipse, theta, phi)
# #
# #     # Plot the rotated curve in 3D
# #     fig = plt.figure()
# #     ax = fig.add_subplot(111, projection='3d')
# #     ax.plot(x, y, z, label=f"Rotated Curve (theta={theta} rad, phi={phi} rad)")
# #     ax.set_xlabel("X axis")
# #     ax.set_ylabel("Y axis")
# #     ax.set_zlabel("Z axis")
# #     plt.title("3D Complex Space Rotation")
# #     ax.legend()
# #     plt.show()
# #
# # # Define the ellipse parameters
# # a, b = 1, 0.5  # Semi-major and semi-minor axes
# #
# # # Define rotation angles in radians
# # theta = np.pi / 4  # Rotate 45 degrees around the z-axis in the complex plane
# # phi = np.pi / 6    # Tilt out of the plane by 30 degrees
# #
# # # Plot the rotated curve in 3D complex space
# # plotRotatedCurve3D(a, b, theta, phi)
# #
# #
# #
# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # from mpl_toolkits.mplot3d import Axes3D
# # #
# # #
# # # def parametricEllipseComplex(a, b, t):
# # #     """
# # #     Define an ellipse in the complex plane using a parametric function.
# # #     a: semi-major axis length
# # #     b: semi-minor axis length
# # #     t: parameter from 0 to 2*pi for a full ellipse
# # #     Returns: Ellipse as a complex-valued array z(t) = x(t) + i*y(t)
# # #     """
# # #     # Define the ellipse using a complex number representation
# # #     return a * np.cos(t) + 1j * b * np.sin(t)
# # #
# # #
# # # def rotateComplexCurve(curve, theta):
# # #     """
# # #     Rotate the complex curve by an angle theta using a complex phase shift.
# # #     - curve: the complex-valued curve (array of complex numbers)
# # #     - theta: angle to rotate the curve by, in radians
# # #     Returns: Rotated curve as a complex-valued array
# # #     """
# # #     # Apply the phase shift using complex multiplication
# # #     rotation = np.exp(1j * theta)  # Equivalent to e^(i*theta)
# # #     return curve * rotation
# # #
# # #
# # # def createEllipsoid(curve, phi):
# # #     """
# # #     Create a 3D ellipsoid by introducing a vertical displacement (z) based on phi.
# # #     - curve: the rotated complex-valued curve
# # #     - phi: angle that creates the 3D ellipsoid
# # #     Returns: (x, y, z) coordinates for the ellipsoid
# # #     """
# # #     # Extract real and imaginary components for the 2D ellipse
# # #     x, y = curve.real, curve.imag
# # #
# # #     # Introduce the third dimension z based on phi to create an ellipsoid shape
# # #     z = np.sin(phi) * y  # Scale the imaginary part by sin(phi) for the third dimension
# # #
# # #     return x, y, z
# # #
# # #
# # # def plotEllipsoid(a, b, theta, phi):
# # #     """
# # #     Plot the ellipsoid created by rotating an ellipse in 3D.
# # #     - a, b: Semi-major and semi-minor axes of the ellipse
# # #     - theta: rotation angle in the complex plane (around z-axis)
# # #     - phi: rotation angle to create the ellipsoid (out of the complex plane)
# # #     """
# # #     # Define the parametric ellipse in the complex plane
# # #     t = np.linspace(0, 2 * np.pi, 100)  # Parameter for the ellipse
# # #     ellipse = parametricEllipseComplex(a, b, t)
# # #
# # #     # Rotate the ellipse in the complex plane using theta
# # #     rotatedEllipse = rotateComplexCurve(ellipse, theta)
# # #
# # #     # Create the 3D ellipsoid by introducing the phi angle
# # #     x, y, z = createEllipsoid(rotatedEllipse, phi)
# # #
# # #     # Plot the 3D ellipsoid
# # #     fig = plt.figure()
# # #     ax = fig.add_subplot(111, projection='3d')
# # #     ax.plot(x, y, z, label=f"Ellipsoid (theta={theta} rad, phi={phi} rad)")
# # #     ax.set_xlabel("X axis")
# # #     ax.set_ylabel("Y axis")
# # #     ax.set_zlabel("Z axis")
# # #     plt.title("3D Ellipsoid from Complex Plane Rotation")
# # #     ax.legend()
# # #     plt.show()
# # #
# # #
# # # # Define the ellipse parameters
# # # a, b = 1, 0.5  # Semi-major and semi-minor axes
# # #
# # # # Define rotation angles in radians
# # # theta = np.pi / 4  # Rotate 45 degrees in the complex plane
# # # phi = np.pi / 6  # Tilt the ellipse to create an ellipsoid
# # #
# # # # Plot the resulting 3D ellipsoid
# # # plotEllipsoid(a, b, theta, phi)
# # #
# # # # import numpy as np
# # # # import matplotlib.pyplot as plt
# # # # from mpl_toolkits.mplot3d import Axes3D
# # # #
# # # #
# # # # def observerPerspectiveShell(r, theta, phi):
# # # #     """
# # # #     From the observer's perspective, convert (r, theta, phi) to Cartesian coordinates (x, y, z).
# # # #     Observer is at the origin, and angles correspond to 'looking around' and 'looking up/down'.
# # # #     """
# # # #     # Convert spherical coordinates to Cartesian coordinates
# # # #     x = r * np.sin(phi) * np.cos(theta)  # X-axis component
# # # #     y = r * np.sin(phi) * np.sin(theta)  # Y-axis component
# # # #     z = r * np.cos(phi)  # Z-axis component (vertical)
# # # #
# # # #     return x, y, z
# # # #
# # # #
# # # # def plotObserverShells(r_values, theta_res=100, phi_res=100):
# # # #     """
# # # #     Visualizes a series of shells centered at the observer's perspective.
# # # #     Each shell is plotted with varying theta and phi to form a spherical surface.
# # # #     """
# # # #     # Define the ranges for theta and phi (angles around the origin)
# # # #     theta = np.linspace(0, 2 * np.pi, theta_res)  # Full rotation around Z-axis
# # # #     phi = np.linspace(0, np.pi, phi_res)  # From top (0) to bottom (π) around Z-axis
# # # #
# # # #     # Create mesh grids for theta and phi
# # # #     theta, phi = np.meshgrid(theta, phi)
# # # #
# # # #     fig = plt.figure()
# # # #     ax = fig.add_subplot(111, projection='3d')
# # # #
# # # #     # Plot each shell separately based on observer-centered perspective
# # # #     for r in r_values:
# # # #         x, y, z = observerPerspectiveShell(r, theta, phi)
# # # #         ax.plot_surface(x, y, z, cmap='viridis', alpha=0.3)
# # # #
# # # #     ax.set_xlabel("X axis")
# # # #     ax.set_ylabel("Y axis")
# # # #     ax.set_zlabel("Z axis")
# # # #     plt.title("Shells from the Observer's Perspective")
# # # #     plt.show()
# # # #
# # # #
# # # # # Example usage with multiple shells
# # # # plotObserverShells(r_values=[0.5, 1, 1.5, 2])
