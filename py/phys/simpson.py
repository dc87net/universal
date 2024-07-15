import numpy as np
import matplotlib.pyplot as plt

# Define the parameter alpha
alpha = 1  # This can be adjusted based on the specific scenario

# Define the function R(t) involving alpha and beta
def R(t, alpha, beta):
    return np.exp(-alpha * (t + beta / (2 * alpha))**2)

# Define parameters for Simpson's Rule
a = 0
b = 10
n = 1000  # Number of subintervals (must be even)
h = (b - a) / n

# Apply Simpson's Rule
x = np.linspace(a, b, n+1)
beta = 1  # This can be adjusted based on the specific scenario
y = R(x, alpha, beta)

S = h/3 * (y[0] + 2 * sum(y[2:n-1:2]) + 4 * sum(y[1:n:2]) + y[n])

# Print the result
print(f"Simpson's Rule Approximation for integral of R(t) after completing the square: {S}")

# Plotting the function and the area under the curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b', label=f'R(t) = e^{{-\\alpha (t + \\beta / 2\\alpha)^2}}')
plt.fill_between(x, y, color='lightblue', alpha=0.5)
plt.title(f"Numerical Integration of R(t) with alpha = {alpha} and beta = {beta} using Simpson's Rule")
plt.xlabel('t')
plt.ylabel('R(t)')
plt.legend()
plt.show()