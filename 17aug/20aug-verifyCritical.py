import numpy as np

# Define the critical points
critical_angles_u = [np.pi / 2 + n * np.pi for n in range(-2, 3)]
critical_angles_v = [n * np.pi for n in range(-2, 3)]
critical_angles_z = [3 * np.pi / 2 + 2 * n * np.pi for n in range(-2, 3)]


# Example functions for x(u,v), y(u,v), z(u,v)
# You need to replace these with your actual function expressions
def x(u, v):
    return np.cos(u) * np.sin(v)


def y(u, v):
    return np.sin(u) * np.sin(v)


def z(u, v):
    return np.sin(2 * u) * np.sin(v) + np.cos(2 * u) * np.sin(2 * v)


# First derivatives (with respect to u and v)
def dx_du(u, v):
    return -np.sin(u) * np.sin(v)


def dx_dv(u, v):
    return np.cos(u) * np.cos(v)


def dy_du(u, v):
    return np.cos(u) * np.sin(v)


def dy_dv(u, v):
    return np.sin(u) * np.cos(v)


def dz_du(u, v):
    return 2 * np.cos(2 * u) * np.sin(v) - 2 * np.sin(2 * u) * np.sin(2 * v)


def dz_dv(u, v):
    return np.sin(2 * u) * np.cos(v) + 2 * np.cos(2 * u) * np.cos(2 * v)


# Evaluate the derivatives at the critical points
def check_critical_points():
    for u in critical_angles_u:
        for v in critical_angles_v:
            derivative_x_u = dx_du(u, v)
            derivative_x_v = dx_dv(u, v)
            derivative_y_u = dy_du(u, v)
            derivative_y_v = dy_dv(u, v)
            derivative_z_u = dz_du(u, v)
            derivative_z_v = dz_dv(u, v)

            print(f"u={u}, v={v}")
            print(f"dx/du={derivative_x_u}, dx/dv={derivative_x_v}")
            print(f"dy/du={derivative_y_u}, dy/dv={derivative_y_v}")
            print(f"dz/du={derivative_z_u}, dz/dv={derivative_z_v}")
            print("-----------")


check_critical_points()

# import numpy as np
# from mpmath import zeta, gamma, cos, pi, mp
#
# # Set precision
# mp.dps = 25
#
# # Critical angles derived from your summary
# critical_points = {
#     "x_critical_points": [np.pi / 2 + 2 * n * np.pi for n in range(-2, 3)],
#     "y_critical_points": [np.pi / 2 + 2 * n * np.pi for n in range(-2, 3)],
#     "z_critical_points": [3 * np.pi / 2 + 2 * n * np.pi for n in range(-2, 3)],
# }
#
#
# # Custom symbolic zeta function method
# def zeta_symbolic(t):
#     s = complex(0.5, t)
#     s_conjugate = complex(0.5, -t)
#     return (2 ** (0.5 - 1j * t) * pi ** (-(0.5 + 1j * t)) * cos(pi * (0.5 + 1j * t) / 2) *
#             gamma(0.5 + 1j * t) * zeta(s_conjugate))
#
#
# # Check each critical point
# results = {}
# for label, points in critical_points.items():
#     derivatives = []
#     for t in points:
#         epsilon = 1e-10  # small value for numerical differentiation
#         zeta_val_plus = zeta_symbolic(t + epsilon)
#         zeta_val_minus = zeta_symbolic(t - epsilon)
#         derivative = (zeta_val_plus - zeta_val_minus) / (2 * epsilon)
#         derivatives.append(derivative)
#
#     results[label] = derivatives
#
# # Output the results
# for label, derivatives in results.items():
#     print(f"\nFirst Derivatives at Critical Points for {label}:")
#     for i, derivative in enumerate(derivatives):
#         print(f"  Critical Point {i + 1}: {derivative}")
#
# # Check if the derivative is near zero
# verified_angles = {}
# for label, derivatives in results.items():
#     verified_angles[label] = [derivative for derivative in derivatives if np.isclose(derivative, 0, atol=1e-8)]
#
# for label, angles in verified_angles.items():
#     print(f"\nVerified Critical Points (where the derivative is near zero) for {label}:")
#     for angle in angles:
#         print(f"  {angle}")
