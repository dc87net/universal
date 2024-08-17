import numpy as np
import matplotlib.pyplot as plt
from sympy import primepi, li
from mpmath import zeta
import pandas as pd
import ace_tools


# Define the range for x
x_values = np.linspace(2, 100, 500)

# Compute the prime counting function π(x)
pi_values = [primepi(x) for x in x_values]

# Compute the logarithmic integral Li(x)
li_values = [li(x) for x in x_values]

# Define the critical line values for t
t_values = np.linspace(1, 10, 10)

# Compute zeta values along the critical line
zeta_values = [zeta(0.5 + 1j*t) for t in t_values]

# Extract real and imaginary parts
real_parts = [z.real for z in zeta_values]
imaginary_parts = [z.imag for z in zeta_values]

# Create a DataFrame to display the zeta values
df = pd.DataFrame({
    't': t_values,
    'Re(ζ(0.5 + it))': real_parts,
    'Im(ζ(0.5 + it))': imaginary_parts
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Riemann Zeta Function Values along Critical Line", dataframe=df)

# Plotting the results
plt.figure(figsize=(14, 7))

# Prime counting function and logarithmic integral
plt.subplot(2, 1, 1)
plt.plot(x_values, pi_values, label='Prime Counting Function π(x)', color='blue')
plt.plot(x_values, li_values, label='Logarithmic Integral Li(x)', linestyle='--', color='red')
plt.title('Prime Counting Function π(x) and Logarithmic Integral Li(x)')
plt.xlabel('x')
plt.ylabel('Count')
plt.legend()
plt.grid(True)

# Zeta function values along the critical line
plt.subplot(2, 1, 2)
t_values_fine = np.linspace(0, 50, 1000)
zeta_values_fine = [zeta(0.5 + 1j*t) for t in t_values_fine]
real_parts_fine = [z.real for z in zeta_values_fine]
imaginary_parts_fine = [z.imag for z in zeta_values_fine]

plt.plot(t_values_fine, real_parts_fine, label='Real Part')
plt.plot(t_values_fine, imaginary_parts_fine, label='Imaginary Part', linestyle='--')
plt.scatter(t_values, real_parts, color='red', zorder=5, label='Computed Real Parts')
plt.scatter(t_values, imaginary_parts, color='blue', zorder=5, label='Computed Imaginary Parts')
plt.title('Riemann Zeta Function along the Critical Line (Re(s) = 0.5)')
plt.xlabel('Imaginary part of s (t)')
plt.ylabel('Zeta(s)')
plt.legend()
plt.grid(True)

# Show plots
plt.tight_layout()
plt.show()