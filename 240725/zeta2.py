import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
import pandas as pd

# Define the critical line values for t
t_values = np.linspace(1, 10, 10)

# Compute zeta values along the critical line
zeta_values = [zeta(0.5 + 1j*t) for t in t_values]

# Extract real and imaginary parts
real_parts = [z.real for z in zeta_values]
imaginary_parts = [z.imag for z in zeta_values]

# Create a DataFrame to display the values
df = pd.DataFrame({
    't': t_values,
    'Re(ζ(0.5 + it))': real_parts,
    'Im(ζ(0.5 + it))': imaginary_parts
})

# Display the DataFrame
print(df)

# Define the critical line values for a finer range of t
t_values_fine = np.linspace(0, 50, 1000)

# Compute zeta values along the critical line
zeta_values_fine = [zeta(0.5 + 1j*t) for t in t_values_fine]

# Extract real and imaginary parts
real_parts_fine = [z.real for z in zeta_values_fine]
imaginary_parts_fine = [z.imag for z in zeta_values_fine]

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(t_values_fine, real_parts_fine, label='Real Part')
plt.plot(t_values_fine, imaginary_parts_fine, label='Imaginary Part', linestyle='--')
plt.scatter(t_values, real_parts, color='red', zorder=5, label='Computed Real Parts')
plt.scatter(t_values, imaginary_parts, color='blue', zorder=5, label='Computed Imaginary Parts')
plt.title('Riemann Zeta Function along the Critical Line (Re(s) = 0.5)')
plt.xlabel('Imaginary part of s (t)')
plt.ylabel('Zeta(s)')
plt.legend()
plt.grid(True)
plt.show()
