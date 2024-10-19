import numpy as np
import matplotlib.pyplot as plt

# Define the volume accumulation functions for disk and shell methods
def V_disk(r):
    return np.pi * r**2

def V_shell(r):
    return 2 * np.pi * r

# Create a range of radii to visualize the volume accumulation
r_values = np.linspace(0, 5, 400)

# Compute volumes for both methods
V_disk_values = V_disk(r_values)
V_shell_values = V_shell(r_values)

# Compute the ratio between V_disk and V_shell
ratio_values = V_disk_values / V_shell_values

# Create a plot to visualize the normalized progress (the ratio)
plt.figure(figsize=(10, 6))
plt.plot(r_values, ratio_values, label="V_disk / V_shell (Normalized Progress)", color='purple')

# Add a title and labels
plt.title('Normalized Progress (Ratio of Disk to Shell Volume)')
plt.xlabel('Radius (r)')
plt.ylabel('Ratio (V_disk / V_shell)')
plt.axhline(y=1, color='green', linestyle='--', label="Ratio = 1 (Coincidence)")

# Highlight regions where the ratio is near 1
plt.fill_between(r_values, ratio_values, 1, where=np.abs(ratio_values - 1) < 0.05, color='green', alpha=0.3)

# Show the plot with a grid and legend
plt.grid(True)
plt.legend()
plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Define the volume accumulation functions for disk and shell methods
def V_disk(r):
    return np.pi * r**2

def V_shell(r):
    return 2 * np.pi * r

# Create a range of radii to visualize the volume accumulation
r_values = np.linspace(0, 5, 400)

# Compute volumes for both methods
V_disk_values = V_disk(r_values)
V_shell_values = V_shell(r_values)

# Normalize the volumes so that the final volume is 100%
V_disk_progress = V_disk_values / np.max(V_disk_values) * 100  # Progress percentage for the disk
V_shell_progress = V_shell_values / np.max(V_shell_values) * 100  # Progress percentage for the shell

# Create a plot to visualize progress bars
plt.figure(figsize=(10, 6))

# Plot the progress for the disk and shell methods
plt.plot(r_values, V_disk_progress, label="Disk Method Progress", color='blue')
plt.plot(r_values, V_shell_progress, label="Shell Method Progress", color='orange')

# Add a title and labels
plt.title('Progress of Volume Accumulation (Disk vs. Shell)')
plt.xlabel('Radius (r)')
plt.ylabel('Progress (%)')
plt.axhline(y=100, color='green', linestyle='--', label="100% Volume Accumulation")

# Highlight regions where the progress is equal
plt.fill_between(r_values, V_disk_progress, V_shell_progress, where=np.abs(V_disk_progress - V_shell_progress) < 1,
                 color='green', alpha=0.3, label="Coincidence Points")

# Show the plot with a grid and legend
plt.grid(True)
plt.legend()
plt.show()
