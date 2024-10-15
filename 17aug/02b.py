# Klein Bottle Parameters
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(0, 2 * np.pi, 100)
u_grid, v_grid = np.meshgrid(u_vals, v_vals)

# Klein Bottle Parametric Equations (Simplified for visualization)
x_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.cos(u_grid)
y_klein = (2 + np.cos(u_grid / 2) * np.sin(v_grid) - np.sin(u_grid / 2) * np.sin(2 * v_grid)) * np.sin(u_grid)
z_klein = np.sin(u_grid / 2) * np.sin(v_grid) + np.cos(u_grid / 2) * np.sin(2 * v_grid)

# Static projection in XY, XZ, YZ planes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].contourf(x_klein, y_klein, np.abs(x_klein)**2 + np.abs(y_klein)**2)
axs[0].set_title('XY Projection')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

axs[1].contourf(x_klein, z_klein, np.abs(x_klein)**2 + np.abs(z_klein)**2)
axs[1].set_title('XZ Projection')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')

axs[2].contourf(y_klein, z_klein, np.abs(y_klein)**2 + np.abs(z_klein)**2)
axs[2].set_title('YZ Projection')
axs[2].set_xlabel('Y')
axs[2].set_ylabel('Z')

plt.suptitle('Klein Bottle Projections')
plt.show()
