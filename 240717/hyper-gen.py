import numpy as np
from mpmath import mp, cosh, pi, gamma, mpc

# Set precision
mp.dps = 50


# Symbolic zeta function with hyperbolic trig functions
def zeta_symbolic(t, terms=1000):
    s = mpc(0.5, t)
    s_conjugate = mpc(0.5, -t)
    return (mp.power(2, mp.mpf(0.5) - 1j * t) * mp.power(pi, -(mp.mpf(0.5) + 1j * t)) * cosh(
        pi * (mp.mpf(0.5) + 1j * t) / 2) *
            gamma(mp.mpf(0.5) + 1j * t) * sum([1 / mp.power(n, s_conjugate) for n in range(1, terms)]))


# Parameters for data calculation
start_t = 0
end_t = 100
total_points = 10000
block_size = 1000  # Adjust block size as needed

# Calculate total blocks
total_blocks = total_points // block_size


# Function to save data to file
def append_data_to_file(filename, t_values, real_parts, imag_parts, amplitude, zeros):
    with open(filename, 'a') as f:
        for t, r, i, a in zip(t_values, real_parts, imag_parts, amplitude):
            f.write(f"{t}\t{r}\t{i}\t{a}\n")
        for zero in zeros:
            f.write(f"zero\t{zero[0]}\t{zero[1]}\n")


# Initialize the data file
data_filename = 'zeta_data.tsv'
with open(data_filename, 'w') as f:
    f.write("t_value\treal_part\timag_part\tamplitude\n")

# Block-wise calculation
for i in range(total_blocks):
    print(f"Calculating block {i + 1} of {total_blocks}... ", end='')

    t_values = []
    real_parts = []
    imag_parts = []
    amplitude = []
    zeros = []

    for j in range(block_size):
        t = start_t + (i * block_size + j) * ((end_t - start_t) / total_points)
        t_values.append(t)

        zeta_val = zeta_symbolic(t, terms=1000)
        real_part = float(zeta_val.real)
        imag_part = float(zeta_val.imag)
        amp = np.sqrt(real_part ** 2 + imag_part ** 2)

        real_parts.append(real_part)
        imag_parts.append(imag_part)
        amplitude.append(amp)

        epsilon = 1e-10  # Smaller threshold for higher precision
        if abs(real_part) < epsilon and abs(imag_part) < epsilon:
            zeros.append((0.5, t))

    append_data_to_file(data_filename, t_values, real_parts, imag_parts, amplitude, zeros)
    print(f"\t{i + 1} saved to {data_filename}")

print("All data blocks have been calculated and saved.")
