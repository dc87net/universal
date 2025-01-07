import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Parameters
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(0, 2 * np.pi, 100)

# Layered Onion Plot
fig_onion = plt.figure()
ax_onion = fig_onion.add_subplot(111, projection='3d')

# Set fixed axis limits
ax_onion.set_xlim([-3, 3])
ax_onion.set_ylim([-3, 3])
ax_onion.set_zlim([-3, 3])

# Generate multiple traces with varying parameters
for scale in np.linspace(0.5, 2.0, 10):  # Change scale to see layers
    x = scale * np.sin(u_vals) * np.cos(v_vals)
    y = scale * np.sin(u_vals) * np.sin(v_vals)
    z = scale * np.cos(u_vals)
    ax_onion.plot(x, y, z, alpha=0.6)  # Transparency for layering

plt.title("Layered Onion Plot")
plt.show()

# Animation of the trace evolution
fig_anim = plt.figure()
ax_anim = fig_anim.add_subplot(111, projection='3d')

# Fixed axis limits for the animation
ax_anim.set_xlim([-3, 3])
ax_anim.set_ylim([-3, 3])
ax_anim.set_zlim([-3, 3])

# Animation function
def animate(i):
    ax_anim.clear()
    u = u_vals * (i / 10.0)
    v = v_vals * (i / 10.0)
    x = np.sin(u) * np.cos(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(u)
    ax_anim.plot(x, y, z, color='b')

ani = animation.FuncAnimation(fig_anim, animate, frames=50, interval=100)

plt.show()
