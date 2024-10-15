import numpy as np

# Given projected zeroes from your recent output
projected_zeros = np.array([
    9.84996999e+01, 9.66070558e+01, 9.10018567e+01, 8.18995073e+01,
    6.96498058e+01, 5.47235012e+01, 3.76942033e+01, 1.92163382e+01,
    6.03136711e-15, -1.92163382e+01, -3.76942033e+01, -5.47235012e+01,
    -6.96498058e+01, -8.18995073e+01, -9.10018567e+01, -9.66070558e+01,
    -9.84996999e+01, -9.66070558e+01, -9.10018567e+01, -8.18995073e+01,
    -6.96498058e+01, -5.47235012e+01, -3.76942033e+01, -1.92163382e+01,
    -1.80941013e-14, 1.92163382e+01, 3.76942033e+01, 5.47235012e+01,
    6.96498058e+01, 8.18995073e+01, 9.10018567e+01, 9.66070558e+01
])

# Value we want to check (around -69.64)
value_to_standardize = -69.64

# Step 1: Calculate the mean and standard deviation of the projected zeros
mean_val = np.mean(projected_zeros)
stddev_val = np.std(projected_zeros)

# Step 2: Standardize the specific value (-69.64)
standardized_value = (value_to_standardize - mean_val) / stddev_val

# Step 3: Output the result
print(f"Mean of projected zeros: {mean_val}")
print(f"Standard deviation of projected zeros: {stddev_val}")
print(f"Standardized value for -69.64: {standardized_value}")

# Step 4: Compare with Euler's number e
euler_number = np.e  # Euler's number
print(f"Euler's number (e): {euler_number}")

# Check how close the standardized value is to e
difference_from_e = np.abs(standardized_value - euler_number)
print(f"Difference from Euler's number: {difference_from_e}")



import matplotlib.pyplot as plt

# Standardize all projected zeroes
standardized_zeros = (projected_zeros - mean_val) / stddev_val
print(f"std zeros: {standardized_zeros}")

# Plot the standardized values
plt.figure(figsize=(10, 6))
plt.plot(standardized_zeros, 'x', label='Standardized Projected Zeros')
plt.axhline(y=-1, color='r', linestyle='--', label='-1 Reference Line')
plt.axhline(y=0, color='g', linestyle='--', label='0 Reference Line')
plt.title("Standardized Projected Zeros (Psi values)")
plt.xlabel("Index")
plt.ylabel("Standardized Value")
plt.grid(True)
plt.legend()

# Show plot
plt.show()

# Output standardized values for inspection
print(f"Standardized Projected Zeros: {standardized_zeros}")
