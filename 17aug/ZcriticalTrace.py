import numpy as np
from mpmath import zeta
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametrize the critical trace on the Klein bottle
u_critical = np.array([-np.pi/2, np.pi/2, 3*np.pi/2])
v_critical = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])

def klein_bottle_param(u, v, r=2):
    x = np.cos(u) * (r + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v))
    y = np.sin(u) * (r + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v))
    z = np.sin(u / 2) * np.sin(v) + np.cos(u / 2) * np.sin(2 * v)
    return x, y, z

# Evaluate the critical trace on the Klein bottle
klein_values = [klein_bottle_param(u, v) for u in u_critical for v in v_critical]

# Zeta function on the critical line (sigma = 1/2)
def zeta_critical_line(t_values):
    sigma = 0.5
    zeta_values = [zeta(sigma + 1j*t) for t in t_values]
    return zeta_values

# Check equality between Klein bottle values and zeta function values
def check_equality(klein_values, zeta_values):
    matches = []
    for i, (x_klein, y_klein, z_klein) in enumerate(klein_values):
        zeta_val = zeta_values[i % len(zeta_values)]
        # Prove equality by checking if the Klein bottle values match zeta function values
        if np.allclose([x_klein, y_klein], [zeta_val.real, zeta_val.imag], atol=1e-6):
            matches.append((i, (x_klein, y_klein, z_klein), zeta_val))
            print(f"Match at index {i}: Klein({x_klein}, {y_klein}, {z_klein}) == Zeta({zeta_val.real}, {zeta_val.imag})")
        else:
            print(f"No match at index {i}: Klein({x_klein}, {y_klein}, {z_klein}) != Zeta({zeta_val.real}, {zeta_val.imag})")
    return matches

# Define a range of t values corresponding to the critical line in the Zeta function
t_values = np.linspace(-10, 10, len(klein_values))

# Calculate Zeta function values on the critical line
zeta_values = zeta_critical_line(t_values)

# Check for matches
matches = check_equality(klein_values, zeta_values)

# Visualization
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot Klein bottle trace
for (x_klein, y_klein, z_klein) in klein_values:
    ax.scatter(x_klein, y_klein, z_klein, color='blue', s=50)

# Highlight matches
for i, (x_klein, y_klein, z_klein), zeta_val in matches:
    ax.scatter(x_klein, y_klein, z_klein, color='red', s=100, edgecolors='black')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Critical Trace on the Klein Bottle and Zeta Function Matches')

plt.show()
