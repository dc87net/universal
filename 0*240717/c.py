import numpy as np
import matplotlib.pyplot as plt

# Define the volume accumulation functions for disk and shell methods
def V_disk(r):
    return np.pi * r**2

def V_shell(r):
    return 2 * np.pi * r

# Normalize the radius range from 0 to 1
r_values = np.linspace(0, 1, 400)  # Now r goes from 0 to 1

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
plt.title('Normalized Progress of Volume Accumulation (Disk vs. Shell)')
plt.xlabel('Progress from 0 to 1 (where 1 is complete)')
plt.ylabel('Progress (%)')
plt.axhline(y=100, color='green', linestyle='--', label="100% Volume Accumulation")

# Highlight regions where the progress is equal
plt.fill_between(r_values, V_disk_progress, V_shell_progress, where=np.abs(V_disk_progress - V_shell_progress) < 1,
                 color='green', alpha=0.3, label="Coincidence Points")

# Show the plot with a grid and legend
plt.grid(True)
plt.legend()
plt.show()
