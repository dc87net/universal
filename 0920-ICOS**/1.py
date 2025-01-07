import sympy as sp

# Define variables
t, A, r_0, omega = sp.symbols('t A r_0 omega')
theta, phi = sp.symbols('theta phi')
r_t = r_0 + A * sp.sin(omega * t)  # Radial function

# Parametric equations for the icosahedron with variable radius
x_t = r_t * sp.cos(theta) * sp.sin(phi)
y_t = r_t * sp.sin(theta) * sp.sin(phi)
z_t = r_t * sp.cos(phi)

# Placeholder for shadow areas as functions of time (to be derived based on projections)
A_xy = sp.Abs(x_t * y_t)  # Simplified projection area for now
A_xz = sp.Abs(x_t * z_t)
A_yz = sp.Abs(y_t * z_t)

# First derivatives to find critical points
dA_xy_dt = sp.diff(A_xy, t)
dA_xz_dt = sp.diff(A_xz, t)
dA_yz_dt = sp.diff(A_yz, t)

# Critical points (solving derivatives equal to zero)
critical_points_xy = sp.solve(dA_xy_dt, t)
critical_points_xz = sp.solve(dA_xz_dt, t)
critical_points_yz = sp.solve(dA_yz_dt, t)

# Compute the maximum areas for each projection
A_xy_max = sp.simplify(A_xy.subs(t, critical_points_xy[0]))
A_xz_max = sp.simplify(A_xz.subs(t, critical_points_xz[0]))
A_yz_max = sp.simplify(A_yz.subs(t, critical_points_yz[0]))

# Normalized areas
A_xy_norm = A_xy / A_xy_max
A_xz_norm = A_xz / A_xz_max
A_yz_norm = A_yz / A_yz_max

# Normalized shadow volume
V_shadow_norm = A_xy_norm * A_xz_norm * A_yz_norm

{
    "A_xy_max": A_xy_max,
    "A_xz_max": A_xz_max,
    "A_yz_max": A_yz_max,
    "V_shadow_norm": V_shadow_norm
}
