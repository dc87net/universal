import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton
from mpmath import zeta

# Define the critical line
sigma = 0.5
t_values = np.linspace(0, 50, 1000)

# Define the zeta function along the critical line
def zeta_critical_line(t):
    s = complex(0.5, t)
    return zeta(s)

# Find zeros along the critical line using a root-finding algorithm
initial_guesses = np.arange(1, 50, 5)  # Initial guesses for the root finding
zeros = []

for guess in initial_guesses:
    try:
        zero = newton(lambda t: float(zeta_critical_line(t).real), guess)
        if zero not in zeros:
            zeros.append(zero)
    except RuntimeError:
        continue

# Plotting the results
plt.figure(figsize=(14, 7))
real_parts = [float(zeta_critical_line(t).real) for t in t_values]
imaginary_parts = [float(zeta_critical_line(t).imag) for t in t_values]

plt.plot(t_values, real_parts, label='Real Part')
plt.plot(t_values, imaginary_parts, label='Imaginary Part', linestyle='--')
plt.scatter(zeros, [0]*len(zeros), color='red', zorder=5, label='Zeros')
plt.title('Riemann Zeta Function along the Critical Line (Re(s) = 0.5)')
plt.xlabel('Imaginary part of s (t)')
plt.ylabel('Zeta(s)')
plt.legend()
plt.grid(True)
plt.show()

# Print the identified zeros
zeros