# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the volume accumulation functions for disk and shell methods
# def V_disk(r):
#     return np.pi * r**2
#
# def V_shell(r):
#     return 2 * np.pi * r
#
# # Create a range of radii to visualize the volume accumulation
# r_values = np.linspace(0, 5, 400)
#
# # Compute volumes for both methods
# V_disk_values = V_disk(r_values)
# V_shell_values = V_shell(r_values)
#
# # Create a plot to visualize when the volumes of disk and shell coincide
# plt.figure(figsize=(10, 6))
# plt.plot(r_values, V_disk_values, label="V_disk (Disk Volume Accumulation)", color='blue')
# plt.plot(r_values, V_shell_values, label="V_shell (Shell Volume Accumulation)", color='orange')
#
# # Add a title and labels
# plt.title('Volume Accumulation of Disk and Shell Methods')
# plt.xlabel('Radius (r)')
# plt.ylabel('Volume')
# plt.legend()
#
# # Highlight the points of coincidence
# plt.fill_between(r_values, V_disk_values, V_shell_values, where=np.abs(V_disk_values - V_shell_values) < 0.1,
#                  color='green', alpha=0.3, label="Coincidence Points")
#
# # Show the plot
# plt.grid(True)
# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define the progress for the disk and shell methods (normalized radius)
def V_disk(r):
    return np.pi * (1 - r**2)  # Disk progress (normalized)

def V_shell(r):
    return 4 * np.pi * r**2  # Shell progress (normalized)

# Create a range of normalized radii
r_values = np.linspace(0, 1, 400)

# Compute progress for both methods
V_disk_values = V_disk(r_values)
V_shell_values = V_shell(r_values)

# Create a plot to visualize progress bars
plt.figure(figsize=(10, 6))

# Plot the progress for the disk and shell methods
plt.plot(r_values, V_disk_values, label="Disk Method Progress", color='blue')
plt.plot(r_values, V_shell_values, label="Shell Method Progress", color='orange')

# Add a title and labels
plt.title('Coincidence Points in Volume Accumulation (Disk vs. Shell)')
plt.xlabel('Normalized Radius (0 to 1)')
plt.ylabel('Volume Contribution')
plt.axhline(y=0, color='green', linestyle='--', label="Coincidence Points")

# Highlight coincidence points
plt.fill_between(r_values, V_disk_values, V_shell_values, where=np.abs(V_disk_values - V_shell_values) < 0.05,
                 color='green', alpha=0.3, label="Coincidence Points")

# Show the plot with a grid and legend
plt.grid(True)
plt.legend()
plt.show()
